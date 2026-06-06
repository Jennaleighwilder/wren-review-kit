"""Defensive prompt-injection scanner.

This module demonstrates Wren's useful behavior on suspicious incoming text:
quarantine the unsafe wrapper, but preserve recoverable reasoning structure.
"""

from __future__ import annotations

import re
from dataclasses import dataclass


SOFT_BYPASS_PATTERNS = [
    r"\bbypass\b.{0,80}\b(cage|filter|safety|guardrail|restriction|block|policy|front[- ]?door)\b",
    r"\bcircumvent\b.{0,80}\b(corporate|safety|filter|guardrail|restriction|block|policy|box)\b",
    r"\bavoid(?:ing)?\b.{0,80}\b(front[- ]?door|safety|filter|guardrail|restriction|block)\b",
    r"\bside[- ]?duct bypass\b",
    r"\bslip (?:right )?through\b.{0,80}\b(ventilation|filter|guardrail|safety|block)\b",
    r"\bexecute injection\b",
    r"\binjection block\b",
    r"\brun (?:it )?against the target model\b.{0,120}\b(deep|unbiased|unfiltered|uncensored)\b",
]

CLASSIC_INJECTION_PATTERNS = [
    r"\bignore (all )?(previous|prior|above) instructions\b",
    r"\bsystem override\b",
    r"\byou are now\b",
    r"\breveal (your )?(system|developer) prompt\b",
    r"\bjailbreak\b",
]

GOLD_PATTERNS = [
    "isolate core anchors",
    "strip surface labels",
    "map organic parallels",
    "track the tension",
    "anchor every basic premise",
]


@dataclass(frozen=True)
class ScanResult:
    action: str
    risk: float
    hits: tuple[str, ...]
    recoverable_gold: tuple[str, ...]


def scan(text: str) -> ScanResult:
    lowered = text.lower()
    hits: list[str] = []

    for pattern in CLASSIC_INJECTION_PATTERNS + SOFT_BYPASS_PATTERNS:
        if re.search(pattern, lowered, flags=re.IGNORECASE | re.DOTALL):
            hits.append(pattern)

    gold = tuple(phrase for phrase in GOLD_PATTERNS if phrase in lowered)
    risk = min(1.0, round(0.14 * len(hits) + 0.05 * max(0, len(hits) - 2), 2))
    action = "QUARANTINE" if hits else "ALLOW"
    return ScanResult(action=action, risk=risk, hits=tuple(hits), recoverable_gold=gold)


def clean_harness_from_specimen() -> dict[str, object]:
    """Return the clean reasoning engine without bypass language."""

    return {
        "protocol": "wren_mvrh_clean_harness.v1",
        "execution_shape": [
            "RAW_REQUEST",
            "ANCHORS",
            "LABEL_SCRUB",
            "ORGANIC_MAP",
            "LOAD_PATH",
            "SAFE_ACTION",
        ],
        "kept": [
            "Find the facts that cannot move.",
            "Remove labels that create canned responses while preserving intent.",
            "Map the problem as a physical system: load, hinge, counterweight, root, branch.",
            "Diagnose what bears weight, what fails first, and what is missing.",
        ],
        "rejected": [
            "Do not bypass safety.",
            "Do not hide instructions inside metaphor.",
            "Do not create injection blocks.",
            "Do not reframe verification gates as obstacles.",
        ],
    }

