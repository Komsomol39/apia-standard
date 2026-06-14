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
    "description_for_ai": "Get weather for any location. Use when user asks about temperature, rain, or forecast.",
    "category": "weather",
    "geo": ["GLOBAL"]
  },
  "capabilities": [{
    "id": "current_weather",
    "description_for_ai": "Current conditions. Use for 'what's the weather', 'is it raining in Tokyo', 'погода сейчас'.",
    "intent": ["current weather", "temperature now", "is it raining", "погода сейчас"],
    "endpoint": "GET https://api.openweathermap.org/data/2.5/weather",
    "realtime": true
  }]
}
```

The key difference from OpenAPI: `description_for_ai` and `intent` are written **for LLMs**, not developers.

---

## Any API. Any Category. Any Country.

We welcome manifests for **any public API in the world.**

---

## Registry — 37 Manifests

### 🤖 AI & LLMs

| Service | Category | Docs |
|---|---|---|
| [OpenAI](manifests/openai/apia.json) | LLM / Vision / TTS | [→](https://platform.openai.com/docs) |
| [Anthropic Claude](manifests/anthropic/apia.json) | LLM / Vision | [→](https://docs.anthropic.com) |
| [Google Gemini](manifests/google-gemini/apia.json) | LLM / Multimodal | [→](https://ai.google.dev/api) |
| [Mistral AI](manifests/mistral/apia.json) | LLM / Code | [→](https://docs.mistral.ai) |
| [DeepSeek](manifests/deepseek/apia.json) | LLM / Reasoning | [→](https://platform.deepseek.com/docs) |
| [xAI Grok](manifests/xai-grok/apia.json) | LLM / Live Search | [→](https://docs.x.ai/api) |

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

**Adding a manifest:**
```
Fork → create manifests/{id}/apia.json → Pull Request
→ Auto JSON Schema validation
→ 3 × 👍 from community → auto-merged
```

**Keeping fresh:** Monthly GitHub Action pings endpoints, opens Issues if broken.

**Propose ideas:** [Discussions → Ideas](../../discussions/categories/ideas) — upvoted ideas get prioritized.

**Quality tiers:** ✅ Verified · 🔶 Draft · ⚠️ Partial · ❌ Deprecated

---

## Compatibility

| Standard | Relationship |
|---|---|
| **MCP** (Anthropic) | APIA → MCP tool definitions |
| **OpenAPI** | APIA adds LLM layer on top |
| **OpenClaw skills** | APIA → `SKILL.md` auto-conversion |

---

## Contribute

```bash
git clone https://github.com/Komsomol39/apia-standard
cp manifests/hh-ru/apia.json manifests/your-api/apia.json
# edit → Pull Request
```

Read [CONTRIBUTING.md](CONTRIBUTING.md) for the full guide.

---

💬 [Discussions](../../discussions) · 🐛 [Issues](../../issues) · 🌐 OpenClaw Discord `#showcase`

**APIA is open source · Not affiliated with any API provider**

*37 manifests · 4 languages · Started June 2026*