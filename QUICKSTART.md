# APIA Quickstart — Using Manifests in Your AI Agent

5-minute guide to putting APIA to work.

---

## The Problem APIA Solves

An AI agent doesn't know which of 260 APIs to call for "track my DHL package" or "send a Telegram message". APIA gives each API a machine-readable manifest the agent can read and understand.

---

## Option 1 — Feed a manifest into a system prompt

The simplest approach. Load one manifest, give it to your LLM.

```python
import json, requests, anthropic

manifest = requests.get(
    "https://raw.githubusercontent.com/Komsomol39/apia-standard/main"
    "/manifests/openweathermap/apia.json"
).json()

client = anthropic.Anthropic()
response = client.messages.create(
    model="claude-haiku-4-5",
    max_tokens=1024,
    system=f"You have access to this API:\n{json.dumps(manifest, indent=2)}\n"
           "When asked, call the right endpoint and return the result.",
    messages=[{"role": "user", "content": "What is the weather in Tokyo?"}]
)
print(response.content[0].text)
```

---

## Option 2 — Discover APIs via registry.json

All 260 manifests indexed in one file. Search by intent, category, or geo.

```python
import json, requests

registry = requests.get(
    "https://raw.githubusercontent.com/Komsomol39/apia-standard/main/registry.json"
).json()

def find_api(task: str) -> list:
    task_lower = task.lower()
    results = []
    for m in registry["manifests"]:
        for cap in m["capabilities"]:
            if any(task_lower in i.lower() or i.lower() in task_lower
                   for i in cap["intent"]):
                results.append({
                    "api": m["name"],
                    "capability": cap["id"],
                    "endpoint": cap["endpoint"],
                    "manifest_url": m["manifest_url"]
                })
    return results

for r in find_api("send telegram message"):
    print(r["api"], "->", r["endpoint"])

# Filter by category
ai_apis = [m for m in registry["manifests"] if m["category"].startswith("ai_")]
print(f"AI APIs: {len(ai_apis)}")

# All free APIs available in Russia
free_ru = [m for m in registry["manifests"]
           if "RU" in m["geo"] and m["anonymous_access"]]
print(f"Free Russian APIs: {len(free_ru)}")
```

---

## Option 3 — Convert APIA capability to OpenAI function definition

```python
def apia_to_openai_tool(capability: dict) -> dict:
    params, required = {}, []
    for name, spec in capability.get("input", {}).items():
        params[name] = {
            "type": spec.get("type", "string"),
            "description": spec.get("description", "")
        }
        if spec.get("required"):
            required.append(name)
    return {
        "type": "function",
        "function": {
            "name": capability["id"],
            "description": capability["description_for_ai"],
            "parameters": {
                "type": "object",
                "properties": params,
                "required": required
            }
        }
    }

manifest = requests.get(
    "https://raw.githubusercontent.com/Komsomol39/apia-standard/main"
    "/manifests/stripe/apia.json"
).json()

openai_tools = [apia_to_openai_tool(cap) for cap in manifest["capabilities"]]
```

---

## Option 4 — Load many manifests, let the agent pick

```python
import json, requests

# Load manifests for a specific domain
CATEGORIES = ["payments", "logistics_shipping", "maps_geocoding"]

manifests = []
for m in registry["manifests"]:
    if m["category"] in CATEGORIES:
        full = requests.get(m["manifest_url"]).json()
        manifests.append(full)

# Give all manifests to the agent
system_prompt = "You have access to these APIs:\n"
for m in manifests:
    system_prompt += f"\n--- {m['service']['name']} ---\n"
    system_prompt += f"{m['service']['description_for_ai']}\n"
    for cap in m["capabilities"]:
        system_prompt += f"  [{cap['id']}] {cap['endpoint']}\n"
        system_prompt += f"    {cap['description_for_ai']}\n"
```

---

## Manifest Structure (reference)

```json
{
  "apia": "1.0",
  "service": {
    "id": "my-api",
    "description_for_ai": "What this does — written for LLMs, not developers",
    "category": "payments",
    "geo": ["GLOBAL"]
  },
  "auth": {
    "type": "apikey",
    "anonymous_access": false,
    "how_to_get": "Register at myapi.com -> API Keys",
    "cost": "Free: 1000 req/day"
  },
  "capabilities": [{
    "id": "do_something",
    "description_for_ai": "When and how to call this endpoint",
    "intent": ["user query phrase", "another phrase", "русская фраза"],
    "endpoint": "POST https://api.myapi.com/v1/action",
    "input": {
      "param": {
        "type": "string",
        "description": "What this parameter does",
        "required": true
      }
    },
    "output": {
      "type": "result",
      "fields": ["result.id", "result.value"]
    },
    "realtime": true,
    "requires_auth": true
  }],
  "agent_hints": {
    "tip": "Important thing AI agents should know"
  },
  "meta": {
    "apia_version": "1.0",
    "last_verified": "2026-06-14"
  }
}
```

---

## Add Your API

1. Fork the repository
2. `cp manifests/openweathermap/apia.json manifests/my-api/apia.json`
3. Edit the manifest
4. Open a Pull Request — JSON Schema validation runs automatically

See [CONTRIBUTING.md](CONTRIBUTING.md) for full guidelines and quality criteria.
