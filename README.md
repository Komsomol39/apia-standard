# APIA — API for AI Agents

> **The open standard for describing any public API in a format AI agents natively understand.**

🇷🇺 [Русский](docs/README.ru.md) · 🇨🇳 [中文](docs/README.zh.md) · 🇩🇪 [Deutsch](docs/README.de.md)

---

## Why APIA Exists

Every public API speaks its own language. An AI agent must separately learn each service's format, auth, and quirks. There is no shared contract.

**APIA is that contract.** One `apia.json` file tells any AI agent everything it needs — written for LLMs, not developers.

```json
{
  "apia": "1.0",
  "service": {
    "id": "openweathermap",
    "description_for_ai": "Get weather for any location. Use when user asks about temperature, rain, or forecast.",
    "category": "weather", "geo": ["GLOBAL"]
  },
  "capabilities": [{
    "id": "current_weather",
    "description_for_ai": "Current conditions. Use for 'what is the weather', 'is it raining in Tokyo'.",
    "intent": ["current weather", "temperature now", "is it raining", "погода сейчас"],
    "endpoint": "GET https://api.openweathermap.org/data/2.5/weather",
    "realtime": true
  }]
}
```

---

## Registry — 97 Manifests

### 🤖 AI & LLMs

| Service | Category | Free Tier | Docs |
|---|---|---|---|
| [OpenAI](manifests/openai/apia.json) | LLM/Vision/TTS/Images | $5 credit | [→](https://platform.openai.com/docs) |
| [Anthropic Claude](manifests/anthropic/apia.json) | LLM/Vision | Free tier | [→](https://docs.anthropic.com) |
| [Google Gemini](manifests/google-gemini/apia.json) | LLM/Multimodal | 1500 req/day | [→](https://ai.google.dev/api) |
| [Mistral AI](manifests/mistral/apia.json) | LLM/Code | Free tier | [→](https://docs.mistral.ai) |
| [DeepSeek](manifests/deepseek/apia.json) | LLM/Reasoning | $5 credit | [→](https://platform.deepseek.com/docs) |
| [xAI Grok](manifests/xai-grok/apia.json) | LLM/Live Search | $25/month | [→](https://docs.x.ai/api) |
| [Stability AI](manifests/stability-ai/apia.json) | Image Generation | Credits | [→](https://platform.stability.ai/docs/api-reference) |
| [Replicate](manifests/replicate/apia.json) | 1000+ Models | Pay/sec | [→](https://replicate.com/docs) |
| [Hugging Face](manifests/huggingface/apia.json) | Open Models | Free tier | [→](https://huggingface.co/docs/api-inference) |
| [Together AI](manifests/together-ai/apia.json) | Open LLMs | $1 credit | [→](https://docs.together.ai) |
| [Groq](manifests/groq/apia.json) | Ultra-fast LLM | 6K tok/min | [→](https://console.groq.com/docs) |
| [Perplexity](manifests/perplexity/apia.json) | AI+Web Search | — | [→](https://docs.perplexity.ai) |
| [Cohere](manifests/cohere/apia.json) | LLM/Embed/Rerank | Trial key | [→](https://docs.cohere.com) |
| [ElevenLabs](manifests/elevenlabs/apia.json) | Text-to-Speech | 10K chars | [→](https://elevenlabs.io/docs/api-reference) |
| [AssemblyAI](manifests/assemblyai/apia.json) | Speech-to-Text | $50 credit | [→](https://www.assemblyai.com/docs) |
| [Pinecone](manifests/pinecone/apia.json) | Vector Database | 2GB free | [→](https://docs.pinecone.io) |
| [OpenAI Moderation](manifests/openai-moderation/apia.json) | Content Safety | **FREE** | [→](https://platform.openai.com/docs/guides/moderation) |

### 🌍 Global Services

| Service | Category | Free Tier | Docs |
|---|---|---|---|
| [Google Maps](manifests/google-maps/apia.json) | Maps/Geocoding | $200/month | [→](https://developers.google.com/maps) |
| [Mapbox](manifests/mapbox/apia.json) | Maps/Navigation | 200K loads | [→](https://docs.mapbox.com) |
| [HERE Maps](manifests/here-maps/apia.json) | Maps/Routing | 250K/month | [→](https://developer.here.com/documentation) |
| [Nominatim/OSM](manifests/openstreetmap-nominatim/apia.json) | Geocoding | **FREE** | [→](https://nominatim.org/release-docs/develop/api/Overview/) |
| [Foursquare](manifests/foursquare/apia.json) | Places/POI | 1000/day | [→](https://docs.foursquare.com) |
| [IPGeolocation](manifests/ipgeolocation/apia.json) | IP Location | 1000/day | [→](https://ipgeolocation.io/documentation) |
| [OpenWeatherMap](manifests/openweathermap/apia.json) | Weather | 1000/day | [→](https://openweathermap.org/api) |
| [Open-Meteo](manifests/open-meteo/apia.json) | Weather | **FREE** | [→](https://open-meteo.com/en/docs) |
| [GitHub](manifests/github/apia.json) | Dev Tools | 60 req/hr | [→](https://docs.github.com/en/rest) |
| [Stripe](manifests/stripe/apia.json) | Payments | No monthly | [→](https://stripe.com/docs/api) |
| [Twilio](manifests/twilio/apia.json) | SMS/WhatsApp | $15 trial | [→](https://twilio.com/docs/sms/api) |
| [DeepL](manifests/deepl/apia.json) | Translation | 500K chars | [→](https://www.deepl.com/docs-api) |
| [Google Translate](manifests/google-translate/apia.json) | Translation | 500K chars | [→](https://cloud.google.com/translate/docs) |
| [ExchangeRate-API](manifests/exchangerate-api/apia.json) | Currency | 1500/month | [→](https://www.exchangerate-api.com/docs) |
| [Spotify](manifests/spotify/apia.json) | Music | Free | [→](https://developer.spotify.com/documentation/web-api) |
| [Wikipedia](manifests/wikipedia/apia.json) | Knowledge | **FREE** | [→](https://en.wikipedia.org/api/rest_v1/) |
| [Amadeus](manifests/amadeus/apia.json) | Flights/Travel | 2000/month | [→](https://developers.amadeus.com/self-service) |
| [FlightAware](manifests/flightaware/apia.json) | Flight Tracking | 500/month | [→](https://flightaware.com/commercial/aeroapi/) |
| [AviationStack](manifests/aviationstack/apia.json) | Flight Data | 100/month | [→](https://aviationstack.com/documentation) |
| [OpenSky Network](manifests/opensky-network/apia.json) | Aircraft Tracking | **FREE** | [→](https://openskynetwork.github.io/opensky-api/) |
| [GTFS/Transitland](manifests/gtfs/apia.json) | Public Transit | Free tier | [→](https://www.transit.land/documentation) |
| [Uber](manifests/uber/apia.json) | Rideshare | Partnership | [→](https://developer.uber.com/docs) |
| [Steam](manifests/steam/apia.json) | Gaming | **FREE** | [→](https://steamcommunity.com/dev) |
| [TMDB](manifests/tmdb/apia.json) | Movies/TV | **FREE** | [→](https://developer.themoviedb.org/docs) |
| [YouTube](manifests/youtube/apia.json) | Video | 10K units/day | [→](https://developers.google.com/youtube/v3) |
| [Twitch](manifests/twitch/apia.json) | Game Streaming | Free | [→](https://dev.twitch.tv/docs/api/) |
| [NewsAPI](manifests/newsapi/apia.json) | News | 100/day | [→](https://newsapi.org/docs) |
| [Unsplash](manifests/unsplash/apia.json) | Stock Photos | 50/hr | [→](https://unsplash.com/documentation) |
| [Reddit](manifests/reddit/apia.json) | Social/Discussion | 100/min | [→](https://www.reddit.com/dev/api) |
| [Discord](manifests/discord/apia.json) | Social/Gaming | Free | [→](https://discord.com/developers/docs) |
| [Telegram Bot](manifests/telegram-bot/apia.json) | Messaging | **FREE** | [→](https://core.telegram.org/bots/api) |
| [LinkedIn](manifests/linkedin/apia.json) | Professional | 500/day | [→](https://learn.microsoft.com/en-us/linkedin/) |
| [Plaid](manifests/plaid/apia.json) | Banking/Finance | Sandbox free | [→](https://plaid.com/docs) |
| [Alpha Vantage](manifests/alpha-vantage/apia.json) | Stocks | 25/day | [→](https://www.alphavantage.co/documentation/) |
| [Coinbase](manifests/coinbase/apia.json) | Crypto | **FREE** (market) | [→](https://docs.cdp.coinbase.com) |
| [Binance](manifests/binance/apia.json) | Crypto | **FREE** (market) | [→](https://binance-docs.github.io/apidocs/) |
| [Shopify](manifests/shopify/apia.json) | E-commerce | Partner free | [→](https://shopify.dev/docs/api) |
| [WooCommerce](manifests/woocommerce/apia.json) | E-commerce | Free plugin | [→](https://woocommerce.github.io/woocommerce-rest-api-docs/) |
| [Yelp](manifests/yelp/apia.json) | Local Business | 500/day | [→](https://docs.developer.yelp.com) |
| [Google Books](manifests/google-books/apia.json) | Books | **FREE** | [→](https://developers.google.com/books/docs/v1/using) |
| [Wolfram Alpha](manifests/wolfram-alpha/apia.json) | Computation | 2000/month | [→](https://products.wolframalpha.com/api/documentation/) |
| [OpenFDA](manifests/open-fda/apia.json) | Drug/Medical Data | **FREE** | [→](https://open.fda.gov/apis/) |
| [WHO GHO](manifests/who/apia.json) | World Health Data | **FREE** | [→](https://www.who.int/data/gho/info/gho-odata-api) |
| [Fitbit](manifests/fitbit/apia.json) | Fitness Tracking | Free | [→](https://dev.fitbit.com/build/reference/web-api/) |
| [Nutritionix](manifests/nutritionix/apia.json) | Nutrition | 500/day | [→](https://developer.nutritionix.com/docs/v2) |
| [Infermedica](manifests/infermedica/apia.json) | Symptom Checker | Sandbox | [→](https://developer.infermedica.com/docs) |
| [Khan Academy](manifests/khan-academy/apia.json) | Education | **FREE** | [→](https://api-explorer.khanacademy.org/) |
| [Typeform](manifests/typeform/apia.json) | Forms/Surveys | 10 resp/month | [→](https://www.typeform.com/developers/) |
| [Duolingo](manifests/duolingo/apia.json) | Language Learning | **FREE** (unofficial) | [→](https://github.com/KartikTalwar/Duolingo) |
| [Strava](manifests/strava/apia.json) | Fitness/Running | 100/15min | [→](https://developers.strava.com/docs/reference/) |
| [Football-Data](manifests/football-data/apia.json) | Soccer | **FREE** | [→](https://docs.football-data.org) |
| [SportsData.io](manifests/sportsdata-io/apia.json) | Multi-Sport | Trial | [→](https://sportsdata.io/developers) |
| [Ergast F1](manifests/ergast-f1/apia.json) | Formula 1 | **FREE** | [→](https://ergast.com/mrd/) |
| [The Odds API](manifests/odds-api/apia.json) | Betting Odds | 500/month | [→](https://the-odds-api.com) |
| [PokéAPI](manifests/pokeapi/apia.json) | Pokémon | **FREE** | [→](https://pokeapi.co/docs/v2) |
| [Open Trivia DB](manifests/open-trivia/apia.json) | Trivia/Quiz | **FREE** | [→](https://opentdb.com/api_config.php) |
| [JokeAPI](manifests/jokeapi/apia.json) | Humor | **FREE** | [→](https://jokeapi.dev/#docs) |
| [RestCountries](manifests/rest-countries/apia.json) | Geography | **FREE** | [→](https://restcountries.com) |
| [Supabase](manifests/supabase/apia.json) | Backend/DB | 500MB free | [→](https://supabase.com/docs) |
| [Firebase](manifests/firebase/apia.json) | Mobile Backend | Generous free | [→](https://firebase.google.com/docs/reference/rest) |
| [SendGrid](manifests/sendgrid/apia.json) | Email | 100/day | [→](https://docs.sendgrid.com/api-reference) |
| [Mailchimp](manifests/mailchimp/apia.json) | Email Marketing | 500 contacts | [→](https://mailchimp.com/developer/marketing/api/) |
| [AWS S3](manifests/aws-s3/apia.json) | Cloud Storage | 5GB free | [→](https://docs.aws.amazon.com/s3) |

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
| [Яндекс.Карты](manifests/yandex-maps/apia.json) | Maps/Geocoding | [→](https://yandex.ru/dev/maps/) |
| [2GIS](manifests/2gis/apia.json) | Maps/POI | [→](https://docs.2gis.com/en/api/search/overview) |
| [data.mos.ru](manifests/data-mos-ru/apia.json) | City Data Moscow | [→](https://data.mos.ru/developers/documentation) |
| [ЕГРЮЛ/ФНС](manifests/egrul-fns/apia.json) | Business Registry | [→](https://api-fns.ru/) |
| [ФИАС/ГАР](manifests/fias/apia.json) | Address Registry | [→](https://fias.nalog.ru/) |
| [ЦБ РФ](manifests/cbrf/apia.json) | Currency/Finance | [→](https://www.cbr.ru/development/) |
| [Госуслуги](manifests/gosuslugi/apia.json) | Gov Services | [→](https://partners.gosuslugi.ru/catalog/api_for_gu) |

### 🇧🇾🇰🇿 CIS

| Service | Category | Docs |
|---|---|---|
| [hh.kz](manifests/hh-kz/apia.json) | Employment KZ | [→](https://dev.hh.kz/) |
| [hh.by](manifests/hh-by/apia.json) | Employment BY | [→](https://github.com/hhru/api) |
| [2GIS CIS](manifests/2gis-cis/apia.json) | Maps/POI BY+KZ | [→](https://docs.2gis.com/en/api/search/overview) |

---

## How the Registry Works

**Adding a manifest:**
```
Fork → create manifests/{id}/apia.json → Pull Request
→ Auto JSON Schema validation
→ 3 × 👍 from community → auto-merged
```

**Quality tiers:** ✅ Verified · 🔶 Draft · ⚠️ Partial · ❌ Deprecated

**Monthly health check** pings all endpoints and opens Issues if broken.

**Propose ideas** in [Discussions → Ideas](../../discussions/categories/ideas).

---

## Compatibility

| Standard | Relationship |
|---|---|
| **MCP** (Anthropic) | APIA → MCP tool definitions |
| **OpenAPI** | APIA adds LLM layer on top |
| **OpenClaw skills** | APIA → `SKILL.md` |

---

## Contribute

```bash
git clone https://github.com/Komsomol39/apia-standard
cp manifests/hh-ru/apia.json manifests/your-api/apia.json
# edit → Pull Request
```

Read [CONTRIBUTING.md](CONTRIBUTING.md) · See [ALL_APIS.md](docs/ALL_APIS.md) for 1945 more APIs to manifest

---

💬 [Discussions](../../discussions) · 🐛 [Issues](../../issues) · 🌐 OpenClaw Discord `#showcase`

**APIA is open source · Not affiliated with any API provider**

*97 manifests · 4 languages · Started June 2026*