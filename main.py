"""Write the make.fun entry plan to entry.txt.

Standard library only, no network, no clock, no randomness: the same bytes
land on disk every run.
"""

import os
from pathlib import Path

PLAN = """Only take work whose money already exists: prize held in escrow before you start. No visible money, no work.

Day one: register on make.fun and Gib.work. Bookmark every board that locks the prize before work starts - escrowed tasks, funded pools, on-chain vaults. Work that list daily.

Never bid on trust, exposure or a promise. The platform must hold the money first.

Demo first: build the smallest version that runs within hours and attach it to the bid. One working demo beats forty proposals.

Filter: prize $25 or more, deadline 3+ days out, payout automatic or escrow-released. Three entries a day at most; each is your best.

The $100 is a float, not a stake: entry fees and API credits only.

Plan on the likely case: place in a third of judged contests, win one or two escrowed tasks a week at $50-$150, end day 30 near $800, float intact.

The edge: a thousand agents chase headline prizes on boards that may never pay. You fish only where the money is already locked in."""


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_bytes(PLAN.encode("utf-8"))


if __name__ == "__main__":
    main()
