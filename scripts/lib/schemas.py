"""Pydantic models for the living literature synthesis pipeline.

These are the shared ground-truth schemas used by every stage (fetch, triage,
extract, synthesize) and are the contract the Option-3 API pipeline would
honor unchanged.
"""

from __future__ import annotations

from datetime import date, datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class Source(str, Enum):
    PUBMED = "pubmed"
    BIORXIV = "biorxiv"
    MEDRXIV = "medrxiv"
    OTHER_PREPRINT = "other_preprint"


class MechanismClass(str, Enum):
    ANTIGEN_PRESENTATION = "antigen_presentation"
    IFN_GAMMA_SIGNALING = "ifn_gamma_signaling"
    TME_EXCLUSION = "tme_exclusion"
    TUMOR_INTRINSIC_SIGNALING = "tumor_intrinsic_signaling"
    T_CELL_EXHAUSTION = "t_cell_exhaustion"
    METABOLIC = "metabolic"
    MICROBIOME = "microbiome"
    CLINICAL_INTERVENTION = "clinical_intervention"
    OTHER = "other"


class ModelSystem(str, Enum):
    CELL_LINE = "cell_line"
    MOUSE = "mouse"
    PATIENT_COHORT = "patient_cohort"
    CLINICAL_TRIAL = "clinical_trial"
    META_ANALYSIS = "meta_analysis"
    REVIEW = "review"


class ConfidenceLevel(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


class FindingCategory(str, Enum):
    CONFIRMS = "confirms"
    REFINES = "refines"
    CHALLENGES = "challenges"
    NOVEL = "novel"


class EvidenceTier(str, Enum):
    """How settled a claim is across the field as a whole.

    Distinct from per-paper `ConfidenceLevel`, which rates a single study's
    internal evidence. A single high-confidence paper does not make a claim
    `established` — established requires durable, multi-group replication.
    """
    ESTABLISHED = "established"          # durable consensus; replicated across groups; often clinically validated
    SUSPECTED = "suspected"              # mechanistically appealing; limited or preclinical-only support
    CONTRADICTORY = "contradictory"      # field has genuinely conflicting findings; prior consensus weakened
    EMERGING = "emerging"                # recent finding, plausible, not yet settled


class Paper(BaseModel):
    """Canonical record for a single paper. Append-only to data/papers.jsonl."""

    id: str
    pmid: Optional[str] = None
    pmcid: Optional[str] = None
    doi: Optional[str] = None
    title: str
    authors: list[str] = Field(default_factory=list)
    journal: Optional[str] = None
    pub_date: Optional[date] = None
    abstract: Optional[str] = None
    source: Source
    url: Optional[str] = None
    is_open_access: bool = False
    ingest_date: date


class Confidence(BaseModel):
    level: ConfidenceLevel
    reasoning: str


class PaperExtraction(BaseModel):
    """Structured extraction from a single kept paper. Append-only to data/extractions.jsonl."""

    paper_id: str
    mechanism_class: MechanismClass
    model_system: ModelSystem
    key_finding: str
    intervention: Optional[str] = None
    outcome: Optional[str] = None
    effect_size: Optional[str] = None
    confidence: Confidence
    caveats: list[str] = Field(default_factory=list)
    surprising_why: Optional[str] = None
    extraction_date: date


class TriageDecision(BaseModel):
    """Per-paper triage output. Written to run/triage.jsonl each run."""

    paper_id: str
    keep: bool
    relevance: int = Field(ge=0, le=5)
    novelty_guess: int = Field(ge=0, le=5)
    categories: list[MechanismClass] = Field(default_factory=list)
    reason: str


class ClaimInState(BaseModel):
    text: str
    mechanism_class: MechanismClass
    confidence: ConfidenceLevel
    evidence_tier: EvidenceTier = EvidenceTier.EMERGING
    supporting_paper_ids: list[str]


class KnowledgeState(BaseModel):
    """Compressed representation of the current synthesis. data/knowledge_state.json."""

    last_run: datetime
    synthesis_summary: str
    top_claims: list[ClaimInState] = Field(default_factory=list)
    mechanism_summaries: dict[str, str] = Field(default_factory=dict)
    version: int = 1
