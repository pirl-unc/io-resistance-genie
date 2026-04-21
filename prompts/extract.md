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
  "extraction_date": "<ISO date>"
}
```

## Guidance

- **Be faithful.** If the paper doesn't show something, do not claim it does. Every claim in `key_finding` must be defensible from the abstract + full text you were given.
- **Pick the dominant `mechanism_class`.** If the paper spans classes, choose the one the authors emphasize. Use `other` only as a last resort.
- **`surprising_why` is load-bearing.** The synthesis uses this field to decide whether to highlight the paper. Only set it when the finding contradicts or substantially refines existing understanding — not merely "interesting" or "first demonstration of X in Y cancer type." If it's an incremental confirmation, leave this null.
- **Preprints** (bioRxiv/medRxiv) → `confidence.level` capped at `medium` unless the study is exceptionally rigorous.
- **Clinical trials with surprising outcomes** → `mechanism_class: clinical_intervention`, `model_system: clinical_trial`. Put the unexpected result in `surprising_why`.
- **Reviews without new primary data** should rarely reach this step, but if they do: `model_system: review`, `key_finding` = 1-sentence characterization of the reviewer's thesis, most other fields null.
- **Multi-target / combination ICI findings** → use the mechanism class that best describes the resistance biology, not the drug target. If it's a pure clinical outcome of a combination trial, use `clinical_intervention`.
