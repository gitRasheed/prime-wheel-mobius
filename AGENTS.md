# AGENTS.md — router and declared facts

This project runs under [`PROOF_OS.md`](PROOF_OS.md) (adopted 2026-08-08;
see `results/001/`). This file holds the program's declared facts. It holds
no state and no narrative — state lives in `JOURNAL.md`, speculation in
`IDEAS.md`, evidence in `results/`.

## The program

Goal: bound the Mertens function `M(x) = Σ_{n≤x} μ(n)`. The two classical
criteria (stated in `paper/seeded_prime_comb_harmonic_reduction.tex`,
§"What has to be bounded"):

- PNT ⟺ `M(x) = o(x)`
- RH ⟺ `M(x) = O_ε(x^{1/2+ε})` for every ε > 0

Two Lean-formalized coordinate systems reduce this to one explicit open
estimate each:

**Prime wheels (this repo).** Residue classes mod primorials; the block
residual `R_k(x) = M(x) − M(W_{k-1})` has an exact finite-torus Fourier
representation. Open statement (paper Conjecture "Prime-wheel harmonic
nonconcentration", eq:HN; Lean name `PrimorialWheelDirichletNonconcentration`):

> For every ε>0 there is C_ε such that for every k≥1 and 1≤N≤H_k,
> |Σ_{r mod Q_k} b_k(r) D_N(r/Q_k)| ≤ C_ε (L_k+N)^{1/2+ε}.

Proved in Lean (`docs/THEOREM_STATUS.md`): the exact equivalence chain
`primorialWheel_dirichletNonconcentration_iff_mertensEnergy`, and — given
the classical Mertens–RH criterion as a typed premise —
`primorialWheel_dirichletNonconcentration_iff_riemannHypothesis`
(`formalization/RHLean/Analysis/PublicPrimeWheelReduction.lean`). The
classical criterion `MertensEnergyBoundedStatement ↔ RiemannHypothesisStatement`
is supplied explicitly, not hidden.

**Square blocks (`/mnt/d/Projects/square-block-mobius`, read-only).**
Integers grouped between consecutive squares; lifetime flow of canonical
sources `m = c·q`, `q = P⁺(m)`. Open statement (README; paper
`conj:survivor-power-saving`): the power-saving estimate for the signed
survivor operator `Z_Λ(t) = −Σ_c μ(c)·K_{Λ,t}(c)`. Everything else in the
spine — low-height occupancy, death-process control, criteria equivalences
— is proved and formalized (paper §"What is proved, formalized, and still
open").

**Synthesis (forthcoming repo — the eventual focus).** Collaborator-stated
(Fred Viole) unified target: `Σ_q C(q)·(unshifted c_q − 2×smooth-shifted
c_q) = O(√x)`, with `c_q` Ramanujan sums and `C(q)` an explicit local
product; the weaker `o(x)` bound yields PNT from the same decomposition.
Status: `[assumed]` — no repo yet; the statement is UNVERIFIED against
sources. Note for reconciliation: the prime-wheel paper explicitly remarks
(remark "Not a Ramanujan sum", after eq:core-fourier) that its truncated
divisor sum is *not* a classical Ramanujan sum; whether the synthesis
recasting is exactly Ramanujan-sum-indexed is a fact to extract from the
synthesis repo when it lands. Resolution owner: Fred Viole.

**Strength ladder (law 10).** Rungs, weakest first: (1) sublinear maximal
control of the same block residual ⟺ PNT — the program's trivial-entrant
rung, demonstrating the machinery closes end-to-end at `o(x)`; (2)
any fixed exponent `θ < 1` improvement; (3) the target `1/2 + ε` (RH).
Stronger than target: `O(√x)` sharp (stronger than RH-known; not a goal).
No rung is currently proved unconditionally — all status: open.

## Channels (law 7)

| Channel | may_promote | may_close | Notes |
|---|---|---|---|
| kernel | **yes** (sole) | yes | Rule: green build + clean axiom audit on the exact statement at a named commit |
| numerics | no, ever | yes, scoped | Exact counterexample closes outright; falsified asymptotics close at `implementation` only; every read declares range + arithmetic model |
| informal argument | no | no | Generates; all output UNVERIFIED until kernel/reviewer confirms |
| literature | no | via reviewed barrier only | Analogue shelf; established results cited, never rediscovered |

## Evaluator identity (law 5)

**prime-wheel-mobius** (this repo):
- Toolchain: `leanprover/lean4:v4.24.0` (`formalization/lean-toolchain`)
- mathlib: `v4.24.0`, manifest rev `f897ebcf72cd` (`formalization/lake-manifest.json`)
- Build: `cd formalization && lake update && lake build RHLean --wfail`
- Axiom/sorry audit: `bash formalization/scripts/audit_assumptions.sh`
  (rejects `sorry`/`admit` and project-local `axiom`/`constant` declarations)
- CI: `.github/workflows/lean.yml` (audit + build), `numerics.yml`
  (hash-manifested numeric reproduction)
- Foundations: standard Lean/mathlib classical foundations; noncomputable
  defs allowed (`docs/THEOREM_STATUS.md`)

**square-block-mobius** (sibling):
- The 2026-08-09 republished export (origin/main `8ff51e1`, local branch
  `agent-os`) **adds build scaffolding**: `lean/lakefile.lean`,
  `lean/lean-toolchain` (`leanprover/lean4:v4.24.0`, mathlib `v4.24.0`),
  `lean/scripts/audit_assumptions.sh`. The former UNOBSERVABLE status is
  resolvable; kernel verification in progress under `results/003/`.

**mobius-synthesis** (sibling, arrived 2026-08-09, commit `e87f728`):
- Toolchain: `leanprover/lean4:v4.24.0`, mathlib `v4.24.0` (root
  `lakefile.lean`, `lean-toolchain`); audit script
  `scripts/audit_assumptions.sh`; 248 modules under `RHLean/`.
- Declared open targets (extracted from source, record 003):
  `NonzeroResponseRHScale` (`RHLean/Analysis/MobiusSynthesisBoundary.lean:46`,
  |H_{k,n}| ≪ X_n^{1/2+ε} at square-prefix samples) and its
  quadratic-form counterpart `ProjectedRenewalQuadraticBoundedStatement`
  (`RHLean/Proof/CanonicalGapAncestryQuadraticClosure.lean:122`), which
  the terminal bridge consumes. Route doc (`CURRENT_PROOF_ROUTE.md`)
  directs attack at the signed object C^PNT − 2E^rec
  (exact decomposition `..._eq_pntCorrected_sub_two_error`,
  `RHLean/Analysis/PrimeSievePNTCentering.lean:213`), explicitly not at
  its two pieces separately.
- Bridge status: **kernel-verified 2026-08-09 (record 003)** — the
  forward chain estimate → RH is criterion-free:
  `projectedRenewalQuadraticBounded_imp_riemannHypothesis_unconditional`
  (`RHLean/Proof/TerminalMertensForward.lean:37`) and its engine
  `riemannHypothesis_of_mertensEnergy`
  (`RHLean/Analysis/MertensEnergyRHForward.lean:66`) both `#print
  axioms` to exactly `[propext, Classical.choice, Quot.sound]` (green
  build + clean audit, EC2 evaluator). The *equivalence* still takes
  the typed premise `ClassicalMertensRHCriterion`; reverse RH → Mertens
  not asserted.
- **Canonical program target**: `ProjectedRenewalQuadraticBoundedStatement`
  ⟺ `NonzeroResponseRHScale` — **kernel-proved equivalent** (record
  007, our contribution: `MobiusSynthesisBoundaryBridge` at
  mobius-synthesis `agent-os` 6026165+59c7fdd, local branch only; the
  formerly orphan module is now imported and audited). One target, two
  proven faces. Upstream `main` still has the orphan gap — report item
  for Fred (owner: Fred Viole).

**Fleet evaluator (record 003 onward).** EC2 `mobius-fleet-1`
(i-0fc2bb4713d1486ca, us-east-1, Ubuntu 24.04, elan → lean4 v4.24.0,
mathlib v4.24.0, warm caches for all three repos). Tooling and
inventory: `/mnt/d/Projects/mobius-ops`. Local drvfs builds are
superseded for verification work.

Audit fact (2026-08-08, this adoption): grep over all 61 `.lean` files in
both repos — zero `sorry`/`admit`, zero project-local `axiom`/`constant`
declarations (one grep hit in
`square-block-mobius/lean/RHLean/Proof/DeathShellSubpolynomial.lean:321`
is the word "constant" inside a docstring, not a declaration). Grep is the
source-level audit; full kernel verification = build + `#print axioms`,
per law 5.

## Declared obstacles (law 8 — attacks must address these)

- **Pinned vs averaged** (paper §"Averaged translations versus the
  primorial origin"): the start `L_k = W_{k-1}` is deterministic and
  arithmetically synchronized with the field; L²-averaged translation
  estimates permit exceptional starts. Any averaged-technique attack must
  prove uniformity in L, exclude `W_{k-1}` from the exceptional set, or use
  the primorial phase directly.
- **Large-sieve non-transfer** (square-block paper, discussion after
  `conj:survivor-power-saving`): the survivor kernel counts primes in a
  window fixed by one arithmetic condition at one synchronized scale — no
  family of shifts to average over; and no constructed map from
  off-diagonal pairs (c,c′) to a shared modulus with sub-square
  multiplicity. Both are named as the missing ingredients.
- **Regime gap** (this repo's README, "Why the regimes do not meet"): the
  completable-wheel cutoff (`y ≍ log x`) and the exact-reconstruction
  cutoff (`y ≍ √x`) are separated by a gap exponential in π(y); sharpening
  the completion error does not close it.
- **Finite-range deception** (square-block paper status box): near-flat
  empirical exponents over few dyadic scales misled the Mertens conjecture
  before Odlyzko–te Riele; numerics never promote.
- **Parity-type obstruction** (literature, `analogue-unverified` for these
  exact coordinates): classical sieve parity barriers limit what
  sieve-only arguments can say about μ-weighted sums; whether it binds the
  survivor/nonconcentration forms specifically is unestablished — an
  attack from sieve machinery should state its position anyway.

## Repos, governance, layout

| Repo | Path | Role | Write? |
|---|---|---|---|
| prime-wheel-mobius | `/mnt/d/Projects/prime-wheel-mobius` | prime-wheel coordinates; OS home | local branch `agent-os` only — **never push** |
| square-block-mobius | `/mnt/d/Projects/square-block-mobius` | square-block coordinates | local branch `agent-os` only — **never push** (relaxed from read-only 2026-08-09, journal 2026-08-09-3) |
| mobius-synthesis | `/mnt/d/Projects/mobius-synthesis` | seam layer joining both systems; primary bounding focus | local branch `agent-os` only — **never push** (journal 2026-08-09-3) |

Uniform rule (Fred's go-ahead as reported by Rasheed, 2026-08-09): all
agent work lives on local `agent-os` branches in each repo; `main` is
never modified, nothing is ever pushed.

Both repos belong to Fred Viole / OVVO-Financial
(`github.com/OVVO-Financial/…`, public). All Proof-OS records, journal and
tree live on local branch `agent-os` in this repo until the collaborator
decides otherwise. Nothing on `main` is modified.

Layout (this repo): `paper/` manuscript; `formalization/` Lean project
(`RHLean/Arithmetic`, `RHLean/Analysis`); `numerics/` deterministic
diagnostics (`primorial_block_validation.py`, `analytic_kill_gates.py` —
"passing them is not a proof", `numerics/README.md`); `docs/` theorem
status + source manifest. Sibling: `paper/`, `lean/RHLean/{Analysis,
Arithmetic,Geometry,Proof}`, `MODULES.md`.

## Routing

| Moment | Open |
|---|---|
| Any rule question | `PROOF_OS.md` |
| Current state / recent decisions | `JOURNAL.md` (head / tail) |
| What to attack next | `IDEAS.md` |
| What is proved in Lean here | `docs/THEOREM_STATUS.md` |
| What is proved in the sibling | `square-block-mobius/MODULES.md`, paper §status table |
