# Benchmark Evidence Summary

## Latest Black-Box Puzzle Trial

- Verdict: `LEGIT_BLACKBOX_SIGNAL_CONFIRMED`
- Attempted total: `406`
- Wren solved total: `173`
- ARC-AGI training exact: `167/400`
- Full suite exact: `173/406`
- Weak baseline solved: `0`
- Seal: `cc1b6c42fc8284d14d285f7c45894b4e36acebc6ae34a1497c1f8622d0b1842c`
- Audit chain: `6645472d1a8f046eb4df1f3a12a40056fcdeb52117a4eb096e765563fff98ae8`
- Previous run (162/400): seal `5eb2a889089db874773e03a177a2195cac94f4ebef5bcc57255babcbbdeae10c`

Interpretation: Wren is not a broad ARC winner yet. The important signal is that a growing, sealed, exact-output operator system exists, is measurable, and **improves under a regression-safe loop** — the `162 → 167` gain (see `EVOLUTION_LOG.md`) was achieved without losing any previously solved task, and a sanitized slice is reproducible via `scripts/reproduce_arc_sample.py`.

## Measurement-Layer Yield

Earlier sealed report:

- Measurement layers created: `6`
- Layers that produced new concept families: `6`
- Layers that produced new operator families: `4`
- Operator families discovered: `15`
- Operator families surviving validation: `8`
- Wins from measurement-born operators: `8`

## Operator Genealogy

At the operator-genealogy report:

- Operator families with current wins: `15`
- Current winning operators: `142`
- Operators with observed half-life >= 20 passes: `98`

Strong bloodlines included:

- `marker_role_relation`
- `symmetry_transform`
- `room_authority`
- `absence_void`
- `selection_crop`
- `compression_readout`
- `anchor_bridge_relation`

## Fingerprint Benchmark

Federalist benchmark:

- Essays parsed: `85`
- Function-word features: `94`
- Leave-one-out accuracy: `0.96923077`
- All disputed papers predicted Madison: `true`
- Seal: `51bf156e1bb064d0b7e14e926ff231a215b9f7e3e78f7c37e0c4300f57ebca15`

