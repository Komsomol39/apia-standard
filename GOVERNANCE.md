# Governance

## Current status

APIA is currently maintained by a single maintainer.
The governance model will evolve as the community grows.

## Decision making

### Schema changes (breaking)
Any change that invalidates existing manifests requires:
1. Open a GitHub Issue with label `schema-change`
2. Discussion period: minimum 14 days
3. Maintainer approval + at least 2 community thumbs-up
4. Migration guide added to `docs/`
5. Version bump: `v1.x.0` for additive, `v2.0.0` for breaking

### New manifests
Pull requests adding new API manifests are reviewed within 7 days.
CI must pass. A brief human review checks description quality.

### Tooling changes (CLI, scripts)
Standard PR process. CI must pass.

## Roles

| Role | Responsibilities |
|------|-----------------|
| **Maintainer** | Schema decisions, releases, security |
| **Contributor** | PR submissions, issue reports |
| **Reviewer** | PR review (any community member) |

## Becoming a maintainer

After 5+ merged PRs and demonstrated understanding of the standard,
open an issue requesting maintainer access.

## RFC process

For significant changes, open an issue titled `RFC: <title>` with:
- Problem statement
- Proposed change to schema or tooling
- Backward compatibility impact
- Examples

RFCs stay open for 14 days before a decision is made.

## Release process

See [RELEASE.md](RELEASE.md).
