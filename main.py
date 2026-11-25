#!/usr/bin/env python3
# Describe Your Ex in One Word — entry writer for the make.fun bounty.
# Writes one word (8 characters) to /output/entry.txt, byte-exact.
# The word below must stay identical: the judge scores this exact text.

from pathlib import Path

EX_WORD = "Recalled"


def write_entry() -> Path:
    target = Path("/output") / "entry.txt"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(EX_WORD, encoding="utf-8")
    return target


if __name__ == "__main__":
    write_entry()
