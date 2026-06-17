"""
APIA Standard — test suite
Run: pytest tests/
"""
import pytest, json, glob, os
from pathlib import Path
from cli.apia import validate_manifest

MANIFESTS = sorted(glob.glob("manifests/*/apia.json"))

# ── Schema validation ────────────────────────────────────────────────────

@pytest.mark.parametrize("path", MANIFESTS)
def test_valid_json(path):
    """Every manifest must be valid JSON."""
    with open(path) as f:
        data = json.load(f)
    assert isinstance(data, dict)

@pytest.mark.parametrize("path", MANIFESTS)
def test_required_fields(path):
    """Every manifest must have all required top-level fields."""
    errors = validate_manifest(path)
    field_errors = [e for e in errors if "Missing required field" in e or "Missing service" in e or "Missing auth" in e or "Missing meta" in e]
    assert not field_errors, f"{path}: {field_errors}"

@pytest.mark.parametrize("path", MANIFESTS)
def test_min_capabilities(path):
    """Every manifest must have at least 5 capabilities."""
    with open(path) as f:
        data = json.load(f)
    caps = data.get("capabilities", [])
    assert len(caps) >= 5, f"{path}: only {len(caps)} capabilities (min 5)"

@pytest.mark.parametrize("path", MANIFESTS)
def test_capability_intents(path):
    """Every capability must have at least 2 intent phrases."""
    with open(path) as f:
        data = json.load(f)
    for i, cap in enumerate(data.get("capabilities", [])):
        intents = cap.get("intent", [])
        assert len(intents) >= 2, f"{path} cap[{i}] '{cap.get('id')}': only {len(intents)} intent phrases"

@pytest.mark.parametrize("path", MANIFESTS)
def test_description_for_ai(path):
    """description_for_ai must be at least 20 chars — not a placeholder."""
    with open(path) as f:
        data = json.load(f)
    svc_desc = data.get("service", {}).get("description_for_ai", "")
    assert len(svc_desc) >= 20, f"{path}: service.description_for_ai too short"
    for i, cap in enumerate(data.get("capabilities", [])):
        cap_desc = cap.get("description_for_ai", "")
        assert len(cap_desc) >= 20, f"{path} cap[{i}]: description_for_ai too short"

@pytest.mark.parametrize("path", MANIFESTS)
def test_apia_version(path):
    """meta.apia_version must be set."""
    with open(path) as f:
        data = json.load(f)
    assert data.get("meta", {}).get("apia_version") == "1.0", f"{path}: meta.apia_version must be 1.0"

@pytest.mark.parametrize("path", MANIFESTS)
def test_service_id_matches_directory(path):
    """service.id must match the directory name."""
    with open(path) as f:
        data = json.load(f)
    dir_name = Path(path).parent.name
    svc_id = data.get("service", {}).get("id", "")
    assert svc_id == dir_name, f"{path}: service.id '{svc_id}' != directory '{dir_name}'"

# ── Registry integrity ────────────────────────────────────────────────────

def test_registry_exists():
    assert Path("registry.json").exists(), "registry.json not found"

def test_registry_count():
    registry = json.loads(Path("registry.json").read_text())
    manifests = registry.get("manifests", [])
    actual = len(MANIFESTS)
    assert len(manifests) == actual, f"registry has {len(manifests)} entries but found {actual} manifest files"

def test_registry_capabilities_count():
    """capabilities_count in registry must match actual manifest."""
    registry = json.loads(Path("registry.json").read_text())
    errors = []
    for entry in registry.get("manifests", []):
        api_id = entry.get("id")
        reg_count = entry.get("capabilities_count", 0)
        manifest_path = Path(f"manifests/{api_id}/apia.json")
        if manifest_path.exists():
            actual = len(json.loads(manifest_path.read_text()).get("capabilities", []))
            if reg_count != actual:
                errors.append(f"{api_id}: registry says {reg_count}, actual {actual}")
    assert not errors, "Stale capabilities_count in registry:\n" + "\n".join(errors[:10])

def test_no_duplicate_ids():
    """No two manifests should have the same service.id."""
    ids = []
    for path in MANIFESTS:
        data = json.loads(open(path).read())
        ids.append(data.get("service", {}).get("id", ""))
    duplicates = [i for i in ids if ids.count(i) > 1]
    assert not duplicates, f"Duplicate service IDs: {set(duplicates)}"
