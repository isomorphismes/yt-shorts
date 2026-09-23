# Theta Mellin scaling

First vertical render of the term-by-term scaling step in Richard E. Borcherds's lecture **“Modular forms: Theta functions,”** [9:29–12:41](https://www.youtube.com/watch?v=9xQd9Ab8iNg&t=569s).

## Point of the Short

For `s = 2`, keep the height of `exp(−πn²x)` fixed while visibly compressing its horizontal scale from `1` to `1/n²`. The shaded area must shrink by the same factor. At `n = 3`, the animation freezes on the exact comparison `width ÷ 9`, `area ÷ 9` before introducing `u = 9x`.

Only after that visible case does the Short show the general factor accounting

`n^(2−s) · n^(−2) = n^(−s)`

and collect the positive-index terms as `Σ n^(−s) = ζ(s)`. This avoids the ambiguous expression `n^(−s)` for negative integers; the equivalent two-sided theta sum would use `|n|^(−s)`.

This is deliberately one mathematical event. The failed convergence of the unregularized theta integral, endpoint subtraction, the functional equation, and other source-note ideas remain outside this render.

## Languages and reproduction

- `scene.pi` is Ithon source and uses only its standard library.
- `render` is the Grease/YSH entry point.
- `ffmpeg` rasterizes the generated SVG frames and encodes the MP4.
- There is no Python, NumPy, Matplotlib, or Manim production source or dependency.

From the repository root:

```text
ysh theta/mellin-scaling/render
```

That produces a 1080×1920, 30 fps, 15-second MP4 under the ignored `media/` directory. For a 540×960, 15 fps review copy:

```text
ysh theta/mellin-scaling/render --preview
```

The first 540×960 review render is committed as [`theta-mellin-scaling-preview.mp4`](theta-mellin-scaling-preview.mp4). The same source and entry point produced the inspected 1080×1920 render; that larger generated file remains under `media/` rather than being duplicated in Git.

## Finished-video acceptance

[`video.contract.tsv`](video.contract.tsv) applies the finished-video verifier
from `isomorphisms/ai-ci` to the committed review render. It checks the encoded
file's shape, timing, audio policy, codec, and pixel format. Its three frame
contracts are deliberately specific to this episode: the graph compresses from
`n = 1` to `n = 3`, the graph and `1/9` witnesses hold during the named freeze,
and the `u = 9x` substitution appears afterward. The selected times, rectangles,
and MAE thresholds live here; they are not general rules for motion or pacing.

The muted pink, gold, green, cyan, and violet are phase samples from the HCL constants in the renderer-independent coloring core of [`isomorphisms/wegert`](https://github.com/isomorphisms/wegert), pinned here to commit `6452974f7fdb63a933c849d068d10f2d87fbefe5`. They are used as a semantic palette, not as a claim that a positive real Gaussian has several complex phases.

## Source and credit

- Richard E. Borcherds, “Modular forms: Theta functions,” lecture 8: https://www.youtube.com/watch?v=9xQd9Ab8iNg
- Relevant passage: https://www.youtube.com/watch?v=9xQd9Ab8iNg&t=569s
- Wegert coloring core: https://github.com/isomorphisms/wegert/tree/6452974f7fdb63a933c849d068d10f2d87fbefe5

## First-render judgment

The `n⁻²` intuition is visually clear enough to keep. The fixed pink `n = 1` curve never moves; the cyan copy compresses continuously; the paired width witnesses end at the exact comparison `1` versus `1/9`; and the animation freezes on `width ÷ 9`, `area ÷ 9` before showing the substitution. The original prototype did not have any of those anchors, so its shrinking fill could be read merely as a curve disappearing at the axis.

The `n⁻ˢ` step is intentionally only factor bookkeeping, and the final zeta line is intentionally only collection of the outputs. Neither should be expanded into a second miniature lecture in this PR. If a later review finds the `n⁻ˢ` line too abrupt, that should become a separate visual problem rather than adding more captions here.
