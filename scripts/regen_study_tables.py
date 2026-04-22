"""Regenerate per-subsection human-study evidence tables.

For each target markdown file (home page + every mechanism page), walks the
four tier subsections (`## What has held up`, `## Where the field has
contradicted itself`, `## Suspected but unconfirmed`, `## New directions
worth watching` on the home page; `## Confidently known` / `## Contradictions
/ surprises` / `## Suspected but unconfirmed` / `## Emerging` on mechanism
pages). For each subsection:

  1. Collects every `[^pmid:...]` citation from the *bullet* lines of the
     subsection (footnote-definition lines at the bottom of the file are
     excluded).
  2. Filters to human studies (`model_system ∈ {patient_cohort,
     clinical_trial, meta_analysis}`) using `data/extractions.jsonl`.
  3. Looks up the structured `human_study` block on each.
  4. Writes a markdown table inside a
     `<!-- STUDY-TABLE:START ... --> ... <!-- STUDY-TABLE:END -->` block.
     The block is appended at the END of the subsection (before the next
     `##` heading, `---`, or EOF) if absent, or rewritten in place.

Idempotent: running twice produces zero additional diff. Use `--check` in CI.

Usage:
    python3 scripts/regen_study_tables.py
    python3 scripts/regen_study_tables.py --check
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

import sys as _sys
_sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from scripts.lib.schemas import HumanStudyData, ModelSystem  # noqa: E402


HUMAN_MODELS = {
    ModelSystem.PATIENT_COHORT.value,
    ModelSystem.CLINICAL_TRIAL.value,
    ModelSystem.META_ANALYSIS.value,
}

TARGET_FILES = [
    "docs/index.md",
    "docs/mechanisms/antigen-presentation.md",
    "docs/mechanisms/clinical-interventions.md",
    "docs/mechanisms/ifn-gamma.md",
    "docs/mechanisms/metabolic.md",
    "docs/mechanisms/microbiome.md",
    "docs/mechanisms/t-cell-exhaustion.md",
    "docs/mechanisms/tme-exclusion.md",
    "docs/mechanisms/tumor-intrinsic.md",
]

TIER_HEADINGS = {
    # heading text -> short tier key used in START marker
    "What has held up": "established",
    "Where the field has contradicted itself": "contested",
    "Suspected but unconfirmed": "suspected",
    "New directions worth watching": "emerging",
    "Confidently known": "established",
    "Contradictions / surprises": "contested",
    "Emerging": "emerging",
}

TIER_HEADING_RE = re.compile(
    r"^##\s+(What has held up|Where the field has contradicted itself"
    r"|Suspected but unconfirmed|New directions worth watching"
    r"|Confidently known|Contradictions / surprises|Emerging)"
    r"(?:\s*\(.*\))?\s*$"
)
NON_TIER_H2_RE = re.compile(r"^##\s+")
SEPARATOR_RE = re.compile(r"^---\s*$")
BULLET_START_RE = re.compile(r"^- ")
PMID_RE = re.compile(r"\[\^pmid:(\d+)\]")

MARKER_START_RE = re.compile(r"^<!-- STUDY-TABLE:START[^>]*-->\s*$")
MARKER_END_RE = re.compile(r"^<!-- STUDY-TABLE:END\s*-->\s*$")


@dataclass
class Section:
    page: str              # "index" or the slug of a mechanism page
    tier_key: str          # "established" / "contested" / "suspected" / "emerging"
    heading_idx: int       # line index of the `## ...` heading
    body_start: int        # first line after the heading
    body_end: int          # exclusive; first line that is a new `##` heading, `---`, or EOF
    pmids: list[str]       # PMIDs cited in bullet lines


def page_slug(path: str) -> str:
    if path == "docs/index.md":
        return "index"
    return Path(path).stem  # e.g. "tme-exclusion"


def load_extractions() -> dict[str, tuple[str, Optional[HumanStudyData]]]:
    d: dict[str, tuple[str, Optional[HumanStudyData]]] = {}
    with open("data/extractions.jsonl") as f:
        for line in f:
            r = json.loads(line)
            hs = r.get("human_study")
            d[r["paper_id"]] = (
                r["model_system"],
                HumanStudyData.model_validate(hs) if hs else None,
            )
    return d


def load_citations() -> dict[str, str]:
    """paper_id -> short markdown citation linked to PubMed."""
    cites: dict[str, str] = {}
    with open("data/papers.jsonl") as f:
        for line in f:
            r = json.loads(line)
            pid = r.get("pmid") or r.get("id")
            if not pid:
                continue
            authors = r.get("authors") or []
            first = authors[0] if authors else ""
            lastname = first.split(" ")[0] if first else "(unknown)"
            year = (r.get("pub_date") or "")[:4] or "????"
            cites[pid] = f"[{lastname} {year}](https://pubmed.ncbi.nlm.nih.gov/{pid}/)"
    return cites


def find_sections(text: str, page: str) -> list[Section]:
    lines = text.splitlines()
    n = len(lines)
    out: list[Section] = []
    # Determine the "prose" region: before the first footnote-definition line.
    # Footnote defs look like `[^pmid:12345]: ...` at column 0.
    footnote_def_re = re.compile(r"^\[\^(?:pmid|doi):")
    prose_end = n
    for i, line in enumerate(lines):
        if footnote_def_re.match(line):
            prose_end = i
            break

    i = 0
    while i < n:
        line = lines[i]
        m = TIER_HEADING_RE.match(line)
        if not m:
            i += 1
            continue
        heading = m.group(1)
        tier_key = TIER_HEADINGS[heading]
        body_start = i + 1
        body_end = n
        j = body_start
        while j < n:
            cand = lines[j]
            if NON_TIER_H2_RE.match(cand) or SEPARATOR_RE.match(cand):
                body_end = j
                break
            if j >= prose_end:
                body_end = j
                break
            j += 1
        # Collect PMIDs from bullet lines only.
        pmids: list[str] = []
        seen: set[str] = set()
        in_generated_block = False
        for k in range(body_start, body_end):
            raw = lines[k]
            if MARKER_START_RE.match(raw):
                in_generated_block = True
                continue
            if MARKER_END_RE.match(raw):
                in_generated_block = False
                continue
            if in_generated_block:
                continue
            if not BULLET_START_RE.match(raw):
                continue
            for pid in PMID_RE.findall(raw):
                if pid not in seen:
                    seen.add(pid)
                    pmids.append(pid)
        out.append(
            Section(
                page=page,
                tier_key=tier_key,
                heading_idx=i,
                body_start=body_start,
                body_end=body_end,
                pmids=pmids,
            )
        )
        i = body_end
    return out


def render_table(
    section: Section,
    extractions: dict[str, tuple[str, Optional[HumanStudyData]]],
    citations: dict[str, str],
    warnings: list[str],
) -> list[str]:
    """Return the list of lines (no trailing newline) that go between the
    START and END markers."""
    out: list[str] = []
    out.append(f"### Human-study evidence")
    out.append("")
    rows: list[str] = []
    for pid in section.pmids:
        entry = extractions.get(pid)
        if entry is None:
            warnings.append(
                f"{section.page}/{section.tier_key}: PMID {pid} not in extractions.jsonl"
            )
            continue
        ms, hs = entry
        if ms not in HUMAN_MODELS:
            continue
        if hs is None:
            warnings.append(
                f"{section.page}/{section.tier_key}: PMID {pid} is human-study but lacks human_study data"
            )
            continue
        rows.append(render_row(pid, hs, citations))
    if not rows:
        out.append("*No human-study citations in this section.*")
        return out
    out.append("| Study | N | Feature | Effect | 95% CI / p | Method |")
    out.append("|---|---:|---|---|---|---|")
    out.extend(rows)
    return out


def render_row(pid: str, hs: HumanStudyData, citations: dict[str, str]) -> str:
    cite = citations.get(pid, f"[PMID {pid}](https://pubmed.ncbi.nlm.nih.gov/{pid}/)")
    # N column: prefer "n=NNN" from n_patients; append n_description if present.
    n_cell = "—"
    if hs.n_patients is not None:
        n_cell = f"n={hs.n_patients}"
        if hs.n_description:
            n_cell += f" ({hs.n_description})"
    elif hs.n_description:
        n_cell = hs.n_description
    # Effect column: join type + value with a space.
    effect_parts = [hs.effect_type, hs.effect_value]
    effect = " ".join(p for p in effect_parts if p)
    effect_cell = effect or "—"
    ci_cell = hs.effect_ci_or_p or "—"
    method_cell = hs.method or "—"
    feature_cell = hs.feature or "—"
    # Pipe-escape each cell.
    cells = [cite, n_cell, feature_cell, effect_cell, ci_cell, method_cell]
    cells = [c.replace("|", "\\|") for c in cells]
    return "| " + " | ".join(cells) + " |"


def splice_block(
    lines: list[str],
    section: Section,
    block_lines: list[str],
) -> list[str]:
    """Return a new `lines` list with the generated block inserted (or updated
    in place) within the subsection body."""
    # Find existing markers within the section body.
    start_idx: Optional[int] = None
    end_idx: Optional[int] = None
    for k in range(section.body_start, section.body_end):
        if start_idx is None and MARKER_START_RE.match(lines[k]):
            start_idx = k
        elif start_idx is not None and MARKER_END_RE.match(lines[k]):
            end_idx = k
            break
    start_marker = f"<!-- STUDY-TABLE:START page={section.page} tier={section.tier_key} -->"
    end_marker = "<!-- STUDY-TABLE:END -->"
    new_block = [start_marker] + block_lines + [end_marker]
    if start_idx is not None and end_idx is not None:
        return lines[:start_idx] + new_block + lines[end_idx + 1:]
    # Insert fresh. Anchor: end of section body, trimmed of trailing blank lines
    # so the block hugs the last bullet.
    insert_at = section.body_end
    while insert_at > section.body_start and lines[insert_at - 1].strip() == "":
        insert_at -= 1
    prefix = [""] if insert_at > section.body_start else []  # leading blank line
    suffix = [""]
    return lines[:insert_at] + prefix + new_block + suffix + lines[insert_at:]


def process_file(
    path: str,
    extractions: dict[str, tuple[str, Optional[HumanStudyData]]],
    citations: dict[str, str],
    warnings: list[str],
) -> tuple[str, str]:
    old_text = Path(path).read_text()
    page = page_slug(path)
    lines = old_text.splitlines()
    # Each run recomputes sections after every splice to keep indices honest.
    # Section order is deterministic because we always process top-to-bottom
    # and insertions only shift lines below the current section.
    processed = 0
    while True:
        sections = find_sections("\n".join(lines), page)
        # Find the first section whose current block content differs from target.
        updated_any = False
        for section in sections:
            block_lines = render_table(section, extractions, citations, warnings)
            new_lines = splice_block(lines, section, block_lines)
            if new_lines != lines:
                lines = new_lines
                updated_any = True
                processed += 1
                break
        if not updated_any:
            break
    new_text = "\n".join(lines)
    if old_text.endswith("\n") and not new_text.endswith("\n"):
        new_text += "\n"
    return old_text, new_text


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="exit 1 if any file would change")
    args = ap.parse_args()

    extractions = load_extractions()
    citations = load_citations()
    warnings: list[str] = []
    any_change = False
    totals = {"files": 0, "sections": 0, "rows": 0}

    for path in TARGET_FILES:
        old_text, new_text = process_file(path, extractions, citations, warnings)
        changed = new_text != old_text
        if changed:
            any_change = True
        totals["files"] += 1 if changed else 0
        # Count STUDY-TABLE blocks in new file for reporting
        block_count = len(MARKER_START_RE.findall(new_text)) if False else sum(
            1 for l in new_text.splitlines() if MARKER_START_RE.match(l)
        )
        row_count = sum(
            1 for l in new_text.splitlines()
            if l.startswith("| [") and "pubmed.ncbi.nlm.nih.gov" in l
        )
        totals["sections"] += block_count
        totals["rows"] += row_count
        status = "UPDATE" if changed else "ok    "
        print(f"[regen] {status} {path:<50} blocks={block_count} rows={row_count}")
        if args.check:
            continue
        if changed:
            Path(path).write_text(new_text)

    if warnings:
        print("\n[regen] warnings:", file=sys.stderr)
        for w in warnings:
            print(f"  {w}", file=sys.stderr)

    print(f"\n[regen] totals: "
          f"{totals['files']} files changed, "
          f"{totals['sections']} STUDY-TABLE blocks, "
          f"{totals['rows']} table rows")

    if args.check and any_change:
        print("[regen] --check: files would change; re-run without --check", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
