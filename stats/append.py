#!/usr/bin/env python3
"""Append today's download snapshot to stats/downloads.json.

GitHub only exposes a *cumulative* per-asset download_count, so "downloads
today" is derived here as (today's cumulative total - the previous day's
cumulative total). Run once a day by .github/workflows/track-downloads.yml.

Usage:  python3 stats/append.py <total:int> [<by_version:json>]
"""
import datetime
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "downloads.json")


def load():
    try:
        with open(DATA, encoding="utf-8") as f:
            d = json.load(f)
    except (FileNotFoundError, ValueError):
        d = {}
    d.setdefault("series", [])
    d.setdefault("by_version", {})
    return d


def main():
    if len(sys.argv) < 2:
        sys.exit("usage: append.py <total:int> [<by_version:json>]")
    total = int(sys.argv[1])
    by_version = json.loads(sys.argv[2]) if len(sys.argv) > 2 and sys.argv[2] else None

    today = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d")
    d = load()
    series = d["series"]

    # The baseline for today's delta is the most recent entry from a PRIOR day.
    prior_total = 0
    for e in reversed(series):
        if e.get("date") != today:
            prior_total = int(e.get("total", 0))
            break

    # download_count is monotonic; clamp so a GitHub-side reset never shows
    # a negative day.
    daily = max(0, total - prior_total)
    entry = {"date": today, "total": total, "daily": daily}

    if series and series[-1].get("date") == today:
        series[-1] = entry        # idempotent re-run on the same day
    else:
        series.append(entry)

    if by_version is not None:
        d["by_version"] = by_version
    d["updated"] = datetime.datetime.now(datetime.timezone.utc).strftime(
        "%Y-%m-%dT%H:%MZ"
    )

    with open(DATA, "w", encoding="utf-8") as f:
        json.dump(d, f, ensure_ascii=False, indent=2)
        f.write("\n")
    print(f"snapshot {today}: total={total} daily={daily}")


if __name__ == "__main__":
    main()
