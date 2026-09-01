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
- <span class="sp sp-mouse">mouse</span> <span class="sp sp-human">human</span> **Citraconate (an itaconate isomer) is markedly depleted from exhausted and hypoxic CD8 T cells in the tumor microenvironment; its depletion drives stemness collapse and ferroptosis through the PDE1A/C–cAMP–PKA–ALOX5 axis**[^doi:10.1126/sciimmunol.adz0348]. Citraconate supplementation preserves stem-like T cell characteristics, limits ALOX5-driven arachidonic acid peroxidation and ferroptosis, maintains mitochondrial integrity, and potentiates ICI in preclinical models. Lower ALOX5 or PDE1A expression in patients with cancer correlates with less T cell exhaustion and improved ICI responsiveness (Liu et al. 2026, Science Immunology). Defines a metabolite-depletion vulnerability in exhausted T cells distinct from TOX/NFAT-mediated chromatin fixation, BETi/polyamine (ODC1) reinvigoration, and PD-L1 post-translational axes — the ferroptotic fate of exhausted T cells is driven by citraconate loss, not lipid peroxidation from TME lipid availability. Patient-level biomarker pair (ALOX5, PDE1A) is immediately testable in prospective ICI cohorts.
- <span class="sp sp-mouse">mouse</span> <span class="sp sp-invitro">in vitro</span> **PPARα activation reprograms the fibroinflammatory liver microenvironment (FILM) to restore GSDME-dependent pyroptosis and overcome anti-PD-1 resistance in HCC** (Chen, Xiong, Huang et al. 2026)[^doi:10.1038/s41467-026-75770-7]. FILM suppresses GSDME-mediated pyroptosis in tumor cells and drives immune exclusion; PPARα agonism reverses this fibroinflammatory reprogramming, restores GSDME cleavage, and synergizes with anti-PD-1 in syngeneic mouse models and patient-derived organoids. Positions PPARα — already an approved target in metabolic liver disease (fibrates) — as a candidate sensitizer for HCC immunotherapy; the fibroinflammatory stromal reprogramming angle distinguishes this from the arginine, oxysterol, citraconate, and lactate metabolic axes already described. See also [TME exclusion](tme-exclusion.md).
- <span class="sp sp-mouse">mouse</span> **SSBP4 promotes tumor-intrinsic cholesteryl ester biosynthesis to suppress CD8+ T-cell activation and confer anti-PD-1 resistance** (Ou et al. 2026)[^doi:10.1158/2326-6066.CIR-25-1312]. SSBP4, a previously uncharacterized protein, upregulates cholesterol synthesis genes in tumor cells, leading to excess cholesteryl ester accumulation that directly impairs intratumoral CD8+ T-cell activation; SSBP4 ablation restores T-cell function and significantly improves anti-PD-1 efficacy in preclinical tumor models. Identifies cholesteryl ester (not free cholesterol) as the functionally immunosuppressive lipid species, distinguishing this from T-cell-intrinsic cholesterol accumulation in the exhaustion literature.

<!-- STUDY-TABLE:START page=metabolic tier=emerging -->
### Human-study evidence

*No human-study citations in this section.*
<!-- STUDY-TABLE:END -->


## Theme

The recent literature places increasing emphasis on **metabolic inputs operating on multiple different substrates at once**: CD8 killing capacity (ferroptosis via AGPAT3 or the citraconate-PDE1A/C-ALOX5 axis), PD-L1 protein stability (palmitoylation, lactylation), macrophage polarization (arginine, oxysterols), and TME immunosuppression (PGE2 from COX1/2, Warburg-effect lactate). The citraconate finding adds a new layer: **it is a CD8 T cell-intrinsic metabolite whose depletion by the hypoxic/exhausted state causes ferroptosis from within**, rather than a TME metabolite acting extrinsically on T cells. These are not a single "metabolic resistance" mechanism but a heterogeneous set of plausible druggable inputs at distinct compartments and substrates.

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
[^doi:10.1126/sciimmunol.adz0348]: Liu et al. 2026 Science Immunology — citraconate (itaconate isomer) depletion from exhausted/hypoxic CD8 T cells drives stemness loss and ferroptosis via PDE1A/C-cAMP-PKA-ALOX5; supplementation potentiates ICI; lower ALOX5/PDE1A expression correlates with less exhaustion and better ICI responsiveness in patients. [Link](https://doi.org/10.1126/sciimmunol.adz0348).
[^doi:10.1038/s41467-026-75770-7]: Chen, Xiong, Huang et al. 2026 Nature Communications — PPARα activation overcomes FILM-associated anti-PD-1 resistance in HCC via GSDME-dependent pyroptosis; syngeneic mouse models and patient-derived organoids. [Link](https://doi.org/10.1038/s41467-026-75770-7).
[^doi:10.1158/2326-6066.CIR-25-1312]: Ou et al. 2026 Cancer Immunology Research — SSBP4 promotes cholesterol biosynthesis in tumor cells, causing cholesteryl ester accumulation that suppresses CD8+ T cell activation; SSBP4 abrogation improves anti-PD-1 efficacy in preclinical models. [Link](https://doi.org/10.1158/2326-6066.CIR-25-1312).
