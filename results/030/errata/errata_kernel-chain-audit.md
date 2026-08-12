# Errata draft — target: kernel-chain-audit (results/029 certification)

Certifier: independent re-derivation against mobius-synthesis origin/main
aa141af (fetched 2026-08-12; includes today's upstream "Research update")
and governance records 015/017/026. All greps, algebra, and numerics redone
from scratch; python spot-checks in this scratchpad directory. Verdicts:
7 CONFIRMED, 2 PARTIAL, 0 REFUTED.

Kernel facts re-verified and used throughout (notation):
- D = `primeSieveMoebiusDiscrepancySum y x` = Σ_{d≤K} μ(d)·R(⌊x/d⌋)  (Abel face)
- P = `primeSieveAbelBoundary y x` = M(K)·R(y), K = ⌊x/(y+1)⌋
- E = `primeSievePNTError y x`;  Abel identity (no hypotheses): E = D − P
- Q = `primeSieveSmoothMobiusMass`, S = `primeSieveReciprocalMertensSignedSum`,
  B = `primeSievePNTBulk`, T = `primeSieveSmoothPNTCorrectedRemainder` = Q − B
- Under `hroot : Nat.sqrt x < y` (⇔ x < y²): Q = M + S and E = S − B,
  hence T = M + E and M = T − D + P.  (Theorem names as cited in the audit;
  all exist on origin/main and compose exactly as claimed.)

---

## Finding 1 (fatal) — no kernel arrow "Abel face ⇒ RH" — CONFIRMED

Re-verified on origin/main aa141af (which includes the new NativePNT*
modules): `primeSieveMoebiusDiscrepancySum` occurs in exactly three files
(PrimeSieveAbelIdentity, PrimeSieveLipschitzExcursion,
PrimeSieveBackwardAffineExcursion); those files contain zero occurrences of
`NonzeroResponseRHScale`, `MertensEnergyBoundedStatement`,
`ProjectedRenewalQuadraticBoundedStatement`, `RiemannHypothesis`; no other
module imports them; no `AbelFace*` predicate exists anywhere.

**Correction — results/026/packet.md §Problem (lines 10–12), and the
identical sentence in results/017/packet.md:**

Wrong text:
> "A kernel-verified chain (Lean 4/mathlib, no unproved premises)
> establishes: if the target below holds, the Riemann Hypothesis holds."

Replacement:
> "A kernel-verified chain (Lean 4/mathlib) establishes: if the QUADRATIC
> face below holds, the Riemann Hypothesis holds
> (`projectedRenewalQuadraticBounded_imp_riemannHypothesis_unconditional`,
> via the proved forward Mertens criterion). NO kernel theorem connects the
> Abel face to RH: the Abel face is one summand of an exact identity for
> `primeSievePNTError` and is not the hypothesis of any implication in the
> repository."

**Correction — standing program-state narrative** ("a kernel-verified Lean
chain reduces RH to ONE estimate, the Abel face"): replace with "the kernel
chain reduces RH to the quadratic face / Mertens energy; the Abel face is an
exact coordinate for one summand of `primeSievePNTError`, with no formal
arrow to RH."

## Finding 2 (fatal) — "ONE estimate" false; M = T − D + P — CONFIRMED

Algebra independently re-derived (see notation block above): with
x < y², M = T − D + P where T = M + E contains M itself and P = M(K)·R(y)
is uncontrolled. Symbol usage re-verified: `primeSieveSmoothPNTCorrectedRemainder`
and `primorialCollapseSmoothCenteredResponse` occur only in
PrimeSieveCollapseIdentity.lean; `primeSieveAbelBoundary` only in
PrimeSieveAbelIdentity.lean; no bounding theorem exists for T or P anywhere.

**Correction — anywhere "one estimate"/"sole remaining obligation" appears:**

Replacement text:
> "Bounding the Abel face D alone does not bound M: the kernel identities
> give M = T − D + P with T = M + E (the smooth PNT-corrected remainder,
> which contains M) and P = M(K)·R(y) (the Abel boundary). A genuine
> Abel-face reduction requires, in addition to |D| ≪ x^{1/2+ε}, an
> independent bound on T that does not route through M, and a bound on P —
> neither of which exists formally or informally."

## Finding 3 (fatal) — collapse and canonical-pin domains disjoint — CONFIRMED

Re-derived and numerically spot-checked (y = 2..7 and at scale 10^12):
every collapse identity producing M or C−2E carries `hroot : Nat.sqrt x < y`,
i.e. x < y²; the backward excursion lives at x₀ = `primeSieveCanonicalPin y`
= (y+1)²−1 = y²+2y with window points in [x₀−y, x₀] = [y²+y, y²+2y], entirely
≥ y². Nat.sqrt(x₀) = y, so hroot fails by exactly one at the pin, for every y.
Block instantiation verified: y_k = Nat.sqrt(U_k)+1 = s+1 (with
`primorialWheelCutoff` = Nat.sqrt U_k), pin = (s+2)²−1, window bottom
= (s+1)(s+2) = s²+3s+2 > (s+1)² > U_k — the whole window lies above the
primorial block, covering none of the square samples X_n = (n+1)²−1 ≤ U_k.

**Correction — results/023 and results/024 narrative (backward pin as the
"composition point"), and results/026/packet.md §named central object:**

Add:
> "DOMAIN CAVEAT (kernel-checked): the collapse/centering identities require
> x < y², while the backward excursion window at the canonical pin
> x₀ = (y+1)²−1 is [y²+y, y²+2y]. For every y these ranges are disjoint;
> at the chain's block cutoff y_k the entire excursion window lies strictly
> above the primorial block U_k. The excursion machinery and the collapse
> chain currently apply at no common (y,x); composing them requires either
> an extension of the collapse identities to x = y²+O(y) or a transport
> lemma across the block boundary. Neither exists."

## Finding 4 (fatal) — "two kernel-equivalent faces" false — CONFIRMED

The only kernel equivalences are
`nonzeroResponseRHScale_iff_projectedRenewalQuadraticBounded` and
`projectedRenewalQuadraticBounded_iff_mertensEnergyBounded` (verified on
origin/main); no theorem in either direction mentions the Abel face together
with any of these. The phrase "Target (two kernel-equivalent faces; attack
either)" appears verbatim in BOTH sealed packets (results/017/packet.md
line 13, results/026/packet.md line 14).

**Correction — results/026/packet.md line 14 and results/017/packet.md line 13:**

Wrong text:
> "## Target (two kernel-equivalent faces; attack either)"

Replacement:
> "## Target
> **Quadratic face (kernel-connected to RH):** ProjectedRenewalQuadratic-
> BoundedStatement — proving it yields RH by kernel theorem.
> **Abel face (exact coordinate, NOT kernel-connected to RH):** the estimate
> |Σ_{d≤K} μ(d)·R(⌊x/d⌋)| ≪_ε x^{1/2+ε} concerns one summand of the exact
> identity E = D − M(K)R(y); a proof of it does not currently imply RH
> through any formal or informal chain we possess."

Any external communication repeating the equivalence claim must carry the
same correction.

## Finding 5 (major) — collapse "remainder" not independent; coordinate
change is circular — CONFIRMED (with one citation-freshness note)

Re-derived: `mertensSummatory_eq_pntCorrectedAllPlus_sub_two_error` gives
M = C − 2E, so C = M + 2E; the Li-subtracted collapse identity reads
C − 2E = −E + T, which after substituting T = M + E is M = M. The remainder
is separately DEFINED (smooth Möbius mass minus bulk) but provably equal to
M + E, so it is not an independent object.

Citation note for the coordinator: the upstream dead-lane entry
`pnt-reciprocal-coordinate-change` (kind "circular", closed_on 2026-08-10,
with the quoted equivalence text and |C|/|M| median 1.296) is verbatim at
upstream commit bf8c360, but was REMOVED from boundary/dead_lanes.json in
today's upstream commit aa141af ("Research update"), which rewrote the lane
list down to three entries. The errata should cite the identity itself and
commit bf8c360, not current main's ledger.

**Correction — any record quoting the collapse docstring "The remainder is
*defined*, not residual" as evidence of independence:**

Add:
> "The remainder is independently defined but NOT independent: kernel
> theorems force T = M + E and C = M + 2E, so the pair of obligations
> {|C| ≪ s, |E| ≪ s} is equivalent to {|M| ≪ s, |E| ≪ s} — strictly
> stronger than the target. The coordinate change relocates the difficulty;
> it does not reduce it (upstream reached the same conclusion independently,
> lane closed 2026-08-10, commit bf8c360)."

## Finding 6 (major) — dropped RH-strength boundary term M(K)R(y) — CONFIRMED
(one scoping note)

The identity `primeSievePNTError_eq_moebiusDiscrepancySum_sub_abelBoundary`
is hypothesis-free and carries −M(K)·R(y) exactly as results/015 recorded.
Best unconditional inputs (Walfisz/Vinogradov–Korobov shapes for both M and
π−Li) give only |M(K)R(y)| ≪ x·exp(−c(log x)^{3/5}(log log x)^{−1/5})
= x^{1−o(1)} at y ≍ √x, far above x^{1/2+ε}; no kernel theorem addresses P.
Scoping note: results/026/packet.md omits the term entirely;
results/017/packet.md line 17 mentions it but waves it off ("separately
self-consistent at 1/2") with no bound — an assertion, not an estimate.
Also, strictly the obligation is on the PRODUCT M(K)·R(y), formally weaker
than RH-strength control of each factor; but no unconditional route to
x^{1/2+ε} for the product is known, so the "second RH-strength obligation"
characterization stands.

**Correction — results/026/packet.md Target section (after the Abel face
line 16–17):**

Add:
> "The Abel face equals E + M(K)R(y) exactly. Any use of an Abel-face bound
> therefore also requires |M(K)·R(y)| ≪ x^{1/2+ε} at the same (y,x); at
> y ≍ √x this is a second obligation of RH strength at scale √x for the
> product, with best unconditional bound only x^{1−o(1)}."

**Correction — results/017/packet.md line 17:** delete "(The boundary term
M(K)R(y) is separately self-consistent at 1/2.)" and substitute the text
above ("self-consistent at 1/2" is a conditional-on-RH statement presented
as if it discharged the term).

## Finding 7 (major) — "W ≍ √x" wrong; window is ~x^ε·log x — CONFIRMED
(constant-factor slip noted, immaterial)

Numerically re-verified at x ≈ 10^12: with C = 1 + y/log(y+1) ≈ 2√x/log x
and a pin height H = x^{1/2+ε}, ⌊H/2C⌋ = x^ε·log x/4 exactly (checked to 3
significant figures for ε ∈ {0.01, 0.05, 0.1}); the cap W = y+1 ≈ √x binds
only when H ≥ 2C(y+1) ≈ 4x/log x (the audit wrote "≈ 2x/log x" — a factor-2
slip; the conclusion "spike near the trivial ceiling" is unaffected).
Additional derivation: even granting a mean-square bound ≪ x^{1+ε} over a
FULL window W₀ ≍ √x, the excursion moment inequality yields only
H ≪ (8·C·W₀·x^{1+ε})^{1/3} ≈ x^{2/3+ε}, NOT the pointwise target; the
implication as printed in the packet is false. What is true: a mean-square
bound ≪ x^{1+ε} over the ACTUAL excursion window (length ~x^ε log x at
target heights) implies the pointwise target — i.e. the sanctioned averaged
coordinate is essentially pointwise, as the audit says.

**Correction — results/026/packet.md lines 28–31:**

Wrong text:
> "Consequently a **windowed mean-square upper bound**
>   (1/W)·Σ_{t<W} |S(y, x₀−t)|² ≪_ε x^{1+ε}   (W ≍ √x)
> implies the pointwise target at canonical pins. Averaged attacks are
> therefore sanctioned coordinates, not a cheat."

Replacement:
> "Consequently a windowed mean-square upper bound
>   (1/W)·Σ_{t<W} |S(y, x₀−t)|² ≪_ε x^{1+ε}
> implies the pointwise target at canonical pins ONLY when it holds with
> W equal to the kernel's backward window W = min(y+1, ⌊H/2C⌋), which at
> target heights H = x^{1/2+ε} has length ≈ x^ε·log x/4 — not ≍ √x. The
> averaged coordinate is therefore essentially pointwise; a mean-square
> bound over windows of length ≍ √x yields only H ≪ x^{2/3+ε}."

Round-3 proposal scoring that relied on the "(W ≍ √x)" affordance
(obstacle 3 as AMENDED) should be flagged in the 026/027 records.

## Finding 8 (minor) — y ≍ √x vs block-constant cutoff conflation — PARTIAL

Right, and re-verified: in the composed centering chain
y_k = `primorialPNTPrimeSieveCutoff k` = Nat.sqrt(U_k)+1 is constant across
the block (L_k, U_k], every collapse theorem forces y > √x (hroot), and the
free-parameter "y ≍ √x" of the standalone Abel identity is a different
convention silently identified with it in the packet prose ("with y ≍ √x,
K = ⌊x/(y+1)⌋", 026 line 16 / 017 line 15).
Wrong, and the reason for PARTIAL: "exceeds √X_n by an astronomical factor
for all but the topmost samples" — the excess factor is bounded by
√(U_k/L_k) = √(wheelPrime k) ≈ √(log U_k) (verified from
`primorialEndpoint`/`wheelPrime` = Nat.nth Nat.Prime: e.g. ~172 for the
10^12835-scale blocks cited in the packet), a slowly growing but decidedly
modest factor; likewise K is below √x by at most that same factor. The
correct statement: y_k/√X_n is unbounded over k (so no uniform ≍), but is
≤ √(p_k) ~ √(log x) within each block — not astronomical.
Load-bearing note: this minor becomes load-bearing for any REPAIR of the
chain (findings 1–3): a repaired composition must pick one y-convention and
carry the √(log x)-factor bookkeeping explicitly.

**Correction — results/026/packet.md line 16 (and 017 line 15):** append
> "(y is a free parameter of the standalone Abel identity; the composed
> centering chain instead fixes y_k = √U_k + 1 per primorial block, where
> y_k/√x ranges over [1, √(p_k)) ≈ [1, √(log x)) across the block — the two
> conventions are not interchangeable.)"

## Finding 9 (minor) — axiom audit scope — CONFIRMED

All sub-claims re-verified on origin/main: TerminalAxiomAudit.lean guards
exactly three theorems; two of them
(`projectedRenewalQuadraticBounded_iff_riemannHypothesis`,
`canonicalHighUniformLocalBounded_iff_riemannHypothesis_realized`) take
`criterion : ClassicalMertensRHCriterion` as an explicit argument, which
`#print axioms` does not surface; that structure is never inhabited in the
repo (only the strictly weaker forward-only `MertensForwardCriterion` is,
by theorem `mertensForwardCriterion`); the criterion-free arrows the
program needs (`riemannHypothesis_of_mertensEnergy`,
`projectedRenewalQuadraticBounded_imp_riemannHypothesis_unconditional`) lie
outside the guarded file; `native_decide` appears in exactly four modules
(SmallModulusResonance, FourPrimeWheelCancellation,
SquareBlockPrefixCombSweep, CompleteFermatSieve); no textual `sorry` or
declared `axiom` in RHLean. Severity minor is correct: the forward
direction is criterion-free and discharged, so "no unproved premises" is
very likely true for the direction used — just not machine-guarded.

**Correction — recommend (upstream PR material, not a record edit): add
`#guard_msgs`/`#print axioms` entries for `riemannHypothesis_of_mertensEnergy`
and `projectedRenewalQuadraticBounded_imp_riemannHypothesis_unconditional`,
and rephrase "no unproved premises" in packets to "axiom footprint
[propext, Classical.choice, Quot.sound], machine-guarded for the quadratic-
face arrows" once the guards exist.**

---

## Cross-cutting note for the error ledger

Findings 1–4 constitute (at least) informal-math errors #9–#11 as the audit
proposed: (#9) the missing Abel-face arrow presented as a kernel reduction,
(#10) the dropped boundary obligation, (#11) the collapse/pin domain
disjointness. Finding 7's "(W ≍ √x)" mis-affordance arguably merits a
separate ledger entry since blind round-3 proposals were scored against it.
