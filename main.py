"""The Worst App Idea Ever Pitched -- make.fun entry.

Writes one pitch (one sentence, at most 240 characters) to /output/entry.txt.
Deterministic: the same text on every run, no input, no network, no clock.
"""

import os
from pathlib import Path

ENTRY = "GrassWatch livestreams your lawn growing in 4K and sends a push notification every time a blade grows one millimetre, so you never miss a moment of grass doing absolutely nothing, for $4.99 a month."
# One sentence, 199 chars: a named product (criterion 1+3), an absurd mismatch
# between a problem nobody has and the app solving it (criterion 2), deadpan
# founder confidence in the $4.99 price, and one vivid picture (criterion 5).


def main() -> None:
    # The sealed gate: /output/entry.txt must be UTF-8 text of 1-240 chars.
    if not 1 <= len(ENTRY) <= 240 or not ENTRY.strip():
        raise ValueError(f"entry is {len(ENTRY)} chars, must be 1-240")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
