# APIA — API for AI Agents

APIA (API for AI Agents) — открытый стандарт описания публичных API в формате понятном AI-агентам. Вдохновлён тем что SOAP сделал для enterprise-контрактов, но создан для эпохи AI.

## Проблема

Каждый публичный API говорит на своём языке. AI-агент который хочет найти вакансию рядом с пользователем должен отдельно изучать HH.ru, SuperJob и Trudvsem — у каждого свой формат, своя авторизация, своя пагинация. Единого контракта нет.

APIA решает это одним файлом манифеста: `apia.json`

## Как выглядит apia.json

```json
{
  "apia": "1.0",
  "service": {
    "id": "hh-ru",
    "name": "HeadHunter",
    "description_for_ai": "Российская биржа труда. Используй для поиска вакансий по ключевым словам, городу или координатам.",
    "category": "employment",
    "geo": ["RU", "BY", "KZ"],
    "language": "ru"
  },
  "capabilities": [
    {
      "id": "search_vacancies",
      "description_for_ai": "Поиск вакансий по ключевому слову и геолокации.",
      "intent": ["найти работу", "вакансии рядом", "поиск работы"],
      "endpoint": "GET https://api.hh.ru/vacancies",
      "realtime": true,
      "requires_auth": false
    }
  ]
}
```

## Реестр российских API

| Сервис | Категория | Статус |
|---|---|---|
| hh.ru | Занятость | ✅ Черновик |
| trudvsem.ru | Занятость | 🔜 Планируется |
| Яндекс.Расписания | Транспорт | 🔜 Планируется |
| 2GIS | Карты / POI | 🔜 Планируется |

## Совместимость

- **MCP** (Anthropic Model Context Protocol)
- **OpenAPI**
- **OpenClaw skills**

## Лицензия

MIT
