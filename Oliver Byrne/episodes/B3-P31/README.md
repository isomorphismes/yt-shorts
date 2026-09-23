# Byrne III.31 — the right angle stays right

First production test of the Manim contract in `../../manim-production.md`.

## Point of the Short

Keep the diameter fixed, move the third vertex continuously along the semicircle, and keep the right-angle marker/readout attached to the moving vertex. Red dotted perpendicular-bisector guides for the two moving chords pass through the circle center and cross each chord at its midpoint, so the underlying construction remains visible while the point moves. The Short is only testing the invariant in the first part of Euclid III.31; it does not expand into the acute/obtuse segment cases from the rest of the proposition.

The animation is an original parametric reconstruction. No C82 diagram, HTML/CSS, Joyce diagram, or Slyusarev implementation is copied into the scene.

## Languages

The episode source follows the repository's project-language rule:

- `scene.pi` is **Ithon** source;
- `render` is **Grease/YSH** glue;
- do not replace either with Python or Bash merely because Manim examples commonly use them.

Ithon is intentionally the language-facing layer for the Manim API here. The render entry point follows the same `#!/usr/bin/env ysh` Grease convention used elsewhere in the user's repositories.

## Reproduce

The render environment needs:

- Grease/YSH (`ysh`);
- an `ithon` executable on `PATH`;
- Manim Community **0.19.1** available to that Ithon runtime, including its Cairo rendering dependencies.

From the repository root:

```text
ysh './Oliver Byrne/episodes/B3-P31/render'
```

`scene.pi` checks the Manim version itself and renders at 1080×1920, 30 fps with Cairo. Generated media stays under this episode's ignored `media/` directory; the PR carries source, not a binary video.

Expected scene length is about 8.8 seconds.

The original contract test was rendered successfully before the source-language cleanup. That proved the visual/mathematical contract, but it does **not** count as validation of the present Ithon/Grease source. The temporary Bash/Python CI harness used for that test was removed rather than preserved as a hidden dependency. A future automated render should execute this same Ithon/Grease entry point.

## Geometry

Let the diameter endpoints be fixed points `B` and `C` on a circle and let `A` move on the upper semicircle. Every frame recomputes `AB`, `AC`, the right-angle marker, and the two perpendicular-bisector guides from the current position of `A`. Each dotted guide runs from the circle center through the midpoint of one moving chord and a little beyond it, making the perpendicular-bisector construction explicit without turning the guide into another triangle edge. This is the first claim of III.31: the angle `BAC` in the semicircle is right.

## Sources and credit

- Euclid, *Elements*, Book III, Proposition 31.
- Oliver Byrne, *The First Six Books of the Elements of Euclid* (1847), public-domain visual source: https://archive.org/details/firstsixbooksofe00byrn
- Byrne/C82 navigation and modern reference: https://www.c82.net/euclid/book3/
- David E. Joyce, proposition text and dependency check: https://mathcs.clarku.edu/~djoyce/elements/bookIII/propIII31.html

The on-screen source line credits Euclid III.31 and Oliver Byrne (1847). Joyce and C82 are linked here as research/navigation sources; their modern diagrams are not reused.
