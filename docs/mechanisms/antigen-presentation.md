# Antigen presentation

## Confidently known

- <span class="sp sp-human">human</span> **JAK1/JAK2 loss-of-function drives both primary and acquired anti-PD-1 resistance.** Zaretsky 2016 (NEJM) documented acquired JAK1 or JAK2 LOF (with LOH) plus one B2M truncating mutation in 3 of 4 melanoma patients relapsing on pembrolizumab[^pmid:27433843]. Shin 2017 extended the same mechanism to primary non-responders despite high TMB[^pmid:27903500]. Rare (<5% of all failures) but biochemically definitive; the mutant tumors are non-responsive to IFN-γ.
- <span class="sp sp-mouse">mouse</span> **PTPN2 is the tumor-intrinsic inverse of JAK/STAT resistance.** An in vivo CRISPR screen (Manguso 2017) identified Ptpn2 loss in tumor cells as an ICI sensitizer by amplifying IFN-γ/JAK-STAT signaling[^pmid:28723893]. Now clinically pursued (e.g., ABBV-514 class).
- <span class="sp sp-human">human</span> **HLA-I allele-specific LOH is a common, positively selected immune-escape event.** McGranahan 2017 (TRACERx 100) used LOHHLA to show HLA LOH in ~40% of NSCLCs, enriched at metastatic sites, with subclonal neoantigen association[^pmid:29107330]. Replicated pan-cancer.
- <span class="sp sp-human">human</span> **dMMR/MSI-H tumors respond broadly to pembrolizumab** (Le 2017)[^pmid:28596308]; basis of the first tissue-agnostic FDA approval and of KEYNOTE-177 for 1L dMMR mCRC[^pmid:33264544]. The presumed mechanism is massive neoantigen load from mismatch-repair failure.

<!-- STUDY-TABLE:START page=antigen-presentation tier=established -->
### Human-study evidence

| Study | N | Feature | Effect | 95% CI / p | Method |
|---|---:|---|---|---|---|
| [Zaretsky 2016](https://pubmed.ncbi.nlm.nih.gov/27433843/) | n=4 (melanoma patients with late relapse on pembrolizumab) | acquired JAK1/JAK2 LOF or B2M truncation | acquired resistance mechanism 3 of 4 relapse tumors harbored a candidate lesion | — | paired WES + functional IFN-γ / MHC-I assays |
| [Shin 2016](https://pubmed.ncbi.nlm.nih.gov/27903500/) | n=39 (23 melanoma + 16 MMR-deficient CRC non-responders) | biallelic JAK1/JAK2 LOF | primary-resistance prevalence ~4% melanoma, ~6% MMR-d CRC non-responders | — | WES + cell-line IFN-γ / ISG induction assays |
| [McGranahan 2017](https://pubmed.ncbi.nlm.nih.gov/29107330/) | n=100 (TRACERx 100 NSCLC) | allele-specific HLA-I LOH | frequency / selection ~40% HLA-I LOH; subclonal, enriched at metastatic sites | — | LOHHLA (allele-specific WES) |
| [Le 2017](https://pubmed.ncbi.nlm.nih.gov/28596308/) | n=86 (phase 2 expansion across 12 tumor types, MMR-deficient tumors) | MMR deficiency | ORR 53% (CR 21%) | — | MMR IHC / MSI testing + pembro phase 2 |
| [André 2020](https://pubmed.ncbi.nlm.nih.gov/33264544/) | n=307 (KEYNOTE-177 phase 3, treatment-naive dMMR/MSI-H mCRC) | 1L pembrolizumab vs 5-FU-based chemotherapy | PFS HR mPFS 16.5 vs 8.2 mo; HR 0.60 | 95% CI 0.45–0.80, p=0.0002 | phase 3 RCT |
<!-- STUDY-TABLE:END -->


## Contradictions / surprises

- <span class="sp sp-human">human</span> **HLA-I LOH is not deterministic.** Landmark biology established the mechanism; clinical implementation has been more nuanced. Some HLA-LOH patients still respond to anti-PD-1, especially when residual heterozygous HLA alleles present the dominant neoantigen(s). The predictive signal depends on which allele is lost, the tumor type, and the neoantigen landscape. So the correct clinical reading is "HLA LOH is a risk marker, not a disqualifier."
- <span class="sp sp-human">human</span> **β2M loss sometimes doesn't prevent response.** The canonical acquired-resistance mechanism in Zaretsky 2016 documents B2M loss causing PD-1 resistance, but rare B2M-low/null tumors still respond — likely via NK-mediated killing or non-classical HLA presentation. β2M/JAK lesions together explain only a minority of acquired failures in larger cohorts.
- <span class="sp sp-human">human</span> **TMB does not generalize cleanly across tumor types.** Rizvi 2015 established the NSCLC association[^pmid:25765070]; Snyder 2014 the melanoma anti-CTLA-4 association[^pmid:25409260]. FDA's pan-tumor pembrolizumab approval for TMB ≥10 mut/Mb has been controversial — certain high-TMB histologies (some gliomas) show limited benefit. The threshold is assay- and context-dependent.
- <span class="sp sp-human">human</span> **The "shared neoantigen tetrapeptide signature" from Snyder 2014 did not replicate.** Only the coarse TMB association survived.
- <span class="sp sp-human">human</span> **KEYNOTE-177 showed dMMR is not universal within mCRC.** ~29% of patients had primary progression on pembrolizumab (worse than chemo in the first 6 months), and final OS did not reach statistical significance (HR ~0.74, crossover confounded)[^pmid:33264544]. dMMR is necessary-but-not-sufficient even in its strongest indication.

<!-- STUDY-TABLE:START page=antigen-presentation tier=contested -->
### Human-study evidence

| Study | N | Feature | Effect | 95% CI / p | Method |
|---|---:|---|---|---|---|
| [Rizvi 2015](https://pubmed.ncbi.nlm.nih.gov/25765070/) | NSCLC discovery + validation cohorts | nonsynonymous tumor mutational burden | DCB / PFS enrichment cutoff ~178 nonsynonymous mutations separates DCB from no-benefit | — | WES |
| [Snyder 2014](https://pubmed.ncbi.nlm.nih.gov/25409260/) | n=64 (discovery n=25 + validation n=39 melanoma on anti-CTLA-4) | somatic mutational load (and shared-neoantigen tetrapeptide signature) | clinical benefit association mutational load associated with benefit | P=0.01 | WES |
| [André 2020](https://pubmed.ncbi.nlm.nih.gov/33264544/) | n=307 (KEYNOTE-177 phase 3, treatment-naive dMMR/MSI-H mCRC) | 1L pembrolizumab vs 5-FU-based chemotherapy | PFS HR mPFS 16.5 vs 8.2 mo; HR 0.60 | 95% CI 0.45–0.80, p=0.0002 | phase 3 RCT |
<!-- STUDY-TABLE:END -->


## Suspected but unconfirmed

- <span class="sp sp-human">human</span> **deltaHED** — a metric combining germline HLA heterozygosity with somatic HLA-I alterations — **predicts worse PD-1 outcomes despite higher TMB/neoantigen load** across POLARIS-02 (NPC), melanoma, and JUPITER-06 (ESCC) cohorts[^pmid:41601354]. Inverts the naïve "more divergent HLA → more neoantigens → better response" prediction. Retrospective; needs prospective validation in a single-agent PD-1 setting.

<!-- STUDY-TABLE:START page=antigen-presentation tier=suspected -->
### Human-study evidence

| Study | N | Feature | Effect | 95% CI / p | Method |
|---|---:|---|---|---|---|
| [Xu 2026](https://pubmed.ncbi.nlm.nih.gov/41601354/) | n=729 (3 cohorts: 164 NPC (POLARIS-02), 88 melanoma, 477 ESCC (JUPITER-06)) | deltaHED (germline + somatic HLA-I evolutionary divergence) | PFS/OS direction worse on PD-1 blockade despite higher TMB/neoantigen load | — | HLA typing + WES (deltaHED metric) |
<!-- STUDY-TABLE:END -->


## Emerging

- <span class="sp sp-mouse">mouse</span> **PAR-2 (F2RL1) activation suppresses DC antigen presentation in lung cancer.** A selective negative allosteric modulator (I-117) restores presentation and synergizes with anti-PD-1 in preclinical models — novel GPCR-to-APC axis with a druggable lead (this period's literature).
- <span class="sp sp-human">human</span> **Tumor B2M expression as a TMB/PD-L1-independent response biomarker in R/M HNSCC progressing on anti-PD-1** (multi-omics 2026). Moves B2M from "LOF = resistance" framing toward a graded expression biomarker.

<!-- STUDY-TABLE:START page=antigen-presentation tier=emerging -->
### Human-study evidence

*No human-study citations in this section.*
<!-- STUDY-TABLE:END -->


## Practical takeaways

- HLA LOH detection (LOHHLA, companion tools) is *not yet* a clinical-grade decision aid; report it as risk context, not a disqualification.
- dMMR / MSI-H remains the strongest single biomarker, but KEYNOTE-177's biphasic PFS warns that a subset will fail immediately; early radiologic reassessment at ~2 months is worth considering.
- TMB thresholds vary by assay and histology; treat the FDA pan-tumor cutoff as a heuristic, not a universal predictor.

---

[^pmid:27433843]: Zaretsky 2016 NEJM. [Link](https://pubmed.ncbi.nlm.nih.gov/27433843/).
[^pmid:27903500]: Shin 2017 Cancer Discov. [Link](https://pubmed.ncbi.nlm.nih.gov/27903500/).
[^pmid:28723893]: Manguso 2017 Nature. [Link](https://pubmed.ncbi.nlm.nih.gov/28723893/).
[^pmid:29107330]: McGranahan 2017 Cell. [Link](https://pubmed.ncbi.nlm.nih.gov/29107330/).
[^pmid:28596308]: Le 2017 Science. [Link](https://pubmed.ncbi.nlm.nih.gov/28596308/).
[^pmid:33264544]: André 2020 NEJM KEYNOTE-177. [Link](https://pubmed.ncbi.nlm.nih.gov/33264544/).
[^pmid:25765070]: Rizvi 2015 Science. [Link](https://pubmed.ncbi.nlm.nih.gov/25765070/).
[^pmid:25409260]: Snyder 2014 NEJM. [Link](https://pubmed.ncbi.nlm.nih.gov/25409260/).
[^pmid:41601354]: deltaHED 2026. [Link](https://pubmed.ncbi.nlm.nih.gov/41601354/).
