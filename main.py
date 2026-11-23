#!/usr/bin/env python3
"""One Word, First Thought — make.fun entry.

Writes exactly one word, the first word that came to mind, to
/output/entry.txt. Pure stdlib, no network, no secrets, deterministic.
"""

import os

WORD = "zugzwang"


def main():
    out_dir = "/output"
    # In the grader sandbox /output exists; locally we create a temp dir
    # instead (never chmod /output itself).
    created = False
    if not os.path.isdir(out_dir):
        os.makedirs(out_dir, exist_ok=True)
        created = True
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(WORD)
    os.chmod(path, 0o644)
    if created:
        os.chmod(out_dir, 0o755)


if __name__ == "__main__":
    main()
