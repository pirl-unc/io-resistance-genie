# Microbiome

## Confidently known

- <span class="sp sp-mouse">mouse</span> **Gut microbiota modulate ICI efficacy in mouse models** (Sivan 2015 Bifidobacterium[^pmid:26541606]; Vétizou 2015 Bacteroides/CTLA-4[^pmid:26541610]). Gnotobiotic/vendor-swap designs, cohousing controls, and FMT demonstrate causality in mice.
- <span class="sp sp-human">human</span> **Antibiotic exposure around ICI initiation is associated with worse outcomes** (Routy 2018[^pmid:29097494]). The antibiotic-harm signal has replicated across tumor types and is the most consistently reproducible microbiome observation in this field. Clinically actionable: avoid non-essential antibiotics in the weeks surrounding ICI start.
- <span class="sp sp-human">human</span> **Gut microbiota composition differs between responders and non-responders** in multiple independent human cohorts (Gopalakrishnan 2018[^pmid:29097493], Routy 2018[^pmid:29097494], Matson 2018). The *existence* of an association is well established.

<!-- STUDY-TABLE:START page=microbiome tier=established -->
### Human-study evidence

| Study | N | Feature | Effect | 95% CI / p | Method |
|---|---:|---|---|---|---|
| [Routy 2017](https://pubmed.ncbi.nlm.nih.gov/29097494/) | n=249 (NSCLC, RCC, urothelial on anti-PD-1/PD-L1) | peri-ICI antibiotic exposure / A. muciniphila abundance | OS HR antibiotics → shorter PFS/OS (NSCLC mOS ~8 vs ~20 mo; HR ~3.5) | — | clinical-record audit + shotgun metagenomics |
| [Gopalakrishnan 2017](https://pubmed.ncbi.nlm.nih.gov/29097493/) | n=112 (melanoma on anti-PD-1; shotgun-metagenomics subset n=43 (30 R, 13 NR)) | gut alpha diversity / Faecalibacterium enrichment | response association higher diversity & Faecalibacterium in responders | P<0.01 | 16S / shotgun metagenomics + responder→GF-mouse FMT |
<!-- STUDY-TABLE:END -->


## Contradictions / surprises

- <span class="sp sp-human">human</span> <span class="sp sp-mouse">mouse</span> **Specific responder-associated taxa do not replicate across geographies.** Gopalakrishnan highlighted Faecalibacterium / Ruminococcaceae; Routy highlighted Akkermansia muciniphila; Matson highlighted Bifidobacterium longum. Meta-analyses (Lee 2022, McCulloch 2022 Nat Med) found **no single taxon reliably predicts anti-PD-1 response across cohorts**. Signatures are cohort-specific.
- <span class="sp sp-human">human</span> **Akkermansia relationship is non-monotonic.** Derosa 2022 Nat Med showed patients with very high A. muciniphila relative abundance had *worse* outcomes than those with intermediate levels. A simple "more Akkermansia = better" reading is wrong.
- <span class="sp sp-human">human</span> <span class="sp sp-mouse">mouse</span> **Bacteroidales sign-flipped across checkpoint targets.** Vétizou 2015 highlighted Bacteroides fragilis as beneficial for anti-CTLA-4[^pmid:26541610]; Gopalakrishnan 2018 reported Bacteroidales enrichment as associated with anti-PD-1 non-response[^pmid:29097493]. The discordance is not fully reconciled.
- <span class="sp sp-mouse">mouse</span> **Bifidobacterium's dramatic preclinical effect (Sivan 2015[^pmid:26541606]) has not cleanly translated to humans.** The mouse vendor-effect mechanism may be too context-dependent to survive the heterogeneity of human microbiomes.

<!-- STUDY-TABLE:START page=microbiome tier=contested -->
### Human-study evidence

| Study | N | Feature | Effect | 95% CI / p | Method |
|---|---:|---|---|---|---|
| [Gopalakrishnan 2017](https://pubmed.ncbi.nlm.nih.gov/29097493/) | n=112 (melanoma on anti-PD-1; shotgun-metagenomics subset n=43 (30 R, 13 NR)) | gut alpha diversity / Faecalibacterium enrichment | response association higher diversity & Faecalibacterium in responders | P<0.01 | 16S / shotgun metagenomics + responder→GF-mouse FMT |
<!-- STUDY-TABLE:END -->


## Suspected but unconfirmed

- <span class="sp sp-human">human</span> <span class="sp sp-mouse">mouse</span> No strong new mechanism nominations in this window. The current state is that the microbiome *does* modulate ICI biology, but which specific taxa, how, and how to manipulate them clinically remain open.

<!-- STUDY-TABLE:START page=microbiome tier=suspected -->
### Human-study evidence

*No human-study citations in this section.*
<!-- STUDY-TABLE:END -->


## Emerging

- <span class="sp sp-human">human</span> **FMT from anti-PD-1 responders can rescue anti-PD-1-refractory melanoma.** Baruch 2021 (phase I, 3/10 objective responses)[^pmid:33303685] and Davar 2021 (phase II, 6/15 clinical benefit including ~20% ORR)[^pmid:33542131] converge independently. **This is the most surprising and actionable microbiome finding to date** — it implies that some proportion of anti-PD-1 refractoriness reflects a reversible host-microbiome state rather than tumor-intrinsic escape.
- <span class="sp sp-human">human</span> The Davar study showed a mechanistic signature: reduced intratumoral IL-8+ myeloid cells, increased CD8+ T cell activation, consistent with microbiome-driven TME reprogramming. This is the first plausible mechanistic link between gut state and tumor immune state beyond correlative signatures.

<!-- STUDY-TABLE:START page=microbiome tier=emerging -->
### Human-study evidence

| Study | N | Feature | Effect | 95% CI / p | Method |
|---|---:|---|---|---|---|
| [Baruch 2020](https://pubmed.ncbi.nlm.nih.gov/33303685/) | n=10 (phase I FMT in anti-PD-1-refractory metastatic melanoma) | FMT from anti-PD-1-responder donors + anti-PD-1 reinduction | ORR 3/10 (1 CR, 2 PR) | — | phase I FMT trial |
| [Davar 2021](https://pubmed.ncbi.nlm.nih.gov/33542131/) | n=15 (single-arm phase II FMT in anti-PD-1-refractory melanoma) | responder-FMT + pembrolizumab | clinical benefit / ORR 6/15 benefit; ORR ~20% | — | phase II single-arm trial |
<!-- STUDY-TABLE:END -->


## Practical takeaways

- **Antibiotics:** avoid unnecessary antibiotic exposure in the 1–2 months around ICI initiation. This is the most robust clinical implication of the microbiome literature.
- **Probiotics / specific supplementation:** not evidence-based as ICI adjuncts outside a clinical trial.
- **Diet:** high-fiber diet shows associations with better ICI outcomes in observational data but is not rigorously established as causal in humans.
- **FMT:** investigational. 20–30% response rates in small refractory trials are promising enough to support ongoing trials but not standard of care.

---

[^pmid:26541606]: Sivan 2015 Science Bifidobacterium. [Link](https://pubmed.ncbi.nlm.nih.gov/26541606/).
[^pmid:26541610]: Vétizou 2015 Science Bacteroides / CTLA-4. [Link](https://pubmed.ncbi.nlm.nih.gov/26541610/).
[^pmid:29097493]: Gopalakrishnan 2018 Science. [Link](https://pubmed.ncbi.nlm.nih.gov/29097493/).
[^pmid:29097494]: Routy 2018 Science. [Link](https://pubmed.ncbi.nlm.nih.gov/29097494/).
[^pmid:33303685]: Baruch 2021 Science FMT phase I. [Link](https://pubmed.ncbi.nlm.nih.gov/33303685/).
[^pmid:33542131]: Davar 2021 Science FMT phase II. [Link](https://pubmed.ncbi.nlm.nih.gov/33542131/).
