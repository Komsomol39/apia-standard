# APIA — API for AI Agents

> **The open standard for describing any public API in a format AI agents natively understand.**

🇷🇺 [Русский](docs/README.ru.md) · 🇨🇳 [中文](docs/README.zh.md) · 🇩🇪 [Deutsch](docs/README.de.md)

---

## Why APIA Exists

Every public API speaks its own language. An AI agent must separately learn each service's format, auth, and quirks. **APIA is the shared contract** — one `apia.json` file written for LLMs, not developers.

```json
{
  "apia": "1.0",
  "service": { "id": "openweathermap", "description_for_ai": "Get weather for any location worldwide.", "geo": ["GLOBAL"] },
  "capabilities": [{ "id": "current_weather",
    "description_for_ai": "Current conditions. Use for 'what is the weather', 'is it raining in Tokyo'.",
    "intent": ["current weather", "temperature now", "погода сейчас"],
    "endpoint": "GET https://api.openweathermap.org/data/2.5/weather", "realtime": true }]
}
```

---

## Registry — 127 Manifests

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
| [Together AI](manifests/together-ai/apia.json) | Open LLMs cheap | $1 credit | [→](https://docs.together.ai) |
| [Groq](manifests/groq/apia.json) | Ultra-fast LLM | 6K tok/min | [→](https://console.groq.com/docs) |
| [Perplexity](manifests/perplexity/apia.json) | AI + Web Search | — | [→](https://docs.perplexity.ai) |
| [Cohere](manifests/cohere/apia.json) | LLM/Embed/Rerank | Trial key | [→](https://docs.cohere.com) |
| [ElevenLabs](manifests/elevenlabs/apia.json) | Text-to-Speech | 10K chars | [→](https://elevenlabs.io/docs/api-reference) |
| [AssemblyAI](manifests/assemblyai/apia.json) | Speech-to-Text | $50 credit | [→](https://www.assemblyai.com/docs) |
| [Pinecone](manifests/pinecone/apia.json) | Vector Database | 2GB free | [→](https://docs.pinecone.io) |
| [OpenAI Moderation](manifests/openai-moderation/apia.json) | Content Safety | **FREE** | [→](https://platform.openai.com/docs/guides/moderation) |

### 🌍 Maps & Location

| Service | Category | Free Tier | Docs |
|---|---|---|---|
| [Google Maps](manifests/google-maps/apia.json) | Maps/Geocoding | $200/month | [→](https://developers.google.com/maps) |
| [Mapbox](manifests/mapbox/apia.json) | Maps/Navigation | 200K loads | [→](https://docs.mapbox.com) |
| [HERE Maps](manifests/here-maps/apia.json) | Maps/Routing | 250K/month | [→](https://developer.here.com/documentation) |
| [Nominatim/OSM](manifests/openstreetmap-nominatim/apia.json) | Geocoding | **FREE** | [→](https://nominatim.org/release-docs/develop/api/Overview/) |
| [Foursquare](manifests/foursquare/apia.json) | Places/POI | 1000/day | [→](https://docs.foursquare.com) |
| [IPGeolocation](manifests/ipgeolocation/apia.json) | IP Location | 1000/day | [→](https://ipgeolocation.io/documentation) |
| [Яндекс.Карты](manifests/yandex-maps/apia.json) | Maps RU/CIS | Free tier | [→](https://yandex.ru/dev/maps/) |
| [2GIS](manifests/2gis/apia.json) | Maps/POI RU | Demo free | [→](https://docs.2gis.com/en/api/search/overview) |
| [2GIS CIS](manifests/2gis-cis/apia.json) | Maps BY+KZ | Demo free | [→](https://docs.2gis.com/en/api/search/overview) |

### ☁️ Weather & Environment

| Service | Category | Free Tier | Docs |
|---|---|---|---|
| [OpenWeatherMap](manifests/openweathermap/apia.json) | Weather | 1000/day | [→](https://openweathermap.org/api) |
| [Open-Meteo](manifests/open-meteo/apia.json) | Weather | **FREE** | [→](https://open-meteo.com/en/docs) |
| [OpenAQ](manifests/openaq/apia.json) | Air Quality | **FREE** | [→](https://docs.openaq.org) |
| [NASA APIs](manifests/nasa/apia.json) | Space/Earth | **FREE** | [→](https://api.nasa.gov/) |
| [Planet Labs](manifests/planet-labs/apia.json) | Satellite Imagery | Education free | [→](https://developers.planet.com/docs/apis/data/) |
| [GBIF](manifests/gbif/apia.json) | Biodiversity | **FREE** | [→](https://www.gbif.org/developer/summary) |
| [Carbon Interface](manifests/carbon-interface/apia.json) | Carbon Emissions | 100/month | [→](https://docs.carboninterface.com) |

### 💰 Finance & Payments

| Service | Category | Free Tier | Docs |
|---|---|---|---|
| [Stripe](manifests/stripe/apia.json) | Payments | No monthly | [→](https://stripe.com/docs/api) |
| [Plaid](manifests/plaid/apia.json) | Banking | Sandbox free | [→](https://plaid.com/docs) |
| [Alpha Vantage](manifests/alpha-vantage/apia.json) | Stocks | 25/day | [→](https://www.alphavantage.co/documentation/) |
| [Coinbase](manifests/coinbase/apia.json) | Crypto | **FREE** (market) | [→](https://docs.cdp.coinbase.com) |
| [Binance](manifests/binance/apia.json) | Crypto | **FREE** (market) | [→](https://binance-docs.github.io/apidocs/) |
| [ExchangeRate-API](manifests/exchangerate-api/apia.json) | Currency | 1500/month | [→](https://www.exchangerate-api.com/docs) |
| [ЦБ РФ](manifests/cbrf/apia.json) | Currency RU | **FREE** | [→](https://www.cbr.ru/development/) |

### ✈️ Transport & Travel

| Service | Category | Free Tier | Docs |
|---|---|---|---|
| [Amadeus](manifests/amadeus/apia.json) | Flights/Hotels | 2000/month | [→](https://developers.amadeus.com/self-service) |
| [FlightAware](manifests/flightaware/apia.json) | Flight Tracking | 500/month | [→](https://flightaware.com/commercial/aeroapi/) |
| [AviationStack](manifests/aviationstack/apia.json) | Flight Data | 100/month | [→](https://aviationstack.com/documentation) |
| [OpenSky Network](manifests/opensky-network/apia.json) | Aircraft Tracking | **FREE** | [→](https://openskynetwork.github.io/opensky-api/) |
| [GTFS/Transitland](manifests/gtfs/apia.json) | Public Transit | Free tier | [→](https://www.transit.land/documentation) |
| [Uber](manifests/uber/apia.json) | Rideshare | Partnership | [→](https://developer.uber.com/docs) |
| [Яндекс.Расписания](manifests/yandex-rasp/apia.json) | Transport RU | API key free | [→](https://yandex.ru/dev/rasp/doc/ru/) |

### 👥 Social & Communication

| Service | Category | Free Tier | Docs |
|---|---|---|---|
| [Telegram Bot](manifests/telegram-bot/apia.json) | Messaging | **FREE** | [→](https://core.telegram.org/bots/api) |
| [Discord](manifests/discord/apia.json) | Social/Gaming | Free | [→](https://discord.com/developers/docs) |
| [Slack API](manifests/slack-api/apia.json) | Team Comms | Free plan | [→](https://api.slack.com/methods) |
| [Reddit](manifests/reddit/apia.json) | Discussion | 100/min | [→](https://www.reddit.com/dev/api) |
| [VK](manifests/vk/apia.json) | Social RU | Free | [→](https://dev.vk.com/ru/api/overview) |
| [LinkedIn](manifests/linkedin/apia.json) | Professional | 500/day | [→](https://learn.microsoft.com/en-us/linkedin/) |
| [Twilio](manifests/twilio/apia.json) | SMS/WhatsApp | $15 trial | [→](https://twilio.com/docs/sms/api) |
| [SendGrid](manifests/sendgrid/apia.json) | Email | 100/day | [→](https://docs.sendgrid.com/api-reference) |
| [Mailchimp](manifests/mailchimp/apia.json) | Email Marketing | 500 contacts | [→](https://mailchimp.com/developer/marketing/api/) |

### 🎮 Entertainment & Media

| Service | Category | Free Tier | Docs |
|---|---|---|---|
| [Steam](manifests/steam/apia.json) | Gaming | **FREE** | [→](https://steamcommunity.com/dev) |
| [TMDB](manifests/tmdb/apia.json) | Movies/TV | **FREE** | [→](https://developer.themoviedb.org/docs) |
| [YouTube](manifests/youtube/apia.json) | Video | 10K units/day | [→](https://developers.google.com/youtube/v3) |
| [Twitch](manifests/twitch/apia.json) | Game Streaming | Free | [→](https://dev.twitch.tv/docs/api/) |
| [Spotify](manifests/spotify/apia.json) | Music | Free | [→](https://developer.spotify.com/documentation/web-api) |
| [NewsAPI](manifests/newsapi/apia.json) | News | 100/day | [→](https://newsapi.org/docs) |
| [Unsplash](manifests/unsplash/apia.json) | Stock Photos | 50/hr | [→](https://unsplash.com/documentation) |
| [PokéAPI](manifests/pokeapi/apia.json) | Pokémon | **FREE** | [→](https://pokeapi.co/docs/v2) |

### 🏋️ Sports & Fitness

| Service | Category | Free Tier | Docs |
|---|---|---|---|
| [Strava](manifests/strava/apia.json) | Fitness/Running | 100/15min | [→](https://developers.strava.com/docs/reference/) |
| [Football-Data](manifests/football-data/apia.json) | Soccer | **FREE** | [→](https://docs.football-data.org) |
| [SportsData.io](manifests/sportsdata-io/apia.json) | Multi-Sport | Trial | [→](https://sportsdata.io/developers) |
| [Ergast F1](manifests/ergast-f1/apia.json) | Formula 1 | **FREE** | [→](https://ergast.com/mrd/) |
| [The Odds API](manifests/odds-api/apia.json) | Betting Odds | 500/month | [→](https://the-odds-api.com) |

### 🏥 Healthcare

| Service | Category | Free Tier | Docs |
|---|---|---|---|
| [OpenFDA](manifests/open-fda/apia.json) | Drug/Medical Data | **FREE** | [→](https://open.fda.gov/apis/) |
| [WHO GHO](manifests/who/apia.json) | World Health Data | **FREE** | [→](https://www.who.int/data/gho/info/gho-odata-api) |
| [Fitbit](manifests/fitbit/apia.json) | Fitness Tracking | Free | [→](https://dev.fitbit.com/build/reference/web-api/) |
| [Nutritionix](manifests/nutritionix/apia.json) | Nutrition | 500/day | [→](https://developer.nutritionix.com/docs/v2) |
| [Infermedica](manifests/infermedica/apia.json) | Symptom Checker | Sandbox | [→](https://developer.infermedica.com/docs) |

### 📚 Education & Knowledge

| Service | Category | Free Tier | Docs |
|---|---|---|---|
| [Wikipedia](manifests/wikipedia/apia.json) | Knowledge | **FREE** | [→](https://en.wikipedia.org/api/rest_v1/) |
| [Wolfram Alpha](manifests/wolfram-alpha/apia.json) | Computation | 2000/month | [→](https://products.wolframalpha.com/api/documentation/) |
| [Khan Academy](manifests/khan-academy/apia.json) | Education | **FREE** | [→](https://api-explorer.khanacademy.org/) |
| [Google Books](manifests/google-books/apia.json) | Books | **FREE** | [→](https://developers.google.com/books/docs/v1/using) |
| [Typeform](manifests/typeform/apia.json) | Forms/Surveys | 10/month | [→](https://www.typeform.com/developers/) |
| [Duolingo](manifests/duolingo/apia.json) | Language Learning | **FREE** | [→](https://github.com/KartikTalwar/Duolingo) |
| [Open Trivia DB](manifests/open-trivia/apia.json) | Trivia/Quiz | **FREE** | [→](https://opentdb.com/api_config.php) |

### 🏠 Real Estate

| Service | Category | Free Tier | Docs |
|---|---|---|---|
| [Zillow](manifests/zillow/apia.json) | Real Estate US | Free tier | [→](https://bridgedataoutput.com/docs) |
| [ЦИАН](manifests/cian/apia.json) | Real Estate RU | Partnership | [→](https://www.cian.ru/help/about/partners-api/) |
| [Rightmove](manifests/rightmove/apia.json) | Real Estate UK | Commercial | [→](https://developer.rightmove.co.uk/) |
| [Idealista](manifests/idealista/apia.json) | Real Estate ES/IT/PT | Commercial | [→](https://developers.idealista.com/) |
| [ATTOM](manifests/attom/apia.json) | Property Data US | Trial | [→](https://api.developer.attomdata.com/docs) |

### 💼 Business & CRM

| Service | Category | Free Tier | Docs |
|---|---|---|---|
| [HubSpot](manifests/hubspot/apia.json) | CRM | **FREE** CRM | [→](https://developers.hubspot.com/docs/api/overview) |
| [Salesforce](manifests/salesforce/apia.json) | Enterprise CRM | Dev org free | [→](https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/) |
| [Pipedrive](manifests/pipedrive/apia.json) | Sales CRM | 14-day trial | [→](https://developers.pipedrive.com/docs/api/v1) |
| [amoCRM](manifests/amocrm/apia.json) | CRM RU/CIS | 14-day trial | [→](https://www.amocrm.ru/developers/content/crm_platform/api-reference) |
| [Bitrix24](manifests/bitrix24/apia.json) | Business Platform RU | 5 users free | [→](https://apidocs.bitrix24.ru/) |

### 🔒 Security

| Service | Category | Free Tier | Docs |
|---|---|---|---|
| [VirusTotal](manifests/virustotal/apia.json) | Malware Scan | 500/day | [→](https://developers.virustotal.com/reference/overview) |
| [Shodan](manifests/shodan/apia.json) | Security Research | 1 credit/month | [→](https://developer.shodan.io/api) |
| [Have I Been Pwned](manifests/have-i-been-pwned/apia.json) | Breach Check | $3.95/month | [→](https://haveibeenpwned.com/API/v3) |
| [Auth0](manifests/auth0/apia.json) | Identity/Auth | 7500 MAU | [→](https://auth0.com/docs/api/management/v2) |
| [Cloudflare Workers](manifests/cloudflare-workers/apia.json) | Edge Computing | 100K req/day | [→](https://developers.cloudflare.com/workers/) |

### 🏡 IoT & Smart Home

| Service | Category | Free Tier | Docs |
|---|---|---|---|
| [Home Assistant](manifests/home-assistant/apia.json) | Smart Home | **FREE** (self-hosted) | [→](https://developers.home-assistant.io/docs/api/rest/) |
| [Philips Hue](manifests/philips-hue/apia.json) | Smart Lights | **FREE** (local) | [→](https://developers.meethue.com/develop/hue-api/) |
| [Tesla Fleet](manifests/tesla/apia.json) | EV/Automotive | Free personal | [→](https://developer.tesla.com/docs/fleet-api) |
| [Particle](manifests/particle/apia.json) | IoT Platform | 100 devices | [→](https://docs.particle.io/reference/cloud-apis/api/) |
| [AWS IoT](manifests/aws-iot/apia.json) | IoT Enterprise | 250K msg/month | [→](https://docs.aws.amazon.com/iot/) |

### 🛒 E-commerce

| Service | Category | Free Tier | Docs |
|---|---|---|---|
| [Shopify](manifests/shopify/apia.json) | E-commerce | Partner free | [→](https://shopify.dev/docs/api) |
| [WooCommerce](manifests/woocommerce/apia.json) | WordPress Store | Free plugin | [→](https://woocommerce.github.io/woocommerce-rest-api-docs/) |
| [Yelp](manifests/yelp/apia.json) | Local Business | 500/day | [→](https://docs.developer.yelp.com) |

### 🧰 Developer Tools & Productivity

| Service | Category | Free Tier | Docs |
|---|---|---|---|
| [GitHub](manifests/github/apia.json) | Dev Tools | 60 req/hr | [→](https://docs.github.com/en/rest) |
| [Supabase](manifests/supabase/apia.json) | Backend/DB | 500MB | [→](https://supabase.com/docs) |
| [Firebase](manifests/firebase/apia.json) | Mobile Backend | Generous | [→](https://firebase.google.com/docs/reference/rest) |
| [AWS S3](manifests/aws-s3/apia.json) | Cloud Storage | 5GB | [→](https://docs.aws.amazon.com/s3) |
| [Cloudflare Workers](manifests/cloudflare-workers/apia.json) | Serverless Edge | 100K/day | [→](https://developers.cloudflare.com/workers/) |
| [Notion](manifests/notion-api/apia.json) | Notes/Database | Free | [→](https://developers.notion.com/reference/intro) |
| [Google Calendar](manifests/google-calendar/apia.json) | Calendar | Free | [→](https://developers.google.com/calendar/api/v3/reference) |
| [Slack](manifests/slack-api/apia.json) | Team Comms | Free plan | [→](https://api.slack.com/methods) |
| [Airtable](manifests/airtable/apia.json) | DB/Spreadsheet | 1000 records | [→](https://airtable.com/developers/web/api/introduction) |
| [Zapier NLA](manifests/zapier/apia.json) | No-code Automation | Paid plans | [→](https://nla.zapier.com/docs/) |

### 🌐 Translation & Language

| Service | Category | Free Tier | Docs |
|---|---|---|---|
| [DeepL](manifests/deepl/apia.json) | Translation | 500K chars | [→](https://www.deepl.com/docs-api) |
| [Google Translate](manifests/google-translate/apia.json) | Translation | 500K chars | [→](https://cloud.google.com/translate/docs) |

### 🎲 Free & Fun

| Service | Category | Free | Docs |
|---|---|---|---|
| [JokeAPI](manifests/jokeapi/apia.json) | Humor | **FREE** | [→](https://jokeapi.dev/#docs) |
| [RestCountries](manifests/rest-countries/apia.json) | Geography | **FREE** | [→](https://restcountries.com) |
| [PokéAPI](manifests/pokeapi/apia.json) | Pokémon | **FREE** | [→](https://pokeapi.co/docs/v2) |
| [Open Trivia DB](manifests/open-trivia/apia.json) | Trivia | **FREE** | [→](https://opentdb.com/api_config.php) |
| [NASA APOD](manifests/nasa/apia.json) | Space Photos | **FREE** | [→](https://api.nasa.gov/) |
| [GBIF](manifests/gbif/apia.json) | Biodiversity | **FREE** | [→](https://www.gbif.org/developer/summary) |
| [Ergast F1](manifests/ergast-f1/apia.json) | Formula 1 | **FREE** | [→](https://ergast.com/mrd/) |
| [OpenSky](manifests/opensky-network/apia.json) | Aircraft | **FREE** | [→](https://openskynetwork.github.io/opensky-api/) |

### 🇷🇺 Russia

| Service | Category | Docs |
|---|---|---|
| [hh.ru](manifests/hh-ru/apia.json) | Employment | [→](https://github.com/hhru/api) |
| [SuperJob](manifests/superjob/apia.json) | Employment | [→](https://api.superjob.ru/) |
| [SuperJob Resumes](manifests/superjob-resumes/apia.json) | Resumes | [→](https://api.superjob.ru/) |
| [Авито.Работа](manifests/avito-jobs/apia.json) | Employment | [→](https://developers.avito.ru/api-catalog/job/documentation) |
| [trudvsem.ru](manifests/trudvsem/apia.json) | Employment Gov | [→](https://trudvsem.ru/opendata/api) |
| [Яндекс.Расписания](manifests/yandex-rasp/apia.json) | Transport | [→](https://yandex.ru/dev/rasp/doc/ru/) |
| [data.mos.ru](manifests/data-mos-ru/apia.json) | City Data Moscow | [→](https://data.mos.ru/developers/documentation) |
| [ЕГРЮЛ/ФНС](manifests/egrul-fns/apia.json) | Business Registry | [→](https://api-fns.ru/) |
| [ФИАС/ГАР](manifests/fias/apia.json) | Address Registry | [→](https://fias.nalog.ru/) |
| [ЦБ РФ](manifests/cbrf/apia.json) | Currency/Finance | [→](https://www.cbr.ru/development/) |
| [Госуслуги](manifests/gosuslugi/apia.json) | Gov Services | [→](https://partners.gosuslugi.ru/catalog/api_for_gu) |
| [VK](manifests/vk/apia.json) | Social Media | [→](https://dev.vk.com/ru/api/overview) |
| [amoCRM](manifests/amocrm/apia.json) | CRM | [→](https://www.amocrm.ru/developers/) |
| [Bitrix24](manifests/bitrix24/apia.json) | Business Platform | [→](https://apidocs.bitrix24.ru/) |
| [ЦИАН](manifests/cian/apia.json) | Real Estate | [→](https://www.cian.ru/help/about/partners-api/) |

### 🇧🇾🇰🇿 CIS

| Service | Category | Docs |
|---|---|---|
| [hh.kz](manifests/hh-kz/apia.json) | Employment KZ | [→](https://dev.hh.kz/) |
| [hh.by](manifests/hh-by/apia.json) | Employment BY | [→](https://github.com/hhru/api) |
| [2GIS CIS](manifests/2gis-cis/apia.json) | Maps BY+KZ | [→](https://docs.2gis.com/en/api/search/overview) |

---

## How the Registry Works

**Adding:** Fork → `manifests/{id}/apia.json` → PR → auto JSON Schema validation → 3× 👍 → auto-merged

**Quality:** ✅ Verified · 🔶 Draft · ⚠️ Partial · ❌ Deprecated

**Health:** Monthly Action pings endpoints, opens Issues if broken

**Ideas:** [Discussions](../../discussions/categories/ideas) — upvoted = prioritized

---

## Compatibility

| Standard | Relationship |
|---|---|
| **MCP** (Anthropic) | APIA → MCP tool definitions |
| **OpenAPI** | APIA adds LLM intent layer |
| **OpenClaw skills** | APIA → `SKILL.md` |

---

## Contribute

```bash
git clone https://github.com/Komsomol39/apia-standard
cp manifests/hh-ru/apia.json manifests/your-api/apia.json
# edit → Pull Request
```

See [CONTRIBUTING.md](CONTRIBUTING.md) · [ALL_APIS.md](docs/ALL_APIS.md) has 1945 more APIs to document

---

💬 [Discussions](../../discussions) · 🐛 [Issues](../../issues) · 🌐 OpenClaw `#showcase`

**APIA · 127 manifests · 4 languages · Open source · June 2026**