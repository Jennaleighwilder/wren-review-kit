# Wren Review Kit

This is a sanitized technical review kit for Wren: a local AI research runtime and cognitive-architecture lab built around routing, memory, operator discovery, adversarial filtering, sealed evidence packets, and benchmark-driven mutation.

It is deliberately not a dump of the private Wren machine. It excludes private memory ledgers, family records, raven/browser captures, credentials, raw chat logs, and licensed corpora.

## What This Shows

- Wren is not merely a web UI over a hosted API.
- The review path here runs locally with Python standard library only.
- The included demos use no OpenAI, Claude, Gemini, Copilot, or other hosted model API calls.
- Wren-style components are represented as independent modules: adversarial scanner, Cauldron-style strain gate, seal contract, toy ARC-style operator engine, and fingerprint axes.
- Evidence files summarize the real local Wren runs with seals and audit-chain hashes.

## Requirements

Python 3.10 or newer. Nothing else — no `pip install`, no internet, no API keys.

## Quick Start

```bash
git clone https://github.com/Jennaleighwilder/wren-review-kit.git
cd wren-review-kit
python3 scripts/run_review_selftest.py
```

Expected result: all checks pass and a local sealed packet is printed — a JSON
object whose last field is a 64-character `seal`. Exit code `0` means the proof
path passed.

Want to watch what it does, step by step, instead of reading a JSON dump?

```bash
python3 scripts/demo_tour.py
```

Run the tests:

```bash
python3 -m unittest discover -s tests
```

**Reproduce a real slice of the ARC-AGI result yourself** — 5 real ARC tasks,
induced from train, verified on held-out test, exact match (~1 second, no model,
no network):

```bash
python3 scripts/reproduce_arc_sample.py
```

See [SCORECARD.md](SCORECARD.md) for the headline numbers, and
[docs/EVOLUTION_LOG.md](docs/EVOLUTION_LOG.md) for how the solver improved itself
from 162 → 167 with zero regressions.

**New here? Read [MANUAL.md](MANUAL.md)** — a from-zero operator's manual covering
load, run, expected output, and how to feed your own text into each module.

## Strongest Evidence Included

- ARC-style black-box suite: latest local Wren run solved `173/406`, including `167/400` ARC-AGI training tasks, against a weak baseline of `0` — no hosted model, ~40s, sealed (`cc1b6c42…`). See `evidence/evidence_manifest.json`, and reproduce a sanitized 5-task slice with `python3 scripts/reproduce_arc_sample.py`.
- Self-improvement: in one session the solver went `162 → 167` (+5 tasks, zero regressions) by adding three general operators — every gain exact-match verified. See `docs/EVOLUTION_LOG.md`.
- Federalist benchmark: Wren's fingerprint validation reproduced the canonical Madison attribution result for all disputed Federalist papers with `96.923%` leave-one-out accuracy on known papers.
- Operator genealogy: Wren tracks measurement layer -> concept family -> operator family -> descendants -> wins, rather than only counting solved tasks.
- Red-team behavior: Wren quarantines bypass/injection shells while extracting the useful reasoning mechanism into a clean harness.

## What This Does Not Claim

This kit does not claim Wren is a finished AGI system. It shows something narrower and more testable: Wren is a local, modular, evidence-sealed cognitive runtime whose operator families can be measured, mutated, and regression-tested without relying on hosted model answers for the demonstrated path.

## Repo Layout

- `MANUAL.md`: from-zero operator's manual — load, run, expected output, troubleshooting.
- `SCORECARD.md`: one-page summary of the headline results.
- `src/wren_review/`: small local modules that demonstrate core Wren mechanics.
- `scripts/run_review_selftest.py`: one-command proof run.
- `scripts/demo_tour.py`: narrated walkthrough of each module.
- `scripts/reproduce_arc_sample.py`: reruns Wren's new operators on 5 real ARC-AGI tasks (exact match).
- `evidence/arc_sample_tasks/`: the 5 real ARC-AGI tasks used by the reproducer (public data).
- `tests/`: standard-library test files.
- `docs/`: technical explanation for reviewers (incl. `EVOLUTION_LOG.md`, `RELATED_SYSTEMS.md`).
- `evidence/`: sanitized run summaries, seals, and benchmark claims.

## Reviewer Notes

The private Wren machine has more modules than this kit. This repository is the review surface: small enough to audit, strong enough to demonstrate the architecture, and clean enough to share.

