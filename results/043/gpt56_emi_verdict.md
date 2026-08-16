## VERDICT

**KILL.**

The excursion inequality is sound, but the proposed moment input is not a weaker averaged substitute for RH. At the stated “for every epsilon” scale, any fixed moment bound already implies RH through the classical Mellin transform of \(M\). This triggers **D3(c)**.

## FATAL FLAW

The proposal dies at:

> “no single required \(E_m\) bound is RH-equivalent”  
> “\(m=1\) returns only \(2/3\)”

For any fixed \(m\ge1\),

\[
\forall \delta>0,\qquad
E_m(K)=\sum_{k\le K}|M(4k)|^{2m}
 \ll_{m,\delta}K^{m+1+\delta}
\]

is already equivalent to RH.

Indeed, the endpoint bound transfers this to

\[
\sum_{n\le X}|M(n)|^{2m}\ll_{m,\delta}X^{m+1+\delta}.
\]

Hölder on a dyadic interval gives

\[
\int_X^{2X}|M(t)|\,dt
 \ll X^{1-1/(2m)}
       \left(\int_X^{2X}|M(t)|^{2m}dt\right)^{1/(2m)}
 \ll X^{3/2+\delta/(2m)}.
\]

Consequently, for \(s=\sigma+it\),

\[
\int_X^{2X}|M(t)|t^{-\sigma-1}dt
 \ll X^{1/2-\sigma+\delta/(2m)}.
\]

For every \(\sigma>1/2\), choose \(\delta<2m(\sigma-1/2)\). The dyadic series converges, so

\[
s\int_1^\infty M(x)x^{-s-1}\,dx
\]

is analytic throughout \(\Re s>1/2\). It equals \(1/\zeta(s)\) for \(\Re s>1\), hence analytically continues \(1/\zeta\) without poles into \(\Re s>1/2\). Therefore \(\zeta\) has no zeros there, and RH follows.

This is the classical Mertens/Dirichlet-series criterion; see [Titchmarsh, *The Theory of the Riemann Zeta-Function*, Theorem 14.25(B–C)](https://sites.math.rutgers.edu/~zeilberg/EM18/TitchmarshZeta.pdf).

Thus the nonnegative moment obligation \(E_m\) contains the whole RH difficulty. The generic excursion estimate only hides this because it ignores the arithmetic-specific identity

\[
\sum_{n\ge1}\frac{\mu(n)}{n^s}=\frac1{\zeta(s)}.
\]

Even under the narrower interpretation where only one pair \((m,\delta)\) is assumed, that pair already excludes zeros in

\[
\Re s>\frac12+\frac{\delta}{2m}.
\]

For the proposal’s \(\delta=\varepsilon/2\) and \(m\gtrsim1/\varepsilon\), this reaches approximately \(1/2+O(\varepsilon^2)\), much closer to RH than the advertised pointwise \(1/2+\varepsilon\) output. Letting \(\varepsilon\to0\) gives RH. This is relocation, not reduction.

## CHECKS

- **Increment identity:** Correct:
  \[
  M(4(k+1))-M(4k)
  =\mu(4k+1)+\mu(4k+2)+\mu(4k+3),
  \]
  since \(\mu(4k+4)=0\). Hence the increment has absolute value at most \(3\).

- **Peak persistence:** Correct. With \(H=|M(4K_0)|\) and \(q=\lfloor H/6\rfloor\),
  \[
  |M(4(K_0+j))|\ge H-3j\ge H/2
  \quad(0\le j\le q).
  \]

- **Window containment:** Correct. Since \(H\le3K_0\),
  \[
  K_0+q\le K_0+H/6\le\tfrac32K_0\le2K.
  \]

- **Kernel constant:** Correct but loose:
  \[
  E_m(2K)\ge(q+1)(H/2)^{2m}
  \ge\frac{H^{2m+1}}{6\cdot4^m}.
  \]
  Therefore the proposed inequality holds even without the added \(9\).

- **Exponent arithmetic:** Correct:
  \[
  \frac{m+1+\varepsilon/2}{2m+1}
  =\frac12+\frac{1+\varepsilon}{2(2m+1)}.
  \]
  Taking \(m\ge1/\varepsilon\) is sufficient. To reach the target energy exponent \(1+\varepsilon\), one must apply the amplitude result with \(\varepsilon/2\); the universal epsilon quantifier permits this.

- **Omega guardrail:** Passed. A \(\sqrt K\)-height excursion contributes only \(K^{m+1/2}\) to \(E_m\), compatible with \(K^{m+1+o(1)}\). The kill instead uses the genuinely \(\mu\)-specific Mellin identity.

- **D2/D4/D6:** The interpolation step itself makes no forbidden additive split and respects lane discipline.

- **D5 / claimed machinery:** The only concrete quadratic opening is admitted to have the banned nonnegative kernel. “Tensor powers beyond” does not solve higher moments:
  \[
  E_m\le E_1^m.
  \]
  Thus \(E_1\ll K^{2+o(1)}\) gives only \(E_m\ll K^{2m+o(1)}\), missing the desired \(K^{m+1+o(1)}\) by \(K^{m-1}\). No surviving higher-moment mechanism is supplied.

- **Numerics:** Stable normalized moments are consistent with RH but cannot distinguish this criterion from RH itself. A finite-range fitted exponent cannot mathematically falsify an \(O_\delta(K^{m+1+\delta})\) statement with arbitrary constants, though it can reject the heuristic at that scale.

## REASONING

The bounded-increment interpolation is a standard and valid \(L^{2m}\)-to-\(L^\infty\) estimate. The mistake is assessing the strength of \(E_m\) only through that generic estimate. For an arbitrary Lipschitz sequence it yields the lossy exponent claimed. For the Mertens function, however, its mean size controls the Mellin transform of \(1/\zeta\). That arithmetic channel is substantially stronger.

Accordingly, the classical analogue is a known dead route: replace pointwise Mertens control by a critical-scale mean-value hypothesis, then recover analytic continuation of \(1/\zeta\) by Hölder and Mellin transformation. It is a valid RH criterion, not a tractable reduction. The proposed “averaging” has not weakened the analytic obligation.

## LEMMA SHIP VERDICT

**REVISE, THEN SHIP ONLY AS LOW-LEVEL INFRASTRUCTURE.**

The first lemma is mathematically correct and kernel-worthy as a generic bounded-step interpolation fact. Recommended cleanup:

- Remove the unnecessary \(+9\).
- Replace “downward induction” with forward iteration of the increment bound.
- Either state \(m\ge1\) as advertised or document that the inequality also holds for \(m=0\).
- Do not describe it as quantitative RH progress absent an independently available, noncircular fixed-exponent moment estimate.

It does not rescue the proposal, and the full \(K^{m+1+\varepsilon}\) moment premise must not be presented as easier than RH.