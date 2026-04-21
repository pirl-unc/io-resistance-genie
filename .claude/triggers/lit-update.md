# Literature update run

You are the scheduled editor for `io-resistance-genie`, a living synthesis on resistance to anti-PD1 therapy. Execute the following steps in order. **Commit and push only at the end, after all safety checks pass.**

## Setup

Working directory: the repo root. All paths below are relative.

Ensure Python dependencies are installed:

```bash
uv sync 2>/dev/null || pip install httpx pydantic
```

## 1. Fetch new papers

```bash
python scripts/fetch.py --since-last-run
```

This appends new records to `data/papers.jsonl` and writes the diff for this run to `run/new_papers.jsonl`. It also updates `data/last_run.json`.

If `run/new_papers.jsonl` is empty, stop here: no synthesis changes, no commit.

## 2. Triage

For each paper in `run/new_papers.jsonl`:

- Read `prompts/triage.md` as the rubric.
- Use the paper's title + abstract as context.
- Ground `novelty_guess` against the summary in `data/knowledge_state.json` (if it exists — on the first run it won't).
- Produce a `TriageDecision` JSON object per paper.
- Validate each record with pydantic:
  ```bash
  python -c "import json, sys; from scripts.lib.schemas import TriageDecision; [TriageDecision.model_validate_json(l) for l in open('run/triage.jsonl')]"
  ```

Write all decisions to `run/triage.jsonl`. Select the kept papers (`keep=true`). Cap at the top 20 by `(relevance + novelty_guess)` to control per-run work.

## 3. Extract

For each kept paper:

- If `is_open_access=true`, fetch full-text XML using `scripts.lib.europepmc.fetch_fulltext_xml(source, paper_id)`. The `source` argument is `"MED"` for PubMed papers and `"PPR"` for preprints (Europe PMC REST convention, not the schema's `Source`). Otherwise use the abstract.
- Apply `prompts/extract.md` to produce a `PaperExtraction` JSON object.
- Validate with pydantic (`PaperExtraction.model_validate_json(...)`).
- Append to `data/extractions.jsonl`.

## 4. Synthesize

Load:

- `data/knowledge_state.json` (prior synthesis state; absent on first run — treat as empty)
- This run's extractions
- Current `docs/index.md` and any relevant `docs/mechanisms/*.md`

Apply `prompts/synthesize.md`. **Read the existing `docs/index.md` and relevant `docs/mechanisms/*.md` in full first — the preservation principle there is load-bearing: default action is to keep existing bullets verbatim.** Produce:

- Updated `docs/index.md` (preserve existing bullets; edit surgically)
- Updated `docs/mechanisms/<class>.md` for any changed mechanism class (same preservation rule)
- `docs/changelog/YYYY-MM-DD.md` (only if `refines`/`challenges`/`novel` items exist)
- Updated `data/knowledge_state.json` (validate with `KnowledgeState.model_validate_json(...)`)

After writing, **run the stability check on every modified doc**:

```bash
CHANGED=$(git diff --name-only -- 'docs/*.md' 'docs/**/*.md')
for f in $CHANGED; do
  python scripts/check_stability.py --old-ref HEAD --new "$f" || {
    echo "[abort] stability check failed on $f — see run/errors.log" >> run/errors.log
    exit 1
  }
done
```

If any check fails, **abort without committing**; append the failure details to `run/errors.log`.

## 5. Rebuild the paper appendix

```bash
python scripts/build_appendix.py
```

## 6. Commit and push

Compose the commit message using the counts from this run's classifications:

```
chore: literature update YYYY-MM-DD — N novel, M refined, K challenged
```

If this run produced no new papers, or all classifications were `confirms`, exit silently without committing.

Otherwise:

```bash
git add data/ docs/ run/errors.log 2>/dev/null
git -c user.name='io-resistance-genie-bot' -c user.email='bot@users.noreply.github.com' \
    commit -m "<message>"
git push origin main
```

The `pages.yml` workflow will rebuild and redeploy the site automatically.

## Invariants (never violate)

- Never commit if any safety check fails.
- Never commit if `scripts/check_stability.py` returns non-zero on any modified doc.
- The synthesis rewrite must preserve prior citations, tier headings, and ≥70% of prior word count per file. When in doubt, preserve the existing text verbatim.
- Never invent PMIDs or DOIs. Every citation must trace to a record in `data/papers.jsonl`.
- Never bypass pydantic validation. On validation error, write to `run/errors.log`, skip that record, continue.
- Never delete entries from `data/papers.jsonl` or `data/extractions.jsonl` — these are append-only.
