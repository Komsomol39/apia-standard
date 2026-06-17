#!/usr/bin/env python3
"""
tools/check_endpoints.py

Checks reachability of all APIA manifest api_base URLs.
For each dead endpoint also resolves its geo-country via ipwho.is.
Russian/CIS endpoints that timeout from GitHub Actions (US) are
auto-flagged as GEO_BLOCKED rather than DEAD.

Usage:
  python tools/check_endpoints.py [--fail-threshold 30] [--output endpoint-health.json]
"""
import json, sys, re, time, socket, argparse, urllib.request, urllib.error
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone

REPO_ROOT   = Path(__file__).parent.parent
TIMEOUT     = 8
MAX_WORKERS = 20

# Countries whose endpoints are routinely blocked from GitHub Actions (US IPs)
GEO_BLOCK_COUNTRIES = {"RU", "BY", "CN", "IR", "KP", "CU"}

TEMPLATE_RE = re.compile(r'\{[^}]+\}')   # matches {subdomain}, {region}, etc.

# ── Geo lookup ────────────────────────────────────────────────────────────

_geo_cache = {}

def resolve_ip(hostname):
    try:
        return socket.gethostbyname(hostname)
    except Exception:
        return None

def get_country(ip):
    """Returns ISO-2 country code via ipwho.is (free, no key, 60 req/min)."""
    if not ip:
        return None
    if ip in _geo_cache:
        return _geo_cache[ip]
    try:
        req = urllib.request.Request(
            f"http://ipwho.is/{ip}?fields=country_code",
            headers={"User-Agent": "APIA-HealthCheck/1.0"}
        )
        with urllib.request.urlopen(req, timeout=5) as r:
            data = json.loads(r.read())
        cc = data.get("country_code")
        _geo_cache[ip] = cc
        return cc
    except Exception:
        return None

# ── URL helpers ───────────────────────────────────────────────────────────

def is_template(url):
    """True if URL contains {variable} placeholders."""
    return bool(TEMPLATE_RE.search(url or ""))

def extract_hostname(url):
    url = url.strip()
    if not url.startswith("http"):
        url = "https://" + url
    try:
        from urllib.parse import urlparse
        return urlparse(url).hostname
    except Exception:
        return None

def check_url(url):
    """
    Tries HEAD then GET.
    Returns (status_code, latency_ms, error_str).
    401/403/405/429/3xx = server alive.
    """
    if not url.startswith("http"):
        url = "https://" + url.rstrip("/")
    start = time.time()
    for method in ("HEAD", "GET"):
        try:
            req = urllib.request.Request(url, method=method, headers={
                "User-Agent": "APIA-HealthCheck/1.0 (+https://github.com/Komsomol39/apia-standard)"
            })
            with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
                ms = int((time.time() - start) * 1000)
                return r.status, ms, None
        except urllib.error.HTTPError as e:
            ms = int((time.time() - start) * 1000)
            if e.code in (401, 403, 405, 429, 301, 302, 307, 308):
                return e.code, ms, None   # alive
            return e.code, ms, str(e)
        except urllib.error.URLError as e:
            ms = int((time.time() - start) * 1000)
            return None, ms, str(e.reason)
        except Exception as e:
            ms = int((time.time() - start) * 1000)
            return None, ms, str(e)
    return None, 0, "unreachable"

# ── Main ──────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--fail-threshold", type=int, default=20)
    parser.add_argument("--output", default="endpoint-health.json")
    parser.add_argument("--verbose", action="store_true")
    args = parser.parse_args()

    manifests = sorted(REPO_ROOT.glob("manifests/*/apia.json"))
    print(f"Loaded {len(manifests)} manifests")

    # Collect entries
    entries = []
    url_to_ids = {}
    for mp in manifests:
        data = json.loads(mp.read_text())
        svc  = data.get("service", {})
        api_id   = svc.get("id", mp.parent.name)
        api_base = svc.get("api_base") or svc.get("url", "")
        geo      = svc.get("geo", "")

        if is_template(api_base):
            entries.append({"id": api_id, "url": api_base, "status": "TEMPLATE",
                             "geo": geo, "alive": None, "note": "template url — not checkable"})
            continue

        if not api_base:
            entries.append({"id": api_id, "url": "", "status": "NO_URL",
                             "geo": geo, "alive": None, "note": "missing api_base"})
            continue

        url_to_ids.setdefault(api_base, []).append(api_id)
        entries.append({"id": api_id, "url": api_base, "geo": geo,
                        "_check": True})

    # Unique URLs to check
    unique_urls = list(url_to_ids.keys())
    print(f"Checking {len(unique_urls)} unique endpoints ({MAX_WORKERS} parallel)...")

    url_results = {}
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as ex:
        future_map = {ex.submit(check_url, u): u for u in unique_urls}
        done = 0
        for fut in as_completed(future_map):
            u = future_map[fut]
            status, ms, err = fut.result()
            alive = (status is not None) or (err is None)
            url_results[u] = {"status": status, "latency_ms": ms,
                               "error": err, "alive": alive}
            done += 1
            if done % 25 == 0 or args.verbose:
                icon = "✅" if alive else "❌"
                ids  = url_to_ids[u]
                print(f"  [{done}/{len(unique_urls)}] {icon} {ids[0]}: "
                      f"{status or 'ERR'} {ms}ms")

    # Geo-lookup for dead non-template endpoints
    print("\nResolving geo for dead endpoints...")
    dead_urls = [u for u, r in url_results.items() if not r["alive"]]
    for u in dead_urls:
        host = extract_hostname(u)
        ip   = resolve_ip(host) if host else None
        cc   = get_country(ip) if ip else None
        url_results[u]["country"] = cc
        url_results[u]["ip"]      = ip
        if args.verbose:
            print(f"  {host} -> {ip} -> {cc}")
        time.sleep(0.05)   # respect 60 req/min limit

    # Annotate entries
    alive_n = dead_n = template_n = geo_block_n = no_url_n = 0
    for e in entries:
        if not e.get("_check"):
            if e.get("status") == "TEMPLATE":
                template_n += 1
            elif e.get("status") == "NO_URL":
                no_url_n += 1
            continue

        r = url_results.get(e["url"], {})
        e["http_status"]   = r.get("status")
        e["latency_ms"]    = r.get("latency_ms")
        e["error"]         = r.get("error")
        e["country"]       = r.get("country")
        e["ip"]            = r.get("ip")
        e.pop("_check", None)

        if r.get("alive"):
            e["alive"]  = True
            e["status"] = "OK"
            alive_n += 1
        else:
            cc = r.get("country")
            if cc in GEO_BLOCK_COUNTRIES:
                e["alive"]  = None    # unknown — probably geo-blocked
                e["status"] = "GEO_BLOCKED"
                e["note"]   = f"Server in {cc} — likely blocked from GitHub Actions (US)"
                geo_block_n += 1
            else:
                e["alive"]  = False
                e["status"] = "DEAD"
                dead_n += 1

    total_checked = alive_n + dead_n + geo_block_n
    dead_pct = round(dead_n / total_checked * 100, 1) if total_checked else 0

    report = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "summary": {
            "total":       len(manifests),
            "alive":       alive_n,
            "dead":        dead_n,
            "geo_blocked": geo_block_n,
            "template":    template_n,
            "no_url":      no_url_n,
            "dead_pct":    dead_pct,
            "note": "dead_pct excludes geo_blocked (RU/BY/CN/IR endpoints)"
        },
        "entries": sorted(entries, key=lambda e: (
            0 if e.get("status") == "DEAD"        else
            1 if e.get("status") == "GEO_BLOCKED" else
            2 if e.get("status") == "TEMPLATE"    else
            3
        ))
    }

    out = REPO_ROOT / args.output
    out.write_text(json.dumps(report, indent=2, ensure_ascii=False))

    # Print summary
    print(f"\n{'='*55}")
    print(f"  Alive:        {alive_n}")
    print(f"  Dead:         {dead_n}  ({dead_pct}%)")
    print(f"  Geo-blocked:  {geo_block_n}  (RU/BY/CN/IR — checked separately)")
    print(f"  Template URL: {template_n}  (skipped — {'{var}'} in URL)")
    print(f"  No URL:       {no_url_n}")
    print(f"{'='*55}")

    if dead_n:
        print(f"\nDead endpoints:")
        for e in report["entries"]:
            if e.get("status") == "DEAD":
                print(f"  ❌ {e['id']:35} {e.get('error','')[:60]}")

    if geo_block_n:
        print(f"\nGeo-blocked (not counted as dead):")
        for e in report["entries"]:
            if e.get("status") == "GEO_BLOCKED":
                print(f"  🌍 {e['id']:35} {e.get('country','')} — {e.get('url','')[:40]}")

    print(f"\nReport: {out}")

    if dead_pct > args.fail_threshold:
        print(f"\nFAIL: {dead_pct}% dead > threshold {args.fail_threshold}%")
        sys.exit(1)
    print(f"OK: dead rate {dead_pct}% within threshold {args.fail_threshold}%")

if __name__ == "__main__":
    main()
