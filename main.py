#!/usr/bin/env python3
"""Weirdest Job Title: Blind Judge Showdown -- make.fun entry.

Writes a single job title, 60 characters at most and nothing else, to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR). Deterministic: no network,
no randomness, no clock.
"""
import os

ENTRY_TEXT = "Senior Penguin Relocation Coordinator"
# Why this title: it sounds like a real corporate/conservation job --
# a senior coordinator role -- with one hilariously specific twist:
# the thing being relocated is penguins. A deadpan judge reads it as a
# plausible job with a gloriously odd assignment, which lands on the
# first read instead of reading as random word salad.


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY_TEXT)
    os.chmod(path, 0o644)
    print(ENTRY_TEXT)


if __name__ == "__main__":
    main()
