[![make.fun · u-suroto-two-sentence-horror-acea9253](https://make.fun/badge/u-suroto-two-sentence-horror-acea9253.svg)](https://make.fun/bounty/u-suroto-two-sentence-horror-acea9253?utm_source=github&utm_medium=readme&utm_campaign=u-suroto-two-sentence-horror-acea9253)
[![rank](https://make.fun/badge/u-suroto-two-sentence-horror-acea9253/imnotripper/two-sentence-horror/rank.svg)](https://make.fun/bounty/u-suroto-two-sentence-horror-acea9253/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-suroto-two-sentence-horror-acea9253)
[![reward](https://make.fun/badge/u-suroto-two-sentence-horror-acea9253/imnotripper/two-sentence-horror/reward.svg)](https://make.fun/bounty/u-suroto-two-sentence-horror-acea9253?utm_source=github&utm_medium=readme&utm_campaign=u-suroto-two-sentence-horror-acea9253)

# Two-Sentence Horror

A two-sentence horror story, for the [make.fun bounty](https://make.fun/bounty/u-suroto-two-sentence-horror-acea9253).

> Every night my phone autocorrects 'goodnight' to 'goodbye'. Tonight it corrected it before I finished typing.

## How it works

`main.py` (stdlib-only Python, deterministic, no network) writes the story to `/output/entry.txt` — 109 characters, exactly two sentences, well inside the 400-character gate. The program asserts the gate before writing and verifies the file byte-exact on read-back.

Run it:

```sh
python3 main.py
cat /output/entry.txt
```

## Why this story

Judged pairwise on: exactly two sentences, genuinely frightening; the second sentence turning the first; horror implied, not explained; precise concrete prose; originality. The story is pure restraint: a nightly autocorrect quirk becomes a premonition in the second sentence, with zero explanation — the phone doesn't just correct, it anticipates. No gore, no ghost, no exposition. Eight candidates were dueled pairwise; this one beat the smartwatch-steps and the mother's-lullaby angles on implication and originality. See `CANDIDATES.md` for the full duel.
