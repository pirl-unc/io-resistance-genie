# Tumor-intrinsic signaling

Tumor cell-autonomous programs that suppress or evade CD8-mediated killing constitute one of the most mechanistically rich axes of ICI resistance. Four recent findings highlight a recurring theme: **post-translational regulation of PD-L1 itself, and tumor-cell-intrinsic transcriptional programs that set immune-cold phenotypes**.

## HILPDA → KLF5 → palmitate → PD-L1 palmitoylation (Cys272)

Xu *et al.* defined a lipogenic circuit in which **HILPDA stabilizes KLF5 via HSP90**, driving fatty acid synthesis and generating palmitate that augments PD-L1 palmitoylation at cysteine 272[^pmid:41876831]. The palmitoylation stabilizes membrane PD-L1. TRIM21 catalyzes K63-linked polyubiquitination of HILPDA, and **pharmacologic TRIM21 engagement with fenretinide** — an existing clinical molecule — degrades HILPDA and restores anti-PD-1 efficacy in breast cancer mouse models.

This is a **post-translational regulatory layer for PD-L1 distinct from transcriptional control**, tractable via a compound with existing clinical familiarity.

**Caveats.** Single tumor type (breast cancer); fenretinide specificity for TRIM21 engagement not fully characterized; no clinical validation yet.

## Lactate → AARS1 → PD-L1 K280 lactylation

Zhao *et al.* identified that **lactate, via the lactyltransferase AARS1, lactylates PD-L1 at K280** in its intracellular domain[^pmid:41864972]. This PTM blocks HUWE1-mediated ubiquitination and proteasomal degradation of PD-L1, stabilizing the protein and impairing CD8 cytotoxicity. K280 lactylation correlated with advanced NSCLC stage and poor survival.

**The counterintuitive finding.** Exogenous sodium lactate *enhanced* anti-PD-L1 efficacy in preclinical models — the opposite of what the simple "lactate stabilizes PD-L1 → worse outcome" framing predicts. This paradox is explicit in the paper and is a red flag worth tracking: either the preclinical model lactate dosing maximizes PD-L1 that antibody can then target, or the mechanistic framing needs refinement. Clinical translation to lactate-modulating interventions would be premature without resolving this.

**Caveats.** NSCLC clinical cohort size not specified; paradox unresolved; no clinical trial.

## NOTCH3 → RBPJ → PVR → TIGIT (colorectal cancer)

Zheng *et al.* showed that **tumor-intrinsic NOTCH3 transcriptionally upregulates PVR** via RBPJ binding in CRC, and that PVR engages TIGIT on CD8 T cells to suppress cytotoxicity[^pmid:41808828]. NOTCH3 depletion synergized with anti-PD-L1 in mice. In a 102-patient institutional cohort plus MSKCC validation, NOTCH3 low-expression or mutation (R1669H activating) was independently associated with improved survival under ICB.

This connects a tumor-intrinsic driver directly to the PD-1/TIGIT axis and suggests NOTCH3 status could be a biomarker for anti-TIGIT combination benefit. No pharmacologic NOTCH3 inhibitor was tested *in vivo*.

## PKMYT1 → cGAS-STING (castration-resistant prostate cancer)

Li *et al.* showed **PKMYT1 overexpression suppresses antitumor immunity in CRPC**, and that its inhibition with the clinical-grade **RP-6306** activates the cGAS-STING pathway, potentiates type I/II IFN signaling, upregulates CCL5 and CXCL10, and enhances CD8 infiltration and anti-PD-L1 efficacy in syngeneic models[^pmid:41617394]. Prostate cancer has been notoriously refractory to ICI; a druggable cell-cycle kinase node that converts cold tumors to responsive is clinically provocative.

**Caveats.** Preclinical only; downstream cGAS-STING activation mechanism not fully dissected. Generalization beyond CRPC untested.

## What's not in this seed

WNT/β-catenin, PTEN loss, MYC amplification, LKB1 mutations, and KRAS-driven immune exclusion remain foundational mechanisms in the tumor-intrinsic axis. They did not surface in the top-ranked set from this three-month window but should appear in subsequent runs.

---

[^pmid:41876831]: HILPDA-KLF5-palmitoylation axis; TRIM21/fenretinide rescue. PMID [41876831](https://pubmed.ncbi.nlm.nih.gov/41876831/).
[^pmid:41864972]: AARS1-mediated PD-L1 K280 lactylation. PMID [41864972](https://pubmed.ncbi.nlm.nih.gov/41864972/).
[^pmid:41808828]: NOTCH3-PVR-TIGIT axis in CRC. PMID [41808828](https://pubmed.ncbi.nlm.nih.gov/41808828/).
[^pmid:41617394]: PKMYT1 inhibition activating cGAS-STING in CRPC. PMID [41617394](https://pubmed.ncbi.nlm.nih.gov/41617394/).
