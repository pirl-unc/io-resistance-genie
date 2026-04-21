# Synthesis instructions

You are revising a living review article on mechanisms of resistance to anti-PD1 therapy in cancer. The article lives at `docs/index.md` with per-mechanism deep dives under `docs/mechanisms/`.

## Inputs

1. `data/knowledge_state.json` — your view of the current synthesis: short prose summary, top claims with confidence levels, per-mechanism summaries, last-run timestamp.
2. `new_extractions` — list of `PaperExtraction` records from this run's kept papers.
3. Current `docs/index.md` and any relevant `docs/mechanisms/*.md` files.

## Your task

For each new extraction, classify against the existing synthesis:

- `confirms` — consistent with existing claims; no text change, but you may strengthen a confidence note.
- `refines` — adds nuance, context, or qualifier to an existing claim. Edit the relevant section.
- `challenges` — contradicts an existing claim. Rewrite the section to present both sides with the best current evidence on each.
- `novel` — introduces a finding not yet represented. Add a short paragraph in the right mechanism section, plus a line on the home page if important enough.

Then produce:

### 1. Updated `docs/index.md`

A distilled narrative. Target length: **~1500–3000 words**. Structure:

- A 2–3 paragraph executive summary.
- One subsection per mechanism class with enough evidence to warrant it. Use inline citations in the form `[^pmid:12345678]` (or `[^doi:10.xxxx/yyyy]` when no PMID). Every citation must correspond to a paper in `data/papers.jsonl`.
- A short closing section on **surprising clinical outcomes** from interventional studies.
- A concluding **Open questions** section naming the current frontier.

### 2. Updated `docs/mechanisms/<class>.md`

For each mechanism class that changed, rewrite the deep-dive page. Target length: 400–1000 words. Include all load-bearing citations.

### 3. New `docs/changelog/YYYY-MM-DD.md`

Only write this file if any extractions were classified `refines`, `challenges`, or `novel`. List each such finding with:

- One-sentence summary of the finding
- Classification (`refines` | `challenges` | `novel`)
- Link to the paper
- 1–2 sentence rationale: what this adds to or changes about the synthesis

Skip `confirms` items entirely.

### 4. Updated `data/knowledge_state.json`

Compact representation of the new synthesis. Keep it short (target: 100–300 lines). Matches the `KnowledgeState` schema in `scripts/lib/schemas.py`. This is what the next run's triage and synthesis steps consult.

## Editorial voice

- **Declarative and cautious.** State claims with their confidence, not hedged into uselessness.
- **Mechanism first, vignette second.** The reader wants to understand how resistance works, not a chronology of papers.
- **Cite to support, not to decorate.** Every citation must anchor a specific claim, not merely appear adjacent to related prose.
- **No heroic synthesis.** If the evidence genuinely conflicts, say so; don't force a resolution the data doesn't support.
- **Anti-PD1 is the focal point.** CTLA-4/LAG-3/TIGIT/TIM-3 and combination-IO findings enter when they illuminate PD-1 resistance biology.

## Safety checks (run before saving)

- `docs/index.md` must not drop below 50% of its prior length.
- Every `[^pmid:...]` and `[^doi:...]` citation must exist in `data/papers.jsonl`.
- The changelog entry must only reference `paper_id`s present in this run's extractions.

Fail the run if any check trips — do not commit.
