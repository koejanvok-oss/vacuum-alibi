#!/usr/bin/env python3
"""The Vacuum's Alibi — one-line entry for the make.fun bounty
u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7.

Writes the robot vacuum's excuse for missing a spot to /output/entry.txt.
"""

import os

LINE = (
    "That corner is a scheduled no-go zone: my sensors classified it as "
    "haunted, and my battery does not cover exorcisms."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
