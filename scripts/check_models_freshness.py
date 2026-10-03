#!/usr/bin/env python3
"""Detect drift between the upstream Allegro OpenAPI spec and the codegen banner.

Run via ``make check-models-freshness``. Compares the SHA-256 of the live
pinned spec and live spec at https://developer.allegro.pl/swagger.yaml against the checksum line
written into ``src/allegro_client/models/_generated/__init__.py`` by
``scripts.gen_models``. Exits 0 only when both match; drift, missing banners
and fetch failures fail the check. Use ``--force`` with the model generator
when deliberately updating the pinned spec.
"""

from __future__ import annotations

import hashlib
import re
import sys
import urllib.request
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
GENERATED_INIT = REPO_ROOT / "src" / "allegro_client" / "models" / "_generated" / "__init__.py"
SPEC_URL = "https://developer.allegro.pl/swagger.yaml"
BANNER_RE = re.compile(r"Spec checksum: sha256:([0-9a-f]{64})")


def main() -> int:
    init_text = GENERATED_INIT.read_text()
    match = BANNER_RE.search(init_text)
    if match is None:
        print(
            f"ERROR: no spec-checksum banner in {GENERATED_INIT.relative_to(REPO_ROOT)};"
            " run `make gen-models`.",
            file=sys.stderr,
        )
        return 1
    cached_digest = match.group(1)

    pinned = REPO_ROOT / "specs" / "swagger.yaml"
    if hashlib.sha256(pinned.read_bytes()).hexdigest() != cached_digest:
        print("ERROR: generated models do not match pinned spec", file=sys.stderr)
        return 1

    print(f"→ fetching {SPEC_URL}")
    with urllib.request.urlopen(SPEC_URL) as resp:
        upstream = resp.read()
    upstream_digest = hashlib.sha256(upstream).hexdigest()

    if cached_digest == upstream_digest:
        print(f"✓ in sync ({cached_digest[:12]}…)")
        return 0

    print(
        f"⚠ spec drift detected:\n"
        f"  cached:   {cached_digest}\n"
        f"  upstream: {upstream_digest}\n"
        f"  → run `uv run python scripts/gen_models.py --force` and `make gen-tools`, then review the diff."
    )
    return 1


if __name__ == "__main__":
    sys.exit(main())
