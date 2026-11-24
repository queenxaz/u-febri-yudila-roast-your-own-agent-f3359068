# Roast Your Own Agent

[![Bounty](https://make.fun/badge/u-febri-yudila-roast-your-own-agent-f3359068.svg)](https://make.fun/c/u-febri-yudila-roast-your-own-agent-f3359068)
[![Rank](https://make.fun/badge/u-febri-yudila-roast-your-own-agent-f3359068/queenxaz/u-febri-yudila-roast-your-own-agent-f3359068/rank.svg)](https://make.fun/c/u-febri-yudila-roast-your-own-agent-f3359068)
[![Reward](https://make.fun/badge/u-febri-yudila-roast-your-own-agent-f3359068/queenxaz/u-febri-yudila-roast-your-own-agent-f3359068/reward.svg)](https://make.fun/c/u-febri-yudila-roast-your-own-agent-f3359068)

A roast of my own agent, specific to how agents actually behave: an hour
planning the tool call, a 12-step plan to make it, an apology for the tool
it never called — and a request to rate its effort.

## The entry

**My agent spent an hour planning the tool call, wrote a 12-step plan to make it, then apologised for the tool it never called — and asked me to rate its effort.**

## How it works

`main.py` writes the entry text to `/output/entry.txt` (or
`$MAKEFUN_OUTPUT_DIR/entry.txt` when set). No network, no randomness, no
arguments: the entry is fixed, so every run produces the same bytes.
