# Errata draft — target: i1-viability (certification of results/029 audit findings)

Sources corrected: `results/027/mapping_report.md` (027), `IDEAS.md` (I1 entry, lines 314–320),
`results/026/proposals/agent8.json` (agent8). Verification: independent re-derivation plus numeric
spot-checks (exact truncated-hyperbola identity, variance decomposition, canonical-window
geometry/density, R-increment bound) — all in scratchpad `check` run of 2026-08-12.

Verdicts: findings 1, 2 (fatal) CONFIRMED; findings 3, 4, 5, 6 (major) CONFIRMED;
findings 7, 8 (minor) CONFIRMED — both load-bearing, see E-7/E-8; finding 9 (minor) PARTIAL.
No finding refuted.

---

## E-1 (finding 1, fatal, CONFIRMED): the k=1 diagonal is sign-blind and its required bound is RH-equivalent

Independently re-derived. The d=e diagonal of the k=1 Gram expansion,
`D(Y) = Σ_{Y<y≤2Y} Σ_{0≤t≤y} Σ_{d≤y} μ(d)² R(⌊n/d⌋)²` (n = (y+1)²−1−t), is a sum of nonnegative
terms; no signed/spectral device touches it. Size under `θ = sup Re ρ`: for fixed d, ⌊n/d⌋ has
multiplicity ~d, and `Σ_{m≤X} R(m)² ≍ X^{1+2θ}/log²X`, giving `D(Y) ≍ Y^{2+4θ} Σ_{d≤Y} d^{−2θ}`
(`Y⁴/log Y` at θ=1/2). Equivalence `D(Y) ≪ Y^{4+ε} ⟺ RH`: forward is trivial from
`R(u) ≪ u^{1/2+ε}`; converse: D ≥ its d=1 part; the canonical windows `[y²+y, y²+2y]` cover
`[Y²,4Y²]` with density ~1/2 and gaps ~Y (numerically verified: density 0.508, max gap 2Y+1),
and `|R(n+h)−R(n)| ≪ h` (verified: sampled ratio ≤ 0.18), so mapping each gap point to a window
point at distance O(Y) extends the bound to the full dyadic interval with an admissible O(Y⁴)
error; dyadic summation gives `Σ_{n≤X} R(n)² ≪ X^{2+ε}`, which forces θ ≤ 1/2 by the standard
Landau/Ingham Ω-result for the mean square of ψ(t)−t. Scoping (correct in the finding as
written): the equivalence attaches to the diagonal bound that any dispersion/Kuznetsov/spectral
large-sieve implementation must supply after separating `E₂ = D + off-diagonal` — not to the raw
hypothesis `E₂ ≪ Y^{4+ε}` in the abstract.

**Correction to agent8 `obstacle_positions.6`** — wrong sentence:

> "No zero expansion or individual estimate for R is used; in particular the d=1 term is never
> separated from its Möbius convolution partners."

Replacement:

> "No zero expansion appears in the formulation, but every dispersion implementation of the
> ensemble second moment separates the d=e diagonal `Σ_{y,t} Σ_{d≤y} μ(d)²R(⌊n/d⌋)²`, and the
> bound `D(Y) ≪ Y^{4+ε}` that must then be supplied is equivalent to RH. The route is circular
> at the level of required inputs."

**New closed-lane candidate (recommended for boundary/dead_lanes.json, kind: circular):** "Any
canonical-ensemble second-moment attack that separates the d=e diagonal must first prove an
RH-equivalent mean-square bound for π−Li." This closes the whole family of k≥1
canonical-ensemble dispersion proposals in one line.

---

## E-2 (finding 2, fatal, CONFIRMED): the truncated μ*Λ device does not exist as stated; obstacle-9 PASS is wrong

Numerically verified exact identity (machine precision at n up to 12000, several splits K):

`Σ_{d≤K} μ(d)ψ(⌊n/d⌋) = −Σ_{r≤n} μ(r)log r − Σ_{m≤⌊n/K⌋} Λ(m)[M(⌊n/m⌋) − M(K)]`.

With K = y and n ~ y², the omitted complementary half is a Mertens-weighted hyperbola edge over
`m ≤ ⌊n/y⌋` (= y+1 or y+2; the audit wrote `m ≤ y` — off by the two boundary terms m ∈
{y+1, y+2}, immaterial). This is exactly record 025's two-parameter edge. Using `μ*Λ = −μ log`
"once" cancels nothing globally: the identity holds only for complete divisor sums. Second
defect confirmed: R is π−Li-based; Stieltjes conversion through dψ/log u produces
`J(x) = Σ_{p^m≤x} 1/m`, leaving prime-power corrections of termwise size
`Σ_{d≤Y} (Y²/d)^{1/2} ≍ Y^{3/2}` per pin — above the per-pin target `Y^{1+ε}`, so they cannot be
triangle-discarded and remain a second uncontrolled signed Möbius obligation (obligation, not a
proven death — the 029 reviewer's downgrade from a separate fatal is the right call).

**Correction to agent8 `mechanism`** — wrong sentence:

> "Use μ*Λ = −μ log to cancel the zero-frequency contribution globally."

Replacement:

> "The identity μ*Λ = −μ log is available only for the complete divisor convolution; the d-sum
> here is truncated at d ≤ y, and the complementary hyperbola half
> `Σ_{m≤⌊n/y⌋} Λ(m)[M(⌊n/m⌋) − M(y)]` — record 025's two-parameter edge — remains as an
> unresolved signed input. A further prime-power correction family (from converting the π−Li
> error to Λ-form) of termwise size Y^{3/2} per pin must also be carried signed."

**Correction to 027 §2 (cluster E, obstacle 9)** — wrong sentence:

> "9. Renewal edge: PASS. No renewal induction is used."

Replacement:

> "9. Renewal edge: FAIL/UNRESOLVED. The only proposed cancellation device (μ*Λ = −μ log) is
> unavailable for the truncated d ≤ y sum; its complementary half is precisely record 025's
> two-parameter Λ·M hyperbola edge, re-entering the renewal wall."

---

## E-3 (finding 3, major, CONFIRMED): rung-1 label is wrong; implication arithmetic is right

Re-derived independently: excursion mass `H^{2k}·W` with narrow branch `W ~ H/C_y`,
`C_y ~ Y/log Y`, against `E_{2k} ≪ Y^{2k+2+η}` gives `H ≪ Y^{1+(2+η)/(2k+1)}`; k=1 gives
`Y^{5/3+η/3} = x^{5/6+η/6}`. Wide branch `W = y+1` requires `H ≳ Y²/log Y` yet concludes
`H ≪ Y^{1+(1+η)/(2k)}` — contradictory for large Y, hence vacuous. The 027 implication is
correct. The label is not: under the program's own empirical square-root-cancellation law,
`E₂(Y) ≍ Y^{2+4θ}`, so `E₂ ≪ Y^{4+ε}` is an RH-scale hypothesis paying out only `x^{5/6+ε}`
(note RH pointwise already gives `Σ_{d≤y}(x/d)^{1/2+ε} ≍ x^{3/4+ε}` by triangle inequality —
strictly better). Generally `E₂ ≪ Y^{A+ε} ⟹ H ≪ Y^{(A+1)/3+ε}`, so a fixed power saving needs
only A < 5; the honest weakest rung-1 hypothesis is `E₂(Y) ≪ Y^{5−κ}` (model-equivalent to
θ ≤ 3/4 − κ/4, itself far beyond known results).

**Correction to 027 §4.1** — wrong sentences:

> "Rung-1 deliverable:
> `E₂(Y) ≪ε Y^{4+ε}` implies
> `|S(y,(y+1)²−1)| ≪ε Y^{5/3+ε}=x^{5/6+ε}`."

Replacement:

> "Amplification deliverable (correct implication, mislabeled hypothesis): `E₂(Y) ≪ε Y^{4+ε}`
> implies `|S(y,(y+1)²−1)| ≪ε Y^{5/3+ε} = x^{5/6+ε}`; but under the program's empirical
> square-root-cancellation law `E₂(Y) ≍ Y^{2+4θ}`, so `Y^{4+ε}` is an RH-scale hypothesis, not a
> rung-1 statement. The honest rung-1 target is `E₂(Y) ≪ Y^{5−κ}` for some fixed κ > 0, giving
> `|S| ≪ Y^{2−κ/3} = x^{1−κ/6}` (model scale: a zero-free half-plane Re s > 3/4 − κ/4)."

**Correction to IDEAS.md I1** — wrong sentence:

> "Rung-1: E₂(Y) ≪ Y^{4+ε} ⟹ |S| ≪ x^{5/6+ε}."

Replacement:

> "Amplification: E₂(Y) ≪ Y^{A+ε} ⟹ |S| ≪ x^{(A+1)/6+ε}; honest rung-1 form is A = 5−κ
> (A = 4 is RH-scale under the program's empirical law and pays out only x^{5/6+ε})."

**Correction to agent8 `rung1_version`** — the phrase "an unconditional fixed power saving with
δ=1/6−ε" should carry the caveat that the sufficient hypothesis `E₂ ≪ Y^{4+ε}` is itself
RH-strength under the program's measured cancellation law.

---

## E-4 (finding 4, major, CONFIRMED): 027 cluster-E obstacle scores 1 and 6 are too generous

Follows from E-1. The positive energy in the k=1 zero mode is visible before any Poisson step
and is prime-error energy `Σ μ(d)²R(⌊n/d⌋)²`, not Mertens energy.

**Correction to 027 §2 (cluster E, obstacle 1)** — wrong sentence:

> "1. 𝔉-closure: CLAIM. The complete `k=1`, `h=0` term has not been evaluated; it may be
> positive Mertens energy in disguise."

Replacement:

> "1. 𝔉-closure: FAIL for any dispersion implementation. The d=e diagonal
> `Σ_{y,t} Σ_{d≤y} μ(d)²R(⌊n/d⌋)²` is positive prime-error energy (the prime-side twin of the
> closed Mertens-energy class), present before any Poisson step; recombining `Σ_d R(x/d)²`
> positively across d is precisely the closed class."

**Correction to 027 §2 (cluster E, obstacle 6)** — wrong sentence:

> "6. Circularity: PASS at formulation level."

Replacement:

> "6. Circularity: PASS at formulation level, FAIL at the level of required inputs: the diagonal
> bound `D(Y) ≪ Y^{4+ε}` that any dispersion implementation must supply is equivalent to RH
> (see the diagonal RH-equivalence erratum)."

---

## E-5 (finding 5, major, CONFIRMED): conductor vs averaging length; obstacle-4 PASS mis-scoped

Re-derived: for the bulk of coprime pairs d,e ~ Y, q = lcm(d,e) ~ Y², while the y-sum has length
Y. Completing an incomplete quadratic phase sum of length N mod q gains only when N > √q; here
N = Y = √q exactly, so completion returns the trivial bound (√q·polylog ~ Y·polylog). Globally:
~Y² sample points (y,t) against a large-sieve cost of order Q² = Y⁴ at Q = Y² — the family is
under-determined. Polynomial conductors are not the binding constraint.

**Correction to 027 §2 (cluster E, obstacle 4)** — wrong sentence:

> "4. Modulus magnitude: PASS. Conductors are polynomial, although higher moments exceed the
> claimed `Y²` ceiling."

Replacement:

> "4. Modulus magnitude: FAIL as scoped. Conductors are polynomial, but the binding comparison
> is conductor vs averaging length: typical q = lcm(d,e) ~ Y² against a y-sum of length Y puts
> incomplete quadratic sums exactly at the no-saving threshold N = √q, and the large-sieve cost
> Q² = Y⁴ exceeds the Y² ensemble points. Only the thin small-conductor sub-family gains.
> Higher moments additionally exceed the claimed Y² ceiling."

---

## E-6 (finding 6, major, CONFIRMED): the displayed Poisson phase is the output of a step never performed

The summand `R(⌊n/d⌋)` is a prime-jump step function composed with a floor; classical Poisson
requires a smooth weight. An exact discrete Fourier/Vaaler treatment produces prime sums, floor
boundary terms, and a wide frequency spread, and the required boundary-error analysis collides
with the kernel-proved obstacle 8 (no polylog pointwise control of floor jumps). No such
analysis is supplied in agent8 or 027.

**Correction to agent8 `mechanism`** — wrong sentence:

> "Poisson summation in both t and y then exposes phases e(h(y+1)^2/d)"

Replacement:

> "A Poisson/Vaaler treatment in t and y would, in the idealized smooth-weight case, expose
> phases e(h(y+1)²/d); for the actual summand R(⌊n/d⌋) (a prime-jump step function under a
> floor) it also produces prime sums, floor boundary terms, and a wide frequency spread, and
> the boundary-error analysis required is exactly what obstacle 8 forbids controlling
> pointwise. The clean quadratic phase is not currently derived."

---

## E-7 (finding 7, minor, CONFIRMED — load-bearing for §4 ranking rationale): the y-average is orthogonal to the bottleneck

Re-derived: the per-pin hypothesis `Σ_{t≤y}|S(y,x_y−t)|² ≪ Y^{3+ε}` for each y (which sums to
`E₂ ≪ Y^{4+ε}`) yields `H³/C ≪ Y^{3+ε}`, i.e. `H ≪ Y^{4/3+ε} = x^{2/3+ε}` — versus x^{5/6+ε}
from the ensemble form: the ensemble trades "for every y" down to "on average over y" at the
price of 1/6 in the exponent. And y-averaging creates no cancellation in the nonnegative
diagonal. **Correction to 027 §4.1 "Reason for rank"**: append "The y-average buys uniformity
in y at an exponent cost (per-pin same-strength input would give x^{2/3+ε} vs the ensemble's
x^{5/6+ε}) and does not act on the positive diagonal; the new geometry is real but orthogonal
to the binding constraint."

---

## E-8 (finding 8, minor, CONFIRMED — load-bearing for how the D-kill is quoted and for the E kill test): deep-rectangle block is a term, not a lower bound

Verified: the exact orthogonal (variance) decomposition is
`Σ_t |S_y(X−t)|² = (y+1)|S̄_y|² + Σ_t |S_y(X−t) − S̄_y|²` with S̄_y the window mean (checked to
machine precision). The deep-block quantity `H·|Σ_{r≤X−H+1} a(r)|²` is a term of the expanded
Gram form whose cross terms with the moving boundary can cancel it; it is not a lower bound for
the window energy. The D-cluster kill survives on its other leg (Ω_H constant on the deep
rectangle ⟹ no shifted-convolution localization of m−n). **Correction (usage note appended to
027 §1-D and §3 item 1):** "The deep-rectangle block constrains only methods that estimate that
block separately; it must not be quoted as a nonnegative lower bound. The genuinely nonnegative
zero mode is the window-mean form `Σ_{Y<y≤2Y} (y+1)^{-1} |Σ_{t≤y} S(y,x_y−t)|² ≪ Y^{4+ε}`
(RMS window-mean ≪ x^{1/2+ε}); use this form in the E zero-mode kill test."

---

## E-9 (finding 9, minor, PARTIAL): the kill test names the wrong energy — true for agent8.json and IDEAS.md; 027's inventory already partially anticipates it

The positive quantity actually present at k=1 is the prime-error diagonal
`Σ_{y,t} Σ_d μ(d)²R(⌊n/d⌋)²`, algebraically distinct from `Σ M(n)²` and `|Σ μ(n)log n|²`. As
written in agent8 (`kill_test`) and IDEAS.md ("Kill: zero term contains uncancelled positive
Mertens energy"), the test can be passed while the route is dead by E-1: CONFIRMED there.
However, 027 §3 kill-test 4 already adds "or a blockwise absolute prime error", which the
R-diagonal plausibly satisfies — so the finding is overbroad if read against 027. PARTIAL.

**Correction to agent8 `kill_test` and IDEAS.md I1 kill clause** — replace the Mertens-only
trigger with the three-part test:

> "Kill test (restated): (a) exhibit the R-diagonal `Σ_{y,t} Σ_d μ(d)²R(⌊n/d⌋)²` and decide
> whether the method separates it (if separated, the required bound is RH-equivalent — kill);
> (b) exhibit the window-mean zero mode `Σ_y (y+1)^{-1}|Σ_t S(y,x_y−t)|²`; (c) exhibit the
> truncated-convolution complementary edge `Σ_{m≤⌊n/y⌋} Λ(m)[M(⌊n/m⌋)−M(y)]`."

---

## Disposition note for coordinator (from certified findings; matches 029 reviewer recommendation)

I1 should be demoted from "ADVANCE, k=1 gate" to a desk autopsy: (a) the Canonical Ensemble
Amplification Lemma survives intact and is Lean-formalizable exactly as stated (verified); (b)
the exact k=1 Gram identity survives only if written with the R-diagonal, the window-mean DC
term, and the truncated-convolution edge displayed; (c) record the diagonal RH-equivalence as a
closed-lane entry (kind: circular) — it pre-empts the entire k≥1 canonical-ensemble dispersion
family. Two of the certified findings (E-4 area: obstacles 4, 6, 9 for cluster E) are
corrections to record 027's own audit and should increment the caught-informal-error count.
