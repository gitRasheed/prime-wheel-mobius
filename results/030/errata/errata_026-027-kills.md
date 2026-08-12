# Errata draft — target "026-027-kills" (records 026/027 vs audit 029)

Certifier: independent re-derivation pass, 2026-08-12. All verdicts below were
re-derived from the source files; numeric spot-checks live in this scratchpad
directory (Omega_H brute force, Gram/variance decompositions, E_u sum
asymptotics, J_W Mellin-kernel decay). No repo file was modified.

Bottom line: all seven KILL verdicts and both ADVANCE verdicts in 027 stand.
Every correction below is to recorded GROUNDS, not verdicts. Since kill grounds
freeze reopen conditions, the grounds should be repaired as follows.

---

## Erratum 1 (audit finding 1, major — CONFIRMED): the cluster-D "structural
## defect" is real but is not a coercive/fatal block; substitute the exact mean
## split

Facts re-verified: Omega_H(m,n;X) = #{0<=t<H : max(m,n) <= X-t}
= max(0, min(H, X-max(m,n)+1)) (brute-forced over 2000 random cases). It
depends on m,n only through max(m,n), so the endpoint average gives ZERO
localization of m-n; and the deep-deep block of the Gram form is exactly
H|A_0|^2 with A_0 = Sum_{r<=X-H+1} a_Y(r). Both statements in the record are
exact. What does NOT follow is that this block is a fatal positive obstruction:
writing S(X-t) = A_0 + T_t, the Gram form is
H|A_0|^2 + 2Re(conj(A_0) Sum_t T_t) + Sum_t |T_t|^2, and the cross term can
cancel the first block (in random trials the deep block *exceeded* the full
Gram form). The airtight coercive statement uses the window MEAN, not the deep
prefix: with A_q = W^{-1} Sum_{t<W} V_t,

    Sum_{t<W} |V_t|^2 = W|A_q|^2 + Sum_{t<W} |V_t - A_q|^2   (exact, both terms >= 0),

so any windowed mean-square bound genuinely forces the DC bound |A_q| and the
un-supplied DC estimate is unavoidable. That is the correct kill ground.

### mapping_report.md, section 1, cluster D — WRONG TEXT:

> Structural defect:
>
> For `Ω_H(m,n;X)=#{t<H:max(m,n)≤X−t}`, one has `Ω_H(m,n;X)=H` throughout the
> deep rectangle `m,n≤X−H+1`. Hence the Gram form contains exactly
>
> `H · |Σ_{r≤X−H+1} a_Y(r)|²`.
>
> The window does not localize `m−n` to size `H`. Conductor lowering applies,
> at best, to the moving-boundary/AC component. The deep rectangle is the DC
> mode and the `q=1` packet is the original problem.

### REPLACEMENT:

> Structural facts (desk-exact): `Ω_H(m,n;X)=#{t<H:max(m,n)≤X−t}
> = max(0, min(H, X−max(m,n)+1))` depends on `m,n` only through `max(m,n)`,
> so the endpoint average provides no localization of `m−n` whatsoever; only
> the boundary–boundary block (both indices in `(X−H+1,X]`) automatically has
> `|m−n|<H`. The deep–deep block of the Gram form is exactly
> `H·|Σ_{r≤X−H+1} a_Y(r)|²`, but that block is cancellable against
> deep–boundary cross terms and is therefore an unsupplied estimate, not a
> contradiction. The coercive formulation is the exact mean split: with
> `A_q = W^{−1}Σ_{t<W}V_t`,
> `Σ_{t<W}|V_t|² = W|A_q|² + Σ_{t<W}|V_t−A_q|²`, both summands nonnegative,
> so the windowed mean-square target forces the DC bound `|A_q| ≪ x^{1/2+ε}`,
> which neither proposal estimates. The `q=1`/DC packet is the original
> problem.

### 027.md, Results — WRONG TEXT:

> **D** (fixed-window δ/Kuznetsov dispersion; agents 6,9) — KILLED by a
> desk-exact structural defect: the window kernel Ω_H is constant (= H)
> on the deep rectangle, so the Gram form contains H·|Σ_{r≤X−H+1}a(r)|²
> — the window never localizes m−n, and spectral large-sieve steps are
> sign-blind.

### REPLACEMENT:

> **D** (fixed-window δ/Kuznetsov dispersion; agents 6,9) — KILLED. Desk-exact
> kernel fact: Ω_H depends only on max(m,n), so the endpoint window never
> localizes m−n (this defeats agent 9's short-shift/conductor-lowering
> geometry). By the exact split Σ|V_t|² = W|A_q|² + Σ|V_t−A_q|², the
> mean-square target forces the DC bound |A_q| ≪ x^{1/2+ε}, which neither
> proposal evaluates before invoking coefficient-uniform (sign-blind)
> spectral large-sieve tools.

---

## Erratum 2 (audit finding 2, major — CONFIRMED): agent 6's kill ground is
## misattributed; the no-short-shift objection belongs to agent 9 alone

Re-verified from agent6.json: agent 6's target estimate carries the exact
kernel `Ω_H(dp,eq;X)` explicitly (no claim that `|dp−eq| ≲ H`), and its
mechanism states "The constant/Cesàro mode must be included in the same signed
dispersion calculation, not estimated separately." The conductor-lowering /
short-shift claim is agent 9's ("The averaging lowers the relevant
circle-method conductor to q≈√(x/W)=x^{1/4}", agent9.json). The correct,
narrower ground against agent 6: it supplies no pre-spectral signed evaluation
of the zero/low-frequency packet, and its only named tools (Kuznetsov + a
spectral large sieve) are coefficient-uniform, hence cannot reach a target
that fails under mu -> |mu|. Agent 6's own kill test ("kill ... if isolating
the zero mode forces |μ| or |ν| before spectral summation") mandates exactly
this check, so KILL stands.

### mapping_report.md, section 5 — WRONG TEXT:

> - **Agent 6 — KILL.** The endpoint Gram kernel does not create a short
>   shifted convolution, and ordinary Kuznetsov large-sieve bounds erase the
>   Möbius signs. Square-shell uniqueness applies only to increments, not the
>   DC mode.

### REPLACEMENT:

> - **Agent 6 — KILL.** Agent 6 keeps the exact kernel Ω_H in its target and
>   never claims short shifts; the defect is narrower: it supplies no
>   pre-spectral signed evaluation of the endpoint/Cesàro (zero-frequency)
>   packet, and its only named tools (Kuznetsov plus a spectral large sieve)
>   are coefficient-uniform, so they cannot prove a bound that fails under
>   μ → |μ|. Its own kill test mandates exactly this check. Square-shell
>   uniqueness applies only to increments, not the DC mode.

### mapping_report.md, section 2, cluster D — WRONG TEXT:

> Independent fatal defect: the endpoint Gram kernel does not impose
> `|dp−eq|≲H`; the proposed shifted-convolution geometry is absent from the
> full moment.

### REPLACEMENT:

> Independent defect against agent 9: the endpoint Gram kernel does not impose
> `|dp−eq|≲H`, so the short shifted-convolution geometry agent 9's conductor
> lowering relies on is absent from the full moment (agent 6 makes no such
> shortness claim; its kernel is retained exactly).

---

## Erratum 3 (audit finding 3, major — CONFIRMED): the D and P rung-2 targets
## are unconditionally equivalent; the record must say so

Re-derived: with V_t = S(y, x0−t), W = q = y+1, A_q = W^{−1}Σ_{t<W}V_t:
(i) exact variance split Σ|V_t|² = W|A_q|² + Σ|V_t−A_q|²;
(ii) exact increment law V_t − V_{t+1} = c_q(X−t), c_q(n)=Σ_{d|n,d<q}μ(d)a(n/d)
(floor difference ⌊(X−t)/d⌋−⌊(X−t−1)/d⌋ = 1_{d | X−t}); |a(m)| bounded gives
|c_q(n)| ≪ τ(n) ≪ n^ε, hence |V_t − A_q| ≪ q^{1+ε} and
W^{−1}Σ|V_t−A_q|² ≪ q^{2+ε} = x^{1+ε} unconditionally (agent 5's own Poincaré
bound). Therefore, unconditionally,

    (1/W) Σ_{t<W} |S(y,x0−t)|² ≪ x^{1+ε}   <=>   |A_q| ≪ q^{1+ε} = x^{1/2+ε}.

Cluster D's rung-2 target and cluster P's DC deliverable are the SAME estimate.
The D-kill / P-advance split is a verdict about METHOD (sign-blind spectral
norms vs exact isolation), not about target. This equivalence is a free,
elementary, Lean-formalizable program result that 027 came one line short of.

### 027.md, Results — ADD after the cluster P sentence ("**P** ... the DC
### contraction is the known missing input."):

> Program result (elementary, unconditional, Lean candidate): by the exact
> split Σ_{t<W}|V_t|² = W|A_q|² + Σ|V_t−A_q|² and agent 5's unconditional
> Poincaré bound W^{−1}Σ|V_t−A_q|² ≪ q^{2+ε} = x^{1+ε}, the cluster-D rung-2
> target (1/W)Σ|S|² ≪ x^{1+ε} is EQUIVALENT to the cluster-P DC deliverable
> |A_q| ≪ q^{1+ε}. D was killed and P advanced on method, not on target.

### mapping_report.md, section 4, item 2 (P) — ADD to Deliverables:

> - Record the equivalence: given the unconditional AC bound, the windowed
>   mean-square target of cluster D and the DC bound |A_q| ≪ q^{1+ε} are the
>   same rung-2 estimate (exact mean split; no hypothesis needed).

---

## Erratum 4 (audit finding 4, minor — CONFIRMED): "covert absolute-value step
## found in every one" is contradicted by the report's own grounds

Re-verified against mapping_report.md's own "Covert absolute-value points" and
agent{0,2,3,4,7}.json: agent 0's recorded ground is that the signed
cancellation is installed as the assumption SR(α) (assumption of conclusion,
not a sign-discarding step); agent 2's is an under-defined E_recur; agent 3's
is unproved self-similarity plus positive-energy renewal (correct as
recorded); agent 4's TT*/large-sieve step is sign-blind but is deployed after
an algebraic zero-mode cancellation the proposal treats as complete — the
operative defect is again assumption of the F–B cross-term cancellation;
agent 7 does contain a genuine absolute step (the L² norm inside the
u-integral) plus a divergent normalization (Erratum 5). So an absolute-value
step is NOT found in every one; freezing "kill an absolute-value step" as
cluster R's reopen condition is wrong — the reopen condition is "supply the
signed contraction."

### 027.md, Results — WRONG TEXT:

> **R** (signed-renewal relabellings; agents 0,2,3,4,7)
> — all KILLED: each restates record 025's reopening condition as an
> assumption, with a covert absolute-value step found in every one.

### REPLACEMENT:

> **R** (signed-renewal relabellings; agents 0,2,3,4,7) — all KILLED: each
> restates record 025's reopening condition (the missing signed contraction)
> as an assumption. Per-agent grounds: 0 installs it as the assumption SR(α);
> 2 asserts it through an under-defined E_recur; 3 relies on unproved
> self-similarity inside a positive-energy renewal induction; 4 assumes the
> zero-mode/cross-term cancellation is complete before a sign-blind TT* step;
> 7 takes a genuine absolute step (norms inside the u-integral) on top of a
> divergent normalization. Reopen condition: supply the signed contraction —
> not merely remove an absolute-value step.

---

## Erratum 5 (audit finding 5, minor — CONFIRMED; flagged as load-bearing for
## the frozen kill ground): agent 7's target estimate is false as written, not
## merely lossy

Re-derived and numerically checked: E_u(m) = Λ(m)m^{−u} − ∫_{m−1}^m v^{−u}dv.
The m=1 term is −∫_0^1 v^{−u}dv, divergent for u ≥ 1, so D_{y,u} is undefined
there. After excising m=1, Σ_{2≤m≤N} E_u(m) → −1/(u−1) as u → ∞, uniformly in
N ≥ 2 (numerics: at u=10 the sum is −0.110415 for N=10,100,1000 vs
−1/9 = −0.111; at u=20, −0.052631 vs −0.052632). Hence
D_{y,u}(X) = Σ_{d≤y}μ(d)Σ_{m≤X/d}E_u(m) ≈ −M(y)/(u−1) uniformly across the
window, and ∫_0^∞ ||D_{y,u}||_{ℓ²(I_y)} du diverges logarithmically whenever
M(y) ≠ 0. Agent 7's target ∫_0^∞||D_{y,u}||_{ℓ²(I_y)}du ≪ y^{3/2+ε} is
therefore FALSE as written (agent 7 flags "finitely many endpoint conventions"
but never fixes them). This strengthens the kill; verdict unchanged.

### mapping_report.md, section 5 — WRONG TEXT (incomplete ground):

> - **Agent 7 — KILL.** Cleanest arm-transpose identity in cluster R, but no
>   contraction estimate follows. The integral of `L²` norms introduces
>   another absolute packet step.

### REPLACEMENT:

> - **Agent 7 — KILL.** Cleanest arm-transpose identity in cluster R, but no
>   contraction estimate follows, and the target estimate is false as
>   written: E_u(1) diverges for u≥1, and after excising m=1 the tail
>   Σ_{m≤N}E_u(m) ~ −1/(u−1) uniformly in N makes D_{y,u} ~ −M(y)/(u−1), so
>   ∫₀^∞||D_{y,u}||₂ du diverges logarithmically whenever M(y)≠0. The
>   integral of L² norms additionally introduces an absolute packet step.

---

## Erratum 6 (audit finding 6, minor — PARTIAL): agent 9's actual error is
## shift-average vs endpoint-average conflation; the record's "AC component"
## scoping is defensible but under-specified

What the audit gets right (re-verified): agent 9 conflates averaging over the
SHIFT h in dn−em=h (what Jutila's short-modulus method exploits) with
averaging over the ENDPOINT x0−t of a sharp partial sum. The endpoint average
acts in the Mellin/radial coordinate: it inserts
J_W(z) = W^{−1}Σ_{t<W}(1−t/X)^z with |J_W(z)| ≪ min(1, X/(W|Im z|))
(numerically verified: |J_W| stays ≈1 until |Im z| ≈ X/W, then decays like
X/(W|Im z|)). So the endpoint average localizes the Mellin frequency only to
|Im z| ≲ X/W = √x, which is exactly critical against balanced
Dirichlet-polynomial length √x — zero surplus. Agent 9's claimed conductor
lowering Q ≈ √(x/W) = x^{1/4} is unsupported for the full moment.

Where the audit overreaches: the record's sentence "Conductor lowering
applies, at best, to the moving-boundary/AC component" is a defensible upper
scoping, since the boundary×boundary block (both indices in (X−H+1,X]) does
carry genuine |m−n| < H localization; it is not a mislocation, but it is
under-specified — the deep×boundary cross blocks carry no localization, and
the record never names the actual conflation.

### mapping_report.md, section 1, cluster D — the sentence

> Conductor lowering applies, at best, to the moving-boundary/AC component.

### should be EXTENDED to:

> Conductor lowering applies, at best, to the boundary×boundary block (both
> indices in `(X−H+1,X]`), where `|m−n|<H` holds automatically; deep×boundary
> cross blocks carry no localization. Agent 9's Q ≈ √(x/W) = x^{1/4} rests on
> conflating an average over the shift h (Jutila) with an average over the
> endpoint x0−t: the endpoint average acts in the Mellin coordinate, inserting
> J_W(z) with |J_W(z)| ≪ min(1, X/(W|Im z|)), i.e. bandwidth X/W = √x —
> exactly critical at balanced length √x, so no surplus is available for the
> full moment.

---

## Not errata (audit points examined and bounded)

- All seven KILL and two ADVANCE verdicts in 027 are unaffected by every item
  above; only grounds change.
- The audit's rejected candidate error (that a fixed-pin windowed mean square
  is not a genuine relaxation) was independently checked and is correctly
  rejected: the mean square is strictly weaker than the pointwise target, and
  the packet's "averaged attacks are sanctioned coordinates" stands.
- Audit finding 4's relabel of agent 4 ("wrongly believes the cancellation is
  complete") slightly overstates: agent 4's target and kill test do name the
  F–B cross-term evaluation as open; the operative defect is still assumption
  of the conclusion, so the replacement text in Erratum 4 stands.
