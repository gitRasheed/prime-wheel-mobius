## VERDICT

**KILL.**

The pointwise multiplicative sign lemma survives. The proposed contraction mechanism does not.

## FATAL FLAW

The proposal dies at step (3):

> “the two-prime interaction remainder is exactly the collision frontier”

No such bridge is supplied, and the proposed site realization is the wrong object.

`sum_correctedCollisionSiteWeight_prefix_eq_defect` selects labels using the physical CRT frontier but evaluates their weights through an arbitrary function `site`. Choosing

\[
\operatorname{site}(a,b)=p^a\operatorname{base}(b)
\]

makes the sign-reversal hypotheses true by construction. It does **not** show that these sites are the actual integers or cofactors represented by the CRT labels. The numerical \(D(K)\), meanwhile, uses the physical incomplete-period cofactor. Thus the Lean instantiation and the measured object are not connected by an equality.

This is precisely D3(b), coordinate relocation. The proposal itself admits that physical faithfulness is unproved; that is not a secondary weakness—it is the entire bridge from the true remainder to \(D(K)\).

B4 cannot repair this. A positive modulus

\[
A t\prod_{p\in S}(1+1/p)+(A+B)N_{\rm active}
\]

only bounds drift after absolute values. It neither identifies the two coordinate systems nor preserves the signed cancellation measured in \(D\). Summing those costs is the sign-blind divisor-family charging killed by D2/D3(a).

## CHECKS

- **B1:** \(M(4K)=W_a+W_b+W_c\) is accepted from the frozen dossier.

- **B2:** The endpoint cost \(3\) is correct: changing \(X\) to \(4\lfloor X/4\rfloor\) removes at most three Möbius terms, each of absolute value at most \(1\).

- **First lemma:** Mathematically correct.

  From `hSprime p hpS`, \(p\) is prime. If \(p\nmid n\), then:

  \[
  v_p(n)=0,\qquad v_p(pn)=1,
  \]

  because \(p^2\mid pn\iff p\mid n\). For every selected prime \(q\ne p\), coprimality gives

  \[
  q\mid pn\iff q\mid n,\qquad q^2\mid pn\iff q^2\mid n.
  \]

  Hence all other local combs agree. Also

  \[
  \operatorname{Squarefree}(pn)\iff\operatorname{Squarefree}(n)
  \]

  and the prime support merely gains the already-selected prime \(p\), so smoothness is preserved. With both sites below `upper`, the existing single-flip theorem applies.

- **One-prime fibre identity:** Correct, conditionally. For any field \(c\) satisfying \(c(pm)=-c(m)\) when \(p\nmid m\), and vanishing on \(p^2\)-multiples,

  \[
  \sum_{n\le X}c(n)
    =\sum_{\substack{X/p<m\le X\\p\nmid m}}c(m).
  \]

  This is just the partition into complete \(\{m,pm\}\) fibres, stranded parents, and square-hit fibres. It is an exact boundary relocation, not an estimate.

- **Abstract package corollary:** Also formally plausible. For \(a=0,1\), multiplication by \(p\) implements the flip; \(a=2\) supplies the square hit. But it is an arbitrary-label construction, not a physical CRT realization.

- **Defect constant:** A corrected site actually has absolute value at most \(1\). Thus at most three stranded labels give absolute frontier mass at most \(3\). The proposal’s wording “three terms, each in \([-3,3]\)” would only imply \(9\), not \(3\). This is repairable but shows the quantitative chain is not stated carefully.

- **Renewal term:** “B5-composed lower-scale Mertens contributes \(K^{1/2+\varepsilon}\)” is not an unconditional estimate. It assumes the desired lower-scale bound and supplies no contracting coefficient. With no new input this is exactly the D5 renewal-only stall.

- **Numerics:** \(50/1039\approx0.048\) and \(\sqrt{4(1.9\times10^6)}\approx2757\), so the reported arithmetic is fine. The interpretation is not:

  - signed fitted exponent \(0.56\) is larger than the triangle fit \(0.476\), so the observed ratio is a constant-factor amplitude saving, not an observed exponent saving;
  - an asymptotic exponent \(0.55\) would not prove \(K^{1/2+\varepsilon}\) for every \(\varepsilon>0\);
  - a kill threshold of \(0.62\) is therefore far too weak;
  - correlation with \(M\) is neither necessary nor sufficient. High correlation can indicate that \(D\) simply carries the original difficulty.

- **D1:** No direct violation. The pointwise law uses Möbius-specific multiplicativity and square killing, and the claimed final scale does not contradict \(\Omega_\pm(\sqrt x)\).

- **D2/D3/D5:** Violated at the physical-to-multiplicative transport, at the B4 absolute drift charge, and at the renewal-only fallback.

- **D4:** Not escaped. Zeroing complete fibres and naming the joint remainder \(D\) is an index partition with no changed analytic character.

- **D6:** No lane violation appears.

- **D7:** There is a precise lemma and a computation, but the computation tests the physical-cofactor defect while the theorem controls the artificial multiplicative-site defect. It therefore does not falsify or support the claimed formal mechanism.

## REASONING

Even granting the missing bridge exposes the relocation directly. Write the hoped-for identity as

\[
M(4K)=R(K)+D(K)+E(K),
\]

where \(R\) is the renewal term and \(E\ll_\varepsilon K^{1/2+\varepsilon}\). If \(R\) is already known at that scale, then

\[
D(K)=M(4K)-R(K)-E(K).
\]

Consequently,

\[
D\ll_\varepsilon K^{1/2+\varepsilon}
\quad\Longleftrightarrow\quad
M(4K)\ll_\varepsilon K^{1/2+\varepsilon}.
\]

That is exactly the D3(b) same-exponent relocation test. If \(R\) is not already controlled unconditionally, then its proposed control comes from the lower-scale Mertens hypothesis with no demonstrated contraction, reverting to the registered D5 renewal stall. The proposal loses under either interpretation.

The classical analogue is an identity-only sieve/renewal route: \(\mu(pm)=-\mu(m)\) and square killing move parity information onto incomplete fibres, but do not estimate the surviving signed boundary. Classical sieve theory recognizes this as the parity obstruction; successful parity-sensitive sieves require an additional bilinear-form estimate, not merely further exact decomposition. Friedlander and Iwaniec explicitly introduce such extra analytic data to break the classical parity barrier in [“Asymptotic sieve for primes”](https://annals.math.princeton.edu/articles/13036). Here the proposed estimate for \(D(K)\) is precisely that missing parity-sensitive input. The involution does not provide it.

## LEMMA SHIP VERDICT

**SHIP the pointwise lemma, narrowly; do not ship the mechanism claim.**

`correctedPrimeWheelSite_mul_selectedPrime_eq_neg` is correct, clean, μ-specific, and useful as a reusable API theorem. The hypothesis `hn : n ≤ upper` is probably redundant because primality of \(p\) and `p * n ≤ upper` imply it.

Do **not** market the arbitrary `p^a * base(b)` package instantiation as quantitative progress or “physical” discharge. It is true about an engineered site map but disconnected from the actual CRT remainder. A worthwhile next lemma would first define and prove a faithful physical-site bridge; without that, the corollary is mathematically harmless but architecturally misleading.