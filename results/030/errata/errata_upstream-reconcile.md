# Errata draft — target: upstream-reconcile (record 029 certification)

Certifier: independent re-derivation session, 2026-08-12. All nine findings examined
(5 fatal/major mandatory + 4 minors skimmed and certified). Verdicts: 9 CONFIRMED,
0 REFUTED, 0 PARTIAL. Numeric spot-checks in `certify_chk.py` (same directory):
Abel identity residual 0.0 at four points including a canonical pin (sieve to 4e5);
I2 increment law and triangular telescope exact to 1.4e-14; classical Ramanujan
c_q(q) = phi(q) = 198 vs tau(q) = 2 at q = 199; sec.7 exponent arithmetic; I1
window-algebra solves. Coordinator integrates; nothing below was applied to any repo.

Sources are cited by file; upstream repo files are read-only for us — items touching
them go to the planned upstream correction memo (record 033), not to edits.

---

## E1 (fatal — finding 1 CONFIRMED): the packets assert a kernel chain from the Abel face to RH that does not exist

Independently verified: the kernel chain on upstream main is
`ProjectedRenewalQuadraticBoundedStatement <-> NonzeroResponseRHScale -> RH`
(`MobiusSynthesisBoundaryBridge.lean:842-884`, `TerminalMertensReduction.lean:56-77`),
and `NonzeroResponseRHScale` bounds H = Z[M] (`MobiusSynthesisBoundary.lean:46`).
`primeSievePNTError` occurs in exactly four modules on main, all pure-identity
(AbelIdentity, CollapseIdentity, PNTCentering, QuotientPNTError); no theorem takes a
bound on E or on the Abel-face S as a hypothesis toward H or RH. Since
`mertensSummatory x = C - 2E` identically (`PrimeSievePNTCentering.lean`,
`mertensSummatory_eq_pntCorrectedAllPlus_sub_two_error`), C = M + 2E, and an E-bound
alone constrains H not at all — exactly upstream's own closed lane
`pnt-reciprocal-coordinate-change` (kind: circular).

**results/026/packet.md (and results/017/packet.md, same wording), WRONG:**
> "A kernel-verified chain (Lean 4/mathlib, no unproved premises) establishes: if the
> target below holds, the Riemann Hypothesis holds."
> "## Target (two kernel-equivalent faces; attack either)"

**Replacement:**
> "A kernel-verified chain (Lean 4/mathlib, no unproved premises) establishes: if the
> **Quadratic face** below holds, the Riemann Hypothesis holds
> (ProjectedRenewalQuadraticBoundedStatement <-> NonzeroResponseRHScale -> RH).
> The **Abel face** is related to the Quadratic face only by exact identities
> (E = S − M(K)R(y); M = C − 2E with C = M + 2E identically); a bound on the Abel
> face S at canonical y ≍ √x does NOT currently imply the Quadratic face, the H-bound,
> or RH by any kernel theorem. The faces are kernel-DUAL objects, not kernel-equivalent
> targets. Exception (degenerate): an Abel bound UNIFORM in y contains K = 1, where
> S = R(x), and is von Koch RH directly — but that is not the canonical target and
> supplies no reduction."

**IDEAS.md line ~261 (node G), WRONG:**
> "the Abel-form bilinear statement Σ_{d≤√x} μ(d)(π(x/d)−Li(x/d)) ≪ x^{1/2+ε} —
> equivalent to the E-face target with no exponent flow"

**Replacement:**
> "the Abel-form bilinear statement Σ_{d≤√x} μ(d)(π(x/d)−Li(x/d)) ≪ x^{1/2+ε} —
> related to the E-face target by the exact identity E = S − M(K)R(y); estimate-
> equivalence at exponent 1/2 additionally requires |M(K)R(y)| ≪ x^{1/2+ε}, whose
> R(√x) half is prime-side RH at half scale and is supplied by no Mertens-side
> induction hypothesis (see erratum E2). Neither face is kernel-linked to H/RH."

**Governance consequence (coordinator):** rounds 2 and 3 blind panels (20 proposals)
and shortlist I1/I2 were seeded with the unsupported equivalence; any round-4 packet
must carry the corrected wording before seeding.

---

## E2 (major — finding 2 CONFIRMED): review 014's boundary-term "no loss" claim is wrong

The boundary M(K)R(y) needs two inputs. A Mertens induction hypothesis at half scale
gives M(K) ≪ x^{1/4+ε} but says nothing about R(y) = π(√x) − Li(√x); the bound
|R(t)| ≪ t^{1/2+ε} is prime-side RH (von Koch), not a consequence of any finite-range
Mertens statement — and review 014 itself states five paragraphs earlier that "the
σ-loop bootstraps the Mertens side only." Best unconditional prime input
(Vinogradov–Korobov, R(y) ≪ y^{1−o(1)} = x^{1/2−o(1)}) gives boundary
x^{1/4+ε} · x^{1/2−o(1)} = x^{3/4−o(1)}, far above x^{1/2+ε}. Same structure as
upstream's closed lane `divisor-band-harmonic-mobius` ("the boundary term literally
regenerates the original Mertens problem").

**results/014/review_full.md:182 region, WRONG:**
> "in these coordinates the boundary term is M(√x)·R(√x) ≪ x^{1/4+ε}·x^{1/4+ε} =
> x^{1/2+ε} under the induction hypothesis at half scale — exactly self-consistent at
> 1/2, with no exponent flow and no loss"

**Replacement:**
> "in these coordinates the boundary term is M(√x)·R(√x); the Mertens induction
> hypothesis at half scale bounds only the first factor (x^{1/4+ε}). The second factor
> R(√x) is prime-side: |R(t)| ≪ t^{1/2+ε} is RH-strength and is NOT supplied by the
> σ-loop, which bootstraps the Mertens side only. Unconditionally (Vinogradov–Korobov)
> the boundary is x^{3/4−o(1)}. The direction a proof needs — Abel-face bound ⟹
> E-bound — therefore carries exponent flow through the boundary unless prime-side
> input at half scale is separately proved; only the reverse direction (RH ⟹ both)
> is free."

**results/017/packet.md, WRONG (inherited):**
> "(The boundary term M(K)R(y) is separately self-consistent at 1/2.)"

**Replacement:** delete, or replace with:
> "(The boundary term M(K)R(y) is x^{3/4−o(1)} unconditionally; bounding it at
> x^{1/2+ε} requires prime-side input at half scale that no Mertens induction
> supplies.)"

**Governance consequence:** log as informal-math error #9.

---

## E3 (major — finding 3 CONFIRMED): "the d=1 term means |E| ≪ x^{1/2+ε} literally contains RH" is an invalid termwise inference

A bound on a signed sum does not bound an individual summand; the remaining d-fibres
can cancel the d=1 term (record 016 measured exactly such massive cross-fibre
cancellation: |S| ~ x^{1/2} against triangle ~ x^{3/4}). The statement is true only in
the degenerate one-term regime K = 1 (y ~ x), not at canonical y ≍ √x.

**results/014/review_full.md:97 (item 5), WRONG:**
> "Since E contains the d = 1 term M(1)Δ₁ = R(⌊x⌋) − R(t₂) with weight 1,
> |E| ≪ x^{1/2+ε} literally contains RH for π"

**Replacement:**
> "Any route that SEPARATES the d = 1 fibre and bounds it individually needs
> R(x) − R(x/2) ≪ x^{1/2+ε}, i.e. prime-side RH-strength input — so termwise/
> fibre-separating attacks on E are circular. The target |E| ≪ x^{1/2+ε} itself does
> not termwise contain RH at canonical y ≍ √x: bounds on the signed sum do not bound
> individual fibres, and cross-fibre cancellation is measured to be large (016)."

**results/026/packet.md obstacle 6, RESCOPE (same defect inherited):**
> "Circularity: R(t) ≪ t^{1/2+ε} for d=1 IS RH."

**Replacement:**
> "Circularity: any fibre-separating route that must individually bound the d=1 fibre
> needs R(t) ≪ t^{1/2+ε}, which IS RH — a warning against termwise routes, not a
> property of the signed target."

**Governance consequence:** log as informal-math error #10.

---

## E4 (major — finding 4 CONFIRMED): "our Abel face" and upstream's E^rec are duals, not the same estimate — three gaps are being collapsed into one

Verified: E(y,x) = S(y,x) − M(⌊x/(y+1)⌋)R(y) exactly (re-verified numerically here,
residual 0.0, four points + canonical pin). Upstream's E^rec is the CENTERED
three-point object Z[E] with Z = `primorialSquareZeroModeCenter` (value at X_n minus
value at L_k minus torus-ratio times endpoint increment), at the BLOCK cutoff
y = primorialPNTPrimeSieveCutoff k — not the per-x canonical y ≍ √x. Hence
Z[E] = Z[S] − Z[B] with B_y(t) = M(⌊t/(y+1)⌋)R(y); the boundary does NOT cancel under
Z (backward stability, records 023/024, makes the quotient constant only on the
length-y backward window at the pin, not at L_k or U_k). And even a full Z[E]-bound is
insufficient since H = Z[C] − 2Z[E] with Z[C] = H + 2Z[E].

**JOURNAL.md 2026-08-12-02 item (4) and any successor record, RESCOPE:** wherever
sec.7's E^rec measurements are read as directly about our Abel face family, insert:

> "Upstream's E^rec is the centered three-point object Z[E] at the block cutoff; our
> Abel face S is a single-x object at canonical y ≍ √x. They differ by (i) the exact
> boundary B_y(t) = M(⌊t/(y+1)⌋)R(y), which does not cancel under centering; (ii) the
> three-point centering itself; and (iii) the comb: H = Z[C] − 2Z[E], so no Z[E]-bound
> alone reaches H. Transfers of estimates or measurements between the two objects must
> pay all three gaps explicitly."

---

## E5 (major — finding 5 CONFIRMED): upstream sec.7's "full square-root cancellation, exactly sufficient" is contradicted by its own fitted exponents — do not import it as settled

Arithmetic on the document's own numbers: D = ⌊x/y⌋ ≍ x^{0.5}; full square-root
cancellation over the fibres would take the triangle exponent 0.678 to 0.428; the
signed fit is 0.51. Measured saving = x^{0.678−0.51} = x^{0.168} = D^{0.336} —
materially less than square root, and below the x^{0.178} ("about x^0.18") the same
paragraph states is required (x^{0.168} at 1e8 ≈ 22.1x, consistent with the reported
median 24.9x). The stated bar ("less than full square-root cancellation cannot close")
is not established by the cited finite-range regression.

**JOURNAL.md 2026-08-12-02 item (4), WRONG (imported over-read):**
> "i.e. the mechanism is full square-root cancellation ACROSS the d-family, with
> essentially no margin."

**Replacement:**
> "upstream reads this as full square-root cancellation across the d-family; on the
> same fitted exponents, however, the measured saving is x^{0.168} = D^{0.336},
> below both full square-root (D^{0.5}) and the required x^{0.178} — the mechanism
> claim is a finite-range regression over-read, and the 'square-root bar' should be
> treated as heuristic, not measured. Note our own 016 item 3 (M-weighted cancellation
> coefficient GROWING with K) points the same way. Open cheap resolution: recompute
> both normalizations (signed-vs-l1 and signed-vs-l2) on one grid with 016's arrays."

**Governance consequence:** include the exponent arithmetic in the record 033 upstream
correction memo.

---

## E6 (minor, load-bearing for transport — finding 6 CONFIRMED): the canonical-orientation-split lane's explicit-formula step is invalid as written

The lane's step "every term of modulus exactly R^{3/2}/|ρ(ρ+1)ζ′(ρ)|, so no
cancellation among zeros can push it below R^{3/2−o(1)}" lower-bounds a sum by the
moduli of its terms — logically invalid (oscillation among the R^{iγ} phases is not
excluded) — and the coefficients 1/ζ′(ρ) presuppose simple zeros. The closure
CONCLUSION stays safe on independent grounds (four decades of flat
|positiveSmooth|·log R/R^{3/2} numerics; a mean-square/Omega argument likely repairs
the step, and an Omega-result suffices against the required O-bound). But the lane's
"invariant that has predicted every closure" (no piece may be a monotone-weighted
Moebius sum) is NOT proved and must not be transported to kill other routes by analogy.

**JOURNAL.md 2026-08-12-02 item (3), RESCOPE:**
> "the canonical orientation split — the latter killed by an
> integral-of-M-against-dpi smoothing argument at X^{3/4+o(1)}"

**Replacement:**
> "the canonical orientation split — closed on strong numerics plus a conditional
> explicit-formula heuristic (the written pointwise lower-bound step is invalid as
> stated and assumes simple zeros; rescuable via mean-square/Omega). Its
> 'monotone-weighted Moebius sum' invariant is unproved and must not be applied to our
> routes by analogy."

**Governance consequence:** include the explicit-formula step in the record 033 memo.

---

## E7 (minor, LOAD-BEARING — finding 7 CONFIRMED; recommend severity upgrade to major): I2's rung-1 |A_q| target is equivalent to the target, not a reduction

Verified exactly (numeric residual 3.6e-15 at q = 199): with V_t = S(q−1, X−t),
A_q = q^{-1}Σ_{t<q}V_t, and c_q(n) = Σ_{d|n,d<q} μ(d)a(n/d), the telescope gives
V_0 − A_q = q^{-1}Σ_{s<q}(q−1−s)c_q(X−s), hence |S − A_q| ≤ Σ_s|c_q(X−s)| ≪_ε q^{1+ε}
unconditionally (measured 108.5 at q = 199 vs q^{1+ε} scale). Therefore
|A_q| ≪ q^{2−2δ} ⟺ |S| ≪ X^{1−δ+ε} and |A_q| ≪ q^{1+ε} ⟺ |S| ≪ X^{1/2+ε}: in
upstream's ledger taxonomy the rung-1 line is closure kind "circular". The AC step is
a pure triangle bound landing at exactly q^{1+ε} = x^{1/2+ε} with zero margin and
captures no cancellation. Mitigation stands (027 labels I2 "ADVANCE, PARTIAL ONLY"),
but the rung-1 line must carry the label.

**IDEAS.md node I, WRONG-BY-OMISSION:**
> "Rung-1: |A_q| ≪ q^{2−2δ}."

**Replacement:**
> "Rung-1: |A_q| ≪ q^{2−2δ} — EQUIVALENT-TO-TARGET, not a reduction:
> |V_0 − A_q| ≤ Σ_{s<q}|c_q(X−s)| ≪_ε q^{1+ε} unconditionally, so any A_q bound at
> exponent ≥ 1+ε is exactly the corresponding S bound (ledger kind: circular). The AC
> estimate is a triangle bound with zero margin. I2's only genuine content is the DC
> contraction, which remains exactly the missing signed input."

**results/027/027.md:61, same correction** to "rung-1 shape: |A_q| ≪ q^{2−2δ} ⟹
|S| ≪ x^{1−δ+ε}": append "(and conversely; the implication is an equivalence, so this
is a restatement of rung 1, not a route to it)".

---

## E8 (minor, load-bearing for record 030 — finding 8 CONFIRMED): I1's rung-1 exponent x^{5/6+ε} is stale; the program's own kernel package gives x^{3/4+ε}

Verified algebra: with the superseded pointwise Lipschitz constant C ≈ 2√x/log x, the
window W ≈ H log x/(4√x) and E₂(Y) ≪ Y^{4+ε} = x^{2+ε} give H³ ≪ x^{5/2+ε}, i.e.
H ≪ x^{5/6+ε} — the recorded number. With record 023's kernel-proved affine modulus
(slope 2+o(1), intercept √x/log x) the excursion window at canonical pins reaches
W = min(Y, ~H/4); for H ≫ Y this caps at Y, so Y·(H/2)² ≪ Y^{4+ε} gives
H ≪ Y^{3/2+ε} = x^{3/4+ε} (general k: H ≪ Y^{1+(1+ε)/(2k)}). The recorded 5/6 is
valid but weaker by x^{1/12} than the program's own formalized package supports.

**IDEAS.md node I, STALE:**
> "Rung-1: E₂(Y) ≪ Y^{4+ε} ⟹ |S| ≪ x^{5/6+ε}."

**Replacement:**
> "Rung-1: E₂(Y) ≪ Y^{4+ε} ⟹ |S| ≪ x^{3/4+ε} at canonical pins (via the
> kernel-proved affine modulus, record 023; general k: |S| ≪ Y^{1+(1+ε)/(2k)}). The
> earlier x^{5/6+ε} used the superseded pointwise Lipschitz constant C ≈ 2√x/log x."

**Same correction** in results/027/027.md:58 and results/027/mapping_report.md:180;
and results/026/packet.md's "named central object" paragraph should state the affine
window (W up to y+1 ≍ √x at pins), not W = min(y+1, ⌊H/2C⌋) with pointwise C.
Do NOT formalize the amplification lemma (record 030) against the stale window.

---

## E9 (minor — finding 9 CONFIRMED): I2's c_q must not be called a Ramanujan sum

c_q(n) = Σ_{d|n, d<q} μ(d)a(n/d), a(m) = R(m) − R(m−1), is a truncated divisor
convolution against the prime-error increment. The classical Ramanujan sum satisfies
c_q(q) = φ(q) (verified: 198 vs τ = 2 at q = 199), which would destroy the
|c_q(n)| ≪ τ(n) bound the AC estimate rests on. The τ-bound itself is sound in I2's
range: X − t ≥ q(q−1) and d < q force every argument (X−t)/d ≥ q, so the Li-increment
singularity never enters. The labeling ambiguity is already flagged open at
AGENTS.md:47-53 ("Not a Ramanujan sum" remark) and IDEAS.md:99; it remains unresolved.

**Correction (any I2 write-up, and the record 031 declaration):** state explicitly:
> "c_q here is a truncated divisor convolution, NOT the classical Ramanujan sum
> (classical c_q(q) = φ(q) violates the τ-bound); the AGENTS.md 'Ramanujan-sum
> labelling' flag remains open and must be resolved against the synthesis source
> before any cross-citation."

---

## Summary of governance actions proposed (coordinator's call)

1. Correct 026/017 packet target wording (E1) before round-4 seeding.
2. Log informal-math errors #9 (E2) and #10 (E3).
3. Re-derive and re-record I1 rung-1 at x^{3/4+ε} (E8); hold record 030 until done.
4. Label I2's A_q rung-1 line "circular / equivalent-to-target" (E7); recommend
   severity upgrade of finding 7 from minor to major.
5. Record 033 upstream memo: sec.7 exponent arithmetic (E5) and orientation-split
   explicit-formula step (E6). Upstream maintainer's name must not appear.
6. Rescope journal 2026-08-12-02 readings of E^rec measurements (E4, E5, E6).
