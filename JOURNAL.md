# JOURNAL.md

## Live block (updated 2026-08-09, post-seeding)

- Phase: **seeded — experiment gate OPEN** (record 005 complete).
  First wave = kill-test diagnostics, not proof attempts.
- Target: `ProjectedRenewalQuadraticBoundedStatement`
  (mobius-synthesis; premise-free bridge to RH, record 003).
- Leading angle: none yet — shortlist G1–G4 (IDEAS.md node G) pending
  kill tests 4/7/1 (mapping report, results/005).
- Evaluator health: GREEN all three repos (record 003, EC2
  mobius-fleet-1). C/E correlation confirmed to 0.94 (record 004).
- Active constraints:
  - NO PUSH, any repo; all agent work on local `agent-os` branches;
    `main` never modified. Expires: only by Fred's explicit direction.
  - Cross-model policy (Rasheed, 2026-08-09): adversarial reviews and
    independent verification via Codex companion; Claude agents for
    deep-context work. Expires: by direction.
- Blocked: nothing.
- Next tasks:
  1. Build the shared 10⁹ segmented-sieve kill-test framework (one
     diagnostic record); run tests 4, 7, 1 (settle clusters L, I, S).
  2. Declare first experiments on surviving shortlist angles (G1
     first), one record each, budgets + gates frozen at declaration;
     Codex adversarial review on each declaration.
  3. Connecting-theorem experiment (NonzeroResponseRHScale ↔ quadratic
     statement) — small, kernel-checkable, closes the orphan gap.
  4. Report to Fred: records 002–005 summary + orphan flag.

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

### 2026-08-09-6 — record 003 verdict: evaluator GREEN everywhere; bridge kernel-clean; canonical-target correction

Phase 0 complete, far faster than expected: the EC2 evaluator built
all three repos in under 10 minutes total (warm mathlib cache + NVMe;
the local drvfs builds were superseded and stopped, partial logs
retained). All three audit scripts pass. `#print axioms` on
`projectedRenewalQuadraticBounded_imp_riemannHypothesis_unconditional`
and `riemannHypothesis_of_mertensEnergy`: exactly
`[propext, Classical.choice, Quot.sound]` — the estimate→RH chain is
premise-free at kernel grade. Known-unknown #6 closed (square-block
verifies).

The finding that matters most: the single unimported module is
`RHLean.Analysis.MobiusSynthesisBoundary`, the file defining the
README's headline `NonzeroResponseRHScale`. It compiles but nothing
references it — no theorem ties it to
`ProjectedRenewalQuadraticBoundedStatement`, which is what the bridge
consumes. Definition drift caught exactly as PROOF_OS's kernel-channel
reference section warns. Program response: canonical target is now
declared as the quadratic statement (AGENTS.md updated); the orphan is
flagged to Fred; proving the connecting theorem is queued as the
candidate first experiment after the blind panel.

Frontier delta: none — this is formalization-support (verified
baseline), honestly labelled. Frontier =
`ProjectedRenewalQuadraticBoundedStatement`. Next: Phase 1
reconnaissance numerics on the EC2 box; seeding packet draft.

### 2026-08-09-7 — diagnostic 004 done: C/E correlation confirmed; box oversized for recon

Record 004 closed. ~12,000 square samples, k=2..8, X ≤ 223,092,870,
all implementation gates green (micro-example asserts, identity
H = C−2E at every sample). Headlines: corr(C,E) rises to 0.94 at k=8
with 77% sign agreement — the route doc's central bet is confirmed in
independent data; cancellation ratio ~0.5–0.6; sup|H|/√X ≤ 0.51
everywhere (mild upward drift in the sup, tracked, not evidence).
Utilization verdict per Rasheed's logging directive: avg CPU 1.6% —
Phase-1 numerics are trivial for c7i.4xlarge; retained solely for
Phase 2's concurrent Lean loops, downscale if Phase 2 telemetry
repeats this. Full 304MB exact k=8 CSV on the box by sha256.

### 2026-08-09-8 — decision: seeding complete, experiment gate OPEN; cross-model review policy

Record 005 closed: 10/10 blind proposals returned and mapped (node G
in IDEAS.md; clusters Q/S/L/I/R; shortlist G1–G4; kill-test
inventory). Convergence worth its own line: five independent lenses
built quadratic-phase dispersion out of X_n = n(n+2) — the sampling
structure as the missing large-sieve substitute — and zero chose the
prime-wheel paper's own program (node A). Both halves of the
experiment-gate constraint are satisfied; gate OPEN. Declared first
wave: the shared segmented-sieve framework + kill tests 4 (μ×err sign
correlation), 7 (exact identity checks — settles cluster I), 1
(per-frequency cancellation — settles cluster S). Note the tension to
test first: record 004's corr(C,E)=0.94 is weak evidence AGAINST
cluster L's load-bearing assumption — cheap to check before any deep
spend there.

Also per Rasheed this session: subagent/workflow model policy —
adversarial reviews and independent verification passes run on the
Codex companion (cross-model diversity, exactly what PROOF_OS's
anti-sycophancy contract wants); Claude agents keep deep-context work.
Recorded as a standing allocation policy, revisable by decision event.

### 2026-08-09-9 — experiment 007 SUCCESS: connecting theorem kernel-proved (first original contribution)

Full success on the program's first declared experiment. The orphan
`NonzeroResponseRHScale` is now kernel-equivalent to
`ProjectedRenewalQuadraticBoundedStatement` (∀Λ≥0 form) — new module
MobiusSynthesisBoundaryBridge at mobius-synthesis agent-os 6026165,
manifest import 59c7fdd; coordinator independently re-ran the full
frozen gate on the box (7602-job build green, audit clean, axioms
baseline-only on all three theorems). Frontier delta: none —
formalization-support, honestly labelled; the analytic frontier is
unchanged but the program now has ONE canonical target with two
proven-equivalent faces, and the definition-drift gap flagged in
record 003 is closed on our branch. Report item for Fred (his README
cites the formerly-orphan predicate). Kill-test wave (006) still
running in parallel.

### 2026-08-09-10 — decision: model-routing refinement (Rasheed)

Extends 2026-08-09-8. Constraint learned: Codex/GPT-5.6 subagents run
sandboxed — no AWS CLI / SSH. Routing policy: Fable = coordinator
(records, gates, briefs); Opus 5 subagents = all infrastructure-
touching work (AWS, box builds, numerics), given tightly-scoped briefs
(frozen targets, exact paths, hard asserts, fixed report formats —
the wander guard); Codex/GPT-5.6 = pure-reasoning work (adversarial
review, proof-sketch critique, independent verification), where the
sandbox costs nothing and cross-model diversity is the value. Hybrid
permitted: Opus agents invoking the Codex plugin to relay GPT-5.6
reasoning into tool-capable hands. Rasheed forecasts ~20-subagent
GPT-5.6 workflow waves — route those at sandbox-safe tasks only.
