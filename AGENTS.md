# Agent instructions

## Cross-repository anti-patterns

These rules apply in addition to stricter repository-specific rules below.

- Claim only the boundary actually exercised. Source presence, fixtures, generation, compilation, packaging, installation, launch, smoke checks, semantic execution, backend execution, and physical-device execution are different evidence levels. If a stronger boundary was not exercised, report it as unverified.
- The named mechanism is part of acceptance. Do not substitute a fallback, oracle, mock, alternate backend, alternate executable, lookalike renderer, or conventional nearby toolchain and keep the original label.
- Do not weaken acceptance to obtain green. Repair the implementation. Change the contract only when the requirement itself is shown to be wrong or obsolete, and keep that semantic decision explicit. Targeted negative tests must fail for the intended reason when the distinction matters.
- Keep semantics independent of convenient representations. Mathematical, domain, and language objects are not defined by tuples, matrices, compiler nodes, ABI records, transport bytes, storage shapes, or UI payloads unless the semantics explicitly say so.
- Current explicit human corrections and current architecture outrank stale source, generated code, upstream conventions, older branches, bootstrap precedent, and familiar practice. Do not restore a rejected abstraction under its old name or a near-synonym.
- Acceptance belongs to an exact head and its material pins. An ancestor's, sibling branch's, or previous pin's green result is historical evidence only.
- Mocks, fixtures, harnesses, and today's platform adapter must cross replaceable interfaces; they do not get to define the permanent architecture merely because they are currently convenient.
- Preserve the repository's chosen implementation path and layout before introducing familiar infrastructure. Where `_` is an established machinery boundary, keep build/package/generated/test/compiler material there and preserve canonical source and intended soft links.

## Do not recreate application footage

When a short is meant to demonstrate another repository, app, APK, compiler backend, renderer, or device path, the source footage must come from that named software actually running.

Do not replace missing footage with AI-generated frames, Python/Manim/HTML lookalikes, a handwritten renderer, CPU reconstruction of a GPU path, cross-fades, interpolation, or synthetic motion and then present it as application output.

If the required behavior is not present in the source application, fix or build the source application and capture it there. `yt-shorts` may assemble and present footage; it must not manufacture the behavior being demonstrated.

## Preserve source provenance

For imported runtime footage, record enough provenance to identify the source repository, exact commit/tag or build, and named backend/device when those facts are part of the claim. A file copied into this repository does not erase its origin.

Editing may trim, crop non-content chrome, encode, resize, add narration/captions, or otherwise package the real capture without changing the demonstrated behavior. Do not use post-production to repair jumps, invent movement, alter mathematical events, or substitute a different renderer.

A reproducible render script proves the assembly process. It does not by itself prove the provenance or behavior of imported application footage.