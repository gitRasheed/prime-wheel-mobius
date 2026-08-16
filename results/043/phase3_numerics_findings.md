# Record 043 — phase-3 numerics: the two decisive measurements

Agent: phase-3 numerics. All heavy compute on EC2 (c7i.4xlarge, 16 cores),
working dir `~/work/probe043/`. Nothing under `~/work/RH_Lean` was touched.

Standing epistemic rules applied throughout: **numerics falsify, never prove**;
every fitted exponent carries its fit window and its lower-cutoff sensitivity;
the program's pre-asymptotic caveat (an exponent excess of order `x^0.015` over
four decades is indistinguishable from a polylog) is attached where it bites —
and, per the round-2 review, is *not* used in reverse as a licence to falsify an
`o(1)` claim just because the measured excess is larger.

---

## 0. Verdicts, in the audit's own terms

**PROBE 1 — greedy-order revival.** The audit's falsification of *"the
fresh-prime induction has no target-compatible per-stage invariant"* **survives
at scale**. Wording that the evidence supports:

> At every tested finite horizon through `N = 10^6`, a state-aware one-step
> greedy found a low-intermediate ordering; the reported randomized-tie-break
> runs attained the **exact floor** `sup_x |g_S(x)|/sqrt(x) = 1.000000` at every
> one of 78 498 stages at `N = 10^6`, with `max|g_S| = 999` against
> `sqrt(N) = 1000`. Along sampled successful trajectories, admissible next moves
> were locally common (estimated median 65.5% of remaining primes at `N = 10^5`;
> minimum over sampled stages 27.5%), and batches of ~30 random candidates
> usually sufficed. The tested `N = 10^5` ordering did **not** transfer to larger
> replay horizons (`sup` degrades to 22.61 at horizon `10^6`), and **no
> horizon-independent ordering or invariant is exhibited**.

Registry sentence I recommend (the round-2 review's, adopted verbatim):

> "No finite-horizon huge-intermediate obstruction was observed through
> `N = 10^6`: state-aware greedy orderings kept the path maximum at most 1.004,
> and the reported randomized runs attained the exact floor. The unresolved issue
> is coherence across horizons — one `N = 10^5` ordering fails larger-window
> replay — and no horizon-independent induction rule or invariant has been found."

I explicitly do **not** file "obstructed by relocation only": relocation is the
remaining *observed* problem, not a proved unique obstruction. Good paths do
not die at any tested scale (`N` up to `10^6`).

**PROBE 2 — orientation-split scale test.** Wording that the evidence supports:

> **The orientation piece is not scale-preserving over the tested range.** Its
> late-window dyadic-block RMS has effective `R`-exponent **1.4164** on
> `[2^16, 2^26)` (n = 10 complete blocks, `R^2 = 0.9988`), rising monotonically
> with the lower cutoff (1.155 from `R >= 8`; 1.293 from `10^3`; 1.416 from
> `6.6e4`; 1.446 from `10^6`); block-MAX 1.473 → 1.540 on the same nested
> windows. `M(R^2-1)`, measured over every integer `R <= 5.29x10^5`, sits at
> exponent **0.95–1.01 in `R`** (`X^{0.48}`–`X^{0.51}`, `R^2 >= 0.999`) — target
> scale. On the common range where both were measured, each orientation piece is
> individually larger than the whole and the gap grows: the scale-destruction
> factor `(A_2(G)+A_2(matched'))/A_2(M(R^2-1))` rises 3.07, 3.64, 3.69, 4.53,
> **5.78** over the last five dyadic blocks. Target-scale `R^{1+o(1)}` behaviour is
> **strongly unsupported on the tested upper blocks**: the effective excess is
> ~0.42, far beyond the program's polylog-resolution caveat, `A_2(T)/T` rises
> persistently through nine consecutive blocks (0.52 → 5.78), and no crossover
> toward exponent 1 is visible. This is strong finite-range evidence against
> treating the split as automatically scale-preserving; it does **not**
> asymptotically exclude the class `R^{1+o(1)}`.

Sign-definiteness of `G` fails at `R = 20939`, so the audit's small-scale
"sign-definite negative, `|G|/R` flat at 0.30" is a true statement about
`R <= 3162` and a false statement about `R <= 10^8`.

So renewal-a's null lands on **its own "horn 1 confirmed" branch**, at the
tested scales. **Additional finding the record must carry:** this split IS a
plain (though horizon-dependent) index-set partition of `{m <= R^2-1}` and it
does not preserve scale, so dossier constraint **D4's rule "a split preserves RH
scale in every piece iff it partitions the summation index itself" is false as a
predictive principle in the direction `index partition ⟹ scale preserved`**
(§2.6).

---

## 1. PROBE 1 — greedy-order revival test

### 1.1 Object, rule, exactness

`g_S(x) = sum_{d | primorial(S), d <= x} mu(d)`; `g_{}(x) = 1` for `x >= 1`,
`g(0) = 0`; inserting `p` maps `g -> g - g(./p)`; with `S =` all primes `<= N`
the state is bit-exactly `M`.

**Greedy rule (identical to the audit's `refute2/p4.c`).** At each stage pick,
among all not-yet-inserted primes `p`, one minimising
`score(p) = sup_{1<=x<=N} |g_S(x) - g_S(floor(x/p))| / sqrt(x)`
— the sup norm of the state AFTER inserting `p`. Mode 0 breaks ties by smallest
prime (p4.c's convention); mode 1 breaks ties uniformly at random. One-step
lookahead over the entire remaining candidate set.

**Exactness.** `g_S(1) = 1` for every `S`, so `score >= 1` always: **1 is a hard
floor**. `score(p) <= 1` is the pure-integer predicate `(g(x)-g(x/p))^2 <= x`;
no floating point enters the decision, so "attains the floor" is a certificate,
not an estimate. When no prime attains 1 (an *above-floor stage*) the code falls
back to a genuine full minimisation over all remaining primes.

**Correctness fix forced by GPT round 1.** The fast path tests only `x >= p`,
sound only while the current state obeys `|g(x)| <= sqrt(x)` — a premise that
dies at the first above-floor stage. Fixed by maintaining exactly
`minviol = min{x : g(x)^2 > x}` (`N+1` if none): a candidate `p` can attain the
floor only if `p <= minviol`, tested first. A full `O(N)` audit (exact sup,
exact energy, exact `minviol`) runs at **every above-floor stage** and every
512 stages. **`audit_mismatch = 0` in every run below**, and the final state
matches an independently sieved `M` bit-for-bit (`sat_mismatch = 0`, reported as
bookkeeping only — the endpoint is order-independent and validates nothing about
the search). The fix was not cosmetic: at `N = 5x10^5` the pre-fix code reported
`sup = 1.003449` with 134 above-floor stages; the corrected code reports
`sup = 1.004024` with 107.

### 1.2 The greedy ladder — mode 0 (the audit's exact rule)

| N | pi(N) | pathmax sup (stage frac) | E/N^2 at that stage | max\|g_S\| | sqrt(N) | pathmax E/N^2 (stage frac) | score at that stage | above-floor | C_p<0 |
|---|---|---|---|---|---|---|---|---|---|
| 2 000 | 303 | 1.000000 (—) | — | 44 | 44.72 | 0.324002 (0.172) | 1.00000 | 0/303 | 92/303 |
| 5 000 | 669 | 1.000000 (—) | — | 70 | 70.71 | 0.330254 (0.127) | 1.00000 | 0/669 | 226/669 |
| 10 000 | 1 229 | 1.000000 (—) | — | 99 | 100.00 | 0.317096 (0.112) | 1.00000 | 0/1229 | 506/1229 |
| 20 000 | 2 262 | 1.000000 (—) | — | 141 | 141.42 | 0.299642 (0.089) | 1.00000 | 0/2262 | 997/2262 |
| 50 000 | 5 133 | 1.000000 (—) | — | 223 | 223.61 | 0.310382 (0.548) | 1.00000 | 0/5133 | 2309/5133 |
| 100 000 | 9 592 | 1.002488 (0.514) | 0.3510 | 316 | 316.23 | 0.356363 (0.514) | 1.00000 | 1/9592 | 4730/9592 |
| 200 000 | 17 984 | 1.002518 (0.666) | 0.3816 | 448 | 447.21 | 0.385889 (0.666) | 1.00192 | 7/17984 | 9434/17984 |
| 500 000 | 41 538 | 1.004024 (0.483) | 0.3855 | 709 | 707.11 | 0.406296 (0.504) | 1.00198 | 107/41538 | 24390/41538 |

("stage frac —" for `sup`: on an exact-floor path every stage attains 1.000000,
so the "worst-score stage" is not unique and no location is reported.)
The first rows reproduce the audit's published numbers to every digit
(`max|g| = 44/99/141`, `E/N^2 = 0.324/0.317/0.2996`, `C_p<0` = 92/303,
506/1229, 997/2262).

**Mode 0 was not carried to `N = 10^6`**: its smallest-prime tie-break forces a
scan of `~0.2 * pi(N)` candidates per stage (8 962/stage, `9.78e7` element
visits/stage, wall 861 s at `N = 5x10^5`), extrapolating to hours of exclusive
machine time. It was stopped at stage 8 192 of 78 498 in favour of the
measurements below, which carry the same content.

### 1.3 The same greedy objective at N = 10^6 (mode 1, random tie-break)

```
RESULT N=1000000 mode=1 primes=78498 sat_mismatch=0 audit_mismatch=0
RESULT pathmax_sup_ratio=1.000000   pathmax_abs_g=999   sqrtN=1000.00
RESULT pathmax_E_over_N2=0.464456 (stage 3343, frac 0.0426, score there 1.00000)
RESULT above_floor_stages=0/78498   Cp_negative_stages=62127/78498
RESULT cost: candidates=2540008 (32.4/stage) full_scans=2377050
             element_visits=1.876e12 (2.39e7/stage)   wall=596.9s
```

**`sup_x |g_S(x)|/sqrt(x) = 1.000000` at every one of 78 498 stages** — the
absolute floor. So the answer to *"does `sup_x |g_S(x)|/sqrt(x)` stay `O(1)` at
every stage along the greedy path?"* is **yes at `N = 10^6`, and it stays exactly
AT the floor**, for this run.

The above-floor stages seen in mode 0 (1, 7, 107 at `N = 10^5, 2x10^5, 5x10^5`,
excess `<= 0.0040`) are **path-dependent and avoidable in the reported randomized
runs** — three independent seeds at `N = 10^5` all give `sup = 1.000000` with
zero above-floor stages, as does the single seed at `N = 10^6`. (I do not claim
they are "an artifact of the tie-break" as a theorem; that is the observed
pattern over the runs made.)

### 1.4 Controls at N = 10^5 — is the greedy result generic? No.

| ordering | pathmax sup | pathmax E/N^2 | max\|g_S\| |
|---|---|---|---|
| greedy, smallest-prime tie-break | 1.002488 | 0.356363 | 316 |
| greedy, random tie-break (seeds 7/8/9) | **1.000000** ×3 | 0.437 / 0.473 / 0.404 | 316 |
| increasing primes (smooth-first) | 13.952457 | **59.998282** | 4412 |
| decreasing primes | 30.125213 | 321.759361 | 9526 |
| random order, 5 seeds | 5.397 / 5.107 / 5.955 / 3.880 / 5.330 | 10.98 / 9.40 / 13.04 / 5.29 / 10.87 | 1227–1883 |

`E/N^2 = 59.998` for increasing order independently reproduces the audit's
59.998 at `N = 10^5`. Random orders sit at `sup ~ 4–6`; decreasing order is the
worst of all. The greedy result is emphatically not generic.
(No "above-floor" count is quoted for the fixed-order controls: those modes take
the prescribed prime without running the candidate test, so the counter is not
computed and would be meaningless.)

### 1.5 How much search does a good path need? (candidate-budget curve, N = 10^5)

Greedy restricted to a random subset of `b` remaining primes per stage,
**one run per budget, one seed each** — this is a coarse curve, not a threshold
determination:

| b | 1 | 3 | 10 | 30 | 100 | 300 |
|---|---|---|---|---|---|---|
| pathmax sup | 6.122481 | 1.312755 | 1.014393 | 1.000000 | 1.003058 | 1.003841 |
| pathmax E/N^2 | 13.857867 | 0.814676 | 0.392257 | 0.367853 | 0.457373 | 0.421376 |
| above-floor | 8119/9592 | 2220/9592 | 434/9592 | 0/9592 | 18/9592 | 5/9592 |

Reading: `b = 1` reproduces random-order behaviour; from `b = 10` upward the
path maximum is within 0.015 of the floor and the above-floor count is small.
The non-monotone `b = 30 / 100 / 300` entries are single runs at different seeds
and I do **not** claim a threshold at 30 — an ensemble per budget was not run.

### 1.6 Branching freedom

Measured by exact full checks of a **systematic sample of 400 remaining primes
with a random start** every 200 stages (and, separately, of the 100 smallest
remaining). These are *estimated* fractions, not exact counts over all remaining
primes:

| N = 10^5, mode-0 path | min | q10 | median | q90 | max | mean |
|---|---|---|---|---|---|---|
| admissible fraction, all remaining | 0.2750 | 0.3595 | **0.6550** | 0.9595 | 1.0000 | 0.6304 |
| admissible fraction, 100 SMALLEST remaining | 0.0000 | 0.0000 | **0.0000** | 0.1450 | 1.0000 | 0.0850 |

| N = 10^6, mode-1 path (20 samples) | min | q10 | median | q90 | max | mean |
|---|---|---|---|---|---|---|
| all remaining | 0.7325 | 0.9880 | **1.0000** | 1.0000 | 1.0000 | 0.9856 |
| 100 smallest remaining | 0.9900 | — | 1.0000 | — | 1.0000 | 0.9995 |

At no sampled stage did fewer than 27.5% of the sampled remaining primes keep
the state exactly at the floor. The small-prime asymmetry on the mode-0 path is
a *path* effect, not a fact about primes: mode 0 spends small primes as early as
it legally can, so the small primes still remaining are exactly the ones already
refuted; on the mode-1 path the remaining small primes are a random subset and
are admissible essentially always. The mechanical reason large primes are safe
is immediate: inserting `p` perturbs `g` only at `x >= p`, by `g(floor(x/p))`,
whose arguments are small.

**What this does and does not establish.** It establishes that **admissible next
moves are locally common along the sampled successful trajectories**. It does
*not* establish abundance of complete successful paths (locally admissible
branches can die later), and it does not settle the attribution
"degrees-of-freedom rather than arithmetic conspiracy" — the arithmetic-destroying
surrogate control that would settle that was not run (stated gap, §3).

### 1.7 Lookahead cost (measured, accounting split out)

| N | mean candidates/stage | element visits/stage | total element visits | wall |
|---|---|---|---|---|
| 2 000 | 53.8 | 4.5e4 | 1.36e7 | 0.0 s |
| 20 000 | 347.6 | 7.9e5 | 1.79e9 | 0.2 s |
| 100 000 | 1 684.5 | 1.17e7 | 1.12e11 | 8.0 s |
| 200 000 | 3 673.4 | 1.98e7 | 3.57e11 | 24.8 s |
| 500 000 | 8 962.1 | 9.78e7 | 4.06e12 | 861.5 s |
| 1 000 000 (mode 1) | 32.4 | 2.39e7 | 1.88e12 | 596.9 s |

Mode-0 candidates/stage track `~0.2 * pi(N)`, so the audit's exact rule costs
`Theta(pi(N))` sup-norm scans per stage. Mode 1 needs only 32.4/stage (batch
size 32 — i.e. the first batch essentially always contains an admissible prime).
**The admissibility test itself remains state-dependent and expensive** — both
rules read the state, hence `mu`, at every step, so this is an existence result
about orderings, not a proof strategy. Prunings used, all sound (they can only
reject candidates that genuinely fail): the `minviol` test, a cached
per-candidate refuting witness re-tested in `O(1)`, and a 1-in-8 strided
pre-scan; verified to reproduce the unpruned output exactly at
`N = 2000, 2x10^4, 10^5, 2x10^5`.

### 1.8 Cross-horizon stability

Take the ordering the greedy produced at horizon `N1 = 10^5` (9 592 primes) and
replay it verbatim, evaluating the sup norm over `x <= N2`:

| replay horizon N2 | 10^5 (self-check) | 2x10^5 | 5x10^5 | 10^6 |
|---|---|---|---|---|
| pathmax sup over the 9 592 stages | 1.002488 | 18.763790 | 22.608847 | 22.608847 |

Profile at horizon `10^6`: score first exceeds 2 at stage 293/9592 (3% of the
way) and 5 at stage 2152 (22%), then rises monotonically to 22.61.

**Confound, stated.** The *terminal* state of the replay is
`S = primesUpTo(10^5)`, order-independent, so its value 22.61 at horizon `10^6`
is forced for *any* ordering of those primes — it is exactly involution-b's /
induction-b's downward-closed "mountain". The profile shows the failure is *not*
confined to that forced endpoint: many earlier prefixes already perform badly on
the larger window.

**Defensible conclusion (weakened per round 2).** Goodness at horizon `N` does
not by itself guarantee goodness at a larger evaluation horizon, and this tested
ordering fails that transfer. It does **not** follow that all good orderings are
horizon-specific: a horizon-independent ordering could interleave primes above
`10^5` before exhausting the smaller ones, so it need not contain this replay as
an initial segment.

### 1.9 Energy

`E_S = sum_{x<=N} g_S(x)^2` (prefix energy over `[1,N]`; the round-1 review
correctly objected to calling it a window energy).

**The deterministic half of the answer (round-2 review's point, and it is the
right one).** On an exact-floor path, `g_S(x)^2 <= x` for every `x` at every
stage, hence
```
E_S  <=  sum_{x<=N} x  =  N(N+1)/2  ~  0.5 N^2 ,
```
with no fit required. The `N = 10^6` mode-1 run attains the floor at every
stage, so its energy bound `E <= 0.5 N^2` is a theorem about that run; the
measured path maximum 0.4645 `N^2` sits just under it. What remains unproved is
the *existence* of exact-floor paths uniformly in `N`.

**The empirical half.** Path maxima of `E/N^2` across the mode-0 ladder: 0.324,
0.330, 0.317, 0.300, 0.310, 0.356, 0.386, 0.406 — flat to within a factor 1.36
over 2.4 decades, with a slow upward drift. Lower-cutoff sensitivity (upper
cutoff `N = 5x10^5`):

| N >= | 2 000 | 5 000 | 10 000 | 20 000 | 50 000 | 100 000 |
|---|---|---|---|---|---|---|
| pathmax E ~ N^ | 2.0423 | 2.0558 | 2.0783 | 2.1044 | 2.1146 | 2.0802 |
| n, R^2 | 8, 0.546 | 7, 0.640 | 6, 0.825 | 5, 0.947 | 4, 0.924 | 3, 0.959 |

The drift is not a clean power law at the full range (`R^2 = 0.55`) and settles
around `N^{2.08}`–`N^{2.11}` on the upper windows. That excess over `N^2` is
within a factor of a few of the program's pre-asymptotic wall and is equally
consistent with `N^2 * polylog`; honest statement: **"consistent with `O(N^2)`,
with an unresolved slow upward drift over the last decade"**. Contrast the
smooth-first order: 2.69, 5.50, 9.49, 60.00, i.e. `N^{2.795}` (n = 4,
`R^2 = 1.0000`; `N^{2.799}` from `N >= 5000`) — a clean, unambiguous power.

---

## 2. PROBE 2 — orientation-split scale test

### 2.1 Objects, and the identity (elementary, not merely numerical)

`G(R) = sum_{p <= R prime} M(p-1)`; the on-main kernel-verified identity
(`SquareRootPositiveSmoothCollapse.lean`) is
`M(R^2-1) = -G(R) + matched(R)`, and `matched'(R) := M(R^2-1) + G(R)`.

**The orientation class is genuinely a unit-weight index subset**, by an
elementary bijection (so no numerical hedging is needed on the combinatorics —
only on its asymptotic scale). Write `m = n p` with `p = P^+(m)` and `n < p`;
the class is `C_R = { m : P^+(m) <= R, m/P^+(m) < P^+(m) }`, and the constraint
`m <= R^2-1` is automatic since `m = np < p^2 <= R^2`. For such `m`, `n < p`
gives `p ∤ n`, so `mu(m) = mu(n) mu(p) = -mu(n)`, whence
```
sum_{m in C_R} mu(m) = sum_{p <= R} sum_{n < p} (-mu(n)) = - sum_{p <= R} M(p-1) = -G(R).
```
Verified computationally as well: direct computation of the class sum from a
largest-prime-factor sieve equals `-G(R)` at 25 values of `R <= 2000`,
**0 mismatches**, including the audit's `R = 100 -> 31`, `R = 316 -> 96`,
`R = 1000 -> 185`.

Other verifications before any fitting:

* **`G` reproduces the audit's list exactly**: `-1, -12, -31, -96, -185, -507,
  -1054` at `R = 10, 31, 100, 316, 1000, 1778, 3162`.
* **Mertens checkpoints from the segmented sieve** (independent code path from
  the plain sieve used for `G`): `M(10^6) = 212`, `M(10^7) = 1037`,
  `M(10^8) = 1928`, `M(10^9) = -222`, `M(10^10) = -33722`, `M(10^11) = -87856`
  — all matching known values.
* **Exact regrouping identity** (§2.3) verified for **every** `R <= 10^8`:
  0 failures out of `10^8`.

### 2.2 `|G(R)|` at scale — the headline measurement

Estimator per the round-1 review: **dyadic-block RMS over every integer `R`**,
integer-uniform weight, no cumulative running maximum, no zero-crossing
excision. `A_2(T) = ((1/T) sum_{T < R <= 2T} G(R)^2)^{1/2}`;
`A_inf(T) = max_{T<R<=2T} |G(R)|` as a secondary envelope. All statements below
are about the **estimator**, not about pointwise `|G|` — `G` changes sign and
comes arbitrarily close to zero, so a pointwise "flat" claim would contradict the
sign data.

`A_2(T)/T` by dyadic block `T = 2^k`, all integers `R <= 10^8`:

| k | 3 | 6 | 9 | 12 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 | 25 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| A_2/T | 0.339 | 0.506 | 0.374 | 0.369 | 0.441 | 0.470 | 0.516 | 0.707 | 1.198 | 1.400 | 1.543 | 2.181 | 3.325 | 4.644 | 5.782 |

Bounded in 0.25–0.52 for `k <= 17` (`R <= 1.3e5`) — **the regime the audit
measured** — then monotone rising through nine consecutive blocks.

Effective exponent with lower-cutoff sensitivity (upper cutoff fixed at the last
complete block, `R < 6.7e7`):

| lower cutoff | R window | slope A_2 | n | R^2 | slope A_inf |
|---|---|---|---|---|---|
| k >= 3 | [8, 6.7e7] | 1.1552 | 23 | 0.9902 | 1.1990 |
| k >= 10 | [1.0e3, 6.7e7] | 1.2926 | 16 | 0.9944 | 1.3374 |
| k >= 13 | [8.2e3, 6.7e7] | 1.3728 | 13 | 0.9985 | — |
| k >= 15 | [3.3e4, 6.7e7] | 1.3952 | 11 | 0.9984 | 1.4275 |
| **k >= 16** | **[6.6e4, 6.7e7]** | **1.4164** | **10** | **0.9988** | **1.4729** |
| k >= 18 | [2.6e5, 6.7e7] | 1.4196 | 8 | 0.9981 | 1.4987 |
| k >= 20 | [1.0e6, 6.7e7] | 1.4460 | 6 | 0.9981 | 1.5403 |

The estimate **increases monotonically with the lower cutoff and settles near
1.42–1.45 (RMS) / 1.47–1.54 (max)**. The dyadic-RMS data are quantitatively
*compatible* with `A_2(T)` of order `T^{3/2}/log T` on the fitted blocks
(`R^{3/2}/log R` has local log-slope `1.5 - 1/log R = 1.44` at `R = 10^7`), but
the high `R^2` does not distinguish that model from nearby powers or from other
slowly-varying corrections.

**Sign structure.** `G(R) < 0` for all `10 <= R < 20939`; the first `R >= 10`
with `G(R) >= 0` is **R = 20939**. 42 sign changes on the geometric grid to
`10^8`; `|G(R)|/R` ranges from `2e-6` (near-zero crossing at `R = 458 196`) to
**7.868** (at `R = 67 250 683`).

### 2.3 The structural half of the explanation

Regrouping the double sum (many-to-one, so multiplicity appears):
```
G(R) = sum_{p <= R} M(p-1) = sum_{n < R} mu(n) * w_R(n),      w_R(n) = pi(R) - pi(n)
     = pi(R) * M(R-1) - sum_{n < R} mu(n) * pi(n).
```
Verified for **every** `R <= 10^8`, 0 failures. So after regrouping into the
`n`-variable each `mu(n)` carries a weight of typical size `pi(R) ~ R/log R`.

The **exact** independent-sign standard deviation of that weighted sum,
`sigma(R) = ( sum_{n<R} mu(n)^2 w_R(n)^2 )^{1/2}`, computed exactly from running
`#squarefree`, `sum mu^2 pi`, `sum mu^2 pi^2`:

| R | 10^2 | 10^3 | 10^4 | 10^5 | 10^6 | 10^7 | 10^8 |
|---|---|---|---|---|---|---|---|
| sigma(R) | 100.3 | 2.20e3 | 5.21e4 | 1.30e6 | 3.40e7 | 9.17e8 | 2.53e10 |
| G(R)/sigma(R) | -0.3091 | -0.0840 | -0.0362 | -0.0323 | -0.0296 | -0.0131 | +0.0264 |

`sigma(10^8) = 0.47 * R^{3/2}/log R`, and `G/sigma` is flat at a few percent with
no trend over four decades.

**Correct statement (the round-2 review deleted my stronger one, rightly).** The
regrouping identity exposes a weight whose independent-sign RMS scale is
`R^{3/2}/log R`, and the observed dyadic growth is compatible with a small
multiple of that scale. Reaching `R^{1+o(1)}` would therefore require
cancellation **substantially stronger than the independent-sign benchmark**.
These numerics neither supply nor rule out such cancellation: independent-sign
variance is a structurally motivated null scale, **not a lower bound**, and
deterministic arithmetic correlations can in principle beat it.

### 2.4 Cancellation controls

| control at `R = 10^8` | value |
|---|---|
| `T(R) = sum_{p<=R} \|M(p-1)\|` (triangle majorant of G) | 5.310e9 |
| `\|G\|/T` | **0.1258** |
| `S(R) = sum_{n<=R} M(n)` (all-integers analogue) | 1.228e10 |
| `TS(R) = sum_{n<=R} \|M(n)\|` | 9.414e10 |
| `\|S\|/TS` | **0.1304** |
| `A(R) = sum_{n<=R} n mu(n)`; `\|A\|/R^{1.5}` | 0.1805 (0.2262 at `R = 10^6`) |

`|G|/T` across decades `R = 10^2..10^8`: 0.838, 0.408, 0.166, 0.152, 0.140,
0.063, 0.126 — bounded and trendless from `R = 10^4` on. So `G` beats its own
triangle majorant by a bounded factor (~7–16) and by **no power** over the
measured range; `T(R)` has measured local decade slopes 1.36, 1.40, 1.43, 1.41,
1.46. And `|S|/TS = 0.1304` versus `|G|/T = 0.1258`: the prime-restricted sum
shows *the same* relative cancellation as the all-integers analogue, so
restricting to primes contributes nothing arithmetically special at these scales.
(`|A|/R^{1.5}` flat at 0.18–0.23 is the same statement in the `n`-weighted
coordinate.) Per the round-1 review, the "decorrelated" prime-difference control
is worthless — it telescopes to `M(p_max-1)`; measured `D = 1925` against
`M(10^8) = 1928`, a bookkeeping check only.

### 2.5 The paired object `matched'(R) = M(R^2-1) + G(R)`

`M(R^2-1)` computed at **every integer** `R <= 529 150` (two independent
segmented `mu` runs: to `10^11`, 827 s, `M(10^11) = -87856` correct; and to
`2.8x10^11`, 1476 s, reproducing `M(10^6)`, `M(10^8)`, `M(10^10)`, `M(10^11)`).
Dyadic blocks over every integer `R`; complete blocks `k = 1..18`:

| k | T = 2^k | A_2(G)/T | A_2(M(R^2-1))/T | A_2(matched')/T | A_2(G)/A_2(M) | A_2(matched')/A_2(M) | sum | corr(-G, matched') |
|---|---|---|---|---|---|---|---|---|
| 11 | 2 048 | 0.3148 | 0.2670 | 0.3678 | 1.18 | 1.38 | 2.56 | -0.086 |
| 12 | 4 096 | 0.3687 | 0.2551 | 0.4208 | 1.45 | 1.65 | 3.09 | -0.440 |
| 13 | 8 192 | 0.2551 | 0.2720 | 0.3966 | 0.94 | 1.46 | 2.40 | -0.599 |
| 14 | 16 384 | 0.3627 | 0.2520 | 0.4121 | 1.44 | 1.64 | 3.07 | -0.550 |
| 15 | 32 768 | 0.4413 | 0.2777 | 0.5689 | 1.59 | 2.05 | 3.64 | -0.850 |
| 16 | 65 536 | 0.4695 | 0.2561 | 0.4749 | 1.83 | 1.85 | 3.69 | -0.821 |
| 17 | 131 072 | 0.5155 | 0.2466 | 0.6014 | 2.09 | 2.44 | 4.53 | -0.895 |
| **18** | **262 144** | **0.7068** | **0.2530** | **0.7543** | **2.79** | **2.98** | **5.78** | **-0.942** |

Effective exponents (lower-cutoff sensitivity, upper cutoff `k = 18`,
`R < 5.24x10^5`, `X < 2.8x10^11`):

| lower cutoff | slope A_2(G) | slope A_2(M(R^2-1)) | slope A_2(matched') |
|---|---|---|---|
| k >= 5 | 1.0119 (n=14, R^2 0.993) | **0.9994** (R^2 0.999) | 1.0013 (R^2 0.995) |
| k >= 10 | 1.1173 (n=9, R^2 0.992) | **0.9996** (R^2 0.999) | 1.0962 (R^2 0.995) |
| k >= 13 | 1.2561 (n=6, R^2 0.997) | **0.9791** (R^2 0.999) | 1.1718 (R^2 0.995) |
| k >= 15 | 1.2173 (n=4, R^2 0.995) | **0.9542** (R^2 0.999) | 1.1562 (R^2 0.985) |

Readings:

* `|M(R^2-1)|` is pinned at **exponent 0.95–1.01 in `R`** (`X^{0.48}`–`X^{0.51}`)
  with `A_2/T` bounded in 0.22–0.29 across **all 18 blocks** and `R^2 >= 0.999`
  at every cutoff — the target scale, as it must be, and a good end-to-end check
  on the pipeline (the sieve, the `G` computation, and the pairing are three
  independent code paths).
* **Both pieces are individually larger than the whole, and the gap grows
  monotonically over the last four blocks**: `A_2(G)/A_2(M)` = 1.44, 1.59, 1.83,
  2.09, 2.79 and `A_2(matched')/A_2(M)` = 1.64, 2.05, 1.85, 2.44, 2.98 for
  `k = 14..18`. The scale-destruction factor `(A_2(G) + A_2(matched'))/A_2(M)`
  rises 3.07, 3.64, 3.69, 4.53, **5.78**. This is now a *measurement* over the
  common range, not an inference.
* Within-block correlation of `-G` with `matched'` reaches **-0.942** at
  `k = 18`; it is *not* monotone (-0.550, -0.850, -0.821, -0.895, -0.942 for
  `k = 14..18`). **This is not independent confirmation of anything**: once `|G|`
  dominates `|M(R^2-1)|`, `matched' = M + G` forces the correlation toward -1 by
  the identity alone. It is reported because it tracks when that dominance sets
  in.
* The paired range reaches `R = 5.3x10^5`, i.e. **above** the `R ~ 1.3x10^5`
  breakpoint by ~0.6 decades. Beyond it, combining the two separately measured
  facts (`A_2(M(R^2-1))/T` bounded near 0.25 over its whole measured range;
  `A_2(G)/T` rising to 5.78 at `R = 3.4x10^7`) gives a **conditional
  extrapolation** of the destruction factor to `~46` at `R = 3.4x10^7`
  (`X = 1.1x10^15`) — conditional on `A_2(M(R^2-1))/T` continuing near 0.25 far
  beyond where it was measured. That last figure is an extrapolation; the
  measured value at the top of the common range is 5.78.

The correlation of `G` with `-M(R^2-1)` (the quantity the task named) shows **no
stable value across normalisations and windows**: -0.310 in levels over
`R <= 10^5`, +0.078 on the `/R` scale, -0.006 and -0.102 within the decade
windows `[10^3,10^4)` and `[10^4,10^5)`. `G` does not track `-M(R^2-1)`;
`matched'` tracks `G` once `|G|` dominates.

### 2.6 Consequence for dossier constraint D4

D4 asserts a rule "with predictive content": *a split preserves RH scale in
every piece iff it partitions the summation index `{n}` itself*, and that
index-set partitions preserve RH scale (at the price of a per-piece GRH
obligation).

The canonical orientation split **is** a plain unit-weight partition of
`{m <= R^2-1}` (§2.1, with an elementary bijective proof, not just numerics),
and one class does not stay at the whole's scale. Two honest qualifications:

1. **The class is horizon-dependent**: it is a family `C_R`, not a fixed
   colouring `C ⊂ ℕ`. An `m = np` can lie in the complement while
   `sqrt(m) <~ R < p` and enter the class once `R >= p`. If D4 meant a fixed,
   cutoff-independent partition, this example sits outside that narrower reading.
2. **The class and the whole were not measured on the same long range**: `G`
   reaches `R ~ 10^8`, `M(R^2-1)` only `R ~ 5.3x10^5`. On the common range the
   separation is real and growing (`A_2(G)/A_2(M)` = 1.44, 1.59, 1.83, 2.09,
   2.79 over `k = 14..18`); its later magnitude is extrapolated.

Even so, **D4's unrestricted implication is false as a mathematical principle**,
and this does not need the numerics: an arbitrary index subset can correlate with
the coefficients — e.g. selecting the indices where `mu(n) = 1` gives a sum of
order `X`. **Index partitioning preserves unit coefficient size, not
cancellation.**

Replacement I recommend for the dossier (round-2 review's wording):

> "Being an index partition does not by itself preserve RH scale. Every piece
> requires a separate, uniform cancellation estimate. Fixed partitions whose
> indicators decompose into analytically controlled twists may inherit RH-scale
> bounds under the corresponding GRH hypotheses; moving partitions require
> uniform control of the resulting family of weights."

My own proposed criterion ("preserves scale iff the regrouped indicator carries
bounded multiplicity") was **rejected in round 2 and I withdraw it**: it is not
sufficient (bounded 0/1 weights can be chosen to correlate with `mu`) and not
necessary (`sum_{n<=X} mu(n) floor(X/n) = 1` has unbounded weights and perfect
cancellation). The usable diagnostic is two-part: (i) does regrouping amplify
coefficient `L^2` mass beyond the target scale? (ii) what uniform arithmetic
estimate controls the correlation between those weights and `mu`? There is no
purely combinatorial index-partition criterion that answers (ii).

---

## 3. GPT-5.6 adversarial review — what each round found, what changed

### Round 1 (`task-msvmrqpp-0jj1zb`, desk-only) — verdict "do not launch unchanged"

1. **CRITICAL, accepted.** Probe 1's `x < p` shortcut is unsound after the first
   above-floor stage. *Change:* exact `minviol` maintenance + `p <= minviol`
   test + full `O(N)` audits at every above-floor stage and every 512 stages.
   Re-ran the ladder; audits all clean; the fix **did** change results at
   `N = 5x10^5` (`1.003449 -> 1.004024`, 134 -> 107 above-floor stages).
2. **Accepted.** `sat_mismatch = 0` validates nothing about the greedy logic.
   *Change:* the audits are the validation; `sat_mismatch` is bookkeeping.
3. **Accepted.** Path-maximum energy hides duration/location. *Change:*
   per-stage logs, stage fractions of both maxima, cross-reported score/energy
   (now inlined in §1.2); "window energy" renamed prefix energy.
4. **Accepted.** Do not fit above-floor count vs `N`. *Change:* reported raw with
   excesses and stage fractions.
5. **Accepted; changed the headline.** Full control battery: increasing,
   decreasing, 5-seed random-order ensemble, 3-seed random tie-break,
   candidate-budget curve, admissible-fraction sampling (§1.4–§1.6). The
   admissible-fraction number exists only because of this point.
6. **Accepted.** Cross-horizon stability (§1.8).
7. **Accepted.** Probe 2 estimator switched to dyadic block RMS over every
   integer, integer-uniform weight, no running maximum, no zero-crossing
   excision, with cutoff sensitivity (§2.2); the earlier grid-only running-max
   analysis was discarded.
8. **Accepted.** The independent-`M(p-1)` null is wrong because `M(p-1)` are
   cumulative sums. *Change:* exact independent-sign `sigma(R)` and the exact
   regrouping identity (§2.3).
9. **Accepted.** `matched` on a comparable range, `M(R^2-1)` at every integer.
   *Change:* checkpoints 564 -> 316 227; sieve pushed to `10^11`.
10. **Accepted.** The complexity description contradicted the timings.
    *Change:* §1.7 splits cache rejections, strided rejections, full scans and
    element visits, measured.
11. **Accepted (bug it surfaced indirectly).** The admissible-fraction sampler
    called a shared-state RNG inside an OpenMP region — a data race. Replaced by
    a systematic sample with random start; re-measured.
12. **Partly rebutted.** It said the two-point 1.192 could not trigger the
    pre-registered `R^{1.2+}` horn — correct, and I did not use it; the horn is
    triggered by the multi-decade block-RMS fit with cutoff sensitivity.
13. **Rebutted (upheld in round 2).** Smooth prime-density proxy and dyadic-`n`
    decomposition judged redundant; round 2 agreed the proxy is reasonably
    redundant, and that the decomposition is optional once the overclaim in §2.3
    is removed (it would still help *localise* the observed cancellation).
14. **Rebutted in part.** Runs it called waste: I kept the telescoping control
    only as bookkeeping, ran an ensemble of 5 random orders rather than one, and
    dropped the uncentred random-integer control.
15. **Not done, for time (stated gap).** Held-out-`x` generalisation and an
    arithmetic-destroying surrogate for probe 1.

### Round 2 (`task-msvoo3ov-81mwtt`, desk-only) — verdict "data much stronger; several conclusions still outrun them"

Accepted and applied in full:

1. **Deleted the strongest claim in the document.** §2.3 previously said "no
   further cancellation is available in this coordinate ... the piece cannot be
   brought to `X^{1/2}` by any sharpening". Independent-sign variance is a null
   scale, **not a lower bound**; `G/sigma` is empirical. Replaced by the
   "would require cancellation substantially stronger than the independent-sign
   benchmark; these numerics neither supply nor rule out such cancellation"
   wording.
2. **Weakened both headline verdicts** to the reviewer's wordings (§0):
   probe 1 no longer says "obstructed by relocation only", "abundant" is scoped
   to *local* branching along *sampled* trajectories, and "finding a good order
   needs no sophistication" is replaced by the measured statement about batch
   size plus the note that the admissibility test is itself expensive.
   Probe 2's "the split is NOT scale-preserving" is scoped to the tested range.
3. **"Inconsistent with `R^{1+o(1)}`" removed.** Replaced by "strongly
   unsupported on the tested upper blocks", with the reasoning (excess ~0.42,
   persistent rise, no crossover) and an explicit statement that the asymptotic
   class is not excluded. The `0.015` rule is a warning threshold, not a licence
   to falsify `o(1)` claims.
4. **All `A_2` statements re-scoped to the estimator**, never to pointwise `|G|`
   (which changes sign and passes near zero).
5. **Direction error fixed.** `R = 3.2x10^5` is *above* the `1.3x10^5`
   breakpoint by ~0.39 decades, not below it.
6. **Ratio misreading fixed.** The table column was `(A_2G + A_2mm)/A_2M`; the
   individual ratios at `k = 17` are 2.09 and 2.44. §2.5 now reports both.
7. **"Monotone from k = 14" corrected** (-0.550, -0.850, -0.821, -0.895), and the
   anti-correlation is now labelled as **forced by the identity** once `G`
   dominates, not as independent confirmation.
8. **"Essentially zero" correlation** replaced by "no stable value across
   normalisations and windows".
9. **The factor `~46` is labelled a conditional extrapolation**, with its
   condition stated.
10. **`above-floor` column removed from the fixed-order controls**, where the
    counter is not computed and would be meaningless.
11. **Sampling described correctly** ("systematic sample with random start",
    "estimated fraction"), and the budget curve is labelled one run per budget
    with the "seed noise" claim withdrawn (no ensemble per `b` was run).
12. **Energy fits given lower-cutoff sensitivity** (§1.9 table).
13. **Cross-horizon conclusion weakened**: goodness at horizon `N` does not
    guarantee goodness at a larger horizon and this ordering fails transfer —
    but a horizon-independent ordering need not contain this replay as a prefix.
14. **Over-correction it identified, and I accepted its fix**: the energy
    discussion was *too* cautious. On an exact-floor path `E <= N(N+1)/2`
    deterministically, so the `N^2`-scale energy bound for the `N = 10^6` run is
    a theorem, not a fit. §1.9 now leads with that.
15. **Combinatorial hedging removed** from §2.1: the orientation class really is
    a unit-weight index subset, with an elementary bijective proof now written
    out. Caution belongs on its asymptotic scale, not on the identity.
16. **D4 discussion rewritten** (§2.6): the counterexample stands as a refutation
    of D4's *predictive heuristic*, with the horizon-dependence and
    unequal-range qualifications stated; my proposed "bounded multiplicity"
    criterion is **withdrawn** (the reviewer's counterexamples:
    bounded 0/1 weights can correlate with `mu`; `sum mu(n) floor(X/n) = 1` has
    unbounded weights and perfect cancellation), and the reviewer's replacement
    wording is adopted.

17. **Extra run triggered by round 2's point G/A**: because the paired table
    stopped short of the divergence, a second segmented sieve to `2.8x10^11`
    (1476 s, 16 threads) extended `M(R^2-1)` to every integer `R <= 529 150`,
    adding the complete dyadic block `k = 18`. That converted the
    scale-destruction factor from an inference into a measurement over the
    common range (3.07 → 5.78 across `k = 14..18`), which is exactly the
    same-range comparison the review said was missing.

Nothing in round 2 was rebutted.

---

## 4. Artifacts

**Local** (`/tmp/claude-1000/-mnt-d-Projects-prime-wheel-mobius/0d31eddd-16a5-4696-aef4-2949c1ddd542/scratchpad/`):

* `phase3_numerics_findings.md` — this document.
* `probe043/gpath.c` — probe-1 path explorer (modes 0–7: greedy smallest-prime,
  greedy random tie-break, increasing, decreasing, random order, candidate
  budget, order replay, prime-restricted greedy), with the `minviol` correctness
  fix and the `O(N)` audits.
* `probe043/greedy.c` — the first (superseded) probe-1 implementation.
* `probe043/gprobe.c` — `G(R)`, `T`, `S`, `TS`, `A`, `P`, exact `sigma(R)`,
  dyadic blocks over every integer, and the regrouping-identity check.
* `probe043/mseg.c` — parallel segmented `mu` sieve with exact checkpointed `M`.
* `probe043/mcheck.c` — plain-sieve cross-check of `M` at checkpoints.
* `probe043/orient.c` — direct computation of the orientation class sum.
* `probe043/analyze2.py`, `probe043/analyze_pair.py`, `probe043/genlist.py`,
  `probe043/genlist2.py`.
* `probe043/gpt_round1_brief.md`, `probe043/gpt_round2_brief.md` (+ head/tail
  fragments).
* `probe043/results/` — copies of `run_controls.log`, `run_ladder.log`,
  `run_mode1_1e6.log`, `run_g4.log`, `run_mseg1e11.log`, `g4_1e8.txt`,
  `run_mseg28.log`, `gp0samp2_1e5.txt`, `replay_1e6.txt`, `order_1e5.txt`,
  `g4_1e8.txt`, `g4_6e5.txt`.

**EC2** (`ubuntu@100.58.127.201:~/work/probe043/`): all sources and binaries
(`gpath gpath2 gpath3 gpath4 greedy greedy2 greedy3 gprobe gprobe2 gprobe3
gprobe4 mseg mcheck orient`); run logs `run_controls.log`, `run_ladder.log`,
`run_mode1_1e6.log`, `run_chain1.log`, `run_chain3.log`, `run_g4.log`,
`run_mseg1e11.log`, `run_mseg28.log`; per-stage logs `gp0_*.txt`,
`gp1_1000000.txt`, `gp0samp2_1e5.txt`, `replay_1e6.txt`, `order_1e5.txt`;
probe-2 data `g4_1e8.txt`, `gdump_1e8.txt`, `m_1e10.txt`, `m_1e11.txt`,
`m_28e10.txt`, `gdump_6e5.txt`, `g4_6e5.txt`, `rlist.txt`, `cplist2.txt`,
`cplist4.txt`.
