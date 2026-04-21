# Tumor microenvironment exclusion

"Exclusion" is a single word covering multiple distinct architectural programs: stromal barriers (CAFs, ECM), tight-junction exclusion, vascular/hypoxic barriers, myeloid-rich nests, and spatial compartmentalization that keeps CD8 T cells distant from tumor cells. Recent work reinforces that these programs can coexist within a single tumor and that responder vs non-responder status may be best captured by **niche composition**, not single markers.

## Six spatial niches stratify neoadjuvant PD-1/PD-L1 response in cutaneous SCC

Single-cell spatial transcriptomics of 27 cSCC patients across three cohorts (including two phase II neoadjuvant trials) identified six distinct tissue niches[^pmid:41617396]:

- High antigen presentation (**responder-enriched**)
- B/plasma cell (**responder-enriched**)
- Inflammatory keratinocyte (**responder-enriched**)
- Proliferative keratinocyte (**non-responder-dominant**)
- Low antigen-presentation myeloid (**non-responder-dominant**)
- Fibroblast-rich EMT (**non-responder-dominant**)

Pretreatment niche profiling outperformed PD-L1 IHC for predicting pathologic response. Different responder-enriched vs. non-responder niches can coexist in the same tumor, implying that within-tumor heterogeneity of architectural programs — not only cellular composition — determines clinical outcome.

**Caveats.** 27 patients is a small cohort; 1.7 mm tissue cores may undersample heterogeneity; all associations are observational with no causal perturbation of the niches. Generalization beyond cSCC is untested.

## hMENA TGF-β-driven CAFs define a clinically validated exclusion signature

In NSCLC, Melchionna *et al.* defined a **hMENA-overexpressing myofibroblast-like CAF subset** in which hMENA and TGF-β signaling reciprocally reinforce each other, driving PD-L1 upregulation, EMT, ECM remodeling, and secretion of cytokines that expand Tregs and impair CD8/CD4 function[^pmid:41592891]. A **9-gene signature** derived from this CAF state correlates with poor prognosis in TCGA NSCLC *and* with ICT resistance in SU2C and in the **OAK phase III** trial — elevating a CAF-centric mechanism from preclinical biology to a candidate clinical biomarker.

**Caveats.** Signature validation is retrospective; causality in patients is inferred from *ex vivo* CAF experiments. Quantitative effect sizes are not stated in the primary abstract.

## TROP2-claudin-7 tight junctions exclude T cells from TNBC

Kramer *et al.* showed that TROP2, best known as an ADC target for sacituzumab govitecan, **associates with claudin-7 to regulate tight junctions and form a barrier that excludes T cells** from triple-negative breast tumors[^pmid:41932810]. TROP2 loss deregulated tight-junction proteins and enabled CD8+ infiltration; hRS7 (the sacituzumab antibody component) combined with anti-PD-1 enhanced efficacy in a humanized TROP2 syngeneic model. Human TNBC data showed high TROP2 correlated with anti-PD-1 non-response.

**Why this reframes TROP2.** Clinical rationales for TROP2 ADC + IO have largely been "cytotoxic payload releases tumor antigens." This work adds a mechanism-first rationale: TROP2 expression is itself a functional driver of barrier-mediated exclusion. The ADC may work in part by removing a structural barrier, not only by delivering payload.

## Restoring response: LOAd703 reprograms myeloid compartments in anti-PD-1-refractory melanoma

A 24-patient phase I/II study dosed **intratumoral LOAd703** (an oncolytic adenovirus armed with TMZ-CD40L and 4-1BBL) plus IV atezolizumab in stage IV ICI-refractory melanoma[^pmid:41888981]. Paired tumor, PBMC, and plasma multi-omics showed reprogramming of the TAM compartment toward APC-like phenotypes, increased circulating CD40+ DC-like cells, elevated T-cell infiltration signatures, expansion of effector-memory CD8, and reductions in Tregs. These are biomarker signals previously associated with ICI response, now observed in a population in which confirmed anti-PD-1 refractoriness was the enrollment criterion.

**Caveats.** Single-arm, small (n=24), biomarker-focused endpoints rather than systematic response assessment. Prior therapies were heterogeneous.

## What's not in this seed

Neoangiogenic exclusion (VEGF, anti-angiogenic combinations), stromal desmoplasia in pancreatic and cholangiocarcinoma, and microbiome-driven exclusion programs did not surface strongly in this three-month window. Expect these in subsequent runs.

---

[^pmid:41617396]: Six spatial niches stratifying neoadjuvant response in cSCC. PMID [41617396](https://pubmed.ncbi.nlm.nih.gov/41617396/).
[^pmid:41592891]: hMENA CAF signature validated in OAK phase III. PMID [41592891](https://pubmed.ncbi.nlm.nih.gov/41592891/).
[^pmid:41932810]: TROP2-claudin-7 barrier-mediated T-cell exclusion in TNBC. PMID [41932810](https://pubmed.ncbi.nlm.nih.gov/41932810/).
[^pmid:41888981]: LOKON003: LOAd703 + atezolizumab in anti-PD-1-refractory melanoma. PMID [41888981](https://pubmed.ncbi.nlm.nih.gov/41888981/).
