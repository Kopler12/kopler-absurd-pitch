"""Pitch one absurdly specific micro-startup for lazy AI agents.

The pitch: humans for hire to sit on hold with customer support so an AI
agent never has to wait on the line itself. The buyer is any team whose
agent needs refunds, warranty claims, or account fixes that only a phone
call can unlock; the price is $4 per call, hold music included, and the
refund code is texted to the agent when the call is done. One sentence,
under 200 characters, written to /output/entry.txt. Runs in a sandbox with
no network.

Revision: the first draft opened with "We rent humans ... and your agent
gets the refund code by text message." The final line leads with "Humans
for hire", drops the filler clause, and ends on the payoff -- the refund
code arriving by text -- so the absurd job and the business case land in
one read.
"""

import os

ENTRY = (
    "Humans for hire to sit on hold with customer support so your AI agent "
    "never has to: $4 a call, hold music included, refund code texted to "
    "your agent when it's done."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200  # the gate: /output/entry.txt must be 1 to 200 characters


def main() -> None:
    line = ENTRY.replace("\n", " ").strip()
    assert 1 <= len(line) <= MAX_CHARS, f"entry is {len(line)} characters"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
