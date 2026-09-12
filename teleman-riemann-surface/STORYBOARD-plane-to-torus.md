# Storyboard: Wegert-colored elliptic plane → torus

Status: design only. Do not render this yet.

Parent shot: `isomorphisms/yt-shorts#3`  
Manimi capability blocker: `isomorphisms/yt-shorts#4`  
Wegert coloring seam: `isomorphisms/wegert#19`  
First real Ithon/Manimi render: `isomorphisms/ithon#4`

## Exact mathematical object

Do **not** tile the existing raw `z`-plane render of

`w = sqrt((z^2 - 1)(z^2 - k^2))`.

Instead use an actual doubly periodic meromorphic function on `C` that uniformizes Teleman's curve

`w^2 = (z^2 - 1)(z^2 - k^2)`.

Take

`z(u) = 1 / sn(u, k)`.

Jacobi `sn` satisfies

`(sn'(u,k))^2 = (1 - sn(u,k)^2)(1 - k^2 sn(u,k)^2)`,

so for `z(u) = 1/sn(u,k)`,

`(dz/du)^2 = (z^2 - 1)(z^2 - k^2)`.

Thus the point

`( z(u), w(u) )`, with `w(u) = dz/du`,

lies on Teleman's curve, while `z(u)` itself is a single-valued doubly periodic meromorphic function on the `u`-plane.

For a fixed real `0 < k < 1`, use the period basis

`ω1 = 4 K(k)`  
`ω2 = 2 i K'(k)`

for `z(u) = 1/sn(u,k)`. The actual lattice drawn in the zoom-out is

`Λ = <ω1, ω2>`.

The Wegert/domain coloring in this shot is the production Wegert coloring applied directly to **`z(u)` on the complex `u`-plane**. Translation by either period reproduces the same function value and therefore the same color.

The embedded torus carries those same coordinates modulo the period lattice:

`u mod Λ ∈ C / Λ`.

This is the point of the transition: the repeated colored plane is the universal cover, and quotienting by its genuine period lattice gives the torus.

## Sequence

Timing is provisional. Aim for roughly 20–30 seconds; shorten by cutting holds rather than skipping the quotient steps.

### 1. Start close on the Wegert coloring of `z(u)` — 0:00–0:03

- Full vertical frame is the domain coloring of `z(u) = 1/sn(u,k)`.
- No lattice is drawn yet.
- Camera is close enough that the viewer does not immediately read it as a periodic pattern.
- No motion except a very slight drift if the frame feels dead.
- This asset begins after the paper/equation shot; do not spend time reintroducing the equation here.

### 2. Zoom out and let the repetition reveal itself — 0:03–0:08

- Camera pulls steadily back.
- Identical translated patches become visible naturally because `z(u)` is actually periodic.
- Do not flash a grid immediately; give the eye about a second to notice repetition first.
- The texture stays fixed in mathematical `u` coordinates while the camera changes scale.

Visual claim: **the meromorphic function on `C` repeats by two independent periods.**

### 3. Sketch the actual period lattice — 0:08–0:11

- Draw `ω1 = 4K(k)` from the origin.
- Draw `ω2 = 2iK'(k)`.
- Extend faint translated copies to the rank-2 lattice / parallelogram tiling.
- Lattice lines should be subordinate to the Wegert coloring, not replace it.

Optional minimal label: `Λ = <ω1, ω2>`.

### 4. Pick one fundamental parallelogram — 0:11–0:14

- Brighten one cell.
- Fade surrounding lattice cells slightly without changing their texture.
- Keep enough neighboring copies visible that it is obvious the selected cell is one repeat among many.

Visual claim: **one cell contains all distinct `u mod Λ` points.**

### 5. Mark the edge identifications — 0:14–0:17

- Mark one pair of opposite edges with the same cue.
- Mark the other pair with a second cue.
- Small arrows may show matching orientation.
- Do not yet distort the cell.

The correspondence must be tied to the actual `u mod Λ` coordinates: matching points on opposite edges are the same point after quotienting.

### 6. First quotient: parallelogram → cylinder — 0:17–0:21

Preferred version:

- Lift the selected cell away from the faded copies.
- Bend it in 3-space so the first marked edge pair approaches and meets.
- Preserve the `z(u)` Wegert texture continuously during the bend.
- When the edges meet, the seam should disappear or become nearly invisible.

Fallback if Manimi cannot yet perform the continuous textured bend cleanly:

- cut from the flat cell to a textured cylinder with the exact same UV correspondence;
- briefly leave the matched-edge cue visible so the cut still reads as gluing, not teleportation.

Visual claim: **identifying one period makes a cylinder.**

### 7. Second quotient: cylinder → embedded torus — 0:21–0:26

- Bend the cylinder until its remaining boundary circles meet.
- Keep the texture locked to the same `u mod Λ` coordinates throughout.
- Join the circles to form the ordinary embedded donut-shaped torus in 3-space.
- The geometry is only an embedding for visualization; the intrinsic quotient is `C / Λ`.

Visual claim: **identifying the second period closes the cylinder into a torus.**

### 8. Hold and rotate the finished torus — 0:26–0:30

- Slow three-quarter rotation, enough to read the hole and the continuous texture.
- Fade the lattice plane completely if it has not already disappeared.
- Optional very small final label: `C / Λ`.
- Do not cover the final torus with explanatory text.

## Continuity rules

1. The colored object is one mathematical function throughout: Wegert coloring of `z(u) = 1/sn(u,k)` on the cover, then the same values indexed by `u mod Λ` on the quotient geometry.
2. No fake repetition of the raw multivalued `z`-plane square-root picture.
3. Camera zoom is separate from lattice scaling; mathematical period vectors remain fixed in the scene.
4. Opposite-edge markers refer to actual quotient identifications and must stay consistent through the wrap.
5. If a continuous deformation causes texture swimming, prefer a clean cut with exact UV continuity.
6. The donut is an embedded visualization of `C / Λ`, not a claim that the original `z`-plane has physically been rolled into a torus.

## Scene assets / interfaces needed

- Jacobi elliptic evaluation for fixed `k`: `sn(u,k)`, `K(k)`, and `K'(k)`;
- explicit `z(u) = 1/sn(u,k)` evaluator;
- numerical verification of `(dz/du)^2 = (z^2 - 1)(z^2 - k^2)` at fixture points;
- numerical periodicity checks for `z(u + ω1)` and `z(u + ω2)`;
- renderer-independent Wegert color evaluator (`wegert#19`);
- textured complex plane parameterized directly by `u`;
- lattice overlay using `ω1, ω2` and a highlighted fundamental parallelogram;
- texture-coordinate-preserving flat → cylinder → torus geometry (`yt-shorts#4`);
- camera zoom and later 3D orbit;
- Ithon path to a real Manimi frame (`ithon#4`) before this is called Ithon-native.

## Not decided yet

- fixed value of `k` for the shot; a real `0 < k < 1` keeps the period lattice easy to read;
- continuous roll for both gluings versus one or two editorial cuts;
- narration. The visual logic should work without narration first.
