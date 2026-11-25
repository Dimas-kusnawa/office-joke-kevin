#!/usr/bin/env python3
"""Write one office joke to /output/entry.txt.

The Funniest Office Joke, Judged Head to Head (make.fun).
"""

import os

LINE = "The birthday card for Dave has been circulating for three weeks; Dave left the company on day two."
# Setup: the birthday card doing the rounds is a ritual every office
# worker recognises — it crawls from desk to desk for weeks.
# Turn: the punchline lands last — Dave, the card's whole reason for
# existing, left the company on day two. The card outlasted the man.


# Gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters.
# This line is 98 characters, one line, no trailing newline, so the
# entry passes the gate and goes straight before the judge.
def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"wrote {path}: {LINE} ({len(LINE)} chars)")


if __name__ == "__main__":
    main()
