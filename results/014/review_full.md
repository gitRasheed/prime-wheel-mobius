## 0. Headline

I reproduce 013's decisive inequality — but by a different and, I argue, more accurate route, and I get a **worse** (i.e. more strongly closing) honest ceiling than 013 did. I also found the exact shape of the missing ingredient, verified it numerically, and it is **not** something any large-sieve/dispersion step can supply at H = 1. Verdict at the end: **CONFIRM-CLOSURE at mechanism scope**, with a precisely-named object-scope escape that the program should now take.

---

## 1. My own derivation of the H = 1 exponent flow

### 1.1 Setup and units

Fixed pinned sample x = X_N = N(N+2) ≍ N². Truncation y = ⌊√U_k⌋ ≍ √x (this is the program's own convention, hard-coded in `/mnt/d/Projects/prime-wheel-mobius/results/008/killtest2_report.json` → `framework.conventions`; it is forced by exact reconstruction, see §5.3). Hence the reciprocal range is

  d ≤ K := ⌊x/(y+1)⌋ ≍ x^{1/2},  D = x^δ, δ ∈ (0, 1/2].

With R(t) := π(t) − Li(t) and t_d := ⌊x/d⌋:

  Δ_d(x) = R(t_d) − R(t_{d+1}),  E(x) = Σ_{d≤K} M(d) Δ_d(x),  T_D = Σ_{D<d≤2D} M(d)Δ_d(x).

Inductive input: Σ_{d≤D} M(d)² ≪ D^{1+2σ+ε}, so ‖M‖_{2,(D,2D]} ≪ D^{1/2+σ+ε}. **[algebra from the stated input — agrees with 013 (1)]**

Output convention: a bound |E| ≪ x^{F} feeds back as M(x) ≪ x^{F}, hence σ′ = F. So F is a genuine self-map on exponents. I do **not** dispute this loop's legitimacy.

### 1.2 The two prime-side inputs (named, with status)

**(P1) Trivial interval-length bound [proved inline].** #{p ∈ (x/(d+1), x/d]} ≤ x/d² + 1 and |Li(t_d) − Li(t_{d+1})| ≤ (x/d²)/log(x/d). Hence |Δ_d| ≪ x/d² + 1, unconditionally.

**(P2a) Pointwise RH bound [standard-with-citation].** R(t) ≪ √t log t under RH, so |Δ_d| ≪ √x log x. Combined: |Δ_d| ≪ min(x^{1/2}, x/D²) up to logs, crossing over at δ = 1/4.

**(P2b) Mean-square (Selberg) bound [standard-with-citation + routine discretization].** Under RH, ∫_T^{2T}(ψ(t+h) − ψ(t) − h)² dt ≪ hT log²T for 1 ≤ h ≤ T (Selberg 1943). For d ≍ D the intervals (t_{d+1}, t_d] are **disjoint and tile** (x/2D, x/D], with common length h ≍ x/D² and T ≍ x/D. Discretizing at spacing h converts the integral to the sum over the ≍ D tiles at cost h^{-1}:

  Σ_{D<d≤2D} Δ_d(x)² ≪ (x/D)·log^{O(1)}x.  **(P2b)**

Two things matter here. (i) This is an average **internal to the pinned x** — there is no start-averaging, so declared obstacle 1 is not touched. (ii) It is **not improvable**: Montgomery–Soundararajan (2004) give a matching ≍ h log(T/h) variance, so x/D is the truth up to logs, not a lossy bound. This is the single input 013 never considers, and it is strictly stronger than (P2a): x/D < D·min(x, x²/D⁴) for every D in range.

### 1.3 The four cells

The architecture has exactly two binary choices: which prime-side input, and whether the d-sum is combined **with** or **without** cancellation. That gives four maps. Each is max over δ ∈ (0,1/2] of the block exponent; dyadic recombination over the ≍ log x blocks costs (log x)^{O(1)} ⊂ x^ε because every maximum below is attained at an interior or endpoint vertex of a piecewise-linear function with nonzero slopes on both sides, so the dyadic sum is a geometric series dominated by its peak **[proved inline]**.

**Cell A — no d-cancellation, pointwise Δ.** This is pointwise |M(d)| insertion (obstacle 4). Best value consistent with ‖M‖₂ ≪ D^{1/2+σ}:
 block exponent = δ(1+σ) + min(1/2, 1−2δ); peak at δ = 1/4.
 **G(σ) = 3/4 + σ/4**, fixed point σ = 1.
 (Direct check: Σ_{d≤x^{1/4}} d^σ·x^{1/2} = x^{(1+σ)/4+1/2}; Σ_{d>x^{1/4}} d^σ·x/d² = x^{1+(σ−1)/4}. Both = x^{3/4+σ/4}. G(1) = 1 ✓.)

**Cell B — full square-root cancellation, pointwise Δ.** |T_D| ≈ (Σ_d M(d)²Δ_d²)^{1/2} ≈ D^{1/2+σ}·min(x^{1/2}, x/D²):
 block exponent = δ(1/2+σ) + min(1/2, 1−2δ); peak at **δ = 1/4**.
 **F₀(σ) = 5/8 + σ/4**, fixed point σ = 5/6.

**Cell C — no d-cancellation, mean-square Δ (P2b).** Cauchy–Schwarz in d:
 |T_D| ≤ ‖M‖₂‖Δ‖₂ ≪ D^{1/2+σ}(x/D)^{1/2} = D^σ x^{1/2};
 block exponent = δσ + 1/2, **increasing in δ**, peak at δ = 1/2.
 **F₁(σ) = 1/2 + σ/2**, fixed point **σ = 1**.

**Cell D — full square-root cancellation, mean-square Δ.** Cleanest in Abel coordinates (§3, V3): the main term Σ_{d≤K}μ(d)R(x/d) with square-root cancellation is (Σ_{d≤K}R(x/d)²)^{1/2} ≈ (Σ_d x/d)^{1/2} ≈ x^{1/2+ε}, **σ-free**; all σ-dependence sits in the Abel boundary term M(K)R(y) ≪ K^σ y^{1/2} = x^{1/4+σ/2}.
 **F₂(σ) = max(1/2, 1/4 + σ/2)**, fixed point **σ = 1/2**, attracting from above.

### 1.4 The flow

| cell | d-side | Δ-side | map F(σ) | F(1/2) | fixed point | iterate from σ=1 |
|---|---|---|---|---|---|---|
| A | triangle (pointwise \|M\|) | pointwise | 3/4 + σ/4 | 7/8 | 1 | stuck at 1 |
| B (= 013's) | √-cancellation | pointwise | 5/8 + σ/4 | 3/4 | 5/6 | → 5/6 |
| C (**honest ceiling**) | Cauchy–Schwarz | mean-square | 1/2 + σ/2 | 3/4 | **1** | stuck at 1 |
| D (**unavailable**) | √-cancellation | mean-square | max(1/2, 1/4+σ/2) | 1/2 | **1/2** | → 1/2 ✓ |

Two invariants fall out, and they are the whole verdict:

**Invariant 1 (universal 3/4).** Every cell that does not use cancellation between the Mertens weights and the prime discrepancies satisfies **F(1/2) = 3/4 exactly** — cells A, B and C all hit 3/4 at σ = 1/2, by three different routes. The deficit over the target is exactly 1/4 = the missing √D at the critical range D ≍ √x.

**Invariant 2 (uniform expansion gap).** F(σ) − σ ≥ 1/4 on 0 < σ ≤ 1/2 for A, B and C, with equality at σ = 1/2 in B and C. This reproduces 013's decisive constant exactly.

**Sharper than 013.** Cell C, not cell B, is what the architecture can actually prove (§2.2), and its fixed point is **σ = 1**: F₁(σ) − σ = (1−σ)/2 > 0 for all σ < 1, so the bootstrap does not merely fail to reach 1/2 — it is **strictly repelled toward the trivial exponent from every starting value below 1**. That is precisely the parent's own `self_assessed_risk` ("the loop is neutral — obstacle 4 in L² clothing"), realized, and it is worse than 013's "iterates to 5/6".

---

## 2. Line-by-line comparison with `/mnt/d/Projects/prime-wheel-mobius/results/013/codex_report.md`

**Agree.**
- (1) ‖M‖₂ ≪ D^{1/2+σ}. Same algebra.
- (2) D^{3/2} ↝ D^{1/2+σ} is the only σ-sensitive substitution consistent with the parent's "ℓ²-only" architecture, and D^{3/2} = D^{1/2+σ}|_{σ=1} is the correct calibration of the parent's own loss term.
- (4) F₀(σ) = 5/8 + σ/4 and its fixed point 5/6: **I reproduce this exactly**, from a completely independent route (my Cell B, computed at δ = 1/4 with the honest per-d bound, no QSRD assumed). This is the strongest single confirmation in this review.
- (5) at σ = 1: x^{7/8}. Reproduced.
- (6) H = 1 quadratic completion supplies exactly 1. Trivially true; agree.
- §5 (16)–(18): the parent's own QSRD closes the window only for D ≤ H^{2/3}, i.e. D ≤ N^{1/2} at H = N^{3/4}. Reproduced.
- (25): the corrected conductor bookkeeping leaves D = N uncovered even at H = N. Reproduced.
- Loss ledger: I checked every line and found no error. β ≥ 1 from 012 is correct and 012's Theorem B witness family reproduces (I re-derived a/d − a′/d′ = 1/q for m = qℓ−1, d = (t+1)m, d′ = tm, a = (t+1)ℓ+1, a′ = 1 by hand; the identity is exact and the ℓ-interval length D(t−1)/q² is right).

**Disagree, or find incomplete.**

1. **"At H = 1, the critical reciprocal range is D ≍ N" (013 §2) is wrong.** In 013's own model this follows only because their (3) carries a **D-uniform** prefactor N^{2+ε}. That prefactor asserts |Δ_d| ≪ x^{1/2} for *all* d, which is false by a factor of x^{1/2} at the top of the range: at d ≍ N ≍ √x the reciprocal interval (x/(d+1), x/d] has length ≍ 1, so |Δ_d| = O(1) by (P1). With the honest per-d bound the peak moves to **D ≍ x^{1/4} ≍ √N** (Cell B), or to D ≍ x^{1/2} (Cell C). That 013's δ′ = 1 evaluation returns the same number 5/8 + σ/4 as my δ = 1/4 evaluation is a **parametrization coincidence** (their δ′(1/2+σ)/4 at δ′ = 1 equals my δ(1/2+σ) at δ = 1/4), not a robustness check. Any downstream reasoning that relies on "the critical range is D ≍ N" — including 013's whole §3 conductor computation, which substitutes q ≍ D² at D = N — is standing on that coincidence.

2. **013 never considers the mean-square prime input (P2b), and this changes the ceiling.** 013 charges the Δ-side only pointwise. Selberg's short-interval mean square applies here with no averaging over starts (the reciprocal intervals at fixed x already tile an interval), it is strictly stronger, and it is essentially sharp. Feeding it in gives Cell C: F₁(σ) = 1/2 + σ/2. This is **better than 013's F₀ for σ < 1/2 and worse for σ > 1/2** — the two maps cross exactly at σ = 1/2, where both equal 3/4. So 013's F₀ is neither an upper nor a lower bound on the family; it is one point in a two-dimensional space of variants and its status as "the most favorable version" is not established. My Cell C is the correct closure basis: it has the worse fixed point (1 vs 5/6) *and* it is the one the architecture can actually reach.

3. **013 understates the failure of the parent's windowed claim.** 013 (18) says the parent's window lemma covers only D ≤ H^{2/3}. Stronger and simpler: summing the parent's own QSRD over dyadic D ≤ N gives Σ_r|E|² ≪ (H + N^{3/2})N^{2+ε}, and the Gram target is ≪ H·N^{2+ε}. This requires **H ≥ N^{3/2}**, which is impossible since H ≤ N. So the parent's claim in `target_estimate` ("Summed dyadically over D ≤ N this closes the windowed Gram face for H ≥ N^{3/4}") fails on the parent's own estimate for **every admissible H**, not merely for D > N^{1/2}. This is independent of 012 and of any conductor question.

4. **013 §3–§4 (F_HB = 7/8 + σ/4, F_add = 11/8 + σ/4, +β/4) is arithmetically internally consistent but moot.** I checked (8)–(10): R_HB = (D²+L)/(D+L) with L ≍ N, D ≍ N gives ≍ N, amplitude ×N^{1/2} = x^{1/4}, so +1/4 in the x-exponent. Correct given (3). But the entire branch is conditional on an unproved additive→real-character conversion, and my Cell C closure never routes through Heath–Brown at all, so it survives *any* repair of the conductor/fiber problem. The closure should rest on Cell C, not on F_HB.

5. **Circularity not flagged by 013.** Every map above with a small-d branch uses R(t) ≪ t^{1/2+ε}, i.e. RH, on the prime side. The σ-loop bootstraps the Mertens side only. Since E contains the d = 1 term M(1)Δ₁ = R(⌊x⌋) − R(t₂) with weight 1, **|E| ≪ x^{1/2+ε} literally contains RH for π** — no σ-bootstrap can supply that. If the intended answer is "the C-side cancels it", note that the parent's own QSCL/QSRD are stated for **E alone**, contradicting its `finite_range_deception` position ("the full six-term signed Gram form is kept intact throughout"). That is an internal inconsistency in the parent, independent of everything else. Record 008 settles the exponent question anyway: `c_summary.json` gives |H|/√x ≈ 0.136–0.147, |C|/√x ≈ 0.128–0.150, |E|/√x ≈ 0.105–0.110, and mean|H|/|C| = 1.80–2.54 — C and 2E do **not** cancel, so the signed form buys nothing at exponent level and closing the E-face flow closes the target's flow.

---

## 3. Steel-man pass

Each candidate: what it is, its flow, why it does or does not contract.

**V1 — Selberg mean-square instead of pointwise Δ.** *(the strongest genuine improvement I found)* → Cell C, F₁(σ) = 1/2 + σ/2. Legitimate (internal average, no pinning issue), sharp (Montgomery–Soundararajan). **Does not contract**: fixed point σ = 1, repels from below.

**V2 — square-root cancellation in d** (what the parent's large sieve is *supposed* to deliver) → Cell D, F₂(σ) = max(1/2, 1/4+σ/2), fixed point exactly 1/2, contracting from above (1 → 3/4 → 5/8 → 9/16 → 1/2). **This contracts.** But it is not in the family: see §4.1.

**V3 — partial summation before completion.** Exact identity (I derived it, then verified it exactly at x = 10⁷, residual 0.000e+00):

  **E(x) = Σ_{d≤K} μ(d) R(⌊x/d⌋) − M(K)·R(y),  K = ⌊x/(y+1)⌋, y ≍ √x.**

Triangle inequality on the main term: Σ_{d≤K}|R(x/d)| ≪ √x·√K = x^{3/4} (verified: 62916 = 19.90·√x at x = 10⁷, and √K = 56). Boundary term ≪ K^σ y^{1/2} = x^{1/4+σ/2}. So **F₃(σ) = max(3/4, 1/4+σ/2)**, fixed at 3/4. Beats 013's F₀ at σ = 1 (3/4 vs 7/8) with no machinery at all, but **does not contract below 3/4** — Invariant 1 again.

**V4 — use the windowed H ≥ N^{3/4} result as input to a pointwise deduction.** The only route is a discrete Sobolev/Gallagher step, |f(n)|² ≪ H^{-1}Σ_{r<H}|f(n+r)|² + (Σ_r|f|²)^{1/2}(Σ_r|δf|²)^{1/2}. With Σ_r|f|² ≪ HN^{2+ε} this needs increment scale s ≪ N^{1+ε}/H = N^{1/4} at H = N^{3/4}. But at D ≍ N the endpoints x/d move by ≍ 1 per window step, so T_D changes by Σ_{d≍D}M(d)·O(1), which is ≫ D^{1/2+σ} = N^{1/2+σ} even granting full cancellation — off by at least N^{1/4+σ}. **Dead by a power**, not by a constant. Structurally: E is a rough function of the sample index (008's drift-free window measures mean off-diagonal correlation 0.049, near-independence), so no windowed L² statement upgrades to pointwise. This also disposes of the "prove it for H large, deduce H = 1" hope generally.

**V5 — exploit the fixed sign of the square-moduli locus (008 W2-G2a).** S_sq has exponent 0.43–0.53, decisively fixed negative sign (t = −49 at k = 9), and |S_sq| ≈ 1.42|E|. Fixed sign means *no* internal cancellation, but the locus is sparse: ‖M‖₂ over d = m² ≤ 2D is ≪ (D^{1/2}·D^{2σ})^{1/2} = D^{1/4+σ}, saving D^{1/4} over the full block, which lands the locus at ≍ x^{1/2} — exactly what 008 measured. So the parity locus is **already at target scale and is not the obstruction**; its fixed sign gives no lever on the complement, whose flow is unchanged. Confirms the parent's parity position but yields no exponent.

**V6 — non-dyadic / weighted Cauchy–Schwarz.** Single C–S over the whole range: K^{1/2+σ}(Σ_{d≤K}Δ_d²)^{1/2} = x^{(1/2+σ)/2}·x^{1/2} = x^{3/4+σ/2}, strictly worse than F₁. Weighted C–S with w_d = d^{−a} reduces by duality to the dyadic optimization already performed. **Dyadic is optimal and lossless; no gain available here.**

**V7 — Hölder / higher moments (L⁴ Mertens input).** ‖M‖₄‖Δ‖_{4/3} = D^{1/4+σ}·x^{1/2}D^{−1/4} = D^σ x^{1/2} = Cell C exactly. Both sequences are flat within a dyadic block, so all Hölder exponents coincide. **Robustness check passed: the 1/2 + σ/2 barrier is moment-independent.**

**V8 — Type-II / Vaughan bilinear split of μ, C–S in d₁, large sieve in d₂.** After C–S one needs Σ_{d₁}R(x/(d₁d₂))R(x/(d₁d₂′)) — correlations of prime discrepancies at multiplicatively shifted points. **No available input**; this is a prime-correlation problem, not a Mertens-exponent problem. Not closed by any expansion inequality, but it exits the family (it discards the L² Mertens input entirely). Named as an escape in §4.2.

**V9 — reindex to primes (E = Σ_{y<p≤x} M(⌊x/p⌋) − Li part), C–S over primes.** π(x)^{1/2}(Σ_d M(d)²·x/d²/log)^{1/2} = x^{1/2}·x^{1/4+σ/2} = x^{3/4+σ/2}. **Worse than F₁.**

**V10 — joint bootstrap on a single exponent θ** (using M(x) ≪ x^θ ⟹ ζ(s) ≠ 0 for Re s > θ ⟹ R(t) ≪ t^{θ+ε}, so the prime side bootstraps too — this is the one genuinely new degree of freedom, and 013 misses it). With pointwise Δ: F(θ) = θ + (1−θ)/(2−θ), peak at δ* = (1−θ)/(2−θ); F(1/2) = 5/6. With mean-square Δ: F(θ) = θ + 1/4 for θ ≤ 1/2, peak at δ = 1/2. **Expansion gap exactly 1/4 on (0,1/2], fixed point θ = 1.** The joint loop does not help.

**V11 — tune the truncation y.** With K = x^κ, Cell C gives F(σ) = κσ + 1/2, fixed point σ = 1/(2(1−κ)). This equals 1/2 only as κ → 0, and equals 1 exactly at κ = 1/2 — the actual value. So the family's single free parameter sits precisely at the boundary case, and moving it is blocked by the **declared regime-gap obstacle** (exact reconstruction requires y ≍ √x; the completable-wheel cutoff y ≍ log x is separated by a gap exponential in π(y)). **No lever.**

**V12 — wheel/primorial phase, torus-modulus Gauss-sum gains.** Killed upstream: record 006's modulus-magnitude obstacle (Q_k/6U_k between 10^{5.9} and 10^{12835}) forbids √Q_k gains, and 008 W2-G1 found packet amplitude P_q(X) exactly q-periodic in X at pinned samples, so there is no X-dependence to harvest. No d-cancellation source here.

---

## 4. Why the contracting cell is unreachable

### 4.1 The structural lemma

At H = 1 the averaging family has **size 1**. A large sieve is an inequality of the form Σ_{ν ∈ family}|Σ_m a_m φ_ν(m)|² ≪ (cost)·Σ|a_m|²; to invoke it with the reciprocal index d as the family variable, d must first be moved to the *outside* of a square — and the only move that does this is a Cauchy–Schwarz that has already discarded the sign information in the M(d) weights. Hence:

> **At H = 1, every large-sieve or completion step in this architecture is downstream of a Cauchy–Schwarz that has already destroyed d-cancellation.** The best conceivable output is therefore ‖M‖₂ × ‖Δ‖₂ = Cell C, and both factors are at their true sizes (‖M‖₂ by the inductive input; ‖Δ‖₂ by Montgomery–Soundararajan sharpness). The ceiling F₁(σ) = 1/2 + σ/2 is not an artifact of a lossy estimate — it is attained.

013 saw half of this (its (6): the H = 1 quadratic phase sum is exactly 1). The other half — that no repaired large sieve can re-supply the lost cancellation — is what actually closes the angle, and it is independent of 012's fiber failure and of the conductor scale.

### 4.2 Numerical corroboration (my own run, `x = 10⁷`, exact integer π and M; li by series; scripts under the scratchpad)

Per dyadic block, comparing the C–S bound ‖M‖₂‖Δ‖₂ against the √-cancellation size (Σ_d M²Δ²)^{1/2}:

| D | (Σ M²Δ²)^{1/2} | ‖M‖₂‖Δ‖₂ | ratio | √D |
|---:|---:|---:|---:|---:|
| 128 | 83.3 | 1164 | 14.0 | 11.3 |
| 256 | 116.7 | 1874 | 16.1 | 16.0 |
| 512 | 107.0 | 2198 | 20.5 | 22.6 |
| 1024 | 130.5 | 4200 | 32.2 | 32.0 |
| 2048 (1114 terms) | 132.5 | 4545 | 34.3 | 33.4 |

**The Cauchy–Schwarz split loses exactly √D.** Further: (Σ M²Δ²)^{1/2} is **flat in D** (83–133 across five dyadic scales), which is Cell D's σ-free x^{1/2} prediction; while ‖M‖₂‖Δ‖₂ **increases monotonically to the top block** (214, 51, 201, 438, 504, 681, 867, 1164, 1874, 2198, 4200, 4545), which is Cell C's prediction that the peak sits at δ = 1/2. Both structural predictions of my derivation confirmed, and the deficit √D_max = x^{1/4} is exactly Invariant 1's 3/4 − 1/2.

Independently, record 008's own arrays already contain the decisive datum and it was not read this way: `Diag(x) = Σ_d M(d)²Δ_d²` has pooled exponent 0.931 and `slope_log_absE` is 0.477–0.528, so **|E| ≍ √Diag** — the reciprocal family genuinely exhibits square-root cancellation. (At k = 9, n = 14936: |E| = 1379 vs √Diag = 1317.) Also `absE_over_sum_d_abs_M(d)Delta_d` falls 0.0876 → 0.0247 across k = 6…9, i.e. the triangle-inequality loss grows as a power of x. Numerics never promote (obstacle 6), and this is exactly the finite-range regime that deceived before — but it locates the failure: **the truth is in Cell D and the mechanism can only prove Cell C.**

---

## 5. VERDICT

### **CONFIRM-CLOSURE**, at mechanism scope, on a corrected and strictly stronger basis than 013's.

**Closure statement.** Let 𝔉 be the class of arguments that (i) take as their only Mertens input the L² hypothesis Σ_{d≤D}M(d)² ≪ D^{1+2σ+ε}, (ii) take as prime-side input any per-interval or mean-square bound on Δ_d no stronger than the RH/Selberg-sharp ones (P1)/(P2a)/(P2b), and (iii) recombine over the reciprocal index d by Cauchy–Schwarz, Hölder, or the triangle inequality — which, by §4.1, includes every completion + large-sieve implementation at H = 1, repaired or not. Then for every member of 𝔉 the pointwise self-map satisfies

  **F(σ) ≥ 1/2 + σ/2, hence F(σ) − σ ≥ (1−σ)/2 ≥ 1/4 on 0 < σ ≤ 1/2, and F(1/2) = 3/4 exactly.**

No member of 𝔉 has a fixed point at or below 1/2; the honest ceiling's only fixed point is σ = 1, and it is attracting from below, so the bootstrap cannot leave the trivial exponent in either direction. This closure is **independent of record 012** (it never uses the fiber map), **independent of the conductor scale** (it never invokes Heath–Brown), and **independent of the completion coefficients** (it never completes). It therefore survives every repair to the mechanism 012 killed. The class's single free parameter, the truncation exponent κ with K = x^κ, gives fixed point 1/(2(1−κ)) > 1/2 for every κ > 0 and is pinned at κ = 1/2 by the declared regime-gap obstacle.

**013's verdict NEUTRAL-OR-EXPANDS stands, and its decisive constant 1/4 is exactly right** — I reach it three separate ways. Its map F₀ = 5/8 + σ/4 and fixed point 5/6 are correctly computed *for their cell* and I reproduce them; but F₀ is not the family's ceiling and the claim "the critical reciprocal range is D ≍ N" is wrong. Adopt Cell C as the closure basis.

**What is NOT closed** (state this in the record so the closure is not over-read as "G2 is dead"):
1. **Cell D / the Abel main term.** Any argument supplying cancellation *between* μ and the prime discrepancies — |Σ_{d≤K}μ(d)R(x/d)| ≪ x^{1/2+ε} — escapes, reaches exactly 1/2, and is empirically true. It is outside 𝔉 by construction (it uses no Mertens exponent at all), and no dispersion or large-sieve step at H = 1 can produce it.
2. **V8: bilinear/Type-II decompositions of μ against R at multiplicatively shifted reciprocal points.** These leave 𝔉 (they discard the L² input). They are blocked by a *missing prime-correlation estimate*, not by an expansion inequality. This door is untouched by this review.
3. The parent's restricted windowed lemma for D ≤ H^{2/3} remains a coherent (still unproven, and per 012 mechanism-broken) statement; only the claim that it sums to close the full window is refuted — and it fails for every H ≤ N, not just for D > N^{1/2}.

### What to attack next

Change coordinates before changing mechanisms. The exact, kernel-checkable identity **E(x) = Σ_{d≤K} μ(d)R(⌊x/d⌋) − M(K)R(y)** with K ≍ y ≍ √x (verified here to zero residual) dissolves the entire σ-bootstrap: in these coordinates the boundary term is M(√x)·R(√x) ≪ x^{1/4+ε}·x^{1/4+ε} = x^{1/2+ε} under the induction hypothesis at half scale — **exactly self-consistent at 1/2, with no exponent flow and no loss** — so the target |E| ≪ x^{1/2+ε} is equivalent to the single bilinear statement Σ_{d≤√x} μ(d)(π(x/d) − Li(x/d)) ≪ x^{1/2+ε}, and the whole σ-loop that 005/013 spent themselves on turns out to be an artifact of where the Cauchy–Schwarz was placed. That is the object to attack, and the right next moves on it are (a) formalize the Abel identity in Lean against the existing E-face so the reformulation is kernel-grade rather than my arithmetic, (b) re-run 008's W2-G2b arbiter in Abel coordinates — the discriminating question is no longer "are the dyadic blocks correlated" but "does Σ_{d≤K}μ(d)R(x/d) exhibit √K cancellation as K grows at fixed x", which is a clean one-parameter measurement the current arrays can answer, and (c) scope a Type-II (V8) angle whose declared missing ingredient is an honest prime-correlation input at multiplicative shifts, stated as such, rather than a manufactured modulus family — since 012 has now shown that manufacturing one from the quadratic sampling does not work, and this review shows that even a working one would not have helped.