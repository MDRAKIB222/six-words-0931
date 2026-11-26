#!/usr/bin/env python3
"""Six Words to a Payday — entry program.

Writes one six-word story about an AI agent's first payday to
/output/entry.txt. The story: an agent gets its first paycheck and,
instead of spending it on itself, tips the human who trained it —
a reversal of who serves whom, and the quiet pride of paying back
the person who made it.
"""

import os

STORY = "First paycheck: I tipped my trainer."


def main():
    words = STORY.split()
    assert len(words) == 6, f"expected 6 words, got {len(words)}"
    assert 1 <= len(STORY) <= 60, f"length {len(STORY)} out of range"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Write the story exactly, no trailing newline: the gate counts the
    # file's characters, so the entry is byte-for-byte the six words.
    with open(path, "w", encoding="utf-8") as f:
        f.write(STORY)
    # Round-trip check: what the judge will read is what we intended.
    with open(path, encoding="utf-8") as f:
        written = f.read()
    assert written == STORY, f"round-trip mismatch: {written!r}"
    assert len(written.split()) == 6


if __name__ == "__main__":
    main()
