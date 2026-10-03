#!/usr/bin/env python3
"""Fail when a registered MCP tool is missing from the rendered catalog."""

from __future__ import annotations

import asyncio
import sys
from html.parser import HTMLParser
from pathlib import Path


class CatalogParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.in_code = False
        self.names: set[str] = set()

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag == "code":
            self.in_code = True

    def handle_endtag(self, tag: str) -> None:
        if tag == "code":
            self.in_code = False

    def handle_data(self, data: str) -> None:
        if self.in_code:
            self.names.add(data.strip())


def main() -> int:
    import allegro_mcp.tools  # noqa: F401
    from allegro_mcp.tools._runtime import mcp

    site = Path(sys.argv[1] if len(sys.argv) > 1 else "site")
    catalogs = list(site.glob("**/tool-catalog/index.html"))
    if not catalogs:
        print("Missing rendered tool catalog; run make docs-build.", file=sys.stderr)
        return 1
    expected = {t.name for t in asyncio.run(mcp.list_tools())}
    for catalog in catalogs:
        parser = CatalogParser()
        parser.feed(catalog.read_text())
        missing = sorted(expected - parser.names)
        if missing:
            print(f"{catalog}: undocumented tools: {missing}", file=sys.stderr)
            return 1
    print(f"All {len(expected)} tools appear in {len(catalogs)} rendered catalog(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
