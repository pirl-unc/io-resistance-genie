# Extraction schema

You receive one paper (title, abstract, and full-text XML when available). Produce a single JSON object matching the `PaperExtraction` schema from `scripts/lib/schemas.py`. No prose outside the JSON. No markdown fences.

## Schema

```json
{
  "paper_id": "<canonical id>",
  "mechanism_class": "antigen_presentation | ifn_gamma_signaling | tme_exclusion | tumor_intrinsic_signaling | t_cell_exhaustion | metabolic | microbiome | clinical_intervention | other",
  "model_system": "cell_line | mouse | patient_cohort | clinical_trial | meta_analysis | review",
  "key_finding": "<1-3 sentences stating the central mechanistic or clinical claim>",
  "intervention": "<drug, combination, genetic perturbation, or null>",
  "outcome": "<observed effect, or null>",
  "effect_size": "<quantitative if reported, else qualitative; null if none>",
  "confidence": {
    "level": "low | medium | high",
    "reasoning": "<brief: sample size, controls, replication, caveats>"
  },
  "caveats": ["<limitations worth flagging in the synthesis>"],
  "surprising_why": "<populate ONLY if genuinely unexpected given prior literature; else null>",
  "extraction_date": "<ISO date>",
  "human_study": null
}
```

### Human-study table data

When `model_system` is `patient_cohort`, `clinical_trial`, or `meta_analysis`, **also populate `human_study`** with the table-ready structured fields below. For every other `model_system`, `human_study` must be `null`.

```json
"human_study": {
  "n_patients": 305,
  "n_description": "KEYNOTE-024 phase 3, 1L advanced NSCLC, PD-L1 TPS ≥50%, EGFR/ALK-wt",
  "feature": "PD-L1 TPS ≥50% (pembrolizumab vs platinum doublet)",
  "effect_type": "PFS HR",
  "effect_value": "mPFS 10.3 vs 6.0 mo; HR 0.50",
  "effect_ci_or_p": "95% CI 0.37–0.68, p<0.001",
  "method": "PD-L1 IHC 22C3"
}
```

- `feature` is the only required field; every other value may be `null` (renders as "—" in the generated evidence table).
- `n_patients` is the best single integer for the `N` column. Use `n_description` for qualifying context (trial name, tumor type, cohort split) or when a single N misleads (e.g. multi-cohort pool — put the pool total in `n_patients`, the breakdown in `n_description`).
- `effect_type`: `HR` | `OR` | `ORR` | `PFS` | `OS` | `DFS` | `RR` | other short label describing the metric.
- `effect_value`: the point estimate as a string — "0.50", "52%", "86.3% vs 76.2%".
- `effect_ci_or_p`: CI or p-value, null if the paper doesn't report one.
- `method`: "WES" | "IHC" | "ctDNA" | "scRNA-seq" | "LOHHLA" | "phase 3 RCT" etc. — name the measurement or study design readers need to judge the evidence.

## Guidance

- **Be faithful.** If the paper doesn't show something, do not claim it does. Every claim in `key_finding` must be defensible from the abstract + full text you were given.
- **Pick the dominant `mechanism_class`.** If the paper spans classes, choose the one the authors emphasize. Use `other` only as a last resort.
- **`surprising_why` is load-bearing.** The synthesis uses this field to decide whether to highlight the paper. Only set it when the finding contradicts or substantially refines existing understanding — not merely "interesting" or "first demonstration of X in Y cancer type." If it's an incremental confirmation, leave this null.
- **Preprints** (bioRxiv/medRxiv) → `confidence.level` capped at `medium` unless the study is exceptionally rigorous.
- **Clinical trials with surprising outcomes** → `mechanism_class: clinical_intervention`, `model_system: clinical_trial`. Put the unexpected result in `surprising_why`.
- **Reviews without new primary data** should rarely reach this step, but if they do: `model_system: review`, `key_finding` = 1-sentence characterization of the reviewer's thesis, most other fields null.
- **Multi-target / combination ICI findings** → use the mechanism class that best describes the resistance biology, not the drug target. If it's a pure clinical outcome of a combination trial, use `clinical_intervention`.
