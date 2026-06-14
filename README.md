# APIA — API for AI Agents

> **Open standard for describing public APIs in a format that AI agents understand natively.**

🇷🇺 [Русский](docs/README.ru.md) · 🇨🇳 [中文](docs/README.zh.md) · 🇩🇪 [Deutsch](docs/README.de.md)

Inspired by what SOAP did for enterprise contracts in the 2000s — built for the AI agent era.

---

## The Problem

An AI agent helping a user find a job near their location, check a bus schedule, and find an open pharmacy needs to separately learn each API. Every service has its own format, auth, and pagination. There is no shared contract.

**APIA solves this with a single `apia.json` manifest** that tells any AI agent:
- 🧠 **What** the service can do (written for LLMs, not developers)
- 🌍 **Where** it works (geography, language)
- 🔑 **How** to authenticate
- ⚡ **Whether** data is realtime or cached
- 💡 **Hints** on how to use correctly in real scenarios

---

## Quick Example

```json
{
  "apia": "1.0",
  "service": {
    "id": "openweathermap",
    "description_for_ai": "Get current weather and forecasts for any city or coordinates worldwide.",
    "category": "weather",
    "geo": ["GLOBAL"]
  },
  "capabilities": [{
    "id": "current_weather",
    "description_for_ai": "Get current weather. Use for 'what's the weather now', 'is it raining in London'.",
    "intent": ["current weather", "temperature now", "is it raining"],
    "endpoint": "GET https://api.openweathermap.org/data/2.5/weather",
    "realtime": true
  }]
}
```

---

## Registry — 25 Manifests

### 🌍 Global APIs

| Service | Category | Cap. | Auth | Docs | Status |
|---|---|---|---|---|---|
| [OpenWeatherMap](manifests/openweathermap/apia.json) | Weather | 3 | API Key | [docs](https://openweathermap.org/api) | ✅ |
| [Google Maps](manifests/google-maps/apia.json) | Maps/Geocoding | 3 | API Key | [docs](https://developers.google.com/maps) | ✅ |
| [GitHub API](manifests/github/apia.json) | Dev Tools | 4 | Token/Anon | [docs](https://docs.github.com/en/rest) | ✅ |
| [Twilio](manifests/twilio/apia.json) | SMS/WhatsApp | 2 | Basic Auth | [docs](https://twilio.com/docs/sms/api) | ✅ |
| [Stripe](manifests/stripe/apia.json) | Payments | 3 | Bearer | [docs](https://stripe.com/docs/api) | ✅ |
| [DeepL](manifests/deepl/apia.json) | Translation | 2 | API Key | [docs](https://www.deepl.com/docs-api) | ✅ |
| [ExchangeRate-API](manifests/exchangerate-api/apia.json) | Currency | 2 | API Key | [docs](https://www.exchangerate-api.com/docs) | ✅ |
| [Spotify](manifests/spotify/apia.json) | Music | 3 | OAuth2 | [docs](https://developer.spotify.com/documentation/web-api) | ✅ |
| [Wikipedia](manifests/wikipedia/apia.json) | Knowledge | 3 | None | [docs](https://en.wikipedia.org/api/rest_v1/) | ✅ |
| [Amadeus](manifests/amadeus/apia.json) | Flights/Travel | 3 | OAuth2 | [docs](https://developers.amadeus.com/self-service) | ✅ |

### 🇷🇺 Russia

| Service | Category | Cap. | Auth | Docs | Status |
|---|---|---|---|---|---|
| [hh.ru](manifests/hh-ru/apia.json) | Employment | 5 | OAuth2/Anon | [docs](https://github.com/hhru/api) | ✅ |
| [SuperJob](manifests/superjob/apia.json) | Employment | 4 | API Key/Anon | [docs](https://api.superjob.ru/) | ✅ |
| [SuperJob Resumes](manifests/superjob-resumes/apia.json) | Resumes | 2 | OAuth2 | [docs](https://api.superjob.ru/) | ✅ |
| [Авито.Работа](manifests/avito-jobs/apia.json) | Employment | 2 | OAuth2 | [docs](https://developers.avito.ru/api-catalog/job/documentation) | ⚠️ |
| [trudvsem.ru](manifests/trudvsem/apia.json) | Employment Gov | 4 | None | [docs](https://trudvsem.ru/opendata/api) | ✅ |
| [Яндекс.Расписания](manifests/yandex-rasp/apia.json) | Transport | 5 | API Key | [docs](https://yandex.ru/dev/rasp/doc/ru/) | ✅ |
| [Яндекс.Карты](manifests/yandex-maps/apia.json) | Maps/Geocoding | 3 | API Key | [docs](https://yandex.ru/dev/maps/) | ✅ |
| [2GIS](manifests/2gis/apia.json) | Maps/POI | 4 | API Key | [docs](https://docs.2gis.com/en/api/search/overview) | ✅ |
| [data.mos.ru](manifests/data-mos-ru/apia.json) | City Data | 3 | API Key | [docs](https://data.mos.ru/developers/documentation) | ✅ |
| [ЕГРЮЛ/ФНС](manifests/egrul-fns/apia.json) | Business Registry | 2 | API Key | [docs](https://api-fns.ru/) | ✅ |
| [ФИАС/ГАР](manifests/fias/apia.json) | Address Registry | 2 | None | [docs](https://fias.nalog.ru/) | ✅ |
| [Госуслуги](manifests/gosuslugi/apia.json) | Gov Services | 1 | ЕСИА | [docs](https://partners.gosuslugi.ru/catalog/api_for_gu) | ⚠️ |

### 🇧🇾🇰🇿 CIS

| Service | Category | Cap. | Auth | Docs | Status |
|---|---|---|---|---|---|
| [hh.kz](manifests/hh-kz/apia.json) | Employment KZ | 3 | OAuth2/Anon | [docs](https://dev.hh.kz/) | ✅ |
| [hh.by](manifests/hh-by/apia.json) | Employment BY | 3 | OAuth2/Anon | [docs](https://github.com/hhru/api) | ✅ |
| [2GIS CIS](manifests/2gis-cis/apia.json) | Maps/POI BY+KZ | 2 | API Key | [docs](https://docs.2gis.com/en/api/search/overview) | ✅ |

> ⚠️ Partial = needs contributor · ✅ Ready to use

---

## Compatibility

| Standard | Relationship |
|---|---|
| **MCP** (Anthropic) | APIA → MCP tool definitions |
| **OpenAPI** | APIA references OpenAPI specs |
| **OpenClaw skills** | APIA → `SKILL.md` |

---

## Contribute

1. Fork → create `manifests/{id}/apia.json`
2. Follow the [HH.ru example](manifests/hh-ru/apia.json)
3. Write `description_for_ai` for LLMs, not developers
4. Pull Request

❌ *"Endpoint for retrieving paginated vacancies"*
✅ *"Search jobs by keyword. Use when user says 'find work nearby'"*

---

💬 [Discussions](../../discussions) · 🐛 [Issues](../../issues) · 🌐 OpenClaw `#showcase`

**25 manifests · 4 languages · Open source · Started June 2026**