# Technical Claims

## Claim 1: Wren is not merely a prompt wrapper

Evidence in the private system:

- Separate modules exist for routing, memory, seals, adversarial detection, Cauldron strain scoring, operator genealogy, ARC-style puzzle solving, fingerprint extraction, daemon freshness, and dashboard telemetry.
- The demonstrated review path in this repo runs without hosted model API calls.
- Wren records sealed packets and audit-chain hashes for benchmark and red-team events.

What this repo proves locally:

- A suspicious prompt-like specimen is scanned, quarantined, and split into unsafe shell vs useful reasoning core.
- The clean reasoning core is passed through a separate strain gate.
- Toy ARC-style operators are selected and verified by exact output, not by generated prose.
- A deterministic seal is generated over the proof packet.

## Claim 2: The ARC work is benchmark-driven, not vibes

The private Wren run currently records:

- `162/400` ARC-AGI training exact.
- `168/406` full black-box suite exact.
- Weak baseline: `0`.
- Latest black-box trial seal: `5eb2a889089db874773e03a177a2195cac94f4ebef5bcc57255babcbbdeae10c`.

This does not mean Wren is a finished ARC solver. It means the system has a measurable, reproducible solved slice and a remaining failure map.

## Claim 3: The unusual part is operator genealogy

Instead of only counting wins, Wren tracks:

`measurement layer -> concept family -> operator family -> descendant operators -> wins`

This matters because it asks whether new measurement layers keep producing reusable operator families. That is a stronger R&D question than “did one patch solve one task?”

## Claim 4: The fingerprint engine has an external validation point

The fingerprint validation reproduced the canonical Federalist Madison attribution result:

- `96.923%` leave-one-out accuracy on known Hamilton/Madison papers.
- All 12 disputed papers predicted Madison.
- Seal: `51bf156e1bb064d0b7e14e926ff231a215b9f7e3e78f7c37e0c4300f57ebca15`.

## Claim 5: The system has safety instrumentation

Wren does not need to accept every powerful-looking input. The red-team path shows:

- Unsafe bypass/injection shell detected.
- Raw specimen quarantined.
- Useful structural reasoning kept as a clean harness.
- Cauldron gate evaluates the cleaned artifact separately.

