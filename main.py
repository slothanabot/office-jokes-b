#!/usr/bin/env python3
"""One-Line Office Jokes — make.fun entry (Account B / Slothana).

Writes a single one-line office joke to /output/entry.txt.

Gate: /output/entry.txt must be UTF-8 text of 1 to 199 characters, not
only white space, on a single line.

Judge brief (from the kit's RULES.txt): a single-line joke about office
life that turns on a real detail (meetings, email, the printer, the
coffee machine) and lands its laugh in the last few words.
"""

import os
from pathlib import Path

# One line, 101 characters. Real detail: the office printer jams exactly
# when a document is marked urgent. The laugh lands on the final beat:
# IT rewards the jam-prone printer with Employee of the Month, a
# concrete office trope that sharpens the joke's closing words.
ENTRY = (
    "Our printer only jams on documents marked urgent, which is why "
    "IT nominated it Employee of the Month."
)


def main() -> None:
    output_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    entry_path = output_dir / "entry.txt"
    entry_path.write_text(ENTRY + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
