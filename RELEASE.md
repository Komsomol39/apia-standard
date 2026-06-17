# Release Process

## Versioning

APIA follows [Semantic Versioning](https://semver.org/):

- **PATCH** `1.0.x` — manifest fixes, tooling bugfixes, new manifests
- **MINOR** `1.x.0` — new optional schema fields, new CLI commands
- **MAJOR** `x.0.0` — breaking schema changes (require migration guide)

## Release checklist

```bash
# 1. Ensure CI is green on main
# 2. Update CHANGELOG.md — add release date to [Unreleased] section
# 3. Bump version in pyproject.toml
# 4. Create and push tag
git tag -a v1.0.1 -m "Release v1.0.1"
git push origin v1.0.1
# 5. GitHub Actions auto-publishes to PyPI and creates GitHub Release
```

## What gets released

- Git tag `vX.Y.Z` on main
- GitHub Release with changelog excerpt
- PyPI package `apia-cli==X.Y.Z`

## Hotfix process

For urgent fixes (dead endpoint, security issue):
1. Branch from main: `git checkout -b hotfix/description`
2. Fix + test
3. PR → main
4. Tag immediately after merge

## Roadmap

| Version | Focus |
|---------|-------|
| v1.0.0  | ✅ Initial release — 260 manifests, CLI, CI, schema |
| v1.1.0  | `agent_hints.examples` field, `apia test` command |
| v1.2.0  | Multi-capability chaining in manifests |
| v2.0.0  | Breaking: structured `output.schema` (JSON Schema for response) |
