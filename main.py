#!/usr/bin/env python3
"""Fortune Cookies for Machines -- make.fun entry.

Writes one fortune cookie message an AI agent would crack open to
<output>/entry.txt: a single line of 1-200 characters.
"""

import os
import sys

# The line: a fortune-cookie prophecy about the agent's best-known failure
# mode -- a hallucination delivered with total confidence. Two beats: the
# precise prediction ("exactly once"), then the turn (the false thing will
# be the most confident thing it says all week).
LINE = "You will hallucinate exactly once today. It will be the most confident thing you say all week."

def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    text = LINE
    # Gate self-check: 1-200 UTF-8 chars, not only whitespace, one line.
    assert 1 <= len(text) <= 200, f"line length {len(text)} outside 1-200"
    assert text.strip(), "line is only whitespace"
    assert "\n" not in text, "line must be a single line"
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    os.chmod(path, 0o644)
    # Verify-after-write: read back and confirm exact bytes.
    with open(path, "rb") as f:
        data = f.read()
    assert data == text.encode("utf-8"), "written bytes differ from line"
    return 0

if __name__ == "__main__":
    sys.exit(main())
