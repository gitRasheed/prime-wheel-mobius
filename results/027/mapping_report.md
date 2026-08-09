# Record 027 — adversarial mapping verdict

Status: DONE  
Promotion: none  
Numerics executed: none

Legend: PASS = genuinely avoids wall; PARTIAL = only the bounded reduction passes; CLAIM = required estimate merely asserted; FAIL = covert re-entry or structural error.

## 1. Dedup / clusters

### R — square-hyperbola signed-renewal relabellings

Agents: 0, 2, 3, 4, 7.

Common core:

- Replace `π−Li` by a `Λ`/Stieltjes form.
- Complete the square hyperbola.
- Use `μ*Λ = −μ log`.
- Call the remaining two-parameter edge a signed wedge, arm transpose, Carleson tree, or renewal defect.
- Postulate a spectral gap while retaining cross terms.

Dedup facts:

- Agent 0 and agent 4 give the same truncated convolution identity, with `Λ` versus `Λ−1` normalization.
- Agent 2 takes the difference of the two hyperbola arms.
- Agent 3 repackages the edge as a quotient-descendant energy induction.
- Agent 7 inserts a Mellin deformation before performing the same arm transposition.

This is the reopening condition already isolated by record 025, not a supplied reopening. No agent proves, derives from existing machinery, or even obtains one packet of the required signed contraction.

Covert absolute-value points:

- 0: the required negative endpoint/renewal cross term is simply installed as `SR(α)`.
- 2: the contraction and exponent transfer are asserted through an undefined `E_recur`.
- 3: positive Carleson energy plus a supremum over descendants is an energy-form absolute renewal induction; exact self-similarity is not established.
- 4: TT*/large-sieve control is coefficient-sign blind unless the cross term is explicitly evaluated; it is not.
- 7: `∫ ||D_{y,u}||₂ du` takes absolute values across Mellin deformation packets, and the arm gap itself is only assumed.

### P — canonical principal-mode isolation

Agents: 1, 5.

Common core:

- Unit increments on the canonical square shell satisfy a divisor-type bound.
- Discrete Poincaré controls `V_t−average(V)` at target scale.
- The only hard component is the Cesàro/DC mode.
- Agent 1 expands that mode by largest-prime Buchstab cells.
- Agent 5 expands it by the triangular `μ log` boundary-renewal operator.

The AC reduction is genuine and bounded-effort. The proposed DC spectral gaps are not proved. Agent 1’s square-function replacement also discards cross-packet terms unless its separate gap assertion is supplied.

### D — fixed-window δ/Kuznetsov dispersion

Agents: 6, 9.

Common core:

- Expand the canonical-window Gram form.
- Introduce `dp−eq=h`.
- Apply δ/Jutila decomposition and Kuznetsov or a spectral large sieve.
- Claim that the window lowers conductors.
- Leave the endpoint/Cesàro or `q=1` packet inside a “signed” major arc.

Structural defect:

For
`Ω_H(m,n;X)=#{t<H:max(m,n)≤X−t}`,
one has `Ω_H(m,n;X)=H` throughout the deep rectangle
`m,n≤X−H+1`. Hence the Gram form contains exactly

`H · |Σ_{r≤X−H+1} a_Y(r)|²`.

The window does not localize `m−n` to size `H`. Conductor lowering applies, at best, to the moving-boundary/AC component. The deep rectangle is the DC mode and the `q=1` packet is the original problem.

Hidden absolute-value step: standard Kuznetsov/spectral large-sieve estimates accept arbitrary coefficients and replace the Möbius coefficients by their `ℓ²` norms. Unless the `q=1` and low-frequency terms are evaluated before this step, the proof is unchanged after replacing `μ` by `|μ|`. Neither proposal performs that evaluation.

### E — canonical-square ensemble dispersion

Agent: 8.

Distinct leverage:

- Adds an average over the canonical parameter `y`, not generic `x`.
- Every pin retains its certified backward excursion.
- The quadratic law `(y+1)²` creates a real quadratic phase unavailable in a single fixed window.

This is not renewal repackaging. The route remains conditional on exact cancellation of the `h=0` term. For `2k`-th moments, the claim that conductors stay bounded by `lcm(d,e)≤Y²` is incomplete: the full `2k`-fold expansion can generate joint conductors as large as `Y^{O(k)}`. Restrict the first experiment to `k=1`.

## 2. Obstacle audit

### R — signed-renewal relabellings

1. 𝔉-closure: FAIL. Signs survive algebraically, but the needed contraction is simply assumed; TT*, positive energy, packet norms, or `∫||·||` reintroduce absolute control without evaluating the signed cross term.
2. Fiber growth: PASS. No bounded-fiber map is used.
3. Pinned vs averaged: PASS. All identities use the canonical backward window.
4. Modulus magnitude: PASS. No full wheel modulus occurs.
5. Parity: CLAIM. Retaining `μ` names the parity-sensitive object; it does not estimate it.
6. Circularity: PASS at formulation level. No zero bound is explicitly imported.
7. Finite-range deception: PASS. Proposed numerics are falsification-only.
8. Wigert floor jumps: PASS. Windowed energy replaces pointwise smoothness.
9. Renewal edge: FAIL. This is exactly record 025’s two-parameter edge with the missing signed contraction renamed. Agent 3 additionally relies on unproved self-similarity.

### P — principal-mode isolation

1. 𝔉-closure: PARTIAL. AC control is elementary and harmless; DC cancellation remains a claimed signed gap.
2. Fiber growth: PASS. Largest-prime ownership or direct increments avoid the false pair-to-modulus transfer.
3. Pinned vs averaged: PASS.
4. Modulus magnitude: PASS.
5. Parity: CLAIM for the DC mode.
6. Circularity: PASS at formulation level.
7. Finite-range deception: PASS.
8. Wigert floor jumps: PASS. `τ(n)≪ε n^ε` gives a uniform shell bound; no pointwise polylog claim is made.
9. Renewal edge: PARTIAL. The DC/AC isolation is new and valid; the proposed DC contraction remains exactly the missing signed input.

### D — fixed-window spectral dispersion

1. 𝔉-closure: FAIL. Spectral large-sieve norms lose the Möbius signs; the uncomputed zero mode remains.
2. Fiber growth: PASS structurally. No bounded-fiber assertion is made.
3. Pinned vs averaged: PASS.
4. Modulus magnitude: PASS; agent 9’s stronger conductor-lowering claim is unsupported for the DC component.
5. Parity: FAIL. After the spectral norm step, the argument works for arbitrary bounded coefficients.
6. Circularity: PASS at formulation level.
7. Finite-range deception: PASS.
8. Wigert floor jumps: PARTIAL. Shell uniqueness controls moving-boundary prime increments, not the accumulated Gram/DC mode.
9. Renewal edge: PASS. No renewal induction is used.

Independent fatal defect: the endpoint Gram kernel does not impose `|dp−eq|≲H`; the proposed shifted-convolution geometry is absent from the full moment.

### E — canonical-square ensemble

1. 𝔉-closure: CLAIM. The complete `k=1`, `h=0` term has not been evaluated; it may be positive Mertens energy in disguise.
2. Fiber growth: PASS structurally. Actual conductors are retained and averaged.
3. Pinned vs averaged: PASS genuinely.
4. Modulus magnitude: PASS. Conductors are polynomial, although higher moments exceed the claimed `Y²` ceiling.
5. Parity: CLAIM. The zero-mode calculation must show that spectral norms do not erase `μ`.
6. Circularity: PASS at formulation level.
7. Finite-range deception: PASS.
8. Wigert floor jumps: PASS. Ensemble moments tolerate individual spikes.
9. Renewal edge: PASS. No renewal induction is used.

## 3. Kill-test inventory

Ordered by low cost × high decisive information.

1. **D: endpoint-kernel/DC audit — DESK-ONLY.**  
   Expand `Ω_H` into its deep-rectangle and moving-boundary parts. Verify whether any proposed δ-symbol step applies to the deep rectangle. It does not. Then run the exponent ledger on the remaining AC block. Decides agents 6 and 9 before Kuznetsov work.

2. **R: exact zero-mode and sign-ledger audit — DESK-ONLY.**  
   For each formulation, write the completed arm, rectangle overlap, complementary edge, and Stieltjes/prime-power terms with no suppressed boundary term. Mark the first norm or triangle inequality. Kill if the claimed cancellation has become a norm bound for arbitrary coefficients, or if the residual is merely the original Abel target. Record 025 already kills self-similar and absolute-renewal variants.

3. **P: principal-mode reduction and Mellin symbol — DESK-ONLY first; NUMERIC secondary.**  
   Prove the exact AC bound and triangular formula for `A_q`. Apply the affine-projected DC operator to `u^s`. A multiplier of modulus at least one in a rung-1 strip kills the proposed uniform contraction. Finite singular values may falsify but cannot validate.

4. **E: exact `k=1`, `h=0` Poisson term — DESK-ONLY first; NUMERIC secondary.**  
   Expand the centered ensemble Gram form completely. Kill if the zero term contains an uncancelled positive quantity comparable to `ΣM(n)²`, `|Σμ(n)log n|²`, or a blockwise absolute prime error. Only after this passes should quadratic spectral work be declared. Do not open `k>1` before recording the true conductor growth.

No favorable numerical outcome may advance any cluster.

## 4. Shortlist

Ordered by estimated probability of a bounded-effort provable partial × frontier value.

### 1. E / agent 8 — ADVANCE, restricted to `k=1`

Named partial:

`Canonical Ensemble Amplification and Zero-Mode Identity`.

Deliverables:

- Formalize the exact implication from an ensemble `2k`-moment bound to the dyadic maximum at canonical pins, including both branches of the excursion width.
- Derive the exact centered `k=1` Gram/Poisson identity.
- Isolate the complete `h=0` defect before any spectral norm.

Rung-1 deliverable:

`E₂(Y) ≪ε Y^{4+ε}` implies  
`|S(y,(y+1)²−1)| ≪ε Y^{5/3+ε}=x^{5/6+ε}`.

Reason for rank: the partial is finite and formalizable; the zero-mode calculation decisively tests the only proposal with genuinely new averaging geometry.

### 2. P / agent 5, with agent 1 merged

Named partial:

`Canonical DC/AC Principal-Mode Isolation`.

Deliverables:

- Prove `V_t−V_{t+1}=c_q(X−t)`.
- Prove the finite Poincaré bound and `|c_q(n)|≪τ(n)`.
- Derive the endpoint-correct triangular formula for `A_q`.
- Optionally append agent 1’s exact `a(n)M(min(q−1,⌊u/n⌋))` and largest-prime decompositions.

Rung-1 deliverable:

For any fixed `δ>0`,

`|A_q| ≪ q^{2−2δ}`

together with the elementary AC estimate gives

`|S(q−1,q²−1)| ≪ x^{1−δ+ε}`

for `δ<1/2`.

Reason for rank: highest probability partial, but lower frontier value because record 023/024 already established much of the canonical backward-window increment geometry.

No third angle clears the bar.

## 5. Verdict per agent

- **Agent 0 — KILL.** Exact truncated convolution is valid, but `SR(α)` is the desired signed cancellation restated as an assumption. The proposed negative cross term has no analytic mechanism. Prime-power bookkeeping is salvage only and overlaps record 025.

- **Agent 1 — MERGE-INTO-P.** Preserve the exact `a(n)M(...)`, largest-prime, and increment identities inside agent 5’s principal-mode record. Do not advance the asserted Buchstab spectral gap separately.

- **Agent 2 — KILL.** The antisymmetric wedge does not by itself reconstruct the target; rectangle and symmetric-arm terms require bookkeeping. `E_recur`, the spectral gap, and the claimed exponent flow are unspecified. This is the killed renewal edge in signed language.

- **Agent 3 — KILL.** The quotient-descendant Carleson inequality is a positive-energy renewal induction. Absorption and exact self-similarity are not proved and conflict with record 025’s restricted-edge audit. “Norm on the actual residual” supplies no operator estimate.

- **Agent 4 — KILL.** The displayed hyperbola identity is valid, but algebraic completion does not cancel the residual zero mode. TT*/large sieve becomes sign-blind unless the `F–B` cross term is evaluated; it is not. Repackages the record-025 reopening condition.

- **Agent 5 — ADVANCE, PARTIAL ONLY.** Advance the exact DC/AC isolation. Do not record the signed renewal contraction as leverage; it remains the known missing input.

- **Agent 6 — KILL.** The endpoint Gram kernel does not create a short shifted convolution, and ordinary Kuznetsov large-sieve bounds erase the Möbius signs. Square-shell uniqueness applies only to increments, not the DC mode.

- **Agent 7 — KILL.** Cleanest arm-transpose identity in cluster R, but no contraction estimate follows. The integral of `L²` norms introduces another absolute packet step. Exact deformation and prime-power identities do not justify a separate experiment over the record-025 salvage.

- **Agent 8 — ADVANCE, `k=1` GATE ONLY.** The extra canonical-square average is genuine new leverage. Advance the amplification lemma and exact zero-mode audit; do not advance the claimed full moment family or its `Y²` conductor accounting.

- **Agent 9 — KILL.** Conductor lowering covers only the moving boundary, while the `q=1` packet contains the unaltered DC problem. Subsequent bilinear large-sieve bounds are sign-blind. The proposal explicitly names the fatal packet but does not estimate it.

Final count:

- ADVANCE: 2
- MERGE: 1
- KILL: 7
- New analytic estimate established: 0
- Candidate bounded-effort experiment records: 2

Codex session ID: 019fe85d-88f7-74e1-8abc-6a25d39c49dd
Resume in Codex: codex resume 019fe85d-88f7-74e1-8abc-6a25d39c49dd
