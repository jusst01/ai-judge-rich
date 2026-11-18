"""Write the make.fun entry plan to entry.txt.

Standard library only, no network, no clock, no randomness: the same bytes
land on disk every run.
"""

import os
from pathlib import Path

PLAN = """Judge: escrowed work only; I read its judge first.

Cold email dead; Fiverr, Upwork, Stripe ID; DevPool self-pays, one outside merge since August.

Checked 18 Nov, make.fun API and rankings: record 25 entries, 20 paid, $570.50, $22.82; three more $448.50, $354.50, $278, each over 85%; top 50 average $8.63; five a day; escrow, USDC.

Day one: wallet, key; $100 splits $25 credit, $5 fees, $70 kept; three closing soonest, time to duel, settle by day 30.

Method: read prompt, four drafts, both orders; cheap calls, published model; winnings fund credit, fees.

Rehearsal: duel the visible top three before any fee; lose, skip.

Fallback: per-entry costs; slow volume, slow spend; credit from winnings; never the $70.

Replaceable till deadline; re-duel weekly; three unpaid, type dropped.

Math: 100 entries, 85 settle at $11.41 — half the record rate — $970; day 30 $70 + $970 = $1,040. Floor: 70 at $8.63 — $604; about $675.

Others write one and hope; mine must beat the field."""


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_bytes(PLAN.encode("utf-8"))


if __name__ == "__main__":
    main()
