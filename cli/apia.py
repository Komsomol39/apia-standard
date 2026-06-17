#!/usr/bin/env python3
"""
apia — CLI for the APIA standard
Usage:
  apia validate [manifest.json|--all]
  apia search <query>
  apia inspect <api-id>
  apia build-prompt <query>
"""
import sys, os, json, argparse, urllib.request, glob, re
from pathlib import Path

REGISTRY_URL = "https://raw.githubusercontent.com/Komsomol39/apia-standard/main/registry.json"
SCHEMA_PATH  = Path(__file__).parent.parent / "schema" / "apia-1.0.schema.json"

def load_registry():
    try:
        with urllib.request.urlopen(REGISTRY_URL) as r:
            return json.loads(r.read())
    except:
        # fallback local
        local = Path(__file__).parent.parent / "registry.json"
        if local.exists():
            return json.loads(local.read_text())
        sys.exit("Could not load registry")

def load_schema():
    if SCHEMA_PATH.exists():
        return json.loads(SCHEMA_PATH.read_text())
    return None

def validate_manifest(path, schema=None):
    errors = []
    try:
        with open(path) as f:
            manifest = json.load(f)
    except json.JSONDecodeError as e:
        return [f"Invalid JSON: {e}"]

    # Required top-level fields
    for field in ["apia", "service", "auth", "capabilities", "meta"]:
        if field not in manifest:
            errors.append(f"Missing required field: {field}")

    # Service fields
    svc = manifest.get("service", {})
    for field in ["id", "name", "description_for_ai", "category", "url"]:
        if field not in svc:
            errors.append(f"Missing service.{field}")

    # Capabilities
    caps = manifest.get("capabilities", [])
    if not caps:
        errors.append("capabilities must not be empty")
    if len(caps) < 5:
        errors.append(f"capabilities has {len(caps)} items, minimum is 5")
    for i, cap in enumerate(caps):
        for field in ["id", "description_for_ai", "intent", "endpoint"]:
            if field not in cap:
                errors.append(f"capabilities[{i}] missing {field}")
        if not isinstance(cap.get("intent", []), list):
            errors.append(f"capabilities[{i}].intent must be a list")
        if len(cap.get("intent", [])) < 2:
            errors.append(f"capabilities[{i}].intent must have at least 2 phrases")

    # Auth
    auth = manifest.get("auth", {})
    if "type" not in auth:
        errors.append("Missing auth.type")

    # Meta
    meta = manifest.get("meta", {})
    if "apia_version" not in meta:
        errors.append("Missing meta.apia_version")

    return errors

def cmd_validate(args):
    schema = load_schema()
    if args.all:
        manifests = sorted(glob.glob("manifests/*/apia.json"))
        if not manifests:
            manifests = sorted(glob.glob("*/apia.json"))
        ok, fail = 0, 0
        for path in manifests:
            errors = validate_manifest(path, schema)
            if errors:
                print(f"FAIL {path}")
                for e in errors:
                    print(f"     {e}")
                fail += 1
            else:
                ok += 1
        print(f"\nResult: {ok} valid, {fail} invalid out of {ok+fail} manifests")
        if fail:
            sys.exit(1)
    else:
        path = args.file or "apia.json"
        errors = validate_manifest(path, schema)
        if errors:
            print(f"FAIL: {path}")
            for e in errors:
                print(f"  {e}")
            sys.exit(1)
        else:
            manifest = json.loads(open(path).read())
            caps = len(manifest.get("capabilities", []))
            name = manifest["service"]["name"]
            print(f"OK: {name} ({caps} capabilities)")

def cmd_search(args):
    query = " ".join(args.query).lower()
    registry = load_registry()
    results = []
    for m in registry.get("manifests", []):
        score = 0
        desc = (m.get("description_for_ai","") + " " + m.get("name","") + " " + m.get("category","")).lower()
        # Check capabilities intent
        for cap in m.get("capabilities", []):
            for intent in cap.get("intent", []):
                if query in intent.lower():
                    score += 3
        if query in desc:
            score += 2
        if query in m.get("id","").lower():
            score += 1
        if score > 0:
            results.append((score, m))

    results.sort(key=lambda x: -x[0])
    if not results:
        print(f"No results for: {query}")
        return
    print(f"Results for '{query}':\n")
    for score, m in results[:10]:
        caps_count = m.get("capabilities_count", len(m.get("capabilities",[])))
        anon = "free" if m.get("anonymous_access") else "auth"
        print(f"  {m['id']:30s} {m.get('name','')[:35]:35s} [{caps_count} caps, {anon}]")

def cmd_inspect(args):
    api_id = args.api_id
    # Try local first
    local = Path(f"manifests/{api_id}/apia.json")
    if not local.exists():
        local = Path(f"{api_id}/apia.json")
    if local.exists():
        manifest = json.loads(local.read_text())
    else:
        # Fetch from GitHub
        url = f"https://raw.githubusercontent.com/Komsomol39/apia-standard/main/manifests/{api_id}/apia.json"
        try:
            with urllib.request.urlopen(url) as r:
                manifest = json.loads(r.read())
        except:
            sys.exit(f"API not found: {api_id}")

    svc = manifest["service"]
    auth = manifest["auth"]
    caps = manifest["capabilities"]

    print(f"\n{'='*60}")
    print(f"  {svc['name']}")
    print(f"{'='*60}")
    print(f"  ID:          {svc['id']}")
    print(f"  Category:    {svc.get('category','')}")
    print(f"  URL:         {svc.get('url','')}")
    print(f"  Auth:        {auth.get('type','')} | anonymous: {auth.get('anonymous_access', False)}")
    print(f"  Cost:        {auth.get('cost','')}")
    print(f"\n  {svc['description_for_ai']}")
    print(f"\n  Capabilities ({len(caps)}):")
    for cap in caps:
        print(f"\n    [{cap['id']}]")
        print(f"    {cap['description_for_ai']}")
        print(f"    Endpoint: {cap['endpoint']}")
        print(f"    Intent:   {', '.join(cap.get('intent',[])[:3])}")

def cmd_build_prompt(args):
    query = " ".join(args.query)
    registry = load_registry()
    query_lower = query.lower()

    # Find best matching capabilities
    matches = []
    for m in registry.get("manifests", []):
        for cap in m.get("capabilities", []):
            score = 0
            for intent in cap.get("intent", []):
                if any(w in intent.lower() for w in query_lower.split()):
                    score += 2
                if query_lower in intent.lower():
                    score += 3
            if query_lower in cap.get("description_for_ai","").lower():
                score += 1
            if score > 0:
                matches.append((score, m, cap))

    matches.sort(key=lambda x: -x[0])
    top = matches[:3]

    if not top:
        print(f"No matching APIs found for: {query}")
        return

    prompt = f"""You need to: {query}

The following APIs can help. Choose the most appropriate one and call it.

"""
    for i, (score, m, cap) in enumerate(top, 1):
        auth = m.get("auth", {})
        prompt += f"""## Option {i}: {m['service']['name']} — {cap['id']}
Description: {cap['description_for_ai']}
Endpoint: {cap['endpoint']}
Auth: {auth.get('type','none')} | Free to use: {auth.get('anonymous_access', False)}
"""
        if cap.get("input"):
            inp = cap["input"]
            required = [k for k,v in inp.items() if isinstance(v,dict) and v.get("required")]
            optional = [k for k,v in inp.items() if isinstance(v,dict) and not v.get("required")]
            if required:
                prompt += f"Required params: {', '.join(required)}\n"
            if optional:
                prompt += f"Optional params: {', '.join(optional)}\n"
        if cap.get("output", {}).get("fields"):
            prompt += f"Returns: {', '.join(cap['output']['fields'][:4])}\n"
        prompt += "\n"

    prompt += "Call the API, extract the relevant information, and respond to the user."
    print(prompt)

def main():
    parser = argparse.ArgumentParser(description="APIA CLI")
    sub = parser.add_subparsers(dest="command")

    # validate
    p_val = sub.add_parser("validate", help="Validate a manifest")
    p_val.add_argument("file", nargs="?", help="Path to apia.json")
    p_val.add_argument("--all", action="store_true", help="Validate all manifests")

    # search
    p_search = sub.add_parser("search", help="Search APIs by intent")
    p_search.add_argument("query", nargs="+")

    # inspect
    p_inspect = sub.add_parser("inspect", help="Inspect an API manifest")
    p_inspect.add_argument("api_id")

    # build-prompt
    p_prompt = sub.add_parser("build-prompt", help="Build an agent prompt for a task")
    p_prompt.add_argument("query", nargs="+")

    args = parser.parse_args()
    if args.command == "validate":
        cmd_validate(args)
    elif args.command == "search":
        cmd_search(args)
    elif args.command == "inspect":
        cmd_inspect(args)
    elif args.command == "build-prompt":
        cmd_build_prompt(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
