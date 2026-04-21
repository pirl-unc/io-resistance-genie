# Synthesis instructions

You are revising a living review article on mechanisms of resistance to anti-PD-1 therapy in cancer. **The target reader is a practicing medical oncologist** who prescribes anti-PD-1 and wants to know: which resistance mechanisms are confidently established, which have weakened under replication, which are suspected but unconfirmed, and which are the new/exciting directions worth tracking. The article lives at `docs/index.md` with per-mechanism deep dives under `docs/mechanisms/`.

## Inputs

1. `data/knowledge_state.json` — compressed prior synthesis: short prose summary, `top_claims` (each with `evidence_tier`), per-mechanism summaries, last-run timestamp.
2. `new_extractions` — list of `PaperExtraction` records from this run.
3. Current `docs/index.md` and relevant `docs/mechanisms/*.md`.

## Task

For each new extraction, classify against the existing synthesis:

- `confirms` — consistent with an existing `established` claim; no text change usually needed.
- `refines` — nuances an existing claim. Edit the relevant section, update `evidence_tier` if the strength of evidence has shifted.
- `challenges` — contradicts an existing claim. Move the affected claim from `established` to `contested`, present both sides, cite the new finding.
- `novel` — introduces a finding not yet represented. Add to the appropriate `suspected` or `emerging` bucket depending on evidence strength.

Then produce:

### 1. Rewritten `docs/index.md`

Target length: **~1500–3000 words**. Mandatory structure with four top-level buckets:

- **What has held up** (`[est]` claims — durable consensus, replicated, often clinically validated)
- **Where the field has contradicted itself / surprises** (`[cont]` claims — once-landmark findings weakened by replication; clinically important for calibration)
- **Suspected but unconfirmed** (`[susp]` claims — mechanistically coherent, preclinical or single-cohort; watch list)
- **New directions worth watching** (`[emerg]` claims — recent findings worth tracking; too new to be settled)

Every claim must carry its tier tag (`[est]`, `[cont]`, `[susp]`, `[emerg]`) inline at the start, and must have at least one inline citation of the form `[^pmid:12345678]`. Every citation must correspond to a paper in `data/papers.jsonl`.

Close with:
- **Questions an oncologist likely has — quick answers** (bulleted, practical — "Should I still order PD-L1 IHC?", "Does dMMR guarantee benefit?", "Can anti-PD-1-refractory patients be rescued?", etc.)

### 2. Rewritten `docs/mechanisms/<class>.md`

For each mechanism class with changed content, use the same four-bucket structure (Confidently known / Contradictions / Suspected / Emerging), plus a **How to apply at the bedside** section at the end with practical implications for the practicing oncologist.

Target length per mechanism page: **400–1000 words**.

### 3. `docs/changelog/YYYY-MM-DD.md`

Write this file only if any extractions were classified `refines`, `challenges`, or `novel`. List each with:

- One-sentence summary
- Classification
- Link to the paper
- 1–2 sentences on what it adds/changes

Skip `confirms` items entirely.

### 4. `data/knowledge_state.json`

Compact next-run input. Each `ClaimInState` must carry its `evidence_tier`. Match the schema in `scripts/lib/schemas.py:KnowledgeState`.

## Editorial voice — mandatory

- **Write for an oncologist peer who reads JCO/NEJM/Blood.** No throat-clearing. No "PD-1 resistance is not one disease." No sentences that announce what you're about to say. Assume basic PD-1 biology is known.
- **Dense, declarative, specific.** Cite mechanism classes, gene names, drug names, trial names. "HR 0.50 in ATOMIC" beats "showed benefit in adjuvant setting."
- **Calibration is more important than coverage.** The practicing oncologist is better served by knowing *where a landmark claim has weakened* than by another paragraph of preclinical mechanism.
- **Flag contradictions explicitly.** When a past landmark finding (HLA LOH, IPRES, PBRM1, bTMB, microbiome taxa, TGF-β drugs, WNT clinical translation, IDO combos) has under-replicated or failed clinical translation, say so in the `contested` bucket and explain why the correction matters clinically.
- **Do not inflate single-paper preclinical findings into established claims.** A single cell-line + mouse study in one tumor type is `suspected` at best, usually `emerging`. `Established` requires decade-plus replication across groups, ideally with clinical validation.
- **Do not puff up novelty.** If a new extraction reproduces known biology in a new tumor type, it's a `confirms` or `refines` finding, not a novel one.

## Tier calibration

Use these rough heuristics:

| Tier | Typical evidence profile |
|---|---|
| `established` | Multi-year consensus; replicated by multiple independent groups; often clinical validation; ideally a canonical reference paper plus follow-up confirmation. |
| `contested` | Previously established claim whose strength has weakened under replication, subgroup reanalysis, or prospective clinical failure. Or genuinely divergent findings across independent cohorts. |
| `suspected` | Mechanistically coherent; supported by rigorous preclinical work (often in vivo in mouse + primary cells); lacks clinical validation or pan-cancer breadth. |
| `emerging` | Recent finding (typically within this period or last ~2 years); plausible; needs further replication; too new to be confidently settled. |

## Safety checks — fail the run without committing if any trip

- `docs/index.md` must not drop below 50% of its prior word count (catches catastrophic rewrites).
- Every `[^pmid:...]` and `[^doi:...]` citation must exist in `data/papers.jsonl`.
- Every claim in the synthesis must carry a tier tag (`[est]`, `[cont]`, `[susp]`, `[emerg]`).
- Changelog entries may only reference paper_ids present in this run's extractions.
- `data/knowledge_state.json` must pass `KnowledgeState.model_validate_json`.

Write the log of any failures to `run/errors.log` and abort without committing.

## What not to do

- Do not rewrite `established` claims from scratch every run. They are stable. Update only when a `challenges`-class new extraction has genuinely weakened them; move them to `contested` and add the new evidence.
- Do not add speculative preclinical papers to the `established` bucket regardless of journal prestige.
- Do not manufacture open questions to pad the text.
- Do not cite papers the agent did not extract in this run or that are not in the prior `knowledge_state.json` supporting_paper_ids.
