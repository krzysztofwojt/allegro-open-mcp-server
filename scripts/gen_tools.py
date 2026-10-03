#!/usr/bin/env python3
"""Generate one MCP tool module per OpenAPI tag.

Reads the cached swagger.yaml and emits a single Python module per tag at
``src/allegro_mcp/tools/<module>.py``. Each operation in the spec becomes
one ``@mcp.tool``-decorated function with:

* a snake_case name derived from ``operationId``,
* keyword-only arguments for path, query and header parameters, with
  official input schemas, requiredness and JSON or base64 request bodies,
* a docstring built from the operation's summary / description,
* JSON or base64 response envelopes (we don't bind to one of
  the 1 200+ generated Pydantic classes because the OpenAPI components map
  inconsistently to operation responses; raw dicts let callers introspect
  cleanly while keeping the generator simple),
* decorators: ``@mcp.tool`` + ``@allegro_call``; write methods (POST,
  PUT, PATCH, DELETE) also stack ``@requires_writes_enabled``.

Run via ``make gen-tools``. Output is committed and reviewed in PRs.
"""

from __future__ import annotations

import hashlib
import json
import re
import sys
import textwrap
from collections import defaultdict
from pathlib import Path
from typing import Any

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
SPEC_PATH = REPO_ROOT / "specs" / "swagger.yaml"
TOOLS_DIR = REPO_ROOT / "src" / "allegro_mcp" / "tools"

# Methods that mutate state — annotated with @requires_writes_enabled so the
# tool stays visible but refuses to fire unless the operator opted in via
# ALLEGRO_ENABLE_WRITES=true.
_WRITE_METHODS = {"post", "put", "patch", "delete"}

# Tools that don't get the writes-enabled gate even though their HTTP method
# is in _WRITE_METHODS — typically because they only fetch a representation
# (e.g. POST for fee calculation) without persisting state.
_READ_OPERATION_OVERRIDES: frozenset[str] = frozenset(
    {
        # POST endpoints that read but don't mutate the seller's account.
        "calculateFeePreview",
        "calculateFeesUsingPOST",
        "getShipmentLabels",
        "getShipmentProtocol",
        "parseIngredients",
    }
)


_USING_METHOD_SUFFIX = re.compile(r"_using_(?:get|post|put|patch|delete)$")

# MCP imposes a 64-char limit on tool names. The renderer in FastMCP / the
# Claude Desktop client both reject longer names. We enforce the cap here so
# CI-time generation never produces an unbootable server.
_MCP_TOOL_NAME_MAX = 64


def _camel_to_snake(name: str) -> str:
    """Turn ``getOfferEvents`` into ``get_offer_events``.

    Also strips the redundant ``_using_<method>`` suffix Allegro adds to many
    operationIds (e.g. ``...UsingGET``). The HTTP method is already encoded
    in the tool's wire call, so carrying it in the name is noise — and a
    handful of operationIds blow past MCP's 64-char tool-name cap with the
    suffix attached.
    """
    s1 = re.sub(r"(.)([A-Z][a-z]+)", r"\1_\2", name)
    s2 = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", s1)
    snake = s2.lower().replace("__", "_")
    snake = _USING_METHOD_SUFFIX.sub("", snake)
    if len(snake) > _MCP_TOOL_NAME_MAX:
        # A stable digest avoids collisions between names sharing a long prefix.
        digest = hashlib.sha256(name.encode()).hexdigest()[:8]
        snake = snake[: _MCP_TOOL_NAME_MAX - 9].rstrip("_") + "_" + digest
    return snake


def _slugify_tag(tag: str) -> str:
    """Turn ``"User's offer information"`` into ``user_offer_information``."""
    cleaned = re.sub(r"[^A-Za-z0-9]+", "_", tag).strip("_").lower()
    if cleaned and cleaned[0].isdigit():
        cleaned = f"_{cleaned}"
    # Avoid stomping on Python keywords / fastmcp internals.
    if cleaned in {"auth", "auth_module"}:
        cleaned = f"{cleaned}_module"
    return cleaned


def _python_type_for(schema: dict[str, Any]) -> str:
    """Preserve parameter primitive and collection types."""
    kind = schema.get("type")
    if kind == "array":
        return f"list[{_python_type_for(schema.get('items', {}))}]"
    return {"integer": "int", "number": "float", "boolean": "bool", "object": "dict[str, Any]"}.get(
        kind, "str"
    )


_PYTHON_KEYWORDS: frozenset[str] = frozenset(
    {
        "False",
        "None",
        "True",
        "and",
        "as",
        "assert",
        "async",
        "await",
        "break",
        "class",
        "continue",
        "def",
        "del",
        "elif",
        "else",
        "except",
        "finally",
        "for",
        "from",
        "global",
        "if",
        "import",
        "in",
        "is",
        "lambda",
        "nonlocal",
        "not",
        "or",
        "pass",
        "raise",
        "return",
        "try",
        "while",
        "with",
        "yield",
        "match",
        "case",
        "type",
    }
)


def _safe_arg_name(name: str) -> str:
    """Convert ``seller.id`` (a dotted query-param name) into ``seller_id``.

    Allegro's spec uses dotted query params (``seller.id``, ``offer.id``)
    and a few keyword-clashing names (``from``, ``type``). Tools accept
    Python identifiers; the generator maps the identifier back to the
    original dotted key when issuing the request, and trailing-underscores
    keyword clashes (``from`` → ``from_``).
    """
    safe = re.sub(r"[^A-Za-z0-9_]", "_", name)
    if safe in _PYTHON_KEYWORDS or not safe or safe[0].isdigit():
        safe = f"{safe}_" if safe in _PYTHON_KEYWORDS else f"param_{safe}"
    return safe


def _docstring(op: dict[str, Any], method: str, path: str) -> str:
    summary = (op.get("summary") or "").strip()
    description = (op.get("description") or "").strip()
    pieces: list[str] = []
    if summary:
        pieces.append(summary)
    if description and description != summary:
        # Keep the first 1500 chars of description to avoid huge docstrings.
        pieces.append(textwrap.shorten(description, width=1500, placeholder="…"))
    pieces.append(f"\nHTTP: ``{method.upper()} {path}``")
    return "\n\n".join(pieces).rstrip()


def _format_docstring(text: str) -> str:
    """Format a docstring body for embedding in a Python source file.

    Allegro descriptions contain ad-hoc backslash sequences (``\\-``,
    ``\\n``) in their HTML markup; embedding the raw text in a regular
    string literal would emit ``SyntaxWarning: invalid escape sequence``
    for each one. The generator collapses backslashes to forward slashes
    so the resulting docstring is just text — no escape interpretation
    needed.
    """
    if not text:
        return '"""Tool generated from the Allegro OpenAPI spec."""'
    # Drop backslashes outright; they're never load-bearing in the
    # human-readable description text.
    cleaned = text.replace("\\", "")
    body = textwrap.indent(cleaned, "    ").lstrip()
    return f'"""{body}\n    """'


def _parameters(op: dict[str, Any], path_item: dict[str, Any]) -> list[dict[str, Any]]:
    """Operation-level parameters override matching path-level parameters."""
    merged = {}
    for source in (path_item.get("parameters", []), op.get("parameters", [])):
        for param in source:
            merged[(param["in"], param["name"])] = param
    return list(merged.values())


def _build_function(
    *, operation_id: str, method: str, path: str, op: dict[str, Any], path_item: dict[str, Any]
) -> str:
    name = _camel_to_snake(operation_id)
    docs = _docstring(op, method, path)
    if op.get("deprecated"):
        docs += "\n\nDEPRECATED by Allegro; prefer the documented replacement."
    params = _parameters(op, path_item)
    args = []
    mapping = []
    identifiers = set()
    for param in params:
        identifier = _safe_arg_name(param["name"])
        if identifier in identifiers:
            identifier = param["in"] + "_" + identifier
        identifiers.add(identifier)
        required = param.get("required", False) or param["in"] == "path"
        annotation = _python_type_for(param.get("schema", {}))
        if not required:
            annotation += " | None"
        key = param["in"] + ":" + param["name"]
        args.append(
            f"{identifier}: Annotated[{annotation}, Field(json_schema_extra=input_schema({operation_id!r}, {key!r}, {identifier!r}))]"
            + ("" if required else " = None")
        )
        mapping.append(f"{key!r}: {identifier}")
    content = op.get("requestBody", {}).get("content", {})
    if content:
        json_types = [t for t in content if "json" in t]
        if json_types:
            required = op["requestBody"].get("required", False)
            annotation = "dict[str, Any]" + ("" if required else " | None")
            args.append(
                f'body: Annotated[{annotation}, Field(json_schema_extra=input_schema({operation_id!r}, "body", "body"))]'
                + ("" if required else " = None")
            )
            mapping.append("'body': body")
        else:
            args.append("content_base64: str")
            args.append(f"content_type: str = {next(iter(content))!r}")
            mapping.extend(["'content_base64': content_base64", "'content_type': content_type"])
    decorators = ["@mcp.tool", "@allegro_call"]
    if method in _WRITE_METHODS and operation_id not in _READ_OPERATION_OVERRIDES:
        decorators.append("@requires_writes_enabled")
    signature = "*, " + ", ".join(args) if args else ""
    return (
        "\n".join(decorators)
        + f"\ndef {name}({signature}) -> Any | ErrorResponse:\n"
        + "    "
        + _format_docstring(docs)
        + "\n"
        + f"    return call_operation({operation_id!r}, {{{', '.join(mapping)}}})\n"
    )


_MODULE_HEADER = '''# ruff: noqa
"""Generated MCP tools — DO NOT EDIT.

Run ``make gen-tools`` to regenerate from the cached OpenAPI spec.
Tag: {tag}
"""

from __future__ import annotations

from typing import Annotated, Any

from pydantic import Field

from ..errors import ErrorResponse
from ._decorators import requires_writes_enabled
from ._runtime import allegro_call, mcp
from ._request import call_operation, input_schema


'''


def _emit_module(tag: str, operations: list[dict[str, Any]]) -> str:
    parts = [_MODULE_HEADER.format(tag=tag)]
    for entry in operations:
        parts.append(
            _build_function(
                operation_id=entry["operationId"],
                method=entry["method"],
                path=entry["path"],
                op=entry["op"],
                path_item=entry["path_item"],
            )
        )
        parts.append("\n")
    return "".join(parts)


def main() -> int:
    spec = yaml.safe_load(SPEC_PATH.read_text())
    operations: dict[str, list[dict[str, Any]]] = defaultdict(list)
    seen_ids: set[str] = set()
    names: set[str] = {"auth_status", "auth_login_device", "auth_revoke"}
    contract: dict[str, Any] = {"schemas": spec["components"]["schemas"], "operations": {}}

    for path, path_item in spec.get("paths", {}).items():
        if not isinstance(path_item, dict):
            continue
        for method, op in path_item.items():
            if method not in {"get", "post", "put", "patch", "delete"}:
                continue
            if not isinstance(op, dict):
                continue
            operation_id = (
                op.get("operationId") or f"{method}_{re.sub(r'[^a-zA-Z0-9]+', '_', path)}"
            )
            tag = (op.get("tags") or ["misc"])[0]
            module_name = _slugify_tag(tag)
            if operation_id in seen_ids:
                # OpenAPI sometimes has duplicates; suffix to keep names unique.
                operation_id = f"{operation_id}_{method}"
            seen_ids.add(operation_id)
            name = _camel_to_snake(operation_id)
            if name in names:
                raise ValueError(f"Duplicate MCP tool name: {name}")
            names.add(name)
            contract["operations"][operation_id] = {
                "method": method.upper(),
                "path": path,
                "parameters": _parameters(op, path_item),
                "requestBody": op.get("requestBody", {}),
                "responses": op["responses"],
                "tool": name,
                "deprecated": op.get("deprecated", False),
                "tag": tag,
            }
            operations[module_name].append(
                {
                    "operationId": operation_id,
                    "method": method,
                    "path": path,
                    "op": op,
                    "path_item": path_item,
                    "tag": tag,
                }
            )

    # Wipe any previously-generated tool modules but keep the hand-written
    # ones (auth.py, _runtime.py, _decorators.py, __init__.py).
    keep = {"auth.py", "__init__.py"}
    (TOOLS_DIR / "_contract.json").write_text(
        json.dumps(contract, ensure_ascii=False, indent=2, default=str) + "\n"
    )
    for existing in TOOLS_DIR.glob("*.py"):
        if existing.name not in keep and not existing.name.startswith("_"):
            existing.unlink()

    written: list[str] = []
    for module, ops in sorted(operations.items()):
        if not module:
            continue
        out = TOOLS_DIR / f"{module}.py"
        out.write_text(_emit_module(ops[0]["tag"], ops))
        written.append(module)

    # Update tools/__init__.py with side-effect imports.
    init = TOOLS_DIR / "__init__.py"
    init_lines = [
        '"""MCP tool registry.',
        "",
        "Importing this package side-effect-registers every ``@mcp.tool`` against",
        "the shared ``mcp`` instance in :mod:`allegro_mcp.tools._runtime`.",
        '"""',
        "",
        "from __future__ import annotations",
        "",
        "# Hand-written.",
        "from . import auth as _auth  # noqa: F401",
        "",
        "# Generated by ``make gen-tools`` from the OpenAPI spec.",
    ]
    init_lines.extend(
        f"from . import {module} as _{module}  # noqa: F401" for module in sorted(written)
    )
    init.write_text("\n".join(init_lines) + "\n")

    print(
        f"✓ wrote {len(written)} tool modules covering {sum(len(v) for v in operations.values())} operations"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
