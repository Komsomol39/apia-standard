# APIA Changelog

## [Unreleased]

### Planned for v1.1.0
- `agent_hints.examples` — concrete usage examples in manifests
- `apia test` CLI command — actually call an API and validate response
- `apia diff` — compare two versions of a manifest

---

## [1.0.0] — 2026-06-17

### Standard
- Initial release of APIA 1.0 schema
- Core manifest structure: `service`, `auth`, `capabilities`, `agent_hints`, `meta`
- Required fields: `description_for_ai`, `intent` (min 2 phrases), `endpoint`, `input`, `output`
- `anonymous_access` flag for auth-free capabilities
- `realtime` flag to distinguish live vs cached data
- `agent_hints`: `rate_limiting`, `pagination`, `errors`, `best_practices`

### Registry
- 260 API manifests across 26 categories
- Categories: ai, analytics, business, devtools, ecommerce, finance, food, healthcare,
  hr, iot, legal, logistics, maps, media, messaging, payments, real_estate, search,
  social, travel, utilities, weather, and more

### Tooling
- `cli/apia.py` — validate, search, inspect, build-prompt
- `tools/openapi2apia.py` — OpenAPI 3.x to APIA converter
- `tests/test_manifests.py` — full pytest suite
- `.github/workflows/ci.yml` — CI for every PR

---

## Backward Compatibility Policy

APIA follows semantic versioning:

- **Patch (1.0.x)**: bug fixes in schema, no breaking changes
- **Minor (1.x.0)**: new optional fields added, all existing manifests remain valid
- **Major (x.0.0)**: breaking changes, migration guide required

### What counts as breaking
- Removing or renaming required fields
- Changing field types
- Changing minimum cardinality (e.g. intent min phrases)

### What does NOT break compatibility
- Adding new optional fields
- Adding new allowed values to enum fields
- Adding new categories to the registry

### Migration policy
Breaking changes will be announced 3 months in advance with a migration guide.
Old schema versions will be supported for 6 months after a major release.
