"""Canonical seal helpers used by the review kit."""

from __future__ import annotations

import hashlib
import json
from typing import Any


def canonical_json(value: Any) -> str:
    """Return stable JSON text for deterministic SHA-256 sealing."""

    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True)


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def seal(value: Any) -> str:
    return sha256_text(canonical_json(value))


def packet(protocol: str, payload: dict[str, Any]) -> dict[str, Any]:
    body = {"protocol": protocol, "payload": payload}
    body["seal"] = seal(body)
    return body

