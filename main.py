"""One-liner dad joke for The One-Liner Groan-Off.

The joke: Dad unplugs the Wi-Fi router, then delivers the pun — the box
that routes the internet is now "rooting" for the family. One concrete
observation, surprise twist in the last few words, no filler.
"""

import os


def joke() -> str:
    """Return the single-line dad joke."""
    return "Dad unplugged the router and said, \"Now it's finally rooting for us.\""


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(joke() + "\n")


if __name__ == "__main__":
    main()
