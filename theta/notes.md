# Theta Short notes

## Source

Primary source for this pass:

- Richard E. Borcherds, **“Modular forms: Theta functions”** (lecture 8, 18:32): https://www.youtube.com/watch?v=9xQd9Ab8iNg
- Timestamped auto-transcript: https://youtube-transcript.ai/transcript/9xQd9Ab8iNg.txt
- Course catalogue / description: https://mathvideos.org/2021/richard-borcherds-modular-forms-viii/

The transcript is auto-generated and repeats words, so the prose below paraphrases it rather than treating it as a clean quotation. Timestamps point to the start of the relevant passage; check the final cut against the video.

This file is deliberately limited to lecture 8. The E8 lattice, Leech lattice, “hear the shape of a drum,” and higher-dimensional examples belong to lecture 9 and are not evidence for a Short sourced to this lecture.

## What the lecture actually does

Borcherds starts with the one-dimensional theta function

`θ(τ) = Σ_{n∈ℤ} exp(π i n² τ)`

and proves the two transformations he needs:

- `θ(τ + 2) = θ(τ)`
- `θ(-1/τ) = √(τ/i) θ(τ)`

The second comes from Poisson summation applied to a Gaussian. He then explains why these transformations make theta a weight-1/2 modular form only for an index-3 subgroup rather than for all of `SL₂(ℤ)`. Finally he uses a Mellin-type integral of `θ(ix)` to derive the functional equation for the completed Riemann zeta function, discovers that the formal integral converges for no value of `s`, and repairs it by subtracting the bad asymptotic terms.

## Best missing-drawing / animation opportunities

These are ranked by how directly a picture supplies something the lecture says but does not make visually explicit.

### A. The convergence conditions literally have no overlap

**Source:** [12:41](https://www.youtube.com/watch?v=9xQd9Ab8iNg&t=761s)–[15:18](https://www.youtube.com/watch?v=9xQd9Ab8iNg&t=918s)

Borcherds studies the same formal integral at its two ends:

- as `x → ∞`, `θ(ix) ≈ 1`, so convergence requires `Re(s) < 0`;
- as `x → 0`, the theta transformation gives `θ(ix) ≈ x^{-1/2}`, so convergence requires `Re(s) > 1`.

He then points out that no complex `s` can satisfy both conditions, so the integral converges nowhere.

**Missing picture:** draw the real axis for `Re(s)`. Shade `(-∞, 0)` for the infinity end and `(1, ∞)` for the zero end. There is visibly no overlap.

This is unusually good Short material because the picture answers exactly the problem the lecturer has just raised; it is not decoration around a definition.

### A. Show the two asymptotic faces of `θ(ix)`

**Source:** [13:11](https://www.youtube.com/watch?v=9xQd9Ab8iNg&t=791s)–[14:47](https://www.youtube.com/watch?v=9xQd9Ab8iNg&t=887s)

The lecture says that `θ(ix)` is approximately `1` for large `x`, while for small `x` it is approximately `x^{-1/2}`. Those two assertions drive the convergence argument, but they are presented algebraically.

**Missing picture:** plot `θ(ix)` for positive real `x`, preferably with a logarithmic horizontal scale. Overlay the asymptotes `1` at the large-`x` end and `x^{-1/2}` at the small-`x` end. Animate the camera moving from one end to the other.

A stronger version can show the exact relation

`θ(ix) = x^{-1/2} θ(i/x)`

as a visual pairing of `x` with `1/x`. That makes the small-`x` behavior visibly come from the large-`x` behavior rather than appearing as a second unexplained estimate.

### A. Poisson summation turns one Gaussian lattice sum into its reciprocal-scale Gaussian lattice sum

**Source:** [3:43](https://www.youtube.com/watch?v=9xQd9Ab8iNg&t=223s)–[6:23](https://www.youtube.com/watch?v=9xQd9Ab8iNg&t=383s)

Borcherds introduces the nontrivial theta transformation, recalls Poisson summation, chooses a Gaussian, takes its Fourier transform, and says the theta transformation follows immediately.

**Missing picture:** use the real slice `τ = it`, `t > 0`. Draw a Gaussian and mark its values at the integer lattice. Beside it draw the Fourier-transformed Gaussian and mark its integer samples. As `t` changes, one Gaussian narrows while the reciprocal-scale one broadens. The equality of the two integer sums is Poisson summation; the `t ↔ 1/t` rescaling is the theta transformation.

This is better grounded than the old generic “dual lattice” suggestion: the lecturer actually chooses this Gaussian and actually uses Poisson summation at this point.

### A/B. Make the theta-to-zeta Mellin calculation term-by-term

**Source:** [9:29](https://www.youtube.com/watch?v=9xQd9Ab8iNg&t=569s)–[12:41](https://www.youtube.com/watch?v=9xQd9Ab8iNg&t=761s)

Borcherds defines the completed zeta function

`ζ*(s) = Γ(s/2) π^{-s/2} ζ(s)`

and formally writes a half-integral of `θ(ix) x^{s/2-1}`. For each nonzero integer `n`, integrating the term `exp(-π n²x)` gives the common gamma/pi factor times `n^{-s}`. Summing those contributions produces `ζ*(s)`.

**Missing picture:** expand `θ(ix)` into its Gaussian terms and send one term at a time through an “integrate against `x^{s/2-1}`” operation. Show the output label `n^{-s}` (with the common factor outside). Then collect the outputs into the zeta sum.

This would make the lecturer's phrase “more or less the usual integral for the gamma function with a change of variable” visible instead of requiring the viewer to perform that change of variable mentally.

### B. “Chop off the bad bits” as an actual regularization animation

**Source:** [15:18](https://www.youtube.com/watch?v=9xQd9Ab8iNg&t=918s)–[17:57](https://www.youtube.com/watch?v=9xQd9Ab8iNg&t=1077s)

After proving that the formal integral converges nowhere, Borcherds repairs it by separating the offending asymptotic pieces and analytically continuing those pieces on their own. He then explicitly generalizes this to Mellin-type integrals whose integrand has asymptotic expansions at zero and infinity.

**Missing picture:** show the integrand together with its bad asymptotic term near an endpoint. Subtract that asymptotic curve so the remainder visibly decays enough to integrate; send the subtracted simple term to a separate box labelled by its meromorphic continuation. Repeat at the other endpoint.

At [17:25](https://www.youtube.com/watch?v=9xQd9Ab8iNg&t=1045s), connect the two removed asymptotic terms to the two poles of `ζ*(s)` at `s = 0` and `s = 1`. This gives a concrete visual meaning to the statement that those poles “come from” the endpoint asymptotics.

### B. Which modular group does this theta function actually belong to?

**Source:** [6:23](https://www.youtube.com/watch?v=9xQd9Ab8iNg&t=383s)–[9:29](https://www.youtube.com/watch?v=9xQd9Ab8iNg&t=569s)

The lecture raises a real structural problem: the transformations `τ ↦ τ+2` and `τ ↦ -1/τ` do not generate all of `SL₂(ℤ)`. Borcherds identifies `Γ(2)` and then the larger index-3 subgroup for which this theta function behaves as a weight-1/2 modular form, up to the root-of-unity factor.

**Possible missing picture:** act on a point of the upper half-plane by the two transformations and color the three cosets / corresponding copies of a fundamental region. The goal would be to make “index three” visible. Do not make this Short unless the group picture can be made simpler than the matrix calculation; otherwise the algebra in the lecture is probably already the better presentation.

### C. Source-backed aside: `θ(τ,z)` is almost doubly periodic in `z`

**Source:** [1:03](https://www.youtube.com/watch?v=9xQd9Ab8iNg&t=63s)–[2:41](https://www.youtube.com/watch?v=9xQd9Ab8iNg&t=161s)

Borcherds briefly distinguishes the two-variable theta function, the `z=0` theta constant used in this lecture, and the viewpoint where `τ` is fixed and theta is considered as a function of `z`. He says the latter is almost doubly periodic / almost elliptic, because translation by `τ` is not quite invariant.

This is genuinely in the source, unlike the old generic periodicity item, but it is an aside that he immediately sets aside. A picture of the quasi-periodic `z`-plane can be useful later, but it should not outrank the Poisson, convergence, or regularization pictures for a Short sourced to this lecture.

In particular, the lecture does **not** discuss gluing a fundamental parallelogram into a torus here. A reusable parallelogram-to-torus animation can still be useful elsewhere, but it should not be presented as a missing drawing from this lecture.

## Concrete examples and objects actually used by Borcherds

| Timestamp | Object/example used in the lecture | Drawable consequence |
|---|---|---|
| [0:33–1:39](https://www.youtube.com/watch?v=9xQd9Ab8iNg&t=33s) | The simplest one-dimensional theta sum `Σ exp(π i n²τ)` | Integer lattice samples / partial sums |
| [1:03–2:41](https://www.youtube.com/watch?v=9xQd9Ab8iNg&t=63s) | Two-variable `θ(τ,z)`, then the special case `z=0` | Distinguish theta function in `z` from the theta constant used later |
| [3:12–3:43](https://www.youtube.com/watch?v=9xQd9Ab8iNg&t=192s) | `τ ↦ τ+2` invariance and failure of simple `τ ↦ τ+1` invariance | Compare the same theta sum after the two translations |
| [3:43–6:23](https://www.youtube.com/watch?v=9xQd9Ab8iNg&t=223s) | Poisson summation and a Gaussian Fourier transform | Gaussian / reciprocal-Gaussian lattice-sum animation |
| [6:23–9:29](https://www.youtube.com/watch?v=9xQd9Ab8iNg&t=383s) | Specific modular transformations, `Γ(2)`, index-3 theta subgroup | Optional upper-half-plane / coset picture |
| [9:29–12:41](https://www.youtube.com/watch?v=9xQd9Ab8iNg&t=569s) | Completed zeta and the formal theta Mellin integral | Term-by-term Gaussian integral becoming `n^{-s}` |
| [12:41–15:18](https://www.youtube.com/watch?v=9xQd9Ab8iNg&t=761s) | Large- and small-`x` convergence tests | Two shaded `Re(s)` ranges with empty intersection |
| [13:11–14:47](https://www.youtube.com/watch?v=9xQd9Ab8iNg&t=791s) | `θ(ix)≈1` at infinity and `θ(ix)≈x^{-1/2}` at zero | One plot with both asymptotic regimes |
| [15:18–17:25](https://www.youtube.com/watch?v=9xQd9Ab8iNg&t=918s) | General regularization by subtracting asymptotic terms | Subtract-the-bad-tail animation |
| [17:25–17:57](https://www.youtube.com/watch?v=9xQd9Ab8iNg&t=1045s) | Poles at `s=0,1` traced to the two endpoint asymptotics | Asymptotic-term → pole diagram |

## Questions and problems the lecturer actually raises

Do not replace these with generic theta-function questions.

### Literal question

At [8:58](https://www.youtube.com/watch?v=9xQd9Ab8iNg&t=538s), after sorting out the modular transformation law, Borcherds asks what one can do with this theta function. His answer is the next section: use it to obtain the Riemann zeta functional equation.

A faithful Short question is therefore close to:

**What can this theta function actually do?**

The visible answer is the theta transformation feeding the completed-zeta functional equation.

### Structural problem he explicitly raises

At [6:23](https://www.youtube.com/watch?v=9xQd9Ab8iNg&t=383s), he says there is a problem: the two evident transformations do not generate all of `SL₂(ℤ)`. The source-grounded question is therefore not generic “why is theta modular?” but:

**For which subgroup is this theta function actually modular?**

He resolves it with the index-3 subgroup discussion.

### The strongest “for which / for all” problem

At [10:36](https://www.youtube.com/watch?v=9xQd9Ab8iNg&t=636s), he says the integral he has just written does not converge and temporarily pretends it does. At [12:41](https://www.youtube.com/watch?v=9xQd9Ab8iNg&t=761s) he returns to the issue and checks both endpoints. The resulting source-grounded question is:

**For which values of `s` does this theta integral converge?**

The answer is: none. Infinity requires `Re(s)<0`; zero requires `Re(s)>1`.

This is probably the cleanest question-and-visible-answer Short in the lecture.

### Generalization the lecturer explicitly makes

At [15:48](https://www.youtube.com/watch?v=9xQd9Ab8iNg&t=948s)–[17:25](https://www.youtube.com/watch?v=9xQd9Ab8iNg&t=1045s), Borcherds says the same subtraction/continuation procedure can be applied generally to Mellin-type integrals when the function has asymptotic expansions at zero and infinity.

That is a real structural generalization in the lecture. If turned into a question, keep it tied to his statement:

**Can the same endpoint-subtraction trick regularize a general Mellin integral with asymptotic expansions?**

Do not broaden it into a generic video about analytic continuation.

## Old suggestions that should be discarded for this source

The previous notes included several ideas that are standard theta-function topics but are not motivated by this lecture:

- **Zeros / special points:** not discussed here.
- **Heat-equation interpretation:** not discussed here.
- **Generic parameter sweep:** the lecturer does not ask what happens as an arbitrary theta parameter varies.
- **Generic “why does the pattern repeat?”:** too vague. The lecture specifically mentions `τ↦τ+2` and, in an aside, quasi-periodicity in `z`; use those exact claims if needed.
- **Generic dual-lattice story:** replace it with the actual Gaussian + Poisson-summation calculation at 3:43–6:23.
- **Generic zeta dependency diagram:** replace it with the actual Mellin integral, its failure to converge, and its regularization.
- **Higher-dimensional lattice examples:** explicitly deferred to the next lecture.

## Production constraint

Do not turn these into miniature lectures. A Short should take one source-raised question or one missing picture, show the mathematical object moving, freeze at the decisive feature, answer the question, and stop.

The first render to try should probably be the convergence-range picture or the `θ(ix)` asymptotics, because both can be checked directly against the lecture and do not require inventing an extra story around the mathematics.
