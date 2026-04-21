# Antigen presentation

Antigen presentation is the most well-characterized axis of ICI resistance: HLA class I loss of heterozygosity, β2-microglobulin mutations, and defects in TAP / proteasomal processing all cause downstream CD8-mediated killing failure. The first wave of this synthesis adds a more subtle layer: **HLA evolutionary divergence itself — the genotypic "width" of the patient's presentation repertoire — may predict PD-1 outcomes in a direction opposite to the naïve prediction**.

## deltaHED: germline + somatic HLA-I divergence predicts worse PD-1 outcomes

Yuan *et al.* introduced **deltaHED**, a metric that integrates germline HLA evolutionary divergence with somatic alterations to HLA-I alleles observed in the tumor[^pmid:41601354]. Across three independent cohorts — 164 recurrent/metastatic nasopharyngeal carcinomas from POLARIS-02, 88 melanomas, and 477 esophageal squamous cell carcinomas from JUPITER-06 — high deltaHED was positively correlated with TMB and neoantigen load *and* negatively correlated with PFS and OS under PD-1 blockade. In ESCC the effect was specific to the immunotherapy arm of the randomized comparison, ruling out purely prognostic interpretations. High deltaHED also tracked with higher frequencies of mutations in antigen-processing and TCR-pathway genes.

**Why this is surprising.** Prior germline HED work has typically associated higher divergence with *better* ICI outcomes, on the reasoning that a broader binding repertoire presents more neoantigens. The deltaHED inversion suggests that a tumor actively accruing HLA-level diversity is one that is *escaping*, not one with expanded presentation capacity — divergence may index the history of immune pressure rather than current presentation function.

**Caveats.** Retrospective biomarker analyses; germline vs somatic attribution of the divergence signal is not fully resolved; the ESCC arm received PD-1 + chemotherapy. Prospective validation in a single-agent PD-1 setting is needed.

## What's not in this seed

Standard antigen-processing defects (β2M LOH, HLA-I LOH, TAP1/2, proteasome subunits, PTPN2/PTPN1) remain load-bearing in the field but did not surface in the top-ranked set from this three-month window. They should be expected to appear in subsequent runs as the window expands.

---

[^pmid:41601354]: deltaHED metric validated in POLARIS-02, melanoma, and JUPITER-06 cohorts. PMID [41601354](https://pubmed.ncbi.nlm.nih.gov/41601354/).
