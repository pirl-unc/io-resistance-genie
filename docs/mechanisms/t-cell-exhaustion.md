# T-cell exhaustion

## Confidently known

- <span class="sp sp-human">human</span> <span class="sp sp-mouse">mouse</span> **Response to PD-1 blockade depends on a Tcf1+PD-1+ CD8+ stem-like progenitor pool, not on reinvigoration of terminally exhausted effectors.** Siddiqui 2019 (Immunity)[^pmid:30635237] established in mouse tumor models that ablation of the stem-like subset abolishes ICI efficacy. Sade-Feldman 2018 (Cell)[^pmid:30388456] validated the TCF7-high vs TCF7-low CD8 axis in human melanoma scRNA-seq + IF. This reframes why a heavily PD-1+ infiltrate is insufficient without the stem-like compartment.
- <span class="sp sp-mouse">mouse</span> **TOX is the master transcription factor of the exhausted chromatin state** (Alfei 2019 Nature[^pmid:31207603] and concurrent work). Necessary and sufficient to program the exhaustion transcriptome and epigenome; induced via NFAT2 and acts feed-forward. Exhaustion is chromatin-fixed.
- <span class="sp sp-human">human</span> <span class="sp sp-mouse">mouse</span> **The "release the brakes" framing is an oversimplification.** Early PD-1 blockade models implied that blocking PD-1 "reactivates" exhausted effector cells. The TCF7/stem-like progenitor work makes it clearer that the operative mechanism is *proliferative expansion of the progenitor pool*, not reactivation of terminally differentiated effectors.

<!-- STUDY-TABLE:START page=t-cell-exhaustion tier=established -->
### Human-study evidence

| Study | N | Feature | Effect | 95% CI / p | Method |
|---|---:|---|---|---|---|
| [Sade-Feldman 2018](https://pubmed.ncbi.nlm.nih.gov/30388456/) | n=48 (checkpoint-blockade-treated melanoma; 16,291 immune cells sequenced) | TCF7⁺ stem-like vs dysfunctional CD8⁺ T-cell state | response direction TCF7⁺ CD8 frequency associated with response (validation cohort) | — | scRNA-seq + IF validation |
<!-- STUDY-TABLE:END -->


## Contradictions / surprises

- <span class="sp sp-mouse">mouse</span> **TOX ablation impairs both exhaustion *and* T-cell persistence.** The initial hope that TOX antagonism could reverse exhaustion therapeutically has been tempered: TOX-deficient CD8+ cells fail to persist under chronic antigen and die faster. TOX is more accurately a cell-intrinsic survival/differentiation program under chronic antigen than a simple brake on effector function. Direct "drug TOX" strategies should be approached carefully.
- <span class="sp sp-human">human</span> <span class="sp sp-mouse">mouse</span> **Exhaustion is not a single state.** Progenitor / transitional / terminal subsets have distinct biology (Miller 2019 Nat Immunol and related). Clinical biomarkers that sum across these subsets (e.g., bulk PD-1+ IHC) average across functionally different populations.

<!-- STUDY-TABLE:START page=t-cell-exhaustion tier=contested -->
### Human-study evidence

*No human-study citations in this section.*
<!-- STUDY-TABLE:END -->


## Suspected but unconfirmed

- <span class="sp sp-human">human</span> <span class="sp sp-invitro">in vitro</span> **PD-1 expression on clonally expanding T cells partially *protects* them from restimulation-induced cell death** (in vitro human primary T cells)[^pmid:41748562]. PD-L1 engagement attenuates TCR/CD28 signaling and modulates pro/anti-apoptotic proteins. If replicated in vivo, would mean anti-PD-1 could in some regimes *accelerate* effector-T-cell attrition — a direct challenge to the release-the-brakes framing. **High-priority validation target.**
- <span class="sp sp-mouse">mouse</span> **T cell-intrinsic VISTA enforces CD8 dysfunction** (distinct from myeloid VISTA)[^pmid:41837284]; loss synergizes with anti-CTLA-4. Direct relevance to PD-1 resistance is inferred.

<!-- STUDY-TABLE:START page=t-cell-exhaustion tier=suspected -->
### Human-study evidence

*No human-study citations in this section.*
<!-- STUDY-TABLE:END -->


## Emerging

- <span class="sp sp-mouse">mouse</span> **KLRG1 nominated as a novel inhibitory checkpoint** in anti-PD-1-resistant melanoma[^pmid:41956544]. KLRG1 upregulated on CD8 T cells after checkpoint therapy; KLRG1-high TILs enriched in anti-PD-1-refractory tumors. A novel anti-human KLRG1 mAb reduces tumor progression in humanized KLRG1 knock-in mice via combined CD8, NK, and γδ-T effects. Mechanistically distinct from the established PD-1/CTLA-4/LAG-3/TIM-3 set.
- <span class="sp sp-mouse">mouse</span> **M2 TAM-derived PGE2 drives TIGIT upregulation on PD-1+ CD8 T cells in MSS colorectal cancer**[^pmid:41196020], creating terminally exhausted PD-1+TIGIT+ cells and blunting anti-PD-L1. COX2 inhibition, PGE2 receptor antagonism, or TIGIT blockade each restore activity preclinically. Specific combinatorial rationale for an indication where PD-1 monotherapy has consistently failed.
- <span class="sp sp-human">human</span> **Anti-TIM-3 (TQB2618) + anti-PD-1 penpulimab achieves 52% ORR in PD-1-pretreated classical Hodgkin lymphoma**[^pmid:41963080] (n=21 phase Ib). Salvage signal in a setting where re-engaging checkpoint biology was not expected to yield substantial response.

<!-- STUDY-TABLE:START page=t-cell-exhaustion tier=emerging -->
### Human-study evidence

| Study | N | Feature | Effect | 95% CI / p | Method |
|---|---:|---|---|---|---|
| [Hong 2026](https://pubmed.ncbi.nlm.nih.gov/41963080/) | n=21 (phase Ib (NCT05400876), PD-1-pretreated relapsed/refractory cHL) | anti-TIM-3 TQB2618 + anti-PD-1 penpulimab | ORR 52% (1 CR, 10 PR); grade ≥3 TRAE 24% | — | phase Ib clinical trial |
<!-- STUDY-TABLE:END -->


## Practical takeaways

- A heavily PD-1+ infiltrate by IHC is not automatically a good prognostic marker — without stem-like progenitor cells, the proliferative response to blockade can be muted.
- The field's post-PD-1 checkpoint pipeline — LAG-3, TIGIT, TIM-3, and now KLRG1 — is adding real options, though most remain investigational.

---

[^pmid:30635237]: Siddiqui 2019 Immunity. [Link](https://pubmed.ncbi.nlm.nih.gov/30635237/).
[^pmid:30388456]: Sade-Feldman 2018 Cell. [Link](https://pubmed.ncbi.nlm.nih.gov/30388456/).
[^pmid:31207603]: Alfei 2019 Nature TOX. [Link](https://pubmed.ncbi.nlm.nih.gov/31207603/).
[^pmid:41748562]: PD-1 RICD protection 2026. [Link](https://pubmed.ncbi.nlm.nih.gov/41748562/).
[^pmid:41837284]: T-intrinsic VISTA 2026. [Link](https://pubmed.ncbi.nlm.nih.gov/41837284/).
[^pmid:41956544]: KLRG1 2026. [Link](https://pubmed.ncbi.nlm.nih.gov/41956544/).
[^pmid:41196020]: TAM-PGE2-TIGIT MSS CRC 2026. [Link](https://pubmed.ncbi.nlm.nih.gov/41196020/).
[^pmid:41963080]: Anti-TIM-3 + penpulimab cHL 2026. [Link](https://pubmed.ncbi.nlm.nih.gov/41963080/).
