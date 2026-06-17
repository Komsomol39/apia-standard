"""APIA Standard test suite. Run: pytest tests/"""
import pytest, json
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
MANIFESTS = sorted((REPO_ROOT / "manifests").glob("*/apia.json"))

def validate(path):
    errors = []
    try:
        d = json.loads(Path(path).read_text())
    except Exception as e:
        return [str(e)]
    for f in ["apia","service","auth","capabilities","meta"]:
        if f not in d: errors.append(f"missing {f}")
    svc = d.get("service",{})
    for f in ["id","name","description_for_ai","category","url"]:
        if f not in svc: errors.append(f"missing service.{f}")
    if "type" not in d.get("auth",{}): errors.append("missing auth.type")
    if "apia_version" not in d.get("meta",{}): errors.append("missing meta.apia_version")
    caps = d.get("capabilities",[])
    if len(caps) < 5: errors.append(f"only {len(caps)} caps")
    for i,cap in enumerate(caps):
        if len(cap.get("intent",[])) < 2: errors.append(f"cap[{i}] needs 2+ intents")
        if len(cap.get("description_for_ai","")) < 20: errors.append(f"cap[{i}] short desc")
    return errors

@pytest.mark.parametrize("path", MANIFESTS)
def test_valid_json(path):
    assert isinstance(json.loads(path.read_text()), dict)

@pytest.mark.parametrize("path", MANIFESTS)
def test_required_fields(path):
    e = [x for x in validate(path) if "missing" in x]
    assert not e, f"{path.parent.name}: {e}"

@pytest.mark.parametrize("path", MANIFESTS)
def test_min_capabilities(path):
    caps = json.loads(path.read_text()).get("capabilities",[])
    assert len(caps) >= 5, f"{path.parent.name}: {len(caps)} caps"

@pytest.mark.parametrize("path", MANIFESTS)
def test_capability_intents(path):
    for i,cap in enumerate(json.loads(path.read_text()).get("capabilities",[])):
        assert len(cap.get("intent",[])) >= 2, f"{path.parent.name}[{i}] needs 2+ intents"

@pytest.mark.parametrize("path", MANIFESTS)
def test_apia_version(path):
    assert json.loads(path.read_text()).get("meta",{}).get("apia_version") == "1.0"

@pytest.mark.parametrize("path", MANIFESTS)
def test_service_id_matches_directory(path):
    assert json.loads(path.read_text()).get("service",{}).get("id") == path.parent.name

def test_registry_exists():
    assert (REPO_ROOT / "registry.json").exists()

def test_registry_count():
    reg = json.loads((REPO_ROOT / "registry.json").read_text())
    assert len(reg["manifests"]) == len(MANIFESTS), f"registry={len(reg['manifests'])} files={len(MANIFESTS)}"

def test_no_duplicate_ids():
    ids = [json.loads(p.read_text()).get("service",{}).get("id","") for p in MANIFESTS]
    dupes = {i for i in ids if ids.count(i)>1}
    assert not dupes, f"Duplicate IDs: {dupes}"
