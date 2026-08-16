# VERDICT — KILL

The overlap-square identity is correct, but the proposed mechanism does not reduce the analytic difficulty. It either remains an exact restatement of RH or, when the balanced sector is isolated, falls into the prohibited factorization-space horn.

# FATAL FLAW

The proposal dies at:

\[
|J(A)|\ll_\varepsilon A^{1+\varepsilon},
\qquad J(A)=M(A)^2.
\]

This is literally the original RH-equivalent obligation, so D3(b), the coordinate-relocation test, applies.

The suggested averaged escape does not help. A full bound

\[
\sum_{T<A\le 2T}J(A)
=\sum_{T<A\le2T}M(A)^2
\ll_\varepsilon T^{2+\varepsilon}
\tag{*}
\]

is itself RH-equivalent, not merely a weaker estimate leading only to the \(2/3\) exponent.

Indeed, assuming (*) and writing \(\sigma>1/2\), choose \(\eta<2\sigma-1\). Cauchy–Schwarz on a dyadic interval gives

\[
\int_T^{2T}|M(x)|x^{-\sigma-1}\,dx
\ll
\left(\int_T^{2T}M(x)^2dx\right)^{1/2}
\left(\int_T^{2T}x^{-2\sigma-2}dx\right)^{1/2}
\ll T^{1/2+\eta/2-\sigma}.
\]

The dyadic series therefore converges. Hence

\[
s\int_1^\infty M(x)x^{-s-1}\,dx
\]

extends \(1/\zeta(s)\) holomorphically to \(\Re s>1/2\), excluding zeta zeros there and proving RH. Conversely, RH gives the pointwise Mertens estimate and therefore (*). The standard Mertens/RH equivalence and the partial-summation argument are summarized by [Conrey, “The Riemann Hypothesis,” Notices of the AMS](https://www.ams.org/notices/200303/fea-conrey-web.pdf).

Thus the proposed “averaged intermediate” triggers D3(c): it is a separately bounded nonnegative energy that is already RH-equivalent. The claim in honest weakness (3) is true only if one artificially restricts oneself to the Lipschitz argument; it is false as an assessment of the analytic strength of the mean-square estimate.

# CHECKS

- **Pin identity: correct.** Let
  \[
  S_A=\sum_{u\le A}\mu(u)M(\lfloor A^2/u\rfloor),\qquad
  M_2(x)=\sum_{uv\le x}\mu(u)\mu(v).
  \]
  Every pair \(uv\le A^2\) has \(u\le A\) or \(v\le A\), since \(u,v>A\) would give \(uv\ge(A+1)^2>A^2\). The overlap is exactly \(u,v\le A\). Therefore
  \[
  M_2(A^2)=2S_A-M(A)^2.
  \]
  This is precisely the classical Dirichlet hyperbola identity; compare the general formula in these [Imperial College analytic-number-theory notes](https://www.ma.ic.ac.uk/~bin06/M34PM16-Analytic-Number-Theory/m3pm16l14.pdf).

- **Tail bookkeeping: correct for \(A\ge1\).**
  \[
  \left\lfloor\frac{A^2}{A+1}\right\rfloor=A-1,\qquad
  \left\lfloor\frac{A^2}{A}\right\rfloor=A,
  \]
  and \(\mu(A)+M(A-1)=M(A)\). The \(A=0\) proof should be dispatched separately rather than forced through the tail calculation.

- **“Free inequality”: correct but tautological.**
  \[
  M_2(A^2)\le2S_A
  \]
  is exactly \(0\le M(A)^2\). It gives no upper bound on either signed quantity and is vacuous against a large negative \(M_2\). It is not quantitative progress.

- **Transfer to the target: correct.** Setting \(A=4K\) and absorbing \(4^{1+\varepsilon}\) into the constant gives the stated energy bound.

- **Averaging arithmetic: incomplete.** The asserted \(T^{5/2}\) “termwise cost” uses an RH-shaped input \(|M(y)|\approx y^{1/2}\). The unconditional trivial cost is closer to \(T^3\log T\) for the full swapped sum. Therefore the advertised \(T^{1/2}\) saving is not measured relative to an unconditional starting bound.

- **The displayed \(\Xi_{\rm bal}\) has an endpoint mismatch.** Swapping \(u\le A\) with \(T<A\le2T\) includes \(A=u\) when \(T<u\le2T\). The condition
  \[
  \max(u,T)<A
  \]
  omits those diagonal terms \(\sum_{T<u\le2T}\mu(u)M(u)\). They can be handled trivially at \(O(T^2)\), but the displayed \(\Xi_{\rm bal}\) is not exactly the claimed swapped balanced sector without that correction.

- **D4 is not escaped.** If the entire \(2S-M_2\) combination remains joint, it is just \(M(A)^2\), hence D3 relocation. If the proposed leverage separately bounds \(\Xi_{\rm bal}\) and handles the far sector through B5, that is a partition in the factorization variable \(u\), not an index partition of the original \(n\)-sum. It takes D4’s factorization-space horn. The \(A\)-window partition does not change that.

- **D1/Omega:** no direct contradiction. Since \(J(A)=M(A)^2\), the \(\Omega_\pm(\sqrt A)\) result produces \(J(A)=\Omega(A)\), consistent with an \(A^{1+\varepsilon}\) upper bound. But the only actual exploitation proposed—quadratic-net averaging—has no demonstrated \(\mu\)-specific estimate. The relation \(\mu*1=\delta\) is genuine, but the proposal supplies only further exact convolution identities, not a quantitative use of it.

- **Falsification thresholds are miscalibrated.** Persistent growth \(T^{2.1}\) already fails the required \(T^{2+\varepsilon}\) statement for \(\varepsilon<0.1\), yet it can pass prediction (iii) and is not killed until \(2.2\). Likewise, a constant \(3\times\) or \(10\times\) cancellation improvement supplies no asymptotic power saving. Record 032’s \(D^{0.33}\) saving plus a constant factor is still short of the required \(D^{1/2}\).

# REASONING

Classically, this is the symmetric Dirichlet hyperbola formula applied to \(f=g=\mu\). The underlying facts are standard: Dirichlet convolution corresponds to multiplying Dirichlet series, while \(\sum\mu(n)n^{-s}=1/\zeta(s)\); see [DLMF §27.4](https://dlmf.nist.gov/27.4) and [DLMF §27.5](https://dlmf.nist.gov/27.5). Consequently \(M_2\) has Dirichlet series \(1/\zeta(s)^2\). An RH-scale separate bound for \(M_2\) would itself exclude zeros to the right of \(1/2\), so that object is not analytically easier.

This is therefore a known classical bookkeeping route, not a new contraction mechanism:

- Taking absolute values after the hyperbola split returns the \(x^{3/4}\)-type barrier.
- Keeping the pieces joint returns \(M(A)^2\) exactly.
- Averaging the joint expression asks for an RH-equivalent second-moment estimate.
- Isolating the empirically favorable balanced sector loses the very cross-region cancellation the trilemma warns about.

There is no theorem saying every conceivable future use of this hyperbola identity is impossible. But this proposal, as written, contains no intervening estimate of genuinely weaker analytic character. The factor \(5\)–\(10\) numerical improvement and fitted exponents cannot fill that missing step.

# LEMMA SHIP VERDICT

**Correct, but ship only as a bookkeeping lemma—not as quantitative progress.**

The exact pin is clean, reusable, and reasonable to formalize if the repository genuinely lacks the symmetric specialization. Prefer expressing \(M_2\) as the summatory function of the existing Dirichlet convolution rather than introducing a bespoke nested-divisor definition unless that definition has other consumers.

The inequality corollary is merely the pin rewritten using \(M(A)^2\ge0\); it should not be advertised as a new analytic inequality or as clearing this round’s quantitative-leverage bar.