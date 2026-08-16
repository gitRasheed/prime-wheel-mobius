# Record 043 — certified kill report (gate option (b))

Scope of this document: it closes record 043 under gate option (b) by naming
every mechanism the round proposed, the argument that killed it, and who
verified that argument. It also records the round's positive residue and the
phase-3 outcome for each thread, the measurement reattributions the
verification phase forced (including one falsification of a frozen dossier
constraint, §4.0), and the registry entries the orchestrator should merge.

Sources, in order of authority:

1. `results/043/phase2_killpanel.md` — the eleven Opus refuter verdicts. The
   `verify-*` sections are the authoritative record; where a `verify-*`
   section narrows or corrects a phase-1 proposal's prose, the narrowed
   version is what this report states.
2. `results/043/gpt56_osp_verdict.md`, `gpt56_mfd_verdict.md`,
   `gpt56_emi_verdict.md` — independent GPT-5.6 desk reviews of the three
   positive routes.
3. `results/043/phase1_proposals.md` — the twelve generators' output.
4. `results/043/dossier.md` — the frozen constraint set this round ran under
   (target Prop, machinery B1–B10, constraints D1–D7, registry E, threads F).
5. `results/043/phase3_numerics_findings.md` — the phase-3 numerics, itself twice
   GPT-5.6-reviewed. Its scopings are binding for §3 and §4.0 and are carried
   here unbroadened.

Nothing in this report is a bound on `M`. Claims below are of four kinds and
are marked as such where it is not obvious from context: exact identities
(with the verification that checked them), counting facts, measured numbers
with their window and scale, and scoped negative statements. Asymptotic
language (`≍`, `o(·)`, `X^{1/2+o(1)}`) is used only where a proof or a
classical theorem is cited; measurements are reported as measurements.
Assertions that were not independently verified are labelled in place and
listed again in the closing ledger.

---

## 1. Mechanism kills

### 1.1 The three positive routes

Each was independently reviewed by two Opus refuter lenses and one GPT-5.6
desk review, and all nine verdicts were KILL. Where the reviewers' grounds
genuinely differ, that is said explicitly below; where they converge on the
same argument, no independence is claimed for it.

**renewal-b/overlap-square-pin (OSP).** Reviewed by `osp-constraints`,
`osp-math`, `gpt56_osp_verdict`; all three KILL. The pin identity
`M(A)^2 + M2(A^2) = 2·S_A(A^2)` (with `S_A(X) = Σ_{u≤A} μ(u) M(⌊X/u⌋)` and
`M2` the summatory of `μ*μ`) is correct — `osp-constraints` verified it for
88 values of `A ≤ 2000` and `osp-math` for every `A = 0..500`, both computing
`M2` independently by Dirichlet convolution rather than through the identity.
It is the classical Dirichlet hyperbola for `μ*μ` at the symmetric cutoff
`A·B = A^2`. The mechanism is nonetheless empty. `J(A) := 2·S_A(A^2) − M2(A^2)`
is identically `M(A)^2`, so the proposal's "single signed combination J" is
the target with two extra symbols beside it, and its chain contains no
inequality step anywhere. `osp-constraints` checked that
`M2(x) ≪ x^{1/2+ε}` for every `ε > 0` is equivalent to RH (via
`1/ζ(s)^2 = s∫M2(x)x^{-s-1}dx`, so convergence for `σ > 1/2` makes `1/ζ^2`
analytic there; converse standard), so the second term is RH-equivalent at
the relevant exponent. It also asserted the same status for
`S_A(A^2) = (M(A)^2 + M2(A^2))/2`; this report records only the direction
that is established — RH implies the corresponding `S_A` bound — since the
identity alone does not exclude cancellation between the nonnegative
`M(A)^2` and a large negative `M2(A^2)`, so an isolated bound on `S_A` is not
shown here to imply RH. The deferred leverage — `Σ_{A≤T} M(A)^2 ≪ T^{2+ε}`
for every `ε`, obtained by A-averaging — is itself RH-equivalent by dyadic
Cauchy–Schwarz on the Mellin integral; all three reviewers derived this, and
GPT-5.6 cites the standard Mertens/RH equivalence. It is the same argument in
three hands, not three independent grounds. The proposal's own honest
weakness (3) is therefore wrong in the safe direction: a full averaged win
does not "yield only `M ≪ T^{2/3+ε}`", it yields RH. The claimed A-averaging
gain does not survive as an exponent: `osp-constraints` measured gains
16.49/20.52/9.38/26.74 across `T = 125..1000` (dyad-to-dyad slopes
−1.13/+1.51/+0.32) and `osp-math` 6.21/42.1/11.7/1148/7.53/5.44/8.92/5.06
across `T = 125..16000`, with the two extreme values sitting exactly at the
observable's zero crossings — there is no stable fitted power law in the
tested range, and per §5 R2 no such fit on this observable would be decisive
anyway. The kill rests on the algebra and the RH-equivalence, not on these
numbers. The `μ^{*k}` tower as proposed does not close: each rung is one
equation introducing a new unknown `M_{k+1}` at scale `A^2`, and the level-2
pin exposes the nonnegative block `M2(A)^2`, whose bound at `A^{1+ε}` is
RH-equivalent (D3(c)). Scale flow is upward (`S_A` reads `M` at arguments up
to `A^2`), so the proposed identity-only tower supplies no descending
recurrence and no closed induction. May **not** be resubmitted: the pin as
leverage rather than substrate; the "free unconditional inequality"
`M2(A^2) ≤ 2·S_A(A^2)`, which is `M(A)^2 ≥ 0` in other letters; and
A-averaging of this identity as a source of power saving (see §5 R5 for the
scope of the general averaging statement — it is narrower than "averaging
never helps"). Named revival condition (`osp-constraints` item 5, `osp-math`
item 3; neither reviewer expects it met): an inequality relating
`2·S_A(A^2)` to `M2(A^2)` that is **not** derived from the identity — an
independent upper bound on `S_A(A^2)` proved without knowing `M2`, or a
non-tautological relation among `M`, `M2`, `M3` at the square pins that
constrains the joint object rather than re-expressing it.

**involution-a/mult-fiber-package-discharge (MFD).** Reviewed by
`mfd-constraints`, `mfd-math`, `gpt56_mfd_verdict`; all three KILL, on three
genuinely different grounds (counting; untethered instantiation; internal
contradiction between the theorem and the measured object). *Counting.* The
new coordinate `D(K)` is unconditionally small with no cancellation used: at
most three defect labels per ordered odd prime pair (`mfd-math` enumerated
all 512 label subsets; max defect cardinality is exactly 3), each carrying
one bounded corrected weight, and `#{(p,q) : p²q² ≤ x} = #{pq ≤ √x}`, which
is `≍ √x·loglog√x/log√x` and hence `o(√x)` by Mertens (the leading constant
depends on the ordered/unordered and distinctness conventions and is not
load-bearing here). `mfd-constraints` measured the label-count proxy
`3·#pairs/√x` decaying 1.19 at `x = 10^7` to 1.01 at `x = 10^12` and tending
to 0; `mfd-math` measured `#pairs` at 792..3864 over `4K = 4·10^6..10^8` with
fitted exponent 0.4939, i.e. `#pairs/√x` in roughly `[0.337, 0.397]` across
the combined window. The reviewers disagree on the per-site constant
(`mfd-constraints` and GPT-5.6: `|weight| ≤ 1`; `mfd-math`: values in
`{−3,−1,0,1,3}`, which makes the safe multiplier 9 rather than 3), and the
counting conclusion is the same under any of them — a uniformly bounded
single-level aggregation is `o(√x)`. Because the bound is `o(√x)` — strictly below the
target scale, not merely at it — `D(K)` cannot carry the `Ω_±(√x)` mass of
`M`, so 100% of the difficulty stays in the "renewal telescope main term",
which the proposal concedes is the registered stall in step (2) and then
assumes away in the quantitative claim. *Untethered instantiation.*
`sum_correctedCollisionSiteWeight_prefix_eq_defect` selects labels by the CRT
frontier but evaluates weights through an arbitrary `site` function; the
proposed `site(a,b) = p^a·base(b)` never touches
`collisionExponentStateResidue`, and `mfd-math` grepped the whole tree and
found no lemma anywhere connecting a collision frontier sum to any Mertens,
three-slot or Möbius prefix, for any site map. *Internal contradiction.* The
numerics carrying the entire evidential case (`defect_agg2.py`, weight = `μ`
at the CRT cofactor `(4·kcell+a+1)/p²`) use exactly the realization the same
submission's companion proposal certifies violates `hother` — theorem,
numerics and target are three different objects. Additionally the B4 "fiber
drift" charge is inapplicable rather than merely lossy: the shipped modulus
is gated by `t ≤ y` at `pin = (y+1)²−1`, while a `p`-shift moves evaluation
from `x` to `x/p`. May **not** be resubmitted: the submitted single-level
per-(p,q) bounded-defect aggregation, which by the counting fact is `o(√x)`
and therefore cannot be a reduction of `M`; any citation of B4 to charge a
macroscopic (`x → x/p`) displacement; the "first non-vacuous full
instantiation of the B7 package" novelty claim (the submission's own class
notes exhibit `site(0,b)=1, site(1,b)=2, site(2,b)=4` as an equally
non-vacuous discharge). A multi-level version is not categorically excluded
but inherits a factor `≈ π(√x)` and must exhibit the cross-level
cancellation explicitly — which is the original problem. Named revival
condition (`mfd-math` item 4): a Lean theorem of the form "`Σ` over
`collisionExponentStatePrefixFrontier p q K` of
`correctedCollisionSiteWeight S upper site s` = an explicit piece of
`mertensSummatory (4K)`", for the **same** site map that discharges the
package. `mfd-constraints` adds that any resubmission must lead with the
renewal term `R(K)`, not with `D(K)`, since `R(K)` is `Ω_±(√K)`.

**wildcard/excursion-moment-interpolation (EMI).** Reviewed by
`emi-constraints`, `emi-math`, `gpt56_emi_verdict`; all three KILL, on the
same Mellin-strength argument plus (from `emi-math`) an independent
domination computation. The excursion lemma is correct — `emi-math` found
zero violations for all `K_0 ≤ 5·10^5` at the tightest legal `K` for
`m = 1,2,3`, and it survives deletion of the `+9` slack. The load-bearing
claim that each finite-`m` obligation is "strictly weaker than the target" is
false at the rung the ladder actually uses. Write `Θ := inf{θ : M(x) ≪_ε x^{θ+ε}}`.
Hölder against 1 gives `E_1 ≤ E_m^{1/m}·K^{1−1/m}`, and
`E_m(K) ≪_{m,ε} K^{1+2mθ+ε}` for every `ε > 0` is equivalent to `Θ ≤ θ` (⇒ by
Hölder, then the elementary endpoint bridge `|M(t) − M(4k)| ≤ 3` on
`[4k, 4k+4)` which turns the sampled `E_1` bound into
`∫_1^X M(t)^2 dt ≪ X^{2+ε}`, then the classical Mellin/Plancherel argument on
`1/(sζ(s)) = ∫M(t)t^{-s-1}dt`; ⇐ trivially). At `θ = 1/2` — the value the
proposal's input assumes — that is RH at every `m`; at a single fixed `δ > 0`,
`E_1 ≪ K^{2+δ}` gives the fixed zero-free half-plane `Re s > 1/2 + δ/2`, and
RH requires the family over every `δ`. All three reviewers derived this;
GPT-5.6 cites Titchmarsh 14.25(B–C). Independently, the converter is
uniformly dominated: with input `E_m ≪ K^{1+2mθ+ε}` the ladder returns
`M ≪ K^{(1+2mθ)/(2m+1)}` while Hölder+Mellin returns `M ≪ K^{θ+ε}`, a gap of
`(1−θ)/(2m+1) > 0` for every `θ < 1` (`emi-math`'s table at `θ = 0.5`: ladder
0.6667/0.6000/0.5714/0.5238 for `m = 1,2,3,10` against classical 0.5000). So
the advertised "quantitative progress at the first rung, `M ≪ x^{2/3+ε}`,
below the certified `x^{3/4}` ceiling" is a strict downgrade of what the same
hypothesis already gives classically. Every nontrivial rung encodes a
nontrivial zero-free result: any `E_1 ≪ K^{3−δ}` yields `Θ ≤ 1 − δ/3` by the
oscillation trick, i.e. a fixed zero-free half-plane, and the best
unconditional input known gives only `K^3/exp(c(log K)^{3/5}…)`. The `m = 1`
opening is D5-closed — `emi-constraints` verified bit-exact that
`E_1(K) = Σ_{m,n≤4K} μ(m)μ(n)·(K+1−⌈max(m,n)/4⌉)`, a nonnegative max-type
kernel — and the named fallback (B9 centred pieces) carries the `muRho`
pathology measured at `N^{+0.485}`. May **not** be resubmitted: this ladder
on pure even power sums of `M` at the RH exponent, in any `m`; any framing of
such a moment as a weaker intermediate; a smoothed or weighted scale moment
swapped in without first exhibiting the Mellin strength of the smoothed
object. Named revival condition (`emi-math` item 5, stated for completeness
and not endorsed): a moment-type hypothesis provably **not** RH-equivalent
that still feeds a sup bound below `x^{3/4}` — for example a restricted or
weighted moment where Hölder cannot reach `E_1`. Note the domination result
applies to any pure moment of `M` at any `θ ≤ 1` (with equality only at
`θ = 1`, and `θ > 1` disposed of by the trivial bound `M(x) ≪ x`), so even
where such a hypothesis is not RH-equivalent — `θ = 0.7`, say — the excursion
converter still adds nothing over the classical transfer. A revival needs a
hypothesis the classical route cannot consume.

### 1.2 The four clean mechanism kills inside the nulls

`verify-null-certificates` checked all six no-viable-mechanism sections,
reproduced every central identity numerically, and endorsed exactly these
four as clean kills of **named mechanisms** — kills "of the variants actually
tried", not of classes (its items 6 and its verdict summary).

**moment-a: the `C_p ≥ 0` monotonicity hypothesis.** Prime-insertion
filtration energy monotonicity, in the form the null proposed, is dead.
Using the exact one-step identity
`E_{S∪p}(N) = E_S(N) + p·E_S(⌊N/p⌋) − r_p − 2C_p(N)` with `r_p ≥ 0` and
`C_p(N) = Σ_X g_S(X)g_S(⌊X/p⌋)`, `C_p ≥ 0` at every step would telescope to
`Σ_{X≤N} M(X)^2 ≤ (6/π²+o(1))N²`. It is refuted directly: `C_p < 0` at a large fraction of steps in increasing
prime order and, in `verify-null-certificates`'s own greedy `√x`-optimal
order, at 92/303, 226/669, 506/1229 and 997/2262 steps at
`N = 2000, 5000, 10000, 20000` — i.e. 30.4%, 33.8%, 41.2%, 44.1%, rising with
scale. (The verifier's summary figure "41–44%" describes only its two largest
scales; the full greedy range is 30–44%.) The hypothesis is therefore dead in
both orders tested. Accompanying **measurement**, over the stated window and not an
impossibility theorem: in increasing order the intermediate energies reach
`max_j E_j/N² = 9.49 / 60.0 / 149.8` at `N = 10^4 / 10^5 / 3·10^5` (peak at
`p ≈ 0.30N`), with negative correlation mass of the same size;
`verify-null-certificates` independently reimplemented this and matched to
three digits (9.488, 59.998; peak at `p/N = 0.297–0.298`; negative mass
9.694, 62.093; `p ≤ √N` truncation 0.472, 2.872). May **not** be resubmitted:
`C_p ≥ 0` as an order-independent hypothesis, or in either of the two orders
tested (increasing, and the greedy `√x`-optimal order). Not killed, and
explicitly left open: other per-step flux conditions, centered variants, and
a specially constructed insertion order not yet tested — the proposal's
own claim that "first-order centering reduces it to the registered renewal
stall" is the proposal's, and `verify-null-certificates` did not verify it.
Revival condition as the proposal stated it: an arithmetically exact
centering `A_S` whose correction terms telescope rather than accumulate, with
measured `max_S Σ_X h_S(X)^2 = O(N²·polylog)`. `verify-null-certificates`
judged that redirect misdirected: its greedy probe reaches `max E = 0.30·N²`
with **no** centering at all, so the cheaper observed lever is ORDER, and
moment-a's "fourth measured horn" framing should be restated as a property of
the increasing-order coordinate rather than of the skeleton.

**moment-b: the gcd coordinate is a total relocation.** For squarefree
`m,n` with `g = gcd(m,n)`, `M(x)^2 = Σ_g μ²(g) C_g(⌊x/g⌋)` with
`C_g(z) = Σ_{m,n≤z, (m,n)=1, (mn,g)=1} μ(m)μ(n)`, and the inverse
`C_g(z) = Σ_{e sf, (e,g)=1} μ(e) M_{ge}(⌊z/e⌋)^2`; composing the two returns
`M(x)^2 = M(x)^2` via `λ = (μ²)^{-1}`. `verify-null-certificates` verified
both directions exactly (collapse at `x = 2000`; inversion at
`(g,z) = (1,200), (2,200), (15,200)`). Measured accompaniment: the
triangle-over-`g` sum `T(x) = Σ_g μ²(g)|C_g(⌊x/g⌋)|` has
`T(x)/(x log x)` in `[0.40, 0.50]` over `x = 10^3..10^6` (phase-1 values
0.446, 0.485, 0.403, 0.492, 0.443, 0.458, 0.421; `verify-null-certificates`
independently reproduced 0.4605 at `x = 2000`). No asymptotic claim about
`T(x)` is made or proved; over the tested range the triangle bound loses no
scale, which is why the coordinate needs no cross-layer cancellation there —
so in the tested regime 100% of the RH content sits inside individual layers,
each an exact copy of the problem at scale `x/g`. The submitted per-layer
inversion opens into the rough squares `M_{ge}(z/e)^2`, and bounding those
uniformly in `g` is RH-equivalent both ways (D3(c)); no claim is made about
every conceivable layer-opening. May **not** be
resubmitted: the submitted per-layer opening via uniformly bounded rough
squares. Not killed: cross-layer inequalities of a different shape — neither
the exact inversion nor the finite-range triangle measurement excludes them.
The null's own scope residual — that it kills second-moment EXPANSIONS, not
second-moment TARGETS — stands, though §5 R5 independently closes the
unweighted full-prefix case. The `θ*` pre-screen bundled with this null is
arithmetically wrong as shipped; see §5 R1.

**renewal-a: sign-blind insertion into the square-cutoff renewal skeleton is
expansive.** On main, `SquareRootPositiveSmoothCollapse.lean` already
kernel-verifies `M(R²−1) = −Σ_{q≤R prime} M(q−1) + matched(R)`
(`verify-null-certificates` confirmed the file exists and states exactly
this, and confirmed the identity to the integer at `R = 100, 316, 1000`).
Inserting a hypothesis `H(θ): |M(y)| ≤ C·y^θ` sign-blindly through the
prime-sampled piece `G(R) = Σ_{p≤R} M(p−1)` gives
`|G(R)| ≤ C·R^{1+θ}/log R`, i.e. exponent `(1+θ)/2` in `X = R²`. The map
`φ(θ) = (1+θ)/2` satisfies `φ(θ) > θ` for every `θ < 1` and has fixed point
1. So even granting the program's open matched-target `matched(R) ≪ R^{1+ε}`,
sign-blind renewal recovers strictly less than the hypothesis at every
`θ < 1`. Arithmetic re-derived and confirmed by `verify-null-certificates`.
This sharpens the existing registry entry "renewal-only iteration stalls at
`x^{1/2+ε}`": signed exact composition is exponent-preserving (relocation);
sign-blind instantiation is exponent-worsening. May **not** be resubmitted:
a Gronwall-shaped self-improvement built from the square-cutoff skeleton plus
a pointwise `H(θ)` inserted sign-blindly. Scope correction the verifier
attached: the null's further claim that both pieces of the orientation
partition are "≥ RH / GRH-flavored" is asserted, not proven, and its own
deferred measurement initially landed on the re-open branch. Phase 3 ran that
measurement to `R ≤ 10^8` and it lands on the null's own "horn 1 confirmed"
branch instead: the orientation piece is strongly unsupported as
scale-preserving on the tested upper blocks — see §3.

**involution-b: uniform per-stage envelopes are incompatible with
`π(X) − π(X/2)`.** Exact stage identity, for
`finiteDifferenceOperator (primesUpTo P)` at the 0-vanishing indicator and
`X/3 ≤ P < X/2`: `g_{<P}(X) = M(X) + π(X) − π(X/2)`, because every `n ≤ X`
with largest prime factor `q > P` has cofactor in `{1,2}`.
`verify-null-certificates` verified this with **zero** mismatches over every
integer `P` in the plateau at `X = 10^5, 10^6, 4·10^6`, reproducing the
quoted integers exactly (`4411 = −48 + 9592 − 5133`;
`37172 = 212 + 78498 − 41538`; `134405 = 192 + 283146 − 148933`), re-derived
the argument independently, and confirmed it is insensitive to the `< P`
versus `≤ P` convention. Consequence: any uniform per-stage envelope with
exponent `α < 1` on this filtration is false at essentially all intermediate
stages, since `π(X) − π(X/2) ≍ X/log X`. May **not** be resubmitted: a
uniform per-stage `L²` or `L^∞` envelope on the downward-closed
(`S = primesUpTo P`) fresh-prime filtration. Scope correction, mandatory:
this kill is valid only for that operator and that plateau. The general
principle the null proposed to register — "the fresh-prime induction has no
target-compatible per-stage invariant; any future mechanism on the B3
skeleton must be stage-blind" — is FALSE as stated and is falsified by the
greedy-order construction in §3. No revival condition was stated; the correct
reading is that the principle needs scoping, not reviving.

**Status of the two nulls not on this list.** `induction-a` was rated by
`verify-null-certificates` as the strongest and most honest of the six: its
complement-smooth inversion identity is exact (verified at four values of `y`
with zero mismatches), it holds for arbitrary disjoint `S, T` rather than only
downward-closed `S`, and it is the one artifact the greedy-order counterexample
does not dent. It is not listed above as a clean mechanism kill because its
final step — that the residual sub-block `Σ_p Σ_x M(x)M(⌊x/p⌋)` at RH scale is
RH-equivalent — is asserted rather than demonstrated; its identity ships as
this round's first-ranked lemma regardless (§7). `induction-b`'s measurements
reproduce but its load-bearing generalization is falsified rather than
narrowed; see §2 and §3.

---

## 2. Scope corrections

The panel's costliest failure mode is an over-broad registry entry. Each row
states what the phase-1 proposal claimed, what the verifier established, and
what may be recorded.

| Item | Claimed | Established | Registrable form |
|---|---|---|---|
| **hother-kill** (`involution-a/crt-mate-hother-kill`) | "The physical R−2H field does NOT satisfy sign reversal on physical prefixes under any faithful transport"; every named faithful realization closed | `verify-hother-kill` reproduced every numeral twice (Python from repo definitions, and Lean 4.24.0 `#eval` against built Mathlib): cells 11 and 211 mod 225, hits 45 = 9·5 and 846 = 9·94, cofactors 5 and 94, `localPrimeComb 5 5 = −1` vs `localPrimeComb 5 94 = +1`. It also **proved the proposed lemma in Lean** (`native_decide` succeeds). But: (a) `hother` is a SUFFICIENT hypothesis of `correctedCollisionSiteWeight_signReversal`, not a necessary condition for its conclusion; (b) over 210 ordered odd-prime pairs at the canonical period, `hother` HOLDS for 182/210 = 86.7%, failing only when the other prime is 3 or 5 — the witness is a small-prime accident, not a demonstrated structural fact; (c) `hstate` fails for 210/210 pairs in that same probe, with a stated (unproved) structural reason: the cofactor transport divides out `p²` at both mates, so `v_p` of both cofactors is generically 0 and the 0↔1 flip cannot occur; (d) unaddressed transports: `site = k` (the cell index, which satisfies `hother` with zero failures at every pair tested), `site = hit/p`, `site = hit/q²`, next-cell value, flip prime taken outside `{p,q}`, adaptive per-frontier choices | "For `(p,q) = (3,5)` with `S = {3,5}` and flip prime 3, the `p²`-cofactor transport fails `hother`. No claim is made about other transports or other moduli." The **conclusion-level upgrade is verified true** at the same witness by `verify-hother-kill` (`correctedPrimeWheelSite {3,5} upper 5 = −1` and `... 94 = −1`, so `w(mate) = −1 ≠ +1 = −w(s)`), requires `upper ≥ 5`, and `hupper` forces `upper ≥ 94`, so it is safe — ship the upgraded form. `hstate` may be recorded only as an **empirically universal** obstruction in the 210-pair canonical-period probe |
| **pin-kill** (`contrarian/pin-window-value-blindness-kill` + `wildcard/intercept-floor-no-go`) | "Any mechanism whose cancellation input is the B4 modulus accumulated sign-blindly over macroscopic fiber transport certifies nothing below `x/log x`"; dossier thread F2 closed | `verify-pin-kill` confirmed the filter semantics against the Lean source, brute-forced the literal filter for all `t ≤ y` at `y = 10,20,30,50`, and reproduced both panelists' numerics from scratch (`y=316`: `N_active/t` = 6.100/4.700/3.130/2.287/2.218; certificate/\|signed\| = 698/423/1482/1847; fiberwise-absolute optimum 1.05t/0.96t/0.60t/0.47t). The general floor is `(A+B)·#{S-smooth squarefree d ≤ t}` at the canonical pin for `1 ≤ t ≤ y`; it becomes `0.4·t·y/log(y+1)` **only at saturation** `S = primesUpTo y` | It is a SATURATION statement. State the general active-fiber floor first, the saturation corollary second. Small wheels survive: `S = primes ≤ 20` at `y = 10^6` gives a full-window RHS ≈ `26√x` — perfectly usable; the honest general form pins the wheel at `≲ x^{2ε} log x` for macroscopic transport. B4 used locally (`t ≲ x^ε·polylog`) around independently established anchors is untouched. The **B3-recurrence half of F2 is NOT killed**: prong 4 ("triangle across the two terms = renewal stall; signs = the original problem") is classification-by-registry, and the dichotomy is not exhaustive (second moments over `p`, orthogonality, partial signed structure are neither). Register as "B4-transport branch of F2 closed", never "F2 closed". Named escape the proposals missed: the **truncated-operator route** — `finiteDifferenceOperatorUpTo` and `finiteDifferenceOperator_eq_upTo_add_tail` are on main and evade the floor at the cost of a tail obligation. That is a named gap, not a refutation |
| **sum-rule kill** (`spectral-a/finite-prime-sum-rule-witness`) | "Sum rules force degree-one cancellation is dead as a mechanism"; the 2-adic dilation family is the only sign-sensitive exact CRT structure at the mod-4 level; surviving mechanisms must run through B3 saturation or B5 renewal | `verify-sumrule-kill` reproduced every number, several to more digits than claimed (`c_P` exactly to `K = 10^9`: 0.8105695, 0.2701898, 0.1688690 for `P = {2}`, `{2,3,5}`, `{2,3,5,7,11}`), and could not kill the core argument. But: (a) the classification is false at refined moduli — exact `p`-adic dilations `μ(4pk+p) = −μ(4k+1)` for `p ∤ 4k+1` verified with zero violations for `p = 3, 5, 7`, and the shipped `P = {2}` witness violates the 3-adic one at 202,614 sites and the 5-adic at 135,090; (b) every witness fails the global identity `Σ_{d\|n} μ(d) = [n=1]` on a positive-density set (measured 999/2000, 533/2000, 457/2000 for `P = {2}`, `{2,3,5}`, `{2,3,5,7}`) | Killed: any inequality derived **solely** from squarefree support, multiplicativity, and prescribed sign `−1` at the primes of a **fixed finite** set `P` — this covers single-scale LP over the 27 counts, finite-depth CRT stencils, the B6 three-pivot bound (confirmed to be a universal predicate bound with zero sign content), and the dilation and pair-transport identities. NOT killed: any system that also uses `μ*1 = δ` or sign data at infinitely many primes. Correction to the verifier's own parenthetical: since `(g_P*1)(n) = ∏_{q\|n}(1+g_P(q))`, which vanishes as soon as `n` has a prime factor in `P`, the violation set is `{n > 1` with **no** prime factor in `P}`, of density `∏_{p∈P}(1−1/p) > 0` — not density 1. Its measured counts (999/2000 = 1/2 for `P={2}`; 533/2000 ≈ 0.2667 = (1/2)(2/3)(4/5); 457/2000 ≈ 0.2286) match the corrected description exactly. The conclusion is unaffected: the escape set has positive density for every finite `P`. 3-adic/5-adic dilation families exist at refined moduli, so the mechanism survives only by enlarging `P` (with `c_P > 0` always), and the deliverable must be `P`-generalized or state its scope in the theorem |
| **`induction-b`'s order-independence claim** | "Every path from empty set to `primesUpTo X` passes through a state with, for some scale `x`, at least `~x^{0.6}` missing primes in `(x/2, x]`, hence bias `~x^{0.6}`"; "no prime-set filtration of `D_S f` qualifies for any fixed `f` with `f(0) = 0` and the M-recovering normalization" | `verify-null-certificates` FALSIFIED both by direct construction (see §3). It also identified the invalid inference underneath: "missing primes in `(x/2,x]` ⇒ bias `~#missing`" is false in general — at `S = ∅` every prime is missing yet `g_S(x) = 1` identically, because the higher rough layers cancel the single-prime layer. The inference is valid only once `S` contains all small primes, i.e. only on the smooth-first path. The measurements themselves (mountain shape, `sup` ratios) reproduce and are not in dispute | The measured mountain is registrable as a property of the smooth-first ORDERING, over the measured window. The order-independence claim must NOT enter the registry in any form; the correct entry is the operator-scoped one in §6 |
| **"class kills" that are mechanism kills** | Six nulls declared their classes closed | `verify-null-certificates`: the four endorsed kills are kills of the variants actually tried. `involution-b`'s "the class is closed" is about the finite-difference recast where `hstate/hother/hsmooth` are vacuous — the physical B7 involution class the dossier names is untouched. `verify-resigning-kill`: `spectral-b`'s kill covers lag-≤2 pair/triple statistics only; its second leg ("the closure of the exact constraint set is the renewal hierarchy") is asserted with no definition of closure and no exhaustiveness argument. `induction-a`'s honest residue (non-`ℓ²`-window functionals of the whole saturated object) is explicitly outside its own kill | Register each as a mechanism kill with its mechanism and premises named. No class in this round was closed; every §6 entry is written to name what died and what did not. In particular, nothing in the six nulls touches dossier F's first bullet (the physical R−2H sign-reversal question), and it must not be recorded as killed |

---

## 3. Re-opened threads

These are the round's positive residue. None is a bound; each is a
measurement over a stated window or an existence statement. Both threads were
carried to scale in phase 3 (`results/043/phase3_numerics_findings.md`, itself twice
GPT-5.6-reviewed); their outcomes are recorded below at the scope that
document states. One re-open was confirmed at scale, one was closed.

**Greedy-ordering existence result — CONFIRMED at `N = 10^6`.**
`verify-null-certificates` ran a
one-step-lookahead greedy insertion order over primes (choosing at each stage
the remaining prime that minimises `sup_x |g_S(x)|/√x`), with `f = 1_{≥1}`,
from `S = ∅` to `S = primesUpTo N`. At `N = 2000 / 5000 / 10000 / 20000` the
path attains `sup_x |g_S(x)|/√x = 1.0000` at **every** stage — the absolute
floor, since `g_S(1) = 1` always — with `max|g_S| = 141` against `√N = 141.4`
at `N = 2·10^4`, and path-maximum window energy `E/N² = 0.324 / 0.330 /
0.317 / 0.2996`, flat across those four scales. The final state equals `M`
bit-exactly in all four runs, so the path really is a full prime-set
filtration to saturation. On the increasing-order path the same code gives
`max E/N² = 2.692 / 5.500 / 9.488` at the smaller scales, rising to 59.998 at
`N = 10^5`, growing like `N^{0.8}`. Consequence: over the tested range the
`X^{1−o(1)}` mountain is a property of the smooth-first ORDERING, not of the
B3 skeleton, and `induction-b`'s explicit claim that every path passes
through a state with bias `~x^{0.6}` is falsified by construction. Two
caveats travel with this and must not be dropped: (i) the order is chosen
using knowledge of `g`, hence of `μ`, so this is an existence result, not a
proof strategy; (ii) by `induction-a`'s complement-smooth inversion lemma
(verified exact — see §7), every intermediate field of a prime-set filtration
whose union is saturated equals `Σ_{n T-smooth} M(⌊x/n⌋)`, so "a good path
exists" is itself a statement about `M`'s multiscale autocorrelations.

Phase 3 carried this to `N = 10^6` and the audit's falsification survives at
scale. With the same greedy objective and a random tie-break, the path
attained the exact floor `sup_x |g_S(x)|/√x = 1.000000` at **every one of
78,498 stages**, with `max|g_S| = 999` against `√N = 1000` and zero
above-floor stages; the audit's own smallest-prime tie-break rule, carried to
`N = 5·10^5`, gives `1.004024` with 107 above-floor stages out of 41,538. (An
exactness note that makes these certificates rather than estimates: `g_S(1) = 1`
for every `S`, so 1 is a hard floor, and `score(p) ≤ 1` is the pure-integer
predicate `(g(x) − g(⌊x/p⌋))² ≤ x`. A round-1 correctness fix to the
candidate test was forced and applied, and full `O(N)` audits at every
above-floor stage and every 512 stages returned zero mismatches in every run.)
Four scope qualifications from the phase-3 document, none of which may be
dropped when this is cited. (a) **It is largely degrees of freedom, not a
narrow escape.** Along sampled successful trajectories admissible next moves
are locally common — estimated median 65.5% of remaining primes at `N = 10^5`,
minimum 27.5% over sampled stages — and a random budget of ~30 candidates per
stage usually suffices (the `N = 10^6` run needed 32.4 candidates/stage). That
establishes local commonness along sampled successful trajectories, not
abundance of complete successful paths, and it does not settle the
degrees-of-freedom-versus-arithmetic-conspiracy attribution: the
arithmetic-destroying surrogate control was not run. (b) **Both rules read the
state, hence `μ`, at every step**, and the admissibility test is itself
expensive — this is an existence result about orderings, not a proof strategy.
(c) **The energy consequence is deterministic, not fitted**: on an exact-floor
path `g_S(x)² ≤ x` for every `x` at every stage, so `E_S ≤ N(N+1)/2 ~ 0.5N²`
with no fit; the `N = 10^6` run attained the floor at every stage, so
`E ≤ 0.5N²` is a theorem about that run, and the measured path maximum
`0.4645 N²` sits just under it. What remains unproved is the *existence* of
exact-floor paths uniformly in `N`. (d) **Cross-horizon transfer fails**: the
`N = 10^5`-optimal ordering replayed with the sup evaluated over `x ≤ 10^6`
degrades to `sup = 22.61`, first exceeding 2 at stage 293/9592 and 5 at stage
2152. A confound is stated: the replay's terminal state is
`S = primesUpTo(10^5)`, which is order-independent, so its bad value at the
larger horizon is forced for any ordering of those primes — it is exactly the
downward-closed mountain — but the profile shows the failure is not confined
to that forced endpoint. The defensible conclusion is therefore only that
goodness at horizon `N` does not by itself guarantee goodness at a larger
evaluation horizon and that this tested ordering fails that transfer; a
horizon-independent ordering could interleave larger primes early and need not
contain this replay as an initial segment.

Registry framing, adopted verbatim from the phase-3 document (which adopted
its round-2 reviewer's wording): "No finite-horizon huge-intermediate
obstruction was observed through `N = 10^6`: state-aware greedy orderings kept
the path maximum at most 1.004, and the reported randomized runs attained the
exact floor. The unresolved issue is coherence across horizons — one
`N = 10^5` ordering fails larger-window replay — and no horizon-independent
induction rule or invariant has been found." The open question is therefore a
**constructive, `μ`-free ordering rule**, with cross-horizon incoherence as
the named obstruction. Two things must NOT be filed: "the induction coordinate
is obstructed by relocation only" (relocation is the remaining *observed*
problem, not a proved unique obstruction — the earlier draft of this report
filed it and the phase-3 document explicitly declines to), and any claim that
good paths die at some scale (they do not, at any tested scale through
`N = 10^6`). `moment-a`'s `C_p ≥ 0` kill remains binding independently — the
greedy path itself has `C_p < 0` at 30–44% of its steps, rising with scale,
and 62,127/78,498 at `N = 10^6`.

**Orientation-split `G(R)` measurement — RE-OPEN CLOSED at `R ≤ 10^8`.**
`renewal-a` declared its own decisive measurement and did not run it, stating
the falsifier in advance: `|G(R)| ~ R^{1.2+}` confirms horn 1,
`|G(R)| ~ R^{1+o(1)}` means "a future round could target it directly".
`verify-null-certificates` ran it to `R = 3162` (`X ≤ 10^7`) and found
`G(R) = Σ_{p≤R} M(p−1)` sign-definite negative with `|G|/R ∈ [0.185, 0.387]`
over `31 ≤ R ≤ 3162` and no trend — which put the null on the re-open branch
by its author's own criterion. **Phase 3 shows that reading was
pre-asymptotic.** Measuring `G` at every integer `R ≤ 10^8` with a
dyadic-block RMS estimator (`A_2(T) = ((1/T)Σ_{T<R≤2T} G(R)²)^{1/2}`,
integer-uniform weight, no running maximum, no zero-crossing excision — all
statements are about the estimator, since `G` changes sign and passes near
zero): `A_2(T)/T` is bounded in 0.25–0.52 for `T ≤ 2^17` (`R ≤ 1.3·10^5`) —
exactly the regime the audit measured — and then rises monotonically through
nine consecutive blocks to 5.782 at `k = 25`. The effective exponent is
**1.4164** on `R ∈ [6.6·10^4, 6.7·10^7]` (`n = 10` complete blocks,
`R² = 0.9988`), and it rises monotonically with the lower cutoff (1.1552 from
`R ≥ 8`; 1.2926 from `10^3`; 1.3952 from `3.3·10^4`; 1.4196 from `2.6·10^5`;
1.4460 from `10^6`), with the block-max envelope running 1.47–1.54.
Sign-definiteness fails at `R = 20939` — the first `R ≥ 10` with `G(R) ≥ 0`,
with 42 sign changes on the geometric grid to `10^8` — so the audit's
"sign-definite negative, `|G|/R` flat at 0.30" is a true statement about
`R ≤ 3162` and a false statement about `R ≤ 10^8`. Meanwhile `|M(R²−1)|`,
measured over every integer `R ≤ 5.29·10^5` (two independent segmented sieves,
Mertens checkpoints to `M(10^11) = −87856` all correct), is pinned at
exponent **0.95–1.01 in `R`** (`X^{0.48}`–`X^{0.51}`) with `A_2/T` bounded in
0.22–0.29 across all 18 blocks — the target scale, and a good end-to-end check
on three independent code paths — while `A_2(matched')` runs at slope
1.00–1.17 across cutoffs. On the common range each piece is individually
larger than the whole and the gap grows: the scale-destruction factor
`(A_2(G) + A_2(matched'))/A_2(M(R²−1))` rises 3.07, 3.64, 3.69, 4.53, **5.78**
over `k = 14..18`. (The within-block correlation of `−G` with `matched'`
reaching `−0.942` at `k = 18` is **not** independent confirmation of anything:
once `|G|` dominates `|M(R²−1)|`, `matched' = M + G` forces the correlation
toward `−1` by the identity alone. And the correlation of `G` with
`−M(R²−1)`, the quantity the null named, has no stable value across
normalisations and windows.) The verdict wording, taken exactly as the
phase-3 document scoped it after its own round-2 review: **target-scale
`R^{1+o(1)}` behaviour is strongly unsupported on the tested upper blocks** —
the effective excess is ~0.42, far beyond the program's polylog-resolution
caveat, `A_2(T)/T` rises persistently through nine consecutive blocks, and no
crossover toward exponent 1 is visible. This is strong finite-range evidence
against treating the split as scale-preserving; it does **not** asymptotically
exclude the class `R^{1+o(1)}`. Net: `renewal-a`'s null lands on its own
"horn 1 confirmed" branch at the tested scales, and the thread is closed
rather than re-opened. What was right in the null stays right — reaching
`R^{1+ε}` for `G` requires essentially square-root cancellation over the
`~R/log R` prime samples — and what was unsupported stays unsupported: the
pricing of that obligation as strictly above RH was never demonstrated, and no
circularity was exhibited.

This is the first confirmed firing of the pre-asymptotic calibration wall
(§5, R1) against the program's own conclusions: a re-open declared on a flat
ratio over `R ≤ 3162` was reversed by measurement three decades further out,
in a regime the original window could not see.

**The B7 physical sign-reversal question remains genuinely open.** No null
touched it; `involution-b` explicitly routed around it into the
finite-difference recast. The round's durable output here is a tripartite
classification (`mfd-math` item 2, consistent with `verify-hother-kill`):
literal collision site ⇒ corrected weight identically zero (already on main,
`PrimeSquareCollisionPhysicalFibreNoGo`); CRT cofactor site ⇒ `hother` fails
at `(3,5)`, and `hstate` fails at all 210 pairs probed; multiplicative site ⇒
the package holds but the frontier sum has no arithmetic anchor to any
Mertens prefix. The missing fourth option — a site realization simultaneously
CRT-determined and multiplicatively coherent — has not been proposed by
anyone. This classification is not a closure: "faithful" has no repo
definition, and `verify-hother-kill` names five concrete unaddressed
transports. Declared future work.

**`hstate`-universality formalization candidate.** `verify-hother-kill`
measured `hstate` failing for 210/210 ordered odd-prime pairs at the
canonical period, with a stated structural reason (both mates are `p²`-hits
by construction, so `v_p` of both cofactors is generically 0 and the required
`0↔1` exponent flip never occurs). That is the empirically universal
obstruction and the one a follow-up should formalize, in place of the
accidental `hother` failure the proposal picked. Declared as a candidate: the
structural reason is stated but not proved, and 210 pairs at one period is
exposure, not a theorem.

---

## 4. Measurement reattribution — and one dossier-constraint falsification

### 4.0 The trilemma's horn-1 rule (D4) is falsified as a predictive principle

This is the round's most consequential correction to the frozen constraint
set, and it should be read before anything else in this section. Dossier D4
states a rule "with predictive content": *a split preserves RH scale in every
piece iff it partitions the summation index `{n}` itself* — with index-set
partitions preserving RH scale at the price of a per-piece GRH obligation.
The phase-3 orientation measurement supplies a counterexample to the
`index partition ⟹ scale preserved` direction.

The canonical orientation split **is** a plain unit-weight index subset, by an
elementary bijection rather than by numerical inference: writing `m = np` with
`p = P⁺(m)` and `n < p`, the class is
`C_R = {m : P⁺(m) ≤ R, m/P⁺(m) < P⁺(m)}`, the constraint `m ≤ R²−1` is
automatic since `m = np < p² ≤ R²`, and `n < p` gives `p ∤ n`, so
`μ(m) = μ(n)μ(p) = −μ(n)` and `Σ_{m∈C_R} μ(m) = −Σ_{p≤R} M(p−1) = −G(R)`.
Phase 3 also computed the class sum directly from a largest-prime-factor sieve
and matched `−G(R)` at 25 values of `R ≤ 2000` with zero mismatches, including
the audit's `R = 100 → 31`, `316 → 96`, `1000 → 185`. Yet this piece does not
stay at the whole's scale: `G` sits at effective exponent ≥ 1.4 in `R` on the
tested upper blocks against a target of 1, while `M(R²−1)` stays pinned at
0.95–1.01 (§3). So a genuine unit-weight index partition destroys scale.

Two qualifications the phase-3 document attaches, and they travel with the
finding: (i) the class is **horizon-dependent** — it is a family `C_R`, not a
fixed colouring `C ⊂ ℕ` (an `m = np` can lie in the complement while
`√m ≲ R < p` and enter the class once `R ≥ p`), so if D4 was meant to be about
fixed cutoff-independent partitions this example sits outside that narrower
reading; (ii) the class and the whole were not measured on the same long range
(`G` to `R ~ 10^8`, `M(R²−1)` to `R ~ 5.3·10^5`), so the separation is
measured on the common range (`A_2(G)/A_2(M)` = 1.44, 1.59, 1.83, 2.09, 2.79
over `k = 14..18`) and only extrapolated beyond it.

Even with both qualifications, D4's unrestricted implication is false as a
mathematical principle, and that does not need the numerics at all: an
arbitrary index subset can correlate with the coefficients — selecting the
indices where `μ(n) = 1` gives a sum of order `X`. **Index partitioning
preserves unit coefficient size, not cancellation.** The trilemma's three
horns remain valid as a catalogue of observed failure modes; what must stop is
using horn 1 as a scale-preservation *guarantee*. Replacement wording for the
dossier, adopted verbatim from the phase-3 document:

> "Being an index partition does not by itself preserve RH scale. Every piece
> requires a separate, uniform cancellation estimate. Fixed partitions whose
> indicators decompose into analytically controlled twists may inherit
> RH-scale bounds under the corresponding GRH hypotheses; moving partitions
> require uniform control of the resulting family of weights."

A candidate replacement criterion — "preserves scale iff the regrouped
indicator carries bounded multiplicity" — was proposed by the numerics agent
and **withdrawn** under review: it is neither sufficient (bounded 0/1 weights
can be chosen to correlate with `μ`) nor necessary
(`Σ_{n≤X} μ(n)⌊X/n⌋ = 1` has unbounded weights and perfect cancellation). The
usable diagnostic is two-part and has no purely combinatorial answer to its
second half: (i) does regrouping amplify coefficient `L²` mass beyond the
target scale? (ii) what uniform arithmetic estimate controls the correlation
between those weights and `μ`?

**The structural explanation, and the null scale it is measured against.**
Regrouping the double sum into the `n`-variable (many-to-one, so multiplicity
appears) gives the exact identity
`G(R) = Σ_{n<R} μ(n)·w_R(n)` with `w_R(n) = π(R) − π(n)`, equivalently
`π(R)·M(R−1) − Σ_{n<R} μ(n)π(n)` — verified for **every** `R ≤ 10^8`, zero
failures out of `10^8`. So after regrouping, each `μ(n)` carries a weight of
typical size `π(R) ~ R/log R`: the growth is a property of the weight
structure the partition induces, not evidence of missing cancellation. The
exact independent-sign standard deviation of that weighted sum,
`σ(R) = (Σ_{n<R} μ(n)²w_R(n)²)^{1/2}`, computed exactly, satisfies
`σ(10^8) = 0.47·R^{3/2}/log R`, and `G(R)/σ(R)` is flat at a few percent with
no trend over four decades (`−0.3091, −0.0840, −0.0362, −0.0323, −0.0296,
−0.0131, +0.0264` at `R = 10^2..10^8`). The correct statement, exactly as the
phase-3 document scoped it after deleting a stronger one: reaching
`R^{1+o(1)}` would require cancellation **substantially stronger than the
independent-sign benchmark**, and these numerics neither supply nor rule out
such cancellation — independent-sign variance is a structurally motivated null
scale, **not a lower bound**, and deterministic arithmetic correlations can in
principle beat it. Two cancellation controls sharpen the reading: at
`R = 10^8`, `|G|/Σ_{p≤R}|M(p−1)| = 0.1258`, bounded and trendless from
`R = 10^4` on, so `G` beats its own triangle majorant by a bounded factor
(~7–16) and by no power over the measured range; and the all-integers analogue
gives `|Σ_{n≤R} M(n)|/Σ_{n≤R}|M(n)| = 0.1304`, so restricting to primes
contributes nothing arithmetically special at these scales.

### 4.1 Record-040 statistics

**Record-040's TV 0.1350 and CMI 0.248 are zero-pattern (`μ²`) statistics.**
`verify-resigning-kill` computed the TV of the 8-state zero-pattern chain
(`μ²` indicators only) and found `TV27 = TV8` to ten decimal places at every
tested `K ≥ 2·10^5`: the measured gap is `9.9·10^{-2}` at `K = 2000`,
`5.9·10^{-3}` at `K = 20000`, `8.3·10^{-17}` at `K = 2·10^5`, and exactly 0
at `K = 5·10^5, 10^6, 3·10^6`. (Equality is not proved for all `K` in that
range; those are the tested values.) The mechanism offered is that
`TV27 ≥ TV8` always, by the triangle inequality over sign-flip orbits, with
equality once each zero-pattern block's deviation dominates within-block
sampling noise. On the CMI side, `CMI8 = 0.2474` — i.e. the dossier's
reported plateau of 0.248 is exactly the zero-pattern CMI — and the 27-state
excess `CMI27 − CMI8` measures 0.017413 / 0.008756 / 0.002987 at
`K = 5·10^5 / 10^6 / 3·10^6`, a decay consistent with pure plug-in bias from
the 27-vs-8 state resolution. Two controls support the attribution: an
iid-random-sign field at every nonzero site, with no multiplicativity at
2, 3, 5 whatsoever, gives `TV27 = 0.1350070318` (identical to 10 dp); and a
constant field `σ ≡ +1` gives `TV27 = TV8 = 0.1350070318` and
`CMI27 = CMI8 = 0.247704` exactly while its partial sum grows linearly at
`2.43176·K`. The same applies to the "memory floor":
`TV[(μ(4m+1), μ(4m+3))] = 0.02349156` equals the 2×2 zero-pattern TV to 8 dp
and is reproduced by the resigned model — a squarefree-exclusion effect (`p²`
cannot divide both `4m+1` and `4m+3`) with no sign content. Consequence for
how D2's mixing ban is read: what these statistics measure is the squarefree
pattern, not sign memory. They cannot be mined for sign cancellation, and
TV 0.1350 / CMI 0.248 must not be cited as evidence about signs in either
direction. Recommended: annotate dossier item C / record 040 with this.

**The δ-biased core-resigning witness is the valid kill certificate for
mechanisms consuming the pre-registered summary statistics.**
`verify-resigning-kill` constructed it: `ε(m) = +1` with
probability `1/2 + δ`, iid per core `m` coprime to 30, extended by exact
2-3-5 multiplicativity onto the real `μ` zero pattern — i.e. inside the
pre-registered constraint set. At `K = 5·10^5`: `δ = 0.02` gives
`TV27 = 0.1350070318` (identical to the real chain to 10 dp), `CMI27 = 0.2658`
(real 0.2651), partial sum `0.00958·K`; `δ = 0.05` gives
`TV27 = 0.1350070318`, `CMI27 = 0.2677` — inside the proposal's own
pre-registered band `[0.225, 0.270]` — and partial sum `0.02596·K`. Both grow
linearly, exponent 1, while matching the ledger. That is the certificate the
kill needed, at the scope the measurements support: the constraint set plus
the pre-registered summary statistics (pair TV, triple CMI, and their bands)
admit completions at exponent 1, so no mechanism consuming **those**
statistics can reach exponent 1/2. Note the limit of the instrument: the
verifier reported `TV27`, `CMI27` and the partial sum for the δ-biased field,
not an `L1` comparison of the full 729-cell pair law (that comparison was run
only for the unbiased model, at `L1 = 0.036–0.040`). A mechanism consuming
the complete lag-1/lag-2 joint laws rather than these summaries is therefore
outside this certificate.

**The unbiased null certifies nothing.** `verify-resigning-kill` replicated
the pilot from scratch (real TV 0.135007 / CMI 0.265117; model TV 0.135007
with seed spread exactly 0.000000, CMI 0.2654–0.2658; ~607k of 1.216M
nonzero sites differing) — so the empirical claim is not falsified. But the
instrument has the wrong logical shape. A kill by indistinguishability needs
an impostor that VIOLATES the target; the unbiased impostor SATISFIES it. Its
Mertens analogue measures `+0.334·√(4K)` and `+0.328·√(4K)` (real `−0.175`),
squarely inside record-040's band `[0.32, 0.41]`, and by the law of the
iterated logarithm the ensemble a.s. obeys `|M̃| ≪ x^{1/2+ε}`. It is a
confirming instance. Two further defects: the pre-registered TV threshold
cannot fail (`TV27` equals `TV8` at these scales, and the model copies `TV8`
by construction), and the `L1` threshold is miscalibrated — the verifier
measured the same-law baseline at `L1 = 0.0388` at `K = 5·10^5`, not the
quoted "~0.06", so the pilot's `L1 = 0.038` sits AT baseline rather than
below it. Do not run the pre-registered `K = 2.5·10^7` test; it would consume
hours and settle nothing. Separately, `spectral-a`'s witness `g_{2,3,5}` has
`TV27 = 0.5929` against the real 0.1350, so it is ledger-DISTINGUISHABLE and
does not double as a covariance-invariance counterexample. The two witnesses
are complementary and must not be conflated: `g_P` kills fixed-finite-`P`
sum-rule mechanisms, the δ-biased field kills bounded-lag covariance
mechanisms.

**Prior art two proposals missed — flag for future dossiers' section B.**
`RHLean/Analysis/DyadicTransportCanonicalForm.lean:235` already carries,
kernel-verified on main,
`mertensSummatory_eq_dyadicCofactorBoundaryMass (B : Nat) : mertensSummatory B = dyadicCofactorBoundaryMass B`
— that is, `M(B) = Σ` over odd `c ∈ (B/2, B]` of `μ(c)`, for ALL `B` — built
on `sum_evenCofactorPrefix_eq_neg_odd_half` and `canonicalMoebiusWeight_two_mul`
in `RHLean/Analysis/DyadicTransportCompression.lean` (with
`oddCofactorPrefix`, `evenCofactorPrefix`, `sum_Icc_eq_odd_add_even`). This is
the classical "M(x) equals the odd-restricted Mertens sum over the top
octave" identity, already formalized. The flagship corollary of both
`spectral-a/octave-increment-skeleton` and `spectral-b`
("`M(8L) = U(2L) − U(L)`, the target as an octave increment of the χ₄-free
object") is exactly its `B = 8L` instance rewritten in three-slot
coordinates, and is strictly weaker. Neither proposal cites either file. Its
absence from the dossier caused two independent generators to sell a special
case of an existing main theorem as a structural discovery; it belongs in
section B of the next dossier.

---

## 5. Standing epistemic rules (proposed as registry-grade)

**R1 — the pre-asymptotic calibration wall.** Differences of order
`x^{0.015}` over four decades (`10^4..10^8`, a factor ≈ 1.14) are
indistinguishable from `x^{1/2}·polylog` by exponent regression. The rule is
therefore scoped to falsification that rests on fitted exponents or on slowly
varying amplitude ratios: such a test cannot certify or kill an engine whose
margin is that thin, and a proposal whose only prediction is of that form is
unfalsifiable at `x ≤ 10^8`. (Sign, identity, constant, or distributional
predictions are not covered and remain fair game.) `renewal-a` and
`verify-null-certificates`'s audit of `moment-b` reached this wall
independently, and phase 3 supplied its **first confirmed firing against the
program's own conclusion**: the orientation-split re-open, declared on a flat
`|G|/R ≈ 0.30` over `R ≤ 3162`, was reversed by measurement to `R ≤ 10^8`,
where the estimator's effective exponent settles near 1.42 and
sign-definiteness fails at `R = 20939` (§3). A flat ratio over three decades
is not evidence of an exponent. Direct consequence: `θ*`-type pre-screens must carry the
caveat, **and the corrected `θ*` is ≈ 0.673, not 5/6**. The map
`2θ_new = 2θ_old + β(2 − s − 2θ_old)` has fixed point `θ* = (2−s)/2`, but `s`
is defined relative to the family size (`s = 1` is square-root cancellation
across the family). Record 032's own artifact
(`results/032/artifacts/sec7_note.md`, lines 52–56) states that full
square-root cancellation over the `D` fibres is `D^{0.5} = x^{0.25}` while
the measured saving is `D^{0.327}`; hence `s = 0.327/0.5 = 0.654` and
`θ* = 0.673`. `moment-b` conflated the amplitude saving with the energy
saving — a factor-2 unit slip that looks self-consistent only because
`D = x^{1/2}` — and shipping "5/6" would encode it in the registry. Across
record-032 runs A/B/D (`D^{0.324}`, `D^{0.404}`, `D^{0.327}`),
`s ∈ [0.65, 0.81]` and `θ* ∈ [0.60, 0.68]`. Under the RH-true limiting values
(signed 0.5, triangle 0.75 = the D3(a) ceiling) the saving would be exactly
`x^{0.25} = D^{0.5}`, so `s = 1` and `θ* = 1/2` — the marginal renewal stall,
not 5/6. The direction of the conclusion at measured values is unchanged
(`θ* > 1/2`), but the pre-screen is calibrated on pre-asymptotic exponents
and must say so.

**R2 — falsifiers must be windowed, not pointwise, for signed near-√ walks.**
Two independent instances this round. `spectral-a`'s pre-registered
prediction (1) asserts `|prefix(K)| ≥ K^{0.30}` throughout
`K ∈ [10^6, 2.5·10^7]`; `verify-sumrule-kill` measured `W_a(10^6) = −21`
against `(10^6)^{0.30} = 63.1`, so it is already false at the first scale it
names — a signed near-√ walk crosses zero, and a pointwise lower bound of
that shape is structurally unattainable. `renewal-b`'s `Ξ_bal` thresholds are
worse: `osp-math` found the observable changes sign between `T = 500` and
`T = 2000` (`+354` at `T = 1000` between magnitudes `10^4` and `10^7`),
giving adjacent-dyad slopes from `−0.75` to `+9.30` and full-range fits
anywhere in `[2.03, 2.27]` depending on the window. Rule: a dyadic-slope kill
threshold on a sign-changing observable is not a test. Use `|·|` of a
definitely-signed object, or a max/median over dyadic windows, and report the
zero crossings. Companion threshold-width rule (`osp-constraints` item 4):
signed double sums over quadratic nets at `T ≤ 10^4` have estimator scatter
exceeding one full unit of exponent, so no falsification test in that regime
with a threshold narrower than ≈ 1.5 units should be accepted as decisive.

**R3 — kill-by-indistinguishability requires an impostor that VIOLATES the
target.** An impostor that matches the ledger and also satisfies the target
bound is a confirming instance, not a certificate. Worked example, both
halves measured this round: unbiased core-resigning matches TV/CMI to four
decimals and satisfies `M ≪ x^{1/2+ε}` a.s. (Mertens analogue at
`+0.33·√(4K)`, inside the real band), certifying nothing; δ-biased
core-resigning matches `TV27` to ten decimals and `CMI` inside the
pre-registered band while growing at exponent 1, and does certify the kill.

Three further rules the verifiers asked to be recorded, adopted here at the
same grade:

**R4 — strength by the best known transfer (strengthening of D3(b)).**
Compute the strength of your obligation using the best known transfer, not
the transfer your mechanism uses. If any known transfer returns the target
exponent family, the coordinate is a relocation regardless of what your
mechanism extracts. `emi-constraints` supplies the clean worked example: the
excursion converter returns 2/3 from a hypothesis the classical Mellin route
turns into `1/2 + δ/2`.

**R5 — the mean-square test.** `Σ_{A≤T} M(A)^2 ≪ T^{2+ε}` for every `ε > 0`
(equivalently `∫_1^X M(t)^2 dt ≪ X^{2+ε}`) is RH-EQUIVALENT. Any proposal
offering **this** statement — the unweighted full-prefix second moment of `M`
at the RH exponent — as an "easier intermediate", "scaffolding" or "warm-up"
is offering RH. Two proposals walked into it in one round, one while
explicitly believing the averaged statement was weaker than the target. Scope:
the rule covers the unweighted full-prefix second moment. Sparse, windowed,
weighted or twisted averages are not covered and are not claimed dead. What
the record offers about averaging is narrower and conditional, and is
recorded here as an argument rather than as an established fact: `osp-math`
argues from Ng's `Ω_±(√x (log log log x)^{5/4})` together with a
limiting-distribution result for `M(x)/√x` that the averaged and pointwise
saving exponents for `M` coincide at 1/2, so A-averaging of `M` yields no
exponent gain. That argument carries hypotheses beyond RH and LI — the
limiting-distribution results in this family require an additional
negative-moment (Gonek–Hejhal-type) assumption — and it should not be cited
as unconditional. Separately measured, not proved:
`Σ_{A≤T} M(A)^2/T^2` is flat at 0.0146–0.0164 over `T = 10^3..10^6`.

**R6 — falsifiers must discriminate the mechanism from "RH is true", and
coordinates must state their counting ceiling first.** A prediction whose
falsification would falsify the target is not a mechanism-killing prediction
(`emi-*`: the `E_m/K^{m+1}` flatness test is a test of RH). And a proposer
introducing a new coordinate must state the triangle/counting ceiling on it
BEFORE reporting a signed saving in it — one line of counting would have
killed MFD at generation time. Related: report savings as fitted exponents
with dyad-to-dyad scatter, never as factors; a bounded factor cannot move a
fixed point.

---

## 6. Proposed dead-end registry additions

One-line entries in the style of IDEAS.md section J / dossier section E,
ready to merge. Each names the mechanism and its premises, and states what is
**not** killed, so that no entry forecloses more than the round established.

- **Overlap-square / symmetric hyperbola pin** (μ*μ at `X = A²`; renewal-b): the identity `M(A)² = 2·S_A(A²) − M2(A²)` is exact and relocation-neutral (`J(A) ≡ M(A)²`), the `M2` term is RH-equivalent at exponent `1/2+ε` (`1/ζ²`), and the proposal's only leverage step targets the unweighted full-prefix mean square, which is RH-equivalent; the `μ^{*k}` tower as proposed does not close (one new unknown `M_{k+1}` at scale `A²` per rung; the level-2 pin exposes the RH-equivalent nonnegative block `M2(A)²`). Cause of death: identity-level relocation with no inequality step. NOT killed: an independent inequality bounding `S_A(A²)` without knowing `M2` (043).
- **Unweighted full-prefix mean square of `M` as an intermediate**: `Σ_{A≤T} M(A)² ≪ T^{2+ε}` for every `ε` (equivalently `∫_1^X M² ≪ X^{2+ε}`) is RH-EQUIVALENT by dyadic Cauchy–Schwarz on `1/(sζ(s)) = ∫ M(t)t^{-s-1}dt`; offering it as scaffolding is offering RH. NOT covered: sparse, windowed, weighted or twisted averages (043).
- **Moment-ladder interpolation on pure even power sums of `M`** (`E_m(K) = Σ_{k≤K} M(4k)^{2m}`): with `Θ := inf{θ : M(x) ≪_ε x^{θ+ε}}`, the family `E_m ≪_{m,ε} K^{1+2mθ+ε}` is equivalent to `Θ ≤ θ` (⇒ Hölder `E_1 ≤ E_m^{1/m}K^{1−1/m}` plus the classical Mellin/Plancherel argument; ⇐ trivial), so the `θ = 1/2` rung the ladder needs is RH at every `m`; and the excursion converter is dominated by the classical transfer at every rung, gap `(1−θ)/(2m+1) > 0` for `θ < 1` (equality at `θ = 1`; `θ > 1` disposed of by `M(x) ≪ x`), so it never improves on the classical route for any pure moment of `M`. NOT killed: moments of objects other than `M`, or restricted/weighted moments where Hölder cannot reach `E_1` (043).
- **Single-level per-(p,q) collision-frontier defect aggregation**: at most 3 bounded defect labels per ordered odd prime pair and `#{(p,q) : p²q² ≤ x} = #{pq ≤ √x} ≍ √x·loglog√x/log√x = o(√x)` by Mertens (measured label-count proxy `3·#pairs/√x` = 1.19 at `x = 10^7` → 1.01 at `10^12` and → 0; `#pairs/√x ∈ [0.337, 0.397]` across the measured window, fitted exponent 0.4939 in `K`), so such an aggregation is unconditionally `o(√x)` for any uniform per-site weight bound and cannot carry the `Ω_±(√x)` mass of `M`. NOT killed outright but explicitly unfunded: multi-level versions, which inherit `≈ π(√x)` levels and must exhibit the cross-level cancellation — the original problem (043).
- **Multiplicative-fiber pairing (`n ↦ pn`) as submitted**: its true defect is the full annulus `{X/p < d ≤ X}`, whose only internal structure is the renewal telescope; the submitted route substitutes a per-pair collision-frontier object for the annulus with no theorem relating the two, and no lemma anywhere in RHLean anchors a collision frontier sum to a Mertens / three-slot / Möbius prefix for any site map. NOT killed: a proven faithful-anchor theorem — the named revival condition (043).
- **CRT `p²`-cofactor transport at `(p,q) = (3,5)`**: with `S = {3,5}`, flip prime 3, mate pair `(0,1)/(1,1)`, cells 11 and 211 mod 225, hits `45 = 9·5` and `846 = 9·94`, cofactors 5 and 94 — `hother` fails (`localPrimeComb 5 5 = −1` vs `localPrimeComb 5 94 = +1`), and for any `upper ≥ 5` (`hupper` forces `upper ≥ 94`) both corrected weights are `−1`, so the sign-reversal **conclusion** fails too. Scoped to this transport, this pair, this modulus: `hother` HOLDS for 182/210 ordered odd-prime pairs at the canonical period, and `hstate` fails at all 210 (a measured, not proved, universality) (043).
- **B4 pin-modulus transport, sign-blind**: at the canonical pin with `1 ≤ t ≤ y`, the shipped `primeSieveFiniteDifference_backward_increment_norm_le_active` RHS charges at least `(A+B)·#{S-smooth squarefree d ≤ t}`; at saturation `S = primesUpTo y` this is `≥ 0.4·t·y/log(y+1)`, hence `≥ 0.4x/log x` at full window `t = y`, so B4 bridges at most `T ≲ x^ε·log x` of fiber distance inside an `x^{1/2+ε}` budget in any step schedule. Its excursion converters are inert at exponent `≥ 1/2` (window capped at `y ≈ √x`, single-fiber modulus `≤ 2.3√x`, so window-moment and pointwise statements are mutually implied up to `O(√x)`). B4 is a LOCAL rigidity tool. NOT killed: small wheels (`S = primes ≤ 20` at `y = 10^6` gives ≈ `26√x`), local use around independent anchors, the B3-recurrence half of F2, and the truncated-operator route (`finiteDifferenceOperatorUpTo` + `finiteDifferenceOperator_eq_upTo_add_tail`) (043).
- **Prime-insertion filtration energy monotonicity via `C_p ≥ 0`**: refuted as an order-independent hypothesis and in both orders tested — `C_p < 0` at a large fraction of steps in increasing order, and at 30.4/33.8/41.2/44.1% of steps at `N = 2000/5000/10^4/2·10^4` along a `√x`-optimal greedy order. Measured accompaniment (window `N ≤ 3·10^5`, not a theorem): in increasing order `max_j E_j/N² = 9.49 / 60.0 / 149.8` at `N = 10^4 / 10^5 / 3·10^5`, with negative correlation mass of the same size. NOT killed: other per-step flux conditions, centered variants, and untested specially constructed insertion orders (043).
- **gcd-layer reorganization of `M(x)²` as submitted**: the coordinate is self-inverse (`M² = Σ_g μ²(g)C_g(x/g)`, `C_g = Σ_e μ(e)M_{ge}(z/e)²`, composition returning `M²` via `λ = (μ²)^{-1}`; both directions verified exactly), and the submitted per-layer inversion opens into the rough squares `M_{ge}(z/e)²`, whose uniform-in-`g` bound is RH-equivalent both ways. Measured accompaniment: `T(x) = Σ_g μ²(g)|C_g(x/g)|` has `T/(x log x) ∈ [0.40, 0.50]` over `x = 10^3..10^6`, so in the tested range triangle-over-`g` loses no scale and no cross-layer cancellation is needed — no asymptotic claim about `T(x)` is made. NOT killed: cross-layer inequalities of a different shape (043).
- **Sign-blind insertion into the square-cutoff renewal skeleton**: `φ(θ) = (1+θ)/2`, with `φ(θ) > θ` for every `θ < 1` and fixed point 1 — signed exact composition is exponent-preserving (relocation), sign-blind instantiation is exponent-WORSENING, even granting `matched(R) ≪ R^{1+ε}`. Sharpens the existing "renewal-only iteration" entry (043).
- **Uniform per-stage envelopes on the downward-closed fresh-prime filtration**: for `finiteDifferenceOperator (primesUpTo P)` at the 0-vanishing indicator and `X/3 ≤ P < X/2`, exactly `g_{<P}(X) = M(X) + π(X) − π(X/2)`, so any uniform envelope with exponent `α < 1` contradicts a Chebyshev-strength lower bound on `π(X) − π(X/2)`. Scoped to that operator, that indicator and that plateau. NOT killed: non-downward-closed filtrations — a state-aware greedy order attains the exact floor `sup_x |g_S(x)|/√x = 1.000000` at every one of 78,498 stages at `N = 10^6` (043).
- **Sum rules from a fixed finite prime set**: no inequality derived **solely** from squarefree support, multiplicativity, and prescribed sign `−1` at the primes of a fixed finite `P` can certify an exponent below 1 — the witness `g_P` models exactly that theory and has `Σ_{n≤4K} g_P(n) = c_P·K + O(√K)` with `c_P = (24/π²)∏_{p∈P}(p−1)/(p+1) > 0` (exact to `K = 10^9`: 0.8105695, 0.2701898, 0.1688690). NOT killed: any system also using `μ*1 = δ` or sign data at infinitely many primes — `(g_P*1)(n) = ∏_{q|n}(1+g_P(q))` vanishes as soon as `n` has a prime factor in `P`, so `g_P` violates `μ*1 = δ` exactly on `{n > 1` with no prime factor in `P}`, of density `∏_{p∈P}(1−1/p) > 0` (measured 999/2000, 533/2000, 457/2000 for `P = {2}`, `{2,3,5}`, `{2,3,5,7}`) (043).
- **Mechanisms consuming the record-040 summary statistics (pair TV, triple CMI)**: the δ-biased core-resigning field (`ε(m) = +1` w.p. `1/2+δ` per core coprime to 30, extended by exact 2-3-5 multiplicativity onto `μ`'s zero pattern) matches `TV27 = 0.1350070318` to 10 dp and `CMI` inside `[0.225, 0.270]` while its partial sum grows linearly (`0.00958·K` at `δ = 0.02`, `0.02596·K` at `δ = 0.05`), so those statistics admit completions at exponent 1. NOT killed: mechanisms consuming the complete lag-1/lag-2 joint laws — the `L1` pair-law comparison was run only for the unbiased model, not for the δ-biased one. Reattribution: record-040's `TV = 0.1350` and `CMI = 0.248` are zero-pattern statistics — `TV27 = TV8` to 10 dp at all tested `K ≥ 2·10^5`, and `CMI8 = 0.2474` with the 27-state excess decreasing with scale, consistently with plug-in bias — and carry no sign information in either direction (043).

Corrections to existing entries, to be applied at merge time:

- "Renewal-only iteration: stalls at `x^{1/2+ε}`" — append the `φ(θ) = (1+θ)/2` sharpening above.
- "Markov/mixing on 27 states: TV 0.1350 flat, CMI 0.248 nats flat (040)" — annotate that both statistics are zero-pattern facts. The surviving kill is of unconditioned 27-state mixing assumptions that predict decay of the reported full-state TV/CMI; models conditioned on the zero pattern, and claims about sign mixing alone, are not addressed by these numbers.
- Dossier section B should gain `mertensSummatory_eq_dyadicCofactorBoundaryMass` (`DyadicTransportCanonicalForm.lean:235`) and the `DyadicTransportCompression.lean` machinery.
- **Dossier constraint D4** (the trilemma) — its horn-1 rule "a split preserves RH scale in every piece iff it partitions the summation index `{n}` itself" must be replaced in the `index partition ⟹ scale preserved` direction; see §4.0 for the counterexample (the canonical orientation split is a plain unit-weight index subset by an elementary bijection, verified against a direct class-sum computation at 25 values of `R ≤ 2000`, and its `G` piece sits at effective exponent ≥ 1.4 against a target of 1), and for the replacement wording. The three horns survive as a catalogue of observed failure modes; horn 1 must not be cited as a scale-preservation guarantee.

---

## 7. Ship record

The verifiers' ranking, with each item's required conditions. Nothing here is
quantitative progress toward the target Prop; every entry is infrastructure
or a certified no-go, and the conditions are what keeps it from being
mis-cited as progress later.

1. **`induction-a`'s complement-smooth inversion lemma** — ranked first by
   `verify-null-certificates`; being shipped in parallel. Statement over repo
   objects: for disjoint prime Finsets `S, T` and `f` with `f 0 = 0`,
   `finiteDifferenceOperator S f x = Σ` over
   `n ∈ (Finset.Icc 1 x).filter (∀ q ∈ n.primeFactors, q ∈ T)` of
   `finiteDifferenceOperator (S ∪ T) f (x/n)`. Verified EXACT at `X = 20000`
   for `y = 5, 20, 97, 313`, zero mismatches in all four runs. Conditions:
   state it for **arbitrary** disjoint `S, T` (not only downward-closed `S`)
   — that generality is the whole point, and it is what makes this the one
   artifact the greedy-order counterexample does not dent; proof by induction
   on `T` from `finiteDifferenceOperator_insert` plus the terminating Neumann
   series (`⌊x/n⌋ = 0` for `n > x`); the docstring's Mertens consequence must
   carry the saturation hypothesis — it is `M` on the right only when
   `S ∪ T ⊇ primesUpTo x`, and only then does it say that every intermediate
   field is a positive-weight convolution of `M` at reduced arguments, so a
   "good path" is itself an `M`-autocorrelation statement.

2. **`involution-b`'s stage identity** — for `X/3 ≤ P < X/2`,
   `g_{<P}(X) = M(X) + π(X) − π(X/2)`, over
   `finiteDifferenceOperator (primesUpTo P)` at the 0-vanishing indicator.
   Verified over every `P` in the plateau at `X = 10^5, 10^6, 4·10^6`, zero
   mismatches. Conditions: **ship the identity only**. Do NOT ship the
   offered corollary in its stated form — it needs `π(X) − π(X/2) ≫ X^{α+δ}`,
   which is Chebyshev-strength, not Bertrand-strength, and "extractable from
   Mathlib's Bertrand machinery" understates the work; the honest source is
   the repo's NativePNT stack (dossier B10). Do NOT ship the accompanying
   registry principle ("no target-compatible per-stage invariant; future
   mechanisms must be stage-blind") — the scoped §6 entry replaces it.

3. **`moment-a`'s parallelogram / fiber bookkeeping** —
   `Σ_{X≤N}(g(X) − g(⌊X/p⌋))² = Σ g² + Σ (shift_p g)² − 2Σ g·shift_p g`,
   together with `Σ_{X≤N} g(⌊X/p⌋)² ≤ p·Σ_{u≤⌊N/p⌋} g(u)²` (needs only
   `g(0) = 0`). Both re-derived and confirmed by `verify-null-certificates`
   (fiber size `≤ p`; the `m = 0` fiber is killed by `g(0) = 0`). Conditions:
   low content standing alone, but it is exactly the instrument an
   order-search revival needs, so its expected value rose as a result of the
   audit; ship it **instead of** `induction-b`'s weighted one-step variant,
   which is the same identity with a weight attached (that one is HOLD —
   duplication).

4. **`N_active` floor refactor** — the same theorem was produced independently
   by `contrarian` and `wildcard`; `verify-pin-kill` reproduced both numeric
   sets from scratch and confirmed the convergence is real. Ship **one**.
   Conditions: prefer the contrarian's `Nat` form `2*t/5 ≤ card` over the
   wildcard's `(2 − π²/6)·t − 1 ≤ (card : ℝ)` (stronger constant, no `ℝ`, no
   `π`, no Basel/tsum plumbing, no spurious `6 ≤ t`, no cosmetic `−1`). The
   `2/5` constant CANNOT be proved from `Σ_{m≥2} 1/m²`, which gives only
   `0.355t`; it needs the prime-restricted union bound
   `Σ_p ⌊t/p²⌋ ≤ 0.522t`, hence `Q(t) ≥ 0.478t ≥ 2t/5`. Recommended refactor
   (better than either as submitted): (A) a constant-free subset lemma
   `((Finset.Icc 1 t).filter Squarefree) ⊆ ((primorial (primesUpTo y)).divisors.filter …)`
   for `1 ≤ t ≤ y` at the canonical pin, which is where all the arithmetic
   lives and is provable in hours; (B) the numeric corollary plus the payload
   corollary bounding the shipped `_le_active` RHS from below, which is what
   makes it a deliverable rather than a curiosity. State the general
   active-fiber floor (`#{S`-smooth squarefree `d ≤ t}`) first and the
   saturation corollary second, so nobody applies `0.4t` to a small wheel.

5. **Narrowed `hother` counterexample** — `verify-hother-kill` verified every
   numeral twice and proved the proposed lemma in Lean. Conditions: accept
   **only** with the claim text rewritten to "for `(p,q) = (3,5)` with
   `S = {3,5}` and flip prime 3, the `p²`-cofactor transport fails `hother`;
   no claim is made about other transports or other moduli". Strongly prefer
   the **conclusion-level upgrade** (verified true at the same witness:
   corrected weights `−1` and `−1`, so sign reversal itself fails, not merely
   its sufficient condition; needs `upper ≥ 5`, and `hupper` forces
   `upper ≥ 94`, so it is safe) — both existing no-gos in this family prove
   conclusion-level statements, so the hypothesis-level version is below the
   repo's own standard. Prefer the kernel-clean proof route (fix
   `(4 : ZMod 9)⁻¹ = 7` and `(4 : ZMod 25)⁻¹ = 19` by
   `ZMod.inv_eq_of_mul_eq_one`, then discharge the residue equation through
   `Equiv.symm_apply_eq` against the computable forward `castHom`) over
   `native_decide`: plain `decide` FAILS here — the blocker is
   `ZMod.chineseRemainder → Nat.xgcd` well-founded recursion, not the
   225-element search space — and while `native_decide` is legitimate in an
   `Arithmetic` no-go module, it must not enter the protected chain. Fix the
   miscomputed comb null (the product null is `41/81 = 0.5062`, not `~0.47`;
   measured 0.4965 on 60k samples) before anyone runs the falsifier. Note
   `primeWheelSmoothCoreSite` is defined with `classical`, so the upgraded
   form is not `decide`-able and needs explicit `if_pos`/`if_neg`.

6. **Octave lemma, with prior art cited** — `spectral-a/octave-increment-skeleton`
   and `spectral-b` propose the same Lean deliverable; ship ONE PR, under
   `spectral-a`'s framing (which concedes the relocation up front and
   self-scores the lemma as bookkeeping). Conditions, all from
   `verify-resigning-kill`: (i) derive the octave corollary from
   `mertensSummatory_eq_dyadicCofactorBoundaryMass`
   (`DyadicTransportCanonicalForm.lean:235`), or at minimum cross-reference it
   as prior art, and state plainly that the corollary is a coordinate
   restatement, not a new identity; (ii) ship the two `threeSlotWb` lemmas
   plus the two chi-level interleave lemmas (≈ 40 lines) and drop or
   explicitly mark the "quadratic pair-transport" lemma as the termwise
   triviality it is (`(−x)(−y) = xy`); (iii) do NOT ship `spectral-b`'s
   sentence that the lemma converts record-040's memory finding into
   kernel-checked arithmetic — it is false, the memory is a zero-pattern fact;
   (iv) `spectral-a`'s memory-floor remark may ship only in weakened form,
   with the zero-pattern attribution attached; (v) the χ₄-annihilation remark
   may appear as one docstring sentence but must not be billed as explaining
   the D4 GRH horn (it is the `q = 4` instance of a textbook fact) nor as a
   reduction (`U` is itself RH-equivalent). Priority: low; hours of work.

7. **`P`-generalized witness** (`spectral-a/finite-prime-sum-rule-witness`) —
   `verify-sumrule-kill` verified both halves and the entire proof-route
   arithmetic. Conditions: (i) **generalize** `witnessG` to take a finite
   prime set, or at minimum instantiate at `P = {2,3,5}` as well as `{2}` —
   as written with `P = {2}` alone the artifact is defeated by the 3-adic
   dilation identity `μ(12k+3) = −μ(4k+1)`, which the witness violates at
   202,614 sites; (ii) state the scope in the theorem docstring, not only in
   prose: "squarefree support plus `μ`'s sign at the primes of `P` does not
   force sub-linear slot growth; constraints using sign data at primes outside
   `P`, in particular `μ*1 = δ`, are not covered"; (iii) file it as a no-go
   (e.g. `RHLean/Arithmetic/FinitePrimeSignWitnessNoGo.lean`), never under
   `RHLean/Proof/SquareRoot*`; (iv) do not give `witnessG` simp lemmas that
   could be confused with `μ` lemmas. Effort: 3–7 days, not "days" — the
   rational tail bound in Nat/Int arithmetic is the real work.

Lemmas from the three killed positive routes that the verifiers nonetheless
rated shippable, all with mandatory anti-mis-citation conditions and none
counting as this round's quantitative progress:

- **Overlap-square pin** (`MobiusOverlapSquarePin.lean`, new file beside
  `MobiusRenewalTelescope.lean`). Verdicts split: `osp-math` SHIP with an
  honest-novelty tag, GPT-5.6 ship as bookkeeping only, `osp-constraints`
  HOLD. Conditions if shipped: docstring must state that `J(A) = M(A)²`
  identically and the file is substrate; the corollary must be dropped or
  labelled as the trivial consequence of squares being nonnegative, never as
  "the first unconditional inequality between two signed renewal objects";
  the docstring must record that `Σ_{A≤T} M(A)² ≪ T^{2+ε}` is RH-equivalent.
  `osp-math` suggests proving it by direct inclusion–exclusion on the pair
  Finset rather than by the split-and-re-swap, which avoids both floor lemmas
  and the re-indexing bijection.
- **`correctedPrimeWheelSite_mul_selectedPrime_eq_neg`** — verified true by
  hand and by 10^4 random trials (`mfd-math`: zero failures, 9586 non-vacuous;
  both `p*n ≤ upper` and `hSprime` are load-bearing). Conditions: file is
  `RHLean/Arithmetic/PrimeWheelCorrectedLocalFlip.lean`, not `Analysis/` as
  the proposal states; `hn : n ≤ upper` is redundant; do NOT ship it as "the
  first non-vacuous full instantiation of the B7 package"; if the
  `p^a·base(b)` package corollary ships at all it must carry a docstring
  stating that the realization is not CRT-anchored — it does not depend on
  `q`, `K`, or `collisionExponentStateResidue`, and no theorem relates its
  frontier sum to any Mertens prefix.
- **`threeSlot_supPow_le_scaleMoment`** — verified with zero violations for
  all `K_0 ≤ 5·10^5` at the tightest legal `K` for `m = 1,2,3`. Conditions:
  ship the strengthened constant-free `Int` form (drop the `+9`, no Complex
  detour, no `mertensSummatory`); the docstring must state that it is an
  instantiation of `affineExcursion_moment_le` (`AffineExcursion.lean:77`) at
  `A = 3, B = 0`, not a new bridge — the genuinely new delta is the `M4`
  Lipschitz modulus, `|M4(k)| ≤ 3k`, the window reindexing, and the
  rearrangement; and it must record the domination inequality
  `(1+2mθ)/(2m+1) ≥ θ` and the Hölder+Mellin collapse, so no future reader
  mistakes the `m = 1` rung for progress.

HOLD / REJECT, for completeness: `moment-b`'s gcd collapse lemma is HOLD (it
certifies a dead coordinate with near-zero downstream reuse; if it ships at
all, ship it **without** the `θ*` pre-screen unless the `s = 0.654 / θ* ≈ 0.673`
correction and the pre-asymptotic caveat are both in the docstring).
`induction-b`'s weighted one-step energy identity is HOLD (duplicate of item
3). `renewal-a`'s fiber regrouping `squareRootFarPrimeTransport` is REJECT —
the arithmetic is right, but it is a one-line `Finset.sum_fiberwise` on top of
a theorem already on main.

---

## Verification ledger

| Claim class | Reviewed by | Method |
|---|---|---|
| OSP kill | `osp-constraints`, `osp-math`, `gpt56_osp_verdict` | independent identity checks (88 and 501 values of `A`, `M2` computed by convolution), independent `Ξ_bal` and averaging-gain probes, Mellin equivalence derived by all three |
| MFD kill | `mfd-constraints`, `mfd-math`, `gpt56_mfd_verdict` | Lean source audit, prime-pair counting to `x = 10^12`, 512-subset enumeration of defect labels, 10^4-trial transcription check, tree-wide grep for a frontier↔Mertens anchor |
| EMI kill | `emi-constraints`, `emi-math`, `gpt56_emi_verdict` | own sieves to `K = 5·10^6` and `10^6`, exact bit-check of the `E_1` kernel identity, exponent-domination table, novelty audit against `AffineExcursion.lean` |
| Four null mechanism kills | `verify-null-certificates` | independent C reimplementations; all central identities reproduced to the integer |
| hother narrowing | `verify-hother-kill` | Python from repo definitions + Lean 4.24.0 `#eval` + `native_decide` proof + 210-pair genericity probe + 60k-sample statistics |
| Pin-kill saturation scoping | `verify-pin-kill` | Lean source read in full, brute-force of the literal filter at `y = 10,20,30,50`, independent recomputation of both panelists' numeric sets |
| Sum-rule scoping | `verify-sumrule-kill` | exact inclusion–exclusion to `K = 10^9`, `p`-adic dilation stress tests at `p = 3,5,7`, witness-vs-`μ*1=δ` density test (its parenthetical description of the violation set is corrected in §2; its counts are right) |
| Measurement reattribution | `verify-resigning-kill` | from-scratch replication, 8-state zero-pattern control, iid and constant-field controls, δ-biased impostor construction |
| Greedy-order revival (§3), orientation-split closure (§3), D4 falsification (§4.0) | phase-3 numerics (EC2, 16 cores), twice GPT-5.6-reviewed | greedy path to `N = 10^6` with a corrected candidate test and full `O(N)` audits (zero mismatches) plus fixed-order, random-order, tie-break, candidate-budget and cross-horizon controls; `G(R)` at every integer `R ≤ 10^8` by dyadic-block RMS with lower-cutoff sensitivity; `M(R²−1)` at every integer `R ≤ 5.29·10^5` from two independent segmented sieves (Mertens checkpoints to `10^11` correct); the regrouping identity checked at all `10^8` values; the orientation class sum computed directly and matched to `−G(R)` at 25 values of `R` |

Claims in this report that are **asserted rather than verified**, labelled as
such in place and repeated here: the structural explanation offered for
`hstate`'s 210/210 failure (the measurement is verified, the reason is stated
but unproved); `moment-a`'s claim that first-order centering collapses onto
the renewal stall (the proposal's, not checked by the verifier);
`induction-a`'s assertion that the residual sub-block
`Σ_p Σ_x M(x)M(⌊x/p⌋)` at RH scale is RH-equivalent; `spectral-b`'s claim
that the closure of its exact constraint set is the renewal hierarchy
(asserted with no definition of closure); and `osp-math`'s
averaging-exponent argument in §5 R5, which rests on a limiting-distribution
result carrying hypotheses beyond RH (Linear Independence plus a
negative-moment assumption) and is recorded as an argument, not a fact.

The phase-3 results are now incorporated (§3, §4.0). Their own stated limits,
carried here unchanged: the greedy revival is an existence result about
orderings whose rule reads `μ`, its branching measurements are estimated
fractions from a systematic sample along *sampled successful trajectories*
(local commonness, not abundance of complete paths), the
degrees-of-freedom-versus-arithmetic attribution was not settled because the
arithmetic-destroying surrogate control was not run, and no horizon-independent
ordering or invariant is exhibited; on the orientation side, "strongly
unsupported on the tested upper blocks" does not asymptotically exclude
`R^{1+o(1)}`, the independent-sign `σ(R)` is a null scale rather than a lower
bound, the extrapolated scale-destruction factor beyond the common range is
conditional on `A_2(M(R²−1))/T` continuing near 0.25 where it was not
measured, and the D4 counterexample's class is horizon-dependent.
