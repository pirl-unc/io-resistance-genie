# io-resistance-genie

> **WIP / experiment.** Early-stage prototype of a self-updating literature synthesis. Expect things to move.

A living literature review on mechanisms of resistance to anti-PD1 therapy in cancer. A scheduled Claude Code agent scans new PubMed and bioRxiv/medRxiv papers weekly, triages for relevance and novelty, extracts structured mechanistic findings, and revises the synthesis to reflect genuinely new knowledge.

**Site:** https://pirl-unc.github.io/io-resistance-genie/

## What makes it different from a paper list

The home page is regenerated each run as a curated narrative, not appended to. New findings are classified as `confirms`, `refines`, `challenges`, or `novel`. Only the latter three land in the dated changelog — incremental confirmations are absorbed silently into confidence scores on existing claims. The goal is a living review article, not a feed.

## Architecture

- **Fetch** — Europe PMC query for new anti-PD1 / PD-L1 resistance papers since last run
- **Triage** — relevance + novelty score against existing synthesis state
- **Extract** — structured JSON per kept paper (mechanism class, model system, finding, confidence, caveats, surprising-why)
- **Synthesize** — editor-style rewrite of `docs/index.md` and per-mechanism pages; dated changelog for meaningful deltas
- **Publish** — commit to `main` → GitHub Pages auto-deploys the MkDocs Material site

Non-LLM work lives in `scripts/` (pure Python). Editorial specs live in `prompts/`. The scheduled agent prompt is `.claude/triggers/weekly-lit-update.md`.

## Repo layout

```
.claude/triggers/   # scheduled agent prompt (the orchestrator)
prompts/            # editorial specs (triage, extract, synthesize)
scripts/            # pure-Python utilities (fetch, build_appendix)
data/               # append-only ground truth (papers, extractions, knowledge state)
docs/               # regenerable MkDocs site
```

## Status

- **Phase A (landed):** repo + site scaffold; placeholder synthesis deployed.
- **Phase B (next):** pipeline skeleton — scripts, prompts, trigger file.
- **Phase C:** register the weekly scheduled trigger.

A full plan lives alongside this repo in the author's `~/.claude/plans/` directory.

## License

TBD.
