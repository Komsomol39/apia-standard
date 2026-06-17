# APIA Quick Guide

Five things you can do right now.

---

## 1. Install

```bash
pip install apia
```

---

## 2. Search APIs by what you want to do

```bash
apia search "get weather forecast"
apia search "send sms"
apia search "find flights"
apia search "translate text"
```

Returns a ranked list of matching APIs from the registry.

---

## 3. Inspect any API

```bash
apia inspect open-meteo
apia inspect stripe
apia inspect telegram-bot
```

Shows capabilities, endpoints, auth requirements — everything an agent needs.

---

## 4. Build an agent prompt

```bash
apia build-prompt "what is the weather in Tokyo?"
```

Outputs a ready-to-use LLM prompt with the top matching APIs, their endpoints, and parameters. Paste it into your agent's system prompt or tool description.

---

## 5. Run a real end-to-end example

No API key needed:

```bash
python examples/weather_demo.py
```

This script:
1. Loads the `open-meteo` manifest from the registry
2. Matches intent "current weather" to a capability
3. Builds the HTTP request from the manifest schema
4. Calls the real API
5. Prints the result

Expected output:
```
Weather in Berlin:
Temperature: 18.4°C
Wind speed:  12.3 km/h
Conditions:  partly cloudy
```

---

## Use APIA in your agent

```python
import json, urllib.request

# Load registry
with urllib.request.urlopen(
    "https://raw.githubusercontent.com/Komsomol39/apia-standard/main/registry.json"
) as r:
    registry = json.loads(r.read())

# Find APIs that match a task
task = "send a telegram message"
matches = [
    m for m in registry["manifests"]
    if any(task in cap.get("intent", [])
           for cap in m.get("capabilities", []))
]

# Load the best manifest
api_id = matches[0]["id"]
with urllib.request.urlopen(
    f"https://raw.githubusercontent.com/Komsomol39/apia-standard/main/manifests/{api_id}/apia.json"
) as r:
    manifest = json.loads(r.read())

# Check auth
auth = manifest["auth"]
print(f"Auth type: {auth['type']}")
print(f"Free to use: {auth['anonymous_access']}")
if not auth["anonymous_access"]:
    print(f"How to get key: {auth['how_to_get']}")

# Get the right capability
cap = manifest["capabilities"][0]
print(f"\nEndpoint: {cap['endpoint']}")
print(f"Required params: {[k for k,v in cap['input'].items() if v.get('required')]}")
```

---

## Add an API to the registry

```bash
# From an OpenAPI spec
python tools/openapi2apia.py https://api.example.com/openapi.json --id my-api

# Validate
apia validate manifests/my-api/apia.json

# Submit PR
git checkout -b add-my-api
git add manifests/my-api/
git commit -m "feat(my-api): add My API manifest"
git push origin add-my-api
```

CI validates automatically. PR review within 7 days.

---

## Registry at a glance

| | |
|---|---|
| Manifests | 260 |
| Categories | 26 |
| Capabilities | 1403 |
| Free APIs (no auth) | ~40 |
| Endpoint alive rate | 97.4% |

Full list: [registry.json](registry.json)
