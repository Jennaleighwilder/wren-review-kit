# Related Systems (independently verifiable)

Wren is one of several systems from The Forgotten Code Research Institute. Two
that a reviewer can check right now, without any access to a private machine:

## GAIA — severe-weather detection (live)

A full-stack atmospheric-intelligence system (~77K Python LOC): Flask / gunicorn
backend, a Ferry County FastAPI + Postgres sub-app, NASA FIRMS integration, and
14 surface engines + 8 sirens (GOES / NEXRAD / GLM / terrain / soil).

- **Live dashboard:** https://jennaleighwilder.github.io/gaia/docs/index.html
- **Live data API** (returns real-time atmospheric state as JSON):
  https://web-production-ce417.up.railway.app/api/bundle
- **Validated baseline:** 386 / 460 = **83.9% detection** across 460 East TN
  severe-weather events (1996–2025), **18.5%** false-alarm rate,
  **176-minute** average lead time. Per-hazard and national multi-state
  breakdowns documented in the GAIA repository.

## Impossibility Gate — deterministic safety gate

A non-downgradable ALLOW / DENY / RESTRICT / REVIEW gate for autonomous systems:
**88 passing tests, zero dependencies**, fully deterministic and auditable. No
black box — every decision is traceable to an explicit rule.
