# Errata draft — target 022-rung0-parking (certification of results/029 audit findings)

Certifier: independent re-derivation of every finding, with numeric spot-checks in
`check_022.py` (same directory). Source files: results/022/022.md, results/022/proof_attempt.md,
results/022/review_refute.md, results/021/021.md, results/021/codex_report.md (line 105).

Status of the rung-0 mathematics: the bound 𝓜 ≪ x^{1/4} + √x(log x)²e^{−h(x)} itself is NOT
challenged by any finding here and survived my re-check of (1.1), (2.2), (2.3), (3.8), (4.1)–(4.7).
Every erratum below concerns the coordinator's parking note (022.md, Results, "Coordinator's
note" paragraph), the rung-1 definition, and the mapping/exhaustion language.

---

## E1 — Majorization claim mis-scoped (audit finding 1, major: CONFIRMED)

**Wrong text (022.md, coordinator's note):**
> "Rung 1 (fixed power saving) via ANY absolute-value route is quasi-RH-hard: the d-sum route
> majorizes |R(x)| (d=1 term), and R(x) ≪ x^{1−δ} is classically equivalent (Ingham) to a
> zero-free strip β ≤ 1−δ — open."

**Why wrong:** the gate object 𝓜 takes absolute values over ZEROS while keeping the signed
Möbius sum inside each G_{x,K}(ρ) = Σ_{d≤K}μ(d)Li_*((x/d)^ρ). |G(ρ)| does not bound its own
d=1 summand |Li_*(x^ρ)|, so 𝓜 does not majorize |R(x)|. The majorization is true only of
(i) the different object Σ_{d≤K}|R(x/d)|, and (ii) 022's actual proof method, which applies the
triangle inequality over d at (2.2)/(3.8)/(4.5): the d=1 slice of that (ρ,d) double-triangle
majorant satisfies Σ_ρ|Li_*(x^ρ)| ≥ (|R(x)| − |C_0(x)|)/2 via the explicit formula, so the
strip-hardness argument does bite there. As written, "ANY absolute-value route" kills 𝓜-type
routes (μ(d) signed inside the amplitude) that have not been argued against.

**Replacement text:**
> "Rung 1 via the triangle-over-d method — any route that majorizes S by Σ_{d≤K}|R(x/d)|, or
> applies the (ρ,d) double triangle as at (2.2)/(3.8)/(4.5) — is strip-hard: the d=1 slice
> majorizes (|R(x)|−|C_0(x)|)/2, and a fixed power saving R(x) ≪ x^{1−δ} forces a zero-free
> strip β ≤ 1−δ (Landau/Mellin correspondence; the direction used here is clean, the converse
> carries ε/log losses). This says nothing about routes that keep μ(d) signed inside the
> amplitude: the gate object 𝓜 itself does not majorize |R(x)|, and the hardness of
> 𝓜 ≪ x^{1/2−δ} is open."

(The "(Ingham)" attribution and exact-δ equivalence phrasing are also corrected here —
audit minor finding, confirmed.)

## E2 — Signed/absolute dichotomy unsupported (audit finding 2, major: PARTIAL)

**Wrong text (022.md, coordinator's note):**
> "Only signed routes (μ×R correlation, Cell D) remain above rung 0."

**Why wrong:** the sentence implies signed routes escape a barrier that kills absolute routes.
No such asymmetry has been established. The audit finding is right about that, and right that
no exponent-preserving S→M (or S→R) bridge away from 1/2+ε is on record — the Abel identity's
boundary term M(K)R(y) (records 014/015) is only controlled under half-scale RH-strength
hypotheses, and the K-truncated Möbius convolution does not invert cleanly. However, the
finding's own flat assertion "rung 1 is zero-free-strip-hard in every coordinate system" is
conditional on exactly that missing bridge: without it, S(x,K) ≪ x^{1−δ} is not known to imply
a fixed-power Mertens bound, so coordinate-independent strip-hardness is itself a conjecture.
Correct scoping: hardness of rung 1 is OPEN in both coordinates.

**Replacement text:**
> "Above rung 0, both signed and absolute coordinates remain open. Any rung-1 route that also
> carries an exponent-preserving bridge to R or M would force a zero-free strip, so a coordinate
> change does not by itself evade that barrier — but no exponent-preserving S→M bridge is on
> record away from 1/2+ε (the Abel boundary term M(K)R(y), 014/015, is only balanced under
> half-scale RH-strength hypotheses), so rung-1 hardness is unverified in both coordinates.
> Signed routes (μ×R correlation, Cell D) are preferred on measurement evidence, not on a
> proven escape from the barrier."

## E3 — Rung-1 definition drift between 021 and 022 (audit finding 3, major: CONFIRMED)

**Conflicting texts:**
- 021.md (Results): "Rung 0 = unconditional 𝓜(x,K,T) = o(√x) (gives S = o(x), PNT-strength);
  𝓜 ≪ x^{1/4−δ} would be rung 1." (Same in 021/codex_report.md line 105: S ≪ x^{3/4−δ}.)
- 022.md (Target): "Stretch (rung 1): any x^{1/2−δ} bound on 𝓜, giving S ≪ x^{1−δ}."

**Why it matters:** the two targets have different binding constraints. 𝓜 ≪ x^{1/4−δ} (021)
forces x^{−1/2}|C_{x,K}| ≪ x^{1/4−δ}, i.e. |C_{x,K}| ≪ x^{3/4−δ} — beating the triangle bound
(3.8) by a power requires power-saving Möbius cancellation in Σ_{d≤K}μ(d)C_0(x/d) ≈
−(2√x/log x)·F^log_{K,x}(1/2), i.e. cancellation at s = 1/2, the exact m=2 obstruction 021
itself identified. The parking note's |R(x)| argument does not address that constraint at all.
𝓜 ≪ x^{1/2−δ} (022) is the weaker target for which the C-part is already fine at x^{1/4}.

**Replacement text (022.md Target, and echoed in the note):**
> "Stretch: rung 1a (this record's target) = any x^{1/2−δ} bound on 𝓜, giving S ≪ x^{1−δ};
> rung 1b (021's frozen sense) = 𝓜 ≪ x^{1/4−δ}, giving S ≪ x^{3/4−δ}, whose binding
> constraint is power-saving Möbius cancellation at s = 1/2 in the C-part (021's m=2
> obstruction), not the zero sum. The two were silently conflated between 021 and 022."

Recommend the coordinator log this as informal-math error #9 (recorded-definition drift).

## E4 — "Fully mapped" / "exhaustion" overclaim (audit finding 4, major: CONFIRMED)

**Wrong text (022.md, coordinator's note):**
> "cluster Z is now fully mapped." ... "Pivot to H1 justified by exhaustion."

**Why wrong:** one majorant was executed (triangle over (ρ,d), uniform top-of-range VK, RvM
total counting), improving 022's own honest trivial scale (2.5) by only e^{h(x)} — subpower —
against a rung-2 gate sitting ≈ √x/polylog below trivial. The rung-1 leg of the "map" rests on
the mis-scoped note (E1–E3). Genuinely untouched in 022: Möbius cancellation inside G_{x,K}(ρ),
discrete moments of the retained log-kernel form at zeros (021), low-vs-high zero-range
splitting, cancellation in C_{x,K}, x-uniform contradiction structure.

**Replacement text:**
> "Cluster Z is mapped at one majorant (triangle over (ρ,d) + uniform VK + RvM counting);
> that method is now killed at rung 2 (see the x^{3/4} ceiling below). Signed-cancellation
> directions inside G_{x,K}(ρ) and C_{x,K} are unexplored. Cluster Z PARKS on resource and
> priority grounds, not exhaustion; pivot to H1 is a prioritization decision."

## E5 — Correct method-level kill and reopening condition (audit finding 5, major: PARTIAL)

**Wrong/incomplete text (022.md, coordinator's note):**
> "Cluster Z PARKS at rung 0; reopens on a signed mechanism or a zero-free-strip advance."
(plus the recorded rationale corrected in E1)

**What the audit gets right (record this):** even assuming RH, R(t) ≪ √t log t gives
Σ_{d≤K}|R(x/d)| ≪ √x log x · Σ_{d≤K}d^{−1/2} ≤ 2√κ₊ · x^{3/4} log x — the triangle-over-d
method has a hard ≍x^{3/4} ceiling (already visible in (3.8)) and can NEVER reach the rung-2
x^{1/2+ε}/polylog gate under any zero-free-region advance whatsoever. This is the correct,
stronger, method-level kill and it is not in the record; §7's "subpower by construction" point
is the correct reason rung 1 was missed by THIS proof.

**Where the audit overreaches (do not record its last clause as stated):** "reopens on a
zero-free-strip advance is therefore also wrong" is overbroad. A strip β ≤ 1−δ gives
R(t) ≪ t^{1−δ}log²t, hence Σ_{d≤K}|R(x/d)| ≪ x^{1−δ/2}log²x and 𝓜 ≪ x^{1/2−δ/2}log x —
rung 1a falls to the same d-triangle method; via M(K) ≪ K^{1−δ+ε} and partial summation the
C-part improves too, so rung 1b also falls. So the strip trigger is a correct reopening
condition for RUNG-1 progress; it is wrong only as a route to the rung-2 gate.

**Replacement text:**
> "Method-level kill (stronger than the strip argument): under RH the d-triangle majorant is
> ≪ 2√κ₊ x^{3/4}log x, and its main part is genuinely of size ≍ x^{3/4}/log x, so no
> zero-free-region advance of any strength lifts the triangle-over-d method to the rung-2
> x^{1/2+ε} gate. Cluster Z PARKS at rung 0. Reopening triggers: (i) a zero-free-strip advance
> reopens RUNG 1 only (both senses 1a/1b, via the same d-triangle method); (ii) the rung-2 gate
> reopens only on a signed mechanism (Möbius cancellation kept inside G_{x,K}(ρ)/C_{x,K})."

---

## Minor findings — certification summary (no errata text mandated beyond the above)

- "𝓜 = o(√x) presentational trap": PARTIAL. The normalization arithmetic is correct
  (𝓜 = o(√x) ⟺ unnormalized o(x), PNT-strength; RH gate is 𝓜 ≪ (log x)^A), but 022.md
  already labels the deliverable "PNT-strength" twice, so "trap" overstates; a one-line
  clarification next to the boxed bound suffices.
- Ingham attribution / exact-δ equivalence: CONFIRMED; folded into E1's replacement.
- Non-effectivity: CONFIRMED. (log x)²e^{−h(x)} < 1 first holds near log x ≈ 4.58×10^{14}
  (numerically verified), i.e. no recordable range; worth one flag sentence in 022.md Results.
- Moment route quantitatively dominated by pointwise VK (exp saving (log x)^{1/3} vs
  (log x)^{3/5}, because every zero pays at T ≍ x² instead of an optimized truncation):
  CONFIRMED; add one clause to the novelty-audit sentence.
- Step-6 common-height truncation lemma still unsupplied: CONFIRMED and load-bearing for any
  future citation of "S = o(x) via the moment route" — the record flags it honestly, severity
  minor stands, but the S-deduction must not be cited as proved-in-record until the lemma is
  inserted. The audit correctly voids the integrality objection (⌊x/d⌋ = ⌊⌊x⌋/d⌋ for integer
  d, so integer x suffices for the S-target).
