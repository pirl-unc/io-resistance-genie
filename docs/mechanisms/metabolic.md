# Metabolic resistance

## Confidently known

- <span class="sp sp-human">human</span> <span class="sp sp-mouse">mouse</span> **Immune-suppressive metabolism in the TME is real and multi-layered.** The established frameworks cover adenosine (CD39/CD73), tryptophan/kynurenine (IDO/TDO), lactate/Warburg, arginine depletion (arginase I), and lipid mediators (PGE2 from COX1/2). Each has preclinical support and some level of clinical translation. However, pharmacologic targeting has been a persistent disappointment: **IDO inhibitors (epacadostat)** failed in combination with pembrolizumab (ECHO-301) despite compelling biology, and adenosine-axis combinations have produced modest-at-best clinical effects so far.

<!-- STUDY-TABLE:START page=metabolic tier=established -->
### Human-study evidence

*No human-study citations in this section.*
<!-- STUDY-TABLE:END -->


## Contradictions / surprises

- <span class="sp sp-human">human</span> **IDO clinical translation failed despite strong preclinical rationale.** ECHO-301 (epacadostat + pembrolizumab in melanoma) did not improve PFS/OS over pembrolizumab monotherapy. The TME metabolic target class is biologically compelling but clinically harder than single-agent ICI.

<!-- STUDY-TABLE:START page=metabolic tier=contested -->
### Human-study evidence

*No human-study citations in this section.*
<!-- STUDY-TABLE:END -->


## Suspected but unconfirmed

- <span class="sp sp-mouse">mouse</span> **Hypoalbuminemia causally drives ICI resistance via macrophage arginine biosynthesis impairment** (LLC mouse model)[^pmid:41940988]. TAM depletion or dietary arginine supplementation rescues anti-PD-1 efficacy. Would recast a routine prognostic lab as a reversible driver. Single preclinical model; no patient-level intervention data.
- <span class="sp sp-mouse">mouse</span> **Lactate → AARS1 → PD-L1 K280 lactylation** is also a metabolic input (see [tumor-intrinsic](tumor-intrinsic.md))[^pmid:41864972]. The paradoxical finding that exogenous lactate *enhances* anti-PD-L1 efficacy in preclinical models needs reconciliation.
- <span class="sp sp-mouse">mouse</span> **HILPDA-driven lipogenesis → PD-L1 palmitoylation** connects lipid metabolism directly to PD-L1 stability[^pmid:41876831]. See [tumor-intrinsic](tumor-intrinsic.md).

<!-- STUDY-TABLE:START page=metabolic tier=suspected -->
### Human-study evidence

*No human-study citations in this section.*
<!-- STUDY-TABLE:END -->


## Emerging

- <span class="sp sp-mouse">mouse</span> **M2 TAM-PGE2 → TIGIT axis in MSS CRC** (see [t-cell-exhaustion](t-cell-exhaustion.md))[^pmid:41196020] — a concrete combinatorial target set (COX2i, PGE2R antagonist, TIGIT blockade) in an indication where PD-1 has consistently failed.
- <span class="sp sp-mouse">mouse</span> **KSR2 (kinase suppressor of Ras 2) is a tumor-intrinsic metabolic checkpoint for anti-PD-1 resistance**: upregulated in resistant lung cancer, KSR2 drives Warburg-effect glucose reprogramming (enhanced uptake, lactate accumulation, disrupted TCA cycle) that creates an immunosuppressive TME with depleted CD8+ TILs and enriched Tregs[^doi:10.1007/s00262-026-04394-z]. KSR2 knockdown resensitizes resistant tumors; connects oncogenic Ras scaffold biology to metabolic immune evasion as a potentially druggable axis.
- <span class="sp sp-mouse">mouse</span> **Immune cell-intrinsic STING activation drives paracrine CRC tumor ferroptosis via TBK1→cPLA2→arachidonic acid→ACSL4 lactylation**[^doi:10.1073/pnas.2524594123]. STING signaling in immune cells leads TBK1 to phosphorylate cPLA2 at Ser505, releasing arachidonic acid (AA) into the TME; adjacent tumor cells take up AA, inhibiting EP300-mediated ACSL4 K426 lactylation and promoting ACSL4-dependent ferroptosis. STING agonist synergizes with anti-PD-1 by engaging this relay. Distinct from the existing IFN-γ→IRF1→AGPAT3 ferroptosis axis: the sensitizing signal originates in immune cells and is transmitted paraculturally via a lipid mediator rather than acting autocrinally on tumor cell lipid metabolism.
- <span class="sp sp-mouse">mouse</span> <span class="sp sp-human">human</span> **PID1 acts as a metabolic checkpoint in tumor-associated macrophages**, limiting LDL receptor expression and thereby suppressing oxysterol production; PID1 loss generates oxysterols that switch macrophage fate to antitumoral phenotypes and improve anti-PD-1 efficacy[^doi:10.1038/s43018-026-01189-0]. Pan-cancer human TAM data confirm elevated PID1 with immunosuppressive signatures. A new lipid-metabolic axis controlling TAM immunosuppression, distinct from arginine depletion, kynurenine, lactate, and PGE2 axes. See also [TME exclusion](tme-exclusion.md).

<!-- STUDY-TABLE:START page=metabolic tier=emerging -->
### Human-study evidence

*No human-study citations in this section.*
<!-- STUDY-TABLE:END -->


## Theme

The recent literature in this period places increasing emphasis on **metabolic inputs operating on multiple different substrates at once**: CD8 killing capacity (ferroptosis via AGPAT3), PD-L1 protein stability (palmitoylation, lactylation), macrophage polarization (arginine), and TAM-driven TIGIT induction. These are not a single "metabolic resistance" mechanism but a heterogeneous set of plausible druggable inputs.

## Practical takeaways

- Hypoalbuminemia remains an informative prognostic marker; whether arginine supplementation should become part of ICI practice is not yet evidence-based.
- Do not expect the next-generation metabolic combo (CD39/CD73, IDO2, arginase inhibitors) to be a uniform benefit; learn from the IDO experience that preclinical rationale alone does not guarantee clinical benefit.

---

[^pmid:41940988]: Hypoalbuminemia / arginine 2026. [Link](https://pubmed.ncbi.nlm.nih.gov/41940988/).
[^pmid:41864972]: AARS1 PD-L1 lactylation 2026. [Link](https://pubmed.ncbi.nlm.nih.gov/41864972/).
[^pmid:41876831]: HILPDA PD-L1 palmitoylation 2026. [Link](https://pubmed.ncbi.nlm.nih.gov/41876831/).
[^pmid:41196020]: TAM-PGE2-TIGIT 2026. [Link](https://pubmed.ncbi.nlm.nih.gov/41196020/).
[^doi:10.1007/s00262-026-04394-z]: Ge 2026 Cancer Immunology, Immunotherapy — KSR2 as metabolic checkpoint linking Ras signaling to anti-PD-1 resistance via Warburg-effect glucose reprogramming; TME immunosuppression reversed by KSR2 knockdown. [Link](https://doi.org/10.1007/s00262-026-04394-z).
[^doi:10.1073/pnas.2524594123]: PNAS 2026 — immune cell-intrinsic STING drives tumor ferroptosis via TBK1→cPLA2→arachidonic acid→ACSL4 K426 lactylation in CRC; paracrine immune-to-tumor ferroptosis relay; STING agonist + anti-PD-1 synergy. [Link](https://doi.org/10.1073/pnas.2524594123).
[^doi:10.1038/s43018-026-01189-0]: Zheng et al. 2026 Nature Cancer — PID1 maintains immunosuppressive TAM identity via LDL receptor limitation → suppressed oxysterol production; PID1 loss → oxysterol generation → macrophage fate switch to antitumoral phenotypes; pan-cancer human expression + mouse functional data. [Link](https://doi.org/10.1038/s43018-026-01189-0).
