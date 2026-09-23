# Oliver Byrne

Source-research folder for **Oliver Byrne's 1847 edition of Euclid**, *The First Six Books of the Elements of Euclid in Which Coloured Diagrams and Symbols Are Used Instead of Letters for the Greater Ease of Learners*.

Byrne did **six** books, not nine. Euclid's *Elements* has thirteen books; David E. Joyce's Clark University edition covers all thirteen, while Byrne's color system covers Books I–VI.

This is research substrate for later YouTube Shorts, not a demand to make one Short for every proposition. The useful unit is usually one construction, one invariant, one surprising equality, or one move in a proof that can be understood visually in a few seconds and later reused inside a larger explanation.

## Production idea

Treat these Shorts as a library of small geometric pieces rather than miniature survey lectures. A later substantial video about, say, similarity, the golden ratio, the Pythagorean theorem, or classical construction should be able to point to or reuse one of these already-built pieces instead of introducing every primitive from zero.

Default workflow for a future Short:

1. Start from a specific proposition, construction, or user-supplied mathematical point.
2. Check Byrne's original 1847 page and Nicholas Rougeux's online reproduction for the visual organization.
3. Check David Joyce's proposition page and Guide for the mathematical dependency chain, terminology, and useful cautions.
4. Reconstruct the geometry parametrically in Manim from the public-domain 1847 source rather than treating a scan as the animation.
5. Keep the Short about one visible move. Do not pad it into a generic explanation of “Euclidean geometry.”
6. Credit Euclid/Byrne and link the source proposition. Credit any modern source whose commentary or reconstruction materially shaped the result.

See [`sources-and-licensing.md`](sources-and-licensing.md) before copying any modern HTML, diagram, or code.

## Primary navigation

### Oliver Byrne / Nicholas Rougeux

- Byrne's Euclid home: https://c82.net/euclid/
- Book I — basic plane geometry: https://c82.net/euclid/en/book1
- Book II — geometric algebra: https://c82.net/euclid/en/book2
- Book III — circles and angles: https://c82.net/euclid/en/book3
- Book IV — regular polygons: https://c82.net/euclid/en/book4
- Book V — ratios and proportions: https://c82.net/euclid/en/book5
- Book VI — geometric proportions: https://c82.net/euclid/en/book6
- About / licensing: https://c82.net/euclid/about/
- Making of the web edition: https://c82.net/blog/?id=79

Rougeux reproduced all six Byrne books online and rebuilt the diagrams for interactive use. His project page says the site contains 269 diagrams across the six books.

### Public-domain scan

- Internet Archive: https://archive.org/details/firstsixbooksofe00byrn
- Alternate scan record: https://archive.org/details/firstsixbooksofe00eucl

The 1847 work itself is public domain. This is the cleanest production source when we want Byrne's visual idea without inheriting the license of a modern redraw.

### David E. Joyce, Clark University

- Elements introduction: https://mathcs.clarku.edu/~djoyce/elements/
- Book I: https://mathcs.clarku.edu/~djoyce/elements/bookI/bookI.html
- Book II: https://mathcs.clarku.edu/~djoyce/elements/bookII/bookII.html
- Book III: https://mathcs.clarku.edu/~djoyce/elements/bookIII/bookIII.html
- Book IV: https://mathcs.clarku.edu/~djoyce/elements/bookIV/bookIV.html
- Book V: https://mathcs.clarku.edu/~djoyce/elements/bookV/bookV.html
- Book VI: https://mathcs.clarku.edu/~djoyce/elements/bookVI/bookVI.html

Joyce is especially useful because each proposition has a separate page, a diagram, explicit references to earlier propositions, and often a Guide explaining what the result is doing or where it is used later.

## Files in this folder

- [`sources-and-licensing.md`](sources-and-licensing.md) — what may be reused, what should only be linked, and the modern open-source reproductions.
- [`short-seeds.md`](short-seeds.md) — a first shortlist of proposition-sized visual pieces across all six Byrne books.
- [`manim-production.md`](manim-production.md) — default reconstruction rules so a future prompt can be as small as “do Byrne III.31” plus whatever mathematical point needs emphasis.

## First-pass priorities

The densest immediately visual clusters are:

- **Book I:** constructions, equal-area shears, triangle angle sum, Pythagorean theorem.
- **Book II:** algebra as literal areas, especially the golden-section construction in II.11.
- **Book III:** circle center, tangents, inscribed angles, Thales' theorem, power-of-a-point identities.
- **Book IV:** inscribed/circumscribed square, pentagon, hexagon, and 15-gon constructions.
- **Book V:** lower priority unless there is a specific conceptual point to make; the important seed is Eudoxus' definition of proportion, including incommensurable magnitudes.
- **Book VI:** similarity, proportional cuts, geometric means, the golden ratio, and the generalized Pythagorean theorem.

The shortlist is deliberately selective. The folder should grow when a proposition contains a good visual move or when there is something specific worth saying, not merely because the proposition exists.
