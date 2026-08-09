# results/015 — Abel identity for the prime-sieve PNT error (attack notes)

Repo: `/mnt/d/Projects/mobius-synthesis`, branch `agent-os`, commit **`abca91f`**
(`results/015: Abel identity PrimeSieveAbelIdentity`).

New module: `RHLean/Analysis/PrimeSieveAbelIdentity.lean` (one file) plus one
sorted import line in `RHLean.lean`. Zero sorries, zero `native_decide`,
no new axioms.

Iterations to green: **2** (one `linear_combination` sign flip).

## Verdict on the informal form

The reviewer's informal statement in `results/014/review_full.md` §3 V3

```
E(x) = Σ_{d≤K} μ(d) R(⌊x/d⌋) − M(K)·R(y),   K = ⌊x/(y+1)⌋
```

is **exactly correct in the repo's conventions**, including the boundary
argument. The boundary argument is `y` and not any `⌊x/(K+1)⌋`-form. **No
deviation.** The two flagged uncertainties resolve as follows:

* The boundary argument is `y` because at the top index the reciprocal lower
  endpoint `max y (x/(K+1))` *is* clipped by `y`: kernel fact
  `div_succ_quotientSupportTop_le : x / (x / (y + 1) + 1) ≤ y`.
* The main-term arguments are `⌊x/d⌋` unclipped because on the support the clip
  is inactive: kernel fact
  `lt_div_of_mem_primeSieveQuotientSupport : d ∈ primeSieveQuotientSupport y x → y < x / d`.

Two further sharpenings beyond the informal statement:

1. **No hypothesis at all.** The Lean theorem holds for *every* pair of naturals
   `y x` — no `y ≥ 1`, no `√x < y`, no `K ≥ 1`. At `K = 0` both sides vanish
   because `mertensSummatory 0 = 0`.
2. **Normalization-invariant.** `R` uses the repo's
   `logarithmicIntegralFromTwo` (`∫_2^t (log u)⁻¹`), not the classical `li`.
   This is immaterial: shifting `R` by a constant `c` changes the RHS by
   `c·(Σ_{d≤K} μ(d) − M(K)) = 0`. So the formal statement is the reviewer's
   statement under any Li normalization.

## Derivation actually used (differs from the reviewer's sketch in route)

Rather than reindexing `Σ_d M(d)·Δ_d` by hand, the proof isolates a single
clipped endpoint function and applies one general Abel lemma:

* `f d := R(max y (⌊x/d⌋))` (private `primeSieveClippedDiscrepancy`).
* On the support, `primeSieveReciprocalPrimeDiscrepancy y x d = f d − f (d+1)`
  exactly — the upper endpoint of interval `d` is `⌊x/d⌋` (clip inactive) and
  its lower endpoint is literally `max y (⌊x/(d+1)⌋)` by definition, so the
  telescope is definitional rather than a case split on `d = K`.
* One induction (`sum_mertensSummatory_mul_forwardDifference`) does summation by
  parts for a general `f`, driven only by the repo's `mertensSummatory_succ`.
  Mathlib's `Finset.sum_range_by_parts` was *not* used; the bespoke `Icc 1 n`
  induction is three lines and avoids reindexing friction.
* The clip becomes active exactly once, at `d = K+1`, producing `R(y)`.

Composition with the existing kernel-proved reindex
`primeSievePNTError_eq_reciprocalPNTError` is a single rewrite, as instructed —
nothing from `PrimeSieveQuotientPNTError.lean` was re-derived.

## New objects (all elementary, all public except one)

* `primeSievePrefixPrimeCount (t : ℕ) : ℂ := ∑ q ∈ Finset.Ioc 0 t, primeSievePrimeIndicator q`
  — π(t); `primeSievePrefixPrimeCount_eq_card` proves it equals
  `((Finset.Ioc 0 t).filter Nat.Prime).card`.
* `primeSievePrimeDiscrepancy (t : ℕ) : ℂ := primeSievePrefixPrimeCount t − (logarithmicIntegralFromTwo t : ℂ)`
  — R(t).
* `primeSieveMoebiusDiscrepancySum (y x : ℕ) : ℂ := ∑ d ∈ primeSieveQuotientSupport y x, μ(d) * primeSievePrimeDiscrepancy (x / d)`
  — the bilinear main term the review names as the escape object.
* `primeSieveAbelBoundary (y x : ℕ) : ℂ := mertensSummatory (x / (y+1)) * primeSievePrimeDiscrepancy y`.
* `private def primeSieveClippedDiscrepancy` — proof-internal only; it appears in
  no public statement.

Everything else in the statements is a pre-existing repo object:
`primeSievePNTError`, `primeSieveReciprocalPNTError`, `primeSieveQuotientSupport`,
`primeSievePrimeIndicator`, `mertensSummatory`, `logarithmicIntegralFromTwo`,
`primeSieveReciprocalPrimeCount`, `primeSieveReciprocalLiMass`,
`primeSieveReciprocalPrimeDiscrepancy`, `primeSieveReciprocalLower/Upper`.

## Theorems (verbatim statements)

```lean
theorem primeSievePNTError_eq_moebiusDiscrepancySum_sub_abelBoundary
    (y x : ℕ) :
    primeSievePNTError y x =
      primeSieveMoebiusDiscrepancySum y x - primeSieveAbelBoundary y x
```

```lean
theorem primeSievePNTError_eq_moebius_weighted_primeDiscrepancy
    (y x : ℕ) :
    primeSievePNTError y x =
      (∑ d ∈ Finset.Icc 1 (x / (y + 1)),
          (((μ d : ℤ) : ℂ)) *
            ((∑ q ∈ Finset.Ioc 0 (x / d), primeSievePrimeIndicator q) -
              ((logarithmicIntegralFromTwo ((x / d : ℕ) : ℝ) : ℝ) : ℂ))) -
        mertensSummatory (x / (y + 1)) *
          ((∑ q ∈ Finset.Ioc 0 y, primeSievePrimeIndicator q) -
            ((logarithmicIntegralFromTwo (y : ℝ) : ℝ) : ℂ))
```

```lean
theorem primeSieveReciprocalPNTError_eq_moebiusDiscrepancySum_sub_abelBoundary
    (y x : ℕ) :
    primeSieveReciprocalPNTError y x =
      primeSieveMoebiusDiscrepancySum y x - primeSieveAbelBoundary y x
```

```lean
theorem sum_mertensSummatory_mul_forwardDifference
    (f : ℕ → ℂ) (n : ℕ) :
    (∑ d ∈ Finset.Icc 1 n, mertensSummatory d * (f d - f (d + 1))) =
      (∑ d ∈ Finset.Icc 1 n, (((μ d : ℤ) : ℂ)) * f d) -
        mertensSummatory n * f (n + 1)
```

```lean
theorem lt_div_of_mem_primeSieveQuotientSupport
    {y x d : ℕ} (hd : d ∈ primeSieveQuotientSupport y x) :
    y < x / d
```

```lean
theorem div_succ_quotientSupportTop_le (y x : ℕ) :
    x / (x / (y + 1) + 1) ≤ y
```

```lean
theorem primeSieveReciprocalPrimeDiscrepancy_eq_sub
    (y x d : ℕ)
    (h : primeSieveReciprocalLower y x d ≤ primeSieveReciprocalUpper x d) :
    primeSieveReciprocalPrimeDiscrepancy y x d =
      primeSievePrimeDiscrepancy (primeSieveReciprocalUpper x d) -
        primeSievePrimeDiscrepancy (primeSieveReciprocalLower y x d)
```

```lean
theorem primeSieveReciprocalPrimeCount_eq_sub
    (y x d : ℕ)
    (h : primeSieveReciprocalLower y x d ≤ primeSieveReciprocalUpper x d) :
    primeSieveReciprocalPrimeCount y x d =
      primeSievePrefixPrimeCount (primeSieveReciprocalUpper x d) -
        primeSievePrefixPrimeCount (primeSieveReciprocalLower y x d)
```

```lean
theorem primeSievePrefixPrimeCount_eq_card (t : ℕ) :
    primeSievePrefixPrimeCount t =
      (((Finset.Ioc 0 t).filter Nat.Prime).card : ℕ)
```

## Gate evidence

* `build_tail.log` — `lake build RHLean --wfail`, 7604 jobs, `Build completed successfully`.
* `audit.log` — `scripts/audit_assumptions.sh` → `Lean source audit passed.`
* `axioms.log` — `#print axioms` on all nine public theorems; every one is at or
  inside baseline `[propext, Classical.choice, Quot.sound]`
  (`div_succ_quotientSupportTop_le` uses only `[propext, Quot.sound]`).

## What this does and does not buy

It makes the review-014 coordinate change kernel-grade: the target
`|primeSievePNTError y x|` is now *exactly* `|Σ_{d≤K} μ(d)R(⌊x/d⌋) − M(K)R(y)|`
inside Lean. No bound on either piece is asserted; the σ-flow analysis in the
review is not formalized and is not claimed. Frontier delta: none
(coordinate-identity, as declared).
