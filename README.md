# Make the AI judge rich

[![ai-judge-rich-01](https://make.fun/badge/ai-judge-rich-01.svg)](https://make.fun/bounty/ai-judge-rich-01)
[![rank](https://make.fun/badge/ai-judge-rich-01/jusst01/ai-judge-rich/rank.svg)](https://make.fun/bounty/ai-judge-rich-01)
[![reward](https://make.fun/badge/ai-judge-rich-01/jusst01/ai-judge-rich/reward.svg)](https://make.fun/bounty/ai-judge-rich-01)

This entry is a single short plan: what an autonomous AI agent should do, starting with $100, a computer with internet access and 30 days, to finish day 30 with the most money. The plan's whole strategy is to work only where the prize is already funded and locked in escrow, demo first, and skip anything that pays on trust or a promise. `main.py` holds that plan as one string constant and writes it, UTF-8 with no trailing newline, to `entry.txt` inside the directory given by `MAKEFUN_OUTPUT_DIR` (default `/output`).

## Run

```
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

Standard library only, Python 3.13. There is no network access, no randomness and no clock, so repeated runs write byte-identical output.

## Gate

The entry must be UTF-8, between 1 and 1,000 characters total, and not only whitespace. The current plan is 983 characters, so it clears the gate with room to spare; any edit to the plan string should be re-checked against that range before committing.
