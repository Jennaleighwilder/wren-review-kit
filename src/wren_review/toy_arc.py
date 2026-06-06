"""Tiny ARC-style operator demo.

This is not the private Wren ARC solver. It is a small, auditable demo of the
same engineering pattern: detect a structural family, select an operator, and
verify exact output locally.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable

Grid = tuple[tuple[int, ...], ...]


@dataclass(frozen=True)
class ToyTask:
    task_id: str
    train_input: Grid
    expected: Grid
    family: str


def nested_symmetric_stamp_closure(grid: Grid) -> Grid:
    """Close a hollow same-color square by mirrored edge tension."""

    h, w = len(grid), len(grid[0])
    out = [list(row) for row in grid]
    colors = sorted({cell for row in grid for cell in row if cell != 0})
    for color in colors:
        coords = [(r, c) for r, row in enumerate(grid) for c, cell in enumerate(row) if cell == color]
        if not coords:
            continue
        rs = [r for r, _ in coords]
        cs = [c for _, c in coords]
        r0, r1 = min(rs), max(rs)
        c0, c1 = min(cs), max(cs)
        if r1 - r0 == c1 - c0 and r1 > r0:
            for c in range(c0, c1 + 1):
                out[r0][c] = color
                out[r1][c] = color
            for r in range(r0, r1 + 1):
                out[r][c0] = color
                out[r][c1] = color
    return tuple(tuple(row) for row in out)


def clean_room_selector(grid: Grid) -> Grid:
    """Choose the intruder-free room split by a separator wall."""

    h, w = len(grid), len(grid[0])
    full_cols = [c for c in range(w) if all(grid[r][c] == 5 for r in range(h))]
    if not full_cols:
        return grid
    wall = full_cols[0]
    left = tuple(tuple(row[:wall]) for row in grid)
    right = tuple(tuple(row[wall + 1 :]) for row in grid)
    left_noise = sum(cell not in (0, 1) for row in left for cell in row)
    right_noise = sum(cell not in (0, 1) for row in right for cell in row)
    return left if left_noise <= right_noise else right


def compression_readout(grid: Grid) -> Grid:
    """Compress signal by discarding zero/noise border and keeping the core."""

    coords = [(r, c) for r, row in enumerate(grid) for c, cell in enumerate(row) if cell not in (0, 9)]
    if not coords:
        return ((0,),)
    rs = [r for r, _ in coords]
    cs = [c for _, c in coords]
    return tuple(tuple(grid[r][c] for c in range(min(cs), max(cs) + 1)) for r in range(min(rs), max(rs) + 1))


OPERATORS: dict[str, Callable[[Grid], Grid]] = {
    "nested_symmetric_stamp_closure": nested_symmetric_stamp_closure,
    "clean_room_selector": clean_room_selector,
    "compression_readout": compression_readout,
}


TOY_TASKS = [
    ToyTask(
        "toy_nested_stamp",
        ((0, 0, 0, 0, 0), (0, 2, 2, 2, 0), (0, 2, 0, 2, 0), (0, 2, 0, 0, 0), (0, 0, 0, 0, 0)),
        ((0, 0, 0, 0, 0), (0, 2, 2, 2, 0), (0, 2, 0, 2, 0), (0, 2, 2, 2, 0), (0, 0, 0, 0, 0)),
        "closure repair / mirrored stamp body-map",
    ),
    ToyTask(
        "toy_separator_room",
        ((1, 0, 5, 1, 7), (1, 0, 5, 0, 0), (0, 1, 5, 7, 0)),
        ((1, 0), (1, 0), (0, 1)),
        "separator_room / clean-room authority",
    ),
    ToyTask(
        "toy_gold_pan",
        ((9, 9, 9, 9), (9, 0, 3, 9), (9, 3, 3, 9), (9, 9, 9, 9)),
        ((0, 3), (3, 3)),
        "compression / noise scrub",
    ),
]


def solve_task(task: ToyTask) -> dict[str, object]:
    for name, operator in OPERATORS.items():
        output = operator(task.train_input)
        if output == task.expected:
            return {
                "task_id": task.task_id,
                "passed": True,
                "operator": name,
                "family": task.family,
                "output": output,
            }
    return {"task_id": task.task_id, "passed": False, "operator": None, "family": task.family}


def run_suite() -> list[dict[str, object]]:
    return [solve_task(task) for task in TOY_TASKS]

