# Blind seeding packet — round 3 (Abel face, post-elimination)

You are asked for attack angles on one open estimate. This packet is
the problem statement, exact target, declared obstacles (now nine,
several proved this round), and strength ladder. You see nothing
else; propose your single strongest angle.

## Problem

μ = Möbius, M(x) = Σ_{n≤x} μ(n), R(t) = π(t) − Li(t). A
kernel-verified chain (Lean 4/mathlib, no unproved premises)
establishes: if the target below holds, the Riemann Hypothesis holds.

## Target (two kernel-equivalent faces; attack either)

**Abel face (canonical):** with y ≍ √x, K = ⌊x/(y+1)⌋:
  |Σ_{d≤K} μ(d)·R(⌊x/d⌋)| ≪_ε x^{1/2+ε}.

**Quadratic face:** ProjectedRenewalQuadraticBoundedStatement — a
windowed Gram bound over square samples X_n = (n+1)²−1 in
synchronized primorial blocks (Lean statement on request).

**The named central object (new this round; kernel-backed):** at the
canonical pin x₀ = (y+1)²−1 the quotient support is exactly stable on
the full backward window [x₀−y, x₀], and a kernel theorem converts
any pointwise spike H = |S(y,x₀)| into the moment lower bound
(H/2)^{2k}·W ≤ Σ_{t<W}|S(y,x₀−t)|^{2k}, W = min(y+1, ⌊H/2C⌋),
C ≈ 2√x/log x. Consequently a **windowed mean-square upper bound**
  (1/W)·Σ_{t<W} |S(y, x₀−t)|² ≪_ε x^{1+ε}   (W ≍ √x)
implies the pointwise target at canonical pins. Averaged attacks are
therefore sanctioned coordinates, not a cheat.

Empirical calibration (numerics, non-promoting, ≤ 10⁹, exhaustive
over 31,449 square samples): |S|/√(Σ_d R(x/d)²) FLAT at 0.35–0.43
over 5.5 decades; |S|/√x ≈ 0.10–0.18.

## Declared obstacles (state your position on EACH; 1–7 carried,
8–9 proved this round)

1. **𝔉-closure (proved, dual-model):** any argument whose only
   Mertens input is Σ_{d≤D}M(d)² ≪ D^{1+2σ} recombined by
   Cauchy–Schwarz/Hölder/triangle over d EXPANDS the exponent:
   F(σ) ≥ 1/2 + σ/2. Keep the μ×R sign interaction alive or exit the
   class. Its zero-coordinate shadow is also closed: CS-over-zeros
   with absolute F_K reproduces trivial scale.
2. **Fiber growth (exact counterexample):** no bounded-fiber
   pair→modulus transfer; fibers grow ~D/9, conductors reach 4D².
3. **Pinned vs averaged — AMENDED:** the pinned point is no longer a
   wall: the backward excursion theorem (kernel-proved) transfers
   windowed mean-square control to the pin. But the window is the
   specific backward window at x₀ = (y+1)²−1; generic-x averages
   still permit exceptional sets containing the pins.
4. **Modulus magnitude:** the wheel modulus exceeds 6x by factors
   10^5.9–10^12835; full-modulus gains are vacuous.
5. **Parity:** sieve-only arguments face the parity wall; μ enters
   linearly.
6. **Circularity:** R(t) ≪ t^{1/2+ε} for d=1 IS RH. Line-only zero
   enumeration IS RH. Any route through zeros must pay off-line zeros
   at weight x^{β−1/2} unconditionally (a fixed off-line zero defeats
   polylog-scale gates; only o(√x)-scale statements survive
   zero-free-region payment — proved this round).
7. **Finite-range deception:** the calibration range is exactly the
   regime that misled the Mertens conjecture. Numerics kill; never
   prove.
8. **Wigert floor-jump (proved this round):** the h=1 increment of
   the Abel sum is EXACTLY a divisor sum over d | x+1; along Wigert
   extremal integers it exceeds every fixed power of log x. Pointwise
   polylog-smooth control is dead; only affine/amortized moduli
   (slope 2+o(1), intercept √x/log x — both kernel-proved) exist.
9. **Renewal/telescoping edge (proved this round):** the complete-
   hyperbola telescope Σ_{n≤X}(g*1)(n)M(⌊X/n⌋) = Σ_{a≤X}g(a) is TRUE
   and exact, but Heath-Brown type-I coefficients are not supported
   on [1,D], the prime-indicator version has no exact scalar kernel,
   the honest kernel mass diverges polynomially at rung-2 scale, and
   the restricted edge is a two-parameter hyperbola sum, NOT the
   Abel functional at smaller scale. Absolute-value renewal
   inductions through this door are dead; only a SIGNED contraction
   for Σ μ(a)log a·F(X/a)-type kernels would reopen it.

Also known: the zeros route is fully mapped — its rung 0 is KNOWN
(VK-strength, proved this round), and any fixed power saving via
absolute values there is equivalent to a zero-free strip. Do not
respawn killed routes without new signed input.

## Strength ladder (updated — rung 0 is now the floor, not a goal)

KNOWN (do not propose as a deliverable): S ≪ x·exp(−c(log x)^{3/5−ε})
(triangle + VK PNT), and its zero-side realization.
Rung 1 (genuine progress): any unconditional FIXED power saving,
S ≪ x^{1−δ} — equivalently any windowed mean-square bound
(1/W)Σ|S|² ≪ x^{2−2δ} at the canonical backward windows.
Rung 2 (target): x^{1/2+ε} pointwise, or x^{1+ε} windowed
mean-square.

## What to return

One strongest angle, as JSON with fields: angle_name, mechanism
(precise), new_leverage (what is NEW — cite which obstacle wall it
passes and why), target_estimate (the named estimate you reduce to),
obstacle_positions (all nine, one line each), kill_test (cheapest,
concrete), rung1_version (your angle's honest fixed-power-saving
deliverable), plausible_partial (named result provable at bounded
effort, Lean-formalizable preferred), weakest_assumption (stated
plainly), self_assessed_probabilities (honest).
