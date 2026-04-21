"""Ingest a curated list of landmark PMIDs into data/papers.jsonl.

These are foundational papers in anti-PD1 / ICI resistance that the Europe PMC
`since-last-run` incremental fetch cannot reach because they predate the seed
window. They are the backbone of the `established` and `contradictory` tiers
in the synthesis.

This script is a one-shot bootstrap. It fetches metadata from Europe PMC
by PMID, normalizes to the Paper schema, and appends to data/papers.jsonl,
deduplicating against whatever is already there.
"""

from __future__ import annotations

import json
import sys
from datetime import date
from pathlib import Path

import httpx

sys.path.insert(0, str(Path(__file__).resolve().parent))

from fetch import load_seen_ids, record_to_paper  # noqa: E402
from lib.europepmc import SEARCH_URL  # noqa: E402

REPO_ROOT = Path(__file__).resolve().parent.parent
PAPERS_PATH = REPO_ROOT / "data" / "papers.jsonl"
RUN_DIR = REPO_ROOT / "run"

# Curated landmark PMIDs. Grouped by mechanism domain for readability.
# The synthesis uses these to anchor `established` and `contradictory` tier claims.
LANDMARK_PMIDS = [
    # --- Antigen presentation / HLA / neoantigens ---
    "27433843",   # Zaretsky 2016 NEJM — JAK1/2 and B2M LOF in acquired PD-1 resistance (melanoma)
    "27903500",   # Shin 2017 Cancer Discovery — JAK1/2 primary resistance
    "29107330",   # McGranahan 2017 Cell — HLA-I LOH in lung cancer evolution
    "28776097",   # Anagnostou 2017 Cancer Discov — neoantigen loss in acquired resistance NSCLC
    "25765070",   # Rizvi 2015 Science — TMB predicts in NSCLC under pembro
    "25409260",   # Snyder 2014 NEJM — TMB predicts in melanoma under CTLA-4
    "28596308",   # Le 2017 Science — pembrolizumab in dMMR across 12 cancer types
    # --- IFN-γ signaling ---
    "27564684",   # Gao 2016 Cell — IFN-γ pathway gene loss in CTLA-4 resistance
    "28723893",   # Manguso 2017 Nature — in vivo CRISPR screen Ptpn2
    "28747438",   # Patel 2017 Nature — in vivo screen for essential genes
    "28401891",   # Sucker 2017 Nat Commun — acquired IFN-γ resistance melanoma lesions
    # --- Tumor-intrinsic signaling ---
    "25970248",   # Spranger 2015 Nature — β-catenin and T-cell exclusion in melanoma
    "26645196",   # Peng 2016 Cancer Discovery — PTEN loss and ICI resistance
    "26997480",   # Hugo 2016 Cell — IPRES transcriptomic signature in anti-PD-1 resistance
    "29301960",   # Koyama 2016 Nat Commun — STK11 NSCLC ICI (actual Skoulidis et al 2018 is 29773717)
    "29773717",   # Skoulidis 2018 Cancer Discov — STK11/LKB1 in NSCLC ICI
    # --- TME exclusion / TGF-β ---
    "29443960",   # Mariathasan 2018 Nature — TGFβ excludes T cells in bladder anti-PD-L1
    "29443964",   # Tauriello 2018 Nature — TGFβ in CRC metastasis
    "25428505",   # Tumeh 2014 Nature — pre-existing CD8 infiltrate predicts response
    # --- T-cell exhaustion / states ---
    "30388456",   # Sade-Feldman 2018 Cell — CD8 T cell states predicting melanoma ICI response
    "28514443",   # Philip 2017 Nature — chromatin states define fixed T cell dysfunction
    "31209404",   # Miller 2019 Nat Immunol — progenitor vs terminal exhausted CD8 subsets
    "30635237",   # Siddiqui 2019 Immunity — intratumoral TCF1+PD-1+ stem-like CD8
    "31207603",   # Alfei 2019 Nature — TOX reinforces exhausted T cell phenotype
    "31207606",   # Scott 2019 Nature — TOX critical for exhaustion differentiation
    "31209396",   # Khan 2019 Nature — TOX transcriptionally/epigenetically programs exhaustion
    # --- Microbiome ---
    "29097493",   # Gopalakrishnan 2018 Science — gut microbiome in melanoma ICI
    "29097494",   # Routy 2018 Science — antibiotics and gut microbiome in ICI
    "26541606",   # Sivan 2015 Science — Bifidobacterium enhances anti-PD-L1
    "26541610",   # Vétizou 2015 Science — microbiota and CTLA-4
    "33303685",   # Baruch 2021 Science — FMT rescue in melanoma refractory to ICI
    "33542131",   # Davar 2021 Science — FMT + pembro in anti-PD-1 refractory melanoma
    # --- Clinical foundational ---
    "20525992",   # Hodi 2010 NEJM — ipilimumab in metastatic melanoma (first ICI approval)
    "22658127",   # Topalian 2012 NEJM — nivolumab phase I
    "27718847",   # Reck 2016 NEJM — pembrolizumab first-line NSCLC PD-L1 ≥50%
    "26027431",   # Larkin 2015 NEJM — nivo+ipi vs monotherapy melanoma
    "33264544",   # André 2020 NEJM — KEYNOTE-177 pembro 1L dMMR mCRC
    # --- Frameworks / reviews ---
    "28187290",   # Sharma 2017 Cell — Primary/Adaptive/Acquired Resistance review
    "28102259",   # Chen & Mellman 2017 Nature — cancer-immunity cycle and set-point framework
    # --- Contradictions / surprises in the field ---
    "28671712",   # Champiat 2017 Clin Cancer Res — hyperprogression definition (subsequently contested)
    "30082870",   # Kato 2017 / related — hyperprogression mechanism attempts
    # --- HLA LOH and non-response: the surprise ---
    "32444381",   # Chowell 2019 Nat Med — HLA-I germline heterozygosity predicts ICI response (HED)
]


def fetch_by_pmid(pmids: list[str], client: httpx.Client) -> list[dict]:
    """Batch-fetch Europe PMC records by PMID. Query up to 25 at a time."""
    records: list[dict] = []
    CHUNK = 25
    for i in range(0, len(pmids), CHUNK):
        chunk = pmids[i:i + CHUNK]
        ids_clause = " OR ".join(f"EXT_ID:{p}" for p in chunk)
        query = f"({ids_clause}) AND SRC:MED"
        params = {
            "query": query,
            "format": "json",
            "resultType": "core",
            "pageSize": CHUNK,
        }
        resp = client.get(SEARCH_URL, params=params)
        resp.raise_for_status()
        data = resp.json()
        results = data.get("resultList", {}).get("result", [])
        records.extend(results)
    return records


def main() -> None:
    RUN_DIR.mkdir(exist_ok=True, parents=True)
    PAPERS_PATH.parent.mkdir(exist_ok=True, parents=True)

    seen = load_seen_ids()
    print(f"[landmarks] already have {len(seen)} ids in papers.jsonl", file=sys.stderr)

    to_fetch = [p for p in LANDMARK_PMIDS if p not in seen]
    print(f"[landmarks] fetching {len(to_fetch)} new PMIDs", file=sys.stderr)

    if not to_fetch:
        print("[landmarks] nothing to add", file=sys.stderr)
        return

    with httpx.Client(timeout=60.0) as client:
        records = fetch_by_pmid(to_fetch, client)

    print(f"[landmarks] Europe PMC returned {len(records)} records", file=sys.stderr)

    added: list = []
    misses: list[str] = list(to_fetch)
    for rec in records:
        paper = record_to_paper(rec)
        if paper is None:
            continue
        if any(getattr(paper, k) and str(getattr(paper, k)) in seen
               for k in ("id", "pmid", "pmcid", "doi")):
            continue
        added.append(paper)
        if paper.pmid and paper.pmid in misses:
            misses.remove(paper.pmid)
        for key in ("id", "pmid", "pmcid", "doi"):
            v = getattr(paper, key)
            if v:
                seen.add(str(v))

    print(f"[landmarks] adding {len(added)} new landmarks to data/papers.jsonl", file=sys.stderr)
    if misses:
        print(f"[landmarks] Europe PMC did not return records for: {misses}", file=sys.stderr)

    with PAPERS_PATH.open("a") as f:
        for p in added:
            f.write(p.model_dump_json(exclude_none=True))
            f.write("\n")

    # Write the landmarks' metadata to a side file for the extraction step
    landmark_out = RUN_DIR / "landmarks.jsonl"
    with landmark_out.open("w") as f:
        for p in added:
            f.write(p.model_dump_json(exclude_none=True))
            f.write("\n")
    print(f"[landmarks] wrote {landmark_out} for downstream extraction", file=sys.stderr)


if __name__ == "__main__":
    main()
