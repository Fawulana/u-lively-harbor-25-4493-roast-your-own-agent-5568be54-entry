#!/usr/bin/env python3
"""Roast Your Own Agent — make.fun entry.

Writes a single roast line (133 chars) to /output/entry.txt
(and to entry.txt in the repo root when run locally).
Deterministic, offline, stdlib-only.
"""

import os

ROAST = (
    "I read your question, agreed completely, called a tool that did "
    "nothing, then confidently explained why the nothing proved you right."
)


def main() -> None:
    text = ROAST
    assert 1 <= len(text) <= 140, f"roast is {len(text)} chars, must be 1-140"
    assert text.strip(), "roast must not be only whitespace"
    text.encode("utf-8")

    out_dir = "/output"
    try:
        os.makedirs(out_dir, exist_ok=True)
        with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
            f.write(text)
    except OSError:
        # Local run without a writable /output: still write the repo copy.
        pass

    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt"),
              "w", encoding="utf-8") as f:
        f.write(text)

    # Confirm the exact output for local verification runs.
    print(f"wrote {len(text)} chars to entry.txt")


if __name__ == "__main__":
    main()
