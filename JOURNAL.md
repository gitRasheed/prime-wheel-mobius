# JOURNAL.md

## Live block (updated 2026-08-08)

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
  - NO PUSH; all OS work stays on local branch `agent-os`. Expires: only
    by Fred's explicit direction.
  - square-block-mobius is read-only. Expires: only by Fred's direction.
  - No experiment declarations until the blind-panel seeding event and
    Fred's sign-off on the OS adoption. Expires: on that sign-off.
- Blocked: node D (synthesis) — repo not published.
- Next tasks:
  1. Run `lake build RHLean --wfail` + audit locally; record evaluator
     health honestly (diagnostic).
  2. Known-unknown #1: compute/plot the eq:HN left side at feasible k
     (diagnostic).
  3. Convene blind panel to re-seed `IDEAS.md` (packet committed first).
  4. On synthesis repo arrival: extract exact target into `AGENTS.md`,
     resolve the Ramanujan-sum labelling flag.

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
