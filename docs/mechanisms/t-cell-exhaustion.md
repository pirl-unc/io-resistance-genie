# T-cell exhaustion and intrinsic biology

T-cell exhaustion is the operational substrate on which PD-1 blockade acts. Recent work both extends the catalog of inhibitory receptors beyond the canonical PD-1/CTLA-4/LAG-3/TIM-3 set and — more unexpectedly — **questions whether PD-1 signaling itself is purely suppressive**.

## PD-1 protects clonally expanding T cells from restimulation-induced cell death

Among the most foundationally challenging recent findings, an *in vitro* study of human primary CD4+ and CD8+ T cells showed that **transient upregulation of PD-1 on clonally expanding effector cells protects them from restimulation-induced cell death (RICD)**[^pmid:41748562]. PD-L1 engagement of PD-1 attenuated proximal TCR/CD28 signaling, modulated pro- and anti-apoptotic proteins, and rescued T cells from RICD in a dose- and synapse-proximity-dependent manner, with the strongest rescue under CD28 co-ligation. Terminally differentiated PD-1-low CD8 effectors were only moderately protected — the protective effect maps onto freshly expanding, PD-1-high clones.

**The implication.** Anti-PD-1 blockade in the release-the-brakes framing "unleashes" effector function. This study suggests PD-1 also has a homeostatic survival role during clonal expansion; blockade could therefore *sensitize* some populations to activation-induced cell death in a regime where continued antigen exposure drives repeated TCR engagement. This is a distinct mechanistic channel from classical "exhaustion reversal" and could help explain variable durability of response.

**Caveats.** In vitro human primary T cell system only. No *in vivo* or patient-level validation. Clinical relevance depends on whether an analogous regime of continuous high antigen exposure + PD-1 blockade occurs in patients. A high-priority validation target.

## KLRG1: a novel inhibitory checkpoint in anti-PD-1-resistant melanoma

Lou *et al.* introduced **KLRG1 as a novel inhibitory checkpoint axis** beyond the established set[^pmid:41956544]. KLRG1 is upregulated on CD8 T cells after checkpoint therapy; KLRG1-high TILs were enriched in anti-PD-1-resistant melanoma patient tumors. KLRG1 genetic knockout, tumor N-cadherin (the KLRG1 ligand) deletion, and a **novel anti-human KLRG1 monoclonal antibody** all reduced tumor progression through combined CD8 T, NK, and gamma-delta T cell effects. The mAb was tested in humanized KLRG1 knock-in mice.

The KLRG1-cadherin axis nominates a checkpoint mechanistically distinct from PD-1, CTLA-4, LAG-3, and TIM-3 — and provides a pharmacologic lead.

**Caveats.** No clinical efficacy data yet; humanized mouse models imperfectly predict patient response.

## T cell-intrinsic VISTA enforces CD8 dysfunction and synergizes with anti-CTLA-4

Xu *et al.* dissected cell-intrinsic vs. myeloid VISTA and found **T cell-intrinsic VISTA enforces CD8 dysfunction**[^pmid:41837284]. Its deletion enhanced early CD8 priming and expansion, but durable tumor control required combination with CTLA-4 blockade because trans-VISTA on myeloid cells and compensatory CTLA-4 upregulation sustained dysfunction. A VISTA-deficient cytotoxic T cell transcriptional signature correlated with favorable ICI outcomes in patient cohorts.

The study positions VISTA as a tractable combination-IO target whose benefit may depend on co-blockade of CTLA-4. Direct relevance to PD-1 resistance is inferred from shared dysfunction programs, not directly tested.

## TAM-PGE2 drives PD-1+TIGIT+ terminal exhaustion in MSS CRC

Li *et al.* dissected why MSS colorectal cancer resists PD-L1 blockade: **M2-like TAMs produce PGE2 via COX1/2**, which drives TIGIT upregulation on PD-1+ CD8 T cells, generating a terminally exhausted phenotype[^pmid:41196020]. M2-TAM depletion, COX2 inhibition, PGE2-receptor inhibition, or TIGIT blockade reduced TIGIT, restored CD8 function, and improved PD-L1 blockade activity in preclinical models. Human CRC transcriptomics corroborated the TAM-COX-TIGIT axis.

This provides a specific combinatorial rationale (COX2i or TIGIT blockade + PD-L1) for an indication in which single-agent PD-1 has consistently failed.

## Anti-TIM-3 + anti-PD-1 salvages PD-1-pretreated classical Hodgkin lymphoma

In a phase Ib trial (NCT05400876), **anti-TIM-3 (TQB2618, 600 mg Q3W) + anti-PD-1 (penpulimab, 200 mg Q3W)** produced clinically meaningful responses in relapsed/refractory classical Hodgkin lymphoma patients who had already failed prior PD-1/PD-L1 therapy[^pmid:41963080]. ORR was **52% (1 CR, 10 PRs) in 21 evaluable patients**, with grade ≥3 TRAEs in 24% and median DOR/OS not reached at 14.1-month median follow-up.

**Why this is notable.** cHL is already highly responsive to single-agent PD-1 (owing to 9p24.1 amplification and Reed-Sternberg PD-L1 reliance); the question is whether re-engaging checkpoint biology after prior PD-1 failure can salvage. A 52% ORR is a strong signal, though the cohort is small and single-arm.

**Caveats.** Small phase Ib (n=21 evaluable); Chinese sites only; DOR/OS immature.

## What's not in this seed

Classical exhaustion transcription factors (TOX, TCF7/TCF1, NR4A), terminal vs progenitor exhaustion biology, alternative checkpoints beyond KLRG1 (e.g., TIGIT as an isolated topic, BTLA, NKG2A, HHLA2), and the epigenetic fixation of exhaustion (stable chromatin states) did not surface in this three-month window but are core background that will likely appear as the window expands.

---

[^pmid:41748562]: PD-1 protects clonally expanding T cells from restimulation-induced cell death. PMID [41748562](https://pubmed.ncbi.nlm.nih.gov/41748562/).
[^pmid:41956544]: KLRG1 as a novel checkpoint in anti-PD-1-resistant melanoma. PMID [41956544](https://pubmed.ncbi.nlm.nih.gov/41956544/).
[^pmid:41837284]: T cell-intrinsic VISTA synergizing with CTLA-4 blockade. PMID [41837284](https://pubmed.ncbi.nlm.nih.gov/41837284/).
[^pmid:41196020]: TAM-PGE2-TIGIT axis in MSS CRC. PMID [41196020](https://pubmed.ncbi.nlm.nih.gov/41196020/).
[^pmid:41963080]: Anti-TIM-3 + penpulimab in PD-1-pretreated cHL. PMID [41963080](https://pubmed.ncbi.nlm.nih.gov/41963080/).
