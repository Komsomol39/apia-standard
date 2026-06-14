# APIA — API for AI Agents

> **The open standard for describing any public API in a format AI agents natively understand.**

🇷🇺 [Русский](docs/README.ru.md) · 🇨🇳 [中文](docs/README.zh.md) · 🇩🇪 [Deutsch](docs/README.de.md)

---

## Why APIA Exists

Every public API speaks its own language. An AI agent trying to help a user find a job, check a flight, convert currency, or get the weather must separately learn each service's format, auth scheme, and quirks. There is no shared contract.

**APIA is that contract.** One file — `apia.json` — tells any AI agent everything it needs:

```json
{
  "apia": "1.0",
  "service": {
    "id": "openweathermap",
    "description_for_ai": "Get current weather and forecasts for any location worldwide. Use when user asks about temperature, rain, or weekly forecast.",
    "category": "weather",
    "geo": ["GLOBAL"]
  },
  "capabilities": [{
    "id": "current_weather",
    "description_for_ai": "Current conditions for a city or coordinates. Use for 'what's the weather', 'is it raining in Tokyo', 'temperature in Moscow now'.",
    "intent": ["current weather", "temperature now", "is it raining", "погода сейчас"],
    "endpoint": "GET https://api.openweathermap.org/data/2.5/weather",
    "realtime": true,
    "requires_auth": false
  }],
  "agent_hints": {
    "coords_tip": "Prefer lat/lon over city name for accuracy — city names are ambiguous."
  }
}
```

The key insight: `description_for_ai` and `intent` are written **for LLMs**, not for developers. That's what makes APIA different from OpenAPI.

---

## Any API. Any Category. Any Country.

APIA is not limited to Russian services or any specific domain. We welcome manifests for **any public API in the world**:

| Already in registry | Want to see next |
|---|---|
| Weather, Maps, Jobs, Transport | Social media, E-commerce |
| Payments, Music, Translation | Healthcare, IoT |
| Gov data, Business registries | Agriculture, Energy |
| Flights, Currency, Knowledge | Legal, Education |

If it has a public API and an AI agent could use it — it belongs here.

---

## Registry

### 🌍 Global

| Service | Category | Docs |
|---|---|---|
| [OpenWeatherMap](manifests/openweathermap/apia.json) | Weather | [→](https://openweathermap.org/api) |
| [Google Maps](manifests/google-maps/apia.json) | Maps / Geocoding | [→](https://developers.google.com/maps) |
| [GitHub](manifests/github/apia.json) | Dev Tools | [→](https://docs.github.com/en/rest) |
| [Twilio](manifests/twilio/apia.json) | SMS / WhatsApp | [→](https://twilio.com/docs/sms/api) |
| [Stripe](manifests/stripe/apia.json) | Payments | [→](https://stripe.com/docs/api) |
| [DeepL](manifests/deepl/apia.json) | Translation | [→](https://www.deepl.com/docs-api) |
| [ExchangeRate-API](manifests/exchangerate-api/apia.json) | Currency | [→](https://www.exchangerate-api.com/docs) |
| [Spotify](manifests/spotify/apia.json) | Music | [→](https://developer.spotify.com/documentation/web-api) |
| [Wikipedia](manifests/wikipedia/apia.json) | Knowledge | [→](https://en.wikipedia.org/api/rest_v1/) |
| [Amadeus](manifests/amadeus/apia.json) | Flights / Travel | [→](https://developers.amadeus.com/self-service) |

### 🇷🇺 Russia

| Service | Category | Docs |
|---|---|---|
| [hh.ru](manifests/hh-ru/apia.json) | Employment | [→](https://github.com/hhru/api) |
| [SuperJob](manifests/superjob/apia.json) | Employment | [→](https://api.superjob.ru/) |
| [SuperJob Resumes](manifests/superjob-resumes/apia.json) | Resumes | [→](https://api.superjob.ru/) |
| [Авито.Работа](manifests/avito-jobs/apia.json) | Employment | [→](https://developers.avito.ru/api-catalog/job/documentation) |
| [trudvsem.ru](manifests/trudvsem/apia.json) | Employment (Gov) | [→](https://trudvsem.ru/opendata/api) |
| [Яндекс.Расписания](manifests/yandex-rasp/apia.json) | Transport | [→](https://yandex.ru/dev/rasp/doc/ru/) |
| [Яндекс.Карты](manifests/yandex-maps/apia.json) | Maps / Geocoding | [→](https://yandex.ru/dev/maps/) |
| [2GIS](manifests/2gis/apia.json) | Maps / POI | [→](https://docs.2gis.com/en/api/search/overview) |
| [data.mos.ru](manifests/data-mos-ru/apia.json) | City Data | [→](https://data.mos.ru/developers/documentation) |
| [ЕГРЮЛ / ФНС](manifests/egrul-fns/apia.json) | Business Registry | [→](https://api-fns.ru/) |
| [ФИАС / ГАР](manifests/fias/apia.json) | Address Registry | [→](https://fias.nalog.ru/) |
| [Госуслуги](manifests/gosuslugi/apia.json) | Gov Services | [→](https://partners.gosuslugi.ru/catalog/api_for_gu) |

### 🇧🇾🇰🇿 CIS

| Service | Category | Docs |
|---|---|---|
| [hh.kz](manifests/hh-kz/apia.json) | Employment KZ | [→](https://dev.hh.kz/) |
| [hh.by](manifests/hh-by/apia.json) | Employment BY | [→](https://github.com/hhru/api) |
| [2GIS CIS](manifests/2gis-cis/apia.json) | Maps / POI | [→](https://docs.2gis.com/en/api/search/overview) |

---

## How the Registry Works

### Adding a new manifest

Anyone can contribute. The process is designed to be fast and low-friction:

```
1. Fork → create manifests/{your-api-id}/apia.json
2. Open a Pull Request
3. GitHub Action auto-validates the JSON schema
4. Get 3+ 👍 from the community
5. Auto-merged into the registry
```

Maintainers can block a PR only for clear reasons: broken endpoint, incorrect data, duplicate, or policy violation.

### Keeping manifests up to date

Every manifest has a `last_verified` date. A monthly GitHub Action pings each endpoint and opens an Issue if it returns errors. The community can mark a manifest as `status: deprecated` when an API shuts down.

Manifest authors are encouraged to watch their files — GitHub will notify you of issues automatically.

### Voting on what to add next

Use [GitHub Discussions → Ideas](../../discussions/categories/ideas) to propose new APIs. The most upvoted ideas get prioritized by contributors. You can also claim an idea by commenting "I'll write this manifest" — that reserves it for 2 weeks.

### Manifest quality tiers

| Tier | Meaning |
|---|---|
| ✅ **Verified** | Endpoint tested, fields confirmed, agent_hints written |
| 🔶 **Draft** | Structure correct, not fully tested |
| ⚠️ **Partial** | Stub with docs links — needs contributor |
| ❌ **Deprecated** | API shut down or changed significantly |

---

## Compatibility

APIA works alongside existing standards — not replacing them:

| Standard | How APIA relates |
|---|---|
| **OpenAPI / Swagger** | APIA references existing OpenAPI specs; adds the LLM layer on top |
| **MCP** (Anthropic) | APIA manifests can auto-convert to MCP tool definitions |
| **OpenClaw skills** | APIA manifests convert to `SKILL.md` automatically |
| **JSON Schema** | APIA manifests are validated against a JSON Schema |

---

## Writing a Good Manifest

The most important fields are the ones written for AI agents, not humans.

### description_for_ai

❌ **Developer-speak:** *"REST endpoint returning paginated vacancy objects filtered by location parameters"*

✅ **Agent-speak:** *"Search job vacancies by keyword and location. Use when user says 'find me work nearby', 'Python developer jobs in Berlin', or 'remote positions with salary above 80k'"*

### intent

List the natural language phrases that should trigger this capability. Think about how real users speak — not API terminology.

```json
"intent": [
  "find job", "work near me", "job vacancies",
  "найти работу", "вакансии рядом", "ищу работу"
]
```

### agent_hints

Hard-won knowledge about how to use the API correctly. Format gotchas, flow recommendations, common mistakes.

```json
"agent_hints": {
  "geo_flow": "If user says 'near me' pass lat/lng. If user names a city, call get_areas first to resolve the ID.",
  "salary_tip": "Users say '80k' — convert to 80000 before passing to the API.",
  "coords_format": "This API uses lng,lat order — NOT lat,lng. Don't mix them up."
}
```

---

## Start Contributing

```bash
git clone https://github.com/Komsomol39/apia-standard
cp manifests/hh-ru/apia.json manifests/your-api/apia.json
# edit the file
git commit -m "feat: add YourAPI manifest"
git push && open a Pull Request
```

Not sure where to start? Check [open ideas in Discussions](../../discussions/categories/ideas) or pick an ⚠️ Partial manifest and complete it.

---

💬 [Discussions](../../discussions) · 🐛 [Issues](../../issues) · 🌐 OpenClaw Discord `#showcase`

**APIA is open source and not affiliated with any API provider.**

*25 manifests · 4 languages · Started June 2026*