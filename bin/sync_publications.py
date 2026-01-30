#!/usr/bin/env python3
"""Sync Google Scholar publications into _bibliography/papers.bib."""

from __future__ import annotations

import argparse
import os
import re
import sys
import textwrap
import time
from pathlib import Path
from typing import Iterable, List

DEFAULT_AUTHOR_ID = "3Cz_lcEAAAAJ"
MAX_RETRIES = 3
RETRY_DELAYS = [5, 15, 30]  # Exponential backoff delays in seconds

try:
    from scholarly import scholarly, ProxyGenerator  # type: ignore
except ImportError as exc:  # pragma: no cover
    raise SystemExit(
        "scholarly is required. Install dependencies with `pip install -r requirements.txt`."
    ) from exc


def setup_proxy(verbose: bool) -> bool:
    """Configure a free proxy to avoid Google Scholar rate limiting.

    Returns True if proxy setup succeeded, False otherwise.
    """
    try:
        pg = ProxyGenerator()
        # Try FreeProxies first (free rotating proxies)
        success = pg.FreeProxies()
        if success:
            scholarly.use_proxy(pg)
            if verbose:
                print("[proxy] Configured free rotating proxy", file=sys.stderr)
            return True
    except Exception as e:
        if verbose:
            print(f"[proxy] Failed to set up proxy: {e}", file=sys.stderr)
    return False


def retry_with_backoff(func, max_retries: int = MAX_RETRIES, verbose: bool = False):
    """Execute function with exponential backoff retries."""
    last_exception = None
    for attempt in range(max_retries):
        try:
            return func()
        except Exception as e:
            last_exception = e
            if attempt < max_retries - 1:
                delay = RETRY_DELAYS[min(attempt, len(RETRY_DELAYS) - 1)]
                if verbose:
                    print(f"[retry] Attempt {attempt + 1} failed: {e}. Retrying in {delay}s...", file=sys.stderr)
                time.sleep(delay)
            else:
                if verbose:
                    print(f"[retry] All {max_retries} attempts failed", file=sys.stderr)
    raise last_exception


def parse_args(argv: Iterable[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Fetch the latest publications from Google Scholar and overwrite a BibTeX file.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent(
            """\
            You can avoid passing --author-id each run by exporting SCHOLAR_AUTHOR_ID.
            Example:
              SCHOLAR_AUTHOR_ID=<ID> bin/sync_publications.py --max-results 80
            """
        ),
    )
    parser.add_argument(
        "--author-id",
        default=os.environ.get("SCHOLAR_AUTHOR_ID", DEFAULT_AUTHOR_ID),
        help=(
            "Google Scholar author identifier (e.g., nYlXfJ4AAAAJ). Defaults to the "
            "SCHOLAR_AUTHOR_ID environment variable or the site default."
        ),
    )
    parser.add_argument(
        "--dest",
        default="_bibliography/papers.bib",
        help="Destination BibTeX path (default: %(default)s).",
    )
    parser.add_argument(
        "--max-results",
        type=int,
        default=120,
        help="Maximum number of publications to fetch (default: %(default)s).",
    )
    parser.add_argument(
        "--sleep",
        type=float,
        default=2.0,
        help="Seconds to sleep between publication fetches to stay polite (default: %(default)s).",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Emit progressing logs.",
    )
    parser.add_argument(
        "--no-proxy",
        action="store_true",
        help="Disable automatic proxy configuration (use direct connection).",
    )
    parser.add_argument(
        "--max-retries",
        type=int,
        default=MAX_RETRIES,
        help=f"Maximum retry attempts for failed requests (default: {MAX_RETRIES}).",
    )
    return parser.parse_args(list(argv))


def fetch_publications(author_id: str, max_results: int, delay: float, verbose: bool, use_proxy: bool = True) -> List[str]:
    # Set up proxy to avoid rate limiting in CI environments
    if use_proxy:
        setup_proxy(verbose)

    if verbose:
        print(f"Looking up author profile for {author_id}", file=sys.stderr)

    # Use retry logic for the initial author lookup (most likely to fail)
    def lookup_author():
        return scholarly.search_author_id(author_id)

    author = retry_with_backoff(lookup_author, verbose=verbose)
    author = scholarly.fill(author, sections=["publications"])
    publications = author.get("publications", [])[:max_results]

    entries: List[str] = []
    seen_keys: set[str] = set()

    for index, publication in enumerate(publications, start=1):
        try:
            filled = scholarly.fill(publication)
            bibtex = scholarly.bibtex(filled)
        except Exception as exc:  # pragma: no cover - network variability
            print(f"[warn] Failed to retrieve publication {publication.get('bib', {}).get('title')!r}: {exc}", file=sys.stderr)
            continue

        key = extract_bibtex_key(bibtex)
        if not key:
            print("[warn] Unable to extract BibTeX key; skipping entry.", file=sys.stderr)
            continue

        if key in seen_keys:
            if verbose:
                print(f"[skip] Duplicate key {key}", file=sys.stderr)
            continue

        entries.append(bibtex.strip())
        seen_keys.add(key)

        if verbose:
            title = publication.get("bib", {}).get("title", "Untitled")
            print(f"[ok] {index:02d}: {title}", file=sys.stderr)

        if delay:
            time.sleep(delay)

    return entries


def extract_bibtex_key(bibtex: str) -> str | None:
    match = re.search(r"@\w+\{([^,]+),", bibtex)
    return match.group(1).strip() if match else None


def write_bibtex(entries: List[str], destination: Path, verbose: bool) -> int:
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text("\n\n".join(entries) + "\n", encoding="utf-8")
    if verbose:
        print(f"[done] Wrote {len(entries)} entries to {destination}", file=sys.stderr)
    return len(entries)


def main(argv: Iterable[str]) -> int:
    args = parse_args(argv)
    if not args.author_id:
        print("Error: provide --author-id or set SCHOLAR_AUTHOR_ID.", file=sys.stderr)
        return 2

    destination = Path(args.dest)

    entries = fetch_publications(
        args.author_id,
        args.max_results,
        args.sleep,
        args.verbose,
        use_proxy=not args.no_proxy,
    )
    if not entries:
        print("Warning: received zero publications; destination file left untouched.", file=sys.stderr)
        return 1

    write_bibtex(entries, destination, args.verbose)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
