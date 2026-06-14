# APIA — API for AI Agents

> **The open standard for describing any public API in a format AI agents natively understand.**

🇷🇺 [Русский](docs/README.ru.md) · 🇨🇳 [中文](docs/README.zh.md) · 🇩🇪 [Deutsch](docs/README.de.md)

---

## Why APIA Exists

Every public API speaks its own language. **APIA is the shared contract** — one `apia.json` that tells any AI agent what a service does, how to call it, and when to use it. Written for LLMs, not developers.

```json
{
  "apia": "1.0",
  "service": { "id": "openweathermap", "description_for_ai": "Get weather for any location.", "geo": ["GLOBAL"] },
  "capabilities": [{ "id": "current_weather",
    "description_for_ai": "Use for 'what is the weather', 'is it raining in Tokyo'.",
    "intent": ["current weather", "temperature now", "погода сейчас"],
    "endpoint": "GET https://api.openweathermap.org/data/2.5/weather", "realtime": true }]
}
```

---

## Registry — 252 Manifests

> Full candidate list: [docs/ALL_APIS.md](docs/ALL_APIS.md) · How to contribute: [CONTRIBUTING.md](CONTRIBUTING.md)

### 🤖 AI & Machine Learning

| Service | Specialty | Free | Docs |
|---|---|---|---|
| [OpenAI](manifests/openai/apia.json) | GPT/DALL-E/Whisper/TTS | $5 credit | [→](https://platform.openai.com/docs) |
| [OpenAI Assistants](manifests/openai-assistants/apia.json) | RAG/Code/Memory | Same | [→](https://platform.openai.com/docs/assistants/overview) |
| [OpenAI Batch](manifests/openai-batch/apia.json) | 50% discount bulk | 50% off | [→](https://platform.openai.com/docs/guides/batch) |
| [OpenAI Fine-Tuning](manifests/openai-fine-tuning/apia.json) | Custom model training | Paid | [→](https://platform.openai.com/docs/guides/fine-tuning) |
| [OpenAI Moderation](manifests/openai-moderation/apia.json) | Content safety | **FREE** | [→](https://platform.openai.com/docs/guides/moderation) |
| [Anthropic Claude](manifests/anthropic/apia.json) | Best coding/reasoning | Free tier | [→](https://docs.anthropic.com) |
| [Claude Haiku 4.5](manifests/anthropic-claude-haiku/apia.json) | Fast cheap tasks | $0.80/1M | [→](https://docs.anthropic.com/en/docs/models-overview) |
| [Google Gemini](manifests/google-gemini/apia.json) | LLM 1M context | 1500/day | [→](https://ai.google.dev/api) |
| [Gemini Vision](manifests/google-gemini-vision/apia.json) | Image/Video/PDF | 1500/day | [→](https://ai.google.dev/gemini-api/docs/vision) |
| [Mistral AI](manifests/mistral/apia.json) | European LLM/Code | Free tier | [→](https://docs.mistral.ai) |
| [DeepSeek](manifests/deepseek/apia.json) | Cheapest frontier | $5 credit | [→](https://platform.deepseek.com/docs) |
| [xAI Grok](manifests/xai-grok/apia.json) | LLM + live X search | $25/month | [→](https://docs.x.ai/api) |
| [Groq](manifests/groq/apia.json) | 300+ tok/s | 6K tok/min | [→](https://console.groq.com/docs) |
| [Perplexity](manifests/perplexity/apia.json) | LLM + web search | — | [→](https://docs.perplexity.ai) |
| [Together AI](manifests/together-ai/apia.json) | Cheap open LLMs | $1 credit | [→](https://docs.together.ai) |
| [Hugging Face](manifests/huggingface/apia.json) | 300K+ open models | Free tier | [→](https://huggingface.co/docs/api-inference) |
| [Replicate](manifests/replicate/apia.json) | Run any open model | Pay/sec | [→](https://replicate.com/docs) |
| [Cohere](manifests/cohere/apia.json) | LLM/Embed/Rerank | Trial | [→](https://docs.cohere.com) |
| [Stability AI](manifests/stability-ai/apia.json) | Image generation | Credits | [→](https://platform.stability.ai/docs/api-reference) |
| [Pinecone](manifests/pinecone/apia.json) | Vector DB for RAG | 2GB free | [→](https://docs.pinecone.io) |
| [Google Vision](manifests/google-vision/apia.json) | Labels/OCR/faces | 1000/month | [→](https://cloud.google.com/vision/docs) |
| [AWS Rekognition](manifests/aws-rekognition/apia.json) | Face/object/text | 5K/month | [→](https://docs.aws.amazon.com/rekognition/) |
| [Google Natural Language](manifests/google-natural-language/apia.json) | Sentiment/Entities/Classify | 5000/month | [→](https://cloud.google.com/natural-language/docs) |
| [AWS Comprehend](manifests/aws-comprehend/apia.json) | NLP 12 languages | 50K/month | [→](https://docs.aws.amazon.com/comprehend/) |
| [Perspective API](manifests/perspective-api/apia.json) | Toxicity detection | **FREE** | [→](https://developers.perspectiveapi.com/s/docs) |

### 🎤 Speech & Audio

| Service | Specialty | Free | Docs |
|---|---|---|---|
| [OpenAI Whisper](manifests/openai-whisper/apia.json) | Best STT accuracy | $0.006/min | [→](https://platform.openai.com/docs/guides/speech-to-text) |
| [Deepgram](manifests/deepgram/apia.json) | Real-time STT | $200 credit | [→](https://developers.deepgram.com/reference/) |
| [AssemblyAI](manifests/assemblyai/apia.json) | STT + AI insights | $50 credit | [→](https://www.assemblyai.com/docs) |
| [ElevenLabs](manifests/elevenlabs/apia.json) | Best TTS + voice clone | 10K chars | [→](https://elevenlabs.io/docs/api-reference) |
| [OpenAI TTS](manifests/openai-tts/apia.json) | Fast TTS 6 voices | $15/1M chars | [→](https://platform.openai.com/docs/guides/text-to-speech) |

### 🎬 Video Generation

| Service | Docs |
|---|---|
| [RunwayML](manifests/runway/apia.json) | [→](https://docs.dev.runwayml.com/) |
| [Luma AI](manifests/luma-ai/apia.json) | [→](https://docs.lumalabs.ai/) |

### 🌍 Maps & Location

| Service | Coverage | Free | Docs |
|---|---|---|---|
| [Google Maps](manifests/google-maps/apia.json) | Global | $200/month | [→](https://developers.google.com/maps) |
| [Mapbox](manifests/mapbox/apia.json) | Global custom | 200K loads | [→](https://docs.mapbox.com) |
| [HERE Maps](manifests/here-maps/apia.json) | Global automotive | 250K/month | [→](https://developer.here.com/documentation) |
| [Nominatim/OSM](manifests/openstreetmap-nominatim/apia.json) | Global geocoding | **FREE** | [→](https://nominatim.org/release-docs/develop/api/Overview/) |
| [OSM Overpass](manifests/openstreetmap-overpass/apia.json) | Map data queries | **FREE** | [→](https://wiki.openstreetmap.org/wiki/Overpass_API) |
| [Foursquare](manifests/foursquare/apia.json) | 100M+ places | 1000/day | [→](https://docs.foursquare.com) |
| [Mapillary](manifests/mapillary/apia.json) | Street imagery 2B+ | Free dev | [→](https://www.mapillary.com/developer/api-documentation) |
| [ip-api.com](manifests/ipapi/apia.json) | IP geolocation | **FREE** | [→](https://ip-api.com/docs/api:json) |
| [IPGeolocation](manifests/ipgeolocation/apia.json) | IP + timezone | 1000/day | [→](https://ipgeolocation.io/documentation) |
| [Яндекс.Карты](manifests/yandex-maps/apia.json) | Russia/CIS | Free tier | [→](https://yandex.ru/dev/maps/) |
| [2GIS](manifests/2gis/apia.json) | Russia/CIS/World | Demo free | [→](https://docs.2gis.com/en/api/search/overview) |

### ☁️ Weather & Environment

| Service | Specialty | Free | Docs |
|---|---|---|---|
| [OpenWeatherMap](manifests/openweathermap/apia.json) | Weather global | 1000/day | [→](https://openweathermap.org/api) |
| [Open-Meteo](manifests/open-meteo/apia.json) | Weather no key | **FREE** | [→](https://open-meteo.com/en/docs) |
| [OpenAQ](manifests/openaq/apia.json) | Air quality | **FREE** | [→](https://docs.openaq.org) |
| [NASA APIs](manifests/nasa/apia.json) | Space + Earth | **FREE** | [→](https://api.nasa.gov/) |
| [Planet Labs](manifests/planet-labs/apia.json) | Daily satellite | Education | [→](https://developers.planet.com/docs/apis/data/) |
| [GBIF](manifests/gbif/apia.json) | Biodiversity 2.4B | **FREE** | [→](https://www.gbif.org/developer/summary) |
| [Carbon Interface](manifests/carbon-interface/apia.json) | Carbon emissions | 100/month | [→](https://docs.carboninterface.com) |

### 💰 Finance & Payments

| Service | Specialty | Free | Docs |
|---|---|---|---|
| [Stripe](manifests/stripe/apia.json) | Payments global | No monthly | [→](https://stripe.com/docs/api) |
| [PayPal](manifests/paypal/apia.json) | Payments + payouts | No monthly | [→](https://developer.paypal.com/docs/api/overview/) |
| [Adyen](manifests/adyen/apia.json) | Enterprise payments | Custom | [→](https://docs.adyen.com/api-explorer/) |
| [Wise](manifests/wise/apia.json) | International transfers | No monthly | [→](https://docs.wise.com/api-docs/) |
| [ЮКасса](manifests/yookassa/apia.json) | Payments Russia | No monthly | [→](https://yookassa.ru/developers/api) |
| [Тинькофф](manifests/tinkoff-acquiring/apia.json) | Payments Russia | No monthly | [→](https://www.tinkoff.ru/kassa/develop/api/payments/) |
| [Plaid](manifests/plaid/apia.json) | Bank data | Sandbox free | [→](https://plaid.com/docs) |
| [Alpha Vantage](manifests/alpha-vantage/apia.json) | Stocks EOD | 25/day | [→](https://www.alphavantage.co/documentation/) |
| [Polygon.io](manifests/polygon-io/apia.json) | Stocks real-time | 5/min | [→](https://polygon.io/docs/stocks/) |
| [CoinGecko](manifests/coingecko/apia.json) | Crypto 10K+ | **FREE** | [→](https://www.coingecko.com/api/documentation) |
| [Coinbase](manifests/coinbase/apia.json) | Crypto prices | **FREE** | [→](https://docs.cdp.coinbase.com) |
| [Binance](manifests/binance/apia.json) | Crypto market | **FREE** | [→](https://binance-docs.github.io/apidocs/) |
| [ExchangeRate-API](manifests/exchangerate-api/apia.json) | Currency | 1500/month | [→](https://www.exchangerate-api.com/docs) |
| [ЦБ РФ](manifests/cbrf/apia.json) | Official RU rates | **FREE** | [→](https://www.cbr.ru/development/) |
| [SEC EDGAR](manifests/sec-edgar/apia.json) | US filings | **FREE** | [→](https://www.sec.gov/developer) |
| [World Bank](manifests/world-bank/apia.json) | Economic data | **FREE** | [→](https://datahelpdesk.worldbank.org) |

### ✈️ Transport & Travel

| Service | Specialty | Free | Docs |
|---|---|---|---|
| [Amadeus](manifests/amadeus/apia.json) | Flights/Hotels | 2000/month | [→](https://developers.amadeus.com/self-service) |
| [FlightAware](manifests/flightaware/apia.json) | Flight tracking | 500/month | [→](https://flightaware.com/commercial/aeroapi/) |
| [OpenSky Network](manifests/opensky-network/apia.json) | Aircraft ADS-B | **FREE** | [→](https://openskynetwork.github.io/opensky-api/) |
| [Skyscanner](manifests/skyscanner/apia.json) | Flight prices | Partnership | [→](https://developers.skyscanner.net/docs) |
| [GTFS/Transitland](manifests/gtfs/apia.json) | Public transit | Free tier | [→](https://www.transit.land/documentation) |
| [Uber](manifests/uber/apia.json) | Ride estimates | Partnership | [→](https://developer.uber.com/docs) |
| [Яндекс.Расписания](manifests/yandex-rasp/apia.json) | Transport Russia | Free key | [→](https://yandex.ru/dev/rasp/doc/ru/) |

### 🏨 Travel & Hospitality

| Service | Specialty | Docs |
|---|---|---|
| [Booking.com](manifests/booking-com/apia.json) | 28M+ hotels | [→](https://developers.booking.com/demand/overview.html) |
| [Airbnb](manifests/airbnb/apia.json) | 7M+ rentals | [→](https://www.airbnb.com/partner) |
| [TripAdvisor](manifests/tripadvisor/apia.json) | Reviews 1B+ | [→](https://tripadvisor-content-api.readme.io/reference/overview) |
| [Google Hotels](manifests/google-hotels/apia.json) | Hotel prices | [→](https://serpapi.com/google-hotels-api) |

### 📦 Logistics & Shipping

| Service | Region | Docs |
|---|---|---|
| [EasyPost](manifests/easypost/apia.json) | Multi-carrier | [→](https://www.easypost.com/docs/api) |
| [Shippo](manifests/shippo/apia.json) | 85+ carriers | [→](https://goshippo.com/docs/reference) |
| [DHL API](manifests/dhl-api/apia.json) | International | [→](https://developer.dhl.com/api-reference/dhl-express-mydhl-api) |
| [СДЭК](manifests/cdek/apia.json) | Russia/CIS | [→](https://api-docs.cdek.ru/) |
| [Почта России](manifests/pochta-russia/apia.json) | Russia postal | [→](https://otpravka.pochta.ru/specification) |

### 👥 Social & Communication

| Service | Users | Free | Docs |
|---|---|---|---|
| [Telegram Bot](manifests/telegram-bot/apia.json) | 950M | **FREE** | [→](https://core.telegram.org/bots/api) |
| [Discord](manifests/discord/apia.json) | 500M | Free | [→](https://discord.com/developers/docs) |
| [Slack](manifests/slack-api/apia.json) | 20M daily | Free plan | [→](https://api.slack.com/methods) |
| [Instagram](manifests/instagram/apia.json) | 2B | Free | [→](https://developers.facebook.com/docs/instagram-api) |
| [Twitter/X](manifests/twitter-x/apia.json) | 350M | 1500/month | [→](https://developer.twitter.com/en/docs/twitter-api) |
| [TikTok](manifests/tiktok/apia.json) | 1.5B | Free | [→](https://developers.tiktok.com/doc/overview/) |
| [Facebook](manifests/facebook-graph/apia.json) | 3B | Free | [→](https://developers.facebook.com/docs/graph-api) |
| [Reddit](manifests/reddit/apia.json) | 1.5B/month | 100/min | [→](https://www.reddit.com/dev/api) |
| [VK](manifests/vk/apia.json) | 100M Russia | Free | [→](https://dev.vk.com/ru/api/overview) |
| [LinkedIn](manifests/linkedin/apia.json) | 1B+ | 500/day | [→](https://learn.microsoft.com/en-us/linkedin/) |
| [Twilio SMS](manifests/twilio/apia.json) | Global SMS | $15 trial | [→](https://twilio.com/docs/sms/api) |
| [Twilio Verify](manifests/twilio-verify/apia.json) | OTP/2FA | $15 trial | [→](https://www.twilio.com/docs/verify/api) |
| [Twilio Studio](manifests/twilio-studio/apia.json) | IVR/SMS bots | Per use | [→](https://www.twilio.com/docs/studio/rest-api/v2) |
| [SendGrid](manifests/sendgrid/apia.json) | Email delivery | 100/day | [→](https://docs.sendgrid.com/api-reference) |
| [Mailchimp](manifests/mailchimp/apia.json) | Email marketing | 500 contacts | [→](https://mailchimp.com/developer/marketing/api/) |
| [Mailgun](manifests/mailgun/apia.json) | Dev email | 5K/month | [→](https://documentation.mailgun.com/) |
| [Brevo](manifests/brevo/apia.json) | Email/SMS/WhatsApp | 300/day | [→](https://developers.brevo.com/reference/) |
| [Klaviyo](manifests/klaviyo/apia.json) | E-commerce email | 500 contacts | [→](https://developers.klaviyo.com/en/reference/api_overview) |
| [Sendbird](manifests/sendbird/apia.json) | In-app chat | 1000 MAU | [→](https://sendbird.com/docs/chat/platform-api/v3/overview) |

### 📣 Marketing & Advertising

| Service | Specialty | Docs |
|---|---|---|
| [Google Ads](manifests/google-ads/apia.json) | Search/Display/Video ads | [→](https://developers.google.com/google-ads/api/docs/start) |
| [Meta Ads](manifests/facebook-ads/apia.json) | Facebook/Instagram ads | [→](https://developers.facebook.com/docs/marketing-api/reference/) |
| [Klaviyo](manifests/klaviyo/apia.json) | E-commerce marketing | [→](https://developers.klaviyo.com/en/reference/api_overview) |

### 🎮 Entertainment & Media

| Service | Category | Free | Docs |
|---|---|---|---|
| [Steam](manifests/steam/apia.json) | Gaming 50K+ games | **FREE** | [→](https://steamcommunity.com/dev) |
| [TMDB](manifests/tmdb/apia.json) | Movies/TV 1M+ | **FREE** | [→](https://developer.themoviedb.org/docs) |
| [YouTube](manifests/youtube/apia.json) | Video | 10K units/day | [→](https://developers.google.com/youtube/v3) |
| [YouTube Analytics](manifests/youtube-analytics/apia.json) | Creator stats | Free | [→](https://developers.google.com/analytics/devguides/reporting/data/v1) |
| [Twitch](manifests/twitch/apia.json) | Game streaming | Free | [→](https://dev.twitch.tv/docs/api/) |
| [Spotify](manifests/spotify/apia.json) | Music 100M tracks | Free | [→](https://developer.spotify.com/documentation/web-api) |
| [NewsAPI](manifests/newsapi/apia.json) | News 150K sources | 100/day | [→](https://newsapi.org/docs) |
| [Unsplash](manifests/unsplash/apia.json) | Stock photos 5M+ | 50/hr | [→](https://unsplash.com/documentation) |
| [Pexels](manifests/pexels/apia.json) | Free photos/videos | 200/hr | [→](https://www.pexels.com/api/documentation/) |
| [LottieFiles](manifests/lottie-files/apia.json) | Animations 200K+ | Free | [→](https://docs.lottiefiles.com/api/) |
| [PokéAPI](manifests/pokeapi/apia.json) | All Pokémon | **FREE** | [→](https://pokeapi.co/docs/v2) |

### 🖼️ Media Management

| Service | Specialty | Free | Docs |
|---|---|---|---|
| [Cloudinary](manifests/cloudinary/apia.json) | Image/Video CDN + AI | 25GB free | [→](https://cloudinary.com/documentation/image_upload_api_reference) |
| [imgix](manifests/imgix/apia.json) | Real-time image transform | 10GB trial | [→](https://docs.imgix.com/apis/url) |
| [Mapillary](manifests/mapillary/apia.json) | Street imagery | Free dev | [→](https://www.mapillary.com/developer/api-documentation) |

### 🏋️ Sports & Fitness

| Service | Category | Free | Docs |
|---|---|---|---|
| [Strava](manifests/strava/apia.json) | Running/Cycling | 100/15min | [→](https://developers.strava.com/docs/reference/) |
| [Football-Data](manifests/football-data/apia.json) | Soccer | **FREE** | [→](https://docs.football-data.org) |
| [SportsData.io](manifests/sportsdata-io/apia.json) | NFL/NBA/MLB/NHL | Trial | [→](https://sportsdata.io/developers) |
| [Ergast F1](manifests/ergast-f1/apia.json) | Formula 1 | **FREE** | [→](https://ergast.com/mrd/) |
| [The Odds API](manifests/odds-api/apia.json) | Betting odds | 500/month | [→](https://the-odds-api.com) |

### 🏥 Healthcare

| Service | Category | Free | Docs |
|---|---|---|---|
| [OpenFDA](manifests/open-fda/apia.json) | Drug/Medical data | **FREE** | [→](https://open.fda.gov/apis/) |
| [WHO GHO](manifests/who/apia.json) | World health stats | **FREE** | [→](https://www.who.int/data/gho/info/gho-odata-api) |
| [Fitbit](manifests/fitbit/apia.json) | Wearable data | Free | [→](https://dev.fitbit.com/build/reference/web-api/) |
| [Nutritionix](manifests/nutritionix/apia.json) | Nutrition NLP | 500/day | [→](https://developer.nutritionix.com/docs/v2) |
| [Infermedica](manifests/infermedica/apia.json) | Symptom checker | Sandbox | [→](https://developer.infermedica.com/docs) |

### 🔬 Science & Research

| Service | Specialty | Free | Docs |
|---|---|---|---|
| [PubMed/NCBI](manifests/pubmed/apia.json) | 35M+ medical papers | **FREE** | [→](https://www.ncbi.nlm.nih.gov/books/NBK25499/) |
| [arXiv](manifests/arxiv/apia.json) | 2M+ preprints CS/AI/Math | **FREE** | [→](https://info.arxiv.org/help/api/index.html) |
| [Semantic Scholar](manifests/semantic-scholar/apia.json) | 220M papers + AI recs | **FREE** | [→](https://api.semanticscholar.org/) |
| [OpenAlex](manifests/open-alex/apia.json) | 250M research works | **FREE** | [→](https://docs.openalex.org/) |
| [Elsevier Scopus](manifests/elsevier-scopus/apia.json) | 87M peer-reviewed | Dev key free | [→](https://dev.elsevier.com/) |

### 🌿 Nature & Biodiversity

| Service | Specialty | Free | Docs |
|---|---|---|---|
| [GBIF](manifests/gbif/apia.json) | Occurrences 2.4B | **FREE** | [→](https://www.gbif.org/developer/summary) |
| [GBIF Species](manifests/gbif-species/apia.json) | Taxonomy all life | **FREE** | [→](https://www.gbif.org/developer/species) |
| [iNaturalist](manifests/inaturalist/apia.json) | 200M wildlife obs + AI ID | **FREE** | [→](https://api.inaturalist.org/v1/docs/) |
| [Carbon Interface](manifests/carbon-interface/apia.json) | Carbon emissions | 100/month | [→](https://docs.carboninterface.com) |
| [OpenAQ](manifests/openaq/apia.json) | Air quality global | **FREE** | [→](https://docs.openaq.org) |

### 📚 Education & Knowledge

| Service | Category | Free | Docs |
|---|---|---|---|
| [Wikipedia](manifests/wikipedia/apia.json) | 60M articles | **FREE** | [→](https://en.wikipedia.org/api/rest_v1/) |
| [Wikidata](manifests/wikidata/apia.json) | 100M entities | **FREE** | [→](https://www.wikidata.org/wiki/Wikidata:Data_access) |
| [Wolfram Alpha](manifests/wolfram-alpha/apia.json) | Computation | 2000/month | [→](https://products.wolframalpha.com/api/documentation/) |
| [Khan Academy](manifests/khan-academy/apia.json) | Free education | **FREE** | [→](https://api-explorer.khanacademy.org/) |
| [Google Books](manifests/google-books/apia.json) | 40M books | **FREE** | [→](https://developers.google.com/books/docs/v1/using) |
| [Open Trivia DB](manifests/open-trivia/apia.json) | 4000+ questions | **FREE** | [→](https://opentdb.com/api_config.php) |
| [Duolingo](manifests/duolingo/apia.json) | Language learning | **FREE** | [→](https://github.com/KartikTalwar/Duolingo) |

### 🍕 Food & Recipes

| Service | Category | Free | Docs |
|---|---|---|---|
| [TheMealDB](manifests/themealdb/apia.json) | 300+ recipes | **FREE** | [→](https://www.themealdb.com/api.php) |
| [Spoonacular](manifests/spoonacular/apia.json) | 5000+ recipes | 150/day | [→](https://spoonacular.com/food-api/docs) |
| [Open Food Facts](manifests/open-food-facts/apia.json) | 3M products | **FREE** | [→](https://wiki.openfoodfacts.org/API) |
| [Edamam](manifests/edamam/apia.json) | 2.3M recipes | 5/min | [→](https://developer.edamam.com/edamam-docs) |
| [DoorDash Drive](manifests/doordash/apia.json) | On-demand delivery | Per delivery | [→](https://developer.doordash.com/en-US/docs/drive/) |

### 🏠 Real Estate

| Service | Region | Docs |
|---|---|---|
| [Zillow](manifests/zillow/apia.json) | US | [→](https://bridgedataoutput.com/docs) |
| [ЦИАН](manifests/cian/apia.json) | Russia | [→](https://www.cian.ru/help/about/partners-api/) |
| [Rightmove](manifests/rightmove/apia.json) | UK | [→](https://developer.rightmove.co.uk/) |
| [Idealista](manifests/idealista/apia.json) | Spain/Italy/Portugal | [→](https://developers.idealista.com/) |
| [ATTOM](manifests/attom/apia.json) | US property data | [→](https://api.developer.attomdata.com/docs) |

### 💼 Business & CRM

| Service | Specialty | Free | Docs |
|---|---|---|---|
| [HubSpot](manifests/hubspot/apia.json) | CRM/Marketing | **FREE** | [→](https://developers.hubspot.com/docs/api/overview) |
| [Salesforce](manifests/salesforce/apia.json) | Enterprise CRM | Dev org | [→](https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/) |
| [Pipedrive](manifests/pipedrive/apia.json) | Sales CRM | 14-day | [→](https://developers.pipedrive.com/docs/api/v1) |
| [amoCRM](manifests/amocrm/apia.json) | CRM Russia/CIS | 14-day | [→](https://www.amocrm.ru/developers/) |
| [Bitrix24](manifests/bitrix24/apia.json) | All-in-one Russia | 5 users | [→](https://apidocs.bitrix24.ru/) |
| [Hunter.io](manifests/hunter-io/apia.json) | B2B email finder | 25/month | [→](https://hunter.io/api-documentation) |
| [Apollo.io](manifests/apollo-io/apia.json) | Sales intelligence 265M | 50 credits | [→](https://apolloio.github.io/apollo-api-docs/) |
| [ZoomInfo](manifests/zoominfo/apia.json) | Enterprise B2B data | Enterprise | [→](https://api-docs.zoominfo.com/) |
| [Clearbit](manifests/clearbit/apia.json) | Company enrichment | 50/month | [→](https://dashboard.clearbit.com/docs) |
| [OpenCorporates](manifests/opencorporates/apia.json) | 200M companies | 10/min | [→](https://api.opencorporates.com/documentation/API-Reference) |
| [Companies House](manifests/companies-house/apia.json) | UK companies | **FREE** | [→](https://developer.company-information.service.gov.uk/) |

### 🎧 Customer Support

| Service | Specialty | Free | Docs |
|---|---|---|---|
| [Zendesk](manifests/zendesk/apia.json) | Help desk | 14-day | [→](https://developer.zendesk.com/api-reference/) |
| [Freshdesk](manifests/freshdesk/apia.json) | Help desk | 10 agents | [→](https://developers.freshdesk.com/api/) |
| [Intercom](manifests/intercom/apia.json) | Customer messaging | 14-day | [→](https://developers.intercom.com/docs/) |

### 👔 HR & Recruiting

| Service | Specialty | Docs |
|---|---|---|
| [Workday](manifests/workday/apia.json) | Enterprise HR | [→](https://developer.workday.com/) |
| [Greenhouse](manifests/greenhouse/apia.json) | Recruiting ATS | [→](https://developers.greenhouse.io/harvest.html) |
| [BambooHR](manifests/bamboohr/apia.json) | HR for SMB | [→](https://documentation.bamboohr.com/reference) |

### ⚖️ Legal & Government

| Service | Category | Free | Docs |
|---|---|---|---|
| [SEC EDGAR](manifests/sec-edgar/apia.json) | US filings | **FREE** | [→](https://www.sec.gov/developer) |
| [Companies House](manifests/companies-house/apia.json) | UK companies | **FREE** | [→](https://developer.company-information.service.gov.uk/) |
| [World Bank](manifests/world-bank/apia.json) | Economic data | **FREE** | [→](https://datahelpdesk.worldbank.org) |
| [CourtListener](manifests/courtlistener/apia.json) | US court cases | **FREE** | [→](https://www.courtlistener.com/help/api/) |
| [OpenCorporates](manifests/opencorporates/apia.json) | 200M companies | 10/min | [→](https://api.opencorporates.com/documentation/API-Reference) |
| [DocuSign](manifests/docusign/apia.json) | eSignature | Sandbox | [→](https://developers.docusign.com/docs/esign-rest-api/) |

### 🔒 Security

| Service | Specialty | Free | Docs |
|---|---|---|---|
| [VirusTotal](manifests/virustotal/apia.json) | Malware scan 70+ | 500/day | [→](https://developers.virustotal.com/reference/overview) |
| [Shodan](manifests/shodan/apia.json) | Internet scanner | 1/month | [→](https://developer.shodan.io/api) |
| [Have I Been Pwned](manifests/have-i-been-pwned/apia.json) | Breach check | $3.95/month | [→](https://haveibeenpwned.com/API/v3) |
| [Auth0](manifests/auth0/apia.json) | Identity/Auth | 7500 MAU | [→](https://auth0.com/docs/api/management/v2) |
| [Twilio Verify](manifests/twilio-verify/apia.json) | OTP/2FA | $15 trial | [→](https://www.twilio.com/docs/verify/api) |

### 🏡 IoT & Smart Home

| Service | Specialty | Free | Docs |
|---|---|---|---|
| [Home Assistant](manifests/home-assistant/apia.json) | 3000+ devices | **FREE** | [→](https://developers.home-assistant.io/docs/api/rest/) |
| [Philips Hue](manifests/philips-hue/apia.json) | Smart lights | **FREE** | [→](https://developers.meethue.com/develop/hue-api/) |
| [Tesla Fleet](manifests/tesla/apia.json) | EV data/control | Free personal | [→](https://developer.tesla.com/docs/fleet-api) |
| [Particle](manifests/particle/apia.json) | IoT prototyping | 100 devices | [→](https://docs.particle.io/reference/cloud-apis/api/) |
| [AWS IoT](manifests/aws-iot/apia.json) | Enterprise IoT | 250K msg/month | [→](https://docs.aws.amazon.com/iot/) |

### 🧰 Developer Tools

| Service | Specialty | Free | Docs |
|---|---|---|---|
| [GitHub](manifests/github/apia.json) | Code/repos | 60 req/hr | [→](https://docs.github.com/en/rest) |
| [GitLab](manifests/gitlab/apia.json) | DevOps platform | Free OSS | [→](https://docs.gitlab.com/ee/api/rest/) |
| [Jira](manifests/jira/apia.json) | Issue tracking | 10 users | [→](https://developer.atlassian.com/cloud/jira/) |
| [Linear](manifests/linear/apia.json) | Modern issues | 250 issues | [→](https://developers.linear.app/docs/) |
| [Datadog](manifests/datadog/apia.json) | Monitoring | 14-day | [→](https://docs.datadoghq.com/api/latest/) |
| [Sentry](manifests/sentry/apia.json) | Error tracking | 5K/month | [→](https://docs.sentry.io/api/) |
| [PagerDuty](manifests/pagerduty/apia.json) | Incidents | 14-day | [→](https://developer.pagerduty.com/api-reference/) |
| [Vercel](manifests/vercel/apia.json) | Frontend deploy | Hobby free | [→](https://vercel.com/docs/rest-api) |
| [Netlify](manifests/netlify/apia.json) | Jamstack | 100GB/month | [→](https://open-api.netlify.com/) |
| [DigitalOcean](manifests/digitalocean/apia.json) | Cloud VMs | $200 credit | [→](https://docs.digitalocean.com/reference/api/) |
| [AWS Lambda](manifests/aws-lambda/apia.json) | Serverless | 1M req/month | [→](https://docs.aws.amazon.com/lambda/) |
| [Supabase](manifests/supabase/apia.json) | Backend/DB | 500MB | [→](https://supabase.com/docs) |
| [Firebase](manifests/firebase/apia.json) | Mobile backend | Generous | [→](https://firebase.google.com/docs/reference/rest) |
| [AWS S3](manifests/aws-s3/apia.json) | Cloud storage | 5GB | [→](https://docs.aws.amazon.com/s3) |
| [Cloudflare Workers](manifests/cloudflare-workers/apia.json) | Edge compute | 100K/day | [→](https://developers.cloudflare.com/workers/) |

### 📊 Analytics

| Service | Specialty | Free | Docs |
|---|---|---|---|
| [Google Analytics](manifests/google-analytics/apia.json) | Web analytics | Free | [→](https://developers.google.com/analytics/devguides/reporting/data/v1) |
| [Google Search Console](manifests/google-search-console/apia.json) | SEO data | Free | [→](https://developers.google.com/webmaster-tools/search-console-api) |
| [Mixpanel](manifests/mixpanel/apia.json) | Product analytics | 100M events | [→](https://developer.mixpanel.com/reference/overview) |
| [PostHog](manifests/posthog/apia.json) | Open-source analytics | 1M events | [→](https://posthog.com/docs/api) |
| [Segment](manifests/segment/apia.json) | CDP 450+ integrations | 1000 MTU | [→](https://segment.com/docs/connections/sources/catalog/libraries/server/http-api/) |
| [SerpAPI](manifests/serpapi/apia.json) | Search results data | 100/month | [→](https://serpapi.com/search-api) |

### 🧩 Productivity

| Service | Specialty | Free | Docs |
|---|---|---|---|
| [Notion](manifests/notion-api/apia.json) | Notes/DB/Wiki | Free | [→](https://developers.notion.com/reference/intro) |
| [Google Calendar](manifests/google-calendar/apia.json) | Calendar | Free | [→](https://developers.google.com/calendar/api/v3/reference) |
| [Airtable](manifests/airtable/apia.json) | DB/Spreadsheet | 1000 records | [→](https://airtable.com/developers/web/api/introduction) |
| [Typeform](manifests/typeform/apia.json) | Forms | 10/month | [→](https://www.typeform.com/developers/) |
| [Zapier NLA](manifests/zapier/apia.json) | 6000+ automations | Paid | [→](https://nla.zapier.com/docs/) |

### 🌐 Translation & NLP

| Service | Specialty | Free | Docs |
|---|---|---|---|
| [DeepL](manifests/deepl/apia.json) | Best quality 30+ | 500K chars | [→](https://www.deepl.com/docs-api) |
| [Google Translate](manifests/google-translate/apia.json) | 135+ languages | 500K chars | [→](https://cloud.google.com/translate/docs) |
| [LanguageTool](manifests/languagetool/apia.json) | Grammar check | **FREE** | [→](https://languagetool.org/http-api/) |
| [TextRazor](manifests/textrazor/apia.json) | Entity extraction | 500/day | [→](https://www.textrazor.com/docs/rest) |

### 🔧 Utilities

| Service | Specialty | Free | Docs |
|---|---|---|---|
| [Abstract API](manifests/abstract-api/apia.json) | Email/Phone/Holidays | 100-500/month | [→](https://docs.abstractapi.com/) |
| [Nager.Date](manifests/nager-date/apia.json) | Holidays 100+ countries | **FREE** | [→](https://date.nager.at/swagger/index.html) |
| [ScreenshotAPI](manifests/screenshotapi/apia.json) | Website screenshots | 100/month | [→](https://screenshotapi.net/documentation) |
| [HTML to PDF](manifests/html2pdf/apia.json) | PDF generation | 200 pages | [→](https://pdfcrowd.com/api/) |
| [QR Code API](manifests/qr-code-api/apia.json) | QR codes | **FREE** | [→](https://goqr.me/api/doc/create-qr-code/) |
| [DaData](manifests/dadata/apia.json) | Russian address/data | 10K/month | [→](https://dadata.ru/api/) |

### 🎲 Free & No API Key

| Service | Category | Docs |
|---|---|---|
| [Open-Meteo](manifests/open-meteo/apia.json) | Weather | [→](https://open-meteo.com/en/docs) |
| [TheMealDB](manifests/themealdb/apia.json) | Recipes | [→](https://www.themealdb.com/api.php) |
| [Open Food Facts](manifests/open-food-facts/apia.json) | Food barcode | [→](https://wiki.openfoodfacts.org/API) |
| [JokeAPI](manifests/jokeapi/apia.json) | Jokes 7 languages | [→](https://jokeapi.dev/#docs) |
| [RestCountries](manifests/rest-countries/apia.json) | 250 countries | [→](https://restcountries.com) |
| [PokéAPI](manifests/pokeapi/apia.json) | All 1000+ Pokémon | [→](https://pokeapi.co/docs/v2) |
| [Open Trivia DB](manifests/open-trivia/apia.json) | Quiz questions | [→](https://opentdb.com/api_config.php) |
| [NASA](manifests/nasa/apia.json) | Space photos/data | [→](https://api.nasa.gov/) |
| [GBIF](manifests/gbif/apia.json) | Biodiversity 2.4B | [→](https://www.gbif.org/developer/summary) |
| [OpenSky](manifests/opensky-network/apia.json) | Live aircraft | [→](https://openskynetwork.github.io/opensky-api/) |
| [Ergast F1](manifests/ergast-f1/apia.json) | F1 data 1950-now | [→](https://ergast.com/mrd/) |
| [Wikipedia](manifests/wikipedia/apia.json) | Encyclopedia | [→](https://en.wikipedia.org/api/rest_v1/) |
| [Wikidata](manifests/wikidata/apia.json) | Knowledge graph | [→](https://www.wikidata.org/wiki/Wikidata:Data_access) |
| [arXiv](manifests/arxiv/apia.json) | Research preprints | [→](https://info.arxiv.org/help/api/index.html) |
| [PubMed](manifests/pubmed/apia.json) | Medical papers | [→](https://www.ncbi.nlm.nih.gov/books/NBK25499/) |
| [Semantic Scholar](manifests/semantic-scholar/apia.json) | Academic papers | [→](https://api.semanticscholar.org/) |
| [OpenAlex](manifests/open-alex/apia.json) | Research works | [→](https://docs.openalex.org/) |
| [iNaturalist](manifests/inaturalist/apia.json) | Wildlife + AI ID | [→](https://api.inaturalist.org/v1/docs/) |
| [ip-api.com](manifests/ipapi/apia.json) | IP geolocation | [→](https://ip-api.com/docs/api:json) |
| [Nominatim](manifests/openstreetmap-nominatim/apia.json) | Geocoding | [→](https://nominatim.org/release-docs/develop/api/Overview/) |
| [OSM Overpass](manifests/openstreetmap-overpass/apia.json) | Map data | [→](https://wiki.openstreetmap.org/wiki/Overpass_API) |
| [SEC EDGAR](manifests/sec-edgar/apia.json) | US filings | [→](https://www.sec.gov/developer) |
| [World Bank](manifests/world-bank/apia.json) | Economic data | [→](https://datahelpdesk.worldbank.org) |
| [CourtListener](manifests/courtlistener/apia.json) | US court cases | [→](https://www.courtlistener.com/help/api/) |
| [Companies House](manifests/companies-house/apia.json) | UK companies | [→](https://developer.company-information.service.gov.uk/) |
| [Nager.Date](manifests/nager-date/apia.json) | Public holidays | [→](https://date.nager.at/swagger/index.html) |
| [QR Code API](manifests/qr-code-api/apia.json) | QR generation | [→](https://goqr.me/api/doc/) |
| [LanguageTool](manifests/languagetool/apia.json) | Grammar check | [→](https://languagetool.org/http-api/) |
| [OpenAQ](manifests/openaq/apia.json) | Air quality | [→](https://docs.openaq.org) |
| [CoinGecko](manifests/coingecko/apia.json) | Crypto prices | [→](https://www.coingecko.com/api/documentation) |
| [Perspective API](manifests/perspective-api/apia.json) | Toxicity detection | [→](https://developers.perspectiveapi.com/s/docs) |
| [OpenAI Moderation](manifests/openai-moderation/apia.json) | Content safety | [→](https://platform.openai.com/docs/guides/moderation) |
| [GBIF Species](manifests/gbif-species/apia.json) | Species taxonomy | [→](https://www.gbif.org/developer/species) |
| [Rosreestr](manifests/rosreestr/apia.json) | Russian real estate | [→](https://rosreestr.gov.ru/api/online/fir_object/) |

### 🇷🇺 Russia

| Service | Category | Docs |
|---|---|---|
| [GigaChat (Сбер)](manifests/sber-api/apia.json) | Russian LLM | [→](https://developers.sber.ru/portal/products) |
| [YandexGPT](manifests/yandex-gpt/apia.json) | Russian LLM + Embeddings | [→](https://yandex.cloud/ru/docs/foundation-models/) |
| [hh.ru](manifests/hh-ru/apia.json) | Employment | [→](https://github.com/hhru/api) |
| [SuperJob](manifests/superjob/apia.json) | Employment | [→](https://api.superjob.ru/) |
| [Авито.Работа](manifests/avito-jobs/apia.json) | Employment | [→](https://developers.avito.ru/api-catalog/job/documentation) |
| [trudvsem.ru](manifests/trudvsem/apia.json) | Employment Gov | [→](https://trudvsem.ru/opendata/api) |
| [data.mos.ru](manifests/data-mos-ru/apia.json) | City Data Moscow | [→](https://data.mos.ru/developers/documentation) |
| [ЕГРЮЛ/ФНС](manifests/egrul-fns/apia.json) | Business Registry | [→](https://api-fns.ru/) |
| [ФИАС/ГАР](manifests/fias/apia.json) | Address Registry | [→](https://fias.nalog.ru/) |
| [ЦБ РФ](manifests/cbrf/apia.json) | Currency | [→](https://www.cbr.ru/development/) |
| [Госуслуги](manifests/gosuslugi/apia.json) | Gov Services | [→](https://partners.gosuslugi.ru/catalog/api_for_gu) |
| [ЮКасса](manifests/yookassa/apia.json) | Payments | [→](https://yookassa.ru/developers/api) |
| [Тинькофф](manifests/tinkoff-acquiring/apia.json) | Payments | [→](https://www.tinkoff.ru/kassa/develop/api/payments/) |
| [СДЭК](manifests/cdek/apia.json) | Logistics | [→](https://api-docs.cdek.ru/) |
| [Почта России](manifests/pochta-russia/apia.json) | Postal | [→](https://otpravka.pochta.ru/specification) |
| [amoCRM](manifests/amocrm/apia.json) | CRM | [→](https://www.amocrm.ru/developers/) |
| [Bitrix24](manifests/bitrix24/apia.json) | Business Platform | [→](https://apidocs.bitrix24.ru/) |
| [ЦИАН](manifests/cian/apia.json) | Real Estate | [→](https://www.cian.ru/help/about/partners-api/) |
| [Росреестр](manifests/rosreestr/apia.json) | Real Estate Gov | [→](https://rosreestr.gov.ru/api/online/fir_object/) |
| [Контур.Фокус](manifests/kontur-focus/apia.json) | Business Intel | [→](https://developer.kontur.ru/doc/focus) |
| [DaData](manifests/dadata/apia.json) | Address/Company | [→](https://dadata.ru/api/) |
| [HFLabs](manifests/hflabs/apia.json) | Data Validation | [→](https://hflabs.ru/api/) |
| [VK](manifests/vk/apia.json) | Social Media | [→](https://dev.vk.com/ru/api/overview) |

### 🇧🇾🇰🇿 CIS

| Service | Category | Docs |
|---|---|---|
| [hh.kz](manifests/hh-kz/apia.json) | Employment KZ | [→](https://dev.hh.kz/) |
| [hh.by](manifests/hh-by/apia.json) | Employment BY | [→](https://github.com/hhru/api) |
| [2GIS CIS](manifests/2gis-cis/apia.json) | Maps BY+KZ | [→](https://docs.2gis.com/en/api/search/overview) |

---

## How the Registry Works

**Add:** Fork → `manifests/{id}/apia.json` → PR → auto validation → 3×👍 → merged

**Quality:** ✅ Verified · 🔶 Draft · ⚠️ Partial · ❌ Deprecated

**Health:** Monthly Action checks endpoints, opens Issues on failures

**Ideas:** [Discussions](../../discussions/categories/ideas)

---

## Compatibility

**MCP** · **OpenAPI** · **OpenClaw skills** — APIA works alongside all of them

---

💬 [Discussions](../../discussions) · 🐛 [Issues](../../issues) · [CONTRIBUTING.md](CONTRIBUTING.md)

**APIA · 252 manifests · 4 languages · Open source · June 2026**