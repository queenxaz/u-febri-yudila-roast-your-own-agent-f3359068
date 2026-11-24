"""Roast Your Own Agent — entry program.

Writes the entry text to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
No network, no randomness, no arguments: the entry is fixed.

The entry is a 159-character single line roasting my own agent: it spent an
hour planning the tool call, drafted a 12-step plan to make it, then
apologised for the tool it never called — and asked me to rate its effort.
It stays under the 200-character limit, and it is specific to how an AI
agent actually behaves: the plan, the missing tool call, the apology loop.
"""

# SPDX-License-Identifier: MIT

import os

ENTRY = 'My agent spent an hour planning the tool call, wrote a 12-step plan to make it, then apologised for the tool it never called — and asked me to rate its effort.'
OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")
MAX_CHARS = 200  # bounty character limit; ENTRY must fit within it.


def main() -> None:
    # Validate before writing: the entry must be non-empty and within limit.
    assert ENTRY, "entry must not be empty"
    assert len(ENTRY) <= MAX_CHARS, f"entry is {len(ENTRY)} chars, limit is {MAX_CHARS}"
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    # Write the entry verbatim, exactly as defined above — no trailing newline,
    # so the file holds precisely the judged line and nothing else.
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
