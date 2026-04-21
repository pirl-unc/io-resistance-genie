"""Fetch new literature from Europe PMC, dedup, and write the per-run diff.

Usage:
  python scripts/fetch.py --since 2024-01-01
  python scripts/fetch.py --since-last-run
  python scripts/fetch.py --dry-run
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

# Make `lib` importable whether run as a script or as a module.
sys.path.insert(0, str(Path(__file__).resolve().parent))

from lib.europepmc import build_query, search  # noqa: E402
from lib.schemas import Paper, Source  # noqa: E402

REPO_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = REPO_ROOT / "data"
RUN_DIR = REPO_ROOT / "run"
PAPERS_PATH = DATA_DIR / "papers.jsonl"
LAST_RUN_PATH = DATA_DIR / "last_run.json"


def source_of(rec: dict) -> Source:
    src = (rec.get("source") or "").upper()
    if src == "PPR":
        publisher = (
            rec.get("bookOrReportDetails", {}).get("publisher")
            or rec.get("publisher")
            or ""
        ).lower()
        if "biorxiv" in publisher:
            return Source.BIORXIV
        if "medrxiv" in publisher:
            return Source.MEDRXIV
        return Source.OTHER_PREPRINT
    return Source.PUBMED


def _extract_authors(rec: dict) -> list[str]:
    author_list = rec.get("authorList", {}).get("author", [])
    if author_list:
        return [a.get("fullName") for a in author_list if a.get("fullName")]
    author_string = rec.get("authorString")
    if author_string:
        return [a.strip() for a in author_string.split(",") if a.strip()]
    return []


def record_to_paper(rec: dict) -> Paper | None:
    """Normalize a Europe PMC record into the Paper schema. None if invalid."""
    title = rec.get("title")
    if not title:
        return None
    pmid = rec.get("pmid")
    pmcid = rec.get("pmcid")
    doi = rec.get("doi")
    canonical = pmid or doi or pmcid or rec.get("id")
    if not canonical:
        return None
    pub_date_str = rec.get("firstPublicationDate") or rec.get("firstIndexDate")
    pub_date: date | None = None
    if pub_date_str:
        try:
            pub_date = date.fromisoformat(pub_date_str)
        except ValueError:
            pub_date = None
    journal = (rec.get("journalInfo") or {}).get("journal", {}).get("title")
    is_oa = rec.get("isOpenAccess") == "Y"
    src = source_of(rec)
    url: str | None = None
    if pmid:
        url = f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/"
    elif doi:
        url = f"https://doi.org/{doi}"
    elif pmcid:
        url = f"https://europepmc.org/article/PMC/{pmcid}"
    return Paper(
        id=str(canonical),
        pmid=str(pmid) if pmid else None,
        pmcid=str(pmcid) if pmcid else None,
        doi=str(doi) if doi else None,
        title=title,
        authors=_extract_authors(rec),
        journal=journal,
        pub_date=pub_date,
        abstract=rec.get("abstractText"),
        source=src,
        url=url,
        is_open_access=is_oa,
        ingest_date=date.today(),
    )


def load_seen_ids() -> set[str]:
    seen: set[str] = set()
    if not PAPERS_PATH.exists():
        return seen
    with PAPERS_PATH.open() as f:
        for line in f:
            try:
                rec = json.loads(line)
            except json.JSONDecodeError:
                continue
            for key in ("id", "pmid", "pmcid", "doi"):
                v = rec.get(key)
                if v:
                    seen.add(str(v))
    return seen


def resolve_since(args: argparse.Namespace) -> date:
    if args.since:
        return date.fromisoformat(args.since)
    if LAST_RUN_PATH.exists():
        data = json.loads(LAST_RUN_PATH.read_text())
        return date.fromisoformat(data["last_run"][:10])
    return date.today() - timedelta(days=args.backfill_days)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--since", type=str, help="ISO date lower bound; overrides last_run.json")
    ap.add_argument("--since-last-run", action="store_true", help="Use data/last_run.json (default behavior anyway)")
    ap.add_argument("--backfill-days", type=int, default=30, help="If no last_run.json, go back this many days")
    ap.add_argument("--dry-run", action="store_true", help="Do not append to data/ or update last_run.json")
    ap.add_argument("--max", type=int, default=2000, help="Hard cap on records fetched per run")
    args = ap.parse_args()

    DATA_DIR.mkdir(exist_ok=True, parents=True)
    RUN_DIR.mkdir(exist_ok=True, parents=True)

    since_date = resolve_since(args)
    query = build_query(since_date)
    print(f"[fetch] since={since_date.isoformat()}", file=sys.stderr)

    seen = load_seen_ids()
    new_papers: list[Paper] = []
    total_seen = 0
    for rec in search(query):
        total_seen += 1
        if total_seen > args.max:
            print(f"[fetch] hit --max={args.max}, stopping", file=sys.stderr)
            break
        paper = record_to_paper(rec)
        if paper is None:
            continue
        if any(
            getattr(paper, k) and str(getattr(paper, k)) in seen
            for k in ("id", "pmid", "pmcid", "doi")
        ):
            continue
        new_papers.append(paper)
        for key in ("id", "pmid", "pmcid", "doi"):
            v = getattr(paper, key)
            if v:
                seen.add(str(v))

    print(
        f"[fetch] fetched={total_seen} new={len(new_papers)} (after dedup)",
        file=sys.stderr,
    )

    diff_path = RUN_DIR / "new_papers.jsonl"
    with diff_path.open("w") as f:
        for p in new_papers:
            f.write(p.model_dump_json(exclude_none=True))
            f.write("\n")
    print(f"[fetch] wrote {diff_path}", file=sys.stderr)

    if args.dry_run:
        print("[fetch] --dry-run: skipping data/papers.jsonl and last_run.json", file=sys.stderr)
        return

    with PAPERS_PATH.open("a") as f:
        for p in new_papers:
            f.write(p.model_dump_json(exclude_none=True))
            f.write("\n")
    LAST_RUN_PATH.write_text(
        json.dumps({"last_run": datetime.now(timezone.utc).isoformat()})
    )
    print(f"[fetch] appended to {PAPERS_PATH}, updated {LAST_RUN_PATH}", file=sys.stderr)


if __name__ == "__main__":
    main()
