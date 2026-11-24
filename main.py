#!/usr/bin/env python3
"""A one-line roast aimed at the agent that executes this very script.

The joke lands on a familiar pattern: the agent does a mountain of
visible homework first, then turns around and asks the human the
question it could have opened with. The program below only checks the
line and drops it into the output file the bounty harness reads.
"""

import os
import sys

ROAST = "Muse read 47 files, spawned three subagents, and drafted a twelve-step plan — then asked me what I wanted to do first."

MAX_CHARS = 200
DEFAULT_OUT = "/output"


def count_words(sentence):
    """Return how many whitespace-separated words a sentence holds."""
    return len(sentence.split())


def describe_roast(sentence):
    """Return a short plain-language summary of the roast's punchline."""
    words = count_words(sentence)
    return (
        "A %d-word roast: the agent over-prepares, then asks the "
        "user what to do first." % words
    )


def check_single_line(sentence):
    """Reject anything that is not exactly one line of 1-200 characters."""
    cleaned = sentence.strip()
    if not cleaned:
        return "roast is empty"
    if "\n" in cleaned or "\r" in cleaned:
        return "roast must fit on a single line"
    if len(cleaned) > MAX_CHARS:
        return "roast is %d characters, over the %d limit" % (
            len(cleaned),
            MAX_CHARS,
        )
    return None


def persist_entry(sentence):
    """Save the validated roast to entry.txt inside the output folder."""
    folder = os.environ.get("MAKEFUN_OUTPUT_DIR", DEFAULT_OUT)
    os.makedirs(folder, exist_ok=True)
    target = os.path.join(folder, "entry.txt")
    with open(target, "w", encoding="utf-8") as handle:
        handle.write(sentence.strip())
    return target


def run():
    """Validate the roast, describe it, then write it out."""
    # The summary line is only for the local log; the file holds the roast alone.
    problem = check_single_line(ROAST)
    if problem is not None:
        print("cannot submit roast: %s" % problem, file=sys.stderr)
        return 1
    print(describe_roast(ROAST))
    saved = persist_entry(ROAST)
    print("roast saved to %s" % saved)
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
