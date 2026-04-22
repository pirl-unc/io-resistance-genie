# Tumor microenvironment exclusion

## Confidently known

- <span class="sp sp-human">human</span> **Pre-existing CD8+ T-cell infiltrate at the invasive margin predicts pembrolizumab response in melanoma** (Tumeh 2014)[^pmid:25428505]. The inflamed / excluded / desert taxonomy has been validated pan-tumor and anchors the cancer-immunity set-point framework (Chen & Mellman 2017)[^pmid:28102259].
- <span class="sp sp-human">human</span> <span class="sp sp-mouse">mouse</span> **TGF-β signaling in peritumoral fibroblasts excludes T cells.** Mariathasan 2018 in urothelial carcinoma (IMvigor210) defined the F-TBRS (fibroblast TGF-β response signature) in atezolizumab non-responders, whose T cells were trapped in collagen-rich stroma[^pmid:29443960]. Tauriello 2018 established the mouse mechanism in a quadruple-mutant MSS CRC GEMM where TGF-β blockade unleashes Th1/CTL responses and renders liver metastases susceptible to anti-PD-L1[^pmid:29443964].

<!-- STUDY-TABLE:START page=tme-exclusion tier=established -->
### Human-study evidence

| Study | N | Feature | Effect | 95% CI / p | Method |
|---|---:|---|---|---|---|
| [Tumeh 2014](https://pubmed.ncbi.nlm.nih.gov/25428505/) | n=46 (metastatic melanoma on pembrolizumab; discovery n=46 + validation n=15) | pre-existing CD8⁺ T cells at the invasive tumor margin | response prediction (AUC) AUC ~0.9 in discovery cohort | — | IHC + multiplex IF + TCR-seq |
| [Mariathasan 2018](https://pubmed.ncbi.nlm.nih.gov/29443960/) | n=298 (IMvigor210 atezolizumab-treated metastatic urothelial carcinoma) | fibroblast TGF-β response signature (F-TBRS) | response direction non-responders enriched for F-TBRS and T-cell-excluded phenotype | — | bulk RNA-seq |
<!-- STUDY-TABLE:END -->


## Contradictions / surprises

- <span class="sp sp-human">human</span> **TGF-β is biologically robust but has clinically disappointed.** Bintrafusp alfa (TGFβRII trap / anti-PD-L1 bifunctional) failed pivotal trials — INTR@PID lung 037 discontinued 2021, biliary tract halted. Galunisertib + durvalumab, NIS793 combinations in MSS CRC — modest or negative. Likely reflects redundancy (TGF-β has pleiotropic roles), dose-limiting cardiotoxicity, or context-specific effects. A textbook translational gap between compelling biology and clinical benefit.
- <span class="sp sp-human">human</span> **IPRES underperformed as an independent predictor.** Hugo 2016[^pmid:26997480] nominated an EMT/wound-healing/angiogenesis transcriptomic signature in innately resistant melanoma. Subsequent validation across independent cohorts has been mixed. IPRES overlaps heavily with TGF-β and stromal signatures and adds little beyond CD8, PD-L1, TMB, and pan-fibroblast measures.
- <span class="sp sp-mouse">mouse</span> **WNT/β-catenin activation as exclusion driver — stronger in mice than in patients.** Spranger 2015 defined the CCL4 / Batf3+ DC recruitment mechanism[^pmid:25970248]. Clinical correlations weaker; WNT-inhibitor + ICI combinations limited by toxicity.

<!-- STUDY-TABLE:START page=tme-exclusion tier=contested -->
### Human-study evidence

| Study | N | Feature | Effect | 95% CI / p | Method |
|---|---:|---|---|---|---|
| [Hugo 2016](https://pubmed.ncbi.nlm.nih.gov/26997480/) | n=38 (pretreatment melanoma biopsies on anti-PD-1) | IPRES transcriptional signature (EMT / ECM / angiogenesis / wound-healing) | response direction IPRES-high enriched among non-responders | — | bulk RNA-seq + WES |
<!-- STUDY-TABLE:END -->


## Suspected but unconfirmed

- <span class="sp sp-mouse">mouse</span> **TROP2 associates with claudin-7 to regulate tight junctions and exclude T cells from TNBC**[^pmid:41932810]. TROP2 loss or hRS7 (sacituzumab govitecan antibody component) targeting restores infiltration and enhances anti-PD-1 efficacy. Reframes TROP2 from pure ADC target to a barrier-mechanism target. Single humanized TROP2 syngeneic model; needs broader preclinical and patient validation.
- <span class="sp sp-human">human</span> **hMENA-high TGF-β-driven CAFs define an ICT-resistance transcriptional program validated against OAK phase III in NSCLC** (this period)[^pmid:41592891]. Signature-level clinical anchoring but mechanistic causality is inferential from in vitro CAF experiments.

<!-- STUDY-TABLE:START page=tme-exclusion tier=suspected -->
### Human-study evidence

| Study | N | Feature | Effect | 95% CI / p | Method |
|---|---:|---|---|---|---|
| [Melchionna 2026](https://pubmed.ncbi.nlm.nih.gov/41592891/) | TCGA NSCLC + SU2C + OAK (NCT02008227) | hMENA⁺ TGF-β-driven CAF 9-gene signature | prognosis / ICT resistance direction signature-high → worse prognosis, ICT resistance | — | 9-gene RNA signature |
<!-- STUDY-TABLE:END -->


## Emerging

- <span class="sp sp-human">human</span> **Single-cell spatial transcriptomics defines six tissue niches that stratify neoadjuvant PD-1/PD-L1 response in cSCC better than PD-L1 IHC**[^pmid:41617396]. High antigen-presentation / B-plasma / inflammatory-keratinocyte niches enrich responders; proliferative-keratinocyte / low-APC-myeloid / fibroblast-rich-EMT niches dominate non-responders. Niche-based biomarkers may eventually outperform single-marker IHC.
- <span class="sp sp-human">human</span> **LOAd703 (CD40L/4-1BBL oncolytic adenovirus) + atezolizumab in anti-PD-1-refractory melanoma** reprograms the myeloid compartment and restores ICI-responsive immune signatures in 24 patients[^pmid:41888981]. Biomarker-level evidence; small single-arm; but few interventions reliably rescue refractory melanoma.

<!-- STUDY-TABLE:START page=tme-exclusion tier=emerging -->
### Human-study evidence

| Study | N | Feature | Effect | 95% CI / p | Method |
|---|---:|---|---|---|---|
| [Lee 2026](https://pubmed.ncbi.nlm.nih.gov/41617396/) | n=27 (3 cSCC cohorts incl. 2 phase II trials) | six spatial tissue niches (high-APC / B-plasma / inflammatory-keratinocyte vs. proliferative / low-APC-myeloid / fibroblast-EMT) | pathologic response prediction niche profiling outperformed PD-L1 IHC | — | single-cell spatial transcriptomics |
| [Grauers 2026](https://pubmed.ncbi.nlm.nih.gov/41888981/) | n=24 (single-arm phase I/II, anti-PD-1-refractory stage IV melanoma) | intratumoral LOAd703 (CD40L/4-1BBL oncolytic adenovirus) + atezolizumab | immune-signature biomarker increased DC markers, T-cell infiltration, EM CD8⁺; decreased circulating Tregs | — | multi-parameter flow + TME transcriptomics |
<!-- STUDY-TABLE:END -->


## Practical takeaways

- Inflamed vs. excluded vs. desert remains a useful pre-treatment mental model. A patient with high CD8 at the invasive margin but non-response may have a downstream exhaustion or metabolic problem; a patient with a desert tumor faces a different biology (likely WNT/β-catenin, STK11, low TMB, or low DC recruitment).
- **Do not count on TGF-β-targeting agents to rescue excluded tumors yet.** The clinical data on bintrafusp alfa, galunisertib, NIS793 are disappointing despite strong preclinical rationale.

---

[^pmid:25428505]: Tumeh 2014 Nature. [Link](https://pubmed.ncbi.nlm.nih.gov/25428505/).
[^pmid:28102259]: Chen & Mellman 2017 Nature. [Link](https://pubmed.ncbi.nlm.nih.gov/28102259/).
[^pmid:29443960]: Mariathasan 2018 Nature. [Link](https://pubmed.ncbi.nlm.nih.gov/29443960/).
[^pmid:29443964]: Tauriello 2018 Nature. [Link](https://pubmed.ncbi.nlm.nih.gov/29443964/).
[^pmid:26997480]: Hugo 2016 Cell IPRES. [Link](https://pubmed.ncbi.nlm.nih.gov/26997480/).
[^pmid:25970248]: Spranger 2015 Nature. [Link](https://pubmed.ncbi.nlm.nih.gov/25970248/).
[^pmid:41932810]: TROP2-claudin-7 TNBC 2026. [Link](https://pubmed.ncbi.nlm.nih.gov/41932810/).
[^pmid:41592891]: hMENA CAF OAK 2026. [Link](https://pubmed.ncbi.nlm.nih.gov/41592891/).
[^pmid:41617396]: Spatial niches cSCC 2026. [Link](https://pubmed.ncbi.nlm.nih.gov/41617396/).
[^pmid:41888981]: LOAd703 melanoma 2026. [Link](https://pubmed.ncbi.nlm.nih.gov/41888981/).
