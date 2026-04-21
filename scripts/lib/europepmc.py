"""Minimal Europe PMC HTTP client.

Europe PMC combines PubMed + bioRxiv/medRxiv behind one search API, which is
why we use it instead of hitting PubMed E-utilities and bioRxiv separately.
"""

from __future__ import annotations

from datetime import date
from typing import Iterator, Optional

import httpx

SEARCH_URL = "https://www.ebi.ac.uk/europepmc/webservices/rest/search"
FULLTEXT_URL_TEMPLATE = (
    "https://www.ebi.ac.uk/europepmc/webservices/rest/{source}/{id}/fullTextXML"
)

ICI_TERMS = (
    '("PD-1" OR "PD-L1" OR "CTLA-4" OR "LAG-3" OR "TIGIT" OR "TIM-3" '
    'OR "anti-PD-1" OR "anti-PD-L1" OR "anti-CTLA-4" '
    'OR pembrolizumab OR nivolumab OR cemiplimab OR dostarlimab '
    'OR atezolizumab OR durvalumab OR avelumab '
    'OR ipilimumab OR tremelimumab OR relatlimab '
    'OR "checkpoint blockade" OR "immune checkpoint inhibitor")'
)

RESISTANCE_TERMS = (
    '(resistance OR refractory OR "immune escape" '
    'OR "primary resistance" OR "acquired resistance" '
    'OR hyperprogression OR "non-responder" OR "non-response")'
)

MECHANISM_TERMS = (
    '(mechanism OR pathway OR signaling OR mutation OR biomarker '
    'OR "clinical trial" OR "case series" OR "tumor microenvironment" '
    'OR transcriptomic OR genomic OR proteomic)'
)

CANCER_TERMS = (
    '(cancer OR tumor OR tumour OR carcinoma OR melanoma OR lymphoma '
    'OR sarcoma OR leukemia OR glioma OR neoplasm)'
)


def build_query(since: date) -> str:
    """Assemble the full boolean query with a date lower bound."""
    date_filter = f"(FIRST_PDATE:[{since.isoformat()} TO *])"
    return (
        f"{ICI_TERMS} AND {RESISTANCE_TERMS} AND {MECHANISM_TERMS} "
        f"AND {CANCER_TERMS} AND {date_filter}"
    )


def search(
    query: str,
    page_size: int = 200,
    client: Optional[httpx.Client] = None,
) -> Iterator[dict]:
    """Yield raw Europe PMC result records, paginating with cursorMark."""
    own_client = client is None
    if client is None:
        client = httpx.Client(timeout=30.0)
    try:
        cursor = "*"
        while True:
            params = {
                "query": query,
                "format": "json",
                "resultType": "core",
                "pageSize": page_size,
                "cursorMark": cursor,
            }
            resp = client.get(SEARCH_URL, params=params)
            resp.raise_for_status()
            data = resp.json()
            results = data.get("resultList", {}).get("result", [])
            if not results:
                break
            for rec in results:
                yield rec
            next_cursor = data.get("nextCursorMark")
            if not next_cursor or next_cursor == cursor:
                break
            cursor = next_cursor
    finally:
        if own_client:
            client.close()


def fetch_fulltext_xml(
    source: str,
    paper_id: str,
    client: Optional[httpx.Client] = None,
) -> Optional[str]:
    """Fetch open-access full-text XML. Returns None if not available (404)."""
    own_client = client is None
    if client is None:
        client = httpx.Client(timeout=60.0)
    try:
        url = FULLTEXT_URL_TEMPLATE.format(source=source, id=paper_id)
        resp = client.get(url)
        if resp.status_code == 404:
            return None
        resp.raise_for_status()
        return resp.text
    finally:
        if own_client:
            client.close()
