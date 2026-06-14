# Contributing to APIA

Thanks for wanting to add an API to the registry! This guide explains how.

## The 5-minute path

```bash
git clone https://github.com/Komsomol39/apia-standard
cd apia-standard
cp manifests/hh-ru/apia.json manifests/your-api-id/apia.json
# edit the file
git add manifests/your-api-id/apia.json
git commit -m "feat: add YourAPI manifest"
git push origin your-branch
# open Pull Request on GitHub
```

## What happens after you open a PR

1. **Automated validation** runs immediately — checks JSON Schema compliance
2. **Community reviews** — anyone can comment or vote with 👍
3. **3 or more 👍** on the PR → auto-merges into the registry
4. Maintainers can only block for clear policy violations

## Writing a great manifest

### The most important field: `description_for_ai`

This is what an AI agent reads to decide whether to use your API. Write it like you're explaining to a smart assistant, not documenting for a developer.

**❌ Don't:**
```json
"description_for_ai": "REST API with OAuth2 authentication providing paginated JSON responses"
```

**✅ Do:**
```json
"description_for_ai": "World weather data for any city or coordinates. Use when user asks about current temperature, rain forecast, or weekly weather. Works globally. Free tier available."
```

### `intent` — how users actually speak

List phrases real users say that should trigger this API. Include multiple languages if the API serves non-English speakers.

```json
"intent": [
  "what's the weather", "is it raining", "temperature today",
  "погода сейчас", "какая погода", "идёт ли дождь"
]
```

### `agent_hints` — the knowledge that saves debugging hours

Capture the non-obvious things: coordinate order gotchas, units, pagination quirks, which fields need extra auth.

```json
"agent_hints": {
  "coords_warning": "This API uses lng,lat order (longitude first) — NOT the usual lat,lng. Easy to mix up.",
  "units_tip": "Default unit is Kelvin. Pass units=metric for Celsius.",
  "free_tier": "Free tier resets monthly, not daily. Plan accordingly."
}
```

## Manifest quality tiers

Your PR will be tagged automatically based on completeness:

| Tier | Requirements |
|---|---|
| ✅ **Verified** | All required fields, tested endpoint, meaningful agent_hints |
| 🔶 **Draft** | All required fields, endpoint not tested |
| ⚠️ **Partial** | Stub with docs link — for APIs that need more research |

Even a ⚠️ Partial manifest is valuable — it signals that an API exists and invites someone with access to complete it.

## Updating an existing manifest

Found outdated info? Just open a PR with the fix. Small corrections (wrong endpoint, outdated version) can be merged by any maintainer without votes.

## Deprecating a manifest

If an API has shut down or fundamentally changed, open a PR that sets:
```json
"meta": {
  "status": "deprecated",
  "deprecation_note": "API shut down on 2026-01-01. Use AlternativeAPI instead."
}
```

## What we don't accept

- Private or internal APIs (must be publicly documented)
- APIs that require NDA to access documentation
- Duplicate manifests (check existing ones first)
- Manifests that exist only to promote a commercial product without real utility

## Questions?

Open a [Discussion](../../discussions) — the community is friendly.