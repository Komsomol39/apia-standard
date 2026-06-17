#!/usr/bin/env python3
"""
tools/check_registry.py

Full registry integrity check:
- manifest file count matches registry.json
- no duplicate service.id
- registry entries match actual manifest content
- required fields present
- capabilities_count accurate
- category and auth.type valid
- last_verified not empty

Usage: python tools/check_registry.py
Exit code 0 = OK, 1 = errors found
"""
import json, sys
from pathlib import Path

try:
    import jsonschema
    HAS_JSONSCHEMA = True
except ImportError:
    HAS_JSONSCHEMA = False

ROOT      = Path(__file__).parent.parent
REG_PATH  = ROOT / "registry.json"
SCHEMA_P  = ROOT / "schema" / "apia-1.0.schema.json"
MANIFESTS = sorted(ROOT.glob("manifests/*/apia.json"))

VALID_CATEGORIES = {
    "ai","ai_media","analytics","business","devtools","ecommerce",
    "environment","finance","food","healthcare","hr","iot","legal",
    "logistics","maps","media","messaging","payments","productivity",
    "real_estate","search","social","sports","transport","travel","utilities","weather"
}
VALID_AUTH_TYPES = {"none","apiKey","bearer","oauth2","basic","cookie","header"}

errors   = []
warnings = []

def err(msg):  errors.append(msg)
def warn(msg): warnings.append(msg)

# ── Load registry ─────────────────────────────────────────────────
registry = json.loads(REG_PATH.read_text())
reg_entries = registry.get("manifests", [])
reg_by_id   = {e["id"]: e for e in reg_entries}

# ── Load schema ────────────────────────────────────────────────────
schema = None
if HAS_JSONSCHEMA and SCHEMA_P.exists():
    schema = json.loads(SCHEMA_P.read_text())

print(f"Registry entries : {len(reg_entries)}")
print(f"Manifest files   : {len(MANIFESTS)}")
print(f"jsonschema       : {'available' if HAS_JSONSCHEMA else 'not installed (pip install jsonschema)'}")
print()

# ── 1. Count match ─────────────────────────────────────────────────
if len(reg_entries) != len(MANIFESTS):
    err(f"COUNT MISMATCH: registry={len(reg_entries)}, files={len(MANIFESTS)}")

# ── 2. Duplicate IDs in registry ──────────────────────────────────
ids = [e["id"] for e in reg_entries]
dupes = {i for i in ids if ids.count(i) > 1}
if dupes:
    err(f"DUPLICATE IDs in registry: {dupes}")

# ── 3. Per-manifest checks ─────────────────────────────────────────
schema_errors = 0
for mp in MANIFESTS:
    api_id = mp.parent.name
    try:
        data = json.loads(mp.read_text())
    except json.JSONDecodeError as e:
        err(f"{api_id}: invalid JSON — {e}"); continue

    svc  = data.get("service", {})
    auth = data.get("auth", {})
    caps = data.get("capabilities", [])
    meta = data.get("meta", {})

    # service.id matches directory
    if svc.get("id") != api_id:
        err(f"{api_id}: service.id='{svc.get('id')}' != directory '{api_id}'")

    # required fields
    for field in ["apia","service","auth","capabilities","meta"]:
        if field not in data:
            err(f"{api_id}: missing top-level field '{field}'")
    for field in ["id","name","description_for_ai","category","url","api_base"]:
        if field not in svc:
            warn(f"{api_id}: missing service.{field}")

    # category valid
    cat = svc.get("category","")
    if cat and cat not in VALID_CATEGORIES:
        warn(f"{api_id}: unknown category '{cat}'")

    # auth.type valid
    atype = auth.get("type","")
    if atype and atype not in VALID_AUTH_TYPES:
        warn(f"{api_id}: unknown auth.type '{atype}'")

    # capabilities count
    if len(caps) < 5:
        err(f"{api_id}: only {len(caps)} capabilities (min 5)")

    # capabilities quality
    for i, cap in enumerate(caps):
        if len(cap.get("intent",[])) < 2:
            err(f"{api_id} cap[{i}] '{cap.get('id','')}': < 2 intent phrases")
        if len(cap.get("description_for_ai","")) < 20:
            err(f"{api_id} cap[{i}]: description_for_ai too short")

    # last_verified
    if not meta.get("last_verified") or meta.get("last_verified") == "TODO":
        warn(f"{api_id}: meta.last_verified is empty or TODO")

    # registry entry matches manifest
    if api_id in reg_by_id:
        entry = reg_by_id[api_id]
        reg_caps = entry.get("capabilities_count", 0)
        if reg_caps != len(caps):
            err(f"{api_id}: registry capabilities_count={reg_caps} but manifest has {len(caps)}")
        if entry.get("category") != svc.get("category"):
            warn(f"{api_id}: registry category='{entry.get('category')}' != manifest '{svc.get('category')}'")
    else:
        warn(f"{api_id}: manifest exists but not in registry")

    # JSON Schema validation
    if HAS_JSONSCHEMA and schema:
        try:
            jsonschema.validate(data, schema)
        except jsonschema.ValidationError as e:
            warn(f"{api_id}: schema note — {e.message[:80]}")
            schema_errors += 1

# ── Summary ────────────────────────────────────────────────────────
print(f"Errors   : {len(errors)}")
print(f"Warnings : {len(warnings)}")
if schema_errors:
    print(f"Schema   : {schema_errors} violations")

if errors:
    print("\nERRORS:")
    for e in errors[:30]:
        print(f"  ❌ {e}")

if warnings:
    print("\nWARNINGS (first 10):")
    for w in warnings[:10]:
        print(f"  ⚠️  {w}")

if not errors:
    print("\nOK: registry integrity check passed")
    sys.exit(0)
else:
    print(f"\nFAIL: {len(errors)} errors found")
    sys.exit(1)
