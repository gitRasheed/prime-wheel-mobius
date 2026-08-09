# results/009 run notes — collapse identity, kernel-formalized

Repo: `/mnt/d/Projects/mobius-synthesis`, branch `agent-os`, commit **8b941b6**
("results/009: collapse identity PrimeSieveCollapseIdentity").
New module: `RHLean/Analysis/PrimeSieveCollapseIdentity.lean` (only new file;
`RHLean.lean` gained exactly one sorted import line).

Zero sorries. Build iterations to green: **3** (two `linear_combination`
coefficient fixes, one unused-simp-arg lint fix; no mathematical rework).

## Gate

- `lake build RHLean --wfail` — exit 0, 7603 jobs, green (see `build_tail.log`).
- `bash scripts/audit_assumptions.sh` — "Lean source audit passed" on box and
  locally (`audit.log`).
- `#print axioms` on 15 public declarations — every one exactly
  `[propext, Classical.choice, Quot.sound]` (`axioms.log`).

## The remainder R, defined explicitly

```lean
def primeSieveSmoothSourceSet (y x : ℕ) : Finset ℕ :=
  (Finset.Icc 1 x).filter fun n => canonicalLargestPrimeFactor n ≤ y

def primeSieveSmoothMobiusMass (y x : ℕ) : ℂ :=
  ∑ n ∈ primeSieveSmoothSourceSet y x, canonicalMoebiusWeight n
```

with the elementary characterization proved as `mem_primeSieveSmoothSourceSet_iff`
(for `1 ≤ y`): `n ∈ primeSieveSmoothSourceSet y x ↔ 1 ≤ n ∧ n ≤ x ∧ ∀ p ∈ n.primeFactors, p ≤ y`.
So `R(y,x)` is the Möbius mass of the y-smooth positive integers through x —
an arithmetic object, not "the rest".

Second (Li-subtracted) remainder, matching record 006's numerics:
`primeSieveSmoothPNTCorrectedRemainder y x = primeSieveSmoothMobiusMass y x - primeSievePNTBulk y x`.

## Discrepancy with the informal derivation (record 006, agent6 kill 1)

The 009 declaration reads Π_d as the reciprocal-interval **prime count**.
Under that reading, with the repo's exact C and E, the Li bulk cancels
identically and the remainder is `R = Msm` with **no** bulk term — not
`Msm − B` as the informal report states.

Both statements are exact; they weight the intervals differently:

| form | signed sum | remainder |
|---|---|---|
| prime count Π_d (as declared in 009) | Σ_d M(d)·π_d = T | Msm |
| discrepancy Π_d − Li_d (what 006 measured) | Σ_d M(d)(π_d − Li_d) = E | Msm − B |

Verified directly against record 006's own numeric artifact
`~/work/killtests/t7_agent6.csv` (203 sampled x, k=4..8):

- `max |Mplus − (Msm + T)| = 8.8e-9` (float epsilon) — the all-plus collapse.
- `max |C_minus_2E − (Msm − T)| = 8.7e-9` — the prime-count form.
- `max |R_006 − (Msm − B)| = 0.0` exactly — 006's R column is the Li-subtracted one.
- `max |C − (Mplus − 2B)| = 0.0` — 006's C is the repo's `primeSievePNTCorrectedAllPlusMass`.

**Size consequence, important for honesty.** The record-006 drift measurement
(θ = 0.501, |R|/√x ≤ 0.228) belongs to `Msm − B`, not to `Msm`. Refit on the
same 203 samples:

| object | log-log slope | max |·|/√x |
|---|---|---|
| `Msm − B` (006's R) | 0.501 | 0.228 |
| `Msm` (R in the prime-count form) | 0.908 | 48.2 |
| `T = Σ_d M(d)·π_d` | 0.981 | 48.4 |

So in the prime-count form the signed sum and the remainder are both ~x^0.9-0.98
objects that nearly cancel; the √x-scale statement attaches only to the
Li-subtracted pairing. No size claim of any kind is made in the Lean module.

## Public declarations

Namespace `RHLean.Analysis`.

Defs: `primeSieveSmoothSourceSet`, `primeSieveSmoothMobiusMass`,
`primeSieveReciprocalMertensSignedSum`,
`primeSieveReciprocalMertensSignedDiscrepancySum`,
`primeSieveSmoothPNTCorrectedRemainder`,
`primorialCollapseSignedSumCenteredResponse`,
`primorialCollapseSmoothCenteredResponse`.

Theorems: `canonicalLargestPrimeFactor_le_iff_forall_primeFactors_le`,
`mem_primeSieveSmoothSourceSet_iff`,
`primeSieveReciprocalMertensSignedSum_eq_reciprocalPrimeTail`,
`primeSieveReciprocalMertensSignedSum_eq_mertensPrimeTail`,
`filter_not_smooth_eq_primeSieveHighSourceSet`,
`mertensSummatory_eq_smoothMass_add_highSourceMass`,
`sum_primeSieveHighSourceSet_eq_neg_mertensPrimeTail`,
`primeSieveSmoothMobiusMass_eq_mertens_add_signedSum`,
`allPlusPrimeCombPrefixMass_eq_smoothMass_add_signedSum`,
`primeSievePNTCorrected_sub_two_error_eq_neg_signedSum_add_smoothMass`,
`mertensSummatory_eq_neg_signedSum_add_smoothMass`,
`primeSieveReciprocalMertensSignedDiscrepancySum_eq_pntError`,
`primeSievePNTCorrected_sub_two_error_eq_neg_signedDiscrepancySum_add_correctedRemainder`,
`primorialMinimalSquareWheelNonzeroResponse_eq_neg_centeredSignedSum_add_centeredSmooth`,
`norm_primorialMinimalSquareWheelNonzeroResponse_le_collapse`.
