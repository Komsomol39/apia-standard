#!/usr/bin/env python3
"""Check that registry.json matches manifest files on disk."""
import json, sys
from pathlib import Path

root = Path(__file__).parent.parent
registry = json.loads((root / "registry.json").read_text())
manifests = list((root / "manifests").glob("*/apia.json"))

reg_n = len(registry["manifests"])
file_n = len(manifests)

print(f"Registry entries: {reg_n}")
print(f"Manifest files:   {file_n}")

if reg_n != file_n:
    print(f"FAIL: mismatch {reg_n} vs {file_n}", file=sys.stderr)
    sys.exit(1)

print("OK: counts match")
