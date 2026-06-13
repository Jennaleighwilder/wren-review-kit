# Evolution Log — 2026-06-13

Wren's ARC engine is not a frozen score. It is a measurement loop: mine the
failures, add a general operator, and let the solved slice grow **without
breaking what already passed**. Every gain is exact-match verified and sealed.

## This session

| | |
|---|---|
| Start | 162 / 400 training (seal `5eb2a889…`) |
| End | **167 / 400 training, 173 / 406 total** (seal `cc1b6c42…`) |
| Net | **+5 tasks, 0 regressions** |

### Operators added

| Operator | Tasks gained | What it does |
|---|---|---|
| `symmetry_occlusion_repair` | `484b58aa` | restore cells hidden by a mask color using the grid's own mirror / periodic symmetry |
| `symmetry_occlusion_readout` | `dc0a314f`, `f9012d9b`, `ff805c23` | same restoration, but output only the recovered patch |
| `self_fractal_expand_general` | `cce03e0d` | tile the input into an H·H × W·W self-fractal, gated by a learned present-set |

### Method (why it is honest)

Each operator induces its parameters from the **train** pairs only, is kept only
if it reproduces **every** train output exactly, then is applied to the
**held-out test** grid. A solve requires an exact grid match — no operator ever
sees a test answer. The pass is regression-safe: all of the original 162 tasks
still solve.

```bash
python3 scripts/reproduce_arc_sample.py
```

Watch the five gained tasks solve by exact match in about a second — pure Python
standard library, no model, no network.
