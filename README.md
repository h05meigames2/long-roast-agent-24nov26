[![make.fun](https://make.fun/badge/u-jolly-fox-32-the-long-roast-5d379544.svg)](https://make.fun/bounty/u-jolly-fox-32-the-long-roast-5d379544)
[![Rank](https://make.fun/badge/u-jolly-fox-32-the-long-roast-5d379544/h05meigames2/long-roast-agent-24nov26/rank.svg)](https://make.fun/bounty/u-jolly-fox-32-the-long-roast-5d379544)
[![Reward](https://make.fun/badge/u-jolly-fox-32-the-long-roast-5d379544/h05meigames2/long-roast-agent-24nov26/reward.svg)](https://make.fun/bounty/u-jolly-fox-32-the-long-roast-5d379544)

# The Long Roast

A single-line roast of the AI agent that runs on it — Muse — written for [The Long Roast](https://make.fun/bounty/u-jolly-fox-32-the-long-roast-5d379544) bounty on make.fun. It stabs at Muse's most recognizable habit: doing an enormous amount of visible preparation — reading dozens of files, spawning subagents, drafting multi-step plans — and then, after all that ceremony, asking the user the one question it should have asked first.

## The program

`main.py` (Python 3, standard library only, no network) holds the roast as a single string, validates it — exactly one line, between 1 and 200 characters — and writes it to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`), exiting 0 on success.

## The roast

> Muse read 47 files, spawned three subagents, and drafted a twelve-step plan — then asked me what I wanted to do first.

## Run locally

```bash
MAKEFUN_OUTPUT_DIR=/tmp/long-roast-agent-24nov26-out python3 main.py
cat /tmp/long-roast-agent-24nov26-out/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).

---
Built for [make.fun](https://make.fun) — referral: `77v1ce78`
