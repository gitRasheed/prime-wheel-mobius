# JOURNAL.md

## Live block (updated 2026-08-09)

- Phase: pre-synthesis. Both coordinate systems formalized and published;
  zero proof attempts run under this OS; synthesis repo pending.
- Target: see `AGENTS.md` — HN (prime-wheel), SPS (square-block), SYN
  (synthesis, forthcoming focus).
- Leading angle: none declared. Tree seeded from papers only
  (`IDEAS.md` A–F); blind-panel re-seed not yet run.
- Evaluator health: prime-wheel `lake build` not yet run locally
  (UNOBSERVABLE here; CI green per repo workflows — unverified this
  session). Source-level grep audit clean (event 2026-08-08-1).
- Active constraints:
  - NO PUSH, any repo; all agent work on local `agent-os` branches in
    all three repos; `main` never modified. Expires: only by Fred's
    explicit direction. (Uniform rule set 2026-08-09-3; square-block
    read-only relaxed to branch-only per Fred's reported go-ahead.)
  - No experiment declarations until the blind-panel seeding event.
    Expires: when the committed packet + panel event land. (Fred's
    sign-off half reported satisfied by Rasheed, 2026-08-09-3.)
- Blocked: nothing. Node D unblocked 2026-08-09: synthesis repo
  published (`OVVO-Financial/mobius-synthesis`, local branch `agent-os`,
  branch-only governance — events 2026-08-09-2/-3). Phase 0 (record
  003) running: builds + audits, all three repos.
- Next tasks:
  1. Extract exact synthesis targets (`NonzeroResponseRHScale`, the
     C−2E signed object) into `AGENTS.md`; reconcile with Fred's earlier
     Ramanujan-sum summary; flag the "no external Mertens→RH axiom"
     claim for kernel verification (event 2026-08-09-2).
  2. Run `lake build RHLean --wfail` + audit locally (here AND
     synthesis — synthesis ships lakefile + audit script); record
     evaluator health honestly (diagnostic).
  3. Convene blind panel to re-seed `IDEAS.md` (packet committed first).
  4. Optional follow-up to 002: structured k=4 spectrum for the
     conductor-decay profile (known-unknown #2).

---

## Event stream (append-only)

### 2026-08-08-1 — decision: adopt Proof-Search OS

Adopted `PROOF_OS.md` (adaptation of the Competition OS; this repo's copy
is the governing revision — see `git log PROOF_OS.md` for the commit read)
on local branch `agent-os`. Migration record: `results/001/`. First
governed record ID: 001. Deliberately not adopted from the source OS:
`submission`/`rescore` record kinds and the `generalisation_design` schema
(rationale inside `PROOF_OS.md`, laws 3 and 7); the four source checklists
are folded into reference sections rather than shipped.

Founding audit, run this session (2026-08-08), source-level grep across
both repos (61 `.lean` files: `formalization/` here,
`../square-block-mobius/lean/`):

- `sorry|admit`: **0 hits**
- `^\s*(axiom|constant)\s`: **0 declarations** — one textual hit at
  `square-block-mobius/.../DeathShellSubpolynomial.lean:321`, inspected:
  the word "constant" inside a docstring, not a declaration.

Scope of that claim, honestly: grep is source-level only. Kernel-grade
promotion evidence (build + `#print axioms` at a named commit, PROOF_OS
law 5) has not been produced this session for either repo; prime-wheel CI
(`.github/workflows/lean.yml`) runs exactly that pipeline upstream.
Square-block has no local build scaffolding (see `AGENTS.md`,
UNOBSERVABLE).

State of the mathematics at adoption, from the source documents: exact
reductions proved and formalized in both coordinate systems; the open
content is exactly HN (⟺ RH given the classical typed premise) and SPS;
zero attempts at either under any recorded process. `IDEAS.md` seeded
from the papers' own programs; every literature analogue marked
speculative/analogue-unverified per the no-fabrication rule.

Expected next: the three diagnostics in the live block, then the blind
panel, then first declarations. My genuine uncertainty going in: whether
eq:HN is even computable at more than k ≈ 4–5 (Q_k growth), and whether
the synthesis statement will match the collaborator's summary exactly —
both flagged as known unknowns rather than assumed.

### 2026-08-09-1 — diagnostic 002 done: eq:HN left side computed for the first time

Record `results/002/` (declared and committed before running, per
declare→commit→run). Rasheed asked for known-unknown #1 directly,
noting honest uncertainty about whether Fred will want the artifact —
recorded here as a diagnostic on `agent-os` regardless; it promotes
nothing and the branch is never pushed, so the question is deferred.

Findings, compressed (full detail in `results/002/002.md`):

- Exact pinned profile k=2..8 reproduces the paper's Section-7 table
  independently; eq:HN's own ratio sup|R_k|/(L_k+N)^{1/2} is 0.43–0.89,
  flat-to-falling; in-block ratio 1.0–1.8, no trend. Deception caveat
  in force — nothing asymptotic follows.
- Spectral side verified end-to-end at k=2,3: b_k(r) built by direct
  DFT reproduces R_k(L_k+N) for every N to ≤1.1e-14; Parseval and the
  ℓ¹ raw-comb identity check exactly. Paper conventions and
  implementation agree.
- Feasibility (the journal's open question) settled: dense spectrum
  k≤3 only; 𝒬₄ ≈ 9.0×10⁸ structured-only; 𝒬₅ has 36 digits, 𝒬₈ 2,638.
  Numerical access to eq:HN at scale is permanently identity-side
  (μ-sieve range), never Fourier-side. Attack gates must not assume
  large-k spectral computation.
- First conductor landscape at k=3 (toy): ℓ² mass in small conductors
  (6 and 30 ≈ half the energy); ℓ¹ mass anti-concentrated at the full
  conductor. Seeds the k=4 structured follow-up for known-unknown #2.

My read going forward: the finite window is unremarkable — comfortably
sub-√ everywhere — which is consistent with the papers' position that
the entire difficulty is asymptotic and coordinate-honest. No new
attack sub-node earned; A1–A5 unblocked from the "never computed"
unknown. Expected the identity check to pass; the useful surprises were
how early dense-spectrum feasibility dies (k=3!) and the ℓ¹/ℓ²
concentration split.

### 2026-08-09-2 — observation: synthesis repo published; both siblings republished; claims to verify

Remote check (Rasheed asked for updates; law 6 standing watch):

- **`OVVO-Financial/mobius-synthesis` is live** (created 2026-08-09
  ~03:28 UTC, single "Initial commit"). Cloned read-only to
  `/mnt/d/Projects/mobius-synthesis`. Node D unblocked. 248 Lean
  modules, toolchain v4.24.0 (matches ours). Source-level grep: zero
  real `sorry`/`admit` (all hits are prose; `TerminalAxiomAudit.lean`
  is the repo's own audit module). Kernel build NOT yet run — all
  claims below UNVERIFIED at kernel grade.
- Both siblings were **republished as fresh single-commit exports**
  (~03:28–03:35 UTC): local `main`s now diverge from `origin/main`s.
  Prime-wheel delta: README +8, SOURCE_MANIFEST reworked, licenses
  added. Square-block delta: **adds `lean/lakefile.lean`,
  `lean-toolchain`, `audit_assumptions.sh`** — the missing build
  scaffolding; known-unknown #6 is now resolvable by running it.
- Synthesis content (from README/SEAMS/CURRENT_PROOF_ROUTE, prose
  reading only): explicitly "not a third route to RH" — a seam layer.
  Canonical target: `NonzeroResponseRHScale`, i.e. |H_{k,n}| ≪
  X_n^{1/2+ε} at complete-square samples X_n=(n+1)²−1 inside
  synchronized blocks, with kernel-checked zero-mode elimination
  (ρ<1/6 contraction) and square-gap transport. Diagnostic-informed
  route directive: attack the signed object C^PNT − 2E^rec directly
  (C, E positively correlated; triangle inequality loses the
  cancellation). Naive strong-induction and direct Bombieri–Vinogradov
  framings are explicitly ruled out in the route doc.
- **Two facts needing reconciliation/verification**: (1) the route doc
  claims the terminal bridge "no longer needs an external Mertens→RH
  axiom" (constructs the forward criterion via Mellin/completed-zeta
  reflection) — stronger than prime-wheel's typed-premise honesty;
  CONFLICTED-pending-kernel-audit until `#print axioms` on the terminal
  theorem is run. (2) Fred's Discord summary described a
  Ramanujan-sum-indexed target; the repo's canonical target is H and
  C−2E (Ramanujan modules exist, e.g. `RamanujanDivisorBoundaryBulk`,
  but are not the headline). AGENTS.md extraction = next task 1.

### 2026-08-09-3 — decision: uniform branch governance; Phase 0 launched

Rasheed's direction this session: (1) all three repos get local
`agent-os` branches; `main` untouched everywhere; nothing ever pushed —
"we don't step on Fred's foot on main"; (2) Fred has given the
go-ahead for us to "do our thing" on our own end (reported by Rasheed;
recorded as such, not as a first-hand Fred statement). Effects:
square-block's read-only constraint relaxed to branch-only writes; the
experiment-gate constraint reduces to the blind-panel half; synthesis
governance set to the same branch-only rule on arrival. AGENTS.md
updated (repo table, evaluator identities). Branches created:
square-block `agent-os` from origin/main `8ff51e1` (the export WITH
build scaffolding), synthesis `agent-os` from `e87f728`.

Phase 0 launched as diagnostic record `results/003/`: kernel builds +
axiom audits in all three repos (elan 4.2.3 installed; all pin
lean4/mathlib v4.24.0), plus extraction of the synthesis repo's exact
open-target declarations and kernel verification of its
"no-external-axiom RH bridge" claim.

### 2026-08-09-4 — extraction verdict: synthesis bridge claim resolved (forward-unconditional); exact targets recorded

Record 003 sub-task (read-only extraction over `mobius-synthesis @
e87f728`, findings verified against source; builds still running).
The 2026-08-09-2 CONFLICTED item resolves with nuance: the forward
chain (open estimate → RH) is criterion-free —
`projectedRenewalQuadraticBounded_imp_riemannHypothesis_unconditional`
rests on an in-repo mathlib-only proof of Mertens-energy → RH
(`riemannHypothesis_of_mertensEnergy`). Only the iff-form theorems
still take the `ClassicalMertensRHCriterion` typed premise; RH →
Mertens is explicitly not asserted. For proving RH, forward is the
direction that matters, so the program's endpoint chain is now
premise-free — pending our own `#print axioms` at kernel grade,
because the repo's `TerminalAxiomAudit.lean` predates this route and
does not cover the unconditional pair. Exact open targets
(`NonzeroResponseRHScale`, `ProjectedRenewalQuadraticBoundedStatement`)
and the C−2E decomposition theorem recorded verbatim in
`results/003/003.md`; AGENTS.md declared facts updated; known-unknown
#7 half-answered. New minor flag: 249 files on disk vs 248 imported —
one unimported module to identify post-build (unimported files escape
build and audit).

### 2026-08-09-5 — decision: EC2 build server + mobius-ops harness repo

Rasheed directed immediate EC2 setup (Phase 2 expected within hours)
and approved a fourth, ours-only ops repo. Created
`/mnt/d/Projects/mobius-ops` (local git, never pushed; code only — no
records/journal content, which stay here per PROOF_OS surfaces rule).
Provisioned in his AWS account (us-east-1): instance
`i-0fc2bb4713d1486ca` (c7i.4xlarge 16vCPU/32GB, 200GB gp3, Ubuntu
24.04, ~$0.71/hr), SSH-only security group locked to our egress IP,
keypair `mobius-fleet`. Bootstrap user-data installs elan and
pre-builds all three repos with mathlib cache; marker BOOTSTRAP_DONE.
vCPU quota increase 16→64 requested (PENDING) for the fleet. Full
inventory: `mobius-ops/README.md`. Local record-003 builds continue in
parallel — the EC2 box is the fleet evaluator going forward; local
remains the OS home. Note: account creds are root — flagged to Rasheed
to move to IAM.
