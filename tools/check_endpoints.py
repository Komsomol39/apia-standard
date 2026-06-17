#!/usr/bin/env python3
"""
tools/check_endpoints.py

Checks that api_base URLs in all APIA manifests are reachable.
Writes results to endpoint-health.json and exits with code 1 if
more than 20% of endpoints are unreachable.

Usage:
  python tools/check_endpoints.py
  python tools/check_endpoints.py --fail-threshold 30
  python tools/check_endpoints.py --output report.json
"""
import json, sys, time, argparse, urllib.request, urllib.error
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone

REPO_ROOT = Path(__file__).parent.parent
TIMEOUT = 8
MAX_WORKERS = 20

def check_url(url):
    """
    Returns (status_code, latency_ms, error_message).
    Treats 401/403/405/429 as ALIVE — auth required but server responds.
    """
    if not url or url == "TODO":
        return None, 0, "no url"
    # Normalize: strip trailing slash, add https if missing
    if not url.startswith("http"):
        url = "https://" + url
    url = url.rstrip("/")
    start = time.time()
    try:
        req = urllib.request.Request(url, method="HEAD", headers={
            "User-Agent": "APIA-HealthCheck/1.0 (+https://github.com/Komsomol39/apia-standard)"
        })
        with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
            latency = int((time.time() - start) * 1000)
            return r.status, latency, None
    except urllib.error.HTTPError as e:
        latency = int((time.time() - start) * 1000)
        # These codes mean server is alive, just needs auth/different method
        if e.code in (401, 403, 405, 429, 301, 302, 307, 308):
            return e.code, latency, None
        return e.code, latency, str(e)
    except urllib.error.URLError as e:
        latency = int((time.time() - start) * 1000)
        return None, latency, str(e.reason)
    except Exception as e:
        latency = int((time.time() - start) * 1000)
        return None, latency, str(e)

def is_alive(status_code, error):
    """Server is considered alive if we got any HTTP response."""
    if error and status_code is None:
        return False
    return True

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--fail-threshold", type=int, default=20,
                        help="Fail if more than N%% of endpoints are down (default: 20)")
    parser.add_argument("--output", default="endpoint-health.json")
    parser.add_argument("--verbose", action="store_true")
    args = parser.parse_args()

    # Load all manifests
    manifests = sorted(REPO_ROOT.glob("manifests/*/apia.json"))
    print(f"Checking {len(manifests)} manifests...")

    # Collect unique URLs
    entries = []
    seen_urls = {}
    for mp in manifests:
        data = json.loads(mp.read_text())
        svc = data.get("service", {})
        api_id = svc.get("id", mp.parent.name)
        api_base = svc.get("api_base", svc.get("url", ""))
        if not api_base or api_base == "TODO":
            entries.append({"id": api_id, "url": api_base, "skip": True})
            continue
        if api_base in seen_urls:
            # Reuse result from same URL
            entries.append({"id": api_id, "url": api_base, "shared_with": seen_urls[api_base]})
        else:
            seen_urls[api_base] = api_id
            entries.append({"id": api_id, "url": api_base, "skip": False})

    # Check unique URLs in parallel
    to_check = [(e["id"], e["url"]) for e in entries if not e.get("skip") and not e.get("shared_with")]
    results = {}

    print(f"Checking {len(to_check)} unique endpoints ({MAX_WORKERS} parallel)...")

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        future_to_id = {
            executor.submit(check_url, url): (api_id, url)
            for api_id, url in to_check
        }
        done = 0
        for future in as_completed(future_to_id):
            api_id, url = future_to_id[future]
            status, latency, error = future.result()
            alive = is_alive(status, error)
            results[url] = {
                "status": status,
                "latency_ms": latency,
                "error": error,
                "alive": alive,
            }
            done += 1
            if done % 20 == 0 or args.verbose:
                icon = "✅" if alive else "❌"
                print(f"  [{done}/{len(to_check)}] {icon} {api_id}: {status or 'ERR'} {latency}ms")

    # Build final report
    report_entries = []
    alive_count = 0
    dead_count = 0
    skip_count = 0

    for entry in entries:
        api_id = entry["id"]
        url = entry["url"]

        if entry.get("skip"):
            report_entries.append({"id": api_id, "url": url, "alive": None, "note": "no url"})
            skip_count += 1
            continue

        shared = entry.get("shared_with")
        lookup_url = url
        r = results.get(lookup_url, {})
        alive = r.get("alive", False)

        report_entries.append({
            "id": api_id,
            "url": url,
            "alive": alive,
            "status": r.get("status"),
            "latency_ms": r.get("latency_ms"),
            "error": r.get("error"),
            "shared_with": shared,
        })

        if alive:
            alive_count += 1
        else:
            dead_count += 1
            if args.verbose or not alive:
                print(f"  DEAD: {api_id} | {url} | {r.get('error','')}")

    total_checked = alive_count + dead_count
    dead_pct = (dead_count / total_checked * 100) if total_checked > 0 else 0

    report = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "summary": {
            "total": len(manifests),
            "checked": total_checked,
            "alive": alive_count,
            "dead": dead_count,
            "skipped": skip_count,
            "dead_pct": round(dead_pct, 1),
        },
        "entries": report_entries,
    }

    output_path = REPO_ROOT / args.output
    output_path.write_text(json.dumps(report, indent=2))

    print(f"\n{'='*50}")
    print(f"Results: {alive_count} alive, {dead_count} dead, {skip_count} skipped")
    print(f"Dead rate: {dead_pct:.1f}%")
    print(f"Report: {output_path}")

    if dead_pct > args.fail_threshold:
        print(f"FAIL: dead rate {dead_pct:.1f}% > threshold {args.fail_threshold}%")
        sys.exit(1)
    else:
        print(f"OK: dead rate within threshold ({args.fail_threshold}%)")

if __name__ == "__main__":
    main()
