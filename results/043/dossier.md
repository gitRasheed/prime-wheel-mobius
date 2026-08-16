# Round-5 dossier: ThreeSlotDegreeOneEnergyBoundedStatement

Self-contained briefing for blind proposal generators. Everything here is
either kernel-verified Lean on RH_Lean main (bd95c72, 2026-08-16), a
measured numeric with its source record, or a certified constraint. Do not
assume anything beyond this document without flagging the assumption.

## A. The target

Kernel-verified on main (`RHLean/Analysis/ThreeSlotDegreeOneCriterion.lean`):

```lean
def ThreeSlotDegreeOneEnergyBoundedStatement : Prop :=
  ∀ ε : ℝ, 0 < ε →
    ∃ C : ℝ, 0 ≤ C ∧
      ∀ K : ℕ,
        ‖(((threeSlotWa K + threeSlotWb K + threeSlotWc K : ℤ)) : ℂ)‖ ^ 2
          ≤ C * Real.rpow ((K + 1 : ℕ) : ℝ) (1 + ε)
```

Proving this Prop IS the Riemann Hypothesis: the chain
`threeSlotDegreeOneEnergyBounded_iff_sqrtWheelRecoveredEnergyBounded` →
`riemannHypothesis_of_threeSlotDegreeOneEnergy` is complete, kernel-checked,
axiom-clean ([propext, Classical.choice, Quot.sound]). Equivalently: prove
|W_a(K)+W_b(K)+W_c(K)| = |M(4K)| ≪_ε K^{1/2+ε}. No bridge work remains; the
open problem is quantitative cancellation, full stop.

Nobody expects a full proof from one round. The deliverable is either ONE
new kernel-provable lemma that makes quantitative progress, or a certified
kill of a mechanism class (both are wins; the kill report is the honest
base case).

## B. Exact machinery on main (all kernel-verified, all usable)

1. **Three-slot projection** (`ThreeSlotMertensDegreeOneProjection.lean`):
   27 states `threeSlotStateCount K i`, characters chiA/chiB/chiC,
   `mertensSummatory_four_mul_eq_degreeOne : M(4K) = W_a+W_b+W_c`, and the
   identification W_j = R_j − 2H_j with the physical corrected wheel field.
2. **Endpoint transfer**: |M(X) − M(4⌊X/4⌋)| ≤ 3
   (`abs_moebiusPrefix_sub_fourCell_le`); complete-cell estimates suffice.
3. **Fresh-prime recurrence** (exact, `MobiusFiniteDifferenceIdentification`):
   D_{S∪{p}} f = D_S f − D_S(shift_p f). Unordered finite Möbius difference
   operator; saturated T1: at level y with S = primesUpTo y, D_S recovers
   the Möbius prefix exactly.
4. **Sharp fiber modulus at the canonical pin** (PRs #365/#366/#368):
   at pin = (y+1)y + y, for t ≤ y,
   ‖D_S S(y,·)(pin) − D_S S(y,·)(pin−t)‖ ≤ A·t·Π_{p∈S}(1+1/p) + (A+B)·N_active,
   with A = slope y y = 1 + harmonicWeight(y)/log(y+1), B = intercept y y =
   y/log(y+1), N_active the moving-fiber count. Affine constants are indexed
   by support level x/(y+1) and monotone in it.
5. **Far-sector renewal** (`SurvivorFarUpperRigidity` + PR #370): the
   fixed-prime survivor cofactor mass in the far sector equals −M(⌊t/q⌋)
   (exact identity for t ≥ 55, q prime, t+9 ≤ q), now COMPOSED with
   lower-scale Mertens on main. This recurses the problem to lower scale;
   note renewal alone gives PNT-strength for free and stalls exactly at
   x^{1/2+ε} — that stall is the problem, not an oversight.
6. **2-3-5 parity stencil** (PR #364, merged): survivor fibres carried on
   the exact three-prime toggle stencil, |Δ₂Δ₃Δ₅| ≤ 4 per site.
7. **Collision involution layer**: sign-reversal is CONDITIONAL
   (`correctedCollisionSiteWeight_signReversal` needs hstate/hother/hsmooth);
   frontier decomposition into pairable + fixed + mate-crosses-cutoff defect
   states is exact; each (p,q) incomplete-period frontier has ≤ 9 residue
   classes. Open route-doc question: does the physical R−2H field satisfy
   sign reversal on physical prefixes? Nobody has proved or refuted it.
8. **Renewal telescope / hyperbola identity** (`MobiusRenewalTelescope`):
   Σ_{uv=n} β(u,v) = μ(n) exactly; cancellation lives BETWEEN balanced and
   extreme factorization regions (measured correlation −0.999986).
9. **Balanced bilinear centering** (PR #372, merged): exact five-piece split
   β = muE + eE + rhoE + muRho + rhoRho against arbitrary density ρ;
   `TypeIILocalEnergyBoundedStatement` and `CoherentLocalEnergyBoundedStatement`
   stated as Props; only implication: both ⟹ block-balanced local energy.
10. **NativePNT stack**: PNT-strength inputs (second Selberg-type identities)
    available in-repo; M(x) = o(x) is usable, M(x) = O(x^{1/2+ε}) is the target.

## C. Measured numerics (falsifiers, never evidence of provability)

- Record 040 (K up to 2.5×10⁷): TV distance of consecutive 27-state pair
  distribution from product of marginals = 0.1350 and FLAT (no decay);
  conditional mutual information plateaus at ≈ 0.248 nats, flat from 10⁶;
  state-frequency imbalance decays like K^{−0.488}; max|M(4K)|/√(4K) stays
  in [0.32, 0.41]. Consequence: the chain has PERSISTENT memory; any
  independence/mixing assumption is empirically false, not just unproven.
- Record 032 (x ≤ 10⁸, upstream probes replicated): the signed d-family sum
  beats its triangle majorant by only ~D^{0.33} (signed exponent 0.5145 vs
  triangle 0.6780, D ≍ √x). Full square-root cancellation across the
  d-family is NOT measured. Mechanisms must engage the saving that exists.
- PR #372 diagnostics (N ≤ 2048, sieve 1.7×10⁷): |H| (smooth core) grows
  like X^0.86, so |H|/√X diverges — R and 2H are each huge, only R−2H is
  small; muRho piece grows N^{+0.485} at 1.72×Δ — the bound
  E_loc(muRho) ≪ H N^{2+ε} is measured FALSE, not merely hard; rhoRho is
  sign-constant (negative in 100% of blocks, prefix ~0.93 N²/log²N);
  typeIICore is flat (N^{−0.304}) but carries 1.4% of the energy.

## D. Auto-kill constraints (any violation kills the proposal, cite the item)

**D1. Omega guardrail.** M(x) = Ω_±(√x) is a classical theorem. Any
mechanism whose conclusion would give o(√x), or that would prove the bound
for a generic ±1 sequence with the same measured local statistics, is
automatically wrong. State explicitly where your mechanism uses arithmetic
specific to μ and where the Ω_± lower bound survives it.

**D2. Route-doc §6 bans.** No 27-state uniformity assumption; no
Markov/mixing/independence of neighboring μ values (D-040 falsifies it); no
sign-blind splitting; never split R − 2H (each piece is X^0.86-huge); never
split the three slot channels W_a, W_b, W_c (cross terms are negative and
load-bearing); no constant-per-prime-pair defect charging (Σ over pairs of
the ≤9 frontier bound is ≫ the target).

**D3. Section-J certified kills (records 029/030/032).** (a) Termwise
absolute values across the d-family: unconditional x^{3/4} ceiling, dead.
(b) Coordinate-relocation test: if the new coordinate's obligation
transfers back unconditionally at the same exponent, it relocated the
difficulty, it didn't reduce it. (c) μ²-diagonal test: extract every
nonnegative sub-block your method must bound separately; if any required
sub-block bound is itself RH-equivalent, the route is circular.

**D4. The trilemma (PR #372, on main).** Any additive decomposition of the
block residual into separately-bounded pieces falls into exactly one of:
index-set partition (preserves RH scale, but each piece costs GRH —
STRONGER than RH); factorization-space split (destroys scale ×3958;
cancellation is between the regions); coefficient split (destroys scale;
ρ > 0 forces a sign-constant piece). Rule with predictive content: a split
preserves RH scale in every piece iff it partitions the summation index
{n} itself — and those don't change the analytic character. If your
mechanism decomposes, you must say which horn you take and why you survive it.

**D5. Closed routes (do not resubmit).** Compression-escape/window
coercivity (σ_max = 1 identically, zero defect, permutation isometry);
bilinear opening with nonnegative kernel (sup over bounded coefficients is
trivial; off-diagonal ~ diagonal); bounding muRho alone (measured false,
D-C above); typeIICore as an RH step (real theorem, 1.4% of the mass);
27-state Markov/transfer-operator spectral gap (record 029/040).

**D6. Lane discipline.** Open upstream PR #373 owns
`RHLean/Proof/SquareRoot*` (legal-ancestry Gram amplification). Proposals
may USE its ideas conceptually but must not plan Lean work in those files.

**D7. Epistemics.** Numerics falsify, never prove. A proposal's value is a
precise first lemma that the kernel could check, plus a computable
prediction that could kill the mechanism cheaply. Heuristic plausibility
without a falsifiable prediction scores zero.

## E. Dead-end registry (named, with cause of death)

- I1 (spectral positivity): required sub-block bound was RH-equivalent — circular.
- C−2E and DC/AC coordinates: relocation, not reduction (record 030/032).
- Triangle-over-d / floor-jump majorants: x^{3/4} ceiling / polylog-dead by Wigert.
- Markov/mixing on 27 states: TV 0.1350 flat, CMI 0.248 nats flat (040).
- Compression-escape coercivity: exact zero defect (372).
- muRho-in-isolation: measured growth N^{+0.485} (372).
- Naive defect summation over prime pairs: scale mismatch (route doc §7).
- Renewal-only iteration: stalls at x^{1/2+ε}, exactly the target (041 framing note).

## F. What the strongest open threads look like (orientation, not prescription)

- The physical sign-reversal question (B7) is the route doc's named "most
  important immediate question" and remains genuinely open.
- The fresh-prime recurrence (B3) + sharp pin moduli (B4) give an exact
  induction skeleton over primes that nobody has driven to an energy bound.
- The far-sector renewal (B5) composed with the stencil (B6) recurses scale
  exactly; the stall at 1/2 is where a genuinely new inequality must enter.
- The trilemma says: don't decompose — find an inequality on the WHOLE
  signed object (variance across scales, energy increment, self-improvement)
  or partition {n} in a way whose pieces you can treat JOINTLY (so no
  per-piece GRH obligation).
