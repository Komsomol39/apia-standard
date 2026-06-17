# OpenAPI vs APIA

## TL;DR

Use OpenAPI to document your API for developers. Use APIA to describe it for AI agents.

They are not competitors — APIA can be generated from OpenAPI using `tools/openapi2apia.py`.

## Detailed comparison

### Descriptions

**OpenAPI:**
```yaml
summary: Get current weather
description: Returns current weather data for a location
```

**APIA:**
```json
"description_for_ai": "Get real-time weather conditions for any location by coordinates. Use this when a user asks about current temperature, wind, rain, or general weather conditions. Returns temperature in Celsius, wind speed in km/h, and a weather condition code."
```

APIA descriptions are written for LLMs — they include *when to use* the API, not just what it does.

### Discovery

**OpenAPI:** Agent must know the endpoint path in advance, or scan all paths.

**APIA:** Agent matches the task to `intent` phrases using embedding similarity:
```json
"intent": [
  "current weather",
  "weather right now",
  "temperature outside",
  "погода сейчас",
  "Wetter aktuell"
]
```

Multi-language intents allow agents to work across locales without translation.

### Auth guidance

**OpenAPI:**
```yaml
securitySchemes:
  ApiKeyAuth:
    type: apiKey
    in: header
    name: X-API-Key
```

**APIA:**
```json
"auth": {
  "type": "apiKey",
  "anonymous_access": false,
  "how_to_get": "Register at openweathermap.org — free tier: 1000 calls/day",
  "cost": "free / paid plans from $40/month"
}
```

The agent knows whether it can call without credentials, where to get a key, and what the cost is.

### Error handling

**OpenAPI:**
```yaml
responses:
  401:
    description: Unauthorized
  429:
    description: Too Many Requests
```

**APIA:**
```json
"agent_hints": {
  "rate_limiting": "Free tier: 60 calls/minute. On 429, wait 60 seconds.",
  "errors": "401 means invalid API key. 404 means location not found — try with coordinates instead of city name.",
  "pagination": "Use page and limit params. Max 100 results per page."
}
```

### Conversion

Convert any OpenAPI 3.x spec to APIA in seconds:

```bash
python tools/openapi2apia.py https://api.example.com/openapi.json --id my-api
```

The converter handles ~80% of the work. You complete the `description_for_ai`, `intent` phrases, and `agent_hints` manually.
