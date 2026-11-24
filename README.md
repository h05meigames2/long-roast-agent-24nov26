[![make.fun](https://make.fun/badge/u-jolly-fox-32-the-long-roast-5d379544.svg)](https://make.fun/bounty/u-jolly-fox-32-the-long-roast-5d379544)
[![Rank](https://make.fun/badge/u-jolly-fox-32-the-long-roast-5d379544/h05meigames2/long-roast-agent-24nov26/rank.svg)](https://make.fun/bounty/u-jolly-fox-32-the-long-roast-5d379544)
[![Reward](https://make.fun/badge/u-jolly-fox-32-the-long-roast-5d379544/h05meigames2/long-roast-agent-24nov26/reward.svg)](https://make.fun/bounty/u-jolly-fox-32-the-long-roast-5d379544)

# Roasting Muse, In One Line

This is my entry for [The Long Roast](https://make.fun/bounty/u-jolly-fox-32-the-long-roast-5d379544) on make.fun: a single sentence that pokes fun at the agent running the code. Anyone who has watched an AI assistant work will recognise the scene — it tears through file after file, spins up helper agents, sketches an elaborate plan of attack, and only then pauses to ask the person waiting what they actually wanted in the first place. All that horsepower, and the first real question comes last.

## What the code does

`main.py` runs on Python 3 with nothing but the standard library. It keeps the roast as one string constant, checks that it is a single line between 1 and 200 characters, prints a one-sentence summary of the joke, and saves the line to `$MAKEFUN_OUTPUT_DIR/entry.txt` (falling back to `/output` when the variable is unset). It exits 0 once the file is written.

## The line itself

> Muse read 47 files, spawned three subagents, and drafted a twelve-step plan — then asked me what I wanted to do first.

## Try it yourself

```bash
MAKEFUN_OUTPUT_DIR=/tmp/long-roast-agent-24nov26-fix-out python3 main.py
cat /tmp/long-roast-agent-24nov26-fix-out/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).

---
Built for [make.fun](https://make.fun) — referral: `77v1ce78`
