"""Small cross-domain fingerprint axis demo."""

from __future__ import annotations

import re
from dataclasses import dataclass


@dataclass(frozen=True)
class Fingerprint:
    rhythm: float
    spacing: float
    parenthetical_aside: float
    embodied_density: float
    entropy_proxy: float
    hinge_density: float
    compression_density: float


BODY_WORDS = {"hand", "hands", "eye", "eyes", "mouth", "bone", "skin", "breath", "body", "throat"}
HINGE_WORDS = {"but", "however", "unless", "counterexample", "hinge", "because", "therefore", "if"}


def extract(text: str) -> Fingerprint:
    words = re.findall(r"[A-Za-z']+", text.lower())
    if not words:
        return Fingerprint(0, 0, 0, 0, 0, 0, 0)

    sentences = max(1, len(re.findall(r"[.!?]", text)))
    unique = len(set(words))
    line_count = max(1, text.count("\n") + 1)
    rhythm = round(len(words) / sentences, 4)
    spacing = round(line_count / max(1, len(text)), 6)
    parenthetical_aside = round((text.count("(") + text.count(")") + text.count(" - ")) / len(words), 6)
    embodied_density = round(sum(1 for word in words if word in BODY_WORDS) / len(words), 6)
    entropy_proxy = round(unique / len(words), 6)
    hinge_density = round(sum(1 for word in words if word in HINGE_WORDS) / len(words), 6)
    compression_density = round(len(words) / max(1, len(text)), 6)
    return Fingerprint(rhythm, spacing, parenthetical_aside, embodied_density, entropy_proxy, hinge_density, compression_density)

