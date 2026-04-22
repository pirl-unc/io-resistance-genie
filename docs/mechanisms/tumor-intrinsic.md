# Tumor-intrinsic signaling

## Confidently known

- <span class="sp sp-human">human</span> **STK11/LKB1 co-mutation with KRAS in lung adenocarcinoma drives primary PD-1/PD-L1 resistance** despite TMB-intermediate/high status (Skoulidis 2018)[^pmid:29773717]. The "KL" subgroup had ORR 7.4% vs 35.7% for KRAS/TP53-comutated ("KP") tumors; replicated in multiple subsequent NSCLC cohorts and used in trial stratification.
- <span class="sp sp-human">human</span> **PTEN loss drives ICI resistance** in melanoma via PI3K-AKT activation, VEGF/CCL2 secretion, reduced autophagy-dependent killing, and reduced CD8 infiltration (Peng 2016)[^pmid:26645196]. Replicated in melanoma and pan-cancer.

<!-- STUDY-TABLE:START page=tumor-intrinsic tier=established -->
### Human-study evidence

| Study | N | Feature | Effect | 95% CI / p | Method |
|---|---:|---|---|---|---|
| [Skoulidis 2018](https://pubmed.ncbi.nlm.nih.gov/29773717/) | SU2C + CheckMate-057 KRAS-mutant NSCLC ICI cohorts | STK11/LKB1 co-mutation (KL subgroup) | ORR KL 7.4% vs KP 35.7% (SU2C); 0% vs 57.1% (CheckMate-057) | P<0.001 | targeted/WES + clinical correlation |
| [Peng 2015](https://pubmed.ncbi.nlm.nih.gov/26645196/) | n=39 (small melanoma anti-PD-1 cohort) | tumor PTEN loss | CD8 infiltration / PFS direction reduced intratumoral CD8, worse PFS | — | IHC + clinical correlation |
<!-- STUDY-TABLE:END -->


## Contradictions / surprises

- <span class="sp sp-mouse">mouse</span> **WNT/β-catenin activation — strong mouse biology, weaker clinical signal.** Spranger 2015 established that melanoma β-catenin activation excludes CD103+ Batf3+ DCs via reduced CCL4[^pmid:25970248]. Clinical cohorts show weaker, more context-dependent correlations. WNT-inhibitor + ICI combinations have been limited by toxicity; β-catenin status is not a clinical biomarker.
- <span class="sp sp-human">human</span> **PBRM1 LOF as ICI sensitizer in ccRCC has not replicated.** Miao 2018[^pmid:29301960] found PBRM1 LOF enriched in responders in two cohorts. Subsequent CheckMate-009/010/025 (Braun 2020 Nat Med) and IMmotion analyses did not confirm the predictive value.
- <span class="sp sp-human">human</span> **IPRES signature underperformed as an independent predictor.** Hugo 2016[^pmid:26997480] defined an EMT/wound-healing/ECM/angiogenesis transcriptional signature in innately resistant melanoma. Subsequent validation has been mixed — IPRES overlaps heavily with TGF-β and stromal signatures and adds little above CD8, PD-L1, TMB, or pan-fibroblast measures.
- <span class="sp sp-human">human</span> **BRCA2 association with ICI response did not replicate** (from the same Hugo paper).

<!-- STUDY-TABLE:START page=tumor-intrinsic tier=contested -->
### Human-study evidence

| Study | N | Feature | Effect | 95% CI / p | Method |
|---|---:|---|---|---|---|
| [Miao 2018](https://pubmed.ncbi.nlm.nih.gov/29301960/) | n=98 (discovery n=35 + validation n=63 ccRCC on anti-PD-1 ± anti-CTLA-4) | PBRM1 LOF | clinical-benefit enrichment enriched among responders | P=0.012 (discovery); P=0.0071 (validation) | WES |
| [Hugo 2016](https://pubmed.ncbi.nlm.nih.gov/26997480/) | n=38 (pretreatment melanoma biopsies on anti-PD-1) | IPRES transcriptional signature (EMT / ECM / angiogenesis / wound-healing) | response direction IPRES-high enriched among non-responders | — | bulk RNA-seq + WES |
<!-- STUDY-TABLE:END -->


## Suspected but unconfirmed

- <span class="sp sp-mouse">mouse</span> **Lactate → AARS1 → PD-L1 K280 lactylation stabilizes PD-L1 against HUWE1-mediated degradation**[^pmid:41864972] — but **exogenous lactate paradoxically enhances anti-PD-L1 efficacy preclinically.** The paradox must be reconciled before clinical translation. Directly implicates metabolic inputs in checkpoint protein turnover.
- <span class="sp sp-mouse">mouse</span> **HILPDA-sustained KLF5-driven fatty acid synthesis palmitoylates PD-L1 at Cys272**, stabilizing membrane PD-L1[^pmid:41876831]. TRIM21 engagement by fenretinide degrades HILPDA and restores anti-PD-1 efficacy in breast cancer mouse models. A post-translational PD-L1 regulatory layer distinct from transcriptional control. Preclinical; single tumor type; fenretinide has prior clinical exposure which helps translation.
- <span class="sp sp-human">human</span> **NOTCH3 → RBPJ → PVR → TIGIT** in CRC[^pmid:41808828]: tumor-intrinsic NOTCH3 transcriptionally upregulates PVR, engaging TIGIT on CD8 cells. Low/mutant NOTCH3 predicts better ICB survival in 102-patient + MSKCC cohorts. No pharmacologic NOTCH3 inhibitor tested in vivo.

<!-- STUDY-TABLE:START page=tumor-intrinsic tier=suspected -->
### Human-study evidence

| Study | N | Feature | Effect | 95% CI / p | Method |
|---|---:|---|---|---|---|
| [Ma 2026](https://pubmed.ncbi.nlm.nih.gov/41808828/) | n=102 (institutional CRC cohort + MSKCC pan-cancer validation) | NOTCH3 mutation or low expression | OS direction improved on ICB | — | targeted sequencing + IHC + RNA-seq |
<!-- STUDY-TABLE:END -->


## Emerging

- <span class="sp sp-mouse">mouse</span> **PKMYT1 inhibition with clinical-grade RP-6306 activates cGAS-STING in castration-resistant prostate cancer**[^pmid:41617394]. Type I/II IFN signaling upregulates CCL5/CXCL10, enhances CD8 infiltration, and potentiates anti-PD-L1 in syngeneic models. Prostate cancer has been stubbornly ICI-refractory; a druggable cell-cycle-kinase–innate-sensing connection is clinically provocative.

<!-- STUDY-TABLE:START page=tumor-intrinsic tier=emerging -->
### Human-study evidence

*No human-study citations in this section.*
<!-- STUDY-TABLE:END -->


## Theme

The emerging literature in this period is heavily focused on **post-translational regulation of PD-L1** (palmitoylation, lactylation) as a distinct layer from transcriptional control. If these preclinical mechanisms yield clinical PTM-modulating strategies, they would complement rather than replace PD-L1-targeting antibodies. None is clinical yet.

---

[^pmid:29773717]: Skoulidis 2018 Cancer Discov. [Link](https://pubmed.ncbi.nlm.nih.gov/29773717/).
[^pmid:26645196]: Peng 2016 Cancer Discov. [Link](https://pubmed.ncbi.nlm.nih.gov/26645196/).
[^pmid:25970248]: Spranger 2015 Nature. [Link](https://pubmed.ncbi.nlm.nih.gov/25970248/).
[^pmid:29301960]: Miao 2018 Science. [Link](https://pubmed.ncbi.nlm.nih.gov/29301960/).
[^pmid:26997480]: Hugo 2016 Cell IPRES. [Link](https://pubmed.ncbi.nlm.nih.gov/26997480/).
[^pmid:41864972]: AARS1 PD-L1 K280 lactylation. [Link](https://pubmed.ncbi.nlm.nih.gov/41864972/).
[^pmid:41876831]: HILPDA-KLF5 PD-L1 palmitoylation. [Link](https://pubmed.ncbi.nlm.nih.gov/41876831/).
[^pmid:41808828]: NOTCH3-PVR-TIGIT. [Link](https://pubmed.ncbi.nlm.nih.gov/41808828/).
[^pmid:41617394]: PKMYT1-cGAS-STING in CRPC. [Link](https://pubmed.ncbi.nlm.nih.gov/41617394/).
