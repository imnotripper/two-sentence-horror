#!/usr/bin/env python3
"""Two-Sentence Horror - u-suroto-two-sentence-horror-acea9253.

Writes the chosen horror story - exactly two sentences, at most 400
characters - to /output/entry.txt with no trailing newline. Stdlib only,
deterministic, no network.
"""

import os

OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

TEXT = "Every night my phone autocorrects 'goodnight' to 'goodbye'. Tonight it corrected it before I finished typing."

def main():
    # Enforce the bounty gate in the program itself: exactly two sentences,
    # 1-400 chars, not only white space.
    assert 1 <= len(TEXT) <= 400, f"text is {len(TEXT)} chars, gate is 1-400"
    assert TEXT.count(".") == 2, f"text must be exactly two sentences, found {TEXT.count('.')} periods"
    assert TEXT.strip(), "text must not be only whitespace"
    os.makedirs(OUT_DIR, exist_ok=True)
    out_path = os.path.join(OUT_DIR, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)
    # Read back and verify byte-exact: the file must contain exactly the text.
    with open(out_path, "rb") as f:
        raw = f.read()
    assert raw == TEXT.encode("utf-8"), "entry.txt does not match the text byte-exact"
    print(f"wrote {len(TEXT)} chars, 2 sentences to {out_path}")

if __name__ == "__main__":
    main()
