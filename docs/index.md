# io-resistance-genie

!!! warning "Work in progress / experiment"
    This site is in early prototype. The living synthesis will populate after the first scheduled literature ingest completes. Until then, this page is a placeholder.

A continuously-updated, curated synthesis of the most important mechanistic findings and surprising clinical results on resistance to anti-PD1 therapy in cancer.

## What this site is

Weekly, a scheduled agent scans new PubMed and bioRxiv/medRxiv papers matching a tuned query on anti-PD1 resistance. It triages each for relevance and novelty against the synthesis already published here, extracts structured findings from the ones worth keeping, and revises this home page — and the per-mechanism deep-dive pages — to reflect genuinely new knowledge.

The intent is a **living review article**, not a feed. Incremental confirmations are absorbed silently. Only findings that `refine`, `challenge`, or add something `novel` to the synthesis land in the dated [changelog](#changelog).

## How it works

- **Sources** — PubMed + bioRxiv/medRxiv via Europe PMC
- **Pipeline** — triage → structured extraction → editorial synthesis → commit
- **Cadence** — weekly
- **Source code** — [pirl-unc/io-resistance-genie](https://github.com/pirl-unc/io-resistance-genie)

## Planned sections

Once the pipeline runs, the synthesis will be organized by mechanism class:

- **Antigen presentation** — HLA loss of heterozygosity, β2M mutations, TAP defects, proteasome subunits
- **IFN-γ signaling** — JAK1/JAK2, IFNGR, STAT1
- **Tumor-intrinsic signaling** — WNT/β-catenin, PTEN, MYC, LKB1
- **Tumor microenvironment exclusion** — TGF-β, VEGF, myeloid skewing, stromal barriers
- **T-cell exhaustion** — TOX, alternative checkpoints, terminal differentiation
- **Metabolic** — adenosine, tryptophan/IDO, lactate, lipid mediators
- **Microbiome** — gut composition, antibiotic effects
- **Clinical interventions** — combination trials with surprising outcomes

## Changelog

No entries yet — the first scheduled run will write `changelog/YYYY-MM-DD.md` if any meaningful deltas are detected.

## Appendix

A full index of every paper seen by the pipeline (kept or rejected) will live at [Papers](papers.md).
