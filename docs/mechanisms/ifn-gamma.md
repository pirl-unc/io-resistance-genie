# IFN-γ signaling

IFN-γ sensing is a canonical checkpoint for PD-1 response biology: JAK1/JAK2, IFNGR, and STAT1 loss-of-function underlie classical acquired resistance in melanoma, and downstream IRF1-driven antigen presentation is a load-bearing effector limb. New work extends the downstream effector biology into lipid metabolism.

## IFN-γ–IRF1–AGPAT3 remodels tumor lipids toward ferroptosis sensitivity

A 2026 study established that **IRF1, activated by IFN-γ, transcriptionally upregulates AGPAT3**[^pmid:41807033]. AGPAT3 remodels the tumor lipidome toward polyunsaturated ether phospholipids, which sensitize tumor cells to ferroptosis. Genetic loss of AGPAT3 impaired IFN-γ-mediated tumor elimination both *in vitro* and *in vivo*, and higher AGPAT3 expression was associated with immune activation and improved overall survival in ICI-treated patients.

The study integrates machine-learning identification of ferroptosis-associated signatures, single-cell RNA-seq, lipidomics, ChIP-seq/CUT&Tag for IRF1 binding, and functional perturbation — a substantial mechanistic package.

**Why this matters.** The canonical IFN-γ → IRF1 → antigen presentation + Fas-mediated apoptosis framework is incomplete. A parallel limb remodels the target cell's lipid composition to sensitize it to a non-apoptotic death pathway. This does not contradict the canonical pathway; it layers on top. Clinically, it nominates AGPAT3 expression as a candidate ICI response biomarker and suggests that IFN-γ-unresponsive tumors may fail immunotherapy not only because of lost antigen presentation but because the lipidomic ferroptosis axis is not engaged.

**Caveats.** ICI-treated cohort details are thin in the primary abstract. Causal role of specific ether phospholipids in ferroptosis sensitization is inferred from lipidomics + AGPAT3 knockout phenotypes. No pharmacologic AGPAT3 modulator has been tested.

## What's not in this seed

Classical JAK1/JAK2 loss-of-function, IFNGR mutations, STAT1 defects, and CMTM6/CMTM4-mediated PD-L1 stability control did not surface in this three-month window. They remain the backbone of the IFN-γ resistance story and should be expected to appear as the window widens.

---

[^pmid:41807033]: IFN-γ–IRF1–AGPAT3 axis sensitizing tumors to ferroptosis. PMID [41807033](https://pubmed.ncbi.nlm.nih.gov/41807033/).
