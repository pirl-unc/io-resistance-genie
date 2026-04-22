"""One-time backfill of HumanStudyData on existing human-study extractions.

Walks `data/extractions.jsonl`. For every record whose `model_system` is one
of {patient_cohort, clinical_trial, meta_analysis}, merges in a per-PMID
hand-curated HumanStudyData block pulled from the record's existing
`effect_size` / `key_finding` / `outcome` prose (plus widely-known trial
metadata for fields not explicit in the prose).

Idempotent: running the script again overwrites the same fields with the
same values. Safe to re-run after adjustments to the per-PMID table.

Usage:
    python3 scripts/backfill_human_study.py
    python3 scripts/backfill_human_study.py --check   # exit 1 if a write would change anything
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

HUMAN_MODELS = {"patient_cohort", "clinical_trial", "meta_analysis"}

# Per-PMID structured backfill. Each entry mirrors the fields on
# scripts.lib.schemas.HumanStudyData. `feature` is required (never None);
# other fields may be None and will render as "—" in the evidence tables.
HUMAN_STUDY_DATA: dict[str, dict] = {
    "41601354": {
        "n_patients": 729,
        "n_description": "3 cohorts: 164 NPC (POLARIS-02), 88 melanoma, 477 ESCC (JUPITER-06)",
        "feature": "deltaHED (germline + somatic HLA-I evolutionary divergence)",
        "effect_type": "PFS/OS direction",
        "effect_value": "worse on PD-1 blockade despite higher TMB/neoantigen load",
        "effect_ci_or_p": None,
        "method": "HLA typing + WES (deltaHED metric)",
    },
    "41617396": {
        "n_patients": 27,
        "n_description": "3 cSCC cohorts incl. 2 phase II trials",
        "feature": "six spatial tissue niches (high-APC / B-plasma / inflammatory-keratinocyte vs. proliferative / low-APC-myeloid / fibroblast-EMT)",
        "effect_type": "pathologic response prediction",
        "effect_value": "niche profiling outperformed PD-L1 IHC",
        "effect_ci_or_p": None,
        "method": "single-cell spatial transcriptomics",
    },
    "41950572": {
        "n_patients": 163,
        "n_description": "pooled across 2 independent dMMR/MSI-H mCRC cohorts",
        "feature": "Cluster A + mucinous histology (15% biomarker-positive subgroup)",
        "effect_type": "24-mo PFS / HR (Combo vs Mono)",
        "effect_value": "72.2% vs 13.8%; HR 0.10",
        "effect_ci_or_p": "95% CI 0.02–0.39, p<0.001",
        "method": "8-gene k-TSP classifier + histology",
    },
    "41808828": {
        "n_patients": 102,
        "n_description": "institutional CRC cohort + MSKCC pan-cancer validation",
        "feature": "NOTCH3 mutation or low expression",
        "effect_type": "OS direction",
        "effect_value": "improved on ICB",
        "effect_ci_or_p": None,
        "method": "targeted sequencing + IHC + RNA-seq",
    },
    "41592891": {
        "n_patients": None,
        "n_description": "TCGA NSCLC + SU2C + OAK (NCT02008227)",
        "feature": "hMENA⁺ TGF-β-driven CAF 9-gene signature",
        "effect_type": "prognosis / ICT resistance direction",
        "effect_value": "signature-high → worse prognosis, ICT resistance",
        "effect_ci_or_p": None,
        "method": "9-gene RNA signature",
    },
    "41880612": {
        "n_patients": 712,
        "n_description": "phase 3 ATOMIC (NCT02912559), stage III dMMR colon cancer",
        "feature": "atezolizumab + mFOLFOX6 vs mFOLFOX6 alone",
        "effect_type": "3-yr DFS / HR",
        "effect_value": "86.3% vs 76.2%; HR 0.50",
        "effect_ci_or_p": "95% CI 0.35–0.73, p<0.001",
        "method": "phase 3 RCT",
    },
    "41888981": {
        "n_patients": 24,
        "n_description": "single-arm phase I/II, anti-PD-1-refractory stage IV melanoma",
        "feature": "intratumoral LOAd703 (CD40L/4-1BBL oncolytic adenovirus) + atezolizumab",
        "effect_type": "immune-signature biomarker",
        "effect_value": "increased DC markers, T-cell infiltration, EM CD8⁺; decreased circulating Tregs",
        "effect_ci_or_p": None,
        "method": "multi-parameter flow + TME transcriptomics",
    },
    "41963080": {
        "n_patients": 21,
        "n_description": "phase Ib (NCT05400876), PD-1-pretreated relapsed/refractory cHL",
        "feature": "anti-TIM-3 TQB2618 + anti-PD-1 penpulimab",
        "effect_type": "ORR",
        "effect_value": "52% (1 CR, 10 PR); grade ≥3 TRAE 24%",
        "effect_ci_or_p": None,
        "method": "phase Ib clinical trial",
    },
    "27433843": {
        "n_patients": 4,
        "n_description": "melanoma patients with late relapse on pembrolizumab",
        "feature": "acquired JAK1/JAK2 LOF or B2M truncation",
        "effect_type": "acquired resistance mechanism",
        "effect_value": "3 of 4 relapse tumors harbored a candidate lesion",
        "effect_ci_or_p": None,
        "method": "paired WES + functional IFN-γ / MHC-I assays",
    },
    "27903500": {
        "n_patients": 39,
        "n_description": "23 melanoma + 16 MMR-deficient CRC non-responders",
        "feature": "biallelic JAK1/JAK2 LOF",
        "effect_type": "primary-resistance prevalence",
        "effect_value": "~4% melanoma, ~6% MMR-d CRC non-responders",
        "effect_ci_or_p": None,
        "method": "WES + cell-line IFN-γ / ISG induction assays",
    },
    "29107330": {
        "n_patients": 100,
        "n_description": "TRACERx 100 NSCLC",
        "feature": "allele-specific HLA-I LOH",
        "effect_type": "frequency / selection",
        "effect_value": "~40% HLA-I LOH; subclonal, enriched at metastatic sites",
        "effect_ci_or_p": None,
        "method": "LOHHLA (allele-specific WES)",
    },
    "25765070": {
        "n_patients": None,
        "n_description": "NSCLC discovery + validation cohorts",
        "feature": "nonsynonymous tumor mutational burden",
        "effect_type": "DCB / PFS enrichment",
        "effect_value": "cutoff ~178 nonsynonymous mutations separates DCB from no-benefit",
        "effect_ci_or_p": None,
        "method": "WES",
    },
    "25409260": {
        "n_patients": 64,
        "n_description": "discovery n=25 + validation n=39 melanoma on anti-CTLA-4",
        "feature": "somatic mutational load (and shared-neoantigen tetrapeptide signature)",
        "effect_type": "clinical benefit association",
        "effect_value": "mutational load associated with benefit",
        "effect_ci_or_p": "P=0.01",
        "method": "WES",
    },
    "28596308": {
        "n_patients": 86,
        "n_description": "phase 2 expansion across 12 tumor types, MMR-deficient tumors",
        "feature": "MMR deficiency",
        "effect_type": "ORR",
        "effect_value": "53% (CR 21%)",
        "effect_ci_or_p": None,
        "method": "MMR IHC / MSI testing + pembro phase 2",
    },
    "30082870": {
        "n_patients": None,
        "n_description": "POPLAR (test) + OAK (validation) NSCLC atezolizumab",
        "feature": "blood TMB ≥16 mut/Mb (FoundationACT ctDNA)",
        "effect_type": "PFS HR (atezo vs docetaxel)",
        "effect_value": "HR ~0.65 at bTMB ≥16 in OAK",
        "effect_ci_or_p": None,
        "method": "ctDNA (FoundationACT)",
    },
    "29301960": {
        "n_patients": 98,
        "n_description": "discovery n=35 + validation n=63 ccRCC on anti-PD-1 ± anti-CTLA-4",
        "feature": "PBRM1 LOF",
        "effect_type": "clinical-benefit enrichment",
        "effect_value": "enriched among responders",
        "effect_ci_or_p": "P=0.012 (discovery); P=0.0071 (validation)",
        "method": "WES",
    },
    "26645196": {
        "n_patients": 39,
        "n_description": "small melanoma anti-PD-1 cohort",
        "feature": "tumor PTEN loss",
        "effect_type": "CD8 infiltration / PFS direction",
        "effect_value": "reduced intratumoral CD8, worse PFS",
        "effect_ci_or_p": None,
        "method": "IHC + clinical correlation",
    },
    "26997480": {
        "n_patients": 38,
        "n_description": "pretreatment melanoma biopsies on anti-PD-1",
        "feature": "IPRES transcriptional signature (EMT / ECM / angiogenesis / wound-healing)",
        "effect_type": "response direction",
        "effect_value": "IPRES-high enriched among non-responders",
        "effect_ci_or_p": None,
        "method": "bulk RNA-seq + WES",
    },
    "29773717": {
        "n_patients": None,
        "n_description": "SU2C + CheckMate-057 KRAS-mutant NSCLC ICI cohorts",
        "feature": "STK11/LKB1 co-mutation (KL subgroup)",
        "effect_type": "ORR",
        "effect_value": "KL 7.4% vs KP 35.7% (SU2C); 0% vs 57.1% (CheckMate-057)",
        "effect_ci_or_p": "P<0.001",
        "method": "targeted/WES + clinical correlation",
    },
    "27718847": {
        "n_patients": 305,
        "n_description": "KEYNOTE-024 phase 3, 1L advanced NSCLC, PD-L1 TPS ≥50%, EGFR/ALK-wt",
        "feature": "PD-L1 TPS ≥50% (pembrolizumab vs platinum doublet)",
        "effect_type": "PFS HR",
        "effect_value": "mPFS 10.3 vs 6.0 mo; HR 0.50",
        "effect_ci_or_p": "95% CI 0.37–0.68, p<0.001",
        "method": "PD-L1 IHC 22C3",
    },
    "20525992": {
        "n_patients": 676,
        "n_description": "phase 3, previously-treated HLA-A*0201⁺ metastatic melanoma",
        "feature": "ipilimumab 3 mg/kg (± gp100) vs gp100",
        "effect_type": "OS HR",
        "effect_value": "ipi+gp100 vs gp100 mOS 10.0 vs 6.4 mo (HR 0.68); ipi vs gp100 HR 0.66",
        "effect_ci_or_p": "p<0.001 (ipi+gp100) / p=0.003 (ipi alone)",
        "method": "phase 3 RCT",
    },
    "22658127": {
        "n_patients": 296,
        "n_description": "melanoma 94, NSCLC 76, RCC 33, and others; phase 1 dose-escalation",
        "feature": "nivolumab (BMS-936558) across histologies; PD-L1 IHC predictive",
        "effect_type": "ORR / PD-L1 association",
        "effect_value": "melanoma 28%, NSCLC 18%, RCC 27%; PD-L1⁺ vs PD-L1⁻ ORR 36% vs 0%",
        "effect_ci_or_p": "p=0.006 (PD-L1 association)",
        "method": "phase 1 dose-escalation + PD-L1 IHC",
    },
    "29443960": {
        "n_patients": 298,
        "n_description": "IMvigor210 atezolizumab-treated metastatic urothelial carcinoma",
        "feature": "fibroblast TGF-β response signature (F-TBRS)",
        "effect_type": "response direction",
        "effect_value": "non-responders enriched for F-TBRS and T-cell-excluded phenotype",
        "effect_ci_or_p": None,
        "method": "bulk RNA-seq",
    },
    "25428505": {
        "n_patients": 46,
        "n_description": "metastatic melanoma on pembrolizumab; discovery n=46 + validation n=15",
        "feature": "pre-existing CD8⁺ T cells at the invasive tumor margin",
        "effect_type": "response prediction (AUC)",
        "effect_value": "AUC ~0.9 in discovery cohort",
        "effect_ci_or_p": None,
        "method": "IHC + multiplex IF + TCR-seq",
    },
    "30388456": {
        "n_patients": 48,
        "n_description": "checkpoint-blockade-treated melanoma; 16,291 immune cells sequenced",
        "feature": "TCF7⁺ stem-like vs dysfunctional CD8⁺ T-cell state",
        "effect_type": "response direction",
        "effect_value": "TCF7⁺ CD8 frequency associated with response (validation cohort)",
        "effect_ci_or_p": None,
        "method": "scRNA-seq + IF validation",
    },
    "29097493": {
        "n_patients": 112,
        "n_description": "melanoma on anti-PD-1; shotgun-metagenomics subset n=43 (30 R, 13 NR)",
        "feature": "gut alpha diversity / Faecalibacterium enrichment",
        "effect_type": "response association",
        "effect_value": "higher diversity & Faecalibacterium in responders",
        "effect_ci_or_p": "P<0.01",
        "method": "16S / shotgun metagenomics + responder→GF-mouse FMT",
    },
    "29097494": {
        "n_patients": 249,
        "n_description": "NSCLC, RCC, urothelial on anti-PD-1/PD-L1",
        "feature": "peri-ICI antibiotic exposure / A. muciniphila abundance",
        "effect_type": "OS HR",
        "effect_value": "antibiotics → shorter PFS/OS (NSCLC mOS ~8 vs ~20 mo; HR ~3.5)",
        "effect_ci_or_p": None,
        "method": "clinical-record audit + shotgun metagenomics",
    },
    "33303685": {
        "n_patients": 10,
        "n_description": "phase I FMT in anti-PD-1-refractory metastatic melanoma",
        "feature": "FMT from anti-PD-1-responder donors + anti-PD-1 reinduction",
        "effect_type": "ORR",
        "effect_value": "3/10 (1 CR, 2 PR)",
        "effect_ci_or_p": None,
        "method": "phase I FMT trial",
    },
    "33542131": {
        "n_patients": 15,
        "n_description": "single-arm phase II FMT in anti-PD-1-refractory melanoma",
        "feature": "responder-FMT + pembrolizumab",
        "effect_type": "clinical benefit / ORR",
        "effect_value": "6/15 benefit; ORR ~20%",
        "effect_ci_or_p": None,
        "method": "phase II single-arm trial",
    },
    "26027431": {
        "n_patients": 945,
        "n_description": "CheckMate-067 phase 3, untreated metastatic melanoma",
        "feature": "nivo+ipi vs nivo vs ipi monotherapy",
        "effect_type": "PFS HR (combo vs ipi)",
        "effect_value": "mPFS 11.5 vs 6.9 vs 2.9 mo; HR 0.42 combo vs ipi (HR 0.57 nivo vs ipi)",
        "effect_ci_or_p": None,
        "method": "phase 3 RCT",
    },
    "33264544": {
        "n_patients": 307,
        "n_description": "KEYNOTE-177 phase 3, treatment-naive dMMR/MSI-H mCRC",
        "feature": "1L pembrolizumab vs 5-FU-based chemotherapy",
        "effect_type": "PFS HR",
        "effect_value": "mPFS 16.5 vs 8.2 mo; HR 0.60",
        "effect_ci_or_p": "95% CI 0.45–0.80, p=0.0002",
        "method": "phase 3 RCT",
    },
}


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "--check",
        action="store_true",
        help="exit 1 without writing if any record would be modified",
    )
    args = ap.parse_args()

    src = Path("data/extractions.jsonl")
    lines = src.read_text().splitlines()

    out_lines: list[str] = []
    updated = 0
    unchanged = 0
    missing: list[str] = []

    for line in lines:
        if not line.strip():
            out_lines.append(line)
            continue
        r = json.loads(line)
        pid = r["paper_id"]
        ms = r["model_system"]
        if ms in HUMAN_MODELS:
            hs = HUMAN_STUDY_DATA.get(pid)
            if hs is None:
                missing.append(pid)
                out_lines.append(line)
                continue
            prior = r.get("human_study")
            if prior != hs:
                updated += 1
            else:
                unchanged += 1
            r["human_study"] = hs
        else:
            # Ensure non-human records have the field absent (or null). We
            # leave pre-existing entries untouched rather than mass-nulling,
            # since the schema default is None.
            if "human_study" in r and r["human_study"] is None:
                del r["human_study"]
        out_lines.append(json.dumps(r, ensure_ascii=False))

    new_text = "\n".join(out_lines) + ("\n" if lines and lines[-1] == "" else "\n")
    old_text = src.read_text()

    if missing:
        print(
            f"[backfill] ERROR: {len(missing)} human-study PMID(s) lack a "
            f"HUMAN_STUDY_DATA entry: {missing}",
            file=sys.stderr,
        )
        sys.exit(2)

    if args.check:
        if new_text != old_text:
            print(f"[backfill] --check: would modify extractions.jsonl ({updated} updated)", file=sys.stderr)
            sys.exit(1)
        print("[backfill] --check: no changes needed")
        return

    src.write_text(new_text)
    print(
        f"[backfill] wrote {src}: {updated} records updated, {unchanged} already current, "
        f"{len(HUMAN_STUDY_DATA)} total curated PMIDs"
    )


if __name__ == "__main__":
    main()
