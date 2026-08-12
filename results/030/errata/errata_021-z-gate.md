# Errata draft — target 021-z-gate (certification of results/029 audit findings)

Sources corrected: `results/021/021.md`, `results/021/codex_report.md`, `IDEAS.md`
(H3 gate-correction block, lines ~281-296). Corroborating record: `results/022/022.md`.
All ten audit findings for this target were independently re-derived; all ten are
CONFIRMED (two with scoping notes recorded inline below). Verdicts and re-derivations
are summarized per item; the coordinator should apply the replacement text verbatim
or equivalent.

---

## E1 — Frozen gate is not a self-contained sufficient condition (finding 1, major, CONFIRMED; folds in finding 10, minor, CONFIRMED and load-bearing)

**Re-derivation.** The chain identity is
S(x,K) = −2Re Σ_{0<γ≤T} G_{x,K}(ρ) + C_{x,K} + E_T(x,K), with S − S₀ = O(K) + O(K/log x).
The boxed gate bounds only x^{−1/2}|C_{x,K}| + 2x^{−1/2}Σ|G|; sufficiency for
|S| ≪ √x·polylog additionally requires E_T(x,K) ≪ √x (log x)^{O(1)} at one common
height T serving all d ≤ K. The codex_report's own inference table tags exactly this
row NONTRIVIAL-BUT-KNOWN ("It is not supplied by record 018") and then the frozen
artifact drops it; record 022 subsequently refused to accept it unsupplied ("Step 6
asserts an unsupplied common-height truncation lemma (one T₀ serving all d ≤ K)",
022.md lines 87-88). The lemma is plausibly provable at T ≍ x² (per-d smooth error
≪ (x/d)log²x/T summing to ≪ x log³x/T ≪ √x; jump terms are each ≤ log x, totaling
≤ K log x ≍ √x log x), but provable-in-principle is not frozen-in-the-ledger.

Finding 10 (quantifier): the boxed left side has nonnegative zero summands and
C_{x,K} is T-independent, so it is nondecreasing in T; "∀T ∈ [x²,2x²]" is equivalent
to evaluating at T = 2x² and is a gratuitous strengthening. Sufficiency needs one
good height, i.e. ∃T, paired with the truncation clause at that same T. T ≍ x² is
safe but not necessary (T ≍ x already puts the smooth truncation error inside the
√x·polylog budget).

**021.md, lines 88-90 — replace**

> ∃A,C,x₀ ∀x≥x₀ ∀K∈[κ₋√x,κ₊√x] ∀T∈[x²,2x²]:
> x^{−1/2}|C_{x,K}| + 2x^{−1/2}·Σ_{0<Im ρ≤T, all zeros, w/ mult.}
> |Σ_{d≤K} μ(d)·Li_*((x/d)^ρ)| ≤ C(log x)^A.

**with**

> ∃A,C,x₀ ∀x≥x₀ ∀K∈[κ₋√x,κ₊√x] ∃T∈[x²,2x²]:
> x^{−1/2}|C_{x,K}| + 2x^{−1/2}·Σ_{0<Im ρ≤T, all zeros, w/ mult.}
> |Σ_{d≤K} μ(d)·Li_*((x/d)^ρ)| ≤ C(log x)^A,
> AND, at the same T, the truncation remainder in
> S(x,K) = −2Re Σ_{0<γ≤T} G_{x,K}(ρ) + C_{x,K} + E_T(x,K)
> satisfies E_T(x,K) ≪ √x (log x)^{O(1)} uniformly over d ≤ K.
> The truncation clause is an unconditional side lemma (standard explicit-formula
> machinery; not supplied by 018 or 021; record 022 hit this wall). Without it the
> boxed inequality alone does NOT imply the Abel target. Note the original ∀T
> quantifier was equivalent to T = 2x² by monotonicity; ∃T is what sufficiency uses.

**IDEAS.md, lines 289-294 (the frozen-gate sentence): apply the same ∀T→∃T change and append the truncation side clause verbatim.** The ledger currently records a gate with no side condition at all.

**codex_report.md Q1 table, "Assume the repaired exact-zero-plus-secondary gate in Q2. | STANDARD" — annotate:** STANDARD only jointly with the NONTRIVIAL-BUT-KNOWN truncation row above it; the frozen artifact must carry both.

---

## E2 — "explicitly RH-strength" mislabels the gate's strength class (finding 2, major, CONFIRMED)

**Re-derivation.** Only gate ⟹ target is claimed (and even that needs E1's clause,
plus the Abel⟹RH bridge separately under audit in 029). RH ⟹ gate is not known in
either clause. (i) C-clause: needs |Σ_{d≤K} μ(d)d^{−1/2}/log(x/d)| ≪ polylog; partial
summation from the best RH-conditional Mertens bounds (M(u) ≪ √u·exp((log u)^{1/2}
(loglog u)^{O(1)}), Soundararajan-type) gives only exp(c(log K)^{1/2}(loglog K)^{O(1)})
= K^{o(1)}, which exceeds every fixed power of log (checked numerically: exp(√ℓ)
overtakes ℓ^10 near ℓ = 10⁴). The log-kernel weight w(d) = 1/(1−log d/log x) has
w ≤ 2 and total variation 1 on [1,K], so it does not change this. (ii) Zero clause:
F_K(ρ) ≈ log K/ζ′(ρ) (Perron double pole at w=0 for simple ρ), so the clause is a
negative-moment demand ≈ Σ_{γ≤T} 1/(γ|ζ′(ρ)|); polylog follows from RH + simple
zeros + J₋₁(T) ≪ T (open, Gonek-conjecture strength; dyadic Cauchy–Schwarz gives
≪ (log T)^{3/2}), and unconditional or RH-only full-family negative-moment upper
bounds do not exist (current results excise exceptional subfamilies). Consequence:
the gate can fail (sufficiently severe small-|ζ′(ρ)| / Lehmer-pair behaviour) while
RH and the Abel target both hold. Program usage treats "RH-strength" as a
strength-class label (022: "Rung 2 gate = RH-strength (021). Rung 0 = known-strength"),
so the frozen label misplaces the gate.

**021.md, lines 100-101 — replace**

> cluster Z survives only as Z-repaired; explicitly RH-strength, open, broader than a J₋₁ moment.

**with**

> cluster Z survives only as Z-repaired; the gate (jointly with its truncation side
> clause) implies the Abel target and is therefore at-or-above RH strength via the
> program's bridge; it is NOT known to follow from RH — the C-clause exceeds the best
> RH-conditional Mertens bounds (K^{o(1)} superpolylog), and the zero clause is an
> open negative-moment demand (J₋₁-type) even under RH + simple zeros. The gate can
> FAIL while RH and the Abel target hold: sufficient-only, possibly strictly stronger
> than the target. Open, broader than a J₋₁ moment.

---

## E3 — C₀ label is wrong: it contains a second family of zero sums, unpriced (finding 3, major, CONFIRMED; finding 6, minor, CONFIRMED feeds the same block)

**Re-derivation.** Expanding π₀(t) = Σ_m (μ(m)/m)J₀(t^{1/m}) against the defining
identity π₀(t) − Li(t) = −2Re Σ_{γ>0} Li_*(t^ρ) + C₀(t) forces
C₀(t) = a(t) + Σ_{m≥2}(μ(m)/m)[Li(t^{1/m}) − Σ_ρ Li_*(t^{ρ/m}) + a(t^{1/m})],
i.e. C₀ carries nontrivial-zero harmonics t^{ρ/m} (including off-line zeros) at
amplitude t^{β/m}/(|ρ|log t). "Prime-power+archimedean" is an origin label, not a
contents description, and contradicts the report's own table row ("Higher m
contribute F_K(1/m) and zero harmonics F_K(ρ/m)"). Pricing (verified numerically):
the m=2 zero harmonics bounded termwise in d cost
x^{1/4}·Σ_{d≤K}d^{−1/4}·polylog ≍ x^{1/4}·(4/3)K^{3/4} ≍ x^{5/8}·polylog,
exceeding the √x·polylog budget by x^{1/8} (ratio confirmed = x^{1/8} at
x = 10^{12}, 10^{18}, 10^{24}). Any termwise-in-d proof of the C-clause therefore
needs power-saving cancellation in Σ_{d≤K}μ(d)d^{−1/4−iγ/2}, uniformly in γ — an
independent Möbius demand at Re s = 1/4, same species as the Abel face. Scoping
note: the record was silent on (rather than explicitly dismissing) the higher-m
harmonics; the defect is the frozen label plus the unpriced cost.

Finding 6 (necessity language): the m=2 block of C_{x,K} collapses to
−(1/2)Σ_{d≤K}μ(d)J₀(√(x/d)), inside which the F_K(1/2) main part and the zero
harmonics can in principle cancel; what is desk-exact is that no termwise proof
exists, not that every proof of the C-clause must bound F_K(1/2). The substantive
obstacle (aggregate μ-cancellation at half scale) stands.

**021.md, lines 84-86 — replace**

> with C₀(t) the exact prime-power+archimedean term of the repo-normalized explicit formula

**with**

> with C₀(t) the exact remainder of the repo-normalized explicit formula (prime-power
> and archimedean terms PLUS the m ≥ 2 zero harmonics Σ_{m≥2}(μ(m)/m)Σ_ρ Li_*(t^{ρ/m}),
> off-line zeros included; termwise in d the m=2 harmonics alone cost x^{5/8}·polylog,
> so the C-clause hides a second Möbius-cancellation demand at Re s = 1/4)

**021.md, lines 74-76 — replace**

> the moment at nontrivial zeros carries no information about F_K(1/2), and bounding it already demands RH-scale Möbius cancellation at s = 1/2.

**with**

> the moment at nontrivial zeros carries no information about F_K(1/2); no termwise
> proof of the C-clause can avoid RH-scale Möbius cancellation at s = 1/2 (aggregate
> cancellation inside −(1/2)Σ_d μ(d)J₀(√(x/d)) is not excluded, but the aggregate is
> itself a μ×prime-count correlation at half scale).

**codex_report.md Q2 ("Let C₀(t) be the exact prime-power plus archimedean term"): same relabel as above.**

---

## E4 — "A < 2 untenable" is a false constraint on the frozen gate; correct forced bound is A ≥ 1 (finding 4, major, CONFIRMED)

**Re-derivation.** The log K·log T lower scale is a Landau–Gonek desk check for the
unnormalized F_K-proxy Σ_γ|F_K(ρ)|/|ρ| (codex_report Q5 kept this scoping: "an
F_K-proxy with polylog exponent A<2 is untenable"). The frozen gate's summand
carries the extra Li_* kernel 1/log(x/d) ≍ 1/L: on-line, |G(ρ)| = x^{1/2}|F̃(ρ)/(ρL)
+ h.o.t.| with F̃(ρ) = Σ_d μ(d)d^{−ρ}w(d), and the absolute values legitimately strip
the x^{iγ} phase, so dyadic-block Landau–Gonek (X = 1/d, main term −(V/2π)Λ(d)/d per
coefficient, per-d error O(log(dT)·loglog d) summing to O(√x·L·loglog) ≪ block main
term for V ≥ x^{1/2+ε}) forces per block ≈ (1/4π)Σ_{p≤K}(log p)w(p)/p ~ (L log 2)/4π
(numerically verified: weighted sum/L·ln2 = 0.89, 0.93, 0.94 at L = 20, 30, 34,
constant O(1) offset; vs unweighted ~ L/2). Roughly L usable dyadic blocks give a
forced signed block ≍ L², and the 1/L kernel normalization divides it down to ≍ L:
Landau–Gonek forces A ≥ 1 for the frozen gate, not A ≥ 2. Cross-check: the RMT
prediction J₋₁/₂(T) ≍ T(log T)^{1/4} gives expected frozen-gate size
Σ 1/(γ|ζ′|) ≍ (log x)^{5/4} — consistent with A ≥ 1, inconsistent with a forced
A ≥ 2. (Caveat, same rigor class as the original claim: both the A ≥ 2 proxy bound
and the A ≥ 1 frozen bound are Landau-main-term desk checks; off-line zeros enter
the block evaluation only through the unconditional all-zero Landau formula.)

**021.md, lines 96-97 — replace**

> secondary desk check: signed scale ≍ log K·log T, so polylog power A < 2 is untenable.

**with**

> secondary desk check (F_K-proxy only): the unnormalized proxy Σ|F_K(ρ)|/|ρ| has
> Landau–Gonek signed scale ≍ log K·log T, so A < 2 is untenable FOR THE PROXY; the
> frozen gate's Li_* kernel divides the forced block by log x, so for the frozen
> gate the same check forces only A ≥ 1 (RMT expectation: (log x)^{5/4}).

**IDEAS.md, lines 291-292 — replace**

> Constraints: A < 2 untenable (Landau–Gonek signed scale log K·log T);

**with**

> Constraints: A ≥ 1 forced for the frozen gate (Landau–Gonek; the earlier "A < 2
> untenable" applied only to the unnormalized F_K-proxy — the Li_* kernel costs a
> log); RMT expectation A = 5/4;

---

## E5 — Rung 0's advertised payoff is already unconditionally known (finding 5, major, CONFIRMED)

**Re-derivation.** With R(t) ≪ t·exp(−c(log t)^{3/5}(loglog t)^{−1/5}) (Vinogradov–
Korobov) and x/d ≥ x/K ≍ √x for d ≤ K, the triangle inequality alone gives
|S(x,K)| ≤ Σ_{d≤K}|R(⌊x/d⌋)| ≪ x log x·exp(−c′(log x)^{3/5}(loglog x)^{−1/5}) = o(x).
So proving 𝓜 = o(√x) yields no new bound on S; the ladder as frozen advertises
strength it does not have. Record 022 confirmed the propagation ("Novelty audit:
S = o(x) is already KNOWN via pointwise VK PNT + triangle inequality", error #7)
and re-graded rung 0 "known-strength"; the mis-set rung originated in 021.

**021.md, lines 97-98 — replace**

> Rung 0 = unconditional 𝓜(x,K,T) = o(√x) (gives S = o(x), PNT-strength); 𝓜 ≪ x^{1/4−δ} would be rung 1.

**with**

> Rung 0 = unconditional 𝓜(x,K,T) = o(√x); its consequence S = o(x) is ALREADY
> KNOWN elementarily (pointwise VK PNT + triangle inequality — see 022, error #7),
> so rung 0's value, if any, is the moment bound on 𝓜 itself, not any new bound on
> S; 𝓜 ≪ x^{1/4−δ} would be rung 1 (gives S ≪ x^{3/4−δ} only for 0 < δ < 1/4 —
> at δ ≥ 1/4 the √x·polylog truncation error and O(K) floor terms dominate).

**IDEAS.md, line 294 ("Rung 0 = 𝓜 = o(√x) unconditional (PNT-strength); 𝓜 ≪ x^{1/4−δ} = rung 1"): apply the same replacement.**

**codex_report.md Q5 ("is a genuine PNT-strength entrant") — annotate:** the S = o(x)
consequence is elementary and unconditional already; only the 𝓜-bound itself would be new.

---

## E6 — m=2 "≈" display is an envelope, not an asymptotic (finding 7, minor, CONFIRMED)

**Re-derivation.** Li(√(x/d)) = 2√(x/d)/log(x/d) + O(√(x/d)/log²(x/d)); summed over
d ≤ K the one-term error is ≍ (√x/L²)·K^{1/2} ≍ x^{3/4}/log²x, which exceeds the
signed main term once Möbius cancellation is present (√x·polylog ≪ x^{3/4}/log²x).
So the displayed relation cannot be used to read off the true size of the C-clause.

**021.md, lines 72-74 — after** "−(1/2)Σ_{d≤K}μ(d)Li(√(x/d)) ≈ −√x·F^log_{K,x}(1/2)/log x" **append:**

> (envelope identification only: the termwise expansion error is O(x^{3/4}/log²x),
> above the signed main term whenever Möbius cancellation is present; the display
> locates the F_K(1/2) demand, it does not size the aggregate)

---

## E7 — "Also FALSE en route" over-grades a repairable step (finding 8, minor, CONFIRMED)

**Re-derivation.** With w(u) = 1/(1−log u/L) on [1,K], K ≤ √x: w ≤ 2 and total
variation = 1, so Abel summation gives |Σ_{d≤K}μ(d)d^{−ρ}w(d)| ≤ 3·sup_{K′≤K}|F_{K′}(ρ)|.
A gate quantified uniformly over partial cutoffs K′ ≤ K controls the log-weighted
amplitude entirely; the codex_report itself listed "uniformly controlled partial
polynomials" as sufficient. The replacement of Li_* by x^ρF_K(ρ)/(ρ log x) is
literally false as an identity but is a uniformity strengthening away from valid,
not an independent structural collapse on par with the off-line-zero and
C-remainder failures.

**021.md, lines 78-80 — replace**

> Also FALSE en route: replacing the log-weighted amplitude Li_*((x/d)^ρ) by x^ρF_K(ρ)/(ρ log x) (the d-dependent log kernel must be retained).

**with**

> Also incorrect en route (repairable): replacing Li_*((x/d)^ρ) by x^ρF_K(ρ)/(ρ log x)
> — the d-dependent log kernel matters, but Abel summation (w ≤ 2, TV = 1 for K ≤ √x)
> bounds the weighted sum by 3·sup_{K′≤K}|F_{K′}(ρ)|, so uniformity over partial
> cutoffs repairs it; unlike the two structural failures above, this is a
> strengthening-of-quantifier issue, not a collapse.

---

## Certification summary

| # | Finding | Severity | Verdict |
|---|---------|----------|---------|
| 1 | Gate not self-contained (missing truncation clause) | major | CONFIRMED |
| 2 | "RH-strength" strength-class mislabel | major | CONFIRMED |
| 3 | C₀ mislabel / unpriced m≥2 zero harmonics (x^{5/8}) | major | CONFIRMED |
| 4 | A < 2 constraint false for frozen gate (A ≥ 1 correct) | major | CONFIRMED |
| 5 | Rung 0 payoff already known (VK elementary) | major | CONFIRMED |
| 6 | F_K(1/2) necessity overstated (termwise-only) | minor | CONFIRMED |
| 7 | m=2 "≈" is envelope, not asymptotic | minor | CONFIRMED |
| 8 | "FALSE en route" grading too high (Abel-repairable) | minor | CONFIRMED |
| 9 | Rung-1 conclusion valid only for 0 < δ < 1/4 | minor | CONFIRMED |
| 10 | ∀T gratuitous; ∃T is the correct quantifier | minor | CONFIRMED — load-bearing, folded into E1 |

Findings 9 and 10 are integrated into E5 and E1 respectively rather than given
standalone blocks. If the coordinator adopts the audit's suggested ledger action,
items E1-E4 correspond to candidate informal-math errors #9-#12 (truncation
omission; C₀ mislabel/under-pricing; strength mislabel; A ≥ 2 propagation), with
the rung-0 defect already counted as #7 at record 022 (E5 marks 021 as its origin).
