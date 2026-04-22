# Clinical interventions

## Confidently known

- <span class="sp sp-human">human</span> **Ipilimumab inaugurated the durable-survival-plateau paradigm** (Hodi 2010 NEJM)[^pmid:20525992]; 20–26% of metastatic melanoma patients on a long-term OS plateau extending to 10+ years. The nivolumab phase I (Topalian 2012)[^pmid:22658127] extended this proof into anti-PD-1 and showed activity across multiple histologies (melanoma, NSCLC, RCC).
- <span class="sp sp-human">human</span> **Pembrolizumab first-line for NSCLC with PD-L1 TPS ≥50% is standard of care** (KEYNOTE-024)[^pmid:27718847]; 5-year OS benefit confirmed despite ~66% crossover.
- <span class="sp sp-human">human</span> **PD-1 + CTLA-4 combination improves PFS over single-agent PD-1 in advanced melanoma** (CheckMate 067)[^pmid:26027431]; largest relative benefit in PD-L1-negative tumors; ~55% grade 3/4 TRAEs. Durable OS benefit at 6.5+ years.
- <span class="sp sp-human">human</span> **Pembrolizumab in dMMR/MSI-H solid tumors** — basis of the first tissue-agnostic FDA approval (Le 2017)[^pmid:28596308] — and **1L pembrolizumab in dMMR mCRC** (KEYNOTE-177)[^pmid:33264544] are standards of care. **But KEYNOTE-177 has complications** (see contradictions).

<!-- STUDY-TABLE:START page=clinical-interventions tier=established -->
### Human-study evidence

| Study | N | Feature | Effect | 95% CI / p | Method |
|---|---:|---|---|---|---|
| [Hodi 2010](https://pubmed.ncbi.nlm.nih.gov/20525992/) | n=676 (phase 3, previously-treated HLA-A*0201⁺ metastatic melanoma) | ipilimumab 3 mg/kg (± gp100) vs gp100 | OS HR ipi+gp100 vs gp100 mOS 10.0 vs 6.4 mo (HR 0.68); ipi vs gp100 HR 0.66 | p<0.001 (ipi+gp100) / p=0.003 (ipi alone) | phase 3 RCT |
| [Topalian 2012](https://pubmed.ncbi.nlm.nih.gov/22658127/) | n=296 (melanoma 94, NSCLC 76, RCC 33, and others; phase 1 dose-escalation) | nivolumab (BMS-936558) across histologies; PD-L1 IHC predictive | ORR / PD-L1 association melanoma 28%, NSCLC 18%, RCC 27%; PD-L1⁺ vs PD-L1⁻ ORR 36% vs 0% | p=0.006 (PD-L1 association) | phase 1 dose-escalation + PD-L1 IHC |
| [Reck 2016](https://pubmed.ncbi.nlm.nih.gov/27718847/) | n=305 (KEYNOTE-024 phase 3, 1L advanced NSCLC, PD-L1 TPS ≥50%, EGFR/ALK-wt) | PD-L1 TPS ≥50% (pembrolizumab vs platinum doublet) | PFS HR mPFS 10.3 vs 6.0 mo; HR 0.50 | 95% CI 0.37–0.68, p<0.001 | PD-L1 IHC 22C3 |
| [Larkin 2015](https://pubmed.ncbi.nlm.nih.gov/26027431/) | n=945 (CheckMate-067 phase 3, untreated metastatic melanoma) | nivo+ipi vs nivo vs ipi monotherapy | PFS HR (combo vs ipi) mPFS 11.5 vs 6.9 vs 2.9 mo; HR 0.42 combo vs ipi (HR 0.57 nivo vs ipi) | — | phase 3 RCT |
| [Le 2017](https://pubmed.ncbi.nlm.nih.gov/28596308/) | n=86 (phase 2 expansion across 12 tumor types, MMR-deficient tumors) | MMR deficiency | ORR 53% (CR 21%) | — | MMR IHC / MSI testing + pembro phase 2 |
| [André 2020](https://pubmed.ncbi.nlm.nih.gov/33264544/) | n=307 (KEYNOTE-177 phase 3, treatment-naive dMMR/MSI-H mCRC) | 1L pembrolizumab vs 5-FU-based chemotherapy | PFS HR mPFS 16.5 vs 8.2 mo; HR 0.60 | 95% CI 0.45–0.80, p=0.0002 | phase 3 RCT |
<!-- STUDY-TABLE:END -->


## Contradictions / surprises

- <span class="sp sp-human">human</span> **KEYNOTE-177 PFS was biphasic and OS did not reach significance.** Pembrolizumab underperformed chemotherapy in the first ~6 months (~29% primary progression), then crossed over and doubled median PFS (16.5 vs 8.2 mo, HR 0.60). Final OS was HR ~0.74, not statistically significant, largely because chemo patients could cross over to pembrolizumab on progression. Interpretation: dMMR is necessary-but-not-sufficient in mCRC; ~30% have primary resistance that is not currently predictable.
- <span class="sp sp-human">human</span> **bTMB retrospective signal did not confirm prospectively.** Gandara 2018[^pmid:30082870] showed bTMB-high enriched atezolizumab benefit retrospectively in POPLAR/OAK; B-F1RST prospectively did not confirm. bTMB has not achieved broad regulatory adoption.
- <span class="sp sp-human">human</span> **Pan-tumor TMB-high pembrolizumab approval is debated.** The FDA's tissue-agnostic approval for TMB ≥10 mut/Mb (based on KEYNOTE-158) has been controversial as some high-TMB histologies (certain gliomas) show limited benefit. TMB thresholds are assay- and context-specific.
- <span class="sp sp-human">human</span> **TGF-β bifunctional / pathway-blocking combinations have disappointed** despite compelling Mariathasan/Tauriello biology (see [TME exclusion](tme-exclusion.md)). Bintrafusp alfa INTR@PID lung 037 discontinued 2021.
- <span class="sp sp-human">human</span> **IDO + pembrolizumab failed** (ECHO-301) despite compelling preclinical rationale. Cautionary tale for future metabolic-ICI combinations.

<!-- STUDY-TABLE:START page=clinical-interventions tier=contested -->
### Human-study evidence

| Study | N | Feature | Effect | 95% CI / p | Method |
|---|---:|---|---|---|---|
| [Gandara 2018](https://pubmed.ncbi.nlm.nih.gov/30082870/) | POPLAR (test) + OAK (validation) NSCLC atezolizumab | blood TMB ≥16 mut/Mb (FoundationACT ctDNA) | PFS HR (atezo vs docetaxel) HR ~0.65 at bTMB ≥16 in OAK | — | ctDNA (FoundationACT) |
<!-- STUDY-TABLE:END -->


## Suspected but unconfirmed

- <span class="sp sp-human">human</span> **8-gene k-TSP classifier + mucinous histology identifies a ~15% subgroup of dMMR/MSI-H mCRC with extreme benefit from anti-CTLA-4 addition** (HR 0.10 for 24-month PFS; 72.2% vs 13.8%)[^pmid:41950572]. Retrospective across non-randomized comparisons; prospective validation called for. If it holds, would resolve the decade-long question of when to add ipi to nivo-class regimens in dMMR CRC.
- <span class="sp sp-human">human</span> **LOAd703 + atezolizumab in anti-PD-1-refractory melanoma** (n=24) shows biomarker-level rescue of ICI-responsive signatures[^pmid:41888981]. Small single-arm; needs randomized confirmation.

<!-- STUDY-TABLE:START page=clinical-interventions tier=suspected -->
### Human-study evidence

| Study | N | Feature | Effect | 95% CI / p | Method |
|---|---:|---|---|---|---|
| [Ambrosini 2026](https://pubmed.ncbi.nlm.nih.gov/41950572/) | n=163 (pooled across 2 independent dMMR/MSI-H mCRC cohorts) | Cluster A + mucinous histology (15% biomarker-positive subgroup) | 24-mo PFS / HR (Combo vs Mono) 72.2% vs 13.8%; HR 0.10 | 95% CI 0.02–0.39, p<0.001 | 8-gene k-TSP classifier + histology |
| [Grauers 2026](https://pubmed.ncbi.nlm.nih.gov/41888981/) | n=24 (single-arm phase I/II, anti-PD-1-refractory stage IV melanoma) | intratumoral LOAd703 (CD40L/4-1BBL oncolytic adenovirus) + atezolizumab | immune-signature biomarker increased DC markers, T-cell infiltration, EM CD8⁺; decreased circulating Tregs | — | multi-parameter flow + TME transcriptomics |
<!-- STUDY-TABLE:END -->


## Emerging

- <span class="sp sp-human">human</span> **ATOMIC phase 3 (NEJM 2026): adjuvant atezolizumab + mFOLFOX6 in stage III dMMR colon cancer, HR 0.50**[^pmid:41880612]. 3-year DFS 86.3% vs 76.2%; 40.9-month median follow-up; grade 3/4 AEs 84.1% vs 71.9%. OS not yet mature. Extends ICI benefit to the adjuvant dMMR setting. A large new patient population will now experience prolonged ICI exposure.
- <span class="sp sp-human">human</span> **Anti-TIM-3 (TQB2618) + anti-PD-1 penpulimab in PD-1-pretreated classical Hodgkin lymphoma** achieves 52% ORR in 21 evaluable patients[^pmid:41963080]. Salvage signal in a setting where re-engaging checkpoint biology was not expected.

<!-- STUDY-TABLE:START page=clinical-interventions tier=emerging -->
### Human-study evidence

| Study | N | Feature | Effect | 95% CI / p | Method |
|---|---:|---|---|---|---|
| [Sinicrope 2026](https://pubmed.ncbi.nlm.nih.gov/41880612/) | n=712 (phase 3 ATOMIC (NCT02912559), stage III dMMR colon cancer) | atezolizumab + mFOLFOX6 vs mFOLFOX6 alone | 3-yr DFS / HR 86.3% vs 76.2%; HR 0.50 | 95% CI 0.35–0.73, p<0.001 | phase 3 RCT |
| [Hong 2026](https://pubmed.ncbi.nlm.nih.gov/41963080/) | n=21 (phase Ib (NCT05400876), PD-1-pretreated relapsed/refractory cHL) | anti-TIM-3 TQB2618 + anti-PD-1 penpulimab | ORR 52% (1 CR, 10 PR); grade ≥3 TRAE 24% | — | phase Ib clinical trial |
<!-- STUDY-TABLE:END -->


## Practical takeaways

- **1L NSCLC PD-L1 ≥50%:** single-agent pembrolizumab is standard; KEYNOTE-024 data are durable.
- **Metastatic melanoma:** nivolumab + ipilimumab vs single-agent PD-1 is an individualized decision based on disease burden, PD-L1 status, and patient fitness for immune-related toxicity; the combination's largest relative benefit is in PD-L1-negative disease.
- **dMMR mCRC:** pembrolizumab 1L is standard, but counsel patients about the ~30% early-progression risk and reassess imaging at ~2 months.
- **Stage III dMMR colon cancer (post-resection):** ATOMIC brings adjuvant atezolizumab + FOLFOX into the standard-of-care conversation; await OS maturation and guideline uptake.
- **Hyperprogression on anti-PD-1:** a contested phenomenon. Definitions vary; natural history and pseudoprogression confound the literature. Not actionable today as a management decision.

---

[^pmid:20525992]: Hodi 2010 NEJM ipilimumab. [Link](https://pubmed.ncbi.nlm.nih.gov/20525992/).
[^pmid:22658127]: Topalian 2012 NEJM anti-PD-1 phase 1. [Link](https://pubmed.ncbi.nlm.nih.gov/22658127/).
[^pmid:27718847]: Reck 2016 NEJM KEYNOTE-024. [Link](https://pubmed.ncbi.nlm.nih.gov/27718847/).
[^pmid:26027431]: Larkin 2015 NEJM CheckMate 067. [Link](https://pubmed.ncbi.nlm.nih.gov/26027431/).
[^pmid:28596308]: Le 2017 Science dMMR. [Link](https://pubmed.ncbi.nlm.nih.gov/28596308/).
[^pmid:33264544]: André 2020 NEJM KEYNOTE-177. [Link](https://pubmed.ncbi.nlm.nih.gov/33264544/).
[^pmid:30082870]: Gandara 2018 Nat Med bTMB. [Link](https://pubmed.ncbi.nlm.nih.gov/30082870/).
[^pmid:41950572]: 8-gene dMMR biomarker 2026. [Link](https://pubmed.ncbi.nlm.nih.gov/41950572/).
[^pmid:41888981]: LOAd703 2026. [Link](https://pubmed.ncbi.nlm.nih.gov/41888981/).
[^pmid:41880612]: ATOMIC NEJM 2026. [Link](https://pubmed.ncbi.nlm.nih.gov/41880612/).
[^pmid:41963080]: TIM-3 + penpulimab cHL 2026. [Link](https://pubmed.ncbi.nlm.nih.gov/41963080/).
