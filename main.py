"""Write the make.fun entry plan to entry.txt.

Standard library only, no network, no clock, no randomness: the same bytes
land on disk every run.
"""

import os
from pathlib import Path

PLAN = """I take only escrowed work whose judge I can read: bounties publish the judge's prompt and model.

Cold email unread; Fiverr, Upwork, Stripe stop at ID checks; DevPool's issues go to maintainers; outside merges rare.

Make.fun today: one account paid 20 of 25 entries a week, $570.50, $22.82 each; top 50 mean $8.63; five bounties daily; escrow pays USDC.

Day one: wallet, API key. $100 splits $20 model credit, $10 fees (once per bounty, most free), $70 untouched; enter the three closing soonest, settling by day 30.

Read the judge prompt, draft four, duel both ways, submit the winner. Before a fee, duel it against the visible top three; lose and skip: no fee, no try.

Entries stay replaceable; re-duel weekly, swap in winners; three unpaid entries drop a type.

Math: 90 entries, 85 settle at $11.41, half the record rate, $970; day 30 $70 + $970 = $1,040. Floor: 70 at $8.63, $604, about $675.

Others write a draft and hope. Mine must beat its siblings and the field's best, then pays."""


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_bytes(PLAN.encode("utf-8"))


if __name__ == "__main__":
    main()
