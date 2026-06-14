# APIA — API für KI-Agenten

> **Offener Standard zur Beschreibung öffentlicher APIs in einem Format, das KI-Agenten nativ verstehen.**

🇬🇧 [English](../README.md) · 🇷🇺 [Русский](README.ru.md) · 🇨🇳 [中文](README.zh.md)

---

## Das Problem

Ein KI-Agent, der einem Nutzer helfen soll, einen Job in der Nähe zu finden, den Busfahrplan abzufragen und eine offene Apotheke zu finden, muss jede API separat erlernen. Jeder Dienst hat sein eigenes Format, seine eigene Authentifizierung, seine eigene Paginierung. Es gibt keinen gemeinsamen Vertrag.

**APIA löst dies mit einer einzigen `apia.json`-Manifestdatei**, die jedem KI-Agenten mitteilt:
- 🧠 **Was** der Dienst kann (für LLMs geschrieben, nicht für Entwickler)
- 🌍 **Wo** er funktioniert (Geografie, Sprache)
- 🔑 **Wie** man sich authentifiziert
- ⚡ **Ob** Daten in Echtzeit oder gecacht sind
- 💡 **Hinweise** zur korrekten Nutzung in realen Szenarien

---

## So funktioniert es

```
Nutzer: "Finde mir einen Python-Job in meiner Nähe"
        ↓
Agent liest APIA-Registry
        ↓
Findet hh-ru → Fähigkeit: search_vacancies
        ↓
Mappt Intent auf API-Parameter:
  text="Python", lat=55.75, lng=37.61
        ↓
Ruft HH.ru API auf → gibt Ergebnisse zurück
        ↓
Agent antwortet dem Nutzer
```

Keine hardcodierte Integration. Kein Custom-Training. Nur das Manifest.

---

## Registry

| Dienst | Kategorie | Fähigkeiten | Auth | API-Version | Geprüft | Status |
|---|---|---|---|---|---|---|
| [hh.ru](../manifests/hh-ru/apia.json) | Arbeit | 5 | OAuth2 / Anonym | v1 | 2026-06-14 | ✅ Bereit |
| [SuperJob](../manifests/superjob/apia.json) | Arbeit | 4 | API Key / Anonym | v2.0 | 2026-06-14 | ✅ Bereit |
| [trudvsem.ru](../manifests/trudvsem/apia.json) | Arbeit (Staat) | 4 | Keine | v1 | 2026-06-14 | ✅ Bereit |
| [Яндекс.Расписания](../manifests/yandex-rasp/apia.json) | Transport | 5 | API Key | v3.0 | 2026-06-14 | ✅ Bereit |
| [Яндекс.Карты](../manifests/yandex-maps/apia.json) | Karten / Geocoding | 3 | API Key | v1.x | 2026-06-14 | ✅ Bereit |
| [2GIS](../manifests/2gis/apia.json) | Karten / POI | 4 | API Key | v3.0 | 2026-06-14 | ✅ Bereit |
| [data.mos.ru](../manifests/data-mos-ru/apia.json) | Stadtdaten (Moskau) | 3 | API Key | v1 | 2026-06-14 | ✅ Bereit |

---

## Wie man beiträgt

1. Forke dieses Repository
2. Erstelle Ordner `manifests/{service-id}/`
3. Füge `apia.json` nach dem [HH.ru-Beispiel](../manifests/hh-ru/apia.json) hinzu
4. Grundregel: Schreibe `description_for_ai` so, als würdest du einem KI-Agenten erklären
5. Öffne einen Pull Request

---

**APIA ist Open Source. Nicht mit einem API-Anbieter verbunden.**