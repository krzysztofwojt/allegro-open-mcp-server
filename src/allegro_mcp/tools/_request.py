"""OpenAPI input schemas and validated request dispatch for generated tools."""

from __future__ import annotations

import base64
import binascii
import json
from functools import cache
from pathlib import Path
from typing import Any
from urllib.parse import quote

from jsonschema import Draft4Validator, FormatChecker

from allegro_client.errors import AllegroError

from ._runtime import get_client

_CONTRACT = json.loads(Path(__file__).with_name("_contract.json").read_text())


def _convert(value: Any) -> Any:
    """Convert OpenAPI 3.0 schemas into Draft 4 JSON Schema."""
    if isinstance(value, list):
        return [_convert(item) for item in value]
    if not isinstance(value, dict):
        return value
    result = {key: _convert(item) for key, item in value.items() if key != "nullable"}
    if "$ref" in result:
        result["$ref"] = result["$ref"].replace("#/components/schemas/", "#/definitions/")
    if "properties" in result and "required" in result:
        result["required"] = [
            key
            for key in result["required"]
            if not result["properties"].get(key, {}).get("readOnly")
        ]
    if value.get("nullable"):
        return {"anyOf": [result, {"type": "null"}]}
    return result


@cache
def _schema(operation_id: str, key: str) -> dict[str, Any]:
    op = _CONTRACT["operations"][operation_id]
    if key == "body" or key.startswith("body:"):
        content = op["requestBody"]["content"]
        schema = next(v["schema"] for k, v in content.items() if "json" in k)
        if key.startswith("body:"):
            if "$ref" in schema:
                schema = _CONTRACT["schemas"][schema["$ref"].split("/")[-1]]
            schema = schema["properties"][key.split(":", 1)[1]]
    else:
        location, name = key.split(":", 1)
        param = next(p for p in op["parameters"] if p["in"] == location and p["name"] == name)
        schema = dict(param.get("schema", {}))
        if param.get("description"):
            schema.setdefault("description", param["description"])
    root = _convert(schema)
    definitions: dict[str, Any] = {}

    def collect(value: Any) -> None:
        if isinstance(value, dict):
            ref = value.get("$ref", "")
            if ref.startswith("#/definitions/"):
                name = ref.removeprefix("#/definitions/")
                if name not in definitions:
                    definitions[name] = _convert(_CONTRACT["schemas"][name])
                    collect(definitions[name])
            for item in value.values():
                collect(item)
        elif isinstance(value, list):
            for item in value:
                collect(item)

    collect(root)
    if definitions:
        root["definitions"] = definitions
    Draft4Validator.check_schema(root)
    return root  # type: ignore[no-any-return]


def input_schema(operation_id: str, key: str, argument: str) -> dict[str, Any]:
    """Embed a self-contained schema in the MCP parameter object's property.

    Inline referenced input models so Pydantic and MCP consumers can expose
    their constraints without references to external OpenAPI components.
    Recursive inputs fail explicitly instead of silently losing validation.
    """
    schema = _schema(operation_id, key)

    def inline(value: Any, stack: tuple[str, ...] = ()) -> Any:
        if isinstance(value, dict):
            if "$ref" in value:
                name = value["$ref"].removeprefix("#/definitions/")
                if name in stack:
                    raise ValueError(f"Recursive input schema requires explicit support: {name}")
                return inline(schema["definitions"][name], (*stack, name))
            return {k: inline(v, stack) for k, v in value.items() if k != "definitions"}
        if isinstance(value, list):
            return [inline(v, stack) for v in value]
        return value

    return inline(schema)  # type: ignore[no-any-return]


@cache
def _validator(operation_id: str, key: str) -> Draft4Validator:
    return Draft4Validator(_schema(operation_id, key), format_checker=FormatChecker())


def call_operation(operation_id: str, arguments: dict[str, Any]) -> Any:
    """Validate before I/O, preserve wire names, media types and binary data."""
    op = _CONTRACT["operations"][operation_id]
    path = op["path"]
    query = {}
    headers = {}
    for param in op["parameters"]:
        key = param["in"] + ":" + param["name"]
        value = arguments.get(key)
        if value is None:
            if param.get("required") or param["in"] == "path":
                raise AllegroError("INVALID_INPUT", f"Missing required parameter: {key}")
            continue
        _validate(operation_id, key, value)
        location = param["in"]
        if location == "path":
            path = path.replace("{" + param["name"] + "}", quote(str(value), safe=""))
        elif location == "query":
            if isinstance(value, list) and not param.get("explode", True):
                separator = {"spaceDelimited": " ", "pipeDelimited": "|"}.get(
                    param.get("style"), ","
                )
                value = separator.join(str(v) for v in value)
            query[param["name"]] = value
        elif location == "header":
            headers[param["name"]] = str(value)
        else:
            raise AllegroError("INVALID_INPUT", f"Unsupported parameter location: {location}")
    content = op["requestBody"].get("content", {})
    body = arguments.get("body")
    flat_body = {
        key.removeprefix("body:"): value
        for key, value in arguments.items()
        if key.startswith("body:") and value is not None
    }
    encoded = arguments.get("content_base64")
    alias = arguments.get("body_base64")
    if encoded is not None and alias is not None:
        raise AllegroError("INVALID_INPUT", "Provide only one base64 upload argument")
    encoded = encoded if encoded is not None else alias
    if sum((body is not None, bool(flat_body), encoded is not None)) > 1:
        raise AllegroError("INVALID_INPUT", "Provide exactly one request payload")
    if flat_body:
        body = flat_body
    raw_content = None
    if content:
        json_types = [kind for kind in content if "json" in kind]
        if encoded is not None:
            kind = arguments.get("content_type")
            if not isinstance(kind, str) or kind not in content or "json" in kind:
                raise AllegroError("INVALID_INPUT", "Unsupported upload content type")
            try:
                raw_content = base64.b64decode(encoded, validate=True)
            except (binascii.Error, ValueError, TypeError) as exc:
                raise AllegroError("INVALID_INPUT", "Invalid base64 upload") from exc
            if not raw_content:
                raise AllegroError("INVALID_INPUT", "Empty binary upload")
            headers["Content-Type"] = str(kind)
        elif json_types:
            if body is None and op["requestBody"].get("required"):
                raise AllegroError("INVALID_INPUT", "Missing required request body")
            if body is not None:
                _validate(operation_id, "body", body)
                headers["Content-Type"] = json_types[0]
        else:
            if op["requestBody"].get("required"):
                raise AllegroError("INVALID_INPUT", "Missing required binary request body")
    success_types = [
        kind
        for status, response in op["responses"].items()
        if status.startswith("2")
        for kind in response.get("content", {})
    ]
    if success_types and not any(key.lower() == "accept" for key in headers):
        headers["Accept"] = next(
            (t for t in success_types if "json" in t), success_types[0]
        ).replace("v1 +json", "v1+json")
    servers = op.get("servers", [])
    upload = bool(servers)
    if upload and servers[0]["url"] != "https://upload.{environment}":
        raise AllegroError("INVALID_INPUT", "Unsupported OpenAPI operation server")
    return get_client().request_json(
        op["method"],
        path,
        json=body,
        params=query,
        headers=headers,
        content=raw_content,
        allow_binary=any("json" not in kind for kind in success_types),
        upload=upload,
    )


def _validate(operation_id: str, key: str, value: Any) -> None:
    error = next(_validator(operation_id, key).iter_errors(value), None)
    if error is not None:
        # Never echo rejected values: request bodies may contain customer data.
        location = ".".join(str(part) for part in error.absolute_path)
        raise AllegroError(
            "INVALID_INPUT", f"Invalid {key} at {location or '<root>'}: {error.validator}"
        )
