# Lean repair spec — record 031 prep (post-029 audit)

Desk-only spec. NO builds were run; every statement below is written to be pasted by a
Lean-writing session with build authority on a branch of `mobius-synthesis`. Nothing in
either repo was modified in producing this spec.

**Ground truth used.**
- `mobius-synthesis` main = `408297384342b79016745a55d3f6c8999acb1da6`.
- Working-tree `RHLean/Analysis/PrimeSieveBackwardAffineExcursion.lean` and
  `RHLean/Analysis/PrimeSieveLipschitzExcursion.lean` are identical to main (029 audit
  scope note confirms `git diff main` empty for the backward file; line numbers below are
  working-tree = main).
- Audit inputs: `results/029/audit.json` reviews `024-lean-module` (6 findings: 2 fatal,
  2 major, 2 minor) and the `plans[]` entry with `lens: "formalization"` (5-step
  sequence). Cross-checked against reviews `023-affine-backward`, `kernel-chain-audit`,
  `025-h4-kill`.
- Anchor theorem name **verified by `git grep` on main**:
  `primeSievePNTError_eq_moebiusDiscrepancySum_sub_abelBoundary`
  at `RHLean/Analysis/PrimeSieveAbelIdentity.lean:188` (defs `primeSieveMoebiusDiscrepancySum`
  line 170, `primeSieveAbelBoundary` line 176; restated forms at lines 240, 256).
- mathlib pin: `lakefile.lean` requires mathlib4 tag `v4.24.0`. All mathlib names below
  are expected at that pin; a pre-build grep checklist is in §7 for the few uncertain ones.

**Convention block for every new file** (house style, copied from the two excursion
modules):

```lean
import Mathlib
import RHLean.Analysis.<parent module>

/-! module docstring -/

noncomputable section

open scoped ArithmeticFunction.Moebius BigOperators

namespace RHLean.Analysis

open RHLean.Arithmetic
open RHLean.Proof

-- content

end RHLean.Analysis

end
```

(`open RHLean.Arithmetic` / `open RHLean.Proof` are harmless if unused; keep for house
style. `μ` is `ArithmeticFunction.moebius` via the scoped notation; Möbius values enter
sums as `(((μ d : ℤ) : ℂ))`.)

**File plan** (new modules registered in `RHLean.lean`, alphabetical order — the root file
is a flat alphabetized import list, 263 lines on main):

| file | contents | spec item |
|---|---|---|
| `RHLean/Analysis/AffineExcursion.lean` (NEW, imports Mathlib only) | abstract affine excursion lemma, window def, moment corollary, nonemptiness, both-direction wrappers | 1, 3(abstract) |
| `RHLean/Analysis/PrimeSieveAffineExcursion.lean` (NEW, imports AffineExcursion + PrimeSieveBackwardAffineExcursion) | harmonic weight, harmonic floor-increment bound, affine slope/intercept, sharp instantiation, new backward window + certificate | 2, 3 |
| `RHLean/Analysis/PrimeSieveAbelTwoObligations.lean` (NEW, imports PrimeSieveAbelIdentity) | honest two-obligation triangle theorems + honesty docstring | 4 |
| `RHLean/Analysis/MobiusRenewalTelescope.lean` (NEW, imports SquarePrefixMertensBridge) | record-025 telescope salvage | 5 |
| `RHLean/Analysis/PrimeSieveBackwardAffineExcursion.lean` (EDIT, docstrings only) | honest-docstring diffs | 6 |
| `RHLean/Analysis/PrimeSieveLipschitzExcursion.lean` (OPTIONAL EDIT, one docstring line) | 6 |

Name-collision check done on main: `affineExcursion*`, `harmonicWeight`,
`primeSieveAffineSlope/Intercept/BackwardWindow`, `TwoObligations`, `RenewalTelescope`
have zero hits. Re-grep before writing (checklist §7).

**Design decision fixed here so the Lean session does not have to choose:** the abstract
window is used with the **inclusive** convention `t ≤ W` (matching the audit's phrasing of
declared item 4: "conclusion on t ≤ W"), and the backward cap is therefore `y` (not
`y + 1` as in the current strict-`<` module). The moment sums run over
`Finset.range (W + 1)` (cardinality `W + 1`). Do not mix conventions.

---

## 1. Abstract affine excursion lemma (the theorem record 024 declared and never delivered)

File: `RHLean/Analysis/AffineExcursion.lean`. Everything is over a generic `f : ℕ → ℂ`
(the core is stated for `g : ℕ → ℂ` in "excursion coordinates" `g t = f (x₀ ± t)`, which
gives both directions from one proof — ℕ-subtraction makes a literal two-sided statement
awkward, and the wrapper cost is one `simpa` each).

```lean
/-- Window length of an affine excursion: from a pinned height `H` and an affine
increment modulus `A·t + B`, the height persists at half strength for
`t ≤ min cap ⌊(H/2 − B)/A⌋₊`.  The `cap` records the range on which the modulus
is known (for the prime-sieve instantiation: the backward stability range `y`). -/
def affineExcursionWindow (A B H : ℝ) (cap : ℕ) : ℕ :=
  min cap ⌊(H / 2 - B) / A⌋₊

/-- **Abstract affine excursion, core form.**  If `‖g t − g 0‖ ≤ A·t + B` for all
`t ≤ cap`, and `2B < H := ‖g 0‖`, then `‖g t‖ ≥ H/2` on the whole window. -/
theorem affineExcursion_norm_le {g : ℕ → ℂ} {A B : ℝ} {cap : ℕ}
    (hA : 0 < A) (hH : 2 * B < ‖g 0‖)
    (hstep : ∀ t : ℕ, t ≤ cap → ‖g t - g 0‖ ≤ A * (t : ℝ) + B) :
    ∀ t : ℕ, t ≤ affineExcursionWindow A B ‖g 0‖ cap →
      ‖g 0‖ / 2 ≤ ‖g t‖ := by
  sorry

/-- **Abstract affine moment corollary.**  `2k`-th moment lower bound over the
window (which has `W + 1` points under the inclusive convention). -/
theorem affineExcursion_moment_le {g : ℕ → ℂ} {A B : ℝ} {cap : ℕ}
    (hA : 0 < A) (hH : 2 * B < ‖g 0‖)
    (hstep : ∀ t : ℕ, t ≤ cap → ‖g t - g 0‖ ≤ A * (t : ℝ) + B) (k : ℕ) :
    (‖g 0‖ / 2) ^ (2 * k) * ((affineExcursionWindow A B ‖g 0‖ cap : ℝ) + 1)
      ≤ ∑ t ∈ Finset.range (affineExcursionWindow A B ‖g 0‖ cap + 1),
          ‖g t‖ ^ (2 * k) := by
  sorry

/-- The window is nonempty (contains `t = 1`) once `H ≥ 2(A + B)` and the cap allows it. -/
theorem one_le_affineExcursionWindow {A B H : ℝ} {cap : ℕ}
    (hA : 0 < A) (hcap : 1 ≤ cap) (hH : 2 * (A + B) ≤ H) :
    1 ≤ affineExcursionWindow A B H cap := by
  sorry

/-- Forward direction. -/
theorem affineExcursion_forward_norm_le {f : ℕ → ℂ} {x₀ : ℕ} {A B : ℝ} {cap : ℕ}
    (hA : 0 < A) (hH : 2 * B < ‖f x₀‖)
    (hstep : ∀ t : ℕ, t ≤ cap → ‖f (x₀ + t) - f x₀‖ ≤ A * (t : ℝ) + B) :
    ∀ t : ℕ, t ≤ affineExcursionWindow A B ‖f x₀‖ cap →
      ‖f x₀‖ / 2 ≤ ‖f (x₀ + t)‖ := by
  sorry

/-- Backward direction (ℕ-subtraction; for `t ≤ x₀` this is the honest backward walk,
and the statement is unconditional because `x₀ - t` truncates). -/
theorem affineExcursion_backward_norm_le {f : ℕ → ℂ} {x₀ : ℕ} {A B : ℝ} {cap : ℕ}
    (hA : 0 < A) (hH : 2 * B < ‖f x₀‖)
    (hstep : ∀ t : ℕ, t ≤ cap → ‖f (x₀ - t) - f x₀‖ ≤ A * (t : ℝ) + B) :
    ∀ t : ℕ, t ≤ affineExcursionWindow A B ‖f x₀‖ cap →
      ‖f x₀‖ / 2 ≤ ‖f (x₀ - t)‖ := by
  sorry

-- Optional but cheap: forward/backward moment wrappers, same `simpa` pattern.
```

**Proof of `affineExcursion_norm_le`** (mirrors `excursionWindow_norm_le`,
PrimeSieveLipschitzExcursion.lean:491-510, almost line for line):

1. From `t ≤ affineExcursionWindow …`: `t ≤ cap` (`min_le_left`) and
   `t ≤ ⌊(H/2 − B)/A⌋₊` (`min_le_right`), both through `le_trans` /
   `Nat.le_of_lt_succ`-free omega on the `min` (use `lt_of_le_of_lt`? no — plain
   `le_min_iff` consumption via `le_trans ht (min_le_left _ _)` pattern as in the backward
   module lines 173-178, adapted to `≤`).
2. `(t : ℝ) ≤ (H/2 − B)/A`: `Nat.floor_le` needs `0 ≤ (H/2 − B)/A`, which follows from
   `hH` (`H/2 − B > 0`) and `hA` via `div_nonneg`/`positivity`; then
   `exact_mod_cast` the ℕ inequality into `(t : ℝ) ≤ ⌊…⌋₊` and chain (`Nat.cast_le`).
3. `A * t + B ≤ H/2`: `mul_le_mul_of_nonneg_left` step 2 by `A`, then
   `A * ((H/2 − B)/A) = H/2 − B` by `mul_div_cancel₀` (needs `hA.ne'`); `linarith`.
4. `‖g t − g 0‖ ≤ H/2` from `hstep t (step 1)` + step 3.
5. Reverse triangle: `norm_sub_norm_le (g 0) (g t)` + `norm_sub_rev` + `linarith`
   (identical to lines 204-207 of the backward module).

**Proof of `affineExcursion_moment_le`**: pointwise bound from the norm lemma,
`pow_le_pow_left₀` (nonneg by `positivity`), `Finset.card_nsmul_le_sum` over
`Finset.range (W + 1)`, `Finset.card_range`, `nsmul_eq_mul`, `push_cast`, `linarith` —
identical skeleton to `excursionWindow_moment_le` (lines 523-538) and
`…_backward_excursion_moment` (lines 212-236 of the backward module). The only new cast:
`((W + 1 : ℕ) : ℝ) = (W : ℝ) + 1` (`push_cast`).

**Proof of `one_le_affineExcursionWindow`**: `le_min` splits into `1 ≤ cap` (given) and
`1 ≤ ⌊(H/2 − B)/A⌋₊`, which is `Nat.le_floor` applied to `(1 : ℝ) ≤ (H/2 − B)/A`, i.e.
`le_div_iff₀ hA` and `linarith [hH]`. (`le_div_iff₀` is already used at
PrimeSieveLipschitzExcursion.lean:517.)

**Proof of wrappers**: `simpa using affineExcursion_norm_le (g := fun t => f (x₀ + t)) …`
— the only friction is `g 0 = f (x₀ + 0)` (`Nat.add_zero` / `Nat.sub_zero`, handled by
`simpa`/`simp only [Nat.add_zero]` at the hypothesis and goal).

**Build risk: LOW.** No new mathematics; every tactic pattern already compiles elsewhere
in the same file pair. Watch item: `⌊…⌋₊` of a possibly negative real is 0, but `hH`
removes that branch; do NOT add a `0 ≤ B` hypothesis (not needed anywhere, and B < 0 is
harmlessly allowed).

Estimated size: ~120 LOC.

---

## 2. Sharp affine instantiation: slope `A_y = 1 + H_K / log (y+1)`

File: `RHLean/Analysis/PrimeSieveAffineExcursion.lean`. This is the core of the repair:
it replaces the crude relaxation `primeSieveFloorIncrementSum_le`
(PrimeSieveLipschitzExcursion.lean:395-409, `Σ ≤ K(h+1)`), which is the audited root
cause of the fatal slope inflation (`A_Lean = C ≈ 2√x/log x` vs the promised `2 + o(1)`),
and it finally **wires in the two currently-dead lemmas**
`floor_add_div_sub_le` (PrimeSieveBackwardAffineExcursion.lean:51) and — in the optional
exact-count lemma — `floor_succ_div_sub_eq_divisor_indicator` (line 44).

### 2.1 Definitions

```lean
/-- The truncated harmonic sum `H_K = Σ_{d=1}^{K} 1/d`, as a real. -/
def harmonicWeight (K : ℕ) : ℝ :=
  ∑ d ∈ Finset.Icc 1 K, ((d : ℝ))⁻¹

/-- The affine slope at prime cutoff `y` and support size `K`:
`A = 1 + H_K / log (y+1)`.  At the canonical pin `K = y` and this is `2 + o(1)`. -/
def primeSieveAffineSlope (y K : ℕ) : ℝ :=
  1 + harmonicWeight K / Real.log ((y : ℝ) + 1)

/-- The affine intercept `B = K / log (y+1)` (the record-023 constant; at `y ≍ √x`
this is `≈ 2√x / log x`). -/
def primeSieveAffineIntercept (y K : ℕ) : ℝ :=
  (K : ℝ) / Real.log ((y : ℝ) + 1)
```

Support lemmas (all one-to-three lines):

```lean
theorem harmonicWeight_nonneg (K : ℕ) : 0 ≤ harmonicWeight K
  -- Finset.sum_nonneg, inv_nonneg, Nat.cast_nonneg

theorem one_le_primeSieveAffineSlope (y K : ℕ) (hy : 1 ≤ y) :
    1 ≤ primeSieveAffineSlope y K
  -- Real.log_pos ((1:ℝ) < y + 1 from hy), div_nonneg, linarith
  -- (mirror one_le_primeSieveLipschitzConstant, Lipschitz file lines 417-423)

theorem primeSieveAffineSlope_pos (y K : ℕ) (hy : 1 ≤ y) :
    0 < primeSieveAffineSlope y K

theorem primeSieveAffineIntercept_nonneg (y K : ℕ) (hy : 1 ≤ y) :
    0 ≤ primeSieveAffineIntercept y K
```

### 2.2 The harmonic floor-increment bound (the one genuinely new estimate)

```lean
/-- **Harmonic relaxation of the floor-increment sum.**  Refines the crude
`K·(h+1)` bound (`primeSieveFloorIncrementSum_le`) to `h·H_K + K`, by using the
per-`d` bound `⌊(x+h)/d⌋ − ⌊x/d⌋ ≤ ⌊h/d⌋ + 1` (`floor_add_div_sub_le`) instead of
the per-`d` bound `h + 1`. -/
theorem primeSieveFloorIncrementSum_le_harmonic (x h K : ℕ) :
    (∑ d ∈ Finset.Icc 1 K, ((((x + h) / d : ℕ) : ℝ) - ((x / d : ℕ) : ℝ)))
      ≤ (h : ℝ) * harmonicWeight K + (K : ℝ) := by
  sorry
```

**The summation argument over `d ≤ K`, spelled out** (this is the audit-named wiring —
do not re-derive, transcribe):

Per `d ∈ Finset.Icc 1 K` (so `0 < d` from `Finset.mem_Icc`):

1. **ℕ level, via the dead lemma.** `floor_add_div_sub_le x h d hd` gives
   `(x + h)/d − x/d ≤ h/d + 1` in truncated ℕ-subtraction. Convert to the
   subtraction-free form `(x + h)/d ≤ h/d + 1 + x/d` by `Nat.sub_le_iff_le_add`
   (which holds unconditionally in ℕ; this is literally the last line of
   `floor_add_div_sub_le`'s own proof run backwards). Equivalently `omega` after `have`
   of both. This step is what makes the lemma live.
   - *Mechanism note for the docstring (divisor-indicator handling):* the quantity
     `(x+h)/d − x/d` counts the multiples of `d` in `(x, x+h]`; for `h = 1` it is exactly
     the divisor indicator `if d ∣ x+1 then 1 else 0`
     (`floor_succ_div_sub_eq_divisor_indicator`). Summed over `d ≤ K` a unit step
     therefore costs `τ_{≤K}(x+1)`, which along Wigert extremals exceeds every fixed
     power of `log x` — this is WHY no slope-only (`B = 0`) uniform bound exists and the
     intercept `K/log(y+1)` is unavoidable in the affine form. In the bound
     `h/d + 1`, the `h/d` term is the density of multiples of `d` and the `+1` absorbs
     the at-most-one extra floor jump from the phase `x mod d`; the `+1`s aggregate to
     `K`, i.e. the intercept, and the `h/d`s aggregate to `h·H_K`, i.e. the slope.
2. **Cast to ℝ.** From step 1, `(((x+h)/d : ℕ) : ℝ) − ((x/d : ℕ) : ℝ) ≤ ((h/d : ℕ) : ℝ) + 1`
   by `exact_mod_cast` + `linarith` (no `Nat.cast_sub` needed — keep the subtraction on
   the ℝ side only, as the existing crude proof does at lines 399-407).
3. **Kill the inner ℕ-division.** `((h / d : ℕ) : ℝ) ≤ (h : ℝ) / (d : ℝ)` by
   `Nat.cast_div_le`. Rewrite `(h : ℝ)/(d : ℝ) = (h : ℝ) * ((d : ℝ))⁻¹`
   (`div_eq_mul_inv`) to match `harmonicWeight`'s shape.
4. **Sum.** `Finset.sum_le_sum` with the per-`d` bound
   `… ≤ (h : ℝ) * ((d : ℝ))⁻¹ + 1`, then
   `Finset.sum_add_distrib`, `← Finset.mul_sum` (pulling `(h : ℝ)` out gives exactly
   `(h : ℝ) * harmonicWeight K`), `Finset.sum_const`, `Nat.card_Icc` (`card (Icc 1 K)`
   `= K + 1 − 1 = K`, closed by `Nat.add_sub_cancel` as at line 409), `nsmul_eq_mul`.

**Optional exact-count lemma** (skippable; include only if time allows — it is the
honest statement of what the `+1` absorbs, and wires the second dead lemma):

```lean
/-- The floor increment counts multiples exactly:
`⌊(x+h)/d⌋ − ⌊x/d⌋ = #{n ∈ (x, x+h] : d ∣ n}`. -/
theorem floor_add_div_sub_eq_card_multiples (x h d : ℕ) (hd : 0 < d) :
    (x + h) / d - x / d = ((Finset.Ioc x (x + h)).filter (d ∣ ·)).card
```

Two routes: (a) induction on `h` with `floor_succ_div_sub_eq_divisor_indicator` and
`Finset.Ioc_union_Ioc_eq_Ioc`/`Finset.sum_boole`; (b) if
`Nat.Ioc_filter_dvd_card_eq_div : ((Finset.Ioc 0 n).filter (d ∣ ·)).card = n / d`
exists at the pin (VERIFY, §7), subtract it at `n = x + h` and `n = x` using the
disjoint split of `Ioc 0 (x+h)`. Route (b) is 5 lines, route (a) ~20.

### 2.3 Threading through the prefix sum (no new estimate — reuse the sharp form)

Key observation for the Lean session: the **sharp** increment bound already exists.
`primeSieveMoebiusPrefixSum_increment_norm_le` (Lipschitz file lines 325-381) proves

```
‖ΔprefixSum‖ ≤ h + (Σ_{d ≤ K} floor-increment_d) / log (y+1),   K = x/(y+1)
```

with NO crude step. The crude step enters only afterwards (line 465). So the affine
theorem is: apply the existing sharp theorem, then bound the numerator by §2.2 instead of
by `primeSieveFloorIncrementSum_le`:

```lean
/-- **Affine increment bound, frozen support.**  `‖S(y,x+h) − S(y,x)‖ ≤ A·h + B` with
`A = 1 + H_K/log(y+1)`, `B = K/log(y+1)`, `K = x/(y+1)` — the record-023 constants. -/
theorem primeSieveMoebiusDiscrepancySum_increment_norm_le_affine
    (y x h : ℕ) (hy : 1 ≤ y) (hsq : x + h < (y + 1) ^ 2)
    (hsupp : (x + h) / (y + 1) = x / (y + 1)) :
    ‖primeSieveMoebiusDiscrepancySum y (x + h) - primeSieveMoebiusDiscrepancySum y x‖
      ≤ primeSieveAffineSlope y (x / (y + 1)) * (h : ℝ)
        + primeSieveAffineIntercept y (x / (y + 1)) := by
  sorry
```

Proof: copy lines 454-483 of the Lipschitz theorem
(`primeSieveMoebiusDiscrepancySum_increment_norm_le`) verbatim up to the `hfloor` step;
replace `primeSieveFloorIncrementSum_le` by `primeSieveFloorIncrementSum_le_harmonic`;
the algebra at the end is
`h + (h·H_K + K)/log(y+1) = (1 + H_K/log(y+1))·h + K/log(y+1)`, closed by
`div_add_div_same`/`add_div`, `div_eq_mul_inv`, `ring_nf`, `linarith` with
`Real.log_pos` positivity (`hlogy`) and `gcongr` for the division-monotone step
(dividing `Σ ≤ h·H_K + K` by `log(y+1) > 0`).

### 2.4 Backward instantiation at the canonical pin

At the pin every quantity freezes: for all `t ≤ y`,
`(primeSieveCanonicalPin y − t) / (y + 1) = y` exactly
(`primeSieveCanonicalPin_backward_stable`), so slope and intercept are **constant** along
the whole backward walk — no monotonicity lemma needed (unlike the crude module, which
needed `primeSieveLipschitzConstant_mono`).

```lean
/-- **Backward affine increment at the canonical pin**: slope `1 + H_y/log(y+1)`
(`= 2 + o(1)`), intercept `y/log(y+1)`.  This is the theorem record 024 claimed
(`023 constants`) and did not deliver. -/
theorem primeSieveMoebiusDiscrepancySum_backward_increment_norm_le_affine
    (y t : ℕ) (hy : 1 ≤ y) (ht : t ≤ y) :
    ‖primeSieveMoebiusDiscrepancySum y (primeSieveCanonicalPin y) -
        primeSieveMoebiusDiscrepancySum y (primeSieveCanonicalPin y - t)‖
      ≤ primeSieveAffineSlope y y * (t : ℝ) + primeSieveAffineIntercept y y := by
  sorry
```

Proof: transcribe lines 129-152 of the backward module
(`primeSieveMoebiusDiscrepancySum_backward_increment_norm_le`) with three changes:
(i) `hmain := primeSieveMoebiusDiscrepancySum_increment_norm_le_affine y (pin − t) t hy hsq hsupp`;
(ii) rewrite the support size in `hmain` from `(pin − t)/(y+1)` to `y` via
`primeSieveCanonicalPin_backward_stable y t ht` (so `primeSieveAffineSlope y y` appears
literally); (iii) delete the `hmono` step entirely. Existing ingredients reused:
`le_primeSieveCanonicalPin`, `Nat.sub_add_cancel`, `primeSieveCanonicalPin_lt_sq`,
`primeSieveCanonicalPin_div`.

### 2.5 The repaired window, excursion, and moments

```lean
/-- The affine backward window at the canonical pin:
`W = min y ⌊(H/2 − B)/A⌋₊` with `H = ‖S(y, x₀)‖`, `A = primeSieveAffineSlope y y`,
`B = primeSieveAffineIntercept y y`.  Inclusive convention: the excursion holds for
`t ≤ W`, and `t ≤ y` is exactly the backward stability range. -/
def primeSieveAffineBackwardWindow (y : ℕ) : ℕ :=
  affineExcursionWindow (primeSieveAffineSlope y y) (primeSieveAffineIntercept y y)
    ‖primeSieveMoebiusDiscrepancySum y (primeSieveCanonicalPin y)‖ y

/-- **Backward affine excursion at the canonical pin.**  Under the explicit height
hypothesis `2B < H` the pinned height persists at half strength on `t ≤ W`. -/
theorem primeSieveMoebiusDiscrepancySum_backward_affine_excursion
    (y : ℕ) (hy : 1 ≤ y)
    (hH : 2 * primeSieveAffineIntercept y y
        < ‖primeSieveMoebiusDiscrepancySum y (primeSieveCanonicalPin y)‖) :
    ∀ t : ℕ, t ≤ primeSieveAffineBackwardWindow y →
      ‖primeSieveMoebiusDiscrepancySum y (primeSieveCanonicalPin y)‖ / 2
        ≤ ‖primeSieveMoebiusDiscrepancySum y (primeSieveCanonicalPin y - t)‖ := by
  sorry

/-- **Backward affine moment lower bound.**  `(H/2)^{2k} · (W+1) ≤ Σ_{t ≤ W} ‖S‖^{2k}`. -/
theorem primeSieveMoebiusDiscrepancySum_backward_affine_excursion_moment
    (y k : ℕ) (hy : 1 ≤ y)
    (hH : 2 * primeSieveAffineIntercept y y
        < ‖primeSieveMoebiusDiscrepancySum y (primeSieveCanonicalPin y)‖) :
    (‖primeSieveMoebiusDiscrepancySum y (primeSieveCanonicalPin y)‖ / 2) ^ (2 * k)
        * ((primeSieveAffineBackwardWindow y : ℝ) + 1)
      ≤ ∑ t ∈ Finset.range (primeSieveAffineBackwardWindow y + 1),
          ‖primeSieveMoebiusDiscrepancySum y (primeSieveCanonicalPin y - t)‖
            ^ (2 * k) := by
  sorry
```

Proofs: instantiate `affineExcursion_backward_norm_le` / the moment wrapper at
`f := primeSieveMoebiusDiscrepancySum y`, `x₀ := primeSieveCanonicalPin y`,
`cap := y`, with `hstep t ht := norm_sub_rev ▸ (backward_increment_norm_le_affine y t hy ht)`
(the abstract lemma wants `‖f(x₀−t) − f(x₀)‖`, the increment theorem produces
`‖f(x₀) − f(x₀−t)‖`; `norm_sub_rev` bridges). `hA` from `primeSieveAffineSlope_pos`.

**Note the honesty upgrade:** unlike the current module, `2B < H` is an *explicit
hypothesis* — the theorem visibly does not fire for free. This is deliberate (audit
finding: "removing a vacuous hypothesis is not the same as certifying non-vacuity").

### 2.6 The `2 + o(1)` slope certificate (formal `o(1)` not attempted — a clean explicit bound instead)

```lean
/-- Bridge to mathlib's harmonic number. -/
theorem harmonicWeight_eq_harmonic (K : ℕ) :
    harmonicWeight K = ((harmonic K : ℚ) : ℝ) := by
  sorry  -- reindex Icc 1 K ↔ range K (Finset.sum_Icc_eq_sum_range or sum_range_succ'
         -- style shift i ↦ i+1), push_cast; harmonic K = Σ_{i ∈ range K} 1/(i+1)

/-- **The slope is `2 + o(1)` in explicit form**: `A_y ≤ 2 + (log (y+1))⁻¹`. -/
theorem primeSieveAffineSlope_le (y : ℕ) (hy : 1 ≤ y) :
    primeSieveAffineSlope y y ≤ 2 + (Real.log ((y : ℝ) + 1))⁻¹ := by
  sorry
```

Proof of the second: `harmonicWeight y ≤ 1 + Real.log y` (mathlib
`harmonic_le_one_add_log`, via the bridge) `≤ 1 + Real.log (y+1)` (`Real.log_le_log`),
so `H_y/log(y+1) ≤ 1/log(y+1) + 1` (`add_div`, `div_self` with `log(y+1) ≠ 0`), hence
`A_y = 1 + H_y/log(y+1) ≤ 2 + (log(y+1))⁻¹`. Numeric sanity (from the 023 audit,
verified there): `A_y = 2.0835` at `y = 10³`, `2.0313` at `y = 10⁸`.

**Fallback if the pinned mathlib lacks `harmonic`/`harmonic_le_one_add_log`** (unlikely
at v4.24.0 but check first, §7): drop §2.6 entirely. Nothing else depends on it — the
affine theorems use `harmonicWeight` symbolically. Alternatively prove
`harmonicWeight K ≤ 1 + Real.log K` directly by the integral-comparison
`(d : ℝ)⁻¹ ≤ Real.log d − Real.log (d − 1)`… — do NOT: that is real work; just drop.

**Build risk: MEDIUM overall.** §2.2 core: LOW-MEDIUM (cast plumbing around ℕ-division;
`Nat.cast_div_le` is the only load-bearing mathlib name not already used in the repo —
verify). §2.3-2.5: LOW (transcription of compiling proofs with one substitution). §2.6:
MEDIUM (name risk only; sacrificial). Optional exact-count lemma: MEDIUM, skippable.

Estimated size: ~200 LOC (without optionals).

---

## 3. Backward-window nonemptiness certificate

Same file, after §2.5. The abstract certificate is `one_le_affineExcursionWindow` (§1);
the concrete statement:

```lean
/-- **Nonemptiness certificate** (absent from record 024's module, audit major
finding): the backward window reaches at least `t = 1` as soon as
`H ≥ 2(A + B)`.  At `y ≍ √x` the threshold is `2(A+B) ≈ 4√x/log x` — the same
threshold as the crude window's `2C`, but past it the affine window grows like
`H/(2A) ≈ H/4` instead of `H·log x/(4√x)`: improvement factor `C/A ≈ y/(2 log y)`. -/
theorem one_le_primeSieveAffineBackwardWindow (y : ℕ) (hy : 1 ≤ y)
    (hH : 2 * (primeSieveAffineSlope y y + primeSieveAffineIntercept y y)
        ≤ ‖primeSieveMoebiusDiscrepancySum y (primeSieveCanonicalPin y)‖) :
    1 ≤ primeSieveAffineBackwardWindow y :=
  one_le_affineExcursionWindow (primeSieveAffineSlope_pos y y hy) hy hH
```

(If the term-mode application fights the definitional unfolding of
`primeSieveAffineBackwardWindow`, use `by unfold primeSieveAffineBackwardWindow; exact …`.)

Also state the general-strength version, since the shortlist consumers want `W ≥ n`:

```lean
theorem le_primeSieveAffineBackwardWindow (y n : ℕ) (hy : 1 ≤ y) (hn : n ≤ y)
    (hH : 2 * (primeSieveAffineSlope y y * (n : ℝ) + primeSieveAffineIntercept y y)
        ≤ ‖primeSieveMoebiusDiscrepancySum y (primeSieveCanonicalPin y)‖) :
    n ≤ primeSieveAffineBackwardWindow y := by
  sorry  -- le_min: n ≤ y given; n ≤ ⌊(H/2−B)/A⌋₊ by Nat.le_floor + le_div_iff₀ + linarith
```

(`one_le_…` is the `n = 1` special case; keep both, the `n = 1` form is the audit's named
deliverable.) **Build risk: LOW.** ~25 LOC.

**Honest scale statement for the record-031 write-up (NOT a Lean claim):**
`W_eff = min(y, ⌊(H/2 − B_y)/A_y⌋) ≈ min(√x, H/4)`. At `H ≍ y` both branches are `≍ √x`
— this is the defensible form of 024's "W ≍ √x" headline. Per the 023-audit cap finding,
at `H ≥ x^{1/2+ε}` the cap binds and the moment bound is `(H/2)^{2k}(y+1) ≤ H^{2k+1}x^{−ε}`,
NOT `H^{2k+1}`; do not restate the `H^{2k+1}`-scale label.

---

## 4. Honest two-obligation triangle theorem

File: `RHLean/Analysis/PrimeSieveAbelTwoObligations.lean`, importing
`RHLean.Analysis.PrimeSieveAbelIdentity`. Anchor (verified on main, exact name):

```
primeSievePNTError_eq_moebiusDiscrepancySum_sub_abelBoundary (y x : ℕ) :
    primeSievePNTError y x =
      primeSieveMoebiusDiscrepancySum y x - primeSieveAbelBoundary y x
```

with `primeSieveAbelBoundary y x = mertensSummatory (x / (y + 1)) * primeSievePrimeDiscrepancy y`.

```lean
/-- The Abel boundary term in factored norm form. -/
theorem norm_primeSieveAbelBoundary (y x : ℕ) :
    ‖primeSieveAbelBoundary y x‖
      = ‖mertensSummatory (x / (y + 1))‖ * ‖primeSievePrimeDiscrepancy y‖ := by
  unfold primeSieveAbelBoundary
  exact norm_mul _ _

/-- **The honest two-obligation bound.**  Bounding the PNT error requires BOTH the
Abel face `S = primeSieveMoebiusDiscrepancySum` AND the boundary term
`M(K)·R(y)`; this triangle inequality is everything the kernel provides in this
direction.  It is NOT a reduction of anything to the Abel face alone. -/
theorem norm_primeSievePNTError_le_two_obligations (y x : ℕ) :
    ‖primeSievePNTError y x‖
      ≤ ‖primeSieveMoebiusDiscrepancySum y x‖
        + ‖mertensSummatory (x / (y + 1))‖ * ‖primeSievePrimeDiscrepancy y‖ := by
  rw [primeSievePNTError_eq_moebiusDiscrepancySum_sub_abelBoundary,
    ← norm_primeSieveAbelBoundary]
  exact norm_sub_le _ _

/-- The reverse triangle: the Abel face is in turn controlled by the PNT error and
the boundary term.  Together with the previous theorem this states the exact
relationship: `S` and `E` differ by the single term `M(K)·R(y)`. -/
theorem norm_primeSieveMoebiusDiscrepancySum_le_two_obligations (y x : ℕ) :
    ‖primeSieveMoebiusDiscrepancySum y x‖
      ≤ ‖primeSievePNTError y x‖
        + ‖mertensSummatory (x / (y + 1))‖ * ‖primeSievePrimeDiscrepancy y‖ := by
  have h : primeSieveMoebiusDiscrepancySum y x
      = primeSievePNTError y x + primeSieveAbelBoundary y x := by
    rw [primeSievePNTError_eq_moebiusDiscrepancySum_sub_abelBoundary]; ring
  rw [h, ← norm_primeSieveAbelBoundary]
  exact norm_add_le _ _
```

**Mandatory module docstring content** (this is the integrity payload; the theorems are
trivial on purpose — "one triangle-inequality step from merged identities"):

1. The identity `E = S − M(K)·R(y)` is exact and hypothesis-free
   (`primeSievePNTError_eq_moebiusDiscrepancySum_sub_abelBoundary`); this module only
   takes norms.
2. **No kernel arrow exists from the Abel face to RH**: `primeSieveMoebiusDiscrepancySum`
   occurs on main in exactly three files (PrimeSieveAbelIdentity,
   PrimeSieveLipschitzExcursion, PrimeSieveBackwardAffineExcursion), none of which
   mention `NonzeroResponseRHScale`, `MertensEnergyBoundedStatement`,
   `ProjectedRenewalQuadraticBoundedStatement`, or `RiemannHypothesis`. Any claim that a
   kernel chain "reduces RH to the Abel face" is false as of this commit.
3. The boundary term is a **second obligation of RH strength at `y ≍ √x`**: both factors
   are then of size `~√x`, and the best unconditional inputs give only
   `|M(K)R(y)| ≪ x^{1−o(1)}`.
4. The collapse-identity domain (`hroot : Nat.sqrt x < y`, i.e. `x < y²`) and the
   canonical-pin domain (`x₀ = (y+1)² − 1 ≥ y²`) are disjoint in `x` for fixed `y`; the
   two halves of the merged development never compose at a common `(y, x)`.

(Do not name any person in the docstring. Cite `results/029` by record number only.)

**Build risk: LOW.** Only possible friction: `unfold` vs `show` on `primeSieveAbelBoundary`
(a plain `def`; `unfold` works in the repo's style, cf. line 263 of the Lipschitz file),
and `ring` on a ℂ `sub`/`add` rearrangement (used repo-wide). ~60 LOC with docstring.

---

## 5. Record-025 telescope salvage module

File: `RHLean/Analysis/MobiusRenewalTelescope.lean`, importing
`RHLean.Analysis.SquarePrefixMertensBridge` (home of
`mertensSummatory (x : ℕ) : ℂ := Σ_{m ∈ range (x+1)} μ m`, with `@[simp]`
`mertensSummatory_zero`, `mertensSummatory_succ`).

Target identity (referee-verified TRUE in the 025 audit; novelty tag must be honest —
this is the classical `Σ_{n≤X} M(⌊X/n⌋) = 1` convolved with `g`, NOT new leverage):

```lean
/-- Bridge: `mertensSummatory` as a sum over `Icc 1 x` (the `m = 0` term vanishes). -/
theorem mertensSummatory_eq_sum_Icc (x : ℕ) :
    mertensSummatory x = ∑ m ∈ Finset.Icc 1 x, (((μ m : ℤ) : ℂ)) := by
  sorry
  -- range (x+1) = Ico 0 (x+1); split off m = 0 (μ 0 = 0, ArithmeticFunction.map_zero);
  -- Nat.Ico_succ_right : Ico 1 (x+1) = Icc 1 x.
  -- Tactics: rw [mertensSummatory, Finset.range_eq_Ico,
  --   Finset.sum_eq_sum_Ico_succ_bot (by omega)]  (VERIFY name; fallback:
  --   Finset.sum_Ico_eq_sum_range juggling, or induction with mertensSummatory_succ)

/-- **The hyperbola swap** (Fubini over divisor pairs): summing `F a b` over all
pairs with `a·b ≤ N` by the product `n = a·b` first or by `a` first agree. -/
theorem sum_Icc_divisorsAntidiagonal_eq_sum_div (F : ℕ → ℕ → ℂ) (N : ℕ) :
    (∑ n ∈ Finset.Icc 1 N, ∑ p ∈ n.divisorsAntidiagonal, F p.1 p.2)
      = ∑ a ∈ Finset.Icc 1 N, ∑ b ∈ Finset.Icc 1 (N / a), F a b := by
  sorry

/-- **The classical unit identity** `Σ_{b ≤ N} M(⌊N/b⌋) = 1` (`N ≥ 1`) — `μ * 1 = δ`
summed along the hyperbola. -/
theorem sum_mertensSummatory_div_eq_one {N : ℕ} (hN : 1 ≤ N) :
    (∑ b ∈ Finset.Icc 1 N, mertensSummatory (N / b)) = 1 := by
  sorry

/-- **The record-025 telescope** (g-weighted renewal identity): for every
`g : ℕ → ℂ` and `X : ℕ`,
`Σ_{n ≤ X} (g*1)(n) · M(⌊X/n⌋) = Σ_{a ≤ X} g a`.
Classical content: this is `Σ_{n≤X} M(⌊X/n⌋) = 1` Dirichlet-convolved with `g`;
recorded as a kernel identity because it is the exact substrate for renewal-type
routes (Harman-schedule kernels `g d = λ_d·1_{d≤D}`, the I2 boundary operator), not
as a novelty. -/
theorem sum_convolveOne_mul_mertensSummatory_div (g : ℕ → ℂ) (X : ℕ) :
    (∑ n ∈ Finset.Icc 1 X, (∑ d ∈ n.divisors, g d) * mertensSummatory (X / n))
      = ∑ a ∈ Finset.Icc 1 X, g a := by
  sorry
```

**Proof sketches (transcribe, do not re-derive):**

*Hyperbola swap.* Both sides are sums over the sigma type; use `Finset.sum_sigma'` on
both and `Finset.sum_nbij'` with
`i : ⟨n, (a, b)⟩ ↦ ⟨a, b⟩` and `j : ⟨a, b⟩ ↦ ⟨a * b, (a, b)⟩`. Membership facts needed:

- `Nat.mem_divisorsAntidiagonal : p ∈ n.divisorsAntidiagonal ↔ p.1 * p.2 = n ∧ n ≠ 0`.
- Forward: from `1 ≤ n ≤ N` and `a·b = n`: `1 ≤ a` (`Nat.pos_of_mul_pos`… simplest:
  `a ≠ 0` since `n ≠ 0`, `Nat.pos_of_ne_zero`), and `b ≤ N / a` ⟺ `a * b ≤ N` by
  `Nat.le_div_iff_mul_le (0 < a)` (mind the multiplication order; `Nat.mul_comm` as
  needed — same pattern as PrimeSieveIncrementPairs_mem_facts, Lipschitz file lines
  199-218).
- Backward: from `1 ≤ a ≤ N`, `1 ≤ b ≤ N/a`: `a * b ≤ N` (same iff), `1 ≤ a * b`
  (`Nat.one_le_iff_ne_zero`, `Nat.mul_pos`), and
  `(a, b) ∈ (a*b).divisorsAntidiagonal` (`Nat.mem_divisorsAntidiagonal`, `a*b ≠ 0`).
- The two `nbij'` inverse conditions are `rfl`-adjacent (`Sigma.ext`; the product
  reconstructs `n` from the antidiagonal membership equation).

This is the fiddliest proof of the whole spec (sigma-type bookkeeping); the repo already
does `Finset.card_sigma` and `Finset.sum_sigma`-adjacent work in
`primeSieveIncrementPairs` — reuse that pattern. Budget ~50 lines.

*Unit identity.* Rewrite each `mertensSummatory (N / b)` by `mertensSummatory_eq_sum_Icc`;
the LHS becomes `Σ_{b ∈ Icc 1 N} Σ_{m ∈ Icc 1 (N/b)} μ m`, which is the RHS of the
hyperbola swap with `F b m := μ m` read in the `a`-first direction — apply the swap
BACKWARD (symm) to regroup as
`Σ_{n ∈ Icc 1 N} Σ_{p ∈ n.divisorsAntidiagonal} μ p.2`. Convert the inner sum to a
divisors sum: `Nat.sum_divisorsAntidiagonal' (f := fun _ d => μ d)` (VERIFY name/argument
order: `Nat.sum_divisorsAntidiagonal` maps `p.1`, the primed version maps `p.2`; if the
version needed is missing, swap `F` to `F b m := μ m` with roles exchanged so the plain
version applies). Then `Σ_{m | n} μ m = if n = 1 then 1 else 0`: exactly the
`moebius_mul_coe_zeta` extraction already written in the repo at
`RHLean/Arithmetic/DyadicFrozenPrefix.lean:29-43`
(`ArithmeticFunction.moebius_mul_coe_zeta`, `ArithmeticFunction.coe_mul_zeta_apply`,
`ArithmeticFunction.one_apply`) — factor that into a small lemma here (in ℂ via
`push_cast`) rather than re-deriving. Finally
`Σ_{n ∈ Icc 1 N} (if n = 1 then 1 else 0) = 1` by `Finset.sum_ite_eq'` /
`Finset.sum_eq_single 1` with `1 ∈ Icc 1 N` from `hN`.

*Main telescope.* 
1. `Finset.sum_congr`: for `n ∈ Icc 1 N`, rewrite
   `(Σ_{d ∈ n.divisors} g d) * M(X/n) = Σ_{p ∈ n.divisorsAntidiagonal} g p.1 * M((X/p.1)/p.2)`:
   distribute the product into the divisors sum (`Finset.sum_mul`), convert divisors ↔
   antidiagonal (`Nat.sum_divisorsAntidiagonal`), and inside use the membership equation
   `p.1 * p.2 = n` plus `Nat.div_div_eq_div_mul : X / a / b = X / (a * b)` (direction:
   rewrite `X / n = X / (p.1 * p.2) = X / p.1 / p.2` — i.e. apply `div_div_eq_div_mul`
   right-to-left).
2. Apply the hyperbola swap with `F a b := g a * mertensSummatory ((X / a) / b)`.
3. Inner sum: `Σ_{b ∈ Icc 1 (X/a)} g a * M((X/a)/b) = g a * Σ_b M(N'/b)` with
   `N' := X / a` (`Finset.mul_sum`), and `1 ≤ N'` from `a ≤ X`, `0 < a`
   (`Nat.one_le_div_iff` — VERIFY name; fallback `Nat.le_div_iff_mul_le` + `one_mul`).
   Unit identity finishes: `= g a * 1`.
4. `mul_one`, done.

Edge conventions to keep in mind: `g 0` never appears (divisors of `n ≥ 1` exclude 0;
`Icc 1 X` excludes 0); `X = 0` makes both sides empty sums = 0, so no hypothesis on `X`
is needed — state it hypothesis-free and let `Icc 1 0 = ∅` do the work (check the main
proof survives `X = 0`: step 3 needs `1 ≤ X/a` only for `a ∈ Icc 1 X`, which is empty).

**Build risk: MEDIUM.** The mathematics is trivial and referee-verified; all risk is
sigma-type/`nbij'` bookkeeping and two uncertain mathlib names
(`Nat.sum_divisorsAntidiagonal'`, `Finset.sum_eq_sum_Ico_succ_bot`) with stated
fallbacks. ~150 LOC.

---

## 6. Honest-docstring diff list

Edits to existing files, docstrings/comments ONLY — zero proof-term changes. Line numbers
are working-tree (= main).

### 6.1 `RHLean/Analysis/PrimeSieveBackwardAffineExcursion.lean`

| lines | current claim | audit status | replacement |
|---|---|---|---|
| 16-20 | "…the affine increment bound applies to every backward step `t <= y`, and the excursion and moment machinery runs on a window of full length at the canonical pin." | FALSIFIED (024 audit, fatal #1 + minor cap finding): the certified window is `min(y+1, ⌊H/(2C)⌋)` with `C = 1 + y/log(y+1) ≈ 2√x/log x`, i.e. `Θ(log x)` at `H ≍ √x`; the `y+1` cap never binds for large `y` (needs `H ≳ 4x/log x`, excluded unconditionally at VK strength). "Full length" is only the *stability* range of the increment bound, not the excursion window. | "…the affine increment bound applies to every backward step `t ≤ y`.  The excursion window certified in THIS module is `min (y+1) ⌊H/(2C)⌋` with the crude constant `C = primeSieveLipschitzConstant ≈ 2√x/log x`, which is `Θ(log x)` at `H ≍ √x`; the sharp affine window (slope `2+o(1)`, intercept `√x`-scale, window `≈ min(√x, H/4)`) is delivered in `RHLean.Analysis.PrimeSieveAffineExcursion`." |
| 22-24 | "The module also records two exact floor facts underlying the affine constant" | FALSIFIED (dead-lemma finding: zero uses repo-wide; the constant actually used is the crude `K(h+1)` relaxation) | "The module also records two exact floor facts (`floor_succ_div_sub_eq_divisor_indicator`, `floor_add_div_sub_le`); they are consumed by the sharp affine slope `1 + H_K/log(y+1)` proved in `PrimeSieveAffineExcursion`." (True once item 2 lands; land the edit in the same PR.) |
| 24 | "…the sharp `h/d + 1` bound" | OVERSTATED (audit minor: exact uniform maximum is `⌈h/d⌉`; the bound wastes 1 when `d ∣ h`) | "…the per-`d` bound `h/d + 1` (one above the exact maximum `⌈h/d⌉` when `d ∣ h`)" |
| 49-50 | "The sharp per-`d` floor increment bound `h/d + 1`, refining the crude `h + 1` bound…" | same as above | "The per-`d` floor increment bound `h/d + 1`, refining the crude `h + 1` bound…" |
| 156-158 | "The backward excursion window at the canonical pin: the affine window length, capped by…" | MISLEADING: `⌊H/(2C)⌋` is the *Lipschitz* (`C·(t+1)`) window, not an affine (`A·t+B`, `A ≠ B`) window | "The backward excursion window at the canonical pin with the crude Lipschitz constant, capped by the exactly-stable backward range `y + 1`.  For the genuine affine window see `primeSieveAffineBackwardWindow`." |
| 164-165 | "The pinned height persists at half strength on the whole backward window.  No stability hypothesis appears: the canonical pin supplies it for free." | TRUE but INCOMPLETE (audit major #4: no nonemptiness witness; `W = 0` whenever `H < 2C`, statement then vacuous) | append: "The window may be empty: `primeSieveBackwardWindow y = 0` whenever `H < 2C ≈ 4√x/log x`, and this module certifies no lower bound on it; see `one_le_primeSieveAffineBackwardWindow` for a certificate under an explicit height hypothesis." |
| 209-211 | "For every `k`, the pinned height at the canonical pin produces a `2k`-th moment lower bound over the backward window — the record-020 transfer with the vacuous forward hypotheses removed." | same vacuity caveat | append: "(vacuous when the window is empty; cf. the nonemptiness certificate in `PrimeSieveAffineExcursion`)" |

### 6.2 `RHLean/Analysis/PrimeSieveLipschitzExcursion.lean` (optional, one line)

The 024/029 audits found this module's docstring honest (it self-declares the Li-half
deviation and `C ≈ 1 + 2√x/log x`). Optional precision, lines 71-73: "…the window used
by the excursion lemma is short enough for it to be typical" → append "(it fails exactly
at the canonical square pins `x₀ = (y+1)² − 1`, where `x₀ % (y+1) = y`; the backward
module exists for that reason)". No other edits.

### 6.3 Out of scope for the Lean diff (list for record 031's governance session)

- `results/024/024.md` Results paragraph (`W ≍ √x` headline — evaluates its own `min`
  backwards; audit fatal #1) and "record-023 constants delivered" (fatal #2), "all five
  items delivered" (major #3).
- `JOURNAL.md` entry 2026-08-09-32 (same `W ≍ log x → W ≍ √x` claim).
- Any packet text with "kernel chain reduces RH to the Abel face" / "two
  kernel-equivalent faces" (kernel-chain audit, three fatal findings) — superseded by the
  item-4 module docstring, which is the kernel-side correction.

This spec's author modified nothing; these edits are for the write-authorized session.

**Build risk: LOW** (docstrings only; risk is doc-lint line length — repo style is
~72-char doc lines).

---

## 7. Pre-build verification checklist (run BEFORE writing any proof)

Name-existence greps in the pinned mathlib checkout
(`.lake/packages/mathlib`, tag v4.24.0), `rg -n "theorem <name>"`:

| name | used in | confidence | fallback |
|---|---|---|---|
| `Nat.cast_div_le` | §2.2 step 3 | high | `Nat.div_le_iff_le_mul_add_pred` route, or `(h/d)*d ≤ h` (`Nat.div_mul_le_self`) + `le_div_iff₀` |
| `harmonic`, `harmonic_le_one_add_log` (`Mathlib.NumberTheory.Harmonic.*`) | §2.6 only | medium | drop §2.6 (sacrificial) |
| `Finset.sum_Icc_eq_sum_range` | §2.6 bridge | medium | `Finset.sum_bij` shift by hand |
| `Nat.Ioc_filter_dvd_card_eq_div` | §2.2 optional lemma | medium | route (a) induction, or skip lemma |
| `Nat.sum_divisorsAntidiagonal`, `Nat.sum_divisorsAntidiagonal'` | §5 | high | swap `F` argument roles |
| `Finset.sum_eq_sum_Ico_succ_bot` | §5 bridge | medium | induction with `mertensSummatory_succ` |
| `Nat.one_le_div_iff` | §5 step 3 | high | `Nat.le_div_iff_mul_le` + `one_mul` |
| `Finset.sum_nbij'`, `Finset.sum_sigma'` | §5 swap | high | `Finset.sum_bij'` on sigma finsets |
| `Nat.Ico_succ_right`, `Finset.range_eq_Ico` | §5 bridge | high | — |
| `mul_div_cancel₀`, `le_div_iff₀`, `div_nonneg` | §1 | high (repo-used) | — |

Already-compiling repo names relied on (no grep needed — cited from the two read files
and main): `floor_add_div_sub_le`, `floor_succ_div_sub_eq_divisor_indicator`,
`primeSieveCanonicalPin{,_eq,_backward_stable,_div,_lt_sq}`, `le_primeSieveCanonicalPin`,
`primeSieveMoebiusPrefixSum_increment_norm_le`,
`primeSieveMoebiusDiscrepancySum_eq_prefixSum`, `primeSieveQuotientTop_stable`,
`primeSieveLipschitzConstant{,_pos,_mono}`,
`primeSievePNTError_eq_moebiusDiscrepancySum_sub_abelBoundary`, `primeSieveAbelBoundary`,
`primeSieveMoebiusDiscrepancySum`, `mertensSummatory{,_zero,_succ}`,
`ArithmeticFunction.{moebius_mul_coe_zeta, coe_mul_zeta_apply, one_apply, map_zero}`.

Registration: add the four new module imports to `RHLean.lean` in alphabetical order
(flat list, 263 lines on main). No lakefile change (single `lean_lib RHLean` glob-by-root
via the import list).

Numeric sanity anchors (from the 023/024 audits, for `#eval`-free eyeballing only):
`A_y(y=10³) = 2.0835`, `A_y(y=10⁸) = 2.0313`; `B_y = y/log(y+1) ≈ 2√x/log x`
(`B_y/√x = 0.054` at `x = 10^16`); window improvement factor over the crude module
`C/A ≈ y/(2 log y)`; nonemptiness threshold `≈ 4√x/log x` (unchanged from crude — the
gain is growth past threshold, not threshold).

## 8. Summary table

| item | new/edit | file | est. LOC | build risk |
|---|---|---|---|---|
| 1. abstract affine excursion (norm + moment + nonemptiness + 2 directions) | NEW | AffineExcursion.lean | ~120 | LOW |
| 2. sharp instantiation (harmonic bound, slope `1 + H_K/log(y+1)`, backward increment, window, excursion, moment, slope ≤ 2 + 1/log) | NEW | PrimeSieveAffineExcursion.lean | ~200 | MEDIUM (core LOW-MEDIUM; §2.6 sacrificial) |
| 3. nonemptiness certificates (`1 ≤ W`, `n ≤ W`) | NEW | (same file) | ~25 | LOW |
| 4. two-obligation triangle + honesty docstring | NEW | PrimeSieveAbelTwoObligations.lean | ~60 | LOW |
| 5. telescope salvage (`Σ (g*1)(n) M(⌊X/n⌋) = Σ g(a)`) | NEW | MobiusRenewalTelescope.lean | ~150 | MEDIUM (nbij' bookkeeping) |
| 6. docstring honesty diffs | EDIT | BackwardAffineExcursion (+ optional Lipschitz) | ~30 changed | LOW |

Suggested landing order (mirrors the 029 formalization plan's integrity-first ordering):
item 4 → items 1+2+3 (one PR unit with item 6, since 6's replacement text cites 2's
names) → item 5. If §2's core stalls at build, the fallback that is still strictly more
honest than main: land items 1, 3(abstract), 4, 6 and keep the crude instantiation with
a TODO — but the audit's judgment (and mine, having read both files) is that §2 is
transcription-grade: the sharp numerator bound already exists at
`primeSieveMoebiusPrefixSum_increment_norm_le` and only the final relaxation changes.
