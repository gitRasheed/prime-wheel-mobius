# Record 034 — PNT boundary scoping diagnostic

Desk-only, read-only. Upstream = mobius-synthesis origin/main (fetched
2026-08-12). All upstream code read via `git show origin/main:<path>` /
`git grep ... origin/main`; no working-tree files touched. Our-side context:
results/030 certified corrections (two-obligation target: bound S AND bound
M(K)·R(y)) and results/030/errata/errata_021-z-gate.md (truncation clause
E_T for the corrected Z-gate).

Notation. Kernel identity (hypothesis-free, upstream
RHLean/Analysis/PrimeSieveAbelIdentity.lean:188 on origin/main,
`primeSievePNTError_eq_moebiusDiscrepancySum_sub_abelBoundary`):
E(y,x) = S(y,x) − P(y,x), where S = `primeSieveMoebiusDiscrepancySum y x`
= Σ_{d ≤ K} μ(d)·R(⌊x/d⌋), P = `primeSieveAbelBoundary y x` = M(K)·R(y),
K = ⌊x/(y+1)⌋, R(t) = `primeSievePrimeDiscrepancy t` = π(t) −
`logarithmicIntegralFromTwo` t, M = `mertensSummatory`.

NAME-COLLISION WARNING (load-bearing for any PR): upstream's new
`nativePNTError (N : ℕ) : ℝ := nativePsi N − N`
(NativePNTErrorMass.lean:28) is the CHEBYSHEV error ψ(N)−N; it is a
different object from the prime-sieve `primeSievePNTError (y x : ℕ) : ℂ`
in the Abel identity. Any bridging module must keep the two apart
explicitly.

---

## Q1 — INVENTORY

### Modules (20, `git ls-tree origin/main`, all under RHLean/Analysis/)

NativePNTAxer, NativePNTChebyshev, NativePNTErdosContraction,
NativePNTErrorMass, NativePNTLogSums, NativePNTMertens,
NativePNTMobiusMoments, NativePNTMobiusSecondMoment,
NativePNTQuantitativeStatements, NativePNTSelberg,
NativePNTSquarePrefixCompensated, NativePNTSquarePrefixContraction,
NativePNTSquarePrefixCubic, NativePNTSquarePrefixGoodMass,
NativePNTSquarePrefixGoodMassRate, NativePNTSquarePrefixMobiusError,
NativePNTSquarePrefixPNT, NativePNTSquarePrefixTransfer,
NativePNTSummatorySelberg, NativePNTTransfer.

Import spine (verified, no NativePNT module imports any PrimeSieve module):
Chebyshev → Selberg/Mertens → ErrorMass → ErdosContraction →
{Axer, Transfer, SquarePrefix* → SquarePrefixCubic → SquarePrefixPNT →
SquarePrefixTransfer} → QuantitativeStatements.

### The headline theorem (SUPPLIED — verbatim,
NativePNTSquarePrefixTransfer.lean:305-313)

```lean
/-- **Fully wired square-prefix Möbius Prime Number Theorem:**
`pi(N) log N / N -> 1`, with the asymptotic input coming from the fully
rederived square-prefix reciprocal-fibre architecture. -/
theorem nativePNTSquarePrefixPrimeNumberTheorem :
    Tendsto
      (fun N : ℕ =>
        (Nat.primeCounting N : ℝ) * Real.log (N : ℝ) / (N : ℝ))
      atTop (𝓝 1) :=
  nativePrimeNumberTheorem_of_theta_div_atTop_one
    nativePNTSquarePrefixTheta_div_atTop_one
```

Note the form: π(N)·log N / N → 1. A qualitative Filter.Tendsto limit — no
rate, no error term, and stated against N/log N, NOT against Li.

### The ψ(N)−N envelope theorems (SUPPLIED — verbatim)

Definition (NativePNTErdosContraction.lean:1831):

```lean
/-- An affine global envelope for the Chebyshev error. ... -/
def nativePNTHasAffineEnvelope (alpha : ℝ) : Prop :=
  ∃ D : ℝ, 0 ≤ D ∧ ∀ N : ℕ,
    |nativePNTError N| ≤ alpha * (N : ℝ) + D
```

with `nativePNTError N = nativePsi N − N`, `nativePsi x = Σ_{n∈Icc 1 x} Λ n`
(LogWeightedPrimeExtensionEndpoint.lean:61).

Base envelope: `nativePNTHasAffineEnvelope_six : nativePNTHasAffineEnvelope 6`
(elementary Chebyshev, via `nativePNTError_abs_le_const_mul`).

Cubic slope-decay step (NativePNTSquarePrefixCubic.lean:25, C =
`nativePNTSquarePrefixRederivedCubicConstant` = 1/1140480000):

```lean
theorem nativePNTSquarePrefixRederivedHasAffineEnvelope_cubic_step
    (alpha : ℝ) (halpha : 0 < alpha) (halpha6 : alpha ≤ 6)
    (henv : nativePNTHasAffineEnvelope alpha) :
    nativePNTHasAffineEnvelope
      (alpha - nativePNTSquarePrefixRederivedCubicConstant * alpha ^ 3)
```

iterated through the explicit budget
`nativePNTSquarePrefixFullIterationBudget eta = ⌊6/(C·eta³)⌋₊ + 1`
(≈ 6.8·10⁹/η³ steps) to give the envelope-family theorem
(NativePNTSquarePrefixPNT.lean):

```lean
theorem nativePNTSquarePrefixHasAffineEnvelope_arbitrarily_small
    (eta : ℝ) (heta : 0 < eta) :
    nativePNTHasAffineEnvelope eta
```

and hence `nativePNTSquarePrefixPNTError_abs_div_atTop_zero`
(|ψ(N)−N|/N → 0), `nativePNTSquarePrefixPsi_div_atTop_one` (ψ(N)/N → 1).
Crucial rate caveat: for each slope η the additive constant D = D(η) comes
out of the iteration with NO tracked growth; the family is exactly
"ψ(N)−N = o(N)" and nothing stronger is extractable kernel-side (no
N/(log N)^A, no N·exp(−c√log N)).

### ψ→π conversion status (SUPPLIED for π·log/N; MISSING for π−Li)

Supplied kernel-side, all elementary and PNT-free:
- ψ→θ bridge: `nativeTheta_div_atTop_one_iff` (NativePNTTransfer.lean:94);
- θ ≤ π·log: `nativeTheta_le_primeCounting_mul_log`
  (NativePNTTransfer.lean:148);
- Chebyshev upper bound: `nativePrimeCounting_mul_log_eventually_le_eight`
  (NativePNTTransfer.lean:245), π(N)·log N ≤ 8N eventually;
- θ→π transfer parameterized by its one asymptotic input:
  `nativePrimeNumberTheorem_of_theta_div_atTop_one`
  (NativePNTSquarePrefixTransfer.lean).

MISSING: any corollary comparable to R(t) = π(t)−Li(t) → o-bound. Verified:
`logarithmicIntegralFromTwo` occurs in exactly five files
(ConcreteLiCoreExtensionWeight — the definition, at RHLean/Proof/...:12 —
plus PrimeSieveAbelIdentity, PrimeSievePNTCentering,
PrimeSieveQuotientPNTError, PrimeSieveLipschitzExcursion); NONE of the 20
NativePNT modules mentions Li, and the only Li estimates anywhere are the
Lipschitz lemmas `logarithmicIntegralFromTwo_sub_eq` /
`abs_logarithmicIntegralFromTwo_sub_le`
(PrimeSieveLipschitzExcursion.lean:117/130) — increment bounds, no
asymptotic. There is no kernel lemma of the form Li(t)·log t/t → 1, nor
even Li(t)/t → 0. So R(t) = o(t) is DERIVABLE (see Q2) but not present,
and no π-vs-Li statement of any kind exists on origin/main.

Partial summation kernel-side: yes, but on the prime-sieve side —
`sum_mertensSummatory_mul_forwardDifference`
(PrimeSieveAbelIdentity.lean:150 ff.) is a general finite Abel-summation
lemma for the Mertens weight (∀ f, ∀ n). The NativePNT side does its own
ad-hoc log summations (NativePNTAxer) rather than exposing a reusable
partial-summation toolkit; Mathlib's `Finset.sum_Ioc_by_parts` etc. are
importable everywhere.

### Bonus inventory item directly relevant to us (SUPPLIED)

`NativePNTAxer.lean` is a Mertens-FROM-PNT module ("Elementary Axer
bridge"), ending in

```lean
theorem nativeMertens_div_atTop_zero :
    Tendsto (fun N : ℕ => nativeMertensSummatory N / (N : ℝ))
      atTop (𝓝 0)
```

with the calibrated quantitative intermediate
`nativeMertens_abs_mul_log_le_of_affineEnvelope`: from any affine envelope
(α, D), |M(N)|·log N ≤ α·N·(1+log N) + (D+2)·N for N ≥ 2 — i.e.
|M(N)| ≤ α·N + (α+D+2)·N/log N. And NativePNTQuantitativeStatements.lean
supplies the exact identification with OUR Mertens object:

```lean
theorem mertensSummatory_eq_complex_nativeMertensSummatory (N : ℕ) :
    mertensSummatory N = (nativeMertensSummatory N : ℂ)
```

so M(K) = o(K) holds verbatim for the `mertensSummatory` appearing in
`primeSieveAbelBoundary`. RH-scale targets are deliberately kept as
unproven Props in the same file: `NativePNTChebyshevRHScaleStatement`
(|ψ(N)−N| ≪_ε N^{1/2+ε}), `MertensRHScaleStatement` (‖M(N)‖ ≪_ε
N^{1/2+ε}), joined in `NativePNTQuantitativeTarget`, with the only
conditional inflow `mertensRHScale_of_energy :
MertensEnergyBoundedStatement → MertensRHScaleStatement`.

**Q1 verdicts.** π·log N/N → 1 theorem: SUPPLIED (qualitative only).
ψ−N affine envelopes at every slope: SUPPLIED. Chebyshev lemmas:
SUPPLIED. Partial summation: SUPPLIED (prime-sieve side + Mathlib).
π−Li corollary: MISSING as stated, DERIVABLE (needs one new Li calculus
lemma + glue; see Q2). Mertens-from-PNT: SUPPLIED (Axer bridge, o(N),
with exact complex-cast identification to our M).

---

## Q2 — BOUNDARY TERM M(K)·R(y) AT y ≍ √x

Factor by factor, strongest in-architecture status:

1. **M(K) = o(K): SUPPLIED (kernel-complete chain).**
   `nativeMertens_div_atTop_zero` +
   `mertensSummatory_eq_complex_nativeMertensSummatory` give
   ‖mertensSummatory K‖/K → 0 with no hypothesis. This is the single
   genuinely new asset for the boundary obligation: before this landing,
   even M(K) = o(K) had no in-architecture proof. There is NO
   Mertens-rate statement (no K/(log K)^A) because the Axer input
   envelope constant D(α) is untracked (see Q1); the calibrated
   intermediate gives, for every fixed α > 0,
   |M(K)| ≤ α·K + (α+D(α)+2)·K/log K — an envelope family equivalent to
   o(K), nothing more.

2. **R(y) = o(y): DERIVABLE, not supplied.** Two routes, both cheap:
   - π(y) = o(y): follows from the SUPPLIED Chebyshev lemma
     `nativePrimeCounting_mul_log_eventually_le_eight` alone (π/N ≤
     8/log N eventually) — doesn't even need their PNT;
   - Li(y) = o(y): MISSING; a new pure-calculus lemma on
     `logarithmicIntegralFromTwo` (standard split at √y gives the
     stronger Li(y) = O(y/log y)); provable from Mathlib integral
     calculus, no arithmetic content.
   Together: ‖R(y)‖ = o(y), and with the O(y/log y) forms of both
   factors, R(y) = O(y/log y). The sharper R(y) = o(y/log y) would need
   Li(y)·log y/y → 1 (also MISSING, also pure calculus) combined with
   their π·log/N → 1; equally derivable, slightly more work. Their
   psi-to-pi conversion contributes only the π-side; the Li-side
   comparison does not exist anywhere in their architecture (Q1).

3. **Composition: DERIVABLE (trivial glue).** K = ⌊x/(y+1)⌋ gives
   K·y ≤ x identically. Hence at y = Nat.sqrt x (or any y ≍ √x):
   ‖P‖ = ‖M(K)‖·‖R(y)‖ ≤ o(K)·O(y/log y) = **o(x/log x)**, and with
   only the o(y) form of R, o(x). No hroot/collapse domain issue: the
   Abel identity is hypothesis-free, and y = Nat.sqrt x is the
   standalone-identity convention (the composed-chain convention
   y_k = √U_k+1 differs by ≤ √log x per results/030 finding 8 — a
   bridging PR must pick one; the statements below use Nat.sqrt).

**Resulting stateable envelope (best in-architecture):**

  ‖primeSieveAbelBoundary (Nat.sqrt x) x‖ = o(x/log x),
  i.e. ‖M(K)·R(y)‖/x → 0 — Filter.Tendsto form only.

**Honest gap to the program target ‖P‖ ≪_ε x^{1/2+ε}:** the achieved
bound is x^{1−o(1)}-grade (in fact literally o(x/log x) with no further
rate); the target is x^{1/2+ε}. Missing factor: x^{1/2−ε}·(1/log x)⁻¹ ≈
**a full x^{1/2−ε} power**. Nothing in the new work yields x^{1−δ} for
any fixed δ > 0 — upstream's own NativePNTQuantitativeStatements module
says exactly this by recording |ψ(N)−N| ≪ N^{1/2+ε} and ‖M(N)‖ ≪
N^{1/2+ε} as open Props "beyond the native PNT baseline". This matches
and slightly SUPERSEDES the results/030 finding-6 assessment: 030 priced
the best unconditional route at x^{1−o(1)} via Walfisz/VK cited
informally; the new landing makes an (weaker-rated, rate-free) o(x)
bound available IN-ARCHITECTURE for the first time, but moves the
distance to x^{1/2+ε} not at all. The boundary obligation remains
RH-grade open; what changes is that its PNT-grade shadow is now
formally dischargeable, which cleanly splits obligation 2 into
"o(x): closable now" + "x^{1/2+ε}: open, same status as obligation 1".

**Q2 verdicts.** M(K) = o(K): SUPPLIED. R(y) = o(y) (and O(y/log y)):
DERIVABLE (one missing Li calculus lemma + glue). Boundary
‖M(K)R(y)‖ = o(x/log x) at y ≍ √x: DERIVABLE. Any power saving
x^{1−δ}, any rate, or the target x^{1/2+ε}: MISSING (upstream records
it as open).

---

## Q3 — TRUNCATION CLAUSE E_T

**Verdict: MISSING — supplies nothing, and cannot in principle.**
Verified three ways:

1. **No analytic apparatus.** The corrected Z-gate clause
   (results/030/errata/errata_021-z-gate.md, E1) is
   E_T(x,K) ≪ √x·(log x)^{O(1)} at one common height T for the
   truncated-explicit-formula decomposition
   S = −2Re Σ_{0<γ≤T} G_{x,K}(ρ) + C_{x,K} + E_T; it is a statement
   about nontrivial zeros of the analytic ζ up to height T. Grep over
   all 20 NativePNT modules: zero occurrences of riemannZeta, Perron,
   "explicit formula", zero-free regions, or any complex-analytic
   object; every "zeta" hit is `ArithmeticFunction.zeta` (the
   coefficient sequence 1) inside the Axer convolution algebra. The
   NativePNTAxer docstring states the design constraint outright:
   "No zeta-function zero information, Perron formula, or Tauberian
   theorem is used", and NativePNTQuantitativeStatements repeats it
   ("No zero-free region, Perron formula, Tauberian theorem ... is
   introduced here"). The entire landing is deliberately Eulerian.

2. **Wrong scale.** E_T must be bounded at √x·polylog — RH scale. The
   strongest magnitude anywhere in the landing is o(N) with no rate.
   An o(x)-grade fact cannot feed a √x·polylog-grade clause even as a
   lemma ingredient; the clause's expected proof route (per the errata:
   per-d smooth truncation error ≪ (x/d)log²x/T at T ≍ x², plus
   jump-term bookkeeping ≤ K·log x) uses explicit-formula machinery
   that is orthogonal to everything upstream built.

3. **Wrong object.** E_T lives inside the zero-sum decomposition of S
   (obligation 1); the native PNT work touches, at most, obligation 2's
   PNT-grade shadow (Q2). No module references
   `primeSieveMoebiusDiscrepancySum` or any Z-gate object (the three
   files that mention the discrepancy sum — PrimeSieveAbelIdentity,
   PrimeSieveLipschitzExcursion, PrimeSieveBackwardAffineExcursion —
   predate the landing and import nothing from NativePNT*).

---

## Q4 — COLLABORATION SURFACE (candidate lemmas, statement-level)

Import-cycle check (verified from headers on origin/main): no NativePNT
module imports any PrimeSieve* module; PrimeSieveAbelIdentity's chain
(← PrimeSieveQuotientPNTError ← PrimeSievePNTCentering ← ...) never
enters NativePNT*. A new bridge module importing BOTH families is
therefore cycle-free by construction (nothing would import it except
RHLean.lean's root aggregation). Proposed placement: one new file,
`RHLean/Analysis/PrimeSieveAbelBoundaryPNT.lean`, ~150-250 LOC, house
conventions (RHLean.Analysis namespace, noncomputable section,
`open Filter`, `open scoped Topology`).

**L1 — Li smallness (pure calculus; the one genuinely missing brick).**
Imports: RHLean.Proof.ConcreteLiCoreExtensionWeight only (could even
live there).

```lean
/-- The logarithmic integral is sublinear: `Li(t) = o(t)`.  Pure
calculus on `logarithmicIntegralFromTwo`; no arithmetic input. -/
theorem logarithmicIntegralFromTwo_div_atTop_zero :
    Tendsto (fun t : ℕ =>
      logarithmicIntegralFromTwo (t : ℝ) / (t : ℝ)) atTop (𝓝 0)
```

(Optional stronger form, same proof skeleton split at `Real.sqrt t`:
`∃ C, ∀ t ≥ 2, |logarithmicIntegralFromTwo t| ≤ C * t / Real.log t`.)

**L2 — classical discrepancy is sublinear.** Imports:
PrimeSieveAbelIdentity (for `primeSievePrimeDiscrepancy`) +
NativePNTTransfer (for `nativePrimeCounting_mul_log_eventually_le_eight`;
Chebyshev suffices — the full square-prefix PNT is not needed) + L1.

```lean
/-- `R(t) = pi(t) - Li(t) = o(t)`: the Chebyshev bound makes `pi`
sublinear and `logarithmicIntegralFromTwo_div_atTop_zero` makes `Li`
sublinear.  PNT-grade, far from the `t^(1/2+eps)` scale. -/
theorem primeSievePrimeDiscrepancy_norm_div_atTop_zero :
    Tendsto (fun t : ℕ =>
      ‖primeSievePrimeDiscrepancy t‖ / (t : ℝ)) atTop (𝓝 0)
```

**L3 — the boundary obligation, PNT-grade discharge.** Imports: L2's
module + NativePNTQuantitativeStatements (for
`mertensSummatory_eq_complex_nativeMertensSummatory`) + NativePNTAxer
(for `nativeMertens_div_atTop_zero`). This is the headline PR payload:
the first formal bound of any kind on `primeSieveAbelBoundary`.

```lean
/-- **PNT-grade discharge of the Abel boundary obligation:** at the
square-root cutoff `y = Nat.sqrt x` the boundary term
`M(x/(y+1)) * (pi(y) - Li(y))` is `o(x)`.  Combines the elementary
Axer bridge `M(N) = o(N)` (via the exact complex-cast identification
with `mertensSummatory`) with `R(y) = o(y)` and `K * y <= x`.  This
does NOT approach the program target `x^(1/2+eps)`; it splits the
second obligation of the two-obligation target into a closed `o(x)`
part and an open RH-scale part. -/
theorem primeSieveAbelBoundary_sqrt_norm_div_atTop_zero :
    Tendsto (fun x : ℕ =>
      ‖primeSieveAbelBoundary (Nat.sqrt x) x‖ / (x : ℝ)) atTop (𝓝 0)
```

**L4 — two-obligation composition made kernel-visible.** Imports: L3's
module only (everything else is the hypothesis). Records formally the
results/030 correction that E needs BOTH summands, and that after this
landing the boundary summand is closed at o(x) grade while the
discrepancy sum S remains the sole open o(x)-grade obligation.

```lean
/-- Conditional composition along the Abel identity: an `o(x)` bound
on the Moebius discrepancy sum at the square-root cutoff yields the
`o(x)` prime-sieve PNT error, the boundary summand being discharged
unconditionally by `primeSieveAbelBoundary_sqrt_norm_div_atTop_zero`.
At RH scale (`x^(1/2+eps)`) BOTH summands reopen; this lemma carries
no content at that scale. -/
theorem primeSievePNTError_sqrt_norm_div_atTop_zero_of_discrepancySum
    (hS : Tendsto (fun x : ℕ =>
        ‖primeSieveMoebiusDiscrepancySum (Nat.sqrt x) x‖ / (x : ℝ))
      atTop (𝓝 0)) :
    Tendsto (fun x : ℕ =>
      ‖primeSievePNTError (Nat.sqrt x) x‖ / (x : ℝ)) atTop (𝓝 0)
```

PR sizing: L1 is the only estimate with real proof work (elementary
integral split); L2-L4 are limit algebra over supplied theorems.
Conventions to settle with upstream in the PR description: (a) the
`Nat.sqrt x` cutoff convention vs the composed-chain `y_k = √U_k + 1`
(results/030 finding 8 — these differ by a factor ≤ √log x and are not
interchangeable); (b) the `nativePNTError` / `primeSievePNTError` name
collision (suggest a docstring cross-reference in both files, or an
upstream rename of one).

**Q4 verdict:** collaboration surface EXISTS and is small — one new
cycle-free module, four statement-level lemmas, exactly one missing
mathematical brick (Li sublinearity). Everything else composes from
theorems already on origin/main.

---

## Summary of verdicts

| Q | Item | Verdict |
|---|------|---------|
| 1 | π·log N/N → 1 (`nativePNTSquarePrefixPrimeNumberTheorem`) | SUPPLIED (qualitative, rate-free) |
| 1 | ψ−N affine envelopes at every slope + cubic decay | SUPPLIED |
| 1 | Chebyshev / partial-summation lemmas kernel-side | SUPPLIED |
| 1 | π−Li (R(t)) o-corollary | MISSING as stated; DERIVABLE (one new Li lemma) |
| 2 | M(K) = o(K) in-architecture (Axer + exact cast to our M) | SUPPLIED |
| 2 | R(y) = o(y) / O(y/log y) | DERIVABLE |
| 2 | Boundary ‖M(K)R(y)‖ = o(x/log x) at y ≍ √x | DERIVABLE (new best in-architecture) |
| 2 | Any x^{1−δ} rate, or the x^{1/2+ε} target | MISSING (upstream records it open) |
| 3 | Truncation clause E_T ≪ √x·polylog | MISSING — no zero/explicit-formula apparatus, wrong scale, wrong object |
| 4 | Bridge PR (4 lemmas, 1 new module, no import cycle) | VIABLE — L1 is the only real proof work |
