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
    "description_for_ai": "Largest Russian job board. Use to search vacancies by keyword, city or coordinates.",
    "category": "employment",
    "geo": ["RU", "BY", "KZ"]
  },
  "capabilities": [
    {
      "id": "search_vacancies",
      "description_for_ai": "Search job vacancies by keyword and geolocation. Use for 'find Python developer jobs near me'.",
      "intent": ["find job", "vacancies nearby", "looking for work"],
      "endpoint": "GET https://api.hh.ru/vacancies",
      "realtime": true,
      "requires_auth": false
    }
  ],
  "agent_hints": {
    "geo_flow": "If user says 'near me' — pass lat/lng. If user names a city — call get_areas first."
  }
}
```

---

## Registry

### 🌍 Global APIs

| Service | Category | Cap. | Auth | API Ver. | Docs | Status |
|---|---|---|---|---|---|---|
| [OpenWeatherMap](manifests/openweathermap/apia.json) | Weather | 3 | API Key | v2.5 | [docs](https://openweathermap.org/api) | ✅ Ready |
| [Google Maps](manifests/google-maps/apia.json) | Maps/Geocoding | 3 | API Key | v3 | [docs](https://developers.google.com/maps) | ✅ Ready |
| [GitHub API](manifests/github/apia.json) | Dev Tools | 4 | Token/Anon | v3 | [docs](https://docs.github.com/en/rest) | ✅ Ready |
| [Twilio](manifests/twilio/apia.json) | Communications | 2 | Basic Auth | 2010-04-01 | [docs](https://twilio.com/docs/sms/api) | ✅ Ready |
| [Stripe](manifests/stripe/apia.json) | Payments | 3 | Bearer | v1 | [docs](https://stripe.com/docs/api) | ✅ Ready |

### 🇷🇺 Russia

| Service | Category | Cap. | Auth | API Ver. | Docs | Status |
|---|---|---|---|---|---|---|
| [hh.ru](manifests/hh-ru/apia.json) | Employment | 5 | OAuth2/Anon | v1 | [docs](https://github.com/hhru/api) | ✅ Ready |
| [SuperJob](manifests/superjob/apia.json) | Employment | 4 | API Key/Anon | v2.0 | [docs](https://api.superjob.ru/) | ✅ Ready |
| [SuperJob Resumes](manifests/superjob-resumes/apia.json) | Resumes | 2 | OAuth2 | v2.0 | [docs](https://api.superjob.ru/) | ✅ Ready |
| [Авито.Работа](manifests/avito-jobs/apia.json) | Employment | 2 | OAuth2 | v1 | [docs](https://developers.avito.ru/api-catalog/job/documentation) | ⚠️ Partial |
| [trudvsem.ru](manifests/trudvsem/apia.json) | Employment Gov | 4 | None | v1 | [docs](https://trudvsem.ru/opendata/api) | ✅ Ready |
| [Яндекс.Расписания](manifests/yandex-rasp/apia.json) | Transport | 5 | API Key | v3.0 | [docs](https://yandex.ru/dev/rasp/doc/ru/) | ✅ Ready |
| [Яндекс.Карты](manifests/yandex-maps/apia.json) | Maps/Geocoding | 3 | API Key | v1.x | [docs](https://yandex.ru/dev/maps/) | ✅ Ready |
| [2GIS](manifests/2gis/apia.json) | Maps/POI | 4 | API Key | v3.0 | [docs](https://docs.2gis.com/en/api/search/overview) | ✅ Ready |
| [data.mos.ru](manifests/data-mos-ru/apia.json) | City Data | 3 | API Key | v1 | [docs](https://data.mos.ru/developers/documentation) | ✅ Ready |
| [ЕГРЮЛ/ФНС](manifests/egrul-fns/apia.json) | Business Registry | 2 | API Key | v1 | [docs](https://api-fns.ru/) | ✅ Ready |
| [ФИАС/ГАР](manifests/fias/apia.json) | Address Registry | 2 | None | v1 | [docs](https://fias.nalog.ru/) | ✅ Ready |
| [Госуслуги](manifests/gosuslugi/apia.json) | Gov Services | 1 | ЕСИА | v1 | [docs](https://partners.gosuslugi.ru/catalog/api_for_gu) | ⚠️ Partial |

### 🇧🇾🇰🇿 CIS

| Service | Category | Cap. | Auth | API Ver. | Docs | Status |
|---|---|---|---|---|---|---|
| [hh.kz](manifests/hh-kz/apia.json) | Employment KZ | 3 | OAuth2/Anon | v1 | [docs](https://dev.hh.kz/) | ✅ Ready |
| [hh.by](manifests/hh-by/apia.json) | Employment BY | 3 | OAuth2/Anon | v1 | [docs](https://github.com/hhru/api) | ✅ Ready |
| [2GIS CIS](manifests/2gis-cis/apia.json) | Maps/POI BY+KZ | 2 | API Key | v3.0 | [docs](https://docs.2gis.com/en/api/search/overview) | ✅ Ready |

> ⚠️ Partial = manifest exists with docs links, needs contributor to complete

---

## Compatibility

| Standard | Relationship |
|---|---|
| **MCP** (Anthropic) | APIA manifests → MCP tool definitions |
| **OpenAPI / Swagger** | APIA references OpenAPI specs |
| **OpenClaw skills** | APIA manifests → `SKILL.md` |

---

## How to Contribute

1. Fork this repository
2. Create `manifests/{service-id}/apia.json`
3. Follow the [HH.ru example](manifests/hh-ru/apia.json)
4. Write `description_for_ai` for LLMs, not developers
5. Open a Pull Request

### ❌ Bad vs ✅ Good

❌ *"Endpoint for retrieving a paginated list of vacancies"*

✅ *"Search job vacancies by keyword. Use when user says 'find work nearby'"*

---

- 💬 [Discussions](../../discussions) · 🐛 [Issues](../../issues) · 🌐 OpenClaw Discord `#showcase`

**APIA is open source · 20 manifests · 4 languages · Started June 2026**