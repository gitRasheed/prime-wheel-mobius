# results/020 — Lipschitz increments of the Abel face + pinned→windowed excursion (attack notes)

Repo: `/mnt/d/Projects/mobius-synthesis`, branch `agent-os`, commit **`b0b44b0`**
(`results/020: Lipschitz excursion PrimeSieveLipschitzExcursion`).

New module: `RHLean/Analysis/PrimeSieveLipschitzExcursion.lean` (one file, 594
lines) plus one sorted import line in `RHLean.lean`. **Zero sorries**, zero
`native_decide`, no new axioms.

Iterations to green: **3** compile runs (2 fix rounds; first round: Mathlib name
drift — `div_le_div_iff`, `Finset.norm_sum_le_of_le`, `pow_le_pow_left`,
`Nat.add_div` named-argument form, `Complex.norm_real` — second round: an
unused-variable warning that would have failed `--wfail`).

## Gate

| check | result |
|---|---|
| `lake build RHLean --wfail` | `Build completed successfully (7605 jobs).` (`build_tail.log`) |
| `scripts/audit_assumptions.sh` | `Lean source audit passed.` (`audit.log`) |
| `#print axioms` on all 13 public results | `[propext, Classical.choice, Quot.sound]` only (`axioms.log`) |
| sorry / native_decide count | `0` / `0` (`sorry_count.log`) |

---

## Target 1 — LIPSCHITZ

### 1a. The counting core (this is the part that fully survives)

```lean
theorem primeSieveIntervalPrimeCount_sum_le (y x h : ℕ) (hsq : x + h < (y + 1) ^ 2) :
    (∑ d ∈ Finset.Icc 1 (x / (y + 1)),
        primeSieveIntervalPrimeCount (x / d) ((x + h) / d)) ≤ h
```

with `primeSieveIntervalPrimeCount a b = ((Finset.Ioc a b).filter Nat.Prime).card`.

This is the honest discrete version of agent0's "π-increments count integers in
`(x,x+h]` with a `>√x` prime factor, ≤ 2h pairs". **The discrete truth is
better than the informal claim: the constant is 1, not 2.** The proof maps the
pair `(d, p)` to `n = d·p`, shows `n ∈ (x, x+h]` and `p > y` (the latter because
`d ≤ ⌊x/(y+1)⌋` forces `d(y+1) ≤ x < dp`), and shows the map is *injective*: two
distinct primes above `y` dividing the same `n` would give `n ≥ (y+1)² > x+h`;
equal primes force equal cofactors. So the total prime-side jump is at most
`#(x, x+h] = h` — a genuine `O(1)`-Lipschitz statement, no hypothesis on `y`
beyond `x + h < (y+1)²` (the `y² > x` condition of the brief, in its exact
discrete form).

Brute-force check before formalizing: all `y ≤ 59`, `x ≤ 1199`, `h ≤ 59` with
`(y+1)² > x+h` — 0 violations, and the bound `≤ h` is attained (`worst tot−h = 0`).

### 1b. The Li side (where the informal argument does NOT survive)

```lean
theorem primeSieveMoebiusPrefixSum_increment_norm_le (y x h : ℕ) (hy : 1 ≤ y)
    (hsq : x + h < (y + 1) ^ 2) :
    ‖primeSieveMoebiusPrefixSum (x / (y + 1)) (x + h)
        - primeSieveMoebiusPrefixSum (x / (y + 1)) x‖
      ≤ (h : ℝ)
        + (∑ d ∈ Finset.Icc 1 (x / (y + 1)),
            ((((x + h) / d : ℕ) : ℝ) - ((x / d : ℕ) : ℝ))) / Real.log ((y : ℝ) + 1)
```

`primeSieveMoebiusPrefixSum K x = ∑_{d ∈ Icc 1 K} μ(d)·R(⌊x/d⌋)` is the Abel face
with the quotient support frozen at `K`; `primeSieveMoebiusDiscrepancySum y x =
primeSieveMoebiusPrefixSum (x/(y+1)) x` by `rfl`.

This is the *sharp* form of what is provable elementarily. The Li drift is
handled by

```lean
theorem abs_logarithmicIntegralFromTwo_sub_le {a b : ℝ} (ha : 2 ≤ a) (hab : a ≤ b) :
    |logarithmicIntegralFromTwo b - logarithmicIntegralFromTwo a| ≤ (b - a) / Real.log a
```

(`logarithmicIntegralFromTwo x = ∫_2^x (log u)⁻¹`, proved via
`integral_add_adjacent_intervals` + `norm_integral_le_of_norm_le_const`), relaxed
to denominator `log(y+1)` since every cutoff `⌊x/d⌋` on the support exceeds `y`
(kernel fact `lt_div_of_mem_primeSieveQuotientSupport` from 015).

### 1c. The advertised `C·(h+1)` shape

```lean
def primeSieveLipschitzConstant (y x : ℕ) : ℝ :=
  1 + ((x / (y + 1) : ℕ) : ℝ) / Real.log ((y : ℝ) + 1)

theorem primeSieveMoebiusDiscrepancySum_increment_norm_le (y x h : ℕ) (hy : 1 ≤ y)
    (hsq : x + h < (y + 1) ^ 2) (hsupp : (x + h) / (y + 1) = x / (y + 1)) :
    ‖primeSieveMoebiusDiscrepancySum y (x + h) - primeSieveMoebiusDiscrepancySum y x‖
      ≤ primeSieveLipschitzConstant y x * ((h : ℝ) + 1)
```

Constant achieved: **`C(y,x) = 1 + ⌊x/(y+1)⌋ / log(y+1)`**, explicit and
unconditional. With `y = ⌊√x⌋` this is `≈ 1 + 2√x/log x`.

Supporting explicit steps:

```lean
theorem primeSieveFloorIncrementSum_le (x h K : ℕ) :
    (∑ d ∈ Finset.Icc 1 K, ((((x + h) / d : ℕ) : ℝ) - ((x / d : ℕ) : ℝ)))
      ≤ (K : ℝ) * ((h : ℝ) + 1)

theorem primeSieveQuotientTop_stable (y x h : ℕ) (hmod : x % (y + 1) + h < y + 1) :
    (x + h) / (y + 1) = x / (y + 1)
```

## DEVIATIONS from agent0's informal argument (report these)

**D1 — the `≤ 2` pair count is not just true, it is `≤ 1`.** Under
`x+h < (y+1)²` the representation `n = dp` with `p` prime `> y` is unique, not
two-to-one. The prime side of the increment is genuinely `O(1)`-Lipschitz with
slope `1`. (Deviation in our favour.)

**D2 — the Li drift is NOT `O(h)` in the repo's discrete conventions.** This is
the substantive failure of the informal sketch. agent0 estimates
`Σ_{d≤K} h/(d log(x/d)) ≤ 2h·log K/log x ≈ h`, which is the drift of
`Li(x/d)` at the **real** point `x/d`. The kernel object (from 015) evaluates
`Li` at the **integer** point `⌊x/d⌋`, and those floors move in unit jumps:
for `h = 1` the Li half is supported on the divisors of `x+1` below `K` and has
size `≈ τ(x+1)/log(y+1)`, which no absolute constant bounds. Honest bound
proved: `(Σ_{d≤K}(⌊(x+h)/d⌋−⌊x/d⌋))/log(y+1)`, sharp; relaxed uniformly to
`K(h+1)/log(y+1)`. Hence `C(y,x) = O(√x/log x)`, not `O(1)`. Recovering `O(1)`
needs a real-vs-floor Li comparison plus a short-interval divisor-sum input —
neither elementary in these conventions.

*(Middle ground not taken: `Σ_{d≤K}(⌊(x+h)/d⌋−⌊x/d⌋) ≤ h·H_K + K` via Mathlib's
`harmonic_le_one_add_log` would give slope `≈ 2` plus an additive floor
`≈ K/log(y+1) ≈ √x/log x`. The additive floor is irreducible either way, so the
crude `K(h+1)` relaxation was preferred: it keeps the pure `C·(h+1)` shape the
excursion lemma consumes, and does not change the order of the constant.)*

**D3 — support growth needs an extra hypothesis.** `K(x) = ⌊x/(y+1)⌋` grows with
`x`; a step that enlarges the support inserts terms `μ(d)·R(⌊(x+h)/d⌋)` with
`⌊(x+h)/d⌋ ≈ y`, for which elementary bounds only give `|R| = O(y)`. agent0
controls these with `√x·exp(−c(log x)^{3/5})`, i.e. **PNT-strength input, not
elementary arithmetic**. The Lean theorem therefore carries the hypothesis
`(x+h)/(y+1) = x/(y+1)`, with `primeSieveQuotientTop_stable` supplying the
checkable sufficient condition `x % (y+1) + h < y+1`. This is not vacuous: the
excursion window is short (`≈ H·log y / y`), so the hypothesis holds for most
pin points.

**D4 — `y ≥ 1` is required** (so that all Li arguments sit above `2`); 015's
identity itself needed no hypothesis at all.

---

## Target 2 — EXCURSION (fully clean, no deviations)

Abstract form over `f : ℕ → ℂ` (so it can be reused for any face):

```lean
theorem excursionWindow_norm_le {f : ℕ → ℂ} {x₀ : ℕ} {C : ℝ} (hC : 0 < C)
    (hlip : ∀ t : ℕ, t < ⌊‖f x₀‖ / (2 * C)⌋₊ →
      ‖f (x₀ + t) - f x₀‖ ≤ C * ((t : ℝ) + 1)) :
    ∀ t : ℕ, t < ⌊‖f x₀‖ / (2 * C)⌋₊ → ‖f x₀‖ / 2 ≤ ‖f (x₀ + t)‖

theorem excursionWindow_moment_le {f : ℕ → ℂ} {x₀ : ℕ} {C : ℝ} (hC : 0 < C)
    (hlip : ∀ t : ℕ, t < ⌊‖f x₀‖ / (2 * C)⌋₊ →
      ‖f (x₀ + t) - f x₀‖ ≤ C * ((t : ℝ) + 1)) (k : ℕ) :
    (‖f x₀‖ / 2) ^ (2 * k) * ((⌊‖f x₀‖ / (2 * C)⌋₊ : ℕ) : ℝ)
      ≤ ∑ t ∈ Finset.range ⌊‖f x₀‖ / (2 * C)⌋₊, ‖f (x₀ + t)‖ ^ (2 * k)

theorem one_le_excursionWindow {f : ℕ → ℂ} {x₀ : ℕ} {C : ℝ} (hC : 0 < C)
    (hH : 2 * C ≤ ‖f x₀‖) : 1 ≤ ⌊‖f x₀‖ / (2 * C)⌋₊
```

Sharpening vs. the brief: the two bounds need **no** `H ≥ 2C` hypothesis — they
are unconditional and vacuous when the window is empty. `H ≥ 2C` is isolated
into `one_le_excursionWindow`, which is exactly where it is needed (window
nonempty, so the moment bound has content). Window length is
`W = ⌊H/(2C)⌋₊`, matching the brief's `⌊H/(2C)⌋` exactly.

Instantiation at the Abel face:

```lean
def primeSieveExcursionWindow (y x₀ : ℕ) : ℕ :=
  ⌊‖primeSieveMoebiusDiscrepancySum y x₀‖ / (2 * primeSieveLipschitzConstant y x₀)⌋₊

theorem primeSieveMoebiusDiscrepancySum_excursion (y x₀ : ℕ) (hy : 1 ≤ y)
    (hsq : x₀ + primeSieveExcursionWindow y x₀ < (y + 1) ^ 2)
    (hmod : x₀ % (y + 1) + primeSieveExcursionWindow y x₀ < y + 1) :
    ∀ t : ℕ, t < primeSieveExcursionWindow y x₀ →
      ‖primeSieveMoebiusDiscrepancySum y x₀‖ / 2
        ≤ ‖primeSieveMoebiusDiscrepancySum y (x₀ + t)‖

theorem primeSieveMoebiusDiscrepancySum_excursion_moment (y x₀ k : ℕ) (hy : 1 ≤ y)
    (hsq : x₀ + primeSieveExcursionWindow y x₀ < (y + 1) ^ 2)
    (hmod : x₀ % (y + 1) + primeSieveExcursionWindow y x₀ < y + 1) :
    (‖primeSieveMoebiusDiscrepancySum y x₀‖ / 2) ^ (2 * k)
        * ((primeSieveExcursionWindow y x₀ : ℕ) : ℝ)
      ≤ ∑ t ∈ Finset.range (primeSieveExcursionWindow y x₀),
          ‖primeSieveMoebiusDiscrepancySum y (x₀ + t)‖ ^ (2 * k)

theorem one_le_primeSieveExcursionWindow (y x₀ : ℕ) (hy : 1 ≤ y)
    (hH : 2 * primeSieveLipschitzConstant y x₀
      ≤ ‖primeSieveMoebiusDiscrepancySum y x₀‖) :
    1 ≤ primeSieveExcursionWindow y x₀
```

So the pinned→windowed transfer is **kernel-proved**, for every `k : ℕ`,
directly against the 015 Abel-face object. Obstacle 3 (pinned vs. averaged) is
formally deleted *as a reduction*; the quantitative value of the reduction is
governed by the constant `C`, which is where D2/D3 bite.

## What this does and does not buy

- The transfer is exact and general: any windowed `2k`-th moment bound on
  `primeSieveMoebiusDiscrepancySum` now yields a pointwise bound at every pin.
- With the **proved** constant `C ≈ 2√x/log x`, the window is
  `W ≈ H log x/(4√x)`, so a pin of the expected size `H ≈ √x` gives
  `W ≈ log x/4` — nonempty, but the exponent gain from the transfer is
  logarithmic, not the `H^{2k+1} ≪ ∫ T^{2k}` power saving agent0's `C = O(1)`
  would deliver. Closing that gap is exactly D2 + D3, i.e. it requires
  PNT-strength input (or a real-argument reformulation of the Li face), and is
  therefore *not* rung-0 elementary.
- Honest label for the frontier: the reduction is proved; the strength of the
  reduction is conditional on improving `C`.

## Files

- `RHLean/Analysis/PrimeSieveLipschitzExcursion.lean` (new, 594 lines)
- `RHLean.lean` (one sorted import line inserted between
  `PrimeSieveCollapseIdentity` and `PrimeSievePNTCentering`)
- evidence here: `build_tail.log`, `audit.log`, `axioms.log`, `sorry_count.log`
