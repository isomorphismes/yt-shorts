# Teleman Riemann-surface: Wegert loop

A 7-second silent test clip for

`w = sqrt((z^2 - 1)(z^2 - k^2))`

with `k = exp(i theta)` making one trip around the unit circle.

This uses `isomorphisms/wegert` as a pinned Git submodule at `third_party/wegert`. The Short now consumes Wegert's extracted renderer-independent coloring core, `app/src/main/assets/wegert_color.glsl`, rather than driving Wegert through its interactive zero/pole state.

The renderer itself evaluates the actual complex function

`w(z;k) = sqrt((z^2 - 1)(z^2 - k^2))`

for each pixel, then passes that complex value to `wegert_color_complex(value)`. Wegert therefore owns the HCL conversion, palette constants, modulus bands, and hue bands, while this project owns only the mathematical function and the animation of `k`.

There is no zero-array encoding of the four branch points, no factor-marker UI in this clip, and no shader surgery that multiplies Wegert's accumulated factor phase by `1/2`.

The pinned Wegert commit is currently from `isomorphisms/wegert` PR #21, which extracts the coloring core while preserving the existing Android factor renderer as its behavior oracle.

There is deliberately no narration or synthetic voice in this test. This is only the moving plot.

## Wegert sources and attribution

The source archive for Wegert's *Complex Beauties* calendars, the official 2011–2024 download links, rights-status note, and the primary phase-portrait citations are kept in [`../sources/wegert-complex-beauties.md`](../sources/wegert-complex-beauties.md).

The calendars are freely downloadable from the authors' official archive, but no explicit redistribution license was located and the calendars carry copyright notices. Do not copy calendar PDFs or images into this repository merely because the official downloads are public; link and cite the originals unless separate permission is established.

## Render

```sh
git submodule update --init --recursive
python3 teleman-riemann-surface/render_wegert_loop.py
```

Output:

`teleman-riemann-surface/wegert-k-loop.mp4`
