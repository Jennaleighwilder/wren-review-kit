# Wren — Review Scorecard

One page. Every number here is local, sealed, and reproducible.

## ARC-AGI (abstract reasoning, exact-output)

| | |
|---|---|
| Training split | **167 / 400** exact match |
| Full black-box suite | **173 / 406** |
| Weak baseline | **0 / 406** |
| Model / API used | **none** |
| Network used | **none** |
| Runtime | **~40 seconds** |
| Seal | `cc1b6c42fc82…` |

Reproduce a sanitized slice yourself in ~1 second:

```bash
python3 scripts/reproduce_arc_sample.py
```

(5 real ARC-AGI tasks, induced from train, verified on held-out test, exact match.)

## Self-improvement (2026-06-13)

| | |
|---|---|
| Before | 162 / 400 |
| After | **167 / 400**  (+5) |
| Regressions | **0** |
| How | 3 general operators added; every gain exact-match verified |

See `docs/EVOLUTION_LOG.md`.

## Federalist Papers (stylometry, external ground truth)

| | |
|---|---|
| Leave-one-out accuracy | **96.9%** |
| Disputed papers | all attributed to **Madison** (matches settled history) |
| Method | Mosteller–Wallace function-word analysis |

## What this is

A local, modular, evidence-sealed cognitive runtime — not a wrapper over a
hosted model. The demonstrated paths call no OpenAI / Claude / Gemini / Copilot
API. See `README.md` and `MANUAL.md` to run it.
