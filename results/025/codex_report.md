RESULT 025 — H4 RENEWAL-KERNEL AUDIT  
MODE: DESK; NO NUMERICS; NO PROMOTION

## Q1

[NONTRIVIAL-BUT-KNOWN (citation: [Heath-Brown 1982](https://doi.org/10.4153/CJM-1982-095-9); [D. H. J. Polymath, Lemma 3.3](https://msp.org/ant/2014/8-9/ant-v8-n9-p03-p.pdf))] Put
\[
L(n)=\log n,\qquad \mu_D(n)=\mu(n)\mathbf1_{n\le D},\qquad
c_j=(-1)^{j-1}\binom{k}{j}.
\]
For \(D=X^{1/k}\) and \(n\le X\),
\[
\Lambda(n)=\sum_{j=1}^{k}c_j\,
  \mu_D^{*j}*1^{*(j-1)}*L(n).
\]

[NEW-BUT-PROVED-HERE (proof: isolate one \(1\)-factor)] For every \(j\ge2\), the exact type-I form is
\[
g_j*1,\qquad
g_j=c_j\,\mu_D^{*j}*1^{*(j-2)}*L.
\]
The \(j=1\) term is
\[
k\,\mu_D*L,
\]
and is not of the form \(g*1\) with \(g\) supported on \([1,D]\).

[NEW-BUT-PROVED-HERE (proof: aggregate all \(j\ge2\) before taking absolute values)] Define
\[
g=\sum_{j=2}^{k}g_j.
\]
For \(a\le D\), truncation is inactive and
\[
\begin{aligned}
g_j(a)
 &=c_j(\mu^{*j}*1^{*(j-2)}*L)(a)\\
 &=c_j(\mu^{*2}*L)(a)
 =-c_j\mu(a)\log a.
\end{aligned}
\]
Since
\[
\sum_{j=2}^{k}c_j=1-k,
\]
one obtains
\[
g(a)=(k-1)\mu(a)\log a\qquad(a\le D).
\]
For \(k=10\),
\[
\boxed{g(a)=9\mu(a)\log a\qquad(a\le D).}
\]

[NEW-BUT-PROVED-HERE (proof: evaluate at a prime \(p>D\))] The proposal’s assertion \(\operatorname{supp}g\subseteq[1,D]\) is false. For every prime \(p>D\),
\[
g_j(p)=c_j\log p,\qquad
g(p)=(1-k)\log p=-9\log p.
\]
Thus the requested \(a\le D\) mass is only a favorable lower slice of the actual coefficient range.

[STANDARD] Heath-Brown’s identity decomposes \(\Lambda\), not \(\mathbf1_{\mathbb P}\).

[STANDARD] Exact conversion requires
\[
\mathbf1_{\mathbb P}(n)
=\frac{\Lambda(n)}{\log n}
-\sum_{\substack{r\ge2\\n=p^r}}\frac1r.
\]

[NEW-BUT-PROVED-HERE (proof: \(1/\log(ab)\) depends jointly on both convolution variables)] Multiplication by \(1/\log n\) destroys the form \(g*1\):
\[
\frac{(g*1)(ab)}{\log(ab)}
\ne \sum_{a\mid n}\widetilde g(a)
\]
for any coefficient \(\widetilde g\) obtained by merely rescaling \(g(a)\). Therefore the actual prime-indicator reduction has no exact scalar renewal kernel of the proposal’s form.

[NEW-BUT-PROVED-HERE (proof: normalize \(T(X/a)\ll(X/a)^\theta\) by \(X^\theta\))] If the nonexistent self-similarity is granted provisionally, the rung-2 scale weight is
\[
w_a=a^{-\theta},\qquad \theta=\frac12+\varepsilon,
\]
not \(a^{-1}\). There is no additional \(1/a\): the factor \(a^{-\theta}\) is the entire decay supplied by the scale change \(X\mapsto X/a\).

[NEW-BUT-PROVED-HERE (proof: \(\mu^2(n)=\sum_{d^2\mid n}\mu(d)\), hence \(\sum_{n\le t}\mu^2(n)=t/\zeta(2)+O(\sqrt t)\), followed by partial summation)] For \(0<\varepsilon<1/2\),
\[
\begin{aligned}
m_\Lambda(D;\theta)
&:=\sum_{2\le a\le D}|g(a)|a^{-\theta}\\
&=9\sum_{a\le D}\frac{\mu^2(a)\log a}{a^\theta}\\
&\sim
\frac{9}{\zeta(2)(1-\theta)}
D^{1-\theta}\log D\\
&=
\frac{108}{\pi^2(1-2\varepsilon)}
D^{1/2-\varepsilon}\log D.
\end{aligned}
\]
Hence the target-scale mass is polynomially divergent: worse than every \((\log D)^j\).

[NEW-BUT-PROVED-HERE (proof: on the extended range \(2\le n\le X\), \(1/\log n\ge1/\log X\))] Even granting the maximally favorable uniform suppression \(1/\log X\) needed to pass from \(\Lambda\) to primes,
\[
m_{\mathbb P}(D;\theta)
\ \gtrsim\ \frac{m_\Lambda(D;\theta)}{\log X}.
\]
With \(D=X^{1/10}\),
\[
m_{\mathbb P}(D;1/2+\varepsilon)
\gtrsim D^{1/2-\varepsilon}.
\]
It is still polynomially divergent.

[NEW-BUT-PROVED-HERE (proof: same partial summation at \(\theta=1\))] Even the proposal’s more favorable linear-scale weight \(a^{-1}\) gives
\[
\sum_{a\le D}\frac{|g(a)|}{a}
\sim\frac{27}{\pi^2}(\log D)^2.
\]
After the artificial factor \(1/\log X=1/(10\log D)\), the mass remains
\[
\asymp\log D,
\]
not \(<1\).

[NEW-BUT-PROVED-HERE (proof: sum the absolute HB level coefficients)] If the \(j\)-pieces are estimated separately, as in the advertised block decomposition,
\[
\sum_{j=2}^{10}|c_j|=2^{10}-1-10=1013.
\]
The favorable aggregated coefficient \(9\) above is then replaced by \(1013\); aggregation across HB levels is already the smallest available mass.

[NEW-BUT-PROVED-HERE] Q1 RESULT: no honest scalar renewal kernel exists; under the strongest charitable scalarization its rung-2 mass is \(\gg D^{1/2-\varepsilon}\), and even the incorrect \(a^{-1}\) scaling gives mass \(\asymp\log D\) after prime normalization.

## Q2

[NEW-BUT-PROVED-HERE (proof: repeat Q1 for general fixed \(k\ge2\))] For general fixed \(k\),
\[
g(a)=(k-1)\mu(a)\log a\qquad(a\le D=X^{1/k}),
\]
so the favorably prime-normalized target mass satisfies
\[
m_{\mathbb P}(D;\theta)
\gtrsim \frac{k-1}{k}D^{1-\theta}.
\]
It diverges for every fixed \(k\ge2\) and every \(\theta<1\).

[NEW-BUT-PROVED-HERE] Fewer HB levels enlarge \(D=X^{1/k}\) and worsen the polynomial divergence.

[NEW-BUT-PROVED-HERE] At \(k=1\), the \(g*1\) part disappears, but the identity becomes \(\Lambda=\mu_X*L\); there is then no telescoping type-I reduction and no claimed type-II block separation.

[NEW-BUT-PROVED-HERE] The decay from \(X/a\) has already been exhausted in \(a^{-\theta}\). Replacing it by \(a^{-1}\) silently changes the induction from the rung-2 scale \(X^{1/2+\varepsilon}\) to the linear scale \(X\).

[NEW-BUT-PROVED-HERE] Preserving cancellation between the \(j=1\) term and the aggregated \(j\ge2\) term reconstructs \(\Lambda\) on the small-\(a\) range. Its cost is loss of the proposed type-I/type-II separation and return to the original prime pairing.

[NEW-BUT-PROVED-HERE] Moving the offending type-I supports into a Harman/type-II remainder removes the claimed exact telescope only by creating unbalanced blocks with variables down to \(1\); these are not the advertised central bilinear Gram blocks.

[NEW-BUT-PROVED-HERE] Taking \(k\to\infty\) so that \(D\) stays bounded incurs
\[
\sum_j|c_j|=2^k-1
\]
and a dyadic convolution/block inventory growing with \(k\); this destroys the bounded-complexity block structure.

[OPEN] A new signed, localized Harman identity could in principle avoid absolute renewal mass, but no such identity or contractive operator estimate is supplied.

[OPEN] Keeping the signs \(g(a)=(k-1)\mu(a)\log a\) would require a new uniform estimate for
\[
\sum_a\mu(a)\log a\,F(X/a)
\]
with the varying smaller-scale values correlated across \(a\). This is new Möbius-correlation input, not an induction repair internal to the proposal.

[NEW-BUT-PROVED-HERE] Q2 RESULT: divergence is structural for the proposed fixed-level HB/telescoping mechanism. Every available “repair” either removes the telescope, restores the original prime object, or replaces the central block family by uncontrolled unbalanced blocks.

## Q3

[NEW-BUT-PROVED-HERE (proof below)] The abstract telescoping lemma is correct with the necessary truncation:
\[
\boxed{
\sum_{n\le X}(g*1)(n)M(\lfloor X/n\rfloor)
=\sum_{a\le X}g(a).
}
\]

[NEW-BUT-PROVED-HERE (proof)] Expanding \(n=ab\) and setting \(N_a=\lfloor X/a\rfloor\),
\[
\begin{aligned}
\sum_{n\le X}(g*1)(n)M(\lfloor X/n\rfloor)
&=\sum_{a\le X}g(a)
  \sum_{b\le N_a}M(\lfloor N_a/b\rfloor)\\
&=\sum_{a\le X}g(a)
  \sum_{bm\le N_a}\mu(m)\\
&=\sum_{a\le X}g(a)
  \sum_{r\le N_a}\sum_{m\mid r}\mu(m)\\
&=\sum_{a\le X}g(a).
\end{aligned}
\]
The final divisor sum is \(1\) only at \(r=1\).

[NEW-BUT-PROVED-HERE] The untruncated RHS \(\sum_a g(a)\) is valid only when \(g\) is supported in \([1,X]\). Replacing it by \(\sum_{a\le D}g(a)\) requires \(\operatorname{supp}g\subseteq[1,D]\), which the actual HB coefficient fails.

[NEW-BUT-PROVED-HERE (proof: exact lower-cutoff expansion)] For \(B_a=\lfloor y/a\rfloor\),
\[
\begin{aligned}
&\sum_{y<n\le X}(g*1)(n)M(\lfloor X/n\rfloor)\\
&\qquad=
\sum_{a\le X}g(a)
-\sum_{a\le y}g(a)\,
 H(N_a,B_a),
\end{aligned}
\]
where
\[
H(N,B):=\sum_{b\le B}M(\lfloor N/b\rfloor).
\]

[NEW-BUT-PROVED-HERE (proof: subtract pairs \(bd\le N\) with \(b>B\) from the complete hyperbola)] The exact edge is
\[
H(N,B)
=
1-\sum_{d\le\lfloor N/(B+1)\rfloor}
\mu(d)\bigl(\lfloor N/d\rfloor-B\bigr).
\]

[NEW-BUT-PROVED-HERE] This edge contains no prime indicator, no \(R\), and no \(\operatorname{Li}\); it is not the original Abel functional.

[NEW-BUT-PROVED-HERE] At \(y\asymp\sqrt X\),
\[
B_a\asymp\frac{\sqrt X}{a},
\qquad
\sqrt{N_a}\asymp\frac{\sqrt X}{\sqrt a}.
\]
For \(a>1\), \(B_a\ne\sqrt{N_a}\); the cutoff is not self-similar under \(X\mapsto X/a\).

[NEW-BUT-PROVED-HERE] Q3 RESULT: the complete-hyperbola telescope is exact; the proposal’s restricted-range “same Abel functional at scale \(X/a\)” conclusion is false.

## Q4

[NEW-BUT-PROVED-HERE] Kill grounds:

1. actual HB type-I coefficients are not supported on \([1,D]\);
2. HB decomposes \(\Lambda\), while division by \(\log n\) destroys the exact convolution telescope for \(\mathbf1_{\mathbb P}\);
3. the restricted edge is a two-parameter truncated hyperbola sum, not the Abel functional at \(X/a\);
4. the favorable \(a\le D\) target-scale mass already grows as \(D^{1/2-\varepsilon}\);
5. all proposed internal repairs destroy the claimed block reduction or require new signed Möbius-correlation input.

[OPEN] REOPEN CONDITION: supply an exact prime-measure decomposition with a genuine one- or two-parameter edge operator whose norm at homogeneity \(1/2+\varepsilon\) is \(<1\), while retaining controlled central bilinear blocks; alternatively prove a uniform signed contraction for the forced \((k-1)\mu(a)\log a\) kernel without absolute values.

Q4 VERDICT: CLOSED-KILLED

Codex session ID: 019fe831-12a5-73b0-a358-60bf9fabb262
Resume in Codex: codex resume 019fe831-12a5-73b0-a358-60bf9fabb262
