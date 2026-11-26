#!/usr/bin/env python3
"""Funniest Cat Voicemail Greeting - make.fun entry.

Writes one single-line voicemail greeting, recorded as if by a cat,
to /output/entry.txt. Python 3 stdlib only, deterministic, no network.

The greeting is written in the cat's own first-person voice: it opens
like a real voicemail ("You've reached Mochi"), lands its joke on two
things only cats do (knocking a vase off the shelf, then napping in
the box it came in), and closes with the classic voicemail cue
("Leave tuna after the beep"), so the punch arrives fast when spoken.
"""

import os

ENTRY = (
    "You've reached Mochi. I knocked your vase off the shelf, "
    "now I'm napping in its box. Leave tuna after the beep."
)

MAX_CHARS = 120


def main() -> None:
    text = ENTRY
    # Gate guards: the sealed scorer requires /output/entry.txt to be
    # UTF-8 text of 1 to 120 characters, a single line, not only
    # whitespace. Fail loudly here rather than shipping a bad entry.
    assert isinstance(text, str) and text.strip(), "entry must be non-whitespace"
    assert 1 <= len(text) <= MAX_CHARS, f"entry is {len(text)} chars, limit {MAX_CHARS}"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    text.encode("utf-8")  # raises if the entry is not valid UTF-8
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
