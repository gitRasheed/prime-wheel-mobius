# Errata draft — results/025 (H4 kill record)

Certifier: independent re-derivation of all eight audit findings for target `025-h4-kill`
(audit: results/029/audit.json). Sources: results/025/025.md, results/025/codex_report.md,
results/017/proposals/agent6.json, results/022/022.md. All arithmetic below re-derived by hand
and spot-checked numerically (scratchpad/check025.py): telescope identity exact for random g
and for 1_P with kernel g_P = 1_P*mu; g_P(p)=1, g_P(p^2)=-1, g_P(p^r)=0 (r>=3), g_P(pq)=-2;
edge formula H(N,B) exact with H(N,1)=M(N); Lambda-side mass constants 9, 108/(pi^2(1-2eps)),
27/pi^2, 1013 all confirmed; HB kernel g(a)=(k-1)mu(a)log a on a<=D and g(p)=(1-k)log p for
p>D confirmed exactly at k=3.

The CLOSED-KILLED verdict on H4-as-proposed SURVIVES every erratum below. Nothing here
reopens the node. The corrections are to the record's justification, scope labels, and two
stated orders of magnitude.

---

## E1 — Ground 2 retraction (audit finding 1, major, CONFIRMED)

**Wrong text (025.md, ground 2, lines 54–56):**

> 2. HB decomposes Λ, not 1_P; dividing by log n destroys the exact
>    convolution telescope. No exact scalar renewal kernel exists for
>    the prime indicator.

The existence claim is false. Every arithmetic function f satisfies f = (f*μ)*1 uniquely
(1 is Dirichlet-invertible), so 1_P has the exact scalar kernel g_P = 1_P*μ, i.e.
g_P(n) = Σ_{p|n} μ(n/p), with g_P(p)=1, g_P(p²)=−1, g_P(p^r)=0 for r≥3, g_P(pq)=−2
(numerically verified). The salvage telescope of §Q3 holds for ANY g*1 weight, hence
Σ_{n≤X} 1_P(n) M(⌊X/n⌋) = Σ_{a≤X} g_P(a) exactly (numerically verified at X=1000).
The telescope is NOT destroyed by Λ → 1_P; what is destroyed is compact support and HB
structure of the kernel. codex_report.md lines 70–75 prove only that no kernel obtained
by "merely rescaling g(a)" works — a restricted class, not an impossibility theorem;
the qualified claim ("no kernel of the proposal's form, i.e. supported on [1,D]") is true,
but by uniqueness of Möbius inversion, not by the rescaling argument.

**Replacement text:**

> 2. HB decomposes Λ, not 1_P. Passage to 1_P does not destroy the
>    telescope — the unique exact kernel g_P = 1_P*μ exists and the
>    §Q3 identity applies to it verbatim. What fails is the proposal's
>    form: g_P is not supported on [1,D] (uniqueness of Möbius
>    inversion forbids any compactly supported alternative), and its
>    absolute mass diverges — its prime values alone give
>    Σ_{p≤D} p^{−θ} ≍ D^{1−θ}/((1−θ) log D). Ground 2 is therefore a
>    support/mass statement, not an independent structural kill; the
>    kill substance is carried by grounds 1 and 3.

Corresponding fix in codex_report.md line 75: replace "the actual prime-indicator
reduction has no exact scalar renewal kernel of the proposal's form" justification
(rescaling argument) with the uniqueness argument above, or retag the rescaling step as
covering only the rescaled class.

## E2 — Ground 5 demotion and "each proved exactly" (audit finding 2, major, CONFIRMED)

**Wrong text (025.md, lines 48–49):**

> **Verdict: CLOSED-KILLED — H4 node closed on five independent desk
> grounds** (each proved exactly, no numerics):

**Replacement:**

> **Verdict: CLOSED-KILLED — H4 node closed on five desk grounds**
> (grounds 1, 3 [Λ-side], and 4 proved exactly, no numerics; ground 2
> corrected per erratum E1; ground 5 is a survey of examined repairs,
> not a non-existence theorem):

**Wrong text (025.md, ground 5, lines 64–66):**

> 5. Every internal repair (fewer levels, Harman schedule, sign
>    preservation) either removes the telescope, restores the original
>    prime object, or destroys the block structure.

The report itself carries two [OPEN] tags inside the section this ground summarizes
(codex_report.md lines 159 and 161–165: the signed localized Harman identity, and the
signed kernel Σ_a μ(a)log a·F(X/a)). An [OPEN] item is not a proof of non-existence, and
the class "internal repair" is never defined, so the universal quantifier has no referent.

**Replacement:**

> 5. No successful internal repair was supplied: fewer levels worsen
>    the polynomial divergence (proved); the Harman schedule dies on
>    the λ₁ = 1 degeneracy (erratum E5); sign preservation requires
>    new Möbius-correlation input (report [OPEN] items) — which is
>    exactly the frozen reopen condition, not a killed repair. This is
>    a survey of the repairs examined, not a proof that every repair
>    fails.

## E3 — Ground 4 scope: two-parameter repair and the H(N,1) = M(N) barrier (audit finding 3, major, PARTIAL)

The audit's mathematics is correct (independently verified): at y ≍ √X, B_a = ⌊y/a⌋ ≍ √X/a
while √(N_a) ≍ √X/√a, so B_a ≠ √(N_a) for a > 1 and the proposal's claimed self-similarity
is false. Ground 4 as written (lines 61–63) is a VALID STRUCTURAL refutation of the
proposal's stated one-parameter identification and needs no retraction — the audit's demand
to reclassify it wholesale as "quantitative" is overbroad. What IS missing from the record:
ground 4 does not foreclose inducting on the two-parameter family H(N,B) itself, and the
record never addresses that repair. It fails for a different, quantitative/circular reason:
H(N,1) = Σ_{b≤1} M(⌊N/b⌋) = M(N) (numerically verified), and the recursion drives
B_a = ⌊y/a⌋ down to 1 as a → y, so closing the family uniformly in B requires Mertens-scale
control of M at scale ≍ √X — the target itself; and with absolute values the kernel mass
still diverges by ground 3.

**Wrong text (025.md, lines 78–79):**

> Frontier delta: **node-closure** (H4 dead as proposed; kill grounds
> 1, 2, 4 are structural, not quantitative).

**Replacement:**

> Frontier delta: **node-closure** (H4 dead as proposed; grounds 1 and
> 4 are structural refutations of the proposal as stated, ground 2 as
> corrected [E1] is a support/mass statement). Ground 4 refutes only
> the proposal's one-parameter self-similarity; the formal repair of
> inducting on the two-parameter family H(N,B) is not foreclosed by it
> and dies instead on circularity — H(N,1) = M(N), so the family
> contains the Mertens target itself, and the recursion reaches B = 1
> at a ≍ y — plus the ground-3 mass divergence under absolute values.

## E4 — Ground 3's Λ→primes bridge is a model, not a proof (audit finding 4, major, CONFIRMED)

**Wrong text (codex_report.md, lines 99–108, tag and inequality):**

> [NEW-BUT-PROVED-HERE (proof: on the extended range 2≤n≤X, 1/log n≥1/log X)]
> Even granting the maximally favorable uniform suppression 1/log X needed
> to pass from Λ to primes, m_P(D;θ) ≳ m_Λ(D;θ)/log X.

and (lines 136–140) the general-k form m_P(D;θ) ≳ ((k−1)/k)D^{1−θ}.

The quantity m_P is never defined — no prime kernel of the proposal's form exists (report's
own Q1 RESULT) — and Möbius inversion is not pointwise division by log, nor is it
positivity-preserving, so |g_Λ(a)|/log X does not lower-bound |g_P(a)|. The exact prime
kernel g_P = 1_P*μ carries no k-dependence, so ((k−1)/k)D^{1−θ} cannot literally describe
it. The [NEW-BUT-PROVED-HERE] tag is wrong; the correct tag is a charitable MODEL. The
divergence CONCLUSION survives by the exact-kernel route: Σ_{p≤D}|g_P(p)|p^{−θ} =
Σ_{p≤D}p^{−θ} ≍ D^{1−θ}/((1−θ)log D). The Λ-side computation is fully rigorous — every
constant re-verified: |g(a)| = 9μ²(a)log a; Σ_{a≤D} μ²(a)(log a)a^{−θ} ~
D^{1−θ}log D/(ζ(2)(1−θ)); at θ = 1/2+ε this is (108/(π²(1−2ε)))D^{1/2−ε}log D; at θ = 1 it
is (27/π²)(log D)² after the factor 9; Σ_{j=2}^{10}|c_j| = 2¹⁰−1−10 = 1013.

**Replacement (tag and framing):** retag lines 99–108 and 136–140 as
[MODEL — charitable scalarization, non-rigorous bridge]; add the exact-kernel divergence
Σ_{p≤D} p^{−θ} ≍ D^{1−θ}/((1−θ)log D) as the rigorous prime-side statement.

## E5 — The Harman/sieve branch was never killed by the stated grounds; add the λ₁ = 1 kill (audit finding 5, major, CONFIRMED)

The proposal (agent6.json) explicitly offers "(or a Harman-sieve schedule)" and asserts the
sieve weights λ± = Σ_{d|n, d≤D} λ_d are "themselves of this (g*1) form". That assertion is
TRUE: the kernel g(d) = λ_d·1_{d≤D} is genuinely supported on [1,D]. Hence ground 1
(support) does not apply, ground 2 does not apply, and ground 3's g(a) = (k−1)μ(a)log a
mass computation does not apply. The record's only treatment is the one-line assertion at
codex_report.md line 151, tagged [NEW-BUT-PROVED-HERE] with no proof. The actual kill,
verified here: normalized sieve weights have λ₁ = 1, so the a = 1 term of the renewal
inequality T(x) ≤ Σ_a |g(a)|(1 + c_a T(x/a)) contributes T(x) to its own right-hand side
and the induction is vacuous before any mass question arises — precisely the degeneracy the
HB kernel escapes, since g(1) = (k−1)μ(1)log 1 = 0. (Equivalently: the a = 1 edge term
λ₁·H(N₁,B₁) is the full same-scale edge with coefficient 1.) Additionally, upper/lower
sieve inequalities cannot replace 1_P inside a sum weighted by the sign-changing M(x/n)
without one-sided majorant use, which the proposal forbade itself ("never as majorants").

**Insertion (after ground 5 in 025.md):**

> Sieve-branch note: the proposal's alternative Harman/β-sieve
> schedule is NOT reached by grounds 1–3 (its kernel g(d) = λ_d·1_{d≤D}
> genuinely has compact support). It dies separately and immediately on
> λ₁ = 1: the a = 1 renewal term contributes T(x) to its own bound and
> the induction is vacuous — the degeneracy HB's g(1) = 0 avoids —
> and majorant substitution inside the signed M(x/n) pairing is
> forbidden by the proposal's own "never as majorants" constraint.

## E6 — Rung-0 deliverable: redundant, not killed (audit finding 6, minor, CONFIRMED)

**Wrong text (025.md, line 81):** "... H4 killed (this record)." — blanket closure. The
proposal's independent rung-0 deliverable S ≪ x·exp(−c(log x)^{3/5−ε}) is untouched by all
five grounds. No live loss: results/022 already banks "S = o(x) is already KNOWN via
pointwise VK PNT + triangle inequality", and the stated shape follows in one line — for
d ≤ K = x/(y+1), x/d ≥ y+1, so |S| ≤ Σ_{d≤K}|R(⌊x/d⌋)| ≪ x·e^{−cΦ(y)}Σ_{d≤K}1/d ≪
x log x·e^{−cΦ(y)} with Φ(t) = (log t)^{3/5}(loglog t)^{−1/5}, which at y ≍ √x is exactly
the stated bound (log x absorbed into the exponent's ε). This also falsifies the
proposal's claim that the product-savings route's named deliverable is "strictly better
than any termwise triangle bound" — at the stated strength the termwise bound already
delivers it (the product route could still beat it by a second savings factor, but that
stronger form was never the named deliverable).

**Replacement:** append to line 81: "H4 killed (this record; the proposal's separate
rung-0 deliverable S ≪ x·exp(−c(log x)^{3/5−ε}) is not killed but REDUNDANT — equal
strength already banked in 022 via the termwise VK triangle bound)."

## E7 — Salvage telescope: true, but not novel (audit finding 7, minor, CONFIRMED)

**Wrong framing (025.md, lines 68–71):** the identity Σ_{n≤X}(g*1)(n)M(⌊X/n⌋) = Σ_{a≤X}g(a)
is TRUE (re-verified: exact for real X ≥ 1 and arbitrary g, no M(0) convention needed), but
the [NEW-BUT-PROVED-HERE] tag / the proposal's "NEW leverage" framing is wrong: g = δ gives
the classical Σ_{n≤X} M(⌊X/n⌋) = 1 (verified at X = 10, 100, 997, 1000), and the general
identity is that classical fact convolved with g — a one-line corollary of μ*1 = δ along
the hyperbola.

**Replacement:** in the Salvage paragraph, after "is TRUE", add: "(a one-line corollary of
the classical Σ_{n≤X} M(⌊X/n⌋) = 1, i.e. μ*1 = δ along the hyperbola — worth formalizing
but not new leverage)".

## E8 — Two dropped log factors in ground 3's headline (audit finding 8, minor, CONFIRMED)

**Wrong text (025.md, lines 58–60):**

> at the rung-2 scale weight a^{−(1/2+ε)} its absolute mass is
> ≍ D^{1/2−ε} — polynomially divergent (even the proposal's
> too-favorable a^{−1} weight gives ≍ log D, not < 1).

The true asymptotic at θ = 1/2+ε is (108/(π²(1−2ε)))·D^{1/2−ε}·log D — the log D factor is
dropped, so "≍ D^{1/2−ε}" is the wrong relation as written. The raw a^{−1} mass is
(27/π²)(log D)², not ≍ log D; the "log D" figure silently imports the non-rigorous
1/log X = 1/(10 log D) prime normalization of erratum E4. Both drops are conservative
(actual masses larger), so the kill is unaffected.

**Replacement:**

> at the rung-2 scale weight a^{−(1/2+ε)} its absolute mass is
> ≍ D^{1/2−ε} log D — polynomially divergent (even the proposal's
> too-favorable a^{−1} weight gives raw mass ≍ (log D)², still ≍ log D
> after the charitable 1/log X prime normalization of E4, not < 1).

---

## Not errata (verified correct, no change needed)

- Ground 1 (support failure): exact; g_j(p) = c_j log p and g(p) = (1−k)log p = −9 log p for
  p > D, k = 10; verified numerically at k = 3.
- Ground 3 Λ-side: all four constants (9, 108/(π²(1−2ε)), 27/π², 1013) re-derived and
  numerically confirmed.
- Ground 4's refutation of the stated self-similarity: exact (B_a ≠ √N_a for a > 1).
- Salvage telescope and edge formula H(N,B) = 1 − Σ_{d≤⌊N/(B+1)⌋} μ(d)(⌊N/d⌋−B): both exact,
  verified including boundary cases B = 0, B = N.
- The CLOSED-KILLED verdict and the frozen reopen condition (signed contraction for the
  (k−1)μ(a)log a kernel / norm-<1 edge operator): stand unchanged.
