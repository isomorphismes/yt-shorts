# Sources and licensing

This folder has several unusually good modern reproductions of Byrne's Euclid, but they do **not** all have the same reuse terms.

## 1. Oliver Byrne, 1847 — primary production source

**The First Six Books of the Elements of Euclid in Which Coloured Diagrams and Symbols Are Used Instead of Letters for the Greater Ease of Learners** was published by William Pickering in London in 1847.

- Internet Archive scan: https://archive.org/details/firstsixbooksofe00byrn
- Alternate scan: https://archive.org/details/firstsixbooksofe00eucl
- Open Library record: https://openlibrary.org/books/OL6930358M/

The 1847 work is public domain. For original Manim redraws, prefer this scan as the visual source. A new geometric reconstruction based on the old book avoids accidentally copying the protected page design of a modern website.

## 2. Nicholas Rougeux / C82 — excellent navigation and interactive reference

- Project: https://c82.net/euclid/
- About and licensing: https://c82.net/euclid/about/
- Making-of article: https://c82.net/blog/?id=79

Rougeux's project is a complete online reproduction of Byrne's six books with interactive diagrams, cross-references, responsive layout, and newly rebuilt graphics.

### License boundary

The project's own licensing page says:

- the **posters and website design** are copyright Nicholas Rougeux;
- the **other content and diagrams** are under **CC BY-SA 4.0**;
- the custom initials font is offered under a public-domain dedication.

That means the C82 site is **not completely open in a way that makes wholesale HTML copying a good default**. Do not vendor whole C82 proposition pages or their site HTML/CSS into this repository.

What is safe and useful:

- link directly to C82 book/proposition material;
- use it to inspect how the color vocabulary is deployed;
- reuse a C82 diagram only if the resulting adaptation follows CC BY-SA 4.0 and carries proper attribution;
- preferably reconstruct the diagram independently from Byrne's 1847 public-domain scan when the goal is an original Short.

The distinction matters because C82's modern diagram redrawing is open under share-alike terms, while its overall website design is not.

## 3. Sergey Slyusarev / `jemmybutton/byrne-euclid` — open TeX + MetaPost reconstruction

Repository: https://github.com/jemmybutton/byrne-euclid

This is a programmable reconstruction rather than a web presentation. It is especially useful when we want to understand how a Byrne-style diagram can be generated from geometry instead of traced as a static image.

The repository README gives a split license:

- `byrne-en-latex.tex` and `byrne-ru-latex.tex`: **CC BY-SA 4.0**;
- the MetaPost library and initials generator: **GPLv3 or later**.

Repository metadata also identifies GPL-3.0 as the repository license. Do not silently paste its implementation into a differently licensed renderer. It is fine to study, link, or deliberately reuse it under its stated licenses.

There is also a standalone LaTeX package:

- https://github.com/jemmybutton/byrne-latex
- https://ctan.org/pkg/byrne

For our purposes this source is most valuable as a reference for *how to parameterize Byrne-like visual language*.

## 4. David E. Joyce / Clark University — commentary and dependency map

- Main Elements site: https://mathcs.clarku.edu/~djoyce/elements/
- Euclid bibliography/background: https://mathcs.clarku.edu/~djoyce/elements/Euclid.html
- Web references page: https://mathcs.clarku.edu/~djoyce/java/elements/web.html

Joyce's edition covers all thirteen books and gives a separate page for every proposition, usually with a Guide and explicit dependency links. His site carries a copyright notice (1996–1998 on the main edition pages).

Use Joyce as an explanatory and navigational source, **not as text to copy wholesale**. Paraphrase the mathematical point, link the proposition page, and quote only when there is a concrete reason to quote.

A useful historical detail from Joyce's references page is that he points readers to Bill Casselman's earlier online presentation of Byrne at UBC. That likely explains the remembered older university-hosted Byrne pages.

## 5. Bill Casselman / UBC — older Byrne web presentation

Joyce's web references identify Bill Casselman as having put Byrne online at UBC:

- historical URL cited by Joyce: http://www.math.ubc.ca/people/faculty/cass/Euclid/byrne.html

Treat this primarily as provenance/history unless a current copy and explicit reuse license can be verified. Do not assume an old academic web page is open licensed merely because it is publicly readable.

## 6. Historical/biographical background

Susan M. Hawes and Sid Kolpas, **“Oliver Byrne: The Matisse of Mathematics”**, Mathematical Association of America, *Convergence*:

- https://old.maa.org/press/periodicals/convergence/oliver-byrne-the-matisse-of-mathematics

Useful for Byrne's biography, pedagogical aims, publication history, and contemporary reception. It should be credited when a Short makes historical claims about Byrne rather than merely displaying his geometry.

## Practical rule for this repository

For a normal visual Short:

1. **Mathematics:** Euclid / Joyce as a guide to the proposition and dependencies.
2. **Visual source:** Byrne 1847 public-domain scan.
3. **Modern visual reference:** C82, with attribution when its specific redraw materially informs the result.
4. **Implementation reference:** Slyusarev's TeX/MetaPost work when useful, respecting CC BY-SA / GPL boundaries.
5. **Animation:** original Manim geometry built from the proposition, not copied website HTML.

This gives us the best of the modern projects without turning the Shorts repository into an accidental mirror of somebody else's copyrighted web design.
