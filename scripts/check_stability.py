"""Stability check for synthesis rewrites.

Enforces three invariants between the git-committed version of a doc and its
newly-written version:

1. Every `[^pmid:...]` / `[^doi:...]` citation in the prior version must still
   appear somewhere in the new version. Claims can move between tier sections
   (e.g. `established` → `contested`), but a landmark citation cannot vanish.
2. The new version must not shrink to less than 70% of the prior word count.
3. No tier section heading may disappear entirely. If the prior file had
   "## Confidently known", the new version must still have it.

Non-zero exit aborts the commit. Log to stderr.

Usage:
    python scripts/check_stability.py --old-ref HEAD --new docs/index.md
    python scripts/check_stability.py --old-file /tmp/before.md --new docs/index.md
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

CITE_RE = re.compile(r"\[\^(?:pmid|doi):([^\]]+)\]")
TIER_HEADING_RE = re.compile(
    r"^##\s*(What has held up|Where the field has contradicted itself"
    r"|Suspected but unconfirmed|New directions worth watching"
    r"|Confidently known|Contradictions / surprises|Emerging)",
    re.MULTILINE,
)


def collect_citations(text: str) -> set[str]:
    return set(CITE_RE.findall(text))


def collect_tier_headings(text: str) -> set[str]:
    return set(TIER_HEADING_RE.findall(text))


def load_old(args: argparse.Namespace, new_path: str) -> str | None:
    """Load the prior version. Returns None if no prior version exists."""
    if args.old_file:
        p = Path(args.old_file)
        return p.read_text() if p.exists() else None
    # --old-ref path: read via git show. If the file did not exist at that ref,
    # git returns non-zero — treat as "no prior version, skip check".
    result = subprocess.run(
        ["git", "show", f"{args.old_ref}:{new_path}"],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        return None
    return result.stdout


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--old-ref", help='git ref (e.g. "HEAD") to read prior version from')
    ap.add_argument("--old-file", help="path to a prior-version snapshot")
    ap.add_argument("--new", required=True, help="path to the new version (under git repo root)")
    ap.add_argument(
        "--min-retention",
        type=float,
        default=0.7,
        help="minimum word-count retention (default 0.7 = cannot shrink below 70%%)",
    )
    args = ap.parse_args()
    if not args.old_ref and not args.old_file:
        print("[stability] must provide --old-ref or --old-file", file=sys.stderr)
        sys.exit(2)

    new_text = Path(args.new).read_text()
    old_text = load_old(args, args.new)
    if old_text is None:
        print(f"[stability] {args.new}: no prior version — skipping (first-time file)")
        return

    old_cites = collect_citations(old_text)
    new_cites = collect_citations(new_text)
    missing = sorted(old_cites - new_cites)
    added = sorted(new_cites - old_cites)

    old_headings = collect_tier_headings(old_text)
    new_headings = collect_tier_headings(new_text)
    dropped_headings = sorted(old_headings - new_headings)

    old_words = len(old_text.split())
    new_words = len(new_text.split())
    retention = new_words / old_words if old_words else 1.0

    fails: list[str] = []
    if missing:
        fails.append(
            f"{len(missing)} prior citation(s) dropped from {args.new}: {missing}"
        )
    if dropped_headings:
        fails.append(
            f"tier heading(s) removed from {args.new}: {dropped_headings}"
        )
    if retention < args.min_retention:
        fails.append(
            f"word count dropped too far in {args.new}: "
            f"{old_words} -> {new_words} (retention {retention:.0%}, min {args.min_retention:.0%})"
        )

    if fails:
        for line in fails:
            print(f"[stability] FAIL {line}", file=sys.stderr)
        sys.exit(1)

    print(
        f"[stability] OK {args.new}: "
        f"{len(old_cites)} citations preserved, +{len(added)} added, "
        f"words {old_words}→{new_words} ({retention:.0%})"
    )


if __name__ == "__main__":
    main()
