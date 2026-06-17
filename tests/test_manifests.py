"""
APIA Standard — test suite
Run from repo root: pytest tests/
"""
import pytest, json
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
MANIFESTS = sorted((REPO_ROOT / "manifests").glob("*/apia.json"))

def validate_manifest(path):
    """Inline validator — no external imports needed."""
    errors = []
    try:
        data = json.loads(Path(path).read_text())
    except json.JSONDecodeError as e:
        return [f"Invalid JSON: {e}"]
    for field in ["apia", "service", "auth", "capabilities", "meta"]:
        if field not in data:
            errors.append(f"Missing required field: {field}")
    svc = data.get("service", {})
    for field in ["id", "name", "description_for_ai", "category", "url"]:
        if field not in svc:
            errors.append(f"Missing service.{field}")
    if "type" not in data.get("auth", {}):
        errors.append("Missing auth.type")
    if "apia_version" not in data.get("meta", {}):
        errors.append("Missing meta.apia_version")
    caps = data.get("capabilities", [])
    if len(caps) < 5:
        errors.append(f"Only {len(caps)} capabilities (min 5)")
    for i, cap in enumerate(caps):
        for f in ["id", "description_for_ai", "intent", "endpoint"]:
            if f not in cap:
                errors.append(f"capabilities[{i}] missing {f}")
        if len(cap.get("intent", [])) < 2:
            errors.append(f"capabilities[{i}] needs >= 2 intent phrases")
    return errors

# ── Per-manifest tests ───────────────────────────────────────────────────

@pytest.mark.parametrize("path", MANIFESTS)
def test_valid_json(path):
    data = json.loads(path.read_text())
    assert isinstance(data, dict)

@pytest.mark.parametrize("path", MANIFESTS)
def test_required_fields(path):
    errors = [e for e in validate_manifest(path) if "Missing" in e]
    assert not errors, f"{path.parent.name}: {errors}"

@pytest.mark.parametrize("path", MANIFESTS)
def test_min_capabilities(path):
    data = json.loads(path.read_text())
    caps = data.get("capabilities", [])
    assert len(caps) >= 5, f"{path.parent.name}: {len(caps)} caps (min 5)"

@pytest.mark.parametrize("path", MANIFESTS)
def test_capability_intents(path):
    data = json.loads(path.read_text())
    for i, cap in enumerate(data.get("capabilities", [])):
        assert len(cap.get("intent", [])) >= 2, \
            f"{path.parent.name} cap[{i}] '{cap.get('id')}': needs >= 2 intents"

@pytest.mark.parametrize("path", MANIFESTS)
def test_description_for_ai(path):
    data = json.loads(path.read_text())
    desc = data.get("service", {}).get("description_for_ai", "")
    assert len(desc) >= 20, f"{path.parent.name}: description_for_ai too short"
    for i, cap in enumerate(data.get("capabilities", [])):
        cdesc = cap.get("description_for_ai", "")
        assert len(cdesc) >= 20, \
            f"{path.parent.name} cap[{i}]: description_for_ai too short"

@pytest.mark.parametrize("path", MANIFESTS)
def test_apia_version(path):
    data = json.loads(path.read_text())
    assert data.get("meta", {}).get("apia_version") == "1.0", \
        f"{path.parent.name}: meta.apia_version must be '1.0'"

@pytest.mark.parametrize("path", MANIFESTS)
def test_service_id_matches_directory(path):
    data = json.loads(path.read_text())
    assert data.get("service", {}).get("id") == path.parent.name, \
        f"service.id != directory name in {path.parent.name}"

# ── Registry integrity ───────────────────────────────────────────────────

def test_registry_exists():
    assert (REPO_ROOT / "registry.json").exists()

def test_registry_count():
    registry = json.loads((REPO_ROOT / "registry.json").read_text())
    assert len(registry["manifests"]) == len(MANIFESTS), \
        f"registry={len(registry['manifests'])} files={len(MANIFESTS)}"

def test_registry_capabilities_count():
    registry = json.loads((REPO_ROOT / "registry.json").read_text())
    errors = []
    for entry in registry["manifests"]:
        api_id = entry.get("id","")
        reg_n = entry.get("capabilities_count", 0)
        mp = REPO_ROOT / "manifests" / api_id / "apia.json"
        if mp.exists():
            actual = len(json.loads(mp.read_text()).get("capabilities", []))
            if reg_n != actual:
                errors.append(f"{api_id}: registry={reg_n} actual={actual}")
    assert not errors, "Stale caps count:\n" + "\n".join(errors[:10])

def test_no_duplicate_ids():
    ids = [json.loads(p.read_text()).get("service",{}).get("id","") for p in MANIFESTS]
    dupes = {i for i in ids if ids.count(i) > 1}
    assert not dupes, f"Duplicate IDs: {dupes}"
