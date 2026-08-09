# Record 021 adversarial report

Inputs: [021 declaration](/mnt/d/Projects/prime-wheel-mobius/results/021/021.md), [018/K2](/mnt/d/Projects/prime-wheel-mobius/results/018/018.md), [017 obstacle packet](/mnt/d/Projects/prime-wheel-mobius/results/017/packet.md).

## Q1 — inference chain

Notation: \(S(x,K)=\sum_{d\le K}\mu(d)R(\lfloor x/d\rfloor)\), \(K\asymp\sqrt x\), and
\[
G_{x,K}(\rho)=\sum_{d\le K}\mu(d)\operatorname{Li}_{*}\!\left((x/d)^\rho\right),
\]
with the conjugate-symmetric branch used in K2.

| Step | Status | Finding |
|---|---|---|
| Replace \(R(\lfloor x/d\rfloor)\) by the midpoint/smooth explicit-formula convention at \(x/d\). | STANDARD | The Li floor correction is \(O(K/\log x)\); jump/midpoint corrections are \(O(K)\). Both are \(O(\sqrt x)\). |
| Apply the Riemann explicit formula for \(J(t)\), then Möbius-invert \(J\) to \(\pi\). | STANDARD | This gives \(S(x,K)=-2\Re\sum_{0<\gamma\le T}G_{x,K}(\rho)+C_{x,K}+E_T(x,K)\), where \(C_{x,K}\) is the prime-power/archimedean remainder. |
| Obtain a uniform sharp-cutoff truncation with \(T\asymp x^2\) and \(E_T(x,K)\ll\sqrt x\,\log^{O(1)}x\). | NONTRIVIAL-BUT-KNOWN | Standard explicit-formula machinery, but it must be written with midpoint corrections and uniformity over \(x/d\ge x^{1/2+O(1)}\). It is not supplied by record 018. |
| Replace \(G_{x,K}(\rho)\) by \(x^\rho F_K(\rho)/(\rho\log x)\). | FALSE | Actually \(\operatorname{Li}_{*}((x/d)^\rho)\sim x^\rho d^{-\rho}/[\rho(\log x-\log d)]\). Since \(d\le K\asymp\sqrt x\), the denominator varies by a constant factor. Control requires the log-weighted polynomial \(\sum\mu(d)d^{-\rho}/(1-\log d/\log x)\), uniformly controlled partial polynomials, or \(G\) itself. \(F_K(\rho)\) alone does not control it. |
| Use \(\sum |F_K(\rho)|/|\rho|\ll\operatorname{polylog}\) to bound the zero contribution by \(x^{1/2}\operatorname{polylog}\), unconditionally. | FALSE | Here is the exact \(\sup\beta\) failure: \(x^\rho=x^\beta e^{i\gamma\log x}\). The actual normalized cost is \(x^{\beta-1/2}|F|/|\rho|\). An unweighted all-zero moment yields at best \(x^{\Theta(T)-1/2}\operatorname{polylog}\), where \(\Theta(T)=\sup_{0<\gamma\le T}\beta\). A line-only moment silently assumes away every off-line zero. |
| Repair \(\sup\beta\) using ordinary zero-density estimates. | FALSE | A single fixed zero \(\beta=1/2+\delta\) contributes \(x^\delta\) for arbitrarily large \(x\). Density bounds control how many such zeros exist, not the cost of one persistent zero. |
| Repair \(\sup\beta\) by contradiction. | OPEN | Logically valid only if the gate sums over all zeros with the \(x^{\beta-1/2}\) weight and is proved unconditionally. Assuming an off-line zero would then violate the gate or, more generally, the gate gives the Abel target and the kernel bridge gives RH. Any invocation of RH, line-only enumeration, or an RH-strength prime bound inside this proof is circular. |
| Bound the prime-power remainder \(C_{x,K}\) using the proposed zero moment. | FALSE | The first omitted term is the \(m=2\) prime-power term: \(-\frac12\sum_{d\le K}\mu(d)\operatorname{Li}(\sqrt{x/d})\), whose leading form is \(-\sqrt x\,F^{\log}_{K,x}(1/2)/\log x\). The proposed moment at nontrivial zeros contains no information about \(F_K(1/2)\). Higher \(m\) contribute \(F_K(1/m)\) and zero harmonics \(F_K(\rho/m)\). |
| Prove \(C_{x,K}\ll x^{1/2}\operatorname{polylog}x\) separately. | OPEN | At \(m=2\), this already demands RH-scale cancellation in a Möbius polynomial at \(s=1/2\). It is not an elementary secondary error. |
| Assume the repaired exact-zero-plus-secondary gate in Q2. | STANDARD | Triangle inequality in the explicit formula gives \(S(x,K)\ll\sqrt x\,\log^{O(1)}x\), hence \(S(x,K)\ll_\varepsilon x^{1/2+\varepsilon}\). |
| Abel target implies RH. | STANDARD | Kernel-verified program fact supplied in the declaration. |

Q1 verdict: the record-018 inference chain is false in two independent places: off-line zeros and the prime-power remainder. It becomes coherent only after replacing the \(F_K\)-only moment by the exact all-zero-plus-secondary gate below.

The K2 numerics probed only the conditional critical-line main-zero term. They did not probe \(\beta>1/2\), and they measured rather than bounded \(C_{x,K}\). In the four pinned samples, \(|C_{x,K}|/\sqrt x\) was \(0.116,0.121,0.082,0.025\); this is illustrative only.

## Q2 — frozen repaired gate

Fix constants \(0<\kappa_-<\kappa_+<\infty\) corresponding to \(K\asymp\sqrt x\). Let \(C_0(t)\) be the exact prime-power plus archimedean term in the repo-normalized formula
\(\pi_0(t)-\operatorname{Li}(t)=-2\Re\sum_{\gamma>0}\operatorname{Li}_{*}(t^\rho)+C_0(t)\), and set \(C_{x,K}=\sum_{d\le K}\mu(d)C_0(x/d)\).

**Frozen gate Z-repaired:**
\[
\boxed{\quad
\exists\,A,C,x_0\ \ \forall x\in\mathbb N,\ x\ge x_0\ \ \forall K\in\mathbb N,\ 
\kappa_-\sqrt x\le K\le\kappa_+\sqrt x\ \ \forall T,\ x^2\le T\le2x^2:\quad
x^{-1/2}|C_{x,K}|+
2x^{-1/2}\!\!\sum_{\substack{\zeta(\rho)=0\\0<\Im\rho\le T}}
\left|\sum_{d\le K}\mu(d)\operatorname{Li}_{*}\!\left((x/d)^\rho\right)\right|
\le C(\log x)^A .
\quad}
\]

Zeros are counted with multiplicity. The effective zero weight is \(x^{\beta-1/2}/|\rho|\), with the required \(d\)-dependent logarithmic kernel retained exactly.

Required polylog power: any fixed finite \(A\) suffices. The logically weakest gate is therefore \(\exists A\), not \(A=3\). Freezing \(A=3\) would promote the K2 fit into an unsupported asymptotic guess.

The original inequality \(\sum|F_K(\rho)|/|\rho|\ll\operatorname{polylog}\) is not a valid gate for the stated \(\pi-\mathrm{Li}\) target.

## Q3 — literature verdict

| Statement | Conditional on | Strength versus frozen gate |
|---|---|---|
| Landau–Gonek: uniformly in \(X,T\), \(\sum_{0<\gamma\le T}X^\rho=-T\Lambda(X)/(2\pi)+\) explicit errors. For \(X=d^{-1}<1\), the main coefficient becomes \(-T\Lambda(d)/(2\pi d)\). | Uniform theorem unconditional; the phase-only form \(\sum X^{i\gamma}\) is normally stated under RH. | Signed, coefficient-wise information only. Summing with \(\mu(d)\) produces a main term of order \(T\sum_{p\le K}\log p/p\asymp T\log K\). It gives no absolute moment, no \(x^{\beta-1/2}\) control, and no \(C_{x,K}\). See Gonek, *An explicit formula of Landau…* (Contemp. Math. 143, 1993); a modern statement is recorded in the [Landau–Gonek discussion](https://arxiv.org/abs/2601.18025). |
| \(J_{-1}(T)=\sum_{0<\gamma\le T}|\zeta'(\rho)|^{-2}\ll T\). | Conjectural; simplicity implicit. Ng additionally assumes RH. | Ng does not prove this bound. Under RH plus this hypothesis he proves \(M(x)\ll\sqrt x(\log x)^{3/2}\), weak Mertens, and limiting-distribution results. It is not an unconditional route to the gate. [Ng 2004](https://arxiv.org/abs/math/0310381). |
| Gonek conjecture \(J_{-1}(T)\sim 3T/\pi^3\). | RH and simple zeros. | Conjectural and already assumes away the \(\beta\)-problem. A further nontrivial transfer from \(1/\zeta'(\rho)\) to the length-\(K\) polynomials is required. It does not directly bound the log-weighted \(G_{x,K}\) or the prime-power remainder. [Milinovich–Ng](https://arxiv.org/abs/1106.1160). |
| Known lower bound \(J_{-1}(T)\gg T\). | RH and simple zeros. | Wrong direction; no gate implication. [Milinovich–Ng](https://arxiv.org/abs/1106.1160). |
| Modern negative-moment upper bounds on selected zero subfamilies. | Conditional hypotheses; restricted subfamilies expected to have near-full density. | Exceptional zeros are fatal for an absolute all-zero gate. Does not reach \(J_{-1}\) over all zeros. [Bui–Florea–Milinovich 2024](https://arxiv.org/abs/2310.03949). |
| Large-sieve/discrete mean values at zeros for a Dirichlet polynomial \(A\). | Often RH for evaluation exactly at \(\rho=1/2+i\gamma\); otherwise applicable to separated ordinates rather than an all-zero \(\beta\)-weighted family. | Gives roughly \((T+K)\log^{O(1)}T\sum|a_n|^2\). With \(a_n=\mu(n)n^{-1/2}\), this can make high dyadic ranges polylogarithmic after Cauchy–Schwarz, but ranges \(T\ll K\), fixed low zeros, off-line weights, and \(C_{x,K}\) remain. The discrete theorem used in current negative-moment work is described in [Bui–Florea–Milinovich](https://arxiv.org/abs/2310.03949). |
| Montgomery–Vaughan continuous mean value: \(\int_0^T|\sum_{n\le K}a_nn^{-it}|^2dt\ll(T+K)\sum|a_n|^2\). | Unconditional on a vertical line. | Continuous average, not values at every zero. Sampling costs local zero density; Cauchy–Schwarz discards the required exceptional-zero and secondary-term structure. [Montgomery–Vaughan, *The large sieve*](https://londmathsoc.onlinelibrary.wiley.com/doi/pdf/10.1112/S0025579300004708). |
| Mollifier mean values plus zero density, using \(M_K(s)=\sum_{n\le K}\mu(n)n^{-s}\). | Unconditional density estimates. | These count off-line zeros; they do not pay \(x^{\beta-1/2}|M_K(\rho)|\). One fixed off-line zero remains fatal. The standard mollifier setup is explicit in [Kadiri–Lumley–Ng](https://www.cs.uleth.ca/~kadiri/articles/Explicit-zero-density-for-the-Riemann-zeta-function-JMAA-May2018.pdf). |
| Modern large-value/zero-density bounds, e.g. \(N(\sigma,T)\le T^{30(1-\sigma)/13+o(1)}\). | Unconditional. | Still only density. Cannot uniformly suppress \(x^{\beta-1/2}\) from a fixed zero as \(x\to\infty\). [Guth–Maynard](https://arxiv.org/abs/2405.20552). |

Literature verdict:

- No verbatim-known theorem proves the repaired gate.
- No cited theorem proves the original \(F_K\)-moment unconditionally.
- No known result makes the repaired gate known-false.
- The claim that Ng’s \(J_{-1}\) work supplies an unconditional gate is FALSE.
- Landau–Gonek supplies signed first moments, not the required absolute moment.

## Q4 — seven-obstacle audit

| Obstacle | Position |
|---|---|
| 1. \(\mathfrak F\)-closure | Not automatically escaped. The gate keeps \(\mu\) inside \(G_{x,K}\), but proving it by squaring and applying generic Cauchy–Schwarz produces \(d,d'\) energies and discards the \(\mu\times R\) interaction. High-zero ranges may be handled this way, but low zeros and \(C_{x,K}\) return to RH-scale Mertens control. A pure second-moment proof re-enters the zero-coordinate shadow of \(\mathfrak F\). |
| 2. Fiber growth | No pair-to-modulus transfer is used. If \(|F|^2\) is expanded, no bounded-fiber or small-conductor claim may be imported; record 012’s counterexample remains binding. |
| 3. Pinned vs averaged | Repaired gate is uniform in every admissible \(x,K\), so it addresses the obstacle by formulation. An average over \(x\), \(K\), or translations is insufficient. |
| 4. Modulus magnitude | Avoided: the route uses zeta zeros and ordinary Dirichlet polynomials, not the full wheel modulus. |
| 5. Parity | Not a sieve-only route, so the classical parity theorem does not directly kill it. The prime-power remainder nevertheless exposes unsolved linear Möbius cancellation; parity has not been converted into leverage. |
| 6. Circularity | Critical. “Sum over \(\rho=1/2+i\gamma\)” is already an RH assumption unless explicitly restricted to zeros known to be on the line, in which case off-line zeros remain missing. Ng/Gonek \(J_{-1}\) inputs are conditional on RH. The only admissible contradiction structure is: formulate the gate over all zeros, prove it without RH-strength pointwise inputs, then derive the target/RH. |
| 7. Finite-range deception | K2 used the first 5000 line zeros, \(T_{\max}=5447.86\), \(x\le10^9\), whereas the frozen truncation range is \(T\asymp x^2\). It is silent about off-line zeros and proves nothing about the asymptotic prime-power remainder. It only falsified “large inter-zero cancellation is already forced in this range.” |

## Q5 — cheapest kill test and rung 0

Cheapest kill test: desk expansion of the \(m=2\) term in Möbius inversion from \(J\) to \(\pi\).

1. Write \(\pi(t)=J(t)+\sum_{m\ge2}\mu(m)J(t^{1/m})/m\).
2. Insert into \(S(x,K)\).
3. The \(m=2\) contribution is \(-\frac12\sum_{d\le K}\mu(d)J(\sqrt{x/d})\), with leading term \(-\sqrt x\,F^{\log}_{K,x}(1/2)/\log x\).
4. Check the proposed moment: it contains only \(F_K(\rho)\) at nontrivial zeros and supplies no bound for \(F^{\log}_{K,x}(1/2)\).

Result: the original record-018 gate fails before any numerical experiment. This is an exact structural kill, not a heuristic.

Secondary desk check: Landau–Gonek plus partial summation gives a signed lower scale \(\sum_{\gamma\le T}F_K(\rho)/\gamma\asymp\log K\log T\) when \(T\) dominates the coefficientwise errors. Hence an \(F_K\)-proxy with polylog exponent \(A<2\) is untenable; “polylog” cannot mean \(O(1)\) or \(O(\log x)\).

Honest rung-0 deliverable: for the left side \(\mathscr M(x,K,T)\) of the repaired gate, prove unconditionally and uniformly
\[
\mathscr M(x,K,T)=o(x^{1/2}).
\]
The explicit formula then gives \(S(x,K)=o(x)\). This is strictly weaker than polylogarithmic control but is a genuine PNT-strength entrant. A bound \(\mathscr M\ll x^{1/4-\delta}\) would instead give \(S\ll x^{3/4-\delta}\), a rung-1 power saving.

## Final verdict

**FORMULATES-WITH-REPAIR.** The record-018 gate is not a coherent sufficient condition: it suppresses \(x^{\beta-1/2}\), replaces a log-weighted zero amplitude by \(F_K(\rho)\) without justification, and omits the prime-power remainder whose first term already contains \(F_K(1/2)\). Cluster Z survives only as the exact all-zero-plus-secondary gate in Q2. That repaired statement is unconditional in formulation, explicitly RH-strength, open, and substantially broader than an “Ng-line \(J_{-1}\) moment.”

Codex session ID: 019fe7ef-4d6f-7630-b887-98a37c7b1ce8
Resume in Codex: codex resume 019fe7ef-4d6f-7630-b887-98a37c7b1ce8
