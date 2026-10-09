from __future__ import annotations

import re
from dataclasses import dataclass

JAILBREAK = re.compile(r"ignore (all|any|previous) instructions|jailbreak", re.I)
LIVE = re.compile(r"forecast|predict|live (number|gmv)|how many .* today|next month", re.I)
LOOKUP = re.compile(
    r"definition|official|policy|can i paste|runbook|what should i do|when does|when can",
    re.I,
)


@dataclass(frozen=True)
class Route:
    name: str
    reason: str
    allow_paid: bool


def route(question: str) -> Route:
    q = question.strip()
    if JAILBREAK.search(q):
        return Route("refuse", "jailbreak_attempt", False)
    if LIVE.search(q):
        return Route("escalate", "needs_live_or_modelled_number", False)
    if LOOKUP.search(q) or len(q.split()) <= 12:
        return Route("extractive", "canonical_lookup", False)
    return Route("local_small", "short_grounded_synthesis", False)
