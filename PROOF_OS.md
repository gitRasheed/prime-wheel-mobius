# Proof-Search OS

A portable operating system for running a formal-mathematics research program
— a search for a kernel-checked proof of a stated target theorem — agent-first.
It adapts the Competition OS built from two full ~330-experiment ML campaigns,
adversarial cross-model review, and live trial installs; the receipts for
every transferred rule live in that repo's `RATIONALE.md`, cited here as
`(source R<n>)`. Nothing in this file assumes a particular theorem, a
particular proof assistant beyond "one exists and has a kernel", or a subject
area.

**The one failure mode this OS exists to prevent, named up front:** an agent
claiming a proof that does not compile, or that compiles with a hidden
`sorry`, `admit`, added axiom, or opaque constant standing in for the
mathematics. This is the exact analogue of leaderboard self-deception in the
source domain — the motivated-reasoning pressure is identical, and every rule
below about frozen declarations, typed records and separated review rights is
aimed at it. A claimed theorem is **UNVERIFIED** until the kernel has checked
it, whoever claims it and however plausible the sketch.

**This is a document, not a package.** A project running this OS carries
exactly **three standing markdown files** —

| File | Job | Mode |
|---|---|---|
| `AGENTS.md` | Thin router + the project's declared facts | in place, rarely |
| `JOURNAL.md` | Live block on top, then append-only event stream | see law 2 |
| `IDEAS.md` | The attack-angle tree | in place |

— plus one markdown file per record under `results/NN/`, and whatever build
scripts, harnesses and orchestration the project needs, written **by the
agent for the project** against the prose contracts here. The OS mandates
*what must be recorded*; it never mandates *how*.

**Git is the integrity layer.** The rule is `declare → git commit → run`.
That single discipline replaces every hash, chain, manifest and ledger an
earlier revision of the source OS shipped. Threat model, stated plainly: git
ordering guards an honest process against its own motivated reasoning — a
later session cannot quietly move a bar that a commit already froze, because
`git log -p` shows the gate committed before the result was recorded. It is
an audit trail for an honest process, not forgery-proofing: it does not stop
a determined history-rewriter, and on a pushed repo that rewrite is loud.
The only code this OS ships is two **optional** conveniences —
`tools/dashboard.py` (renders a table from record frontmatter) and
`tools/lint.py` (frontmatter completeness) — never required, never gating,
never depended on by a rule.

## Labels

| Label | Meaning | Changeable? |
|---|---|---|
| `[invariant]` | Mechanically checkable — including by git or the kernel. | No |
| `[policy]` | A judgement call with a threshold, declared per project. | Yes — retune by decision event |
| `[reference]` | One workable implementation, not normative. | Replace freely |

A rule whose key terms are semantic is `[policy]` however much you want it to
be an invariant. Two reporting states are first-class and never faked: where
you cannot observe the predicate you must judge, report **`UNOBSERVABLE`**
`[invariant]` and do not invent a value — `N/A` says the question is
undefined; `UNOBSERVABLE` says it is defined and you cannot currently see the
answer. A declared fact takes `unknown` with a reason and a resolution owner,
because "we did not check" is not `false` (source R4). Where two source
documents disagree — a paper and its formalization, a collaborator's
statement and the repository — the fact is recorded **CONFLICTED** with a
resolution owner, never silently resolved by picking the convenient reading
(source R22). One state this domain adds: **UNVERIFIED** — a mathematical
claim the kernel has not checked and no reviewer has confirmed. UNVERIFIED
claims may seed the tree; they may never promote, close, or release.

**The balance test `[policy]` — apply it to every edit of this file.**
Falsification machinery is easy to build and compounds; generation machinery
is hard to build and decays. A revision that adds more ways to reject work
than to produce it makes the next campaign worse, however well-evidenced
each rule is. The counting unit is the independent procedure family. The
ledger as of this revision: ~7 generation families (attack tree, literature
analogue search, blind panel, protected exploration, reference-grade
formalization effort, retention/recombination of partial results,
known-unknown reopening) against ~11 rejection/control families. An edit
that widens the gap must add generation machinery first — and in proof
search the asymmetry bites harder than in ML: a failed attempt produces no
gradient, so the only renewable resource is the tree.

## The laws

**1 — Three jobs.** A proof-search agent must generate candidate attack
angles, must avoid fooling itself about what has actually been proved, and
must carry a promising sketch all the way to a kernel-checked formal proof.
The third job is the one most often lost: an informal argument that is
"basically done" and never formalized is worth exactly nothing to the
program's stated goal, and left alone, an agent searches one basin
exhaustively with beautiful rigour while missing the reformulation that
makes the problem tractable (source R2). Incentives select behaviour more
reliably than rules constrain it (source R3): when you add a rule, ask what
an agent optimising the accounting surface does.

**2 — The journal.** `JOURNAL.md` is untouchable: one per project,
agent-written, comprehensive — a bounded mutable live block at the top
(current state, active constraints with expiry conditions, next tasks), then
an append-only event stream holding every decision, its reasoning, and the
session narrative. This is the core thesis of the whole system: a single
journal an agent can read in full — head for now, tail for recent, the whole
file when depth is needed — is the primary cross-session context, and every
audit that ever improved the source OS was possible only because such a
journal existed. It is not to be merged, split, summarised into a dashboard,
or thinned into machine events. Write it with conviction: the reasoning, the
doubt, and what you expected to happen, because the reader is a future agent
with none of your context. A decision that is not in the stream did not
happen `[invariant]` — and `git log JOURNAL.md` shows when it was written.

**3 — Typed decision-bearing records.** Every decision-bearing record gets an
immutable `id` and a `kind`: `experiment | diagnostic | review | migration`
`[invariant]`. An `experiment` is a **proof attempt**: a record whose result
may promote a statement to proved, close an attack angle, or replace the
program's leading approach — declared *before results are observed*. A
`diagnostic` is everything that only informs: numeric exploration, lemma
reconnaissance, refactoring probes, literature reads, build-health checks. A
diagnostic can never be the sole evidence for promotion or closure — it
spawns an experiment, it does not become one. The source OS's `submission`
and `rescore` kinds are retired: there is no platform to submit to, and
re-verification under a new toolchain is a `diagnostic` whose failure
triggers a review (law 5). Untyped work goes invisible (source R4), and
relabelling after seeing the outcome is the escape hatch this rule welds
shut; commit timestamps make the weld hold.

**4 — Two gates, two jobs.** `promotion_gate` is frozen **by the launch
commit** and never edited: it binds what a result may promote, and it stops
the bar moving after the outcome lands `[invariant]`, provable by
`git log -p`. For any claim of the form "X is proved", the promotion gate is
fixed by law 5 and is not negotiable. `viability_gate` binds only whether to
keep spending: a budget decision, revisable by a later commit plus a journal
event naming the observation that justified the revision. Fusing them
converts "we are out of patience" into "this approach is dead" (source R2).
You may change your mind about spending; you may not change the record of
having done so `[invariant]`.

**5 — The evaluator is the kernel.** The proof assistant's kernel is the one
perfect evaluation channel this domain has: noiseless, stationary,
non-adaptive, immune to overfitting — the channel whose absence the source
OS's entire uncertainty machinery existed to compensate for. Evaluator
identity is still typed and epoch-versioned `[invariant]`: **toolchain
version + mathlib (or standard-library) pin + repo commit**, recorded in
`AGENTS.md`. Promotion evidence for "theorem T is proved" is exactly: the
project builds green (`lake build` or equivalent) at a named commit, **and**
the axiom audit on the exact declaration (`#print axioms T` or the project's
audit script) shows nothing beyond the declared foundational baseline
`[invariant]`. Nothing less promotes: not a clean-looking file, not a
passing CI badge on a different commit, not an agent's report that it
compiled. A toolchain or library bump is an epoch change; after a bump, the
re-build of previously proved statements is the bridge, and a proof that no
longer compiles under the new pin is a reversal and a review trigger, never
a quiet fix.

**6 — Program source documents first (standing rule 0).** A published fact is
never a discovery `[invariant]`. The program's own papers, theorem-status
documents, module manifests and formalization are the organiser
documentation of this domain: extract each declared fact — what is proved,
what is explicitly open, the exact open statement, the declared proof
boundary, the toolchain pins — into `AGENTS.md` with a citation to the
source file; an uncited declaration is `[assumed]` and flagged. The
literature meets the same standard: a known theorem is cited, not
rediscovered, and a known **barrier** is a declared fact an attack must
address, not a surprise re-derived mid-attempt. Contradictions are
CONFLICTED with a resolution owner. This is a standing watch: a new paper
version, sibling repo, or upstream change touching used lemmas is a review
event.

**7 — Channels carry declared, scoped authority.** Four channels, each
declaring in `AGENTS.md`, per predicate it bears on, a policy object —
`may_promote`, `promotion_rule`, `may_close`, `closure_rule`, `rationale`:

- **kernel** — the only channel with `may_promote: true`, under law 5. It
  may also close: a kernel-checked disproof is a closure of the strongest
  kind.
- **numerics** — `may_promote: false`, always and unconditionally. It may
  **close** conjectured auxiliary statements: an exact counterexample
  closes a universally-quantified candidate outright; a falsified
  asymptotic closes at `implementation` strength only, because finite-range
  behaviour of arithmetic quantities is a known liar. Every numeric read
  declares its precision, range, and arithmetic model (exact integer vs
  float) `[invariant]`; a float-derived "counterexample" to an exact
  statement is UNVERIFIED until reproduced exactly.
- **informal argument** (drafts, sketches, agent reasoning chains) —
  generates candidates and decompositions; promotes nothing, closes
  nothing. Its output enters the record UNVERIFIED and stays so until the
  kernel or a reviewer confirms each load-bearing step.
- **literature** — the analogue shelf for the target. It promotes nothing;
  it may close a node only via a *cited, checked* impossibility or barrier
  whose applicability a reviewer confirms.

The source OS's `generalisation_design` object — observation unit,
resampling unit, effective n, leakage keys, uncertainty protocol — is
**deliberately collapsed**, and the dead schema is not dragged along: the
kernel is exact, so there are no sampling units, no generalisation gap, no
confidence intervals over proof-checking. Its one surviving fragment is the
numerics channel's range-and-precision declaration, because *it*
extrapolates and the kernel does not.

**8 — Closures are typed, scoped, and assayed.** Every closure carries a
type and a scope line — *under \<formulation\>, attacked with \<technique\>,
at \<budget\>* — the narrowest claim the evidence supports. The two live
types, sharpened for proof search:

- **`implementation`** — "this tactic, this formalization route, this
  estimate chain failed here." Reopens on a stated condition. The default
  verdict for every failed attempt, however discouraging the failure felt.
- **`class`** — "this approach cannot work, for a stated reason." The
  reason must be **checkable or reviewed**: a kernel-checked disproof, an
  exact counterexample, a cited barrier theorem whose hypotheses a reviewer
  has confirmed apply, or a deductive argument recorded in full. "It seems
  hopeless" is not a reason; "the technique is averaged and the target is
  pinned, and here is the exact statement of the gap" is. Known barriers
  belong on class nodes in `IDEAS.md` as **declared obstacles**: an attack
  under such a node states, at declaration time, how it addresses or evades
  the obstacle, or its widest possible closure is `implementation`.

The third source type, `redundant-with-current-incumbent`, survives
narrowed: a lemma made redundant by a stronger proved lemma auto-expires as
a target but stays retained (law 9). A closed branch is never a deleted
branch (source R10).

**9 — Dual status; retention is the default.** `deployment_status` (is this
statement proved / this approach the leading one?) and `candidate_status`
(is this object still useful inside something later?) are different
verdicts, and `deployment-closed` never implies `candidate-rejected`
`[invariant]`. A failed proof attempt routinely leaves behind compiling
sublemmas, definitions, numeric tables and counterexample generators;
retain the record and the cheapest aligned artifact for everything that
reached a verdict — discarding requires a recorded reason `[policy]`. The
measured failure mode is deletion, not hoarding (source R13): partial
formalizations are exactly what a later synthesis recombines.

**10 — A conditional result names its hypotheses; a strength ladder brackets
the target.** The proof-search analogue of the ceiling estimate is the
**bracket**: what is provable under weaker demands (a weaker bound, a
special case, an added hypothesis) and what known barrier blocks the
stronger form. Maintain the ladder explicitly in `IDEAS.md`: the weakest
statement whose proof would still be progress, the target, and the stronger
statements known out of reach, each with its status. The weakest-rung
result is this domain's trivial entrant: machinery that demonstrably closes
end-to-end at lower strength proves the pipeline and isolates the
difficulty. A conditional result is titled with its hypothesis —
`theorem-T-given-H`, never `theorem-T` `[policy]` — and closing a
conditional route never closes the unconditional target (source R15).

**11 — Release discipline.** There is no leaderboard and no submission slot;
what replaces the endgame is the moment a claim leaves the repo — a
preprint, a message to a collaborator, a public README line. A claimed
theorem ships **only** with its kernel evidence recorded: the exact repo
commit, toolchain and library pins, the build command and its green result,
and the axiom audit output on the exact released statements `[invariant]`.
Drafts and preprints cite the exact commit they were built against. The
release enumeration is generated from the record files, never recalled from
memory (source R16). A README asserting more than the kernel checked is the
preamble's failure mode with the program's public credibility attached.

**12 — Compute in pools; throughput first; attention budgeted.** Split
effort into exploration (new angles, first contacts, analogue prototypes),
scaling (carrying the leading angle to full formalization), and evaluation
(builds, audits, numeric verification). The exploration floor — default 25%
`[policy]` — is protected: an early highest-EV estimate may not consume it.
If the build or the numeric harness will run more than a few dozen times,
make it fast before making it deep (source R17). Long builds and sweeps run
detached and durable, preserving terminal evidence. Agent attention is a
budgeted resource: wake on decision events plus a bounded heartbeat, one
batched turn per wakeup — never poll.

**13 — Adversarial review at checkpoints; generation stays blind.** Blocking
triggers — first attempt under a new angle above the budget threshold,
class closures (no threshold at all — source R3), promotion of any released
statement, reversals under a toolchain bump, channel-policy or
declared-fact changes — admit no progress without a review or a recorded
waiver `[policy]`. Separated decision rights on first contact: the
implementer proposes the attempt's gate; someone else approves the budget
and closure scope. Idea generation is staged-blind: the pass-1 packet is
**committed before dispatch** and carries the problem statement only,
because a panel shown the incumbent returns variations on the incumbent.
Reviews use the fixed anti-sycophancy contract and are recorded as `review`
records. One extra tooth here: a reviewer confirming an informal step is an
UNVERIFIED→reviewed transition, recorded per step, and "the reviewer found
no error" is weaker evidence than "the kernel checked it" — the record
never conflates the two.

## The record system

**One directory per decision-bearing record: `results/NN/`, holding `NN.md`.**
That file is the whole ceremony for light kinds; experiments add the frozen
declaration below. Everything else in the directory — Lean stubs, numeric
outputs, build logs — is written by the project's own code and never
hand-edited. `NN` is the next integer after the highest directory under
`results/` `[invariant]`: one namespace for every kind, no parallel
numbering for "probes" (source R4).

**Frontmatter, every kind.** `id`, `kind`, `status`, `one_line`, and where
applicable `class` (the `IDEAS.md` node) and `parent`. A `diagnostic` adds
its producer and machine-readable outputs, and owes nothing else. A
`migration` records an adoption or format cutover. Keys are prose — no
schema file. **Frontmatter is the live summary**: `status` and `one_line`
are updated when the verdict lands; the frozen declaration below never
changes. Status vocabulary `[reference]`: `declared → launched → done |
failed`, then `closed | retained | legacy` as judgment settles.

**The canonical specimen.** Every record file has this shape and no other:

```markdown
---
id: 007
kind: experiment
status: launched
one_line: bilinear route to the survivor bound via conductor pairing
class: bilinear-offdiagonal
parent: 003
---
## Declaration (frozen at launch commit)
target: the exact statement attacked — ideally the Lean signature verbatim;
  where not yet stated in Lean, say so and freeze the prose statement
approach: the technique family and the specific plan of attack, 3-10 lines
analogue: where this technique comes from, with citation;
  `analogue-unverified` if the relevance is conjectured
obstacles_addressed: how this attempt addresses or evades each declared
  obstacle on the class node
decision_rule: what each outcome causes — explicitly including what a
  failure would close (nothing? this formulation? this angle?) at what
  type and scope
promotion_gate: kernel evidence per law 5 on the named target
viability_gate: the observable that says keep going
budget: agent-hours / compute / calendar bound for this attempt
## Gate revisions
(none)
## Run
(evidence pointers: commits, build logs, axiom-audit output, numeric
artifacts with range and precision, where the Lean sources live)
## Verdict
(appended after the run: deployment_status, candidate_status, closure_type,
closure_scope, untested_axes, retained_artifacts, reasoning)
```

Non-experiments use the same frontmatter and drop the Declaration/Gate
sections. Write the decision rule first — if you cannot state what each
outcome causes before running, you have a diagnostic: "I will explore this
reformulation and see" is a diagnostic, whatever the file says.

**`declare → commit → run` `[invariant]`.** The commit *is* the freeze.
Commit `results/NN/NN.md` with its declaration before result-bearing work
begins; `git log -p results/NN/` afterwards shows the gate was committed
before any result was recorded against it. This is the entire integrity
mechanism (source R19, R25). An attempt launched before its declaration was
committed is a diagnostic.

**Verdicts are appended, never edits.** The verdict section is written after
the run, below the frozen block. Gate and budget revisions are new dated
lines under `## Gate revisions` — new value, the observation that justified
superseding it — plus a journal decision event, and the old line stays. A
different promotion claim is a new experiment.

**Evidence is committed or pinned.** Small evidence — audit outputs, key
numeric tables — goes in the record directory and into git; large artifacts
are referenced by location plus digest. A kernel claim's evidence is always
reproducible from the named commit; a dangling reference invalidates the
record.

`NN.md` is read on drill-down, never in bulk: keep the journal event short —
a few lines and a pointer — and let the record hold the reasoning.

## Project surfaces

**`AGENTS.md` — thin router plus declared facts.** It routes to this
document and states the project's facts: the target statement(s) and their
provenance; the channels with their policy objects (law 7); the evaluator
identity per repo; repo governance — what may be pushed, what is
local-only, who owns what; the declared obstacles; the strength ladder's
rungs. Any value may be `unknown` with a reason and a resolution owner, and
changing a declared fact or resolving an `unknown` is a journal decision
event. `AGENTS.md` holds no state and no narrative.

**`JOURNAL.md`.** The live block sits at the **top** `[invariant]`, so
appends grow away from it: `head` gives current state, `tail` recent
events. Fields: updated date, phase, target, leading angle, evaluator
health (does the build pass at HEAD?), active constraints **each with an
expiry condition** `[invariant]`, what is blocked, next tasks. Caps
`[policy]`: ~25 lines, ≤5 tasks. Forbidden inside: strategy essays,
completed tasks, attempt summaries, historical rationale — those append
below as events. Below it, every decision that is not a record in its own
right is an explicit `decision` event.

**`IDEAS.md`.** The attack-angle tree, and the only document where
speculation is allowed. Per node: `Status` (`unexplored | active | dormant |
closed-dead | closed-exhausted | promoted`, plus this domain's
`speculative` for angles whose relevance is itself unestablished), `New
leverage` ("another tactic" is not leverage), `Cheapest kill test`,
`Distance` (a node that cannot say how it differs from its siblings gets
merged), `Analogue` (`analogue-unverified` where the mapping is
conjectured), `Declared obstacles`, `Committed`, `See also`. Per branch:
status, the experiments that touched it, `Closure type`, `Why closed`,
`Reopens when`. Maintain a **known-unknowns** section — unplotted
quantities, unread sources, unstated Lean signatures, untested assumptions
— reviewed whenever a branch closes; that is usually where the next angle
is.

**No other standing files.** No `plan.md` (its strategic half is the tree,
its task half is the live block), no maintained dashboard, no state files.
Dashboards are rendered on demand and thrown away; a rendered one shows
every record of every kind and flags missing ones loudly (source R19).

## Reference

### The kernel channel

A green build plus a clean axiom audit at a named commit proves the
statement as written — not the statement as intended. The standing check at
every promotion: **does the formal statement say what the mathematics
means?** Definition drift — a formalized statement subtly weaker than the
paper statement it claims to capture — is the kernel-era failure mode that
compiles. Promotion of any statement bridging to a classical result records
the bridge's exact form: what is proved outright, what is a typed premise
(a hypothesis argument standing for a cited classical theorem), and what
remains open. A typed premise is honest and lawful; an undeclared one is
the failure mode in the preamble.

### The numerics channel

Numerics are diagnostics and falsifiers, never provers. The honest
declaration per read: range, arithmetic model, and what the read can and
cannot distinguish — a near-flat empirical exponent over a handful of
dyadic scales is exactly the signature that misled the constant-one Mertens
conjecture, and every asymptotic read carries that caveat structurally.
Legitimate products: exact counterexamples (closing power), identity
validation, and landscape reconnaissance — where is the sum large, which
terms dominate, does the conjectured decay appear — which seeds the tree
and calibrates viability gates. Preregister numeric kill criteria where
possible: "if the ratio exceeds B before x = 10^7, the conjectured form is
dead at this range" is a declaration worth freezing.

### Informal argument and literature

The informal channel is the generator. Its discipline is labelling, not
suppression — every load-bearing step in a sketch is tagged proved (with
its record), standard (with its citation), or UNVERIFIED, and a sketch
whose tags are all green is a formalization plan, not a proof. The
literature channel runs the analogue search `[policy]` — the highest-value
generation instrument here, as in the source domain (source R5): name what
the target *is* in the vocabulary of neighbouring fields — a large-sieve
inequality, an equidistribution statement, a bilinear form bound, a
maximal-function estimate — retrieve each field's canonical machinery, and
put 3–5 analogue formulations in `IDEAS.md` with honest
`analogue-unverified` marks where the mapping is hoped rather than checked.
Both source campaigns paid for skipping this step; the mathematical version
costs an afternoon of reading and can retire a wrong-basin year.

### The attack tree and closures

`class` closures are almost never empirically earned — a failed attempt is
`implementation` until a stated, checkable reason says otherwise. Barriers
deserve first-class treatment: known obstructions are declared on class
nodes *before* attempts run, so an attempt's declaration must say how it
gets past them — converting the barrier from post-hoc excuse into pre-hoc
filter; an attempt that cannot state its evasion is redirected to a cheaper
node before spending. Concentration in one angle is a review trigger, not a
gate `[policy]`. Robust repeated failure without a nameable reason is a
valid `closed-exhausted` — do not demand a barrier theorem you lack, but
scope the closure to the budget spent.

### First contact and the strength ladder

Until an angle has produced a kernel-checked artifact its viability gate is
**self-referential** — is its own intrinsic progress measure still
improving at the kill point (lemmas stated, sorries burned down, the
estimate chain's weakest link strengthening), and does it beat its own
trivial control (its machinery applied to the weakest ladder rung)?
Leading-angle-relative gates are allocation decisions, legal only once the
new angle has had effort of the same order as the leading angle's own
development spend: a two-hour sketch asked to out-perform a month-old
formalization measures the budget, not the idea (source R12). At every
gate, check that the evidence named is the quantity the gate names — a
compiling *special case* is not the target's gate.

Keep the ladder explicit and current in `IDEAS.md`: weakest rung (the
program's trivial entrant), intermediate rungs (partial exponents, added
hypotheses, special cases), the target, and the known-too-strong rungs
above it, each with its status and establishing record. Rungs are the
program's parity checks: an angle that cannot prove the weakest rung will
not prove the target, and that is a cheap, honest viability gate available
before any deep spend. A conditional result (`target-given-H`) brackets
from above; its value is the reduction it exhibits and the hypothesis it
isolates — record both.

### Release discipline and provenance

Before any claim leaves the repo: build the release enumeration from the
records — every asserted statement mapped to its proving record and commit,
or explicitly labelled open/conjectural in the release text itself. Re-run
the build and the axiom audit fresh at the release commit — not a cached
result, not a remembered green (source R16). The release text's
mathematical-boundary section is the enumeration made prose, and it is
reviewed as a blocking trigger. Cite exact commits in drafts and preprints.
Where a collaborator's public statement outruns the records, that is a
CONFLICTED fact with the collaborator as resolution owner — flag it, do not
silently ratify it. **Tracked ≠ public** — repo visibility and the release
policy are stated facts in `AGENTS.md`, checked against the remote's actual
state rather than guessed (source R19). Where the program spans sibling
repos, each record names the repo *and* commit its evidence lives at; a
cross-repo claim with a dangling half is invalid.

### Multi-agent coordination

The intended operating shape: **one coordinator, several attack agents.**

- The **coordinator** owns `JOURNAL.md`, `IDEAS.md`, allocation across
  angles, and the review calendar. It writes no proofs in anger.
- Each **attack agent** owns exactly one open `experiment` record at a time
  `[policy]`: one declared target, one frozen gate, one budget. Its claims
  enter the shared record only through its record file and journal events,
  and every mathematical claim it reports is **UNVERIFIED until the kernel
  or a reviewer confirms it** `[invariant]` — the coordinator records the
  claim with its label, never launders it into fact by restatement.
- **Blind seeding**: a panel packet is the problem statement, the exact
  target, the declared obstacles, and the strength ladder — **not** the
  coordinator's rankings, the attempt history, or the current leading
  angle. The packet is committed before dispatch.
- **Convergence is a signal, not a vote**: two agents independently
  proposing the same decomposition is worth a journal event, and is still
  UNVERIFIED mathematics. Contested closures escalate to review; the
  coordinator breaks allocation ties, never evidence ties — evidence ties
  are broken by the kernel or not at all.

### Compute and attention

Long builds, cache downloads and wide numeric sweeps run detached with
terminal evidence preserved; smoke-test before a long run; freeze a working
toolchain environment the first time it works. The project writes its own
runner and harness against these obligations: a **runner** refuses to start
result-bearing work unless the declaration is committed, and records the
launch descriptor (source commit, invocation, environment, start/end,
terminal state); a **harness** identifies the evaluator identity per law 5
and **fails rather than reports** when the audit script or build diverges
from the declared pins.

### Adversarial review

Constant cross-model review is noise; checkpoint use is the
highest-leverage thing here. **Advisory triggers**: three consecutive
closures with no new angle opened · eight records with no status change ·
three patches at one failing lemma · six of the last ten attempts in one
angle — coalesced, with a cooldown. **Do not review** plumbing,
refactoring, predeclared build matrices, executing a defined gate, cheap
reversible probes, or anything answerable by running the kernel — the
kernel is cheaper and stricter than any reviewer, so never convene a panel
to ask whether a file compiles.

**Anti-sycophancy `[policy]`.** Two models asked "what do you think of this
proof strategy" will ratify it. Fixed output contract: the strongest
refutation of the primary plan; the assumptions most likely false; N attack
angles each naming its leverage; the cheapest kill test for each; each
mapped to the tree as novel / partial duplicate / duplicate; one
recommendation the primary will probably reject; the evidence that would
reverse the adversary's own view. The adversary must not see the primary's
conclusion first. For proof review specifically: attack the *statement*
(does it say what is meant?) and the *unformalized steps* before the tactic
choices — the tactic level is the kernel's job. Score on mechanism novelty
and whether a decision changed — similarly-trained models share blind
spots, so a clean review is weak evidence.

**Recording `[invariant]`.** A `review` record: trigger, blocking or
advisory, both models, the committed packet's path and commit, blindness
stage, refutations, proposal-to-tree mapping, recommendations accepted and
rejected with reasons, decisions changed, experiments spawned, waiver if
any.

## Adopting on an existing project

A project that already has records adopts this OS **going forward**. Legacy
records, papers and repos keep their format, untouched: not rewritten, not
migrated, not "brought into compliance". Never rewrite history — the audit
value of an old record is that it says what it said at the time.

1. Write `AGENTS.md`, `JOURNAL.md` (live block plus a first event) and
   `IDEAS.md`, seeding the tree from what the program's own papers already
   believe — their stated open problems and suggested programs are the
   founding nodes, before any panel adds to them.
2. Commit a `migration` record at the next integer under `results/`,
   stating the adoption date and the first governed record ID.
3. Append a journal decision event naming the adoption, the OS revision
   read, and anything deliberately not adopted.

From that commit forward every rule here applies to records allocated after
the cutover and to nothing before it. Adoption means the conventions are
*practiced*, not that files exist — a repo can carry every named file and
run none of this (source R1); the journal's event stream is the only
evidence of adoption that counts.

## Routing

| Moment | Do |
|---|---|
| First attempt under a new angle | First-contact reference section, above |
| Closing an angle | Closure section + blocking review |
| Toolchain or library bump | Epoch rules in law 5; re-verify; review reversals |
| A claim about to leave the repo | Release discipline section — blocking |
| Challenging or changing a rule | The source OS's `RATIONALE.md`, then a decision event |
| Everything else | this file — the section headings are the index |

The source OS shipped four checklists (day-0, new-class, submission,
endgame); this adaptation folds their content into the reference sections
above. A project may extract its own checklist files as the moments first
occur; a checklist's identity is then its filename, its version the commit
it was read at, and its completion a journal event naming both.

The two optional scripts: `tools/dashboard.py` renders a table from record
frontmatter; `tools/lint.py` reports frontmatter completeness. Neither is
required, neither gates anything, and no rule here depends on either
existing. The manual is what runs; the ceremony that costs twelve surfaces
per experiment is what stops being consulted (source R24).
