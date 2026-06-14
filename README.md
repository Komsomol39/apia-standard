# APIA — API for AI Agents

> **The open standard for describing any public API in a format AI agents natively understand.**

🇷🇺 [Русский](docs/README.ru.md) · 🇨🇳 [中文](docs/README.zh.md) · 🇩🇪 [Deutsch](docs/README.de.md)

---

## Why APIA Exists

Every public API speaks its own language. An AI agent trying to help a user find a job, check a flight, or convert currency must separately learn each service's format, auth, and quirks. There is no shared contract.

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
    "description_for_ai": "Current conditions for a city or coordinates. Use for 'what's the weather', 'is it raining in Tokyo', 'погода сейчас'.",
    "intent": ["current weather", "temperature now", "is it raining", "погода сейчас"],
    "endpoint": "GET https://api.openweathermap.org/data/2.5/weather",
    "realtime": true
  }],
  "agent_hints": {
    "tip": "Prefer lat/lon over city name — city names are ambiguous across countries."
  }
}
```

The key difference from OpenAPI: `description_for_ai` and `intent` are written **for LLMs**, not developers.

---

## Any API. Any Category. Any Country.

We welcome manifests for **any public API in the world**:

| Already in registry | Still waiting |
|---|---|
| Weather, Maps, Jobs | Social media posting |
| Payments, Music | Healthcare, IoT |
| Translation, Currency | E-commerce, Legal |
| Flights, Knowledge | Agriculture, Energy |
| Gaming, Messaging | And everything else |

If it has a public API and an AI agent could use it — it belongs here.

---

## Registry — 31 Manifests

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
| [Steam](manifests/steam/apia.json) | Gaming | [→](https://steamcommunity.com/dev) |
| [Reddit](manifests/reddit/apia.json) | Social / Discussion | [→](https://www.reddit.com/dev/api) |
| [Discord](manifests/discord/apia.json) | Social / Gaming | [→](https://discord.com/developers/docs) |
| [Telegram Bot](manifests/telegram-bot/apia.json) | Messaging | [→](https://core.telegram.org/bots/api) |
| [LinkedIn](manifests/linkedin/apia.json) | Professional Network | [→](https://learn.microsoft.com/en-us/linkedin/) |

### 🇷🇺 Russia

| Service | Category | Docs |
|---|---|---|
| [VK](manifests/vk/apia.json) | Social Media | [→](https://dev.vk.com/ru/api/overview) |
| [hh.ru](manifests/hh-ru/apia.json) | Employment | [→](https://github.com/hhru/api) |
| [SuperJob](manifests/superjob/apia.json) | Employment | [→](https://api.superjob.ru/) |
| [SuperJob Resumes](manifests/superjob-resumes/apia.json) | Resumes | [→](https://api.superjob.ru/) |
| [Авито.Работа](manifests/avito-jobs/apia.json) | Employment | [→](https://developers.avito.ru/api-catalog/job/documentation) |
| [trudvsem.ru](manifests/trudvsem/apia.json) | Employment Gov | [→](https://trudvsem.ru/opendata/api) |
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

### Adding a manifest

```
Fork → create manifests/{id}/apia.json → Pull Request
↓
Auto-validation (JSON Schema) runs immediately
↓
3 × 👍 from the community → auto-merged
```

Maintainers can only block for policy violations.

### Keeping manifests fresh

Every manifest has `last_verified`. A monthly GitHub Action pings each endpoint and opens an Issue if something breaks. Mark outdated manifests as `deprecated`.

### Propose what to add next

Use [Discussions → Ideas](../../discussions/categories/ideas) to propose APIs. Upvoted ideas get prioritized. Comment "I'll write this" to claim it for 2 weeks.

### Quality tiers

| Tier | Meaning |
|---|---|
| ✅ Verified | Tested, fields confirmed, agent_hints written |
| 🔶 Draft | Structure correct, not fully tested |
| ⚠️ Partial | Stub with docs links — needs contributor |
| ❌ Deprecated | API shut down or changed |

---

## Compatibility

| Standard | Relationship |
|---|---|
| **MCP** (Anthropic) | APIA → MCP tool definitions |
| **OpenAPI / Swagger** | APIA adds LLM layer on top of OpenAPI |
| **OpenClaw skills** | APIA → `SKILL.md` auto-conversion |

---

## Contribute

```bash
git clone https://github.com/Komsomol39/apia-standard
cp manifests/hh-ru/apia.json manifests/your-api/apia.json
# edit it
git commit -m "feat: add YourAPI manifest"
# open Pull Request
```

Read [CONTRIBUTING.md](CONTRIBUTING.md) for the full guide on writing great manifests.

---

💬 [Discussions](../../discussions) · 🐛 [Issues](../../issues) · 🌐 OpenClaw Discord `#showcase`

**APIA is open source · Not affiliated with any API provider**

*31 manifests · 4 languages · Started June 2026*