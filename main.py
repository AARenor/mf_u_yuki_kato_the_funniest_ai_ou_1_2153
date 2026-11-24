#!/usr/bin/env python3
"""Write one short out-of-office reply for a make.fun bounty."""

import os
import sys
from pathlib import Path

TEXT = "On leave until the 14th. A wasp has built a nest in the mailbox and I respect her. All my mail is being held at the post office, and by the wasp."

OUTPUT_NAME = "entry.txt"


def output_dir() -> Path:
    chosen = (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )
    return Path(chosen)


def main() -> None:
    assert 1 <= len(TEXT) <= 280, "entry text must be between 1 and 280 characters"
    target_dir = output_dir()
    target_dir.mkdir(parents=True, exist_ok=True)
    target = target_dir / OUTPUT_NAME
    target.write_bytes(TEXT.encode("utf-8"))
    print(len(TEXT), file=sys.stderr)


if __name__ == "__main__":
    main()
