# Errata draft — target 023-affine-backward (audit 029 certification)

Certifier: independent re-derivation pass, 2026-08-12. All arithmetic below was
re-derived from scratch; numeric spot-checks run in the scratchpad (python3.12).
No repo files touched. Verdict tally: 5 CONFIRMED, 1 PARTIAL, 0 REFUTED.

Source files:
- /mnt/d/Projects/prime-wheel-mobius/results/023/023.md
- /mnt/d/Projects/prime-wheel-mobius/results/023/codex_report.md
- /mnt/d/Projects/prime-wheel-mobius/results/020/020.md
- Merged kernel module read via `git show main:RHLean/Analysis/PrimeSieveLipschitzExcursion.lean`
  (confirms the formalized increment bound is `C*(t+1)`, W = ⌊H/(2C)⌋).

Propagation targets found outside 023 (coordinator: these need the same fixes):
- JOURNAL.md entry 2026-08-09-30 (lines ~542-551)
- results/026/packet.md obstacle 8 (lines ~65-69) — this copy is the worst one; see E2.

---

## E1 — [major, CONFIRMED] Uncapped W ≍ √x / H^{2k+1} headline

**Verified independently.** At the canonical pin x0 = (y+1)^2−1 = y(y+1)+y the
backward frozen-support window is hard-capped at t ≤ y: ⌊(x0−t)/(y+1)⌋ = y for
0 ≤ t ≤ y and drops to y−1 at t = y+1 (checked exhaustively for 2 ≤ y < 500,
zero failures; ⌊√(x0−t)⌋ = y holds out to t = 2y, so every window point is a
genuine Abel-face point). The affine excursion window is (H/2−B_y)/A_y ≈ H/4.
At x = 10^16: H = x^0.55 gives affine window 1.53e8 > cap y+1 = 1e8; H = x^0.5
gives 2.19e7 < cap. So W_eff = min((H/2−B_y)/A_y, y+1) ≍ min(H, √x), and for
pin heights H ≥ x^{1/2+ε} — the heights an RH-contradiction pin must have —
the moment payoff is (H/2)^{2k}·Θ(√x) = H^{2k+1}·Θ(√x/H) ≤ H^{2k+1}·x^{−ε},
not H^{2k+1}. The audit's mitigation is also verified: the per-point bound
|S| ≥ H/2 holds on the whole capped window, so the per-point average
(1/W)Σ|S|^{2k} ≥ (H/2)^{2k} is untouched by the cap at every H. The codex
derivation is internally scoped ("At H ≍ y ≍ √x") and correct as displayed;
the defect is the unscoped 023.md Results bullet and codex's word "intended".

**023.md, Results, third bullet — replace:**

> A backward affine version upgrades the excursion window at canonical pins from
> W ≍ log x to W ≍ √x, recovering the H^{2k+1}-scale moment lower bound
> unconditionally on the increment side.

**with:**

> A backward affine version upgrades the excursion window at canonical pins:
> W_eff = min((H/2−B_y)/A_y, y+1) ≍ min(H, √x), since the backward
> frozen-support window is capped at t ≤ y. At pin height H ≍ √x this gives
> W ≍ H ≍ √x and the H^{2k+1}-scale moment lower bound (H/2)^{2k}·W
> unconditionally on the increment side; at H ≫ √x the cap binds and the
> payoff is (H/2)^{2k}·Θ(√x) = H^{2k+1}·Θ(√x/H). The per-point bound
> |S| ≥ H/2 on the whole capped window — hence the average
> (1/W)Σ_{t<W}|S|^{2k} ≥ (H/2)^{2k} — holds at every H.

**codex_report.md, Q3, the "NEW-BUT-PROVED-HERE [UNCONDITIONAL REDUCTION]"
block conclusion — replace:**

> Thus the intended H^{2k+1}-scale moment lower bound is recovered
> unconditionally on the increment side.

**with:**

> Thus at pin heights H ≍ y ≍ √x the H^{2k+1}-scale moment lower bound is
> recovered unconditionally on the increment side. For H ≫ √x the
> frozen-support cap W ≤ y+1 limits the payoff to (H/2)^{2k}·Θ(√x); only the
> per-point average (1/W)Σ|S|^{2k} ≥ (H/2)^{2k} survives at all heights.

---

## E2 — [major, CONFIRMED] "pointwise polylog is DEAD" without the absolute-majorant qualifier

**Verified independently.** Wigert kills only the absolute floor-Li jump
majorant J(x) = Σ_{d≤K}|Li_*(⌊(x+1)/d⌋) − Li_*(⌊x/d⌋)| (exact divisor sum
over d | x+1, d ≤ K). The actual signed frozen-support increment is
Σ_{d|x+1, d≤K} μ(d)(1_{(x+1)/d prime} − ∫_{(x+1)/d−1}^{(x+1)/d} du/log u),
where μ vanishes off squarefree d and Σ_{d|n}μ(d) = 0 supplies cancellation
the majorant discards. Numeric demonstration: at x+1 = 720720 (Wigert-type,
120 divisors ≤ K) the signed increment is 0.40 while the absolute majorant is
14.0; at x+1 = 831600 the signed increment is 0.017 vs 13.9. codex_report.md
itself marks the signed question OPEN twice (Q1 last paragraph; Q4 kill test
scoped to "the absolute pointwise-polylog claim"); 023.md's headline drops the
qualifier and the unqualified form has propagated.

**023.md, Results, first bullet — replace:**

> **D2: pointwise polylog is DEAD (desk-exact kill).**

**with:**

> **D2: pointwise polylog via the ABSOLUTE floor-jump majorant is DEAD
> (desk-exact kill); the signed increment, which keeps the μ(d)-cancellation,
> remains OPEN.**

**JOURNAL.md, 2026-08-09-30 — replace:**

> Pointwise-polylog Lipschitz is dead (h=1 jump sum = exact divisor sum;
> Wigert extremal kill),

**with:**

> Pointwise-polylog Lipschitz via the absolute floor-jump majorant is dead
> (h=1 absolute jump sum = exact divisor sum; Wigert extremal kill; the signed
> increment stays open),

**results/026/packet.md, obstacle 8 (propagated copy — materially false as
written, flagged beyond the audit's quote) — replace:**

> **Wigert floor-jump (proved this round):** the h=1 increment of the Abel sum
> is EXACTLY a divisor sum over d | x+1; along Wigert extremal integers it
> exceeds every fixed power of log x. Pointwise polylog-smooth control is dead;
> only affine/amortized moduli (slope 2+o(1), intercept √x/log x — both
> kernel-proved) exist.

**with:**

> **Wigert floor-jump (proved this round):** the h=1 ABSOLUTE floor-Li jump
> majorant of the Abel sum is EXACTLY a divisor sum over d | x+1; along Wigert
> extremal integers it exceeds every fixed power of log x. Pointwise
> polylog-smooth control THROUGH ABSOLUTE VALUES is dead; only affine/amortized
> moduli (slope 2+o(1), intercept √x/log x — both kernel-proved) exist on that
> route. A polylog bound on the signed increment, retaining the
> μ(d)-cancellation, is not ruled out.

Rationale for the 026 fix being load-bearing: the packet told ten blind agents
that pointwise smooth control of the Abel sum itself is dead; as written it
suppresses signed pointwise-smoothness routes the program's own bar (signed
mechanisms only) is supposed to protect.

---

## E3 — [minor, CONFIRMED] "yields only W ≍ log x at generic stable pins" is H-normalized

**Verified independently.** W = ⌊H/(2C)⌋ with C = 1 + K/log(y+1) ≈ 2√x/log x,
so W ≈ H·log x/(4√x) — this is ≍ log x only at pin height H ≍ √x. Recomputed
at x = 10^16: H = x^0.55 ⇒ W = 58; H = x^0.60 ⇒ W = 366 (audit said ≈367;
floor gives 366 — immaterial); both far above log x/4 ≈ 9.2 and far below the
cap y = 10^8, and reachable at pins with x0 ≡ 0 (mod y+1) (both kernel
hypotheses satisfied). The audit's scale-free formulation is also correct:
C/A_y ≈ (K/log(y+1))/2 ≈ y/(2 log y) is the window multiplier at every H
until the cap binds.

**codex_report.md, Q3 — replace:**

> Record 020's present formal theorem yields only W ≍ log x at generic stable
> pins and yields W = 0 at canonical square endpoints.

**with:**

> Record 020's present formal theorem yields W = ⌊H/(2C)⌋ ≈ H·log x/(4√x) at
> generic stable pins — ≍ log x at pin height H ≍ √x — and yields W = 0 at
> canonical square endpoints. The affine form multiplies the window by
> C/A_y ≈ y/(2 log y) at every pin height, until the frozen-support cap
> W ≤ y+1 binds.

---

## E4 — [minor, CONFIRMED] τ_{≤K} pairing sentence misses the d = y loss

**Verified independently, exhaustively for 4 ≤ x < 60000 (zero failures):**
with n = x+1, K = ⌊x/(y+1)⌋ ∈ {y−1, y} and √n ∈ (y, y+1], the exact law is
τ_{≤K}(n) = (τ(n)−1)/2 at n = (y+1)^2 (central divisor y+1 lost),
τ(n)/2 − 1 at n = y(y+1) (non-central divisor d = y lost, since K = y−1 there),
and τ(n)/2 otherwise; max |τ_{≤K}(n) − τ(n)/2| = 1. The O(1) conclusion and
every downstream use stand; only the one-line justification is incomplete. The
audit's rejection of the further demand (steer the Wigert sequence around
n = y(y+1), (y+1)^2) is also right — losing one divisor out of
exp((log 2+o(1))log n/loglog n) changes nothing.

**codex_report.md, Q1, second proof — replace:**

> divisor pairing d ↔ n/d supplies half the divisors below √n, with at most
> the central divisor lost.

**with:**

> divisor pairing d ↔ n/d supplies half the divisors below √n; since
> K ∈ {y−1, y} and √n ∈ (y, y+1], at most one divisor is lost — the central
> divisor y+1 at n = (y+1)^2, or the non-central divisor d = y at n = y(y+1)
> (where K = y−1). Exactly: τ_{≤K}(n) = (τ(n)−1)/2, τ(n)/2 − 1, τ(n)/2 in the
> three cases, so the error is at most 1 in absolute value.

---

## E5 — [minor, PARTIAL] "honest uniform replacement" and the zero-intercept alternative

**What is confirmed:** the constants (A_y = 2.0835 at y = 10^3, 2.0313 at
y = 10^8; B_y/√x = 0.054 at x = 10^16); the affine bound strictly dominates
the formalized C·(h+1) bound by exactly 1 + (K−H_K)h/log(y+1) ≥ 1 (the Lean
module's excursion lemma consumes a C·(t+1) bound, so C·(h+1) is the right
comparand); and the zero-intercept bound is valid on frozen support with
x+h < (y+1)^2: |S_y(x+h)−S_y(x)| ≤ h + Σ_{x<n≤x+h} τ_{≤K}(n)/log(y+1)
≤ h·(1 + max_{n≤2x}τ(n)/log(y+1)), via the exact identity
Σ_{d≤K}(⌊(x+h)/d⌋−⌊x/d⌋) = Σ_{x<n≤x+h} τ_{≤K}(n) and the prime-side ≤ h.

**What is corrected (the PARTIAL):** (i) the audit's crossover "only worse
once h ≍ y" is wrong — the crossover is h ≈ K/τ_max(2x) = x^{1/2−o(1)} =
y/x^{o(1)}, and the x^{o(1)} gap is superpolylogarithmic and numerically
large: at x = 10^16 with τ_max(2·10^16) ≈ 4·10^4 the zero-intercept bound is
already worse for h ≳ 3·10^3, four orders of magnitude below y = 10^8. It
remains true that it wins for all h up to any fixed power of log x and loses
at excursion scale h ≍ y. (ii) "overclaims optimality" overreads the record:
"honest" in 023 inherits 020's usage ("honest constant" = not the false O(1)
claim), not an optimality claim. The substantive edit is still worth making:

**023.md, Results, first bullet — replace:**

> and the honest uniform replacement is an AFFINE modulus:

**with:**

> and an honest uniform replacement, chosen for the excursion scale h ≍ y, is
> an AFFINE modulus:

**and append to that bullet:**

> (For short windows a zero-intercept bound is sharper: on frozen support with
> x+h < (y+1)^2, |S_y(x+h) − S_y(x)| ≤ h·(1 + max_{n≤2x}τ(n)/log(y+1)),
> better than the affine form for h ≲ K/τ_max(2x) = x^{1/2−o(1)} and worse at
> h ≍ y; carry whichever is smaller. The intercept B_y is an artifact of the
> "+1 per d" floor step, not a feature of the object.)

---

## E6 — [minor, CONFIRMED] "informal-math error #8" is a scope correction, not a math error

**Verified independently.** 023's mathematics is right and correctly
qualified: Chebyshev alone gives R(y) ≪ y/log y = o(y) (split Li_* at √y),
so one support insertion μ(K+1)R(y+1) is absorbable into the affine intercept
at excursion scale without PNT. But 020's D3 sentence lives inside 020's
polylog-C goal, and under that reading "killing them needs PNT-strength input"
is an understatement rather than an error: no input strength yields a polylog
bound on the standalone insertion, since Littlewood forces
R(t) = Ω_±(√t·logloglog t/log t). The falsity appears only under 023's
excursion-scale reading of "kill" (make the insertion o(y)). Counting this in
the informal-math-error ledger inflates the error-catch statistic used for
calibration.

**023.md, Results, second bullet — replace:**

> **D3: record 020's blanket "needs PNT-strength" is FALSE at excursion scale**
> (informal-math error #8, caught by review channel):

**with:**

> **D3: record 020's blanket "needs PNT-strength" is corrected in scope**: at
> excursion scale (insertion absorbed as o(y)) it is false — elementary
> Chebyshev suffices; under 020's own polylog goal it was instead an
> understatement (no input strength gives polylog: Littlewood forces
> R(t) = Ω_±(√t·logloglog t/log t)). Logged as a scope correction to 020/D3,
> not as informal-math error #8.

**JOURNAL.md, 2026-08-09-30 — replace:**

> Error #8: 020's "D3 needs PNT-strength" false at excursion scale (Chebyshev
> suffices).

**with:**

> Scope correction to 020/D3 (not counted as informal-math error #8): at
> excursion scale Chebyshev suffices, so "needs PNT-strength" is false under
> that reading; under 020's polylog goal it was an understatement (Littlewood
> makes polylog impossible at any input strength). Error ledger stays at 7.

(Coordinator: if the ledger number 8 is referenced elsewhere, renumber or
annotate consistently.)

---

## Cross-reference note (no separate erratum)

Findings E1 and E3 are the same defect class — silent normalization at pin
height H ≍ √x — and the same normalization underlies record 024's
"W ≍ √x window" headline (separate audit target 024; its certifier should
align wording with E1's W_eff = min((H/2−B_y)/A_y, y+1) form).

None of the minors upgrades to major on my reading, but E2's propagated copy
in results/026/packet.md obstacle 8 should be treated with major urgency: it
was the seeding packet shown to ten blind agents and as written it kills
signed routes that are in fact open.
