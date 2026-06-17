# Security Policy

## Supported Versions

| Version | Supported |
|---------|-----------|
| 1.0.x   | ✅ Yes    |

## Reporting a Vulnerability

If you discover a security issue in APIA — for example:
- A manifest pointing to a malicious or phishing endpoint
- Schema validation bypass that allows injecting harmful content
- A capability description designed to mislead AI agents

Please **do not open a public GitHub issue**.

Instead, report privately via GitHub Security Advisories:
**https://github.com/Komsomol39/apia-standard/security/advisories/new**

You will receive a response within **72 hours**.

## Scope

APIA is a description standard — it does not execute code or handle credentials directly.
Security concerns most relevant to this project:

- **Malicious manifests** — endpoints designed to exfiltrate data when called by an AI agent
- **Prompt injection** — `description_for_ai` or `intent` fields crafted to hijack agent behavior
- **Schema bypass** — techniques to pass validation with harmful content

## Out of scope

- Vulnerabilities in APIs described by APIA manifests (report to those API providers)
- General security of AI agents that happen to use APIA
