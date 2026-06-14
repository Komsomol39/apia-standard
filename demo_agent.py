#!/usr/bin/env python3
"""
APIA Demo Agent — discovers and uses APIs from the APIA registry.

Run:
    pip install anthropic requests
    export ANTHROPIC_API_KEY=sk-ant-...
    python demo_agent.py
"""

import json, os, urllib.request
import anthropic

REGISTRY_URL = "https://raw.githubusercontent.com/Komsomol39/apia-standard/main/registry.json"


def load_registry() -> list[dict]:
    """Load the APIA registry (257 APIs) from GitHub."""
    with urllib.request.urlopen(REGISTRY_URL) as r:
        return json.loads(r.read())["manifests"]


def find_apis(task: str, registry: list[dict], top_k: int = 3) -> list[dict]:
    """
    Find the most relevant APIs for a given task by matching against
    description_for_ai and capability intent phrases.
    """
    task_lower = task.lower()
    scored = []

    for m in registry:
        score = 0
        # Match service description
        if any(word in m["description_for_ai"].lower() for word in task_lower.split()):
            score += 1
        # Match capability intents (stronger signal)
        for cap in m["capabilities"]:
            if any(task_lower in intent.lower() or intent.lower() in task_lower
                   for intent in cap["intent"]):
                score += 3
                break
        if score > 0:
            scored.append((score, m))

    scored.sort(key=lambda x: -x[0])
    return [m for _, m in scored[:top_k]]


def build_system_prompt(apis: list[dict]) -> str:
    """Build a system prompt containing selected API manifests."""
    prompt = """You are an AI agent with access to external APIs via the APIA standard.

When the user asks something, identify which API capability to use, explain your reasoning,
then show the exact API call (method, URL, params).

Available APIs:
"""
    for api in apis:
        prompt += f"""
─── {api["name"]} ───
{api["description_for_ai"]}
Auth: {api["auth_type"]} | Cost: {api.get("cost", "unknown")}

Capabilities:"""
        for cap in api["capabilities"]:
            prompt += f"""
  [{cap["id"]}]  {cap["endpoint"]}
  When: {cap["description_for_ai"]}
  Intent: {", ".join(cap["intent"][:4])}"""

        if api.get("agent_hints"):
            prompt += "\n\nHints:"
            for k, v in list(api["agent_hints"].items())[:3]:
                prompt += f"\n  • {k}: {v}"

    prompt += """

Format your response as:
1. **API chosen**: <name> → <capability_id>
2. **Why**: <one sentence>
3. **Call**:
```
METHOD URL
Headers: ...
Body: {...}
```
4. **Expected response**: <key fields>
"""
    return prompt


def run_agent(task: str, registry: list[dict]) -> str:
    """Run the APIA agent for a given task."""
    print(f"\n🔍 Task: {task}")

    # Discover relevant APIs
    apis = find_apis(task, registry)
    if not apis:
        return "No matching APIs found in registry."

    print(f"📚 Found {len(apis)} relevant APIs: {[a['name'] for a in apis]}")

    # Build prompt and call Claude
    client = anthropic.Anthropic()
    system = build_system_prompt(apis)

    response = client.messages.create(
        model="claude-haiku-4-5",
        max_tokens=1024,
        system=system,
        messages=[{"role": "user", "content": task}]
    )
    return response.content[0].text


def main():
    print("Loading APIA registry...")
    registry = load_registry()
    print(f"✅ Loaded {len(registry)} APIs across "
          f"{len(set(m['category'] for m in registry))} categories\n")

    # Example tasks
    tasks = [
        "Send a Telegram message to user 12345 saying Hello",
        "What is the weather in Berlin right now?",
        "Track DHL shipment 1234567890",
        "Get the current Bitcoin price in USD",
        "Find Python developer jobs in Moscow",
    ]

    for task in tasks:
        result = run_agent(task, registry)
        print(f"\n{'='*60}")
        print(result)
        print()


if __name__ == "__main__":
    main()
