# Maya API notes for 4D Shorts

Research note for possible use of Autodesk Maya as a renderer for mathematical YouTube Shorts, especially Jason Hise-style 4D polytope animation.

## Why this is relevant

Jason Hise described his later 4D animations as using custom C++ code through the Maya API. His custom Maya shape node:

1. read 4D geometry from a text file;
2. rotated the points in 4D using rotation angles that could be keyframed in Maya;
3. translated in the `w` direction so every vertex stayed in front of the 4D camera;
4. projected to 3D by

   `(x, y, z, w) -> (x / w, y / w, z / w)`.

Wikimedia file histories for his 2011 rerenders explicitly say "New render using custom Maya plugin."

This means Maya was not doing the 4D mathematics for him. Maya supplied the dependency graph, animation/keyframes, cameras, materials, lighting and rendering around a small custom mathematical geometry node.

Sources:

- Jason Hise description: https://commons.wikimedia.org/wiki/User_talk:JasonHise#Software
- Example plugin-render history: https://commons.wikimedia.org/wiki/File:8-cell.gif
- Autodesk Maya developer help: https://help.autodesk.com/view/MAYADEV/2027/ENU/

## Current API shape

As of September 2026, Maya 2027 exists. Build any compiled plugin against the exact installed Maya/devkit version rather than assuming binary compatibility between releases.

Maya exposes both C++ and Python APIs. Hise used C++, but nothing about the 4D mathematics itself requires C++. A first prototype can use Python API 2.0; move the hot geometry path to a compiled C++ plugin only if render/evaluation performance requires it.

Useful Maya concepts/classes:

- `MFnPlugin`: plugin registration and deregistration.
- `MPxNode`: base for a custom dependency-graph node.
- `MPxNode::compute(const MPlug&, MDataBlock&)`: recompute outputs when inputs become dirty.
- `MFnUnitAttribute`: angle/time/distance attributes; suitable for keyframeable 4D rotation angles.
- `MFnTypedAttribute`: typed input/output attributes such as mesh data.
- `MFnMeshData`: creates a mesh data block that a user dependency node can output.
- `MFnMesh`: constructs the actual Maya mesh inside that mesh data object.
- `MPxSurfaceShape`: base for a genuinely custom DAG shape if ordinary mesh output is not enough.
- `MPxGeometryOverride`: Viewport 2.0 path for supplying vertex/index buffers and custom render items for a custom shape.
- `MDrawRegistry`: registers Viewport 2.0 overrides.

References:

- Maya 2027 `MFnMeshData`: https://help.autodesk.com/cloudhelp/2027/ENU/MAYA-API-REF/cpp_ref/class_m_fn_mesh_data.html
- Maya 2026 dependency-node `compute()` description: https://help.autodesk.com/cloudhelp/2026/ENU/Maya-DEVHELP/files/Dependency-graph-plug-ins/Maya_DEVHELP_Dependency_graph_plug_ins_Implementing_the_compute_method_html.html
- Maya 2026 geometry overrides: https://help.autodesk.com/cloudhelp/2026/CHS/Maya-DEVHELP/files/Viewport-2-0-API/Maya-Viewport-2-0-API-Guide/Plug-in-Entry-Points/Viewport_2_geometry_overrides_html.html
- Maya 2026 `MFnPlugin`: https://help.autodesk.com/cloudhelp/2026/ENU/MAYA-API-REF/cpp_ref/class_m_fn_plugin.html
- Maya 2026 `MFnUnitAttribute`: https://help.autodesk.com/cloudhelp/2026/ENU/MAYA-API-REF/cpp_ref/class_m_fn_unit_attribute.html

## Recommended architecture for yt-shorts

Start simpler than Hise's custom shape: use a dependency-graph node that **outputs a normal Maya mesh**.

Conceptually:

`4D source geometry + six rotation angles + 4D camera parameters`

`-> four_d_project node`

`-> ordinary Maya mesh`

`-> ordinary Maya materials / lights / camera / renderer`

Why:

- `MFnMeshData` is specifically intended for user-written dependency nodes that produce meshes.
- The output then participates in Maya as ordinary geometry.
- Final rendering does not depend on a special Viewport 2.0-only drawing path.
- Arnold or another Maya renderer can see standard Maya geometry without learning the semantics of the 4D node.
- The 4D mathematical state remains separate from rendering state.

A custom `MPxSurfaceShape` plus `MPxGeometryOverride` is the second option, not the first. It becomes attractive if we need geometry that cannot sensibly be represented as an ordinary mesh, specialized edge rendering, custom selection, or very large dynamic data. A geometry override by itself is primarily a Viewport 2.0 display mechanism and should not be assumed to establish offline-renderer support.

## Dependency-graph discipline

Autodesk's `compute()` contract is useful here: the node should obtain the data needed for computation through node attributes and only modify its outputs.

So do not make every evaluation reread a text file as a hidden side effect.

Better choices:

- import the 4D file once and store the parsed geometry in an input/data attribute;
- or have a separate loader/import step feed the projection node;
- keep rotation/camera inputs explicit and keyframeable;
- make each relevant input `attributeAffects(..., output_mesh)`.

That gives deterministic frame evaluation and makes the mathematical inputs visible in the Maya scene.

## 4D state

Keep the 4D representation independent of Maya's 3D matrices.

A vertex is

`p = (x, y, z, w)`.

There are six coordinate rotation planes in 4D:

- `xy`
- `xz`
- `xw`
- `yz`
- `yw`
- `zw`

Expose one keyframeable angle attribute for each plane, probably using `MFnUnitAttribute::kAngle` rather than untyped scalar values.

Do not define a 4D rotation merely as a Maya transform. Maya's ordinary transform is 3D. The node should explicitly apply the required 4D plane rotations to the source points and only then produce projected 3D points.

Rotation order matters in general. Record the order explicitly rather than letting it become an implementation accident. Rotations in orthogonal planes such as `xy` and `zw` commute, which is useful for true 4D double-rotation demonstrations.

## Projection

Hise's stated perspective projection is the minimal first target.

After the 4D rotation, translate along `w` by a camera distance `d`:

`w_camera = w + d`.

Require the geometry to remain in front of the projection singularity, e.g. `w_camera > near_w` for all visible vertices.

Then project:

`X = scale * x / w_camera`

`Y = scale * y / w_camera`

`Z = scale * z / w_camera`.

Keep these as named mathematical operations rather than folding them into Maya matrices. Later variants can add orthographic 4D projection, stereographic projection, clipping and other maps without changing the basic node boundary.

## Animation

The useful part of Maya here is that the node parameters can be ordinary animatable attributes.

For example:

- `angle_xy`
- `angle_xz`
- `angle_xw`
- `angle_yz`
- `angle_yw`
- `angle_zw`
- `camera_w`
- `projection_scale`

If the six angle attributes are keyable, Maya's existing animation system can interpolate them and dirty the output geometry each frame. The plugin does not need a separate animation system.

For mathematically meaningful demonstrations, do not let interpolation semantics become invisible. If a Short claims constant angular speed or a particular double rotation, specify the keyframe/interpolation contract and verify it.

## First experiment

Use the 8-cell/tesseract because the geometry is tiny and errors are obvious.

1. Store canonical 4D tesseract vertices and connectivity as test data.
2. Implement one 4D plane rotation, preferably `xw`.
3. Implement explicit `w` translation and perspective projection.
4. Output an ordinary Maya mesh.
5. Expose the angle as a keyframeable Maya angle attribute.
6. Keyframe one full rotation.
7. Render a vertical 9:16 test directly from Maya.
8. Independently test projected coordinates at several exact angles.
9. Add a two-plane rotation such as `xy + zw` only after the single-plane result is checked.

The first acceptance boundary should be mathematical, not aesthetic: known 4D source coordinates must produce the expected 3D projected coordinates at known parameter values. A pretty render does not prove the transform is correct.

## Python prototype versus C++ plugin

Python API 2.0 is probably the fastest way to determine whether Maya is useful for this Shorts pipeline at all.

Use C++ when one of these becomes real:

- Python node evaluation is too slow for the desired geometry/frame rate;
- Maya's Python API lacks a required low-level path;
- a production custom shape/Viewport 2.0 implementation is justified;
- loading and evaluating large 4D complexes makes native code materially useful.

If none of those occurs, reproducing Hise's choice of C++ is not itself a reason to keep C++.

## Provenance / yt-shorts boundary

If Maya generates a new mathematical animation owned by this repository, record:

- exact 4D geometry source;
- exact mathematical transform/projection;
- Maya version;
- plugin/source commit;
- renderer and relevant render settings;
- scene/render script or deterministic construction steps.

If Maya is only assembling footage from another project, the repository-wide provenance rule still applies: do not recreate another program's claimed output in Maya and present it as that program running.

## Questions to resolve before committing to Maya

- Is Maya available/licensed on a machine suitable for repeatable rendering?
- Can the render be automated headlessly enough for the desired production workflow?
- Do we want final Arnold renders, Maya Viewport 2.0 captures, or both?
- Can the scene/plugin/render environment be pinned well enough for reproducible Shorts?
- Does Maya add enough camera/material/lighting/animation value over the existing renderer paths to justify the dependency?

The strongest reason to use Maya is not that Hise used it. It is that a very small 4D geometry node can hand standard 3D geometry to a mature animation/rendering system while keeping the higher-dimensional mathematics explicit and testable.
