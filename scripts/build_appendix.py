"""Regenerate docs/papers.md as a Markdown table from data/papers.jsonl."""

from __future__ import annotations

import json
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
PAPERS_JSONL = REPO_ROOT / "data" / "papers.jsonl"
OUTPUT = REPO_ROOT / "docs" / "papers.md"


def main() -> None:
    rows: list[dict] = []
    if PAPERS_JSONL.exists():
        with PAPERS_JSONL.open() as f:
            for line in f:
                try:
                    rows.append(json.loads(line))
                except json.JSONDecodeError:
                    continue

    rows.sort(key=lambda r: r.get("pub_date") or "", reverse=True)

    lines = [
        "# Papers",
        "",
        f"Every paper seen by the pipeline. **{len(rows)}** total.",
        "",
    ]

    if not rows:
        lines.append("No papers yet — the first scheduled run has not completed.")
    else:
        lines.extend(
            [
                "| Date | Title | Journal | Source | Links |",
                "| --- | --- | --- | --- | --- |",
            ]
        )
        for r in rows:
            date_s = r.get("pub_date") or ""
            title = (r.get("title") or "").replace("|", "\\|").strip()
            journal = (r.get("journal") or "").replace("|", "\\|")
            src = r.get("source") or ""
            links = []
            if r.get("pmid"):
                links.append(f"[PMID](https://pubmed.ncbi.nlm.nih.gov/{r['pmid']}/)")
            if r.get("doi"):
                links.append(f"[DOI](https://doi.org/{r['doi']})")
            if r.get("pmcid"):
                links.append(f"[PMC](https://europepmc.org/article/PMC/{r['pmcid']})")
            lines.append(
                f"| {date_s} | {title} | {journal} | {src} | {' '.join(links)} |"
            )

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text("\n".join(lines) + "\n")
    print(f"[build_appendix] wrote {OUTPUT} with {len(rows)} papers")


if __name__ == "__main__":
    main()
