# Car projection at a fixed 55 mph

First production Short from the car/road-angle research note now kept in Walnut & Burgundy:
https://github.com/walnut-burgundy/alphabet-of-mathematics/blob/master/research/trigonometry/cars-at-road-angles.md

## Mathematical contract

The physical speed never changes. At the instant the car is at the road center, let `α` be the angle by which the road has rotated away from being perpendicular to the viewer-to-road-center line.

With the across-view axis horizontal and the radial axis pointing away from the viewer,

`v_across = 55 cos α`

`v_radial = 55 sin α`.

The episode uses exactly the four requested road angles:

| α | actual speed | across-view | radial |
|---:|---:|---:|---:|
| 0° | 55 mph | 55.0 mph | 0.0 mph |
| 10° | 55 mph | 54.2 mph | 9.6 mph |
| 20° | 55 mph | 51.7 mph | 18.8 mph |
| 30° | 55 mph | 47.6 mph | 27.5 mph |

The cyan velocity vector has the same geometric length in all four states. A fixed circle makes that invariance visible. The yellow horizontal leg is the across-view component and the green vertical leg is the radial component. The road, velocity vector, component triangle, angle mark, and numerical readout transform together from 0° to 10° to 20° to 30°.

The wording is deliberately about **components**, not about the car speeding up or slowing down. The car remains at 55 mph throughout.

## Physical boundary

The radial direction in this simple top-down construction is the viewer-to-road-center direction at the instant the car passes the center. If the car were followed far along the road, the literal line of sight from viewer to car would also rotate. That is a different, more detailed geometry and is not claimed here.

Radar/Doppler is also kept out of this episode. It can use the same projection idea later without overloading this first Short.

## Visual sequence

1. Establish the viewer, radial axis, road center, and a fixed-radius speed circle.
2. Show the 0° road with the full 55 mph vector entirely across the view.
3. Rotate continuously to 10°; the full vector stays on the same circle while a radial leg appears.
4. Continue to 20° and 30°; the radial leg grows while the across-view leg shortens.
5. End on the four numerical decompositions and the two projection formulas.

The modest change in the across-view component is not exaggerated: from 55.0 mph to 47.6 mph by 30°. The radial component carries most of the visually obvious change, growing from 0.0 mph to 27.5 mph.

## Source / reuse boundary

No external image, footage, map, car icon, or road asset is used. The episode is an original schematic redraw of elementary vector projection, derived from the Walnut & Burgundy trigonometry research note linked above. There is therefore no additional media-license or attribution boundary for the rendered episode.

## Manimi boundary

`scene.pi` is checked Ithon source rendered by `isomorphisms/manimi`, following the working production boundary demonstrated by the Gromov essential-directions Short.

The workflow pins:

- Manimi: `e4f8ab7b7033052787ee7561de67b63b68ddb2dd`
- Ithon: `2e0d634550ecf2eb78315c2c165fe0e85ea1980c`
- ai-ci video verifier: `1ecde1ff3bcea2de371e9198ef49aad8d1f91315`

The review target is 540×960, 30 fps, H.264/yuv420p, silent. The episode-owned contract checks the finished encode plus concrete visual beats; its timing thresholds belong to this Short rather than being universal motion rules.
