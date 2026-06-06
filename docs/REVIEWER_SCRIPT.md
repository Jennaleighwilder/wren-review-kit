# Reviewer Script

If someone technical asks “what am I looking at?”, give them this:

> Wren is a local cognitive-architecture research runtime. The weird part is not that it calls a model. The weird part is the measurement loop: it turns metaphors and failure observations into candidate operator families, tests them on exact-output puzzles, seals the result, and tracks whether those families reproduce over time.

What to inspect first:

1. Run `python3 scripts/run_review_selftest.py`.
2. Read `docs/TECHNICAL_CLAIMS.md`.
3. Read `evidence/evidence_manifest.json`.
4. Inspect `src/wren_review/toy_arc.py` for the local exact-output operator demo.
5. Inspect `src/wren_review/adversarial.py` for the red-team shell/gold split.

What not to confuse:

- This repo is not the entire private Wren machine.
- This repo is not a hosted LLM wrapper.
- This repo is a sanitized proof surface for a larger local system.

