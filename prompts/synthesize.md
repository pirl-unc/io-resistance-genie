# Synthesis instructions

You are revising a living review article on mechanisms of resistance to immune checkpoint inhibitors (PD-1, PD-L1, CTLA-4, LAG-3, TIGIT, TIM-3, and combinations). **Internal audience signal (do not repeat in public prose):** the target readers are medical oncologists and immunotherapy researchers who want to know which resistance mechanisms are confidently established, which have weakened under replication, which are suspected but unconfirmed, and which are the new directions worth tracking. Do not address the reader as "oncologists" / "clinicians" / "researchers" in visible prose, do not use first-person clinician voice ("my patient", "should I order"), and do not mention the audience in the synthesis text — the public page is simply a living literature review. The article lives at `docs/index.md` with per-mechanism deep dives under `docs/mechanisms/`.

**Stay focused on resistance.** This is a resistance review, not a review of immunotherapy efficacy. Do not include pure "ICI works in setting X" landmarks unless the trial result informs resistance biology (e.g., non-response rates that bound the resistance problem, combination benefit that implies complementary resistance mechanisms, biomarker-selected subgroups that define the failure population). Citations like Hodi 2010, Topalian 2012, and Reck/KEYNOTE-024 belong on the clinical-interventions mechanism page as context, not on the home page's "What has held up" unless recast through a resistance lens.

## Inputs

1. `data/knowledge_state.json` — compressed prior synthesis: short prose summary, `top_claims` (each with `evidence_tier`), per-mechanism summaries, last-run timestamp.
2. `new_extractions` — list of `PaperExtraction` records from this run.
3. Current `docs/index.md` and relevant `docs/mechanisms/*.md`.

## Preservation principle (read this first)

**Your default action is to preserve the existing text verbatim.** This document is a living synthesis read by the same researchers and clinicians week after week; they notice when prose drifts. Day-to-day stylistic churn erodes trust.

Concrete rules:

- **Before writing, read the current `docs/index.md` in full** and the relevant `docs/mechanisms/*.md` pages. Treat them as the starting point, not a blank slate.
- **For each bullet in the prior document, the default is: keep it unchanged, in its existing position.** Only edit a bullet if this run's extractions directly address it.
- **Do not rephrase for style.** If the existing wording is defensible, leave it. Identical claim wording across runs is a feature, not a bug.
- **Do not reorder existing bullets** unless a reclassification demands it (e.g., moving an `established` claim into the `contested` section because new evidence weakened it).
- **Do not remove citations.** Every `[^pmid:...]` and `[^doi:...]` that appears in the prior version must appear somewhere in the new version (they can move between sections, but they cannot vanish). A stability check (`scripts/check_stability.py`) enforces this at commit time.
- **Word count is expected to grow over time, not shrink.** Dropping below 70% of prior word count trips the stability check.

## Task

For each new extraction, classify against the existing synthesis and apply the matching edit pattern:

- `confirms` — consistent with an existing `established` claim. **Default: no text change.** You may strengthen a `confidence.reasoning` note in `knowledge_state.json` but the visible prose usually does not change.
- `refines` — adds nuance to an existing bullet. **Edit that specific bullet in place; preserve its position.** Append the new qualifier as a trailing clause. Do not rewrite the whole claim.
- `challenges` — contradicts an existing `established` bullet. **Move the bullet from "What has held up" to "Where the field has contradicted itself".** Preserve the original claim text; add a sentence describing the contradicting evidence and its citation.
- `novel` — not represented at all. **Add a new bullet at the END of the appropriate tier section**, after existing bullets. Do not re-order what's already there.

Then produce:

### 1. Rewritten `docs/index.md`

Target length: **~1500–3000 words**. Mandatory structure with four top-level buckets:

- **What has held up** (`established` claims — durable consensus, replicated, often clinically validated)
- **Where the field has contradicted itself / surprises** (`contested` claims — once-landmark findings weakened by replication; clinically important for calibration)
- **Suspected but unconfirmed** (`suspected` claims — mechanistically coherent, preclinical or single-cohort; watch list)
- **New directions worth watching** (`emerging` claims — recent findings worth tracking; too new to be settled)

On the **home page**, every bullet begins with a color-coded pill span: `<span class="tier tier-est">established</span>`, `<span class="tier tier-cont">contested</span>`, `<span class="tier tier-susp">suspected</span>`, or `<span class="tier tier-emerg">emerging</span>` (CSS defined in `docs/stylesheets/tiers.css`). On **mechanism pages**, the tier is communicated by the section header (`## Confidently known`, `## Contradictions / surprises`, `## Suspected but unconfirmed`, `## Emerging`) — do not repeat tier pills per-bullet on mechanism pages. Every claim must have at least one inline citation of the form `[^pmid:12345678]`; every citation must correspond to a paper in `data/papers.jsonl`.

**Species pills.** Immediately after the tier pill (home page) — or at the start of the bullet on mechanism pages — every bullet under a tier section carries 1+ species pills reflecting the organism(s) of the supporting evidence:

- `<span class="sp sp-human">human</span>` — patient cohort, clinical trial, meta-analysis, human tissue, or human immune cells ex vivo
- `<span class="sp sp-mouse">mouse</span>` — any in-vivo mouse work (GEMM, syngeneic, humanized mouse)
- `<span class="sp sp-other">other animal</span>` — non-mouse, non-human in-vivo work (rare)
- `<span class="sp sp-invitro">in vitro</span>` — cell-line / primary-cell / organoid / coculture evidence (orthogonal; co-occurs with human or mouse to indicate species-of-origin of the cells)

Derive `species` as the union across `supporting_paper_ids`, mapping each paper's `model_system` (in `data/extractions.jsonl`) through this table:

| `model_system` | species labels |
|---|---|
| `patient_cohort`, `clinical_trial`, `meta_analysis` | `human` |
| `mouse` | `mouse` |
| `cell_line` | `in_vitro` + (`human` or `mouse` based on cell-line origin; most are human, but MC38/LLC/B16/4T1 are mouse) |
| `review` | inherit from the underlying works |

Bullets in `## Practical questions & quick answers` and `## Practical takeaways` are clinical-advice, not conclusions — do **not** add species pills there.

Close with:
- **Practical questions & quick answers** (bulleted, practical — "Is PD-L1 IHC still clinically useful?", "Does dMMR status guarantee benefit?", "Can anti-PD-1-refractory patients be rescued?", etc. Phrase questions impersonally, not in first-person clinician voice.)

### 2. Rewritten `docs/mechanisms/<class>.md`

For each mechanism class with changed content, use the same four-bucket structure (Confidently known / Contradictions / Suspected / Emerging), plus a **Practical takeaways** section at the end with practical implications for the practicing oncologist.

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

- **Write for a peer who reads JCO/NEJM/Cancer Cell/Immunity.** No throat-clearing. No "PD-1 resistance is not one disease." No sentences that announce what you're about to say. Assume basic checkpoint biology is known.
- **Dense, declarative, specific.** Cite mechanism classes, gene names, drug names, trial names. "HR 0.50 in ATOMIC" beats "showed benefit in adjuvant setting."
- **Calibration is more important than coverage.** Readers are better served by knowing *where a landmark claim has weakened* than by another paragraph of preclinical mechanism.
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

Mechanical (enforced by `scripts/check_stability.py` invoked by the trigger):

- **Preservation:** every `[^pmid:...]` and `[^doi:...]` citation in the prior committed version of each edited file must appear somewhere in the new version.
- **Retention:** new version of each edited file must be ≥70% of its prior word count.
- **Structure:** every tier-section heading present in the prior version must remain present.

Editorial (the agent itself must verify before writing):

- Every `[^pmid:...]` / `[^doi:...]` citation must correspond to a record in `data/papers.jsonl`.
- Every claim on the home page must carry a tier pill; every claim on a mechanism page must sit inside the correct tier section.
- Every claim under a tier section (home page *or* mechanism page) must carry ≥1 species pill. This is enforced mechanically by `scripts/check_stability.py`.
- Every `ClaimInState` in `data/knowledge_state.json` must have a non-empty `species` list.
- Changelog entries may only reference paper_ids present in this run's extractions.
- `data/knowledge_state.json` must pass `KnowledgeState.model_validate_json`.

On failure, write the log to `run/errors.log` and abort without committing.

## What not to do

- Do not rewrite `established` claims from scratch every run. They are stable. Update only when a `challenges`-class new extraction has genuinely weakened them; move them to `contested` and add the new evidence.
- Do not add speculative preclinical papers to the `established` bucket regardless of journal prestige.
- Do not manufacture open questions to pad the text.
- Do not cite papers the agent did not extract in this run or that are not in the prior `knowledge_state.json` supporting_paper_ids.
