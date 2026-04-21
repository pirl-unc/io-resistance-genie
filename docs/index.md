# Mechanisms of resistance to immune checkpoint inhibitors

A living literature review of ICI resistance across PD-1, PD-L1, CTLA-4, LAG-3, TIGIT, TIM-3, and combination regimens. Regenerated on each scheduled update — see [changelog](changelog/2026-04-21.md).

<p class="tier-legend"><span class="tier tier-est">established</span> replicated, field consensus &nbsp;·&nbsp; <span class="tier tier-cont">contested</span> landmark weakened under replication &nbsp;·&nbsp; <span class="tier tier-susp">suspected</span> mechanistic, not yet clinical &nbsp;·&nbsp; <span class="tier tier-emerg">emerging</span> new, worth tracking</p>

## What has held up

- <span class="tier tier-est">established</span> **Pre-existing CD8+ T-cell infiltrate at the invasive margin predicts pembrolizumab response in melanoma** (Tumeh 2014)[^pmid:25428505]. The inflamed / excluded / desert taxonomy has been validated pan-tumor and is the backbone of most subsequent biomarker frameworks (Chen & Mellman 2017)[^pmid:28102259].
- <span class="tier tier-est">established</span> **TMB predicts anti-PD-1 benefit in NSCLC** (Rizvi 2015)[^pmid:25765070] and anti-CTLA-4 benefit in melanoma (Snyder 2014)[^pmid:25409260]. The association survives, but **see "contradictions" for the pan-tumor threshold debate**.
- <span class="tier tier-est">established</span> **dMMR/MSI-H is the single most reliable ICI biomarker across histologies** (Le 2017)[^pmid:28596308]; basis of the first tissue-agnostic FDA approval. Confirmed in KEYNOTE-177 for 1L dMMR mCRC[^pmid:33264544] — but not uniformly predictive (see contradictions).
- <span class="tier tier-est">established</span> **JAK1/JAK2 and B2M LOF cause acquired anti-PD-1 resistance in melanoma** (Zaretsky 2016)[^pmid:27433843]; rare (<5%) but biochemically definitive. JAK1/2 LOF also drives a subset of primary resistance (Shin 2017)[^pmid:27903500]. PTPN2 loss in tumor cells is the inverse — a sensitizer that amplifies IFN-γ response (Manguso 2017)[^pmid:28723893], now in clinical development.
- <span class="tier tier-est">established</span> **KRAS-mutant NSCLC with STK11/LKB1 co-mutation is primary ICI-refractory** despite TMB-intermediate/high status (Skoulidis 2018)[^pmid:29773717]. Now used in NSCLC trial stratification.
- <span class="tier tier-est">established</span> **PD-1 + CTLA-4 combination rescues a meaningful fraction of single-agent PD-1 non-responders in melanoma**, with the largest relative benefit in PD-L1-negative tumors (CheckMate 067)[^pmid:26027431] — indicating CTLA-4 and PD-1 address partly-complementary resistance mechanisms. ~55% grade 3/4 TRAE cost.
- <span class="tier tier-est">established</span> **PD-L1 IHC (TPS ≥50%) prospectively identifies the NSCLC sub-population for whom single-agent PD-1 blockade is sufficient** (KEYNOTE-024)[^pmid:27718847]. The PD-L1-low population defines the monotherapy resistance group; they now receive chemo-IO by default.
- <span class="tier tier-est">established</span> **Response depends on a stem-like Tcf1+PD-1+ CD8+ progenitor pool, not reinvigoration of terminally exhausted effectors** (Siddiqui 2019, Sade-Feldman 2018, Miller 2019)[^pmid:30635237][^pmid:30388456]. Explains why a heavily PD-1+ infiltrate is not enough if it lacks the stem-like subset.
- <span class="tier tier-est">established</span> **TOX is the master transcription factor of the exhausted chromatin state** (Alfei 2019 and concurrent work)[^pmid:31207603]. Epigenetic fixation of exhaustion is a durable barrier to reinvigoration — and TOX ablation impairs both exhaustion *and* persistence, so it is not a simple therapeutic brake.
- <span class="tier tier-est">established</span> **TGF-β signaling in peritumoral fibroblasts drives T-cell exclusion** (Mariathasan 2018 in urothelial[^pmid:29443960]; Tauriello 2018 in MSS CRC GEMM[^pmid:29443964]). **But clinical translation has failed — see contradictions.**
- <span class="tier tier-est">established</span> **Canonical resistance taxonomy — primary / adaptive / acquired** (Sharma 2017)[^pmid:28187290] — remains the organizing framework.

## Where the field has contradicted itself (the surprises)

Known initial findings that later weakened under replication or didn't translate. Useful to avoid over-weighting any single-study narrative.

- <span class="tier tier-cont">contested</span> **HLA-I LOH is a selected immune-escape event (~40% of NSCLCs, McGranahan 2017[^pmid:29107330]) but is *not* deterministic for ICI response.** Subsequent pan-cancer ICI cohorts show some HLA-LOH patients still respond. What matters is *which* allele is lost (loss of the allele presenting a dominant neoantigen), tumor type, and whether residual heterozygous HLA alleles can still present key neoantigens. So: "this patient has HLA LOH" does not imply "this patient will fail anti-PD-1."
- <span class="tier tier-cont">contested</span> **β2M loss does not uniformly predict resistance either.** Documented case-level resistance (Zaretsky 2016[^pmid:27433843]) and rare B2M-low/null tumors that still respond suggest NK-mediated or non-classical HLA-dependent mechanisms can partially compensate. The acquired-resistance rate attributable to β2M/JAK is a small fraction of overall failures.
- <span class="tier tier-cont">contested</span> **Microbiome responder signatures do not replicate cleanly across geographies.** Gopalakrishnan 2018 (Faecalibacterium/Ruminococcaceae)[^pmid:29097493], Routy 2018 (Akkermansia)[^pmid:29097494], Matson 2018 (Bifidobacterium longum), and Sivan 2015[^pmid:26541606] / Vétizou 2015[^pmid:26541610] mouse work each nominated different beneficial taxa. Meta-analyses (Lee 2022, McCulloch 2022 Nat Med) found no single taxon reliably predicts anti-PD-1 response across cohorts. For *Akkermansia* specifically, Derosa 2022 Nat Med showed a non-monotonic relationship — very high levels were worse than intermediate. **Bacteroidales sign-flipped**: beneficial in Vétizou's anti-CTLA-4 mouse work, associated with non-response in Gopalakrishnan's anti-PD-1 cohort. The antibiotic-harm signal is the only microbiome finding that has replicated consistently.
- <span class="tier tier-cont">contested</span> **FMT rescues anti-PD-1-refractory melanoma** (Baruch 2021[^pmid:33303685]: 3/10; Davar 2021[^pmid:33542131]: 6/15 benefit including ORR ~20%). This was unexpected because refractoriness had been widely assumed to reflect tumor-intrinsic escape (B2M/JAK loss), not a reversible host-ecosystem state. The convergent independent replication at Sheba and NCI/Pittsburgh using different donors strengthens the signal.
- <span class="tier tier-cont">contested</span> **TGF-β is a biologically robust exclusion driver that has clinically disappointed.** Bintrafusp alfa (TGFβRII trap / anti-PD-L1 bifunctional) failed pivotal trials — INTR@PID lung 037 discontinued 2021, biliary tract halted. Galunisertib + durvalumab, NIS793 combinations in MSS CRC — modest or negative. A reproducibility gap between GEMM and clinic; likely reflects redundancy, dose-limiting cardiotoxicity of TGF-β antagonism, or context-specific effects.
- <span class="tier tier-cont">contested</span> **bTMB failed prospective validation.** Gandara 2018[^pmid:30082870] retrospectively showed bTMB-high enriches atezolizumab benefit in POPLAR/OAK; prospective B-F1RST did not confirm a first-line predictive effect. bTMB is not broadly adopted.
- <span class="tier tier-cont">contested</span> **PBRM1 LOF as ICI sensitizer in ccRCC has not replicated.** Miao 2018[^pmid:29301960] reported enrichment in responders in two cohorts; subsequent CheckMate-009/010/025 (Braun 2020) and IMmotion analyses did not confirm.
- <span class="tier tier-cont">contested</span> **IPRES transcriptomic signature has underperformed as an independent predictor.** Hugo 2016[^pmid:26997480] nominated an EMT/wound-healing / angiogenesis program in innately resistant melanoma. Validation has been mixed — IPRES overlaps heavily with TGF-β and stromal signatures and adds little above CD8, PD-L1, TMB, and pan-fibroblast measures.
- <span class="tier tier-cont">contested</span> **dMMR is not a universal ICI predictor even in 1L mCRC.** KEYNOTE-177[^pmid:33264544] PFS was biphasic — pembrolizumab underperformed chemotherapy in the first ~6 months (~29% primary progression), and the final OS analysis did not reach statistical significance (HR ~0.74, crossover confounded).
- <span class="tier tier-cont">contested</span> **WNT/β-catenin activation as clinical exclusion driver is weaker than Spranger 2015[^pmid:25970248] mouse biology suggested.** Subsequent clinical cohorts show context-dependent correlations; WNT inhibition + ICI limited by toxicity.
- <span class="tier tier-cont">contested</span> **The specific "shared neoantigen tetrapeptide signature" from Snyder 2014** did not replicate in larger cohorts; the TMB association survives but the signature itself is widely considered a small-sample artifact.

## Suspected but unconfirmed (mechanistically coherent, not yet clinically validated)

- <span class="tier tier-susp">suspected</span> **PD-1 partially *protects* clonally expanding T cells from restimulation-induced cell death**[^pmid:41748562]. In vitro human primary T cells only. If replicated in vivo, would complicate the "release the brakes" framing and explain some non-durability of response.
- <span class="tier tier-susp">suspected</span> **AARS1-mediated PD-L1 K280 lactylation stabilizes PD-L1 against HUWE1 ubiquitination**[^pmid:41864972]. Counterintuitively, exogenous lactate *enhances* anti-PD-L1 efficacy preclinically — this paradox must be reconciled before clinical translation.
- <span class="tier tier-susp">suspected</span> **HILPDA-driven lipogenesis palmitoylates PD-L1 at Cys272**[^pmid:41876831]. Fenretinide (TRIM21 engager) degrades HILPDA and restores anti-PD-1 efficacy in breast cancer models. Single tumor type; preclinical only; but fenretinide has existing clinical exposure.
- <span class="tier tier-susp">suspected</span> **deltaHED (germline + somatic HLA-I evolutionary divergence) predicts worse PD-1 outcomes despite higher TMB/neoantigen load** across three cohorts[^pmid:41601354]. Inverts a naïve HED prediction; needs prospective single-agent PD-1 validation.
- <span class="tier tier-susp">suspected</span> **Hypoalbuminemia causally drives ICI resistance via macrophage arginine biosynthesis impairment** (LLC mice)[^pmid:41940988]. Would recast a routine prognostic lab as a reversible driver; dietary arginine rescue would need clinical study.
- <span class="tier tier-susp">suspected</span> **Hyperprogression on anti-PD-1** (Champiat 2017, Kato 2017 class of reports) remains contested; definitions vary and natural-history confounding is substantial. Not listed as established.

## New directions worth watching (emerging this period)

- <span class="tier tier-emerg">emerging</span> **ATOMIC phase 3 (NEJM 2026): adjuvant atezolizumab + mFOLFOX6 in stage III dMMR colon cancer, HR 0.50**[^pmid:41880612]. 3-year DFS 86.3% vs 76.2%. Extends ICI benefit into adjuvant dMMR. OS not yet mature. A new large population will now experience prolonged adjuvant ICI exposure, creating a fresh substrate for late-resistance biology.
- <span class="tier tier-emerg">emerging</span> **KLRG1 nominated as a novel inhibitory checkpoint** in anti-PD-1-resistant melanoma[^pmid:41956544]; novel anti-human KLRG1 mAb reduces tumor progression in humanized KI mice via combined CD8, NK, and γδ-T effects. Distinct from PD-1/CTLA-4/LAG-3/TIM-3.
- <span class="tier tier-emerg">emerging</span> **Anti-TIM-3 (TQB2618) + anti-PD-1 penpulimab achieves 52% ORR in PD-1-pretreated classical Hodgkin lymphoma** (n=21, phase Ib)[^pmid:41963080]. Salvage signal in a setting where re-engaging checkpoint biology was not expected to help.
- <span class="tier tier-emerg">emerging</span> **TROP2-claudin-7 tight junctions functionally exclude T cells from TNBC**[^pmid:41932810] — reframes TROP2 from ADC target to barrier-mechanism target; mechanistic rationale for TROP2 ADC + anti-PD-1 combinations beyond cytotoxic payload delivery.
- <span class="tier tier-emerg">emerging</span> **PKMYT1 inhibition (clinical-grade RP-6306) activates cGAS-STING in castration-resistant prostate cancer**[^pmid:41617394]. Converts cold CRPC to anti-PD-L1-responsive in preclinical models; prostate cancer has been stubbornly ICI-refractory.
- <span class="tier tier-emerg">emerging</span> **IFN-γ → IRF1 → AGPAT3 axis sensitizes tumors to ferroptosis**[^pmid:41807033]. Extends IFN-γ consequences beyond antigen presentation and apoptosis to a lipidomic vulnerability.
- <span class="tier tier-emerg">emerging</span> **8-gene k-TSP + mucinous composite biomarker identifies a 15% dMMR/MSI-H mCRC subgroup with extreme benefit (HR 0.10) from anti-CTLA-4 addition to anti-PD-1**[^pmid:41950572]. Retrospective (n=25 in positive subgroup); prospective validation called for. If it holds, would resolve a decade-long open question.
- <span class="tier tier-emerg">emerging</span> **LOAd703 (CD40L/4-1BBL oncolytic adenovirus) + atezolizumab in anti-PD-1-refractory melanoma restores ICI-responsive immune signatures** in 24 patients[^pmid:41888981]. Biomarker-level evidence of myeloid-compartment rescue in a refractory population.
- <span class="tier tier-emerg">emerging</span> **Single-cell spatial profiling defines six niches stratifying neoadjuvant cSCC response better than PD-L1 IHC**[^pmid:41617396]. Niche-composition biomarkers may eventually outperform single-marker IHC.
- <span class="tier tier-emerg">emerging</span> **hMENA TGF-β-driven CAF signature validated against OAK phase III**[^pmid:41592891] — a clinically anchored exclusion biomarker despite the TGF-β clinical translation gap on the drug side.

## Practical questions & quick answers

- **Is PD-L1 IHC still clinically useful?** Yes, for 1L NSCLC selection (TPS ≥50% standard for pembro monotherapy). Less useful elsewhere; increasingly replaced by tumor-type-specific algorithms.
- **Does dMMR status guarantee benefit?** No. KEYNOTE-177[^pmid:33264544] PFS was biphasic with ~29% primary progression. dMMR is necessary-but-not-sufficient in mCRC.
- **Does peri-ICI antibiotic exposure matter?** Yes — the antibiotic-harm signal is the most robustly replicated microbiome observation. Specific probiotic or taxonomy-guided interventions are not clinically ready.
- **Can anti-PD-1-refractory patients be rescued?** Emerging positive signals: FMT from a responder donor (~20–30% response in small trials), TIM-3 combination in PD-1-pretreated cHL (52% ORR n=21), LOAd703 oncolytic in melanoma (biomarker-level). None are standard of care yet.
- **Is STK11/KEAP1 testing informative in KRAS-mutant NSCLC?** Yes — it guides prognosis on ICI and supports clinical trial stratification, though no FDA-level companion biomarker yet.
- **Is there a prospective biomarker beyond PD-L1 / TMB / dMMR / STK11 ready for clinical use?** Not yet. HLA LOH, HED/deltaHED, microbiome, IPRES, PBRM1, bTMB — all research-only or have failed prospective validation.
- **What about hyperprogression?** Definitions vary; the literature is contested. Natural history and pseudoprogression confound the phenomenon. Not actionable today.

See per-mechanism deep dives in the navigation. The [papers appendix](papers.md) lists every paper ingested (N>1,000) with links.

---

[^pmid:25428505]: Tumeh 2014 Nature — pre-existing CD8 infiltrate predicts PD-1 response. [Link](https://pubmed.ncbi.nlm.nih.gov/25428505/).
[^pmid:28102259]: Chen & Mellman 2017 Nature — cancer-immunity set-point framework. [Link](https://pubmed.ncbi.nlm.nih.gov/28102259/).
[^pmid:25765070]: Rizvi 2015 Science — TMB in NSCLC under pembrolizumab. [Link](https://pubmed.ncbi.nlm.nih.gov/25765070/).
[^pmid:25409260]: Snyder 2014 NEJM — TMB under anti-CTLA-4 in melanoma. [Link](https://pubmed.ncbi.nlm.nih.gov/25409260/).
[^pmid:28596308]: Le 2017 Science — pembrolizumab in MMR-deficient tumors across 12 histologies. [Link](https://pubmed.ncbi.nlm.nih.gov/28596308/).
[^pmid:33264544]: André 2020 NEJM — KEYNOTE-177 pembrolizumab 1L dMMR mCRC. [Link](https://pubmed.ncbi.nlm.nih.gov/33264544/).
[^pmid:27433843]: Zaretsky 2016 NEJM — JAK1/2 and B2M LOF in acquired anti-PD-1 resistance. [Link](https://pubmed.ncbi.nlm.nih.gov/27433843/).
[^pmid:27903500]: Shin 2017 Cancer Discov — JAK1/2 LOF in primary resistance. [Link](https://pubmed.ncbi.nlm.nih.gov/27903500/).
[^pmid:28723893]: Manguso 2017 Nature — Ptpn2 as ICI sensitizer. [Link](https://pubmed.ncbi.nlm.nih.gov/28723893/).
[^pmid:29773717]: Skoulidis 2018 Cancer Discov — STK11/LKB1 in KRAS-mutant NSCLC ICI. [Link](https://pubmed.ncbi.nlm.nih.gov/29773717/).
[^pmid:26027431]: Larkin 2015 NEJM — CheckMate 067 nivo+ipi vs mono in melanoma. [Link](https://pubmed.ncbi.nlm.nih.gov/26027431/).
[^pmid:27718847]: Reck 2016 NEJM — KEYNOTE-024 pembrolizumab 1L NSCLC PD-L1 ≥50%. [Link](https://pubmed.ncbi.nlm.nih.gov/27718847/).
[^pmid:30635237]: Siddiqui 2019 Immunity — stem-like Tcf1+PD-1+ CD8 subset. [Link](https://pubmed.ncbi.nlm.nih.gov/30635237/).
[^pmid:30388456]: Sade-Feldman 2018 Cell — CD8 T cell states and melanoma ICI response. [Link](https://pubmed.ncbi.nlm.nih.gov/30388456/).
[^pmid:31207603]: Alfei 2019 Nature — TOX reinforces exhausted CD8 phenotype. [Link](https://pubmed.ncbi.nlm.nih.gov/31207603/).
[^pmid:29443960]: Mariathasan 2018 Nature — TGF-β excludes T cells in urothelial ICI. [Link](https://pubmed.ncbi.nlm.nih.gov/29443960/).
[^pmid:29443964]: Tauriello 2018 Nature — TGF-β in MSS CRC metastasis GEMM. [Link](https://pubmed.ncbi.nlm.nih.gov/29443964/).
[^pmid:28187290]: Sharma 2017 Cell — Primary/Adaptive/Acquired resistance review. [Link](https://pubmed.ncbi.nlm.nih.gov/28187290/).
[^pmid:29107330]: McGranahan 2017 Cell — allele-specific HLA-I LOH in NSCLC. [Link](https://pubmed.ncbi.nlm.nih.gov/29107330/).
[^pmid:29097493]: Gopalakrishnan 2018 Science — gut microbiome and anti-PD-1 in melanoma. [Link](https://pubmed.ncbi.nlm.nih.gov/29097493/).
[^pmid:29097494]: Routy 2018 Science — antibiotics, Akkermansia, and PD-1 therapy. [Link](https://pubmed.ncbi.nlm.nih.gov/29097494/).
[^pmid:26541606]: Sivan 2015 Science — Bifidobacterium enhances anti-PD-L1 in mice. [Link](https://pubmed.ncbi.nlm.nih.gov/26541606/).
[^pmid:26541610]: Vétizou 2015 Science — microbiota and anti-CTLA-4 in mice. [Link](https://pubmed.ncbi.nlm.nih.gov/26541610/).
[^pmid:33303685]: Baruch 2021 Science — FMT rescue in anti-PD-1-refractory melanoma (phase I). [Link](https://pubmed.ncbi.nlm.nih.gov/33303685/).
[^pmid:33542131]: Davar 2021 Science — FMT + pembrolizumab in anti-PD-1-refractory melanoma (phase II). [Link](https://pubmed.ncbi.nlm.nih.gov/33542131/).
[^pmid:30082870]: Gandara 2018 Nat Med — blood TMB in NSCLC atezolizumab (retrospective). [Link](https://pubmed.ncbi.nlm.nih.gov/30082870/).
[^pmid:29301960]: Miao 2018 Science — PBRM1 and anti-PD-1 response in ccRCC. [Link](https://pubmed.ncbi.nlm.nih.gov/29301960/).
[^pmid:26997480]: Hugo 2016 Cell — IPRES signature in anti-PD-1 resistant melanoma. [Link](https://pubmed.ncbi.nlm.nih.gov/26997480/).
[^pmid:25970248]: Spranger 2015 Nature — WNT/β-catenin and T-cell exclusion. [Link](https://pubmed.ncbi.nlm.nih.gov/25970248/).
[^pmid:41748562]: RICD protection by PD-1 on expanding T cells. [Link](https://pubmed.ncbi.nlm.nih.gov/41748562/).
[^pmid:41864972]: AARS1 lactylation of PD-L1 K280. [Link](https://pubmed.ncbi.nlm.nih.gov/41864972/).
[^pmid:41876831]: HILPDA-KLF5-palmitoylation of PD-L1. [Link](https://pubmed.ncbi.nlm.nih.gov/41876831/).
[^pmid:41601354]: deltaHED metric across three ICI cohorts. [Link](https://pubmed.ncbi.nlm.nih.gov/41601354/).
[^pmid:41940988]: Hypoalbuminemia and macrophage arginine in ICI resistance. [Link](https://pubmed.ncbi.nlm.nih.gov/41940988/).
[^pmid:41880612]: ATOMIC phase 3 — adjuvant atezolizumab + FOLFOX in stage III dMMR. [Link](https://pubmed.ncbi.nlm.nih.gov/41880612/).
[^pmid:41956544]: KLRG1 as novel checkpoint. [Link](https://pubmed.ncbi.nlm.nih.gov/41956544/).
[^pmid:41963080]: Anti-TIM-3 + penpulimab in PD-1-pretreated cHL. [Link](https://pubmed.ncbi.nlm.nih.gov/41963080/).
[^pmid:41932810]: TROP2-claudin-7 tight junction barrier in TNBC. [Link](https://pubmed.ncbi.nlm.nih.gov/41932810/).
[^pmid:41617394]: PKMYT1 inhibition activating cGAS-STING in CRPC. [Link](https://pubmed.ncbi.nlm.nih.gov/41617394/).
[^pmid:41807033]: IFN-γ–IRF1–AGPAT3–ferroptosis axis. [Link](https://pubmed.ncbi.nlm.nih.gov/41807033/).
[^pmid:41950572]: 8-gene k-TSP + mucinous biomarker for anti-CTLA-4 addition in dMMR/MSI-H mCRC. [Link](https://pubmed.ncbi.nlm.nih.gov/41950572/).
[^pmid:41888981]: LOAd703 + atezolizumab in anti-PD-1-refractory melanoma. [Link](https://pubmed.ncbi.nlm.nih.gov/41888981/).
[^pmid:41617396]: Spatial niches stratifying neoadjuvant cSCC response. [Link](https://pubmed.ncbi.nlm.nih.gov/41617396/).
[^pmid:41592891]: hMENA CAF signature validated in OAK phase III. [Link](https://pubmed.ncbi.nlm.nih.gov/41592891/).
