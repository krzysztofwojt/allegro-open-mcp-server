#!/usr/bin/env python3
"""Regenerate into a temporary tree and fail if committed output differs."""

from __future__ import annotations

import subprocess
import tempfile
from pathlib import Path

import gen_models
import gen_tools

ROOT = Path(__file__).resolve().parent.parent


def main() -> int:
    with tempfile.TemporaryDirectory() as temp:
        target = Path(temp)
        gen_models.OUTPUT_DIR = target / "models"
        gen_models.OUTPUT_FILE = gen_models.OUTPUT_DIR / "models.py"
        gen_models.main([])
        gen_tools.TOOLS_DIR = target / "tools"
        gen_tools.TOOLS_DIR.mkdir()
        gen_tools.main()
        subprocess.run(["ruff", "format", str(gen_tools.TOOLS_DIR)], check=True)
        subprocess.run(["ruff", "check", "--fix", str(gen_tools.TOOLS_DIR)], check=True)
        mismatches = []
        for generated, committed in (
            (gen_models.OUTPUT_DIR, ROOT / "src/allegro_client/models/_generated"),
            (gen_tools.TOOLS_DIR, ROOT / "src/allegro_mcp/tools"),
        ):
            for file in generated.iterdir():
                original = committed / file.name
                if not original.exists() or file.read_bytes() != original.read_bytes():
                    mismatches.append(str(original.relative_to(ROOT)))
            expected = {p.name for p in generated.iterdir()}
            mismatches.extend(
                str(file.relative_to(ROOT))
                for file in committed.glob("*.py")
                if file.name not in expected
                and file.name != "auth.py"
                and not file.name.startswith("_")
            )
        if mismatches:
            print("Stale generated files:\n" + "\n".join(mismatches))
            return 1
    print("Generated models, tools and operation contract are reproducible.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
