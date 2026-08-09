I recomputed the proof end to end (including the F_K contour, both Perron ledgers, the exponent arithmetic, and the constant normalization against the literature). Findings below.

---

# Blocking adversarial review — results/019, `theoremA_proof.md`

## 0. What I verified as CORRECT (so the record knows what was actually checked)

Before the findings, the load-bearing recomputations that **passed**:

- **Lemma 3.1 (the completion lemma), in full.** Inner Perron: with `b = αΔ + 1/log U`, `Re(z+b) = 1 + 1/log U > 1` ✓; error `Σ_n n^{−σ}(U/n)^b min(1, 1/(T|log(U/n)|))` with `n^{−σ}(U/n)^b = U^b n^{−1−1/log U}`. Middle range `U/2 ≤ n ≤ 2U`: `≍ U^{b−1}·Σ_j min(1, U/(T(j+½))) ≍ U^{b−1}(U/T)(1+log T) = U^b log(2T)/T`; outer ranges `≪ U^b log U /T` using `Σ_{n>U} n^{−1−1/log U} ≍ e^{−1}log U`. Since `U^b = e·U^{αΔ}`, (3.9) holds (with `log 2T ≤ log 2U`, i.e. slightly lossy but valid).
- **The doubled-height geometry (3.10)–(3.11)** — the exact point the K1 audit flagged as the risk. `q = z+w` with `Re w ∈ [−η,b]`, `Im w ∈ [−T,T]`, `|t| ≤ T` gives `|Im q| ≤ 2T` and `Re q ≥ σ−η = 1−αΔ−(1−α)Δ = 1−Δ` exactly. With `Δ = a/D(2T)` the whole rectangle sits in **one** region (1.1) at `V = 2T`. The K1 counterexample (local width `δ(t)`) is genuinely defused. The `(1−α)^{−A}` factor that K1 carried in `B_T` is correctly *dropped* here, because the margin now comes from `a < a_*` rather than from `(1−α)Δ` — that is an improvement on the audited route, not an error.
- Residue (3.12) `= 1/ζ(z)` ✓; `z+w = 1` harmless (`1/ζ` has a zero) ✓, including the degenerate case `|t| = T` where `w = 1−z` lands on a horizontal side.
- (3.13): `∫_{−T}^{T} dv/√(η²+v²) = 2 arcsinh(T/η) ≪ log(2+T/η)` ✓. (3.14): `∫_{−η}^{b} U^u du ≤ U^b/log U` ✓.
- **Frullani** (2.7): `v = e^w` gives `∫_0^∞ (e^{−(s−1)w} − e^{−sw})/w\,dw = log(s/(s−1))` ✓.
- **`L_0 − Li`** (7.4): `L_0' − Li' = −1/(u log u)` ⟹ difference `= −log log u + C` ✓; cost `≪ K log log X` ✓.
- **Floors** (8.1): `⌊X/d⌋ = ⌊N/d⌋` because no integer lies in `(N, N+½]` ✓.
- **`Σ_{d≤K} d^{−u} ≪ K^{max(1−u,0)} log 2K`** (used in (5.7)/(6.2)): `d^{−u} = d^{1−u}/d ≤ K^{1−u}/d` ✓; `X^u K^{1−u} = K(X/K)^u` increasing ✓.
- **The exponent arithmetic (6.5)–(6.8)**, symbolically. With `log T = λΦ(X)`: `loglog T = (3/5+o(1))loglog X`, `D(2T) = λ^{2/3}(3/5)^{1/3}(log X)^{2/5}(loglog X)^{1/5}(1+o(1))`, hence `Δ log X = a(5/3)^{1/3}λ^{−2/3}Φ(X)`. `max_λ min(λ, a(5/3)^{1/3}λ^{−2/3})` is at `λ^{5/3} = a(5/3)^{1/3}`, i.e. `λ = a^{3/5}(5/3)^{1/5} = c(a)` — so (1.4)/(1.6)/(4.4) are right and the choice is optimal for this contour. Then `αΔ log X + η log K = Δ log X·(1+α)/2` ✓ (6.6); `αΔ(log X − log K) + log T = (α/2 + 1)c(a)Φ` ✓ (6.7). Numerical spot-check at `log X = 10^6, a = 1`: `Φ = 2354.7`, `log T = 2608.1`, `D(2T) = 376.8`, `Δ log X = 2654.3` — ratio `1.018`, converging to 1 ✓.
- Assembly (8.5) and the `ε/3 → ε` absorption ✓; `X^{3/4}log X` and `X^{1/2}loglog X` absorbed since `Φ = o(log X)` ✓.
- **Statement match on everything except the constant**: quantifiers, `y ≍ √x`, `K = ⌊x/(y+1)⌋`, `R = π − Li`, the exponent `(log x)^{3/5}(loglog x)^{−1/5}`, `(1−ε)`, `≤` rather than `≪`, and the decomposition `Σμ(d)R(⌊x/d⌋) = (6.9) + (7.3) + (7.5) + (8.4)` — all correct and complete.

Now the findings.

---

## Finding 1 — GAP (borderline SEVERE): `c₀` is the *Ingham-level* constant, ≈ 0.51× the actual Korobov–Vinogradov PNT constant

The boxed theorem says "`c₀` is the Korobov–Vinogradov **PNT constant**". §1 then defines `c₀ := sup_a c(a)`, `c(a) = a^{3/5}(5/3)^{1/5}`. Those are **not** the same number.

Recomputation of what the contour balance yields:

```
c(a) = a^{3/5}(5/3)^{1/5} = 1.107566 · a^{3/5}
```

Recomputation of the actual best-known PNT constant from the same zero-free constant `a` (Pintz's method: `ω(x) = min_{t≥3}{η(t)log x + log t}`, `η(t) = a/D(t)`):

```
h(u) = a·L/(u^{2/3}(log u)^{1/3}) + u,  L = log x, u = log t
h'(u)=0  ⟹  u^{5/3}(log u)^{1/3} = (2/3)aL
       ⟹  f(u_opt) = (3/2)u_opt,  h = (5/2)u_opt
u_opt  = (2/3)^{3/5} a^{3/5} (5/3)^{1/5} Φ(x)
ω(x)   = (5/2)(2/3)^{3/5}(5/3)^{1/5} · a^{3/5} Φ(x) = 2.170983 · a^{3/5} Φ(x)
```

Cross-check against the closed form in the literature, `(5⁶/(2²·3⁴·c³))^{1/5}` with `c = 1/a`: `(15625/324)^{1/5} = 2.17095` — **exact agreement**. Numeric anchor: with the explicit zero-free constant `a = 1/48.1588`, `a^{3/5} = 0.0977905`, so my formula gives `d = 0.21230`, matching the published `d ≥ 0.2123` (which improved the previous best `0.2098`) to four figures. The reviewed proof's `c(a)` at the same `a` is `0.10831`.

So:

```
c₀(proof)  =  1.1076 a_*^{3/5}
c₀(KV PNT) =  2.1710 a_*^{3/5}          ratio = (5/2)(2/3)^{3/5} = 1.9601
```

The proof's `c₀` is **1.96× smaller** than the constant a reader (and the frozen declaration's "`c₀` the Korobov–Vinogradov constant") would take the phrase to mean. The factor is not an artifact of the doubled-height repair — I checked that even a curved contour `σ(t) = 1 − a/D(t)` is still dominated at `t ≈ T` (the zero-count weight `log t` is increasing in `t`), so it too yields `c(a)`. The 1.96 gain is Pintz's, and it requires **zero-density estimates**, which this route cannot use: `E_K` in Lemma 3.1 is a pointwise-in-`t` bound with no density saving available.

**Consequence that must be recorded (this is the sharp edge):** applying the best-known KV PNT termwise and using the triangle inequality gives, since `Φ(√x) = (2^{−3/5}+o(1))Φ(x)`,

```
Σ_{d≤K}|μ(d)R(x/d)| ≪ x log x · exp(−2^{−3/5}·2.1710·a_*^{3/5}Φ(x))
                      = x exp(−(1.4324 − o(1))·a_*^{3/5}Φ(x))
```

versus the theorem's `x exp(−(1.1076 − o(1))a_*^{3/5}Φ(x))`. **The trivial route is stronger by a factor 1.293 in the exponent constant.** The K1 report's comparison ("triangle inequality alone gives `2^{−3/5}c₀`") is only valid if both sides are forced to use the same, suboptimal, `c₀`; with best-known inputs on both sides the sharpening is negative.

**Repair (mandatory, and it is a restatement, not a fix):** delete "the Korobov–Vinogradov PNT constant" from the boxed theorem and write `c₀ := sup{a^{3/5}(5/3)^{1/5} : a` admissible in (1.1)–(1.3)`}`, described as *the constant delivered by the zero-free region alone via the classical (Ingham) contour balance*. The theorem is then true as stated and the record must not claim "full KV constant".

## Finding 2 — GAP: "for some absolute `A`" in (1.2)/(1.3) is false; `A = A(a) → ∞` as `a → a_*`

The proof asserts (1.2)–(1.3) hold "for every fixed `0 < a < a_*`" with "some absolute `A`". The first half is true — I verified it rather than deferring — but `A` is not absolute.

Derivation (Borel–Carathéodory, which is what the cited sources actually require and which the proof does not state): fix `t`, `3 ≤ |t| ≤ V`, `z₀ = 1 + 1/log V + it`, disc radius `R = a_*(1−κ)/D(V)`; the disc is zero-free by (1.1) at height `V+R` (`D(V+R) = D(V)(1+o(1))`). The Vinogradov growth bound gives `|ζ| ≪ t^{B(1−σ)^{3/2}}(log t)^{2/3} ≪ (log V)^{2/3}` throughout the disc, since `(1−σ)^{3/2} ≍ D(V)^{−3/2}` makes `t^{B(1−σ)^{3/2}} = exp(B/(loglog t)^{1/2}) ≍ 1` — note this holds for *any* width constant, so `M := max Re log ζ ≪ loglog V`; and `−log|ζ(z₀)| ≪ loglog V` by the classical `3+4cos+cos2` bound. Reaching `σ = 1 − a/D(V)` needs `r ≥ a/D(V)`, so

```
|log ζ(s) − log ζ(z₀)| ≤ (2r/(R−r))(M − Re log ζ(z₀)) ≪ (a/(a_*−a))·loglog V
⟹  1/|ζ(s)| ≪ (log V)^{C·a/(a_*−a)}
```

and by Cauchy on `log ζ`, `ζ'/ζ ≪ (a_*−a)^{-1}D(V)loglog V ≪ (log V)^{A(a)}`.

So (1.2)/(1.3) are genuine, but `A(a) = Θ(a/(a_*−a))` blows up as `a ↑ a_*`. Downstream this means `A₁,…,A₆`, `B_T`, and every implied constant depend on `ε` (through the choice (1.7) of `a`). The proof's conclusions are stated as `≪_ε`, so nothing breaks — the order of quantifiers (`ε` → `a` → `A(a)` → `x₀`) is sound. **Repair: one sentence replacing "some absolute `A`" with "`A = A(a)`, and all implied constants below depend on `a`, hence on `ε`."**

## Finding 3 — GAP (citation): the "package" (1.1)–(1.3) is not quoted in the cited form

- **Iwaniec–Kowalski Ch. 8 is "Exponential sums."** Corollary 8.28 / Theorem 8.29 can at best be the Vinogradov–Korobov *growth* bound for `ζ`; they are not a zero-free region plus `1/ζ`, `ζ'/ζ` bounds. The sentence "This package follows from the Vinogradov–Korobov estimate and the standard zero-detection argument: [IK] Cor. 8.28 and Thm 8.29" conflates the input with the package.
- **Titchmarsh Ch. III (Thms 3.10/3.11, pp. 58–60)** is the de la Vallée Poussin region in the book's own organization; the Vinogradov strengthening lives in Ch. VI (whence the "(6.19.2)" and pp. 134–135 pointers) and in Heath-Brown's end-notes. The combination is legitimate in substance but is a derivation, not a quotation — and, critically, the textbook statements give the `1/ζ`/`ζ'/ζ` bounds for *some* constant, not for every `a < a_*`. That step is exactly Finding 2's Borel–Carathéodory argument and must appear in the proof.
- **Ford, Theorem 1** is correctly cited, but supplies only the zero-free region — not (1.2)/(1.3).
- **Montgomery–Vaughan Corollary 5.3** for (2.1) is the right citation and the right form.

**Repair:** state (1.2)/(1.3) as a lemma with the Borel–Carathéodory proof sketched (four lines, given above), citing Ford Thm 1 for (1.1) and the VK growth bound for `M`.

## Finding 4 — COSMETIC: dropped `1/T` in a Lemma 2.1 display

Line 168–172: "For `m < X/2` or `m > 2X` … `X^c Σ_m log(2m)/m^c ≪ X(log X)²`". The factor `min(1, 1/(T|log(X/m)|)) ≪ 1/T` is omitted from the display. Recomputation: `Σ_m log(2m)m^{−1−1/log X} ≍ (log X)²`, `X^c = eX`, times `1/T` ⟹ `≪ X(log X)²/T`, which is what (2.2) claims. Conclusion unaffected.

## Finding 5 — COSMETIC: middle-range harmonic factors are `log(2T)`, stated as `log(2U)`/`log X`

In (3.9) and in Lemma 2.2 the true factor is `log(2T)` (the sum/integral over `|U−n| > U/T` has range ratio `T`, not `U`). Since `T ≤ K < U`, the stated bounds are valid but lossy. No effect.

## Finding 6 — COSMETIC: `x₀` also depends on the implied constants in `y ≍ √x`

`log K = ½log X + O(1)` (4.5) and (7.3) carry the `≍`-constants, which enter the `o(1)` in (6.6)/(6.7) and the `X^{3/4}` cost. The theorem writes `x₀(ε)`; it should be `x₀(ε, C)` where `C` is the `≍` constant. (Uniformity does hold for each fixed `C`.)

## Finding 7 — COSMETIC: §5 is decorative for Theorem A, and (5.8) is asserted

The declared route element "exact `s=1` residue cancellation" is delivered in §5 for `A_ψ` — the residue computation (5.3) `= X F_K(1)` is correct — but `A_ψ` is never used in §§6–8. For Theorem A the `s=1` handling is instead the removable singularity of `H(s) = log(ζ(s)(s−1)/s)`, which I verified is analytic and single-valued on the (simply connected, zero-free, `s ≠ 0`) union of `Re s > 1` with the shift rectangle. (5.8) itself is stated with "the same estimates used below therefore give" — i.e. asserted, in a section whose whole point was to be explicit. Not load-bearing; flagging because the declaration forbade "clearly" at truncation terms.

## Finding 8 — the self-declared weakest step is under-declared

The proof's "Weakest step" section frames the `c₀` issue as *endpoint attainment* (`sup` not attained ⟹ only `(1−ε)c₀`). That framing is correct but incomplete: the real content of Finding 1 is that the *definition* of `c₀` is a factor `1.96` below the constant the name denotes, and no choice of `a`, `α`, or `T` inside this route recovers it. So yes — it hides a gap, and the gap is the one that decides what the record may claim.

---

**Verdict: PROOF-REPAIRABLE(1, 2, 3)** — with the explicit caveat that repair 1 is a *restatement*, not a strengthening: after it, the theorem is true, unconditional, and internally airtight, but its constant `c₀ = sup_a a^{3/5}(5/3)^{1/5}` is ≈0.51× the best-known Korobov–Vinogradov PNT constant, and the resulting bound is strictly **weaker** (by 1.293× in the exponent constant) than the triangle inequality combined with the best-known PNT. The mathematics survives; the novelty claim does not.

Sources used for the constant check: [Zero-density estimates and the optimality of the error term in the PNT (arXiv:2411.13791)](https://arxiv.org/html/2411.13791), [Explicit zero-free regions for the Riemann zeta-function (arXiv:2212.06867)](https://arxiv.org/pdf/2212.06867), [Ford, Zero-free regions for the Riemann zeta function (arXiv:1910.08205)](https://arxiv.org/pdf/1910.08205), [Iwaniec–Kowalski, Analytic Number Theory (AMS Colloq. 53) contents](https://www.ams.org/books/coll/053/).