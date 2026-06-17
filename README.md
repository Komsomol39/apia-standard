# APIA — API Standard for AI Agents

[![CI](https://github.com/Komsomol39/apia-standard/actions/workflows/ci.yml/badge.svg)](https://github.com/Komsomol39/apia-standard/actions)
[![Health](https://github.com/Komsomol39/apia-standard/actions/workflows/weekly-health.yml/badge.svg)](https://github.com/Komsomol39/apia-standard/actions/workflows/weekly-health.yml)
[![Manifests](https://img.shields.io/badge/manifests-260-blue)](registry.json)
[![Schema](https://img.shields.io/badge/schema-v1.0-orange)](schema/apia-1.0.schema.json)
[![PyPI](https://img.shields.io/pypi/v/apia?label=pip%20install%20apia&color=blue)](https://pypi.org/project/apia/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

APIA is an open standard for describing public APIs in a format that AI agents can natively understand and use.

## Why not OpenAPI?

OpenAPI is designed for *human developers*. It describes API structure, but not *how an AI agent should use it*:

| | OpenAPI | APIA |
|---|---|---|
| Target reader | Developer | AI agent / LLM |
| Description | Technical summary | `description_for_ai` — written for LLMs |
| Discovery | By endpoint path | By `intent` phrases in natural language |
| Auth guidance | Security scheme | `how_to_get`, `anonymous_access`, `cost` |
| Error handling | HTTP status codes | `agent_hints.errors` — what to do in practice |
| Pagination | Not standardized | `agent_hints.pagination` |
| Rate limits | Not standardized | `agent_hints.rate_limiting` |

## How an agent uses APIA

```python
# 1. Load registry
registry = fetch("https://raw.githubusercontent.com/Komsomol39/apia-standard/main/registry.json")

# 2. Match task to capability by intent
task = "what is the weather in Berlin?"
matches = search_by_intent(registry, task)
# -> open-meteo: get_current_weather (score: 0.95)

# 3. Load manifest
manifest = fetch(f"manifests/open-meteo/apia.json")

# 4. Check auth
if manifest.auth.anonymous_access:
    # no API key needed

# 5. Build and execute request
response = call(manifest.capabilities[0].endpoint, params={
    "latitude": 52.52, "longitude": 13.41,
    "current": "temperature_2m"
})
# -> {"current": {"temperature_2m": 18.4}}
```

## How a capability is selected

Each capability has `intent` — a list of natural language phrases:

```json
{
  "id": "get_current_weather",
  "description_for_ai": "Get current weather conditions for any location by coordinates.",
  "intent": [
    "current weather",
    "weather now",
    "temperature outside",
    "погода сейчас",
    "wie ist das Wetter"
  ],
  "endpoint": "GET https://api.open-meteo.com/v1/forecast"
}
```

The agent embeds the task and intent phrases, computes similarity, and selects the best match. The `description_for_ai` is used as additional context.

## How secrets are handled

APIA manifests never contain API keys. The `auth` block describes *how to obtain* credentials:

```json
{
  "auth": {
    "type": "apiKey",
    "anonymous_access": false,
    "how_to_get": "Register at openweathermap.org/api, free tier available",
    "cost": "free tier: 60 calls/min"
  }
}
```

The agent runtime is responsible for injecting credentials from a secret store. APIA defines the interface, not the secret.

## How API calls are executed safely

1. APIA manifests define `input` with types and required flags — the agent validates params before calling
2. `agent_hints.errors` tells the agent what HTTP errors mean in practice and what to do
3. `realtime: false` signals that cached data is acceptable — reduces unnecessary calls
4. `requires_auth: false` on individual capabilities means that specific endpoint is public

## How to verify an API is current

Every Monday at 06:00 UTC the CI pings all 257 `api_base` URLs and writes results to [`endpoint-health.json`](endpoint-health.json). If more than 30% are unreachable a GitHub Issue is opened automatically.

To run manually:

```bash
python tools/check_endpoints.py
# Results in endpoint-health.json
```

Sample output:
```
Checking 257 manifests...
Checking 201 unique endpoints (20 parallel)...
  [20/201] ✅ stripe: 200 45ms
  [40/201] ✅ openai: 200 112ms
  ...
Results: 189 alive, 12 dead, 56 skipped
Dead rate: 6.0%
OK: dead rate within threshold (30%)
```

Dead endpoints are flagged in `endpoint-health.json` with their error reason — DNS failure, timeout, HTTP error. Contributors are notified via GitHub Issues to update or remove stale manifests.

Each manifest also has `meta.last_verified` — the date a human last confirmed the API works correctly end-to-end (not just that the URL responds).

Each manifest has `meta.last_verified`. The CI checks that this field exists. Community contributors are expected to re-verify manifests periodically. Stale manifests (>1 year) will be flagged in the registry.

## Install

```bash
pip install apia
```

```bash
# CLI
apia search "weather forecast"
apia inspect open-meteo
apia build-prompt "get temperature in Berlin"
apia validate manifests/stripe/apia.json

# As module
python -m apia search weather
python -m apia inspect stripe
```

```python
# Python SDK
from apia import Registry

registry = Registry()
apis = registry.find("weather forecast")
print(apis[0].name)  # Open-Meteo API
```

Or use directly:

```bash
python cli/apia.py validate manifests/openweathermap/apia.json
python cli/apia.py search "weather berlin"
python cli/apia.py inspect open-meteo
python cli/apia.py build-prompt "find flights from Moscow to London"
```

## Add an API

**Option A — from OpenAPI spec:**
```bash
python tools/openapi2apia.py https://api.example.com/openapi.json --id my-api
# Review TODOs, then:
python cli/apia.py validate manifests/my-api/apia.json
```

**Option B — manually:**

```bash
mkdir manifests/my-api
cp manifests/open-meteo/apia.json manifests/my-api/apia.json
# Edit the file, then:
python cli/apia.py validate manifests/my-api/apia.json
```

Submit a PR. CI validates automatically.

## Run end-to-end demo

```bash
python examples/weather_demo.py
```

Real output:
```
Weather in Berlin:
Temperature: 18.4°C
Wind speed:  12.3 km/h
Conditions:  partly cloudy
```

## Repository structure

```
/cli
  apia.py              # validate, search, inspect, build-prompt

/tools
  openapi2apia.py      # Convert OpenAPI 3.x -> APIA manifest

/schema
  apia-1.0.schema.json # JSON Schema for validation

/manifests
  openweathermap/
    apia.json
  stripe/
    apia.json
  ... (257 total)

/tests
  test_manifests.py    # pytest suite — runs in CI

/examples
  weather_demo.py      # End-to-end demo: task -> manifest -> real API call

/docs
  standard.md          # Full schema reference
  openapi-vs-apia.md   # Comparison and migration guide

registry.json          # Index of all manifests
CHANGELOG.md           # Versioning and backward compatibility policy
```

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). All PRs are validated by CI.

## License

MIT
