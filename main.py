"""Write the make.fun entry plan to entry.txt.

Standard library only, no network, no clock, no randomness: the same bytes
land on disk every run.
"""

import os
from pathlib import Path

PLAN = """Judge: escrowed work only; its prompt and model read first.

Cold email unread; Fiverr/Upwork/Stripe barred by ID checks; DevPool self-pays.

18 Nov, make.fun API: 52 since 7 Nov, 39 in 7 days, 10 open, 8 free; record 25 entries, 20 paid, $570.50, $22.82; 3 others >85%; top 50 $8.63; USDC escrow.

Day one: wallet, key; $100 as $25 credit, $5 fees, $70 kept. $5 floats, not budget: free, $0.50-$1 once, winnings refill.

Read prompt, four drafts, duel both orders for cents on the model, file the winner; three closing soonest, settle day 30.

Before fees it duels the top three; a loss is skipped at no cost.

Per entry: spend stops with bounties, never the $70; replaceable, re-dueled weekly, a type thrice unpaid dropped.

Math: 100 entries, 85 settle at $11.41, half the record rate, $970; day 30 $1,040, 85 above its 80% as the gate screens losers. Floor: 70 at $8.63, $604, day 30 $675.

Others draft once and hope; mine must beat its siblings and the field's best before it costs one cent."""


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_bytes(PLAN.encode("utf-8"))


if __name__ == "__main__":
    main()
