# Blind seeding packet — round 2 (Abel face)

You are asked for attack angles on one open estimate. This packet is
the problem statement, exact target, declared obstacles, and strength
ladder only.

## Problem

μ = Möbius, M(x) = Σ_{n≤x} μ(n), R(t) = π(t) − Li(t). A kernel-
verified chain (Lean 4/mathlib, no unproved premises) establishes:
if the target below holds, the Riemann Hypothesis holds.

## Target (two kernel-equivalent faces; attack either)

**Abel face (canonical):** with y ≍ √x, K = ⌊x/(y+1)⌋:
  |Σ_{d≤K} μ(d)·R(⌊x/d⌋)| ≪_ε x^{1/2+ε}.
(The boundary term M(K)R(y) is separately self-consistent at 1/2.)

**Quadratic-form face:** ProjectedRenewalQuadraticBoundedStatement —
a windowed Gram bound over square samples X_n = (n+1)²−1 in
synchronized primorial blocks (Lean statement available on request in
the repo mobius-synthesis).

Empirical calibration (numerics, non-promoting, range ≤ 10⁹,
exhaustive over 31,449 square samples): the Abel sum's cancellation
coefficient |S|/√(Σ_d R(x/d)²) is FLAT at 0.35–0.43 over 5.5 decades
of K — the truth appears to be genuine square-root cancellation with
a small constant. |S|/√x ≈ 0.10–0.18 in range.

## Declared obstacles (state your position on EACH)

1. **𝔉-closure (proved-by-audit, dual-model):** any argument whose
   only Mertens input is Σ_{d≤D}M(d)² ≪ D^{1+2σ} and whose
   recombination over d is Cauchy–Schwarz/Hölder/triangle EXPANDS the
   exponent: F(σ) ≥ 1/2 + σ/2. At H=1 every completion/large-sieve
   step is downstream of such a split. Your mechanism must keep the
   μ×R sign interaction alive or exit this class entirely.
2. **Fiber growth (exact counterexample):** mapping off-diagonal
   pairs (d,d′,a,a′) to shared reduced denominators has fibers
   growing linearly in D; conductors reach 4D². No bounded-fiber
   pair→modulus transfer exists in these coordinates.
3. **Pinned vs averaged:** x is a deterministic, arithmetically
   synchronized point; L²-averaged translation estimates permit
   exceptional sets that may contain it.
4. **Modulus magnitude:** the natural wheel modulus exceeds 6x by
   factors 10^5.9..10^12835; √(full-modulus) gains are vacuous;
   packet-conductor level only.
5. **Parity:** sieve-only arguments face the classical parity wall;
   μ enters linearly here — state where your mechanism stands.
6. **Circularity watch:** R(t) ≪ t^{1/2+ε} for the d=1 term IS RH for
   π. Any use of pointwise RH-strength prime bounds must be confined
   to where it is legitimately inductive or avoided.
7. **Finite-range deception:** the calibration above is exactly the
   regime that misled the Mertens conjecture. Numerics kill; never
   prove.

## Strength ladder

Rung 0 (trivial entrant): any unconditional PNT-strength bound
(o of the trivial scale) on the Abel sum — genuine publishable
progress. Rung 1: any unconditional exponent strictly below the
triangle-inequality scale (≈ x^{3/4} empirically; derive your own
honest trivial bound and beat it). Rung 2 (target): x^{1/2+ε}.
Above target: sharp O(√x) — not a goal.

## What to return

One strongest angle. Mechanism precisely; NEW leverage; position on
all 7 obstacles; cheapest kill test; rung-0 version; the named
partial result plausibly provable at bounded effort; your weakest
assumption stated plainly.
