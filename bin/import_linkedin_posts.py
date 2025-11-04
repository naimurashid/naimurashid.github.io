#!/usr/bin/env python3
"""Convert a LinkedIn data export CSV into social staging entries.

Usage:
    bin/import_linkedin_posts.py --csv path/to/Shares.csv

The script reads the CSV that LinkedIn emails when you request a "Posts"
export (usually named `Shares.csv` or `Posts.csv`) and merges the most
recent updates into `_data/social_staging.yml`. You can then copy the
highlights you want to publish into `_data/social_curated.yml`.
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import sys
from pathlib import Path
from typing import Iterable, List, Sequence

import yaml

ROOT = Path(__file__).resolve().parents[1]
STAGING_FILE = ROOT / "_data" / "social_staging.yml"

DATE_PATTERNS = (
    "%Y-%m-%d %H:%M:%S %Z",  # 2024-05-07 14:25:58 UTC
    "%Y-%m-%d %H:%M:%S",  # naive timestamp
    "%Y-%m-%dT%H:%M:%S.%fZ",  # 2024-05-07T14:25:58.123Z
    "%Y-%m-%dT%H:%M:%SZ",  # 2024-05-07T14:25:58Z
)


def parse_args(argv: Sequence[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--csv",
        required=True,
        help="Path to the LinkedIn Shares/Posts CSV export.",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=100,
        help="Maximum entries to import (default: %(default)s).",
    )
    parser.add_argument(
        "--since-days",
        type=int,
        default=730,
        help="Only include posts newer than this many days (default: %(default)s).",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Print progress information.",
    )
    return parser.parse_args(list(argv))


def parse_date(raw: str) -> dt.datetime | None:
    raw = raw.strip()
    if not raw:
        return None
    for pattern in DATE_PATTERNS:
        try:
            parsed = dt.datetime.strptime(raw, pattern)
            if parsed.tzinfo is None:
                parsed = parsed.replace(tzinfo=dt.timezone.utc)
            return parsed.astimezone(dt.timezone.utc)
        except ValueError:
            continue
    return None


def trim(text: str | None, limit: int = 260) -> str | None:
    if not text:
        return None
    cleaned = " ".join(text.replace('""', '"').split())
    if len(cleaned) <= limit:
        return cleaned
    return cleaned[: limit - 1].rstrip() + "…"


def load_existing() -> List[dict]:
    if not STAGING_FILE.exists():
        return []
    try:
        with STAGING_FILE.open(encoding="utf-8") as handle:
            data = yaml.safe_load(handle) or []
        if isinstance(data, list):
            return data
    except Exception:  # pragma: no cover - best effort
        pass
    return []


def load_csv(path: Path, since_days: int, limit: int, verbose: bool) -> List[dict]:
    cutoff = dt.datetime.now(dt.timezone.utc) - dt.timedelta(days=since_days)
    entries: List[dict] = []

    with path.open(encoding="utf-8-sig") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            raw_date = row.get("Created Date") or row.get("Date")
            permalink = row.get("Permalink") or row.get("ShareLink")
            commentary = (
                row.get("Share Commentary")
                or row.get("ShareCommentary")
                or row.get("Commentary")
                or row.get("Text")
            )

            if not raw_date or not permalink:
                continue

            created = parse_date(raw_date)
            if not created or created < cutoff:
                continue

            entry = {
                "date": created.isoformat(),
                "platform": "LinkedIn",
                "title": trim(commentary, limit=120) or "LinkedIn update",
                "url": permalink,
                "summary": trim(commentary),
                "source": {
                    "platform": "LinkedIn",
                    "csv": str(path),
                },
            }
            entries.append(entry)

    entries.sort(key=lambda item: item["date"], reverse=True)
    if verbose:
        print(f"[linkedin] extracted {len(entries)} entries from {path}", file=sys.stderr)
    return entries[:limit]


def deduplicate(entries: Iterable[dict]) -> List[dict]:
    seen = set()
    unique: List[dict] = []
    for entry in entries:
        key = entry.get("url") or (entry.get("platform"), entry.get("date"))
        if key in seen:
            continue
        seen.add(key)
        unique.append(entry)
    unique.sort(key=lambda item: item["date"], reverse=True)
    return unique


def write(entries: List[dict], verbose: bool) -> None:
    STAGING_FILE.parent.mkdir(parents=True, exist_ok=True)
    with STAGING_FILE.open("w", encoding="utf-8") as handle:
        yaml.safe_dump(entries, handle, sort_keys=False, default_flow_style=False, allow_unicode=True)
    if verbose:
        print(f"[done] wrote {len(entries)} entries to {STAGING_FILE}", file=sys.stderr)


def main(argv: Sequence[str]) -> int:
    args = parse_args(argv)
    csv_path = Path(args.csv).expanduser()
    if not csv_path.exists():
        print(f"Error: CSV not found at {csv_path}", file=sys.stderr)
        return 2

    existing = load_existing()
    imported = load_csv(csv_path, since_days=args.since_days, limit=args.limit, verbose=args.verbose)

    combined = deduplicate(imported + existing)
    write(combined, args.verbose)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
