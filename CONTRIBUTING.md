# Contributing to APIA

## Quick start

```bash
git clone https://github.com/Komsomol39/apia-standard
cd apia-standard
pip install pytest
pytest tests/ -v
```

## Adding an API

**Option A — from OpenAPI spec (fastest):**
```bash
python tools/openapi2apia.py https://api.example.com/openapi.json --id my-api
python cli/apia.py validate manifests/my-api/apia.json
```

**Option B — manually:**
```bash
mkdir manifests/my-api
# Copy and edit an existing manifest as template
cp manifests/open-meteo/apia.json manifests/my-api/apia.json
# Edit, then validate:
python cli/apia.py validate manifests/my-api/apia.json
```

Submit a pull request. CI runs automatically and checks:
- JSON schema validation for every manifest
- Minimum 5 capabilities per manifest
- Minimum 2 intent phrases per capability
- `service.id` matches directory name
- `registry.json` count matches manifest files
- End-to-end demo (real HTTP call to Open-Meteo)

## Manifest quality checklist

Before submitting:
- [ ] `description_for_ai` written for LLMs, not developers (>20 chars)
- [ ] `intent` has phrases in natural language (include Russian if geo=ru)
- [ ] `endpoint` is a real, working URL
- [ ] `auth.how_to_get` explains where to get credentials
- [ ] `meta.last_verified` set to today's date
- [ ] `agent_hints` filled with rate limiting and pagination info

## Validating locally

```bash
# Validate one manifest
python cli/apia.py validate manifests/my-api/apia.json

# Validate all 260 manifests
python cli/apia.py validate --all

# Run full test suite
pytest tests/ -v

# Check registry integrity
python tools/check_registry.py
```

## CLI usage

```bash
# Search APIs by intent
python cli/apia.py search "weather forecast"

# Inspect an API
python cli/apia.py inspect open-meteo

# Generate agent prompt for a task
python cli/apia.py build-prompt "get current temperature in Berlin"

# Or as a module:
python -m apia search weather
python -m apia inspect stripe
```

## Schema reference

Full schema: [`schema/apia-1.0.schema.json`](schema/apia-1.0.schema.json)

Detailed comparison with OpenAPI: [`docs/openapi-vs-apia.md`](docs/openapi-vs-apia.md)

## License

MIT. All contributions are accepted under the same license.
