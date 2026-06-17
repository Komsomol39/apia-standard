#!/usr/bin/env python3
"""
openapi2apia — Convert an OpenAPI 3.x spec to an APIA manifest

Usage:
  python tools/openapi2apia.py openapi.yaml --id my-api --output manifests/my-api/apia.json
  python tools/openapi2apia.py https://petstore3.swagger.io/api/v3/openapi.json --id petstore

The converter:
- Extracts all endpoints and creates capabilities
- Uses operationId or summary as capability ID
- Maps OpenAPI description to description_for_ai
- Infers auth type from securitySchemes
- Generates intent phrases from operation tags and summary
- Leaves agent_hints blank for human review
"""
import sys, json, argparse, urllib.request, re
from pathlib import Path

try:
    import yaml
    HAS_YAML = True
except ImportError:
    HAS_YAML = False

def load_spec(source):
    if source.startswith("http"):
        with urllib.request.urlopen(source) as r:
            content = r.read()
    else:
        content = Path(source).read_bytes()

    if source.endswith(".yaml") or source.endswith(".yml"):
        if not HAS_YAML:
            sys.exit("PyYAML required: pip install pyyaml")
        return yaml.safe_load(content)
    return json.loads(content)

def slugify(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")

def infer_intent(operation, path, method):
    phrases = []
    summary = operation.get("summary", "")
    tags = operation.get("tags", [])
    op_id = operation.get("operationId", "")

    if summary:
        phrases.append(summary.lower())

    # Generate from method + path
    path_parts = [p for p in path.split("/") if p and not p.startswith("{")]
    if path_parts:
        resource = path_parts[-1].replace("-", " ").replace("_", " ")
        if method == "get":
            phrases.append(f"get {resource}")
            phrases.append(f"fetch {resource}")
        elif method == "post":
            phrases.append(f"create {resource}")
            phrases.append(f"add {resource}")
        elif method == "put" or method == "patch":
            phrases.append(f"update {resource}")
        elif method == "delete":
            phrases.append(f"delete {resource}")

    for tag in tags:
        phrases.append(f"{method} {tag.lower()}")

    # Deduplicate preserving order
    seen = set()
    result = []
    for p in phrases:
        if p not in seen and len(p) > 3:
            seen.add(p)
            result.append(p)

    return result[:6] if result else [f"{method} {path}"]

def infer_auth(spec):
    schemes = spec.get("components", {}).get("securitySchemes", {})
    if not schemes:
        security = spec.get("security", [])
        if not security:
            return {"type": "none", "anonymous_access": True, "cost": "free"}

    for name, scheme in schemes.items():
        stype = scheme.get("type", "").lower()
        if stype == "apikey":
            return {"type": "apiKey", "anonymous_access": False,
                    "how_to_get": f"Get API key from provider website",
                    "cost": "see provider pricing"}
        elif stype == "oauth2":
            return {"type": "oauth2", "anonymous_access": False,
                    "how_to_get": "OAuth2 flow required",
                    "cost": "see provider pricing"}
        elif stype == "http":
            scheme_name = scheme.get("scheme", "bearer").lower()
            return {"type": scheme_name, "anonymous_access": False,
                    "how_to_get": "See API documentation",
                    "cost": "see provider pricing"}

    return {"type": "apiKey", "anonymous_access": False,
            "how_to_get": "See API documentation",
            "cost": "see provider pricing"}

def build_input_schema(operation, spec):
    params = operation.get("parameters", [])
    body = operation.get("requestBody", {})
    result = {}

    for param in params:
        name = param.get("name", "")
        schema = param.get("schema", {})
        required = param.get("required", False)
        description = param.get("description", schema.get("description", ""))
        result[name] = {
            "type": schema.get("type", "string"),
            "required": required,
            "description": description,
        }
        if "default" in schema:
            result[name]["default"] = schema["default"]

    if body:
        content = body.get("content", {})
        for media_type, media in content.items():
            if "schema" in media:
                s = media["schema"]
                props = s.get("properties", {})
                required_props = s.get("required", [])
                for pname, pschema in list(props.items())[:10]:
                    result[pname] = {
                        "type": pschema.get("type", "string"),
                        "required": pname in required_props,
                        "description": pschema.get("description", ""),
                    }
            break

    return result

def convert(spec, api_id, base_url=None):
    info = spec.get("info", {})
    servers = spec.get("servers", [{}])
    if base_url is None:
        base_url = servers[0].get("url", "") if servers else ""

    paths = spec.get("paths", {})
    capabilities = []
    seen_ids = set()

    for path, path_item in list(paths.items())[:50]:  # limit to 50 endpoints
        for method in ["get", "post", "put", "patch", "delete"]:
            operation = path_item.get(method)
            if not operation:
                continue

            # Build capability ID
            op_id = operation.get("operationId", "")
            if op_id:
                cap_id = slugify(op_id)[:40]
            else:
                path_slug = slugify(path)[:30]
                cap_id = f"{method}_{path_slug}"

            # Deduplicate
            original = cap_id
            counter = 1
            while cap_id in seen_ids:
                cap_id = f"{original}_{counter}"
                counter += 1
            seen_ids.add(cap_id)

            summary = operation.get("summary", "")
            description = operation.get("description", summary or f"{method.upper()} {path}")

            endpoint = f"{method.upper()} {base_url}{path}"
            input_schema = build_input_schema(operation, spec)
            intent = infer_intent(operation, path, method)

            # Output fields from responses
            output_fields = []
            responses = operation.get("responses", {})
            for status, resp in responses.items():
                if str(status).startswith("2"):
                    content = resp.get("content", {})
                    for media_type, media in content.items():
                        schema = media.get("schema", {})
                        props = schema.get("properties", {})
                        output_fields = [f"{k}: {v.get('type','?')}" for k, v in list(props.items())[:5]]
                        break
                    break

            cap = {
                "id": cap_id,
                "description_for_ai": description[:300],
                "intent": intent,
                "endpoint": endpoint,
                "input": input_schema,
                "output": {
                    "type": "object",
                    "fields": output_fields or ["response body"]
                },
                "realtime": True,
                "requires_auth": bool(operation.get("security") or spec.get("security"))
            }
            capabilities.append(cap)

    # Ensure minimum 5 caps (pad with placeholders if needed)
    while len(capabilities) < 5:
        capabilities.append({
            "id": f"placeholder_{len(capabilities)+1}",
            "description_for_ai": "TODO: add description for this capability",
            "intent": ["TODO: add intent phrases"],
            "endpoint": "TODO",
            "input": {},
            "output": {"type": "object", "fields": []},
            "realtime": True,
            "requires_auth": True
        })

    manifest = {
        "apia": "1.0",
        "service": {
            "id": api_id,
            "name": info.get("title", api_id),
            "description_for_ai": info.get("description", f"TODO: describe {api_id} for AI agents")[:500],
            "category": "TODO",
            "geo": "global",
            "language": "en",
            "url": base_url or "TODO",
            "api_base": base_url or "TODO",
            "docs": info.get("termsOfService", "TODO")
        },
        "auth": infer_auth(spec),
        "capabilities": capabilities,
        "agent_hints": {
            "rate_limiting": "TODO: describe rate limits",
            "pagination": "TODO: describe pagination",
            "errors": "TODO: describe common errors"
        },
        "meta": {
            "apia_version": "1.0",
            "last_verified": "TODO",
            "notes": f"Auto-generated from OpenAPI spec. Review and complete TODOs before submitting."
        }
    }

    return manifest

def main():
    parser = argparse.ArgumentParser(description="Convert OpenAPI spec to APIA manifest")
    parser.add_argument("source", help="Path or URL to OpenAPI spec (JSON or YAML)")
    parser.add_argument("--id", required=True, dest="api_id", help="API identifier (e.g. my-service)")
    parser.add_argument("--output", "-o", help="Output path (default: manifests/<id>/apia.json)")
    parser.add_argument("--base-url", help="Override base URL from spec")
    args = parser.parse_args()

    print(f"Loading spec from {args.source}...")
    spec = load_spec(args.source)

    print(f"Converting to APIA manifest (id={args.api_id})...")
    manifest = convert(spec, args.api_id, args.base_url)

    caps = len(manifest["capabilities"])
    todos = json.dumps(manifest).count("TODO")

    output = args.output or f"manifests/{args.api_id}/apia.json"
    Path(output).parent.mkdir(parents=True, exist_ok=True)
    Path(output).write_text(json.dumps(manifest, indent=2, ensure_ascii=False))

    print(f"\nWrote {output}")
    print(f"Capabilities: {caps}")
    print(f"TODOs to complete: {todos}")
    print(f"\nNext steps:")
    print(f"  1. Review and complete all TODO fields")
    print(f"  2. Run: python cli/apia.py validate {output}")
    print(f"  3. Submit PR to github.com/Komsomol39/apia-standard")

if __name__ == "__main__":
    main()
