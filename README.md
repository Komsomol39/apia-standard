# APIA — API for AI Agents

> **Open standard for describing public APIs in a format that AI agents understand natively.**

🇷🇺 [Русский](docs/README.ru.md) · 🇨🇳 [中文](docs/README.zh.md) · 🇩🇪 [Deutsch](docs/README.de.md)

Inspired by what SOAP did for enterprise contracts in the 2000s — built for the AI agent era.

---

## The Problem

An AI agent helping a user find a job near their location, check a bus schedule, and find an open pharmacy needs to separately learn each API. Every service has its own format, its own auth, its own pagination. There is no shared contract.

**APIA solves this with a single `apia.json` manifest** — a machine-readable file that tells any AI agent:

- 🧠 **What** the service can do (written for LLMs, not developers)
- 🌍 **Where** it works (geography, language)
- 🔑 **How** to authenticate
- ⚡ **Whether** data is realtime or cached
- 💡 **Hints** on how to use the API correctly in real-world scenarios

---

## How It Works

```
User: "Find me a Python job near me with salary above 80k"
        ↓
Agent reads APIA registry
        ↓
Finds hh-ru → capability: search_vacancies
        ↓
Maps intent to API parameters:
  text="Python", lat=55.75, lng=37.61, salary=80000
        ↓
Calls HH.ru API → returns results
        ↓
Agent answers user
```

No hardcoded integration. No custom training. Just the manifest.

---

## Quick Example

```json
{
  "apia": "1.0",
  "service": {
    "id": "hh-ru",
    "name": "HeadHunter",
    "description_for_ai": "Largest Russian job board. Use to search vacancies by keyword, city or user coordinates. Returns salary, employer, schedule, remote status.",
    "category": "employment",
    "geo": ["RU", "BY", "KZ"]
  },
  "capabilities": [
    {
      "id": "search_vacancies",
      "description_for_ai": "Search job vacancies by keyword and geolocation. Use for requests like 'find Python developer jobs near me' or 'courier vacancies in Kazan with salary above 50000'.",
      "intent": ["find job", "vacancies nearby", "looking for work"],
      "endpoint": "GET https://api.hh.ru/vacancies",
      "realtime": true,
      "requires_auth": false
    }
  ],
  "agent_hints": {
    "geo_flow": "If user says 'near me' — pass lat/lng. If user names a city — call get_areas first to find area_id."
  }
}
```

Key difference from OpenAPI: `description_for_ai`, `intent` and `agent_hints` are written **for LLMs**, not for developers.

---

## Registry

| Service | Category | Capabilities | Auth | API Version | Last Verified | Status |
|---|---|---|---|---|---|---|
| [hh.ru](manifests/hh-ru/apia.json) | Employment | 5 | OAuth2 / Anonymous | v1 | 2026-06-14 | ✅ Ready |
| [SuperJob](manifests/superjob/apia.json) | Employment | 4 | API Key / Anonymous | v2.0 | 2026-06-14 | ✅ Ready |
| [trudvsem.ru](manifests/trudvsem/apia.json) | Employment (Gov) | 4 | None | v1 | 2026-06-14 | ✅ Ready |
| [Яндекс.Расписания](manifests/yandex-rasp/apia.json) | Transport | 5 | API Key | v3.0 | 2026-06-14 | ✅ Ready |
| [Яндекс.Карты](manifests/yandex-maps/apia.json) | Maps / Geocoding | 3 | API Key | v1.x | 2026-06-14 | ✅ Ready |
| [2GIS](manifests/2gis/apia.json) | Maps / POI | 4 | API Key | v3.0 | 2026-06-14 | ✅ Ready |
| [data.mos.ru](manifests/data-mos-ru/apia.json) | City Data (Moscow) | 3 | API Key | v1 | 2026-06-14 | ✅ Ready |
| SuperJob Resume | Employment | — | — | — | — | 🔜 Needs contributor |
| ЕГРЮЛ / ФНС | Business Registry | — | — | — | — | 🔜 Needs contributor |
| Госуслуги | Gov Services | — | — | — | — | 🔜 Needs contributor |
| ФИАС | Address Registry | — | — | — | — | 🔜 Needs contributor |
| hh.kz | Employment (KZ) | — | — | — | — | 🔜 Needs contributor |

---

## Compatibility

APIA works alongside existing standards — it doesn't replace them:

| Standard | Relationship |
|---|---|
| **MCP** (Anthropic) | APIA manifests can be auto-converted to MCP tool definitions |
| **OpenAPI / Swagger** | APIA references existing OpenAPI specs, not replaces them |
| **OpenClaw skills** | APIA manifests convert to `SKILL.md` automatically |

---

## How to Contribute

1. Fork this repository
2. Create folder `manifests/{service-id}/`
3. Add `apia.json` following the [HH.ru example](manifests/hh-ru/apia.json)
4. Key rule: write `description_for_ai` and `intent` as if explaining to an AI agent, not a developer
5. Open a Pull Request

### Writing description_for_ai

❌ **Bad:** *"Endpoint for retrieving a paginated list of vacancies with filtering"*

✅ **Good:** *"Search job vacancies by keyword and geolocation. Use when user says 'find work nearby' or 'Python developer jobs in Kazan'"*

---

## Discussions & Support

- 💬 [GitHub Discussions](../../discussions) — ideas and questions
- 🐛 [Issues](../../issues) — bugs and proposals
- 🌐 OpenClaw Discord — `#showcase` channel

---

**APIA is open source. Not affiliated with any API provider.**

*Started June 2026 as an initiative to standardize Russian public APIs for AI agents.*