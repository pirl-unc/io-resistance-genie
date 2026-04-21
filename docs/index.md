# Mechanisms of resistance to anti-PD1 therapy

!!! info "Living synthesis — seeded 2026-04-21"
    This is the first pass synthesis, built from a triaged 3-month backfill (2026-01-20 → 2026-04-21) of Europe PMC (PubMed + bioRxiv/medRxiv). Eighteen papers were selected from 1,000 candidates. The synthesis is regenerated on each scheduled run; the [changelog](changelog/2026-04-21.md) tracks what changed.

## Executive summary

Resistance to PD-1 blockade is not one disease. The last three months of literature continue a pattern visible for several years: **multiple, partially-overlapping mechanisms operate simultaneously within the same tumor**, and the dominant mechanism varies by cancer type, prior therapy, and spatial niche. Three themes are prominent in recent work. First, biomarker biology has moved beyond TMB: HLA evolutionary divergence between germline and somatic alleles (deltaHED) can predict *worse* PD-1 outcomes despite higher neoantigen load, complicating the simple "more neoantigens → better response" heuristic[^pmid:41601354]. Second, **post-translational regulation of PD-L1 itself** — palmitoylation by a HILPDA/KLF5 lipogenic circuit[^pmid:41876831], lactylation at K280 that blocks HUWE1-mediated degradation[^pmid:41864972] — is emerging as a druggable layer distinct from transcriptional PD-L1 control. Third, **combination and sequencing strategies continue to produce surprising clinical wins** in settings where single-agent PD-1 has failed, most notably the ATOMIC phase 3 trial establishing adjuvant atezolizumab + mFOLFOX6 in stage III dMMR colon cancer (HR 0.50)[^pmid:41880612].

A genuinely foundational finding also appeared: PD-1 expression on clonally expanding T cells is, in a specific regime, *protective* against restimulation-induced cell death (RICD)[^pmid:41748562]. If replicated *in vivo*, this inverts part of the dogma that anti-PD-1 is a pure "release the brakes" intervention and implies some of the variability in effector-T-cell durability under blockade may reflect loss of homeostatic PD-1 signaling, not merely release of suppression.

The synthesis is organized by mechanism class below. Deep-dive pages for each class carry the full evidence inventory; this page is the overview.

## Antigen presentation

The dominant new finding is that **evolutionary divergence between germline and somatic HLA class I alleles (deltaHED)** predicts worse PD-1 outcomes across three cohorts spanning nasopharyngeal carcinoma (POLARIS-02), melanoma, and esophageal squamous cell carcinoma (JUPITER-06), and does so *despite* high deltaHED correlating with higher TMB and neoantigen load[^pmid:41601354]. In ESCC the association was specific to the immunotherapy arm. High deltaHED also tracked with mutations in antigen-processing and TCR pathways, suggesting that divergence marks ongoing immune escape rather than broad presentation capacity. This refines but does not cleanly challenge the TMB paradigm: high mutational burden remains informative, but an additional HLA-level metric may identify the subset in which TMB fails to predict benefit.

See [mechanisms/antigen-presentation.md](mechanisms/antigen-presentation.md) for details.

## IFN-γ signaling and its metabolic consequences

The canonical IFN-γ → IRF1/STAT1 → antigen presentation + apoptosis axis has long been central to PD-1 biology. New work extends it into lipid metabolism: **IFN-γ-induced IRF1 transcriptionally upregulates AGPAT3**, which remodels tumor lipid composition toward polyunsaturated ether phospholipids that sensitize tumor cells to ferroptosis[^pmid:41807033]. Loss of AGPAT3 impairs IFN-γ-mediated tumor elimination; higher tumor AGPAT3 correlates with better ICI survival. This refines the IFN-γ killing paradigm — it is not only about apoptosis and antigen presentation, but about a lipidomic vulnerability that coexists with the classical pathway and may be pharmacologically accessible.

See [mechanisms/ifn-gamma.md](mechanisms/ifn-gamma.md) for details.

## Tumor microenvironment exclusion

Four findings converge on the idea that **exclusion is not a single phenomenon** but a set of architectural programs that coexist in the same tumor. Spatial single-cell transcriptomics of cutaneous squamous cell carcinoma across three cohorts defined **six distinct niches** — some antigen-presenting and inflammatory (responder-enriched), others proliferative-keratinocyte, low-APC myeloid, or fibroblast-rich EMT (non-responder-dominant) — with niche profiling outperforming PD-L1 IHC for pathologic response[^pmid:41617396]. In NSCLC, **hMENA-high TGF-β-driven CAFs** propagate an exclusion program validated against the OAK phase III trial, elevating a CAF subtype to biomarker status[^pmid:41592891]. In TNBC, **TROP2 associates with claudin-7** to build a tight-junction barrier that excludes T cells; TROP2 loss or targeting restores infiltration and anti-PD-1 efficacy, providing a mechanistic rationale for TROP2 ADC + IO combinations beyond cytotoxic payload delivery[^pmid:41932810]. And in **anti-PD-1-refractory melanoma**, intratumoral LOAd703 (CD40L/4-1BBL-armed oncolytic adenovirus) + atezolizumab reprograms the myeloid compartment to an APC phenotype and restores ICI-responsive systemic immune signatures in 24 patients[^pmid:41888981].

See [mechanisms/tme-exclusion.md](mechanisms/tme-exclusion.md).

## Tumor-intrinsic signaling

Four tumor-intrinsic nodes emerged with mechanism-to-therapeutic arcs:

- **HILPDA → KLF5 → palmitate → PD-L1 palmitoylation at Cys272.** A lipid-droplet regulator stabilizes PD-L1 via a PTM that is blocked by TRIM21-mediated K63 polyubiquitination; fenretinide engages TRIM21 and restores anti-PD-1 efficacy in breast cancer models[^pmid:41876831].
- **NOTCH3 → RBPJ → PVR → TIGIT.** Tumor-intrinsic NOTCH3 transcriptionally upregulates PVR in CRC, engaging TIGIT to suppress CD8 cytotoxicity; loss/mutation of NOTCH3 predicts better ICB survival across two clinical cohorts[^pmid:41808828].
- **PKMYT1 → cGAS-STING.** Inhibition of cell-cycle kinase PKMYT1 with the clinical-grade RP-6306 activates cGAS-STING, upregulates CCL5/CXCL10, and converts immune-cold castration-resistant prostate cancer to anti-PD-L1-responsive disease in preclinical models[^pmid:41617394].
- **Lactate → AARS1 → PD-L1 K280 lactylation.** Lactate drives AARS1-catalyzed lactylation of PD-L1 K280, blocking HUWE1-mediated ubiquitination and stabilizing PD-L1. Counterintuitively, exogenous sodium lactate *enhanced* anti-PD-L1 efficacy in preclinical models[^pmid:41864972], a paradox that warrants careful reconciliation before clinical translation.

See [mechanisms/tumor-intrinsic.md](mechanisms/tumor-intrinsic.md).

## T-cell intrinsic biology and exhaustion

Five findings cluster here, two of them genuinely surprising.

The biggest conceptual shift: **transient PD-1 upregulation on clonally expanding T cells protects them from restimulation-induced cell death** by attenuating TCR/CD28 signaling and modulating pro/anti-apoptotic proteins[^pmid:41748562]. This is an *in vitro* human primary T cell study and needs *in vivo* validation, but if it holds it implies PD-1 blockade could, in some regimes, accelerate effector T-cell attrition rather than merely release suppression — a confound for interpreting response durability.

The second strong new signal is **KLRG1 as a novel inhibitory checkpoint**. KLRG1 is upregulated on CD8+ T cells after checkpoint therapy, correlates with anti-PD-1 resistance in melanoma, and its genetic or antibody-mediated blockade (via a novel anti-human KLRG1 mAb in humanized KLRG1 knock-in mice) reduces tumor progression through combined CD8, NK, and gamma-delta T effects[^pmid:41956544]. The KLRG1–cadherin axis nominates a checkpoint distinct from the established PD-1/CTLA-4/LAG-3/TIM-3 set.

Also notable:

- **T cell-intrinsic VISTA** enforces CD8 dysfunction and its loss synergizes with anti-CTLA-4; the VISTA-deficient cytotoxic signature correlates with better ICI outcomes in patients[^pmid:41837284].
- In MSS colorectal cancer, **M2 TAM-derived PGE2 drives TIGIT upregulation** on PD-1+ CD8 T cells, creating a terminally exhausted phenotype that COX2 or TIGIT blockade can rescue[^pmid:41196020].
- In **PD-1-pretreated classical Hodgkin lymphoma**, adding anti-TIM-3 (TQB2618) to anti-PD-1 penpulimab produced a 52% ORR in 21 patients — a meaningful clinical signal in a post-PD-1-failure setting where re-engaging checkpoint biology is not typically expected to yield substantial salvage[^pmid:41963080].

See [mechanisms/t-cell-exhaustion.md](mechanisms/t-cell-exhaustion.md).

## Metabolic resistance

One strong new signal this period: **hypoalbuminemia from low-protein diet causally drives ICI resistance** in LLC mouse models via impaired macrophage arginine biosynthesis, reduced CD8 infiltration, and expanded TAMs. TAM depletion or arginine supplementation rescues anti-PD-1 efficacy[^pmid:41940988]. The finding reframes hypoalbuminemia not merely as a prognostic biomarker but as a mechanism-anchored, potentially reversible metabolic driver of resistance. Clinical translation would need dietary intervention studies; the preclinical story is a single-model mouse system.

See [mechanisms/metabolic.md](mechanisms/metabolic.md).

## Clinical interventions and surprising outcomes

Three clinical results stand out:

**ATOMIC (NEJM phase 3).** Adjuvant atezolizumab + mFOLFOX6 in stage III dMMR colon cancer cut 3-year DFS events roughly in half (86.3% vs 76.2%; HR 0.50, p<0.001) in 712 patients with 40.9-month median follow-up. OS is not yet mature. Grade ≥3 AE rate rose from 71.9% to 84.1%. This extends ICI benefit into the adjuvant dMMR setting and shifts the locus where future resistance biology will be defined[^pmid:41880612].

**8-gene + mucinous-histology biomarker for CTLA-4 addition in dMMR/MSI-H mCRC.** A k-TSP classifier combined with mucinous histology identifies a 15% subgroup of dMMR/MSI-H mCRC patients in whom anti-CTLA-4 addition to anti-PD-1 yields 72.2% vs 13.8% 24-month PFS (HR 0.10). The subgroup is small (n=25) and the comparison is retrospective across non-randomized regimens, but the effect is large enough to warrant prospective validation[^pmid:41950572].

**LOAd703 in anti-PD-1-refractory melanoma.** The clinical signal (biomarker-level) is covered under TME exclusion above, but deserves flagging here: few interventions reliably re-sensitize confirmed anti-PD-1-refractory melanoma to checkpoint blockade[^pmid:41888981].

See [mechanisms/clinical-interventions.md](mechanisms/clinical-interventions.md).

## Open questions

- **Does PD-1 blockade accelerate effector T-cell attrition in patients?** The [RICD protection finding](mechanisms/t-cell-exhaustion.md) is *in vitro*. The implication would reshape how we think about durability of response.
- **Can post-translational PD-L1 regulation (palmitoylation, lactylation) be drugged clinically?** Fenretinide (TRIM21 engagement) and the AARS1 axis are pharmacologically tractable but far from trials.
- **Is deltaHED additive or orthogonal to TMB in a prospective biomarker strategy?** The three retrospective cohorts are compelling but not decisive.
- **Will the 8-gene dMMR k-TSP biomarker survive prospective validation?** If yes, it could resolve the open question of when to add anti-CTLA-4 to anti-PD-1 in colorectal cancer — a field that has struggled with this for nearly a decade.
- **How much of the TIM-3 result in PD-1-pretreated Hodgkin generalizes?** cHL has unique biology (9p24.1 amplification, Reed-Sternberg cell reliance on PD-L1); a 52% salvage ORR is striking but a single arm at Chinese sites only.
- **Does adjuvant ICI in dMMR disease change the resistance landscape?** ATOMIC brings a large new population into prolonged ICI exposure; mechanisms of late / adjuvant-setting resistance are yet to be characterized.

## Appendix

Every paper ingested by the pipeline — kept or rejected — is listed at [Papers](papers.md).

---

[^pmid:41601354]: Introduction of deltaHED metric across POLARIS-02, melanoma, and JUPITER-06 cohorts. Europe PMC PMID [41601354](https://pubmed.ncbi.nlm.nih.gov/41601354/).
[^pmid:41876831]: HILPDA-KLF5-palmitoylation axis and TRIM21/fenretinide rescue. PMID [41876831](https://pubmed.ncbi.nlm.nih.gov/41876831/).
[^pmid:41864972]: AARS1-mediated PD-L1 K280 lactylation blocks HUWE1 ubiquitination. PMID [41864972](https://pubmed.ncbi.nlm.nih.gov/41864972/).
[^pmid:41880612]: ATOMIC phase 3 trial of adjuvant atezolizumab + mFOLFOX6 in stage III dMMR colon cancer. PMID [41880612](https://pubmed.ncbi.nlm.nih.gov/41880612/).
[^pmid:41748562]: PD-1 protects clonally expanding T cells from restimulation-induced cell death. PMID [41748562](https://pubmed.ncbi.nlm.nih.gov/41748562/).
[^pmid:41807033]: IFN-γ–IRF1–AGPAT3 axis sensitizing tumors to ferroptosis. PMID [41807033](https://pubmed.ncbi.nlm.nih.gov/41807033/).
[^pmid:41617396]: Six spatial niches stratifying neoadjuvant PD-1/PD-L1 response in cSCC. PMID [41617396](https://pubmed.ncbi.nlm.nih.gov/41617396/).
[^pmid:41592891]: hMENA TGF-β CAF signature validated in OAK phase III. PMID [41592891](https://pubmed.ncbi.nlm.nih.gov/41592891/).
[^pmid:41932810]: TROP2-claudin-7 barrier excluding T cells in TNBC. PMID [41932810](https://pubmed.ncbi.nlm.nih.gov/41932810/).
[^pmid:41888981]: LOKON003 phase I/II: intratumoral LOAd703 + atezolizumab in anti-PD-1-refractory melanoma. PMID [41888981](https://pubmed.ncbi.nlm.nih.gov/41888981/).
[^pmid:41808828]: NOTCH3-PVR-TIGIT axis in CRC. PMID [41808828](https://pubmed.ncbi.nlm.nih.gov/41808828/).
[^pmid:41617394]: PKMYT1 inhibition activating cGAS-STING in CRPC. PMID [41617394](https://pubmed.ncbi.nlm.nih.gov/41617394/).
[^pmid:41956544]: KLRG1 as a novel checkpoint in anti-PD-1-resistant melanoma. PMID [41956544](https://pubmed.ncbi.nlm.nih.gov/41956544/).
[^pmid:41837284]: T cell-intrinsic VISTA synergizing with CTLA-4 blockade. PMID [41837284](https://pubmed.ncbi.nlm.nih.gov/41837284/).
[^pmid:41196020]: TAM-PGE2-TIGIT axis in MSS CRC. PMID [41196020](https://pubmed.ncbi.nlm.nih.gov/41196020/).
[^pmid:41963080]: Anti-TIM-3 (TQB2618) + penpulimab in PD-1-pretreated classical Hodgkin lymphoma. PMID [41963080](https://pubmed.ncbi.nlm.nih.gov/41963080/).
[^pmid:41940988]: Hypoalbuminemia, macrophage arginine metabolism, and ICI resistance. PMID [41940988](https://pubmed.ncbi.nlm.nih.gov/41940988/).
[^pmid:41950572]: 8-gene + mucinous classifier identifying dMMR/MSI-H subgroup benefiting from anti-CTLA-4 addition. PMID [41950572](https://pubmed.ncbi.nlm.nih.gov/41950572/).
