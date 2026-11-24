#!/usr/bin/env python3
"""The Funniest Out-of-Office — entry program.

Writes a one-line out-of-office message to /output/entry.txt. This
contest's gate is 1 to 140 characters; the line below sits inside it
and is written with no trailing newline.
"""

import os
from pathlib import Path


def message() -> str:
    away = "I'm out of office until Monday."
    cover = (
        "My inbox is being monitored by a goldfish with a law degree; "
        "response times may improve."
    )
    return f"{away} {cover}"


def main() -> None:
    target_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    target_dir.mkdir(parents=True, exist_ok=True)
    entry = target_dir / "entry.txt"
    entry.write_text(message(), encoding="utf-8")


if __name__ == "__main__":
    main()
