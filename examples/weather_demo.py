#!/usr/bin/env python3
"""
APIA end-to-end demo: weather in Berlin
1. Loads the open-meteo manifest from the registry
2. Matches intent "weather berlin" to a capability
3. Builds the HTTP request from the manifest
4. Calls the real API (no auth required)
5. Returns a human-readable answer

Run: python examples/weather_demo.py
"""
import json, urllib.request, sys
from pathlib import Path

def load_manifest(api_id):
    local = Path(f"manifests/{api_id}/apia.json")
    if local.exists():
        return json.loads(local.read_text())
    url = f"https://raw.githubusercontent.com/Komsomol39/apia-standard/main/manifests/{api_id}/apia.json"
    with urllib.request.urlopen(url) as r:
        return json.loads(r.read())

def find_capability(manifest, intent_query):
    query = intent_query.lower()
    best_score, best_cap = 0, None
    for cap in manifest.get("capabilities", []):
        score = 0
        for phrase in cap.get("intent", []):
            if query in phrase.lower():
                score += 3
            elif any(w in phrase.lower() for w in query.split()):
                score += 1
        if cap.get("description_for_ai","").lower().find(query) != -1:
            score += 1
        if score > best_score:
            best_score, best_cap = score, cap
    return best_cap

def call_api(capability, params):
    endpoint = capability["endpoint"]
    # Extract base URL (GET <url>)
    base_url = endpoint.split(" ")[-1]
    # Replace path params
    for k, v in params.items():
        base_url = base_url.replace(f"{{{k}}}", str(v))
    # Add query params
    query_str = "&".join(f"{k}={v}" for k, v in params.items()
                         if f"{{{k}}}" not in endpoint)
    if query_str:
        sep = "&" if "?" in base_url else "?"
        base_url = base_url + sep + query_str
    print(f"Calling: {base_url}")
    with urllib.request.urlopen(base_url) as r:
        return json.loads(r.read())

def main():
    print("="*60)
    print("APIA Demo: What is the weather in Berlin?")
    print("="*60)

    # Step 1: Load manifest
    print("\n[1] Loading open-meteo manifest...")
    manifest = load_manifest("open-meteo")
    svc = manifest["service"]
    print(f"    Loaded: {svc['name']} — {svc['description_for_ai'][:80]}")

    # Step 2: Find capability
    print("\n[2] Matching intent: 'current weather'...")
    cap = find_capability(manifest, "current weather")
    if not cap:
        sys.exit("No matching capability found")
    print(f"    Matched: [{cap['id']}] {cap['description_for_ai'][:80]}")

    # Step 3: Build request
    print("\n[3] Building request for Berlin (lat=52.52, lon=13.41)...")
    params = {
        "latitude": 52.52,
        "longitude": 13.41,
        "current": "temperature_2m,wind_speed_10m,weathercode",
        "timezone": "Europe/Berlin"
    }

    # Step 4: Call API
    print("\n[4] Calling API...")
    data = call_api(cap, params)

    # Step 5: Parse and display
    print("\n[5] Result:")
    current = data.get("current", {})
    temp = current.get("temperature_2m", "?")
    wind = current.get("wind_speed_10m", "?")
    code = current.get("weathercode", 0)

    weather_codes = {
        0: "clear sky", 1: "mainly clear", 2: "partly cloudy", 3: "overcast",
        45: "foggy", 51: "light drizzle", 61: "light rain", 71: "light snow",
        80: "rain showers", 95: "thunderstorm"
    }
    weather = weather_codes.get(code, f"code {code}")

    print(f"\n    Weather in Berlin:")
    print(f"    Temperature: {temp}°C")
    print(f"    Wind speed:  {wind} km/h")
    print(f"    Conditions:  {weather}")
    print(f"\n    Source: {svc['url']}")
    print(f"    Manifest: manifests/open-meteo/apia.json")
    print("\nDemo complete!")

if __name__ == "__main__":
    main()
