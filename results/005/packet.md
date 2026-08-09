# Blind seeding packet — Möbius synthesis open estimate

You are being asked for attack angles on one open mathematical
estimate. This packet is deliberately limited to the problem statement,
the exact target, the declared obstacles, and the strength ladder. You
are not told what anyone has tried or prefers.

## Problem

Let μ be the Möbius function, M(x) = Σ_{n≤x} μ(n) the Mertens
function. A kernel-verified (Lean 4 + mathlib) reduction chain
establishes, with no unproved premises: if the target estimate below
holds, then the Riemann Hypothesis holds. The chain runs through
synchronized primorial blocks (L_k, U_k] = (W_{k-1}, W_k], W_k the
k-th primorial, sampled at complete-square endpoints
X_n = (n+1)² − 1, through a finite wheel of modulus Q_k > 6·U_k, with
the block's zero-frequency self-coupling eliminated exactly
(contraction factor ρ_{k,n} = (X_n−L_k)/Q_k < 1/6) and square-gap
interpolation already at √-scale.

## Exact target (Lean, verbatim)

```lean
def ProjectedRenewalQuadraticBoundedStatement (Λ : ℝ) : Prop :=
  ∀ ε : ℝ, 0 < ε →
    ∃ C : ℝ, 0 ≤ C ∧
      ∀ N H : ℕ, 1 ≤ H → H ≤ N →
        ∃ B : ℕ,
          (∀ r ∈ Finset.range H,
            RHLean.Analysis.squarePrefixEndpoint (N + r) ≤ B) ∧
          ((projectedRenewalGramValue Λ B N H : ℤ) : ℝ) ≤
            C * (H : ℝ) * Real.rpow (N : ℝ) (2 + ε)
```

(`mobius-synthesis/RHLean/Proof/CanonicalGapAncestryQuadraticClosure.lean:122`;
needed for every Λ ≥ 0, or any single Λ ≥ 0 — the bridge takes it
per-Λ. `projectedRenewalGramValue` is a signed Gram/quadratic form over
a window of square samples.)

An equivalent scalar face: the centered nonzero response H_{k,n}
satisfies |H_{k,n}| ≪_ε X_n^{1/2+ε} uniformly over synchronized blocks
and complete-square samples, where (kernel-checked identity)

    H_{k,n} = C_{k,n} − 2·E_{k,n},

C = the zero-mode-centered, PNT-corrected all-plus prime-comb mass;
E = the centered prime-count-minus-Li discrepancy, exactly reindexable
(kernel-checked) as a finite Mertens-weighted family over d ≥ 1 of
prime discrepancies on the reciprocal intervals
max(y, ⌊x/(d+1)⌋) < q ≤ ⌊x/d⌋.

The source route document states, from finite diagnostics: C and E are
usually same-sign and positively correlated; bounding |C| and |E|
separately and combining by triangle inequality provably loses the
cancellation that matters. The plausible mechanism is a *signed*
short-interval or dispersion estimate adapted to the reciprocal
family, or an exact transformation preserving the C − 2E correlation.

## Declared obstacles (an attack must state its position on each)

1. **Pinned vs averaged**: the block start L_k = W_{k-1} is
   deterministic and arithmetically synchronized; L²-averaged
   translation estimates permit exceptional starts. Uniformity in the
   start, exclusion of W_{k-1} from exceptional sets, or direct use of
   the primorial phase is required.
2. **Large-sieve non-transfer**: the objects live at one synchronized
   scale with no family of shifts/moduli to average over; no
   constructed map from off-diagonal pairs to a shared modulus with
   sub-square multiplicity is known.
3. **Not directly Bombieri–Vinogradov**: the reciprocal-d family
   averages over disjoint short ordinary intervals, not residue
   classes to varying moduli (source route doc).
4. **Naive strong induction fails**: inserting |M(d)| ≤ Kd^{1/2+ε}
   with absolute values into the reciprocal family produces an
   operator too large to close (source route doc).
5. **Parity-type obstruction**: classical sieve parity limits
   sieve-only arguments about μ-weighted sums; position unestablished
   for these exact coordinates but must be stated.
6. **Finite-range deception**: near-flat empirical exponents over few
   dyadic scales misled the Mertens conjecture; numerics never prove.

## Strength ladder

- Rung 0 (trivial entrant): the same machinery closing at o(x) /
  PNT strength. An angle that cannot articulate its rung-0 version
  fails its own viability control.
- Rung 1: any fixed exponent θ < 1.
- Rung 2 (target): 1/2 + ε.
- Above target (not a goal): sharp O(√x).

## What to return

Your single strongest attack angle (not a survey). Name the mechanism
precisely; say what NEW leverage it brings (「another standard tactic」
is not leverage); state its position on each declared obstacle; give
the cheapest computation or special case that would kill it; sketch
its rung-0 version; estimate what partial result is plausibly provable
within a bounded effort. Commit to specifics — a named estimate you
would prove, in what variables, with what loss.
