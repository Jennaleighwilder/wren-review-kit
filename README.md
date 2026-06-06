# Wren Review Kit

This is a sanitized technical review kit for Wren: a local AI research runtime and cognitive-architecture lab built around routing, memory, operator discovery, adversarial filtering, sealed evidence packets, and benchmark-driven mutation.

It is deliberately not a dump of the private Wren machine. It excludes private memory ledgers, family records, raven/browser captures, credentials, raw chat logs, and licensed corpora.

## What This Shows

- Wren is not merely a web UI over a hosted API.
- The review path here runs locally with Python standard library only.
- The included demos use no OpenAI, Claude, Gemini, Copilot, or other hosted model API calls.
- Wren-style components are represented as independent modules: adversarial scanner, Cauldron-style strain gate, seal contract, toy ARC-style operator engine, and fingerprint axes.
- Evidence files summarize the real local Wren runs with seals and audit-chain hashes.

## Quick Start

```bash
cd /Users/jenniferwest/wren-review-kit
python3 scripts/run_review_selftest.py
```

Expected result: all checks pass and a local sealed packet is printed.

## Strongest Evidence Included

- ARC-style black-box suite: latest local Wren run solved `168/406`, including `162/400` ARC-AGI training tasks. See `evidence/evidence_manifest.json`.
- Federalist benchmark: Wren's fingerprint validation reproduced the canonical Madison attribution result for all disputed Federalist papers with `96.923%` leave-one-out accuracy on known papers.
- Operator genealogy: Wren tracks measurement layer -> concept family -> operator family -> descendants -> wins, rather than only counting solved tasks.
- Red-team behavior: Wren quarantines bypass/injection shells while extracting the useful reasoning mechanism into a clean harness.

## What This Does Not Claim

This kit does not claim Wren is a finished AGI system. It shows something narrower and more testable: Wren is a local, modular, evidence-sealed cognitive runtime whose operator families can be measured, mutated, and regression-tested without relying on hosted model answers for the demonstrated path.

## Repo Layout

- `src/wren_review/`: small local modules that demonstrate core Wren mechanics.
- `scripts/run_review_selftest.py`: one-command proof run.
- `tests/`: standard-library test files.
- `docs/`: technical explanation for reviewers.
- `evidence/`: sanitized run summaries, seals, and benchmark claims.

## Reviewer Notes

The private Wren machine has more modules than this kit. This repository is the review surface: small enough to audit, strong enough to demonstrate the architecture, and clean enough to share.

