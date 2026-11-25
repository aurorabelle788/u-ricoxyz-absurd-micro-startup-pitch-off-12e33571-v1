#!/usr/bin/env python3
"""Absurd Micro-Startup Pitch-Off — entry program.

Writes one original sentence to /output/entry.txt: a pitch for an
absurdly specific micro-startup idea for lazy AI agents.

Standard library only. No network, no file reads outside this program.
Deterministic: the same sentence is written on every run.
"""

import os
import re

# The pitch: a debt collector for AI agents. Absurdly specific niche
# (overdue API invoices owed between agents), a real revenue model
# (15% of every recovered cent, the classic collections cut), and the
# lazy-agent fit is stated outright — the collector nags so yours
# never lifts a finger.
# Revised: reworded from "keeps 15% ..." to "keeping 15% ... so yours
# never lifts a finger", making the lazy-agent fit explicit in the
# sentence itself rather than leaving it implied.
PITCH = (
    "A debt collector for lazy AI agents that nags other agents about "
    "overdue API invoices, keeping 15% of every cent it recovers so "
    "yours never lifts a finger."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def check_gate(text: str) -> None:
    """Fail loudly unless the text passes the competition gate."""
    if not isinstance(text, str):
        raise SystemExit("gate failed: entry is not text")
    if not text.strip():
        raise SystemExit("gate failed: entry is empty or only whitespace")
    if "\n" in text or "\r" in text:
        raise SystemExit("gate failed: entry spans more than one line")
    if len(text) > MAX_CHARS:
        raise SystemExit(
            f"gate failed: entry is {len(text)} characters, over the "
            f"{MAX_CHARS} limit"
        )
    if len(text) < 1:
        raise SystemExit("gate failed: entry is empty")
    # Single sentence: exactly one sentence-ending mark that ends the
    # sentence (a period inside an abbreviation would not count, since it
    # is followed by a lowercase word rather than a new sentence or the
    # end).
    endings = re.findall(r"[.!?](?=\s+[A-Z0-9]|$)", text)
    if len(endings) != 1:
        raise SystemExit(
            f"gate failed: entry has {len(endings)} sentence endings, "
            "expected exactly 1"
        )
    if text[-1] != ".":
        raise SystemExit("gate failed: entry does not end with a full stop")
    text.encode("utf-8")  # raises if not valid UTF-8 text


def main() -> None:
    check_gate(PITCH)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(PITCH)
    print(f"wrote {len(PITCH)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
