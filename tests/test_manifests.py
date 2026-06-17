"""
APIA Standard — test suite
Run from repo root: pytest tests/
"""
import pytest, json, os
from pathlib import Path

# Всегда находим корень репо относительно этого файла
REPO_ROOT = Path(__file__).parent.parent
MANIFESTS = sorted((REPO_ROOT / "manifests").glob("*/apia.json"))

# ── Schema validation ────────────────────────────────────────────────────

@pytest.mark.parametrize("path", MANIFESTS)
def test_valid_json(path):
    """Every manifest must be valid JSON."""
    data = json.loads(path.read_text())
    assert isinstance(data, dict)

@pytest.mark.parametrize("path", MANIFESTS)
def test_required_fields(path):
    """Every manifest must have all required top-level fields."""
    data = json.loads(path.read_text())
    for field in ["apia", "service", "auth", "capabilities", "meta"]:
        assert field in data, f"{path.name}: missing top-level field '{field}'"
    svc = data.get("service", {})
    for field in ["id", "name", "description_for_ai", "category", "url"]:
        assert field in svc, f"{path.name}: missing service.{field}"
    assert "type" in data.get("auth", {}), f"{path.name}: missing auth.type"
    assert "apia_version" in data.get("meta", {}), f"{path.name}: missing meta.apia_version"

@pytest.mark.parametrize("path", MANIFESTS)
def test_min_capabilities(path):
    """Every manifest must have at least 5 capabilities."""
    data = json.loads(path.read_text())
    caps = data.get("capabilities", [])
    assert len(caps) >= 5, f"{path.parent.name}: only {len(caps)} capabilities (min 5)"

@pytest.mark.parametrize("path", MANIFESTS)
def test_capability_intents(path):
    """Every capability must have at least 2 intent phrases."""
    data = json.loads(path.read_text())
    for i, cap in enumerate(data.get("capabilities", [])):
        intents = cap.get("intent", [])
        assert len(intents) >= 2,             f"{path.parent.name} cap[{i}] '{cap.get('id')}': only {len(intents)} intent phrases"

@pytest.mark.parametrize("path", MANIFESTS)
def test_description_for_ai(path):
    """description_for_ai must be at least 20 chars."""
    data = json.loads(path.read_text())
    svc_desc = data.get("service", {}).get("description_for_ai", "")
    assert len(svc_desc) >= 20, f"{path.parent.name}: service.description_for_ai too short"
    for i, cap in enumerate(data.get("capabilities", [])):
        cap_desc = cap.get("description_for_ai", "")
        assert len(cap_desc) >= 20,             f"{path.parent.name} cap[{i}] '{cap.get('id')}': description_for_ai too short"

@pytest.mark.parametrize("path", MANIFESTS)
def test_apia_version(path):
    """meta.apia_version must be 1.0."""
    data = json.loads(path.read_text())
    assert data.get("meta", {}).get("apia_version") == "1.0",         f"{path.parent.name}: meta.apia_version must be '1.0'"

@pytest.mark.parametrize("path", MANIFESTS)
def test_service_id_matches_directory(path):
    """service.id must match the directory name."""
    data = json.loads(path.read_text())
    dir_name = path.parent.name
    svc_id = data.get("service", {}).get("id", "")
    assert svc_id == dir_name,         f"service.id '{svc_id}' != directory '{dir_name}'"

# ── Registry integrity ────────────────────────────────────────────────────

def test_registry_exists():
    assert (REPO_ROOT / "registry.json").exists(), "registry.json not found"

def test_registry_count():
    """registry.json must have exactly as many entries as manifest files."""
    registry = json.loads((REPO_ROOT / "registry.json").read_text())
    reg_count = len(registry.get("manifests", []))
    file_count = len(MANIFESTS)
    assert reg_count == file_count,         f"registry has {reg_count} entries but found {file_count} manifest files"

def test_registry_capabilities_count():
    """capabilities_count in registry must match actual manifest."""
    registry = json.loads((REPO_ROOT / "registry.json").read_text())
    errors = []
    for entry in registry.get("manifests", []):
        api_id = entry.get("id")
        reg_count = entry.get("capabilities_count", 0)
        manifest_path = REPO_ROOT / "manifests" / api_id / "apia.json"
        if manifest_path.exists():
            actual = len(json.loads(manifest_path.read_text()).get("capabilities", []))
            if reg_count != actual:
                errors.append(f"{api_id}: registry says {reg_count}, actual {actual}")
    assert not errors, "Stale capabilities_count:\n" + "\n".join(errors[:10])

def test_no_duplicate_ids():
    """No two manifests should have the same service.id."""
    ids = [json.loads(p.read_text()).get("service", {}).get("id", "") for p in MANIFESTS]
    duplicates = {i for i in ids if ids.count(i) > 1}
    assert not duplicates, f"Duplicate service IDs: {duplicates}"
