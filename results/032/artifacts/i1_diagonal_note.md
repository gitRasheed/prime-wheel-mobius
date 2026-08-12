# Record 032a — I1 mu^2-diagonal probe, scaled run (methods note)

Date: 2026-08-12. Falsification-grade numerics only; per both repos' conventions
these runs gate/deprioritize records but cannot close a cluster.

## Object

At canonical pins x_y = (y+1)^2 - 1, ensemble y in (Y, 2Y], window t in [0, y]
(W = y+1 values, "t < W"):

    S(y, x) = sum_{d <= floor(x/(y+1))} mu(d) * R(floor(x/d))
    R(t)    = pi(t) - Li(t)
    E2(Y)   = sum_{y,t} S(y, x_y - t)^2                       (k=1 Gram form)
    D(Y)    = sum_{y,t} sum_{d<=K} mu(d)^2 R(floor(n/d))^2    (sign-blind diagonal)
    window split: sum_t S^2 = (y+1)*Sbar^2  +  sum_t (S - Sbar)^2
                              [meanblock/DC]   [varblock/AC]

Structural fact used (proved trivially, asserted in code): for n = x_y - t with
0 <= t <= y we have n = y(y+1) + (y-t), so the truncation K = floor(n/(y+1)) = y
is CONSTANT across the whole window.

## Normalization

Li via base-2 midpoint quadrature, differences-only: Li(2) = 0,
Li(n) = sum_{k=2}^{n-1} 1/log(k+0.5). Identical convention to
pilot_i1_diagonal.py and the record-028 cross-stack protocol. Moebius sieve
self-checked against direct factorization on 200 random points plus edge cases.

## Run

Script: i1_diagonal_scaled.py (this directory), python3.12 + numpy 2.4.5,
vectorized over t (full (y+1) x #squarefree matrix per y; ~60x over the pilot's
per-t loop). Levels Y = 32 ... 2048 (ensemble max y = 4096, sieve to
n = 16,785,409). Total 669 s, single core, well under the 35-min cap. Full data:
i1_diagonal_scaled.csv; log: i1_diagonal_scaled.log.

## Results vs frozen predictions (audit 029, i1-viability fatal #1)

| prediction | frozen | measured at scale | verdict |
|---|---|---|---|
| P1: D(Y) exponent in [3.7, 4] | pilot 3.74 | full fit 3.743, last-5 fit 3.757; local slopes 3.72-3.79, drift-free over 13 levels | HOLDS |
| P2: E2/D bounded away from 1 | pilot ~0.17 | range 0.169-0.278 over all levels; 0.184 at Y=2048; no upward trend | HOLDS |
| P3: DC/mean block ~99% of window energy | pilot 99.5% | 96.7% at Y=32 rising monotonically to 99.86% at Y=2048 | HOLDS (strengthens with Y) |
| kill: E2/D -> 1 with subdominant diagonal | — | does not fire | — |

Secondary fits: E2 ~ Y^3.700 (last-5 3.889) but with noisy local slopes
(2.6-5.2) because E2 is 99.9% DC-block and inherits the coherent fluctuations
of the window mean; the AC/variance block is cleanly smaller, ~Y^2.94.

## Interpretation (supports the audit finding)

1. The mu^2 diagonal D(Y) grows at exponent ~3.75 with an extremely stable
   local slope — consistent with the digest's Y^{2+4theta}/log-type prediction
   at theta = 1/2 (Y^4/log Y has effective local slope 4 - 1/log Y ~ 3.86-3.88
   in this range; the measured 3.75 sits in the frozen [3.7, 4] band, the gap
   being the usual finite-size log-structure ambiguity flagged in the digest's
   risk note). Nothing about it is small: it is the dominant object in the form.
2. The signed off-diagonal buys only a bounded constant (E2/D ~ 0.17-0.28,
   i.e. ~75-83% cancellation by FACTOR, zero cancellation by EXPONENT): E2
   tracks D at the same power of Y. Hence the rung-1 hypothesis
   E2(Y) << Y^{4+eps} is not weaker than controlling the sign-blind diagonal
   itself — an RH-strength input no signed/dispersion argument can supply,
   exactly as the fatal finding states.
3. The window energy is ~99.9% DC (mean block) at scale, and the DC share is
   still RISING with Y. Any "zero-mode gate" that subtracts the window mean
   removes essentially all of E2 but leaves D untouched — the diagonal lives
   inside the mean block, so mean-subtraction does not rescue the route; the
   residual AC energy (~Y^2.94) is a different, much smaller object.

Caveat (finite-size): at Y <= 2048 a log factor is not distinguishable from
Y^{+-0.1}; the fits are gating evidence for the audit's structural claim, not
an independent proof of the Y^{2+4theta} law. The structural half of the
finding (mu^2 >= 0, D contained in E2's expansion, D << Y^{4+eps} equivalent
to RH via the d=1 term and R(u) << u^{1/2+eps}) is desk mathematics and stands
on its own.

## Outcome

SUPPORTS-AUDIT. All three frozen predictions hold at 4x the pilot's Y (2x was
the minimum asked); the kill condition does not fire. Gates per the digest:
029's zero-mode gate is dead on arrival unless restated diagonal-subtracted;
030 (Lean amplification of E2 << Y^{4+eps}) amplifies an RH-strength input;
any restated shortlist target must be off-diagonal-only.

## Files

- /tmp/claude-1000/-mnt-d-Projects-prime-wheel-mobius/0d31eddd-16a5-4696-aef4-2949c1ddd542/scratchpad/i1_diagonal_scaled.py
- /tmp/claude-1000/-mnt-d-Projects-prime-wheel-mobius/0d31eddd-16a5-4696-aef4-2949c1ddd542/scratchpad/i1_diagonal_scaled.csv
- /tmp/claude-1000/-mnt-d-Projects-prime-wheel-mobius/0d31eddd-16a5-4696-aef4-2949c1ddd542/scratchpad/i1_diagonal_scaled.log
- Pilot (unchanged): pilot_i1_diagonal.py
