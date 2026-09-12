# Manim production notes

The goal is to make a future request such as **“Byrne III.31 — show the angle staying 90° as the point moves”** sufficient to start a good first render. Do not require a full script prompt when the mathematical target is already specific.

## Default source order

1. Read the relevant Euclid proposition and its dependencies in David Joyce's edition.
2. Inspect Byrne's 1847 public-domain page for the colored visual grammar.
3. Use C82 as a modern navigation/reference layer, not as HTML/CSS to copy.
4. When useful, inspect the open TeX/MetaPost Byrne reconstruction for ideas about parameterizing the geometry, while respecting its licenses.
5. Build the actual Short as an original geometric reconstruction in Manim.

Licensing details: [`sources-and-licensing.md`](sources-and-licensing.md).

## Project languages

Manim does not imply Python source in this repository.

- Write Manim scene source in **Ithon**, normally `scene.pi`.
- Write render/build glue in **Grease/YSH**, following the existing `#!/usr/bin/env ysh` convention.
- Do not introduce `scene.py`, Bash render scripts, or Bash-driven CI merely because upstream Manim examples use them.
- If automated rendering is added, it should execute the same Ithon/Grease entry point used locally rather than maintain a second implementation in another language.

The first Byrne III.31 contract test exposed this as a real requirement: a mathematically correct render is not sufficient if the production source bypasses the user's language stack.

## Geometry first

Do not trace a screenshot when the construction can be represented exactly.

- Define the important points, lines, circles, intersections, parallels, perpendiculars, and ratios as geometric objects.
- Derive dependent positions from the construction rather than hand-placing them frame by frame.
- If a point moves, recompute all dependent geometry from that parameter so the theorem remains true throughout the animation.
- Prefer exact geometric relations over decorative approximation.
- If a proposition depends on an earlier construction, either perform that construction briefly or begin from a clearly established result; do not smuggle in unexplained geometry.

## Byrne's visual language

The attraction is not merely an antique page style. Byrne replaces a large amount of letter naming with direct visual identity.

For a new animation:

- use color to identify the same segment, angle, area, or geometric role across the proof;
- keep black/neutral construction geometry available when color is not carrying semantic identity;
- avoid assigning colors just for decoration;
- when two areas are being compared, make the correspondence between colored pieces spatially explicit;
- when the argument changes roles, let the color change communicate that deliberately rather than accidentally.

Do **not** imitate C82's website chrome, responsive page composition, typography, or other modern site-design choices. The Short should be an independent animation of Byrne/Euclid, not a screen recording or clone of the website.

## Motion should expose the theorem

Use motion only when it answers a mathematical question.

Good patterns:

- **construction:** objects appear in the exact order needed to determine the next object;
- **invariant:** move one free point continuously while the claimed angle, ratio, incidence, or area relation remains fixed;
- **reassembly:** move equal-area pieces into a visibly comparable arrangement;
- **auxiliary-line reveal:** first show the problem, then add the one line that makes the proof work;
- **dependency reuse:** briefly recall a previously animated primitive rather than re-teaching it in full.

Bad default patterns:

- arbitrary spinning or zooming;
- redrawing a finished diagram stroke by stroke when construction order is irrelevant;
- moving objects in ways that break the proposition between key frames;
- adding a parameter sweep merely because Manim makes it easy;
- turning one visual fact into a survey of Euclid.

## One Short, one piece

The normal Short should have one principal mathematical event. Examples:

- two circles determine the equilateral triangle;
- a parallel line makes the triangle angle sum visible;
- a shear changes shape while area stays fixed;
- an inscribed angle stays right while its vertex moves;
- the circle radius steps around exactly six times to make a hexagon;
- an altitude reveals three similar right triangles.

If the user has something more specific to say, that statement takes precedence over these generic framings.

## Text

Keep visible prose sparse.

Usually enough:

- `Euclid I.47` / `Byrne I.47` or equivalent source tag;
- the one relation currently being demonstrated;
- a short user-supplied sentence when the point is conceptual rather than purely geometric;
- source/credit text at the end or in publishing metadata.

Do not paste Joyce's Guide or Byrne's prose onto the screen. The geometry should do most of the explanatory work.

## Modern explanatory overlays

It is fine to add a modern explanatory layer when Byrne's static color scheme alone is insufficient, but distinguish it visually from the original geometry. Examples:

- a temporary dashed auxiliary line;
- a moving angle measure;
- a small equality of products or areas;
- arrows showing a reassembly;
- a trace showing the locus of a moving point.

The overlay should answer a particular question and then disappear or settle. It should not make the diagram look as if Byrne himself printed the modern annotation.

## Framing and timing

Default to a vertical Shorts composition unless the specific diagram is unreadable that way.

- Start close enough that the proposition is legible immediately.
- Give the construction/motion enough time to register; do not race through the crucial geometric event.
- Once the result becomes clear, hold the final configuration long enough to inspect it.
- If a moving invariant is the point, show enough of the path that the viewer sees it is not a coincidence at two sampled positions.
- Avoid dead time before the first mathematical change.

## Credit and reuse

For an independently reconstructed animation:

- credit **Euclid** for the proposition;
- credit **Oliver Byrne (1847)** for the colored pedagogical presentation when Byrne's visual method is used;
- link the Byrne scan or C82 navigation page;
- link **David E. Joyce** when his Guide/dependency organization materially informed the explanation;
- if a modern C82 diagram itself is copied, traced, or adapted rather than independently reconstructed, record that explicitly and follow its CC BY-SA 4.0 terms;
- if code or visual implementation is copied from the Slyusarev Byrne projects, follow the applicable CC BY-SA/GPL license rather than treating it as public domain.

## Episode layout when a real Short is started

Do not create hundreds of empty proposition folders. Create an episode folder only when work begins.

Suggested name:

`Oliver Byrne/episodes/B3-P31/`

Suggested files as needed:

- `README.md` — the actual point to make, proposition, source links, and any credit/license notes;
- `scene.pi` — Ithon Manim scene;
- `render` — Grease/YSH entry point when a repeatable render command is useful;
- local assets only when they are genuinely needed and reusable under their license;
- rendered preview using the repository's normal render/preview conventions.

The episode README should preserve the user's specific reason for choosing the proposition. That reason is usually more important than a generic theorem summary.

## Minimum prompt contract

Once this folder exists, prompts of roughly these forms should be actionable without another research round:

- `Byrne I.35 — show the top edge sliding while the area stays fixed.`
- `Byrne II.11 — I want the moment where the golden section appears, not the whole Book II argument.`
- `Byrne III.31 — move the point around the semicircle and keep the right angle readout visible.`
- `Byrne IV.15 — show why the radius is already the hexagon side.`
- `Byrne VI.31 — use the same weird similar shape on all three sides instead of squares.`

The assistant should then verify the exact proposition/source, preserve the user's mathematical point, implement the geometry, and render a first pass. It should not replace that point with a generic “interesting Euclid fact.”
