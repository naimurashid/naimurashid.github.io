#!/usr/bin/env python3
"""Fetch recent social posts into _data/social_staging.yml.

The script reads source definitions from `_data/social_sources.yml` and collects
posts published within the last two years. Use it locally or via CI to refresh
the staging list, then copy the desired items into `_data/social_curated.yml`.
"""

from __future__ import annotations

import argparse
import datetime as dt
import sys
from pathlib import Path
from typing import Iterable, List, Sequence

import feedparser  # type: ignore
import yaml

ROOT = Path(__file__).resolve().parents[1]
SOURCES_FILE = ROOT / "_data" / "social_sources.yml"
STAGING_FILE = ROOT / "_data" / "social_staging.yml"
DEFAULT_WINDOW_DAYS = 730  # two years


def parse_args(argv: Sequence[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--window-days",
        type=int,
        default=DEFAULT_WINDOW_DAYS,
        help="Number of trailing days to keep (default: %(default)s).",
    )
    parser.add_argument(
        "--max-per-source",
        type=int,
        default=60,
        help="Maximum posts per source to consider (default: %(default)s).",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Print progress information.",
    )
    return parser.parse_args(list(argv))


def load_sources() -> List[dict]:
    if not SOURCES_FILE.exists():
        raise SystemExit(f"Missing sources config: {SOURCES_FILE}")
    with SOURCES_FILE.open(encoding="utf-8") as handle:
        data = yaml.safe_load(handle) or []
    if not isinstance(data, list):
        raise SystemExit("Expected a list of sources in social_sources.yml")
    return [source for source in data if source.get("rss_url")]


def normalise_date(entry) -> dt.datetime | None:
    for attr in ("published_parsed", "updated_parsed"):
        parsed = getattr(entry, attr, None)
        if parsed:
            return dt.datetime(*parsed[:6], tzinfo=dt.timezone.utc)
    if "published_parsed" in entry:
        struct = entry.published_parsed
        if struct:
            return dt.datetime(*struct[:6], tzinfo=dt.timezone.utc)
    if "updated_parsed" in entry:
        struct = entry.updated_parsed
        if struct:
            return dt.datetime(*struct[:6], tzinfo=dt.timezone.utc)
    return None


def trim_summary(text: str | None, limit: int = 260) -> str | None:
    if not text:
        return None
    clean = " ".join(text.split())
    if len(clean) <= limit:
        return clean
    return clean[: limit - 1].rstrip() + "…"


def collect_posts(sources: Iterable[dict], window_days: int, max_per_source: int, verbose: bool) -> List[dict]:
    cutoff = dt.datetime.now(dt.timezone.utc) - dt.timedelta(days=window_days)
    collected: List[dict] = []

    for source in sources:
        rss_url = source.get("rss_url")
        label = source.get("label") or source.get("platform") or "Update"
        platform = source.get("platform") or label

        if verbose:
            print(f"[fetch] {label}: {rss_url}", file=sys.stderr)

        feed = feedparser.parse(rss_url)
        entries = getattr(feed, "entries", [])[:max_per_source]

        for entry in entries:
            published = normalise_date(entry)
            if not published or published < cutoff:
                continue

            title = entry.get("title", "Untitled update").strip()
            link = entry.get("link")
            summary = entry.get("summary") or entry.get("description")
            collected.append(
                {
                    "date": published.isoformat(),
                    "platform": label,
                    "title": title,
                    "url": link,
                    "summary": trim_summary(summary),
                    "source": {
                        "platform": platform,
                        "handle": source.get("handle"),
                        "rss_url": rss_url,
                    },
                }
            )

    collected.sort(key=lambda item: item["date"], reverse=True)
    return collected


def write_yaml(entries: List[dict], destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    with destination.open("w", encoding="utf-8") as handle:
        yaml.safe_dump(
            entries,
            handle,
            sort_keys=False,
            allow_unicode=True,
            default_flow_style=False,
        )


def main(argv: Sequence[str]) -> int:
    args = parse_args(argv)
    sources = load_sources()
    entries = collect_posts(sources, args.window_days, args.max_per_source, args.verbose)
    write_yaml(entries, STAGING_FILE)
    if args.verbose:
        print(f"[done] Wrote {len(entries)} entries to {STAGING_FILE}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
