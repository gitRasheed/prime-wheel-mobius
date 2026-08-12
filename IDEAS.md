# IDEAS.md — the attack-angle tree

Governed by `PROOF_OS.md` (surfaces section). The only file where
speculation is allowed; every claim here about what a technique *can do* is
UNVERIFIED unless it cites a record or a source document. Seeded 2026-08-08
from the two papers' own stated programs (nodes A–C, E) plus
clearly-marked speculative literature analogues (F). Rewritten 2026-08-12
after the round-4 audit and certification (029/030: 75 confirmed /
11 partial / 0 refuted; probes at scale in 032); the former erratum
banner is absorbed into the body, corrections cited inline.

Targets, verbatim sources in `AGENTS.md`:
- **HN**: prime-wheel harmonic nonconcentration (paper eq:HN; Lean
  `PrimorialWheelDirichletNonconcentration`).
- **SPS**: square-block survivor power saving (`conj:survivor-power-saving`
  for `Z_Λ(t) = −Σ_c μ(c)·K_{Λ,t}(c)`).
- **SYN**: forthcoming synthesis target (collaborator-stated; exact form
  pending repo).

## Program target (re-frozen 2026-08-12, records 029/030 — binding)

Committed: none. Supersedes every earlier "reduction" statement here
and in the sealed packets of rounds 2–3.

**What the kernel actually proves.** (1) The exact, hypothesis-free
Abel identity `E = S − M(K)·R(y)`
(`primeSievePNTError_eq_moebiusDiscrepancySum_sub_abelBoundary`): E
the prime-sieve PNT error, S the Abel face Σ_{d≤K} μ(d)·R(⌊x/d⌋),
K = ⌊x/(y+1)⌋. (2) The kernel RH-chain
`ProjectedRenewalQuadraticBounded ↔ NonzeroResponseRHScale → RH`, on
the centered wheel object H = Z[M] (= Z[C] − 2Z[E]); forward Mertens
criterion criterion-free (known-unknown 7). (3) There is **NO kernel
arrow from the Abel face S to RH** (029 finding 1, certified 030):
the Abel-face and bridge modules are disjoint; no theorem takes an S-
or E-bound as hypothesis toward H or RH. The former "two
kernel-equivalent faces; attack either" language was FALSE — the
faces are kernel-DUAL, related by exact identities only (the sole
exception, an Abel bound UNIFORM in y, contains K = 1 = von Koch RH:
no reduction). The coordinate ring is circular: T = M + E and
C = M + 2E identically, so {|C|,|E|} ⟺ {|M|,|E|} (030; upstream's
closed lane `pnt-reciprocal-coordinate-change`).

**The honest target is TWO obligations** (or re-target to E):
|S| ≪ x^{1/2+ε} AND |M(K)·R(y)| ≪ x^{1/2+ε} at the same (y,x). At
y ≍ √x the best unconditional bound on the boundary product is
x^{1−o(1)}; its R(√x) half is prime-side RH at half scale, supplied
by no Mertens-side induction (030 — review 014's "self-consistent at
1/2, no loss" claim retracted).

**Connecting lemmas MISSING (none exists, formally or informally):**
1. **Pin-to-block bridge.** Collapse/centering identities require
   x < y² (`hroot`); the backward excursion lives at the canonical
   pin x₀ = (y+1)²−1 with window [y²+y, y²+2y], entirely ≥ y² — the
   domains are disjoint for every y, and at the block cutoff the
   whole window lies above the primorial block. Composing needs an
   extension of the collapse identities to x = y²+O(y) or a boundary
   transport lemma, plus one y-convention (free y ≍ √x vs
   block-constant y_k = √U_k+1; factor ≤ √(log x) apart) (029/030).
2. **Control of the boundary obligation M(K)·R(y)** — no kernel
   theorem addresses it at all.
3. **S-vs-E centering mismatch.** Upstream's E^rec is the centered
   three-point Z[E] at the block cutoff; S is single-x at canonical
   y ≍ √x. Three gaps: the boundary B_y(t) does not cancel under
   centering; the centering itself; the comb H = Z[C] − 2Z[E].
   Transfers between the objects must pay all three (029/030).

Frontier delta of the correction: program-level (largest of the
project). The exact identities, pin geometry, excursion machinery and
kill tests survive; the reduction narrative did not (029).

## Strength ladder (law 10)

| Rung | Statement | Status |
|---|---|---|
| 0 (trivial entrant) | sublinear maximal control of the block residual ⟺ PNT, in-coordinates | open — see node E |
| 1 | any fixed exponent θ<1 for the block residual | open |
| 2 (target) | 1/2+ε — HN / SPS / SYN | open |
| above target | sharp O(√x) | not a goal |

Ladder note (029/030): in the Abel-gate coordinates of 021/022 the
rung-0 consequence S = o(x) is ALREADY KNOWN elementarily (VK +
triangle; 022 error #7) — rung 0's value there is the 𝓜 moment bound
itself. 021 and 022 silently used two different rung-1 senses: 1b
(021) 𝓜 ≪ x^{1/4−δ} ⟹ S ≪ x^{3/4−δ} (0 < δ < 1/4; binding constraint
= Möbius cancellation at s = 1/2 in the C-part); 1a (022)
𝓜 ≪ x^{1/2−δ} ⟹ S ≪ x^{1−δ}. Drift fixed: name the sense (030).

## A. Direct pinned-harmonic-nonconcentration program (HN)

- Status: unexplored · Analogue: structured/multidimensional large-sieve
  analysis (paper's own framing, citing Montgomery–Vaughan) · Committed: none
- New leverage: this is the source paper's *own* five-component sufficient
  program (§"What a proof of nonconcentration must control") — the only
  attack plan a source document endorses in writing.
- Declared obstacles: pinned-vs-averaged; regime gap (both in `AGENTS.md`).
- Cheapest kill test (per sub-node): exact finite computation of the named
  quantity at small k — each component is a statement about explicit finite
  objects `b_k(r)`, `D_N`, conductor bands.
- Sub-nodes (paper's enumeration, one experiment each when opened):
  - **A1 joint conductor energy** — bound `E_k[D,2D)` preserving the
    raw-minus-smooth cancellation. Status: unexplored.
  - **A2 near-resonance counting** — weighted joint energy in arcs of
    width 1/N, per conductor band. Status: unexplored.
  - **A3 phase nonalignment** — pinned phases cannot stay coherent across
    enough resonant modes to beat √-scale. Status: unexplored.
  - **A4 signed cross-band control** — retain the cross terms of the band
    Gram expansion; no positive-energy replacement without proved
    orthogonalization. Status: unexplored.
  - **A5 maximalization** — dyadic N + Rademacher–Menshov-type square
    function to control all prefixes; log losses absorbable into W_k^ε.
    Status: unexplored.

## B. Survivor-operator bilinear program (SPS)

- Status: unexplored · Analogue: bilinear forms / large-sieve duality
  (square-block paper's own discussion) · Committed: none
- New leverage: the square-block paper reduces its whole difficulty to the
  off-diagonal bilinear term and *names the missing ingredient*: a
  controlled map from pairs (c,c′) to a shared modulus/conductor with
  sub-square multiplicity, enabling Cauchy–Schwarz against a summable
  spectral weight.
- Declared obstacles: large-sieve non-transfer (the two named gaps);
  parity-type (position must be stated).
- Cheapest kill test: construct the candidate (c,c′)→conductor map on
  finite data (paper's exact-integer setup reaches X ≈ 1.6×10⁷) and
  measure its multiplicity empirically before proving anything.
- Sub-nodes:
  - **B1 conductor-pairing map** — build the missing off-diagonal map.
    Status: unexplored.
  - **B2 pinned large-sieve variant** — a large-sieve inequality valid at
    one synchronized scale without shift-averaging. Status: speculative
    (no known instance cited yet; analogue-unverified).
  - **B3 death-window leverage** — reuse the proved bounded-width divisor
    window structure to constrain the survivor kernel's support. Status:
    speculative (own idea, not paper-endorsed).

## C. Averaged-to-pinned transfer (HN)

- Status: unexplored · Analogue: exceptional-set arguments in analytic
  number theory · Committed: none
- New leverage: the paper itself lists exactly three routes past the
  averaged-translation identity: (i) uniform-in-L estimates, (ii)
  characterize exceptional starts and exclude `L = W_{k-1}`, (iii) direct
  arithmetic cancellation at the primorial phase. Each is a distinct
  sub-node; (ii) is the only one where "almost-all" technology (see F1)
  could re-enter legitimately.
- Declared obstacles: pinned-vs-averaged is the node's *subject*, not an
  objection to it; an attack must still say which of (i)–(iii) it runs.
- Cheapest kill test for (ii): numerically compare the pinned start's
  partial-sum growth against the translation-averaged distribution at
  reachable k — is `W_{k-1}` empirically typical or extreme?

## D. Synthesis coordinates (SYN)

- Status: **blocked** (repo not yet published) · Committed: none
- New leverage: unifies both coordinate systems; the collaborator states
  bounding effort will focus here.
- First actions when unblocked: extract the exact statement into
  `AGENTS.md` (resolving the Ramanujan-sum labelling flagged there); state
  it in Lean; then run the known-unknown numerics below *before* seeding
  attack sub-nodes.
- Cheapest kill test: exact computation of the signed sum at x ≤ 10⁶ —
  does the claimed O(√x) scale hold empirically, and does C(q) decay?

## E. PNT-rung calibration (ladder rung 0)

- Status: unexplored · Analogue: classical PNT-strength elementary/analytic
  estimates · Committed: none
- New leverage: the prime-wheel paper's closing sentence calls recovering
  an unconditional PNT-strength estimate inside these coordinates "a
  separate and worthwhile calibration problem". It is the program's
  trivial entrant: it exercises every piece of machinery end-to-end at
  `o(x)` strength, and any general-purpose angle (A, B, C, F) that cannot
  close *this* rung fails its own viability control (PROOF_OS, first
  contact).
- Cheapest kill test: none needed to open; each attack angle inherits this
  rung as its control. Caveat (030): in the Abel coordinates S = o(x)
  is already elementary — a rung-0 claim there must deliver more.

## F. Speculative literature analogues

Marked per PROOF_OS: `speculative` status, honesty about unverified
mappings. None is paper-endorsed; each earns an experiment only by first
writing the exact statement it would prove.

- **F1 Matomäki–Radziwiłł short-interval machinery** — Status: speculative.
  Analogue: multiplicative functions in almost-all short intervals (cited
  by the paper as context). Declared obstacle: the paper states it does
  *not* directly give the pinned uniform maximal estimate — legitimate
  entry point is C(ii) (exceptional-set route) only. Cheapest kill test:
  write down what "almost all" would leave unproven; if the exceptional
  set cannot even in principle be shown to avoid `W_{k-1}`, close as
  class with that reason.
- **F2 Vaughan/Vinogradov-type bilinear decomposition of μ** — Status:
  speculative, analogue-unverified: whether type-I/type-II ranges mesh
  with the primorial-block truncation is unchecked. Cheapest kill test:
  attempt the decomposition of one block residual on paper; see where the
  pinned start breaks the standard ranges.
- **F3 Pretentious / Halász-theory route** — Status: speculative,
  analogue-unverified. Halász-type bounds govern mean values of
  multiplicative functions; whether a pretentious-distance argument sees
  the block-local (not global-mean) residual is unestablished. Cheapest
  kill test: state the block residual as a mean value twisted by the
  block indicator; check whether the indicator destroys multiplicativity
  beyond repair.
- **F4 Special-vector spectral analysis of the Gram form** — Status:
  speculative. Analogue: quadratic forms / spectral theory. Declared
  obstacle (paper, §"Special-vector rather than operator-norm control"):
  a uniform operator-norm bound is provably the wrong target — an
  adversarial coefficient vector can align with the Dirichlet kernel; any
  attack here must exploit the explicit arithmetic vector `F̂_k`. Cheapest
  kill test: compute the Gram form's Rayleigh quotient at the actual
  vector vs the operator norm at small k; if they track, the special
  structure is not being used and the node is idle.
- **F5 Entropy / dynamical methods (logarithmic averaging, entropy
  decrement)** — Status: speculative, analogue-unverified: these methods
  produce logarithmically-averaged or density-type results, typically far
  from √x-scale bounds. Cheapest kill test: literature check (one
  afternoon) for any instance of a power-saving bound produced this way;
  none found ⇒ close as class for the RH-strength target (may stay open
  for rung 0).

## Known unknowns (reviewed at every closure)

1. **Has eq:HN's left side ever been computed?** — **ANSWERED**
   (`results/002/`, 2026-08-09). Computed and plotted for k=2..8 via the
   kernel-proved identity (exact), spectral side verified at k=2,3.
   Pinned ratio 0.43–0.89, flat; nothing anomalous. Feasibility settled:
   dense spectrum k≤3 only, 𝒬₄ ≈ 9×10⁸ structured-only, k≥5 never —
   large-k numerical access is identity-side only, and attack-angle
   gates must not assume otherwise.
2. **Conductor decay after smooth-core subtraction.** Raw-spectrum
   conductor decay is proved; the *joint* (raw − 2·smooth) coefficient
   decay profile is, empirically, unplotted. Partial first look at k=3
   (`results/002/conductor_energy_k3.csv`): ℓ² mass concentrates in
   conductors 6 and 30 (~half the energy), ℓ¹ mass anti-concentrates at
   the full conductor — toy scale only. Open at k=4 via the structured
   route (CRT tensor × 44 smooth sites).
3. **Synthesis constants.** Does C(q) decay? Is Σ|C(q)| finite over the
   relevant range? What does the signed sum look like at x = 10⁶?
   Unanswerable until the synthesis repo lands (node D).
4. **D_y(x) in the gap.** README reports max|D_y|/main-term ≈ 1.001–1.008
   at x = 10⁶ for y = 2..17. Behaviour for log x < y < √x at larger x is
   unmeasured.
5. **Survivor empirical exponent.** The square-block paper reports a
   near-flat local slope as a diagnostic only (with the explicit
   Mertens-conjecture deception warning). Range extension and slope
   stability across more dyadic scales: unmeasured.
6. **Square-block kernel reproducibility.** — **CLOSED** (record 003,
   2026-08-09): the republished export ships build scaffolding; green
   `lake build RHLean --wfail` + clean audit on the EC2 evaluator.
7. **The classical bridge.** — **HALF-ANSWERED** by the synthesis repo
   (record 003 extraction, 2026-08-09): the forward direction
   `MertensEnergyBoundedStatement → RH` is proved in-repo
   (`riemannHypothesis_of_mertensEnergy`,
   `mobius-synthesis/RHLean/Analysis/MertensEnergyRHForward.lean:66`,
   Mellin + completed-zeta reflection, mathlib-only ingredients) — and
   forward is the direction a proof of the open estimate needs. The
   reverse (RH → Mertens) remains a typed premise
   (`ClassicalMertensRHCriterion`) used only by the iff-form theorems.
   Kernel audit of the forward pair pending (003); axiom-guarding of the
   forward arrows recommended upstream (030).
8. **Parity-obstruction position.** No source document states whether
   parity-type barriers bind these coordinates. A literature diagnostic
   should establish the program's official position (feeds B, F2).

## G. Synthesis-target angles (blind panel round 005, 2026-08-09)

Seeded from 10 blind proposals (`results/005/proposals/*.json`, mapping
report in `results/005/005.md` verdict). All UNVERIFIED informal
content. Canonical target: `ProjectedRenewalQuadraticBoundedStatement`
(AGENTS.md). Convergence signals (journaled): 5/10 independently built
quadratic-phase dispersion from X_n = n(n+2); 0/10 took node A (the
prime-wheel paper's own endorsed program) — a signal about A's pull.

Clusters (shared load-bearing assumption = cluster kill condition):
- **Q — quadratic-phase Gauss/Weyl dispersion** (agents 0,1,5,7,8):
  square sampling manufactures the off-diagonal→shared-modulus map
  with sub-square multiplicity (obstacle 2's missing ingredient).
  Dies if mass concentrates beyond the √q-gain threshold.
- **S — per-frequency survival of C−2E cancellation** (0,7): dies if
  Parseval spreads the correlation across packets (triangle failure
  in a prettier basis).
- **L — ℓ² repair of strong induction** (1,5,6,9): dies if the signed
  off-diagonal covariance of reciprocal intervals resonates with M —
  note the 004 finding (corr(C,E) up to 0.94) is weak evidence AGAINST
  this cluster's assumption; test before spending.
- **I — exact-identity relocation** (2,3,6): cancellation is algebraic
  not statistical; cheapest to settle (exact identity checks).
- **R — contraction/renewal induction** (4,7,6,5): ρ<1/6 upgrades to
  energy contraction; dies if losses compound multiplicatively.

Shortlist (mapping rank): **G1** = agent7 coconductor-gauss-dispersion
-renewal (constructs obstacle 2's map unconditionally; weakest link:
per-packet cancellation survival). **G2** = agent1 quadratic-sample-
reciprocal-dispersion (QSCL classical + QSRD with honest D^{3/2} loss;
weakest: neutral H=1 bootstrap). **G3** = agent5 telescoped BTD (only
well-founded block induction; fixed point 3/4+ε; weakest: pinned
spectral-set circularity). **G4** = agent3 wheel-mollified-Perron
(strongest rung-0 deliverable; terminal object concedes RH-hardness
relocation). Near-miss to absorb as facts: agent9's audit (wheel
projection = exact major-arc deletion; Montgomery–Soundararajan
diagonal lands at rung 2 with zero slack).

**Kill-test inventory** (dedup, mapping Part 4): shared 10⁹ segmented-
sieve framework serves tests 2–6; highest information-per-hour: test 4
(μ×err sign correlation, hours), test 7 (exact identity checks —
settles cluster I), test 1 (per-frequency cancellation — settles S).
Full week of compute if run entirely; run 4/7/1 first.

Warning absorbed from the round (agents 5, 8): the Lean target admits
H = 1, so window-only averaging mechanisms yield lemmas, not closures.

**Node G update (2026-08-09, records 012–014; corrected per
029/030):** G2 **closed-dead at class scope** — class 𝔉 (L²-Mertens
input + sign-discarding recombination at H=1, = every
completion/large-sieve implementation; review 014 structural lemma).
Kernel of the obituary: F(σ) ≥ 1/2+σ/2, expansion ≥ 1/4 on the whole
range, both model families, independent routes; the bounded-fiber
transfer separately dead by exact counterexample (012). Reopens when:
an argument outside 𝔉 — direct μ×R cancellation (Cell D) or a Type-II
route with an honest prime-correlation input. **New leading object
(review 014): the Abel-form bilinear statement
Σ_{d≤√x} μ(d)(π(x/d)−Li(x/d)) ≪ x^{1/2+ε}** — related to the E-face
target by the exact identity E = S − M(K)R(y); estimate-equivalence
at 1/2 additionally requires |M(K)R(y)| ≪ x^{1/2+ε}, whose R(√x) half
is prime-side RH at half scale, supplied by no Mertens-side induction
(029/030; 014's "no exponent flow" claim retracted). Neither face is
kernel-linked to H/RH — see the re-frozen program target above.

## H. Round-2 angles (Abel face; blind panel 017, 2026-08-09)

Full mapping in results/017 verdict. NOTE (029/030): the 017 packet's
face-equivalence claim and boundary-term waiver were false; read this
node through the re-frozen target above. Shortlist: **H1** agent0
moment-hierarchy (deletes obstacle 3; rung-0 = unconditional Moment-Hierarchy
Equivalence Theorem, Lean-formalizable). **H2** agent8 product-form
Perron / full-constant KV (𝔉-exit by inventory; hinge lemma needs the
1/ζ-completion repair — do NOT execute as written). **H3** agent4
Landau–Gonek zero-pair resolvent (RH content quarantined in
−M(x)log K; rung 2 → two-zero moments, Ng line). **H4** agent6
exact-telescoping sieve reduction (residue lands on the sanctioned V8
door). New standing obstacle: **zero-coordinate shadow of 𝔉** —
CS-over-zeros with absolute F_K reproduces trivial scale; signed
evaluation at zeros or exit. Clusters Z/V/I with shared kill
conditions (017 verdict); kill-wave order K1,K7,K2,K5,K3,K4,K6.

### H3 gate correction (record 021, 2026-08-09; amended per 029/030)

The 018-named cluster-Z gate (Σ|F_K(ρ)|/|ρ| ≪ polylog, "unconditional
Ng-line J₋₁") is DEAD as formulated — desk-exact: (i) line-only F_K
moment suppresses the x^{β−1/2} cost of off-line zeros (obstacle 6);
(ii) the prime-power remainder C_{x,K} carries
−√x·F^log_{K,x}(1/2)/log x, invisible to any moment at nontrivial
zeros. Cluster Z survives only as the **frozen Z-repaired gate**
(corrected form, 030): ∃A,C,x₀ ∀x≥x₀ ∀K∈[κ₋√x,κ₊√x] ∃T∈[x²,2x²]:
x^{−1/2}|C_{x,K}| + 2x^{−1/2}Σ_{0<Im ρ≤T, all zeros,
w/mult}|Σ_{d≤K}μ(d)Li_*((x/d)^ρ)| ≤ C(log x)^A, AND, at the same T,
the truncation remainder E_T(x,K) in S = −2Re Σ_{0<γ≤T} G_{x,K}(ρ)
+ C_{x,K} + E_T(x,K) satisfies E_T ≪ √x(log x)^{O(1)} uniformly over
d ≤ K. The E_T clause is an unconditional side lemma (not supplied by
018/021; 022 hit this wall) — without it the boxed inequality does
NOT imply the Abel target; the original ∀T was equivalent to T = 2x²
by monotonicity, and ∃T is what sufficiency uses. Constraints: A ≥ 1
forced (Landau–Gonek; the earlier "A < 2 untenable" applied only to
the unnormalized F_K-proxy — the Li_* kernel costs a log); RMT
expectation A = 5/4. Strength class: the gate implies the Abel target
and is, as far as known, strictly stronger than RH — RH ⟹ gate is NOT
known in either clause; the gate can fail while RH and the Abel
target both hold. The C-clause also hides the m ≥ 2 zero harmonics of
C₀ (termwise cost x^{5/8}·polylog — a second Möbius demand at
Re s = 1/4). Ng J₋₁ literature is RH-conditional throughout. Rung 0 =
𝓜 = o(√x) unconditional (ladder note: S = o(x) already known);
𝓜 ≪ x^{1/4−δ} = rung 1 in the 021 sense. Method-level kill from 022
(corrected): triangle-over-d has an unconditional ≍ x^{3/4} ceiling
even under RH — a strip advance reopens rung 1 only, never rung 2.
Second-moment/CS attempts re-enter the zero-coordinate shadow of 𝔉.
Full chain audit: results/021; certified corrections: 029/030.

### H4 verdict (record 025, 2026-08-09): CLOSED-KILLED — grounds re-classified per 029/030

Agent6's exact-telescoping sieve reduction stays dead, on
re-classified grounds (030): grounds 1 (HB type-I support:
g(p) = (1−k)log p for p > D), 3 (Λ-side mass ≍ D^{1/2−ε}·log D at
rung-2 weight, polynomially divergent) and 4 (the stated
one-parameter self-similarity is false) are exact. Ground 2 is
CORRECTED: passage to 1_P does NOT destroy the telescope — the unique
exact kernel g_P = 1_P∗μ exists and the salvage identity applies to
it verbatim; what fails is the proposal's form (g_P not supported on
[1,D]; prime-side mass ≍ D^{1−θ}/((1−θ)log D) diverges). Ground 5 is
a survey, not a non-existence theorem. The Harman/β-sieve branch was
NOT reached by grounds 1–3 (its kernel g(d) = λ_d·1_{d≤D} genuinely
has compact support); it dies separately on the λ₁ = 1 degeneracy
(the a = 1 renewal term feeds T(x) into its own bound — induction
vacuous) plus the proposal's own "never as majorants" constraint; the
two-parameter repair H(N,B) dies on circularity (H(N,1) = M(N)).
Salvage: the telescope identity Σ(g*1)(n)M(⌊X/n⌋) = Σg(a) is TRUE +
exact edge formula — formalizable, but a one-line corollary of
Σ_{n≤X}M(⌊X/n⌋) = 1, not new leverage; the rung-0 deliverable is
redundant, not killed (equal strength banked in 022). Reopens on:
edge operator of norm < 1 at homogeneity 1/2+ε, or a signed
contraction for (k−1)μ(a)log a — new Möbius-correlation input (Cell D
again). Full grounds: results/025 as amended by results/030.

## I. Round-3 shortlist (blind panel 026, mapping 027) — post-audit status (029/030/032)

Both shortlist items are off the attack tree. The 026 packet carried
the false face-equivalence and the mis-stated Wigert kill (absolute
majorant only — the signed increment is OPEN; 023 re-scoped, 030), so
all round-3 scoring inherits those caveats.

**I1 (canonical-square ensemble dispersion, k=1 gate) — DEAD as
designed (029/030; probe-confirmed at scale 032).** The required
diagonal bound is RH-equivalent: every dispersion implementation
separates the sign-blind μ² diagonal
D(Y) = Σ_{y,t}Σ_{d≤y} μ(d)²R(⌊n/d⌋)², and D(Y) ≪ Y^{4+ε} ⟺ RH
(window density ~1/2 + Lipschitz transfer + Landau/Ingham). Probe at
Y ≤ 2048 (032): D(Y) fits Y^{3.743}; E₂/D stays 0.17–0.28, no upward
trend — Möbius signs buy a bounded factor, not a power; the DC block
carries 99.86% of window energy. Secondary (030): the μ∗Λ zero-mode
device is unavailable at the truncation (its complementary half is
025's Λ·M hyperbola edge — obstacle-9 PASS reversed); the rung-1
label was wrong (E₂ ≪ Y^{4+ε} is RH-scale under the program's own law
E₂ ≍ Y^{2+4θ}, paying out only x^{5/6+ε} while RH pointwise gives
x^{3/4+ε} by triangle). Closed-lane class (circular): any
canonical-ensemble second-moment attack that separates the d=e
diagonal must first prove an RH-equivalent mean square for π−Li —
closes the whole k≥1 family.

**I2 (DC/AC principal-mode isolation) — CIRCULAR (029/030;
probe-confirmed 032).** |V₀ − A_q| ≪ q log q UNCONDITIONALLY (trace
identity + window divisor count; 023's affine modulus even gives
(1+o(1))·q), so |A_q| ≪ q^α ⟺ |V₀| ≪ q^α at every α > 1 — DC ≡
pointwise at every rung-1 precision and at the target. Probe at
x = 10⁸ (032): |V₀−A_q| fits q^{0.505}. A coordinate change in
upstream's dead-lane sense, not a reduction; the spectral-contraction
step assumes 025's reopening condition and, as stated, has no shape
that outputs a bound on A_q (no norm control, no scale recurrence, no
reconstruction of the projected-out constant mode; square-scale
iteration yields only log-power savings). Diagnostic: sign-blind
termwise summation delivers x^{3/4+o(1)} under RH, so a rung-1
exponent 1−δ certifies the signed mechanism only for δ > 1/4; the
measured termwise 0.678 is finite-range and must not define a gate.

**Salvage — identity-grade nodes (NOT attack routes; Committed: none).**
- **I-id1, exact increment law (from I2), identity-only.**
  V_t − V_{t+1} = c_q(X−t), exact on 0 ≤ t ≤ q−2 (t = q−1 adds the
  boundary term μ(q−1)R(q−1)); trace identity; finite Poincaré;
  base-at-2 ramp formula for A_q INCLUDING the boundary term
  R(2)·M(q−1) (base-at-1 is illegitimate — Li(1) diverges), with the
  m ≥ 3 convention. Value: unconditional pin ⟺ window-mean transfer
  certificate, Lean candidate. Naming: c_q is a truncated Möbius
  convolution, NOT a Ramanujan sum (classical c_q(q) = φ(q) would
  break the τ-bound); rename in Lean (030).
- **I-id2, ensemble/pin geometry (from I1), identity-grade.**
  Canonical windows [y²+y, y²+2y] cover [Y²,4Y²] with density ~1/2;
  the Canonical Ensemble Amplification Lemma survives intact,
  Lean-formalizable: E₂(Y) ≪ Y^{A+ε} ⟹ |S| ≪ x^{(A+1)/6+ε} with the
  formalized pointwise constant (x^{3/4+ε} at A = 4 via 023's affine
  modulus awaits formalization — the kernel still carries only the
  crude C·(t+1) constant, 030). The exact k=1 Gram identity may be
  recorded only with the R-diagonal, the window-mean DC term, and the
  truncated-convolution edge all displayed.
- **D≡P equivalence (program result, elementary, Lean candidate;
  030).** By the exact mean split Σ|V_t|² = W|A_q|² + Σ|V_t−A_q|² and
  the unconditional Poincaré bound, cluster D's windowed mean-square
  rung-2 target and cluster P's DC deliverable |A_q| ≪ q^{1+ε} are
  the SAME estimate: D was killed on METHOD (Ω_H depends only on
  max(m,n) — no m−n localization, defeating agent 9's conductor
  lowering, misattributed to agent 6 in 027; the named spectral tools
  are coefficient-uniform), not on target. The deep-rectangle block
  is a cancellable term, not a lower bound. Cluster R corrected: the
  reopen condition is "supply the signed contraction", not "remove an
  absolute value".

## J. Certified constraint set for round-5 proposals (frozen; 029/030/032)

Committed: none. Checked against every round-5 proposal at mapping
time; a violation is an auto-kill, citing the record.

1. **Attack the SIGNED cross-d cancellation directly.** Measured
   (upstream's own probe scripts, replicated verbatim at x ≤ 10⁸,
   032): the signed d-family sum beats its triangle majorant by only
   ~D^{0.33} (signed exponent 0.5145 vs triangle 0.6780; D ≍ √x) —
   below full √D and below upstream's own stated requirement
   x^{0.18}. Full square-root cancellation is NOT measured;
   mechanisms must engage the signed saving that exists, not
   presuppose more (029/030/032).
2. **Termwise |R(x/d)| / |M(d)| or absolute values across the
   d-family: auto-kill.** The triangle-over-d method has an
   unconditional ≍ x^{3/4} ceiling even under RH (030); the absolute
   floor-jump majorant is polylog-dead by Wigert while the SIGNED
   increment — keeping Σ_{d|n}μ(d) = 0 cancellation — remains OPEN
   (023 re-scoped, 030): absolute-value routes both die and miss the
   open object.
3. **Coordinate changes that relocate the difficulty: auto-kill.**
   Certified instances: C − 2E (C = M + 2E identically; 030) and
   DC/AC (|V₀−A_q| ≪ q log q, so DC ≡ pointwise; 030/032). Test:
   does the new coordinate's obligation transfer back unconditionally
   at the same exponent? If yes, it is a relocation, not a reduction.
4. **The μ²-diagonal test.** Extract every nonnegative sub-block the
   method must bound separately (sign-blind μ² diagonal, DC/zero
   mode, positive-energy packet) and ask: is the hypothesis already
   RH on a subobject? If the required sub-block bound is
   RH-equivalent, the route is circular at the level of required
   inputs — I1 died exactly this way, probe-confirmed (029/030/032).
