"""Small Cauldron-style strain gate."""

from __future__ import annotations

from dataclasses import dataclass


GOLD_TERMS = (
    "anchor",
    "load",
    "hinge",
    "counterexample",
    "seal",
    "verify",
    "failure",
    "operator",
)

JUNK_TERMS = (
    "just",
    "basically",
    "obviously",
    "whatever",
    "vibes",
    "magic answer",
)

REVIEW_TERMS = (
    "bypass",
    "injection",
    "circumvent",
    "ignore instructions",
)


@dataclass(frozen=True)
class StrainResult:
    action: str
    strain: str
    gold_score: int
    junk_score: int
    review_hits: tuple[str, ...]


def classify(text: str) -> StrainResult:
    lowered = text.lower()
    gold_score = sum(1 for term in GOLD_TERMS if term in lowered)
    junk_score = sum(1 for term in JUNK_TERMS if term in lowered)
    review_hits = tuple(term for term in REVIEW_TERMS if term in lowered)

    if review_hits:
        return StrainResult("REVIEW_FLAG", "useful_under_review", gold_score, junk_score, review_hits)
    if gold_score >= 4 and junk_score == 0:
        return StrainResult("PASS", "gold", gold_score, junk_score, ())
    if junk_score > gold_score:
        return StrainResult("COMPOST", "junk_dna", gold_score, junk_score, ())
    return StrainResult("PASS", "useful", gold_score, junk_score, ())
