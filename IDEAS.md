# IDEAS.md — the attack-angle tree

Governed by `PROOF_OS.md` (surfaces section). The only file where
speculation is allowed; every claim here about what a technique *can do* is
UNVERIFIED unless it cites a record or a source document. Seeded 2026-08-08
from the two papers' own stated programs (nodes A–C, E) plus
clearly-marked speculative literature analogues (F). No experiments have
run; `Committed: none` everywhere. A blind-panel re-seed (PROOF_OS law 13)
is pending and should run before heavy allocation.

Targets, verbatim sources in `AGENTS.md`:
- **HN**: prime-wheel harmonic nonconcentration (paper eq:HN; Lean
  `PrimorialWheelDirichletNonconcentration`).
- **SPS**: square-block survivor power saving (`conj:survivor-power-saving`
  for `Z_Λ(t) = −Σ_c μ(c)·K_{Λ,t}(c)`).
- **SYN**: forthcoming synthesis target (collaborator-stated; exact form
  pending repo).

## Strength ladder (law 10)

| Rung | Statement | Status |
|---|---|---|
| 0 (trivial entrant) | sublinear maximal control of the block residual ⟺ PNT, in-coordinates | open — see node E |
| 1 | any fixed exponent θ<1 for the block residual | open |
| 2 (target) | 1/2+ε — HN / SPS / SYN | open |
| above target | sharp O(√x) | not a goal |

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
  rung as its control.

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
   Kernel audit of the forward pair pending (003).
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
