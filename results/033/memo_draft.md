# Memo: correction to our kernel-chain claim, Sec.7 numbers, PNT spec sheet

Re-verified against your current main (through the latest "Research update" commit). Your new commits do not touch the five merged prime-sieve modules, so all statements below hold on today's main.

## 1. Correction

Our blind-panel packets and program summaries shipped the sentence: "a kernel-verified chain reduces RH to one estimate, the Abel face," with "two kernel-equivalent faces; attack either." Our adversarial audit found this false; each fact below is re-checked on your main:

- `primeSieveMoebiusDiscrepancySum` (the Abel face S) occurs in exactly three files: `PrimeSieveAbelIdentity`, `PrimeSieveLipschitzExcursion`, `PrimeSieveBackwardAffineExcursion`. No file containing it also mentions `NonzeroResponseRHScale`, any Mertens-energy predicate, or `RiemannHypothesis`. There is no kernel arrow from any bound on S to RH, and no predicate exists that could serve as the hypothesis of one.
- The Abel identity (`primeSievePNTError_eq_moebiusDiscrepancySum_sub_abelBoundary`) is exact and hypothesis-free, but it carries the boundary term: E(y,x) = S(y,x) − M(⌊x/(y+1)⌋)·R(y). At y ≍ √x both factors are √x-scale objects; controlling M(K)R(y) at x^{1/2+ε} is a second RH-strength obligation, discharged nowhere.
- The domains of the two halves are disjoint. Every collapse/centering theorem carries `hroot : Nat.sqrt x < y` (x < y²); the backward-affine module works only at the pin x₀ = (y+1)²−1 = y²+2y, window [x₀−y, x₀], entirely at or above y². Since Nat.sqrt x₀ = y, `hroot` fails at the pin by one. No (y,x) satisfies both.
- The kernel equivalence that does exist is `NonzeroResponseRHScale` ↔ `ProjectedRenewalQuadraticBounded` ↔ Mertens energy ⇒ RH. None of it mentions the Abel face. "Two kernel-equivalent faces" is withdrawn.

What the kernel does prove, all exact and unchanged by your new commit: the two-way Abel bridge above; the collapse/centering identities under x < y²; the support-insertion identity (ΔS at x+1 = (K+1)(y+1) equals the frozen-support increment plus μ(K+1)·R(y+1)); and the unconditional backward increment bound |S(y,x₀) − S(y,x₀−t)| ≤ C·(t+1) for t ≤ y, with C = 1 + K/log(y+1) and the quotient exactly stable on the window. Identities and one Lipschitz bound — no estimate on S, E, or R.

If our "one estimate / two faces" sentence entered your own planning, please discard it.

## 2. Sec.7 note (numbers only)

Your previous route text fitted the termwise triangle bound Σ_d|E_d| at exponent 0.678 and the signed |E^rec| at 0.51, reading the gap as square-root cancellation across the d-fibres with required saving about x^0.18. On those point estimates the measured saving is x^{0.678−0.51} = x^{0.168} = D^{0.336} (D ≈ x^{1/2}), against full √D = D^{0.5} = x^{0.25}; 0.168 also sits below the stated 0.18. Your latest revision removed that paragraph; the numbers refer to the earlier text. Our replication of the fits on our own stack: [STATUS — fill in before sending].

## 3. PNT spec sheet

What our merged, kernel-green modules can feed your native-PNT architecture, tiered by what each needs.

**Tier 1 — exact identities, no inputs.** (a) Abel bridge E = S − M(K)R(y), all y, x; interface note: our R is π − Li, your `nativePNTError` is ψ(N) − N, so a partial-summation shim is needed between them. (b) Collapse/centering rewrites under x < y²; coordinates only — the corrected remainder T satisfies T = M + E, so bounding one face never bounds M. (c) Support insertion: between insertions the quotient support is frozen and increments of S are pure R-increments — exact bookkeeping for your reciprocal-family short-interval framing.

**Tier 2 — unconditional bounds, honest constants.** Backward Lipschitz at the pin with C = 1 + K/log(y+1) ≈ 2√x/log x at y ≍ √x. The excursion window at pinned height H is W = min(y+1, ⌊H/2C⌋); at H = x^{1/2+ε} that is ≍ x^ε·log x, not ≍ √x — our earlier W ≍ √x headline was wrong. The moment theorem transfers pinned heights to mean squares over that short window only.

**Tier 3 — conditional templates.** Given any two of {M(K) bound, R(y) bound, E(y,x) bound}, the bridge yields the third at the summed scale. Your affine-envelope inputs (ψ-error slope arbitrarily small, M(x) = o(x)) feed this at o-scale only: M(K)R(y) stays far above x^{1/2+ε}, consistent with your frontier bookkeeping in route sec.9.

**Not provided:** no upper bound on R(t) at any power scale is kernel-proved in our modules; the boundary term is an obligation, not a resource; nothing connects a bound on S to H_{k,n} or RH.
