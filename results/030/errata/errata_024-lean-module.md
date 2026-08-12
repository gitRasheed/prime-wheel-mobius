# Errata draft — target 024-lean-module (results/029 certification)

Certifier: independent re-derivation of all six audit findings (2 fatal, 2 major,
2 minor). All six CONFIRMED; scoping remarks on findings 5 and 6 below. Sources
corrected: results/024/024.md, JOURNAL.md entry 2026-08-09-32, and (proposed, for
a future docstring-only Lean PR — no proof changes) the module docstring of
RHLean/Analysis/PrimeSieveBackwardAffineExcursion.lean.

Verified numerically: at H = y, floor(H/2C) = 3, 6, 10, 13 at y = 10^3, 10^6,
10^9, 10^12, i.e. -> (1/4)log x, never anywhere near sqrt(x); with the record-023
constants (A = 1 + H_K/log(y+1) ~ 2.03, B = K/log(y+1)) the window (H/2 - B)/A
is ~ 0.21*sqrt(x). The record's own displayed min is evaluated backwards:
min(sqrt(x), H*log x/sqrt(x)) at H ~ sqrt(x) is Theta(log x), the SMALLER branch.

---

## E1 — results/024/024.md, Results paragraph (fatal; findings 1 + 2)

WRONG (024.md lines 71-74):

> "All five declared items delivered; nothing dropped, no extra
> hypotheses smuggled in. At canonical pins the excursion window is now
> W = min(y+1, ⌊H/2C⌋) ≍ min(√x, H·log x/√x): with H ≍ y (the
> record-023 scale) this is W ≍ √x — the upgrade from W ≍ log x."

REPLACEMENT:

> "Items 1 and 2 delivered in full; items 3 and 5 delivered only in the
> degenerate C·(t+1) form (slope = intercept = C(y,x₀) = 1 + y/log(y+1)
> ≍ √x/log x), NOT with the record-023 constants (harmonic-sum slope
> A = 2+o(1), intercept B = K/log(y+1)); item 4 (the two-constant A·t+B
> abstract excursion lemma, both directions, B < H/2, window (H/2−B)/A)
> was dropped — no A·t+B shape exists in the module. Consequently the
> backward window is W = min(y+1, ⌊H/2C⌋), and with H ≍ y this is
> ⌊H/2C⌋ ≈ H·log(y+1)/(2y) ≍ (1/4)·log x: W ≍ log x, the SAME order as
> record 020's forward window (and, since the y+1 cap cannot bind at any
> realistic height, the same number). The window length was not upgraded.
> W ≍ √x would follow only from the record-023 slope, which remains
> unformalized; the crude K(h+1) relaxation (primeSieveFloorIncrementSum_le,
> inherited from record 020) is still the constant actually used."

## E2 — results/024/024.md, frontier-delta sentence (major; findings 3 + 4)

WRONG (024.md lines 75-77):

> "Frontier delta: **formalization-support + machinery-upgrade** (the
> pinned-to-windowed transfer now actually fires at the program's own
> sample points)."

REPLACEMENT:

> "Frontier delta: **formalization-support + applicability** — the backward
> machinery is stated at canonical pins where the forward hypotheses were
> provably vacuous (x₀ % (y+1) = y forces the forward window empty), and
> its hypotheses reduce to 1 ≤ y. CAVEAT: no kernel theorem witnesses that
> primeSieveBackwardWindow y ≥ 1 — when H < 2C the window is 0, the
> excursion quantifier is empty, and the moment bound degenerates to
> 0 ≤ 0. The transfer 'fires' only given the unproved height certificate
> H ≥ 2C(y,x₀) ≍ 2√x/log x (H ≥ 4C to reach the first genuine backward
> point t = 1). A one_le_primeSieveBackwardWindow certificate, analogous
> to the forward module's one_le_primeSieveExcursionWindow, should be
> added before any use of the moment bound."

## E3 — results/024/024.md, window bullet (major; finding 4, minor finding 5)

WRONG (024.md lines 61-65):

> "`primeSieveBackwardWindow` = min(y+1, ⌊H/2C⌋) with excursion
> theorem (H/2 persists on the whole backward window) and the
> 2k-th moment lower bound (H/2)^{2k}·W ≤ Σ_{t<W}‖S(y,x₀−t)‖^{2k} —
> record 020's transfer with the vacuous forward hypotheses REMOVED
> at canonical pins: hypotheses are now just 1 ≤ y."

REPLACEMENT:

> "`primeSieveBackwardWindow` = min(y+1, ⌊H/2C⌋) with excursion theorem
> and 2k-th moment lower bound; hypotheses are just 1 ≤ y, but the
> theorems are contentful only when the window is nonempty, which nothing
> in the kernel set certifies (see caveat above). The y+1 cap is
> decorative: it binds only when H ≥ 2C(y+1) ≍ 4x/log x, which no
> admissible height reaches (unconditionally H = o(x/log y) by
> Vinogradov–Korobov, already in hand from record 022; and at the
> program's own scale H ≍ y the uncapped branch is ≍ (1/4)log x ≪ y+1
> at every finite scale)."

## E4 — results/024/024.md, floor-fact bullet (minor; finding 6 — flagged
LOAD-BEARING: it contains both a false documentation claim in a merged kernel
module and the concrete repair path for E1)

WRONG (024.md line 57):

> "`floor_add_div_sub_le`: sharp per-d bound ⌊(x+h)/d⌋−⌊x/d⌋ ≤ h/d+1."

REPLACEMENT:

> "`floor_add_div_sub_le`: per-d bound ⌊(x+h)/d⌋−⌊x/d⌋ ≤ ⌊h/d⌋+1 (the
> exact per-d maximum is ⌈h/d⌉, so the bound is off by one when d ∣ h).
> NOTE: this lemma and floor_succ_div_sub_eq_divisor_indicator are
> currently unused by any theorem in the repository — the affine constant
> in the increment bound comes from the crude K(h+1) relaxation, not from
> these. They are recorded content, not working machinery."

## E5 — JOURNAL.md, entry 2026-08-09-32 (fatal; findings 1 + 2)

WRONG (lines 566-568):

> "Excursion window at canonical pins upgraded W ≍ log x → W ≍ √x (at H ≍ y)."

REPLACEMENT:

> "Excursion machinery made applicable at canonical pins (backward
> direction; forward version was vacuous there). Window length NOT
> upgraded: with the formalized constant C ≍ √x/log x the window stays
> W ≍ log x at H ≍ y; the W ≍ √x claim required the record-023 slope
> A = 2+o(1), which was not formalized. No nonemptiness certificate for
> the backward window exists in the kernel set. [Corrected per
> results/029 certification.]"

## E6 — Proposed docstring corrections, PrimeSieveBackwardAffineExcursion.lean
(docstring-only; no proof or statement changes; kernel set #5 theorems are
correct as proved)

WRONG (lines 18-20):

> "the affine increment bound applies to every backward step `t <= y`, and
> the excursion and moment machinery runs on a window of full length at
> the canonical pin."

REPLACEMENT:

> "the affine increment bound applies to every backward step `t <= y`; the
> excursion and moment machinery then runs on the window
> `min (y+1) ⌊H/(2C)⌋`, which is nonempty only when `H ≥ 2C` — a height
> hypothesis this module does not certify."

WRONG (lines 22-24):

> "The module also records two exact floor facts underlying the affine
> constant: the unit-step floor jump is precisely the divisor indicator of
> `x + 1`, and a general step obeys the sharp `h/d + 1` bound."

REPLACEMENT:

> "The module also records two exact floor facts (currently unused by the
> increment bound, whose constant comes from the crude `K*(h+1)`
> relaxation in `PrimeSieveLipschitzExcursion`): the unit-step floor jump
> is precisely the divisor indicator of `x + 1`, and a general step obeys
> `⌊(x+h)/d⌋ − ⌊x/d⌋ ≤ h/d + 1` (exact per-`d` maximum: `⌈h/d⌉`)."

## Repair path (verified sound, bounded Lean scope; from audit notes, re-derived)

Prove Σ_{d ∈ Icc 1 K} (⌊(x+h)/d⌋ − ⌊x/d⌋) ≤ h·H_K + K via the already-proved
floor_add_div_sub_le (H_K = Σ_{d≤K} 1/d), thread through
primeSieveMoebiusPrefixSum_increment_norm_le (whose Li half is already stated
against the exact floor-increment sum) to get |ΔS| ≤ A·t + B with
A = 1 + H_K/log(y+1) = 2+o(1), B = K/log(y+1); state the abstract two-constant
excursion lemma (declared item 4) with window ⌊(H/2 − B)/A⌋; redefine or
supplement primeSieveBackwardWindow accordingly; add
one_le_primeSieveBackwardWindow. Only then is W ≍ √x at H ≍ y a defensible
record claim (numerically ≈ 0.21·√x).
