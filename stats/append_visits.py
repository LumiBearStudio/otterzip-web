#!/usr/bin/env python3
"""Upsert one day's page-visit count into stats/visits.json.

Fed by .github/workflows/pull-visits.yml, which reads the daily UTC pageview
total from the GoatCounter API (cookieless, no PII). Kept separate from the
download series so each can be enabled independently.

Usage:  python3 stats/append_visits.py <date:YYYY-MM-DD> <visits:int>
"""
import datetime
import json
import os
import sys

DATA = os.path.join(os.path.dirname(os.path.abspath(__file__)), "visits.json")


def main():
    if len(sys.argv) < 3:
        sys.exit("usage: append_visits.py <date> <visits:int>")
    date = sys.argv[1]
    visits = max(0, int(sys.argv[2]))

    try:
        with open(DATA, encoding="utf-8") as f:
            d = json.load(f)
    except (FileNotFoundError, ValueError):
        d = {}
    d.setdefault("series", [])

    entry = {"date": date, "visits": visits}
    series = d["series"]
    # Upsert: replace the same date, else append; keep chronological order.
    for i, e in enumerate(series):
        if e.get("date") == date:
            series[i] = entry
            break
    else:
        series.append(entry)
    series.sort(key=lambda e: e.get("date", ""))

    d["updated"] = datetime.datetime.now(datetime.timezone.utc).strftime(
        "%Y-%m-%dT%H:%MZ"
    )
    with open(DATA, "w", encoding="utf-8") as f:
        json.dump(d, f, ensure_ascii=False, indent=2)
        f.write("\n")
    print(f"visits {date}: {visits}")


if __name__ == "__main__":
    main()
