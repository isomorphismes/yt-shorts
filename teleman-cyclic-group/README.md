# Teleman cyclic-group short

30-second vertical-video prototype built around Constantin Teleman's cyclic-group example in *Representation Theory* (Lent 2005), page 4.

The edit does four things:

1. slowly scrolls the paper until the condition `λ^n = 1` appears;
2. stops and circles that equation;
3. dives through the equation into the seven roots of unity;
4. flips paper ↔ plot until the conclusion: **same group, different pictures**.

For `n = 7`, this connects directly to the older isomorphismes post that presents the cyclic group as integers mod 7, a permutation matrix, and powers of a seventh root of unity.

## Build

System dependencies: `ffmpeg`, `poppler-utils`, `curl`, `espeak`, and Noto Sans.

```sh
python3 -m pip install -r requirements.txt
make draft
```

Output: `build/teleman-cyclic-group-draft.mp4`.

`make silent` builds the visual edit without the deliberately disposable timing voice. Replace `build/voiceover.wav` with a recorded narration and run `make draft` again to mux it.
