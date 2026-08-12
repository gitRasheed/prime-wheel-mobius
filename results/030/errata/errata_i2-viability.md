# Errata draft — target: i2-viability (record 029 certification, record 030)

Certifier: independent re-derivation + numeric spot-checks
(`i2_check.py` in this scratchpad; q = 100..1600, X = q²−1 ≤ 2.56e6,
python3.12/numpy, exact-identity residuals ≤ 2e-14).

Source files affected: `results/027/mapping_report.md`,
`results/027/027.md`, `IDEAS.md` §I. The blind-panel proposals
(`results/026/proposals/agent5.json`, `agent1.json`) are immutable
panel submissions; corrections to their content are recorded here as
annotations to be carried by 027/IDEAS and by any future record-031
declaration, not as edits to the proposal files.

Verdicts on the 13 findings: 9 CONFIRMED, 4 PARTIAL, 0 REFUTED.
Numeric anchors: increment identity and trace identity hold to 1e-14
on 0 ≤ t ≤ q−2; |V₀−A_q| measured O(10) (far below q);
Σ_t|c_q(X−t)| ≈ 0.5·q (slope ≈ 0.94); window τ-sum ≈ 2.2·q·log q;
sign-blind prime-power mass ≈ 2.8·q^{3/2}/log q; termwise
Σ_{d<q}|R(X/d)| local slope 0.68–0.71 vs X (matches upstream's 0.678,
below the RH-asymptotic 3/4 envelope); Abel-face truncation
K = ⌊(X−t)/q⌋ equals q−1 for all 0 ≤ t ≤ q−1 and drops to q−2 at
t = q, with the dropped term μ(q−1)R(q−1).

---

## E1. Circularity of the DC/AC "reduction" (finding 1, fatal — CONFIRMED)

The chain |c_q(n)| ≤ τ(n) on the legal range (n ≥ q²−q+1, d ≤ q−1
forces m = n/d ≥ q+1, where |a(m)| < 1), plus
Σ_{n∈(X−q,X]} τ(n) ≪ q log q (hyperbola count; measured ≈ 2.2·q·log q),
plus the exact trace identity
V₀ − A_q = q⁻¹·Σ_{s=0}^{q−2} (q−1−s)·c_q(X−s) (verified to 1e-14),
gives |V₀ − A_q| ≪ q log q UNCONDITIONALLY. Hence for every exponent
α > 1 — every rung-1 exponent 2−2δ with δ < 1/2 AND the full target
1+ε — the statements |A_q| ≪ q^α and |V₀| ≪ q^α are equivalent. A_q is
not an easier object than V₀; the isolation is a coordinate change
(upstream lane class `pnt-reciprocal-coordinate-change`; route doc §3:
"merely rewriting `H` is not quantitative progress").

**`results/027/mapping_report.md`, §2 "P — principal-mode isolation",
item 9 — wrong sentence:**

> 9. Renewal edge: PARTIAL. The DC/AC isolation is new and valid; the
> proposed DC contraction remains exactly the missing signed input.

**Replacement:**

> 9. Renewal edge: FAIL as a reduction, valid as a transfer identity.
> The DC/AC isolation is an unconditional EQUIVALENCE: |V₀ − A_q| ≪
> q log q (trace identity + window divisor count), so |A_q| ≪ q^α ⟺
> |V₀| ≪ q^α at every exponent α > 1, i.e. at every rung and at the
> target. This is a coordinate change in upstream's dead-lane sense,
> not a reduction; its value is a pin-to-window-mean transfer
> certificate. The proposed DC contraction remains exactly the
> missing signed input.

**`results/027/mapping_report.md`, §4.2 rung-1 deliverable — wrong
sentence:**

> For any fixed `δ>0`,
> `|A_q| ≪ q^{2−2δ}`
> together with the elementary AC estimate gives
> `|S(q−1,q²−1)| ≪ x^{1−δ+ε}`
> for `δ<1/2`.

**Replacement:**

> For any fixed `δ<1/2`, `|A_q| ≪ q^{2−2δ}` and
> `|S(q−1,q²−1)| ≪ x^{1−δ+ε}` are EQUIVALENT (unconditional transfer
> `|V₀−A_q| ≪ q log q`); the "rung-1 deliverable" is therefore the
> pinned rung-1 target itself in window-mean coordinates, not a
> ladder rung, and cluster Z's record-022 parking (no known route to
> any fixed δ > 0 short of a fixed-width zero-free strip, itself
> open) applies to it verbatim.

**`results/027/027.md`, shortlist paragraph — wrong phrase:**

> rung-1 shape: |A_q| ≪ q^{2−2δ} ⟹ |S| ≪ x^{1−δ+ε}.

**Replacement:**

> rung-1 shape: |A_q| ≪ q^{2−2δ} ⟺ |S| ≪ x^{1−δ+ε} (equivalence, not
> reduction — see record 030 erratum E1).

**`IDEAS.md` §I, I2 entry — wrong phrase:**

> Rung-1: |A_q| ≪ q^{2−2δ}.

**Replacement:**

> Rung-1: |A_q| ≪ q^{2−2δ} — CIRCULAR as a reduction (unconditionally
> ⟺ the pinned target |S| ≪ x^{1−δ+ε}, since |V₀−A_q| ≪ q log q);
> retained only as a transfer identity / Lean closure certificate.

---

## E2. μ*Λ recombination unavailable at the truncation; contraction is record 025's parked reopening condition (finding 2, fatal — CONFIRMED)

Two defects in agent5's mechanism sentence "combine the complete and
complementary hyperbolas before estimating. The complete convolution
μ*Λ=−μ log then leaves one signed boundary-renewal operator with
coefficients μ(a)log a":

(a) μ*Λ = −μ·log (verified: n=p and n=p² check out) is a COMPLETE
divisor-convolution identity. The object in play carries a hard
cutoff d < q ≈ √X. Completing it generates the complementary block
Σ_{m ≲ √x} Λ(m)·(M(⌊x/m⌋) − M(q−1)) — unestimated Mertens
cancellation of the same difficulty class. The claimed "new leverage"
(recombining μ*Λ algebraically before norming) is not available at
the truncation actually in play; the proposal nowhere performs or
prices the completion step.

(b) The proposed sufficient lemma ("uniform norm gap ρ(T_q|Aff⊥) ≤
1−η for the exact signed μ(a)log a boundary-renewal operator") is
record 025's recorded reopening condition ("a signed contraction for
(k−1)μ(a)log a — new Möbius-correlation input") assumed rather than
derived. Note: 027/IDEAS already decline to record the contraction as
leverage; the NEW content of this finding is (a), the truncation
obstruction.

**Correction to carry in 027/IDEAS/031 (annotation of
`agent5.json`, mechanism and new_leverage fields):** any future I2
text must state that the μ*Λ = −μ log recombination requires
completing the divisor sum past d = q, that the complementary block
is Σ_{m≲√x} Λ(m)(M(⌊x/m⌋) − M(q−1)) (open Mertens cancellation), and
that the proposed operator lemma is the record-025 reopening
condition, not new leverage.

---

## E3. Spectral gap does not bound A_q as claimed (finding 3, fatal — CONFIRMED)

Three independent gaps in "The proposed attack is to prove a uniform
spectral contraction for this operator after removing its two affine
modes. Iterating that contraction across square scales bounds A_q":
(i) a spectral-radius gap for a non-normal, q-dependent operator
family controls neither operator norms nor transient powers without
a uniform-in-q resolvent/norm bound (stronger, unstated); (ii) no
scale recurrence is defined — no inhomogeneous renewal equation, no
control of forcing that replenishes the removed affine modes; (iii)
the affine (constant) modes are projected OUT of the operator, yet
the quantity to be bounded, A_q, is the constant mode — no
reconstruction identity is supplied. **Correction to carry:** the
contraction step is not merely "unproved"; as stated it does not even
have the shape of an argument that outputs a bound on A_q.

---

## E4. Rung-1 milestone non-diagnostic for δ ≤ 1/4 (finding 4, major — PARTIAL)

CONFIRMED half: under RH the fully sign-blind termwise bound gives
Σ_{d<q}|R(X/d)| ≪ x^{1/2}·log x·Σ_{d<q}d^{−1/2} ≪ x^{3/4}·log x, so
any |S| ≪ x^{1−δ} with δ ≤ 1/4 is deliverable in principle with the
cross-d signed mechanism fully discarded; the mechanism-diagnostic
threshold is δ > 1/4. The measured 0.678 termwise exponent is
finite-range (obstacle 7; our local slopes 0.68–0.71 at x ≤ 2.6e6,
drifting logarithmically); the RH-asymptotic envelope is 3/4 and any
diagnostic gate must use it.

OVERBROAD half (correcting the finding): NO I2 source (agent5.json,
agent1.json, mapping_report.md, 027.md, IDEAS.md §I) leans on 0.678
to define a proof gate. The 0.678 figure enters the program state
only through the journal's upstream-convergence note, as upstream's
measurement. The erratum is prophylactic:

**Addition to `IDEAS.md` §I (I2 entry) and any 031 declaration:**

> Diagnostic note: sign-blind termwise summation delivers x^{3/4+o(1)}
> under RH, so a rung-1 exponent 1−δ certifies the signed cross-d
> mechanism only for δ > 1/4; the measured termwise exponent 0.678 is
> finite-range and must not define a gate.

---

## E5. Rung-1 milestone simultaneously out of reach; "restates the parked rung" (finding 5, major — PARTIAL)

CONFIRMED half: a fixed zero-free strip Re(s) > 1−η gives rung 1 with
δ ≈ η/2 (termwise: Σ_{d<q}(x/d)^{1−η+ε} ≪ x^{1−η/2+ε}); no fixed-width
strip is known for any η > 0; the converse (rung 1 ⟹ strip) is NOT
established because the truncation at K ≈ √x breaks the μ*Λ route
(E2(a)); and by E1 the milestone IS record 022's parked cluster-Z
rung-1 in window-mean coordinates, so 022's parking applies verbatim.

WRONG-AS-STATED half (correcting the finding): "I2 restates the same
rung without noting that its own proposed route is the parked missing
input" — the note IS present: IDEAS §I says "DC contraction NOT
recorded as leverage (it is the known missing input)" and
mapping_report §5 says "Do not record the signed renewal contraction
as leverage; it remains the known missing input." What is genuinely
missing is the equivalence-to-target flag, covered by E1. No text
change beyond E1's, plus one addition to the §4.2 rank reason:

**`results/027/mapping_report.md` §4.2 — wrong sentence:**

> Reason for rank: highest probability partial, but lower frontier
> value because record 023/024 already established much of the
> canonical backward-window increment geometry.

**Replacement:**

> Reason for rank: highest probability partial, but frontier value is
> formalization-only: the rung-1 line is target-equivalent (E1), has
> no known route short of a fixed-width zero-free strip (open for
> every width), and record 023's affine modulus already gives the
> window-mean transfer at a better constant (E6).

---

## E6. "DC/AC isolation is new" — false; record 023 already gives it with a better constant (finding 6, major — CONFIRMED)

023's unconditional affine modulus |S_y(x±t) − S_y(x)| ≤ A_y·t + B_y,
A_y = 2+o(1), B_y = K/log(y+1) ≈ q/log q = o(q), averaged over the
backward window (exactly stable at the pin, so no support-growth
terms), gives |V₀ − A_q| ≤ A_y(q−1)/2 + B_y = (1+o(1))·q — strictly
stronger than the τ-route's q log q. The τ(n) bound discards the
1/log(n/d) factor carried by ℓ(m) = Li(m)−Li(m−1), which is what
makes the amortized slope O(1) rather than O(log q). Genuine residual
value is formalization-only: the kernel (record 024) carries only the
crude per-step constant C ≈ 2√x/log x, so the amortized O(q) window
bound is not machine-checked. Text fix is included in E1's
replacement of §2.P item 9 ("new and valid" → "valid as a transfer
identity... not new"); additionally:

**`results/027/mapping_report.md` §1 P cluster — wrong sentence:**

> The AC reduction is genuine and bounded-effort.

**Replacement:**

> The AC reduction is genuine and bounded-effort, but not new: record
> 023's affine modulus already yields the window-averaged bound
> |V₀ − A_q| ≤ (1+o(1))·q, a log factor stronger than the τ-route;
> the residual value is kernel formalization of the amortized
> constant.

---

## E7. Λ/log replacement: prime-power terms are not bookkeeping (finding 7, major — CONFIRMED)

1_P(n) = Λ(n)/log n − Σ_{k≥2} (1/k)·1_{n=p^k}. Aggregated sign-blind
over d < q with the ramp weight, the prime-power terms total
≍ q^{3/2}/log q (measured: 2.79 ± 0.02 × q^{3/2}/log q at
q = 100..1600) — a half power ABOVE the stated target estimate
|A_q| ≪ q^{1+ε}. Reaching q^{1+ε} for this block requires
Mertens-type cancellation in Σ_{d<q} μ(d)·Li((X/d)^{1/2}) (reduces by
partial summation to Mertens sums; RH-strength for a full power
saving to q^{1+ε}), which the proposal never performs; Abel boundary
terms are likewise unaccounted. Scope note: for the rung-1 budget
q^{2−2δ} with δ < 1/4 the block fits sign-blind; it is fatal for the
q^{1+ε} target as stated. **Correction to carry:** any 031 text must
either restrict claims to δ < 1/4 or add an explicit prime-power and
Abel-boundary ledger with its own Mertens input priced.

---

## E8. "Endpoint-correct triangular formula" drops a Mertens boundary term (finding 8, major — CONFIRMED, normalization refined)

Base-at-1 telescoping is illegitimate: analytically R(1) = π(1)−Li(1)
diverges (+∞) in BOTH the li-normalization and the repo's actual
`logarithmicIntegralFromTwo` normalization (∫₂¹ dt/log t diverges
through the t=1 singularity; in Lean the non-integrable interval
integral takes the junk value 0, which must not be relied on). The
correct base-at-2 formula carries the boundary term R(2)·M(q−1) —
and in the repo normalization Li(2) = 0, so R(2) = π(2) = 1 and the
term is EXACTLY M(q−1): a bare Mertens value at scale q inside the
"principal mode" formula. It is harmless in size (unconditionally
o(q), under RH ≪ q^{1/2+ε} — within every stated budget) but the
formula is wrong without it. The ramp weight w_q(r) = 1 for
r ≤ X−q+1, (X−r+1)/q for X−q+2 ≤ r ≤ X, 0 beyond, is otherwise exact.

**`results/027/mapping_report.md` §4.2 deliverable — wrong phrase:**

> Derive the endpoint-correct triangular formula for `A_q`.

**Replacement:**

> Derive the base-at-2 triangular formula for `A_q`, INCLUDING the
> boundary term R(2)·M(q−1) (= M(q−1) exactly in the repo's
> logarithmicIntegralFromTwo normalization, where R(2) = 1) and an
> explicit small-argument convention for a(m) (base-at-1 telescoping
> is illegitimate: Li(1) diverges; Lean's junk value 0 for the
> non-integrable integral must not be load-bearing).

Same fix applies to the phrase "triangular A_q formula" in `IDEAS.md`
§I and "endpoint-correct triangular formula for A_q" in
`results/027/027.md`.

---

## E9. "Ramanujan sums" label (finding 9, major — PARTIAL)

CONFIRMED half (mathematics): c_q(n) = Σ_{d|n, d<q} μ(d)·a(n/d) is
NOT a Ramanujan sum — it is non-periodic in n mod q, non-integral
(a carries Li increments), and depends on q through a cutoff, not
through gcd(n,q). Importing any classical c_q fact (multiplicativity
in q, |c_q(n)| ≤ gcd(n,q), Hölder's formula, orthogonality,
Ramanujan–Fourier expansion) would be an outright error; e.g. the
classical c_q(q) = φ(q) would violate the τ-bound the AC estimate
rests on.

REFUTED half (provenance): no committed program-state file describes
I2 this way. Grep over IDEAS.md, JOURNAL.md, PROOF_OS.md,
results/026/026.md, results/026/packet.md, results/027/* finds no
"Ramanujan" attached to I2; the phrase existed only in the audit
orchestrator's own session summary (quoted into the review prompt as
"a downstream program summary"). The repo's only Ramanujan labels
concern upstream's synthesis target (AGENTS.md/JOURNAL), where the
c_q genuinely are classical Ramanujan sums and the labelling tension
is already flagged (IDEAS.md line 99). **Erratum is prophylactic
only:** add one naming sentence to any 031 declaration —

> Naming: the increment kernel c_q(n) of I2 is a truncated Möbius
> convolution against prime-discrepancy increments, NOT a Ramanujan
> sum; no classical c_q identity may be imported. Rename to e.g.
> `w_q(n)` in Lean to avoid collision with upstream's genuine
> Ramanujan-sum modules.

---

## E10. AC-RMS non-sequitur in the rung-1 derivation (finding 10, minor — CONFIRMED; LOAD-BEARING)

Flagged as load-bearing: agent5's rung1_version sentence "the AC
estimate is O(q^{1+ε}) in root-mean-square and is therefore
negligible. This gives S(y,X) ≪ X^{1−δ}" is wrong as written — RMS
control alone loses √q at the single pin t = 0 (only q^{3/2+ε}). The
same-quality repair is the trace identity
V₀ − A_q = q⁻¹Σ_{j=0}^{q−2}(q−1−j)·c_q(X−j) (verified numerically to
1e-14) with the ℓ¹ bound Σ_{n∈(X−q,X]} τ(n) ≪ q log q (measured
≈ 2.2·q log q). This repair is exactly what makes E1's circularity
airtight, so it must be stated wherever the rung-1 line is corrected
(E1 text already uses it).

---

## E11. Increment-identity range (finding 11, minor — CONFIRMED)

The identity V_t − V_{t+1} = c_q(X−t) is exact for 0 ≤ t ≤ q−2
(verified to 1e-14). At t = q−1 it invokes V_q = S(y, X−q), where the
Abel-face truncation K = ⌊(X−q)/q⌋ drops from q−1 to q−2 (verified
numerically for q = 100..1600), producing the extra boundary term
μ(q−1)·R(q−1). The increment index set is X−q+2 ≤ n ≤ X. Any Lean
statement (031) must carry the range 0 ≤ t ≤ q−2 and, if V_q is
mentioned, the explicit boundary term. Correct the quantifier in any
quotation of agent5's "for 0≤t<q ... Then V_t−V_{t+1}=c_q(X−t)".

---

## E12. "|a(m)| is uniformly bounded" (finding 12, minor — CONFIRMED, normalization scoped)

False globally: a(2) = R(2)−R(1) is analytically divergent under BOTH
the li- and the repo's from-two normalization (Li(1) = ∫₂¹dt/log t
diverges; Lean assigns the junk value 0, making a(2) convention-
dependent). Saved on the legal range only because n ≥ q²−q+1 and
d ≤ q−1 force m = n/d ≥ q+1 ≥ 3, where |a(m)| < 1 with sharp
supremum 1 (approached at large primes: a(p) = 1 − (Li(p)−Li(p−1)) →
1). Any 031 statement must carry the m ≥ 3 (in practice m ≥ q+1)
restriction and a fixed small-argument convention before c_q(n) is
well defined. (Folded into E8's replacement text.)

---

## E13. Iteration bookkeeping cannot produce a power saving (finding 13, major — CONFIRMED)

To convert a fixed contraction factor (1−η) into a power saving
q^{−γ} one needs ≍ log q geometric steps. The only recursion the
square-pin geometry naturally offers is q → √q, giving O(log log q)
steps and hence merely (1−η)^{O(log log q)} = (log q)^{−γ'} — a
log-power, not a fixed power. No scale recurrence is defined anywhere
in the proposal, so "Iterating that contraction across square scales
bounds A_q" has unspecified and, on the natural reading, insufficient
exponent bookkeeping. Fold into E3's correction: the contraction
step, even if granted, does not reach any rung-1 exponent as
structured.

---

## Disposition note for the coordinator

The certified picture matches the audit notes' recommended
disposition: I2 survives only as a small corrected formalization
package — increment identity on 0 ≤ t ≤ q−2, finite Poincaré, trace
identity + ℓ¹ window divisor bound (unconditional |V₀−A_q| ≪ q log q,
or O(q) via 023's amortized constant, the one item with real kernel
value), and the base-at-2 ramp formula WITH the M(q−1) term — framed
as a pin ⟺ window-mean transfer/closure certificate, never as a
reduction. The rung-1 line must be struck or re-labelled
target-equivalent everywhere it appears (IDEAS §I, 027.md,
mapping_report §4.2).
