VERDICT: **CONFIRMED-WITH-REPAIRS**

SCOPE:

- \(\mathcal M(x,K,T)=o(\sqrt x)\): correct.
- The quantitative bound (6.1): correct.
- The deduction \(S(x,K)=o(x)\): not proved as written; repairable.
- No fatal false inequality found.

## 1. Step (2.1): SURVIVES; citation/branch repair required

Set \(z=\rho\log u\), \(w=-z\). For \(\Im z>0\),
\[
\operatorname{Ei}(z)-i\pi=-E_1(-z).
\]
Thus the branch in [proof_attempt.md:37](/mnt/d/Projects/prime-wheel-mobius/results/022/proof_attempt.md:37) is correct.

For \(\gamma\ge3\), \(0<\beta<1\),
\[
-\pi+\arctan 3\le\arg w<-\pi/2.
\]
This is a fixed closed subsector of
\[
|\arg w|\le 3\pi/2-\delta.
\]
The DLMF expansion is therefore uniform. Its first-remainder estimate gives
\[
-E_1(-z)=\frac{e^z}{z}(1+R),\qquad
|R|\ll |z|^{-1},
\]
uniformly there. Hence, for sufficiently large \(u\),
\[
|\operatorname{Li}_*(u^\rho)|
\le \frac{2u^\beta}{|\rho|\log u}.
\]
[DLMF §6.12(i)](https://dlmf.nist.gov/6.12) states the required sector.

Zeros with \(0<\gamma<3\) form a finite set and can be absorbed into the threshold for \(u\).

MANDATORY REPAIR:

- Replace “on the relevant fixed sector” with the displayed sector computation.
- State the exact connection formula \(\operatorname{Ei}(z)-i\pi=-E_1(-z)\).
- Cite the explicit remainder statement, not merely the asymptotic symbol.

No branch misuse remains after this repair. The absolute moment is branch-dependent, but the chosen branch is explicitly part of its definition; the signed explicit formula is unchanged because the alternative adds only a purely imaginary constant.

## 2. Steps (4.1)–(4.3): CONFIRMED

The constant, exponents, and range are exactly correct:
\[
\sigma\ge1-\frac{1}{55.241(\log|t|)^{2/3}
(\log\log|t|)^{1/3}},\qquad |t|\ge3.
\]
This is Theorem 1.1 of [Mossinghoff–Trudgian–Yang](https://arxiv.org/abs/2212.06867).

For
\[
q(t)=(\log t)^{2/3}(\log\log t)^{1/3},
\]
\[
\frac{q'(t)}{q(t)}
=\frac{1}{t\log t}\left(\frac23+
\frac{1}{3\log\log t}\right)>0
\qquad(t\ge3).
\]
Therefore \(q(\gamma)\le q(2x^2)\) for \(3\le\gamma\le2x^2\), and
\[
1-\beta>\frac1{55.241q(\gamma)}
\ge\frac1{55.241q(2x^2)}=\eta(x).
\]
Step (4.3) is legitimate.

## 3. Steps (3.1)–(3.3): CONFIRMED; normalization must be made explicit

The identity chain is correct:
\[
\pi_0(u)
=J_0(u)+\sum_{m\ge2}\frac{\mu(m)}mJ_0(u^{1/m}),
\]
so
\[
C_0(u)=A(u)+
\sum_{m\ge2}\frac{\mu(m)}mJ_0(u^{1/m}).
\]
This matches record 021’s definition of \(C_0\). Lower prime-power zero harmonics are contained inside the exact \(J_0(u^{1/m})\); none is discarded.

For the repo’s \(\operatorname{Li}(u)=\int_2^u dt/\log t\), the proof should state explicitly
\[
A(u)=\operatorname{li}(2)-\log2+
\int_u^\infty\frac{dv}{v(v^2-1)\log v},
\]
subject to the declared complex-\(\operatorname{li}\) convention.

Floor/midpoint corrections:

\[
|\pi(\lfloor u_d\rfloor)-\pi_0(u_d)|\le\frac12,
\]
hence their total is \(O(K)=O(\sqrt x)\). Also,
\[
|\operatorname{Li}(u_d)-\operatorname{Li}(\lfloor u_d\rfloor)|
\ll\frac1{\log(x/K)},
\]
so their total is \(O(K/\log x)\).

Thus the \(K\cdot O(1)\) concern is real but harmless: it is \(O(\sqrt x)\), not smaller, and is sufficient for the claimed \(o(x)\) deduction.

MANDATORY REPAIR:

- Display \(A(u)\) under the repo normalization.
- Separate the \(O(K)\) midpoint correction and \(O(K/\log x)\) floor-\(\operatorname{Li}\) correction from the analytic truncation error.

## 4. Step 6: GAP AS WRITTEN; REPAIRABLE

[proof_attempt.md:348](/mnt/d/Projects/prime-wheel-mobius/results/022/proof_attempt.md:348) merely reasserts the unsupplied lemma already flagged in [codex_report.md:17](/mnt/d/Projects/prime-wheel-mobius/results/021/codex_report.md:17). “Choose a standard admissible height” is insufficient because one common \(T_0\) must work for all \(d\le K\).

The suggested error accumulation does not kill the claim. With \(u_d=x/d\), \(T\asymp x^2\),
\[
\sum_{d\le K}\frac{u_d\log^2(u_dT)}T
\ll \frac{\log^3x}{x}.
\]
Moreover, for any integer \(n\), unless \(u_d=n\),
\[
|u_d-n|=\frac{|x-dn|}{d}\ge\frac1d.
\]
Consequently a standard proximity term satisfies
\[
\frac{u_d}{T|u_d-n|}
\le\frac{x}{T}\ll\frac1x.
\]
Exact prime-power equality is handled by the midpoint convention. Even an \(O(\log^B x)\) per-\(d\) residual totals only
\[
O(K\log^B x)=O(\sqrt x\log^B x)=o(x).
\]

MANDATORY REPAIR:

Insert a precise common-height lemma:
\[
J_0(x/d)-\operatorname{Li}(x/d)
=
-2\Re\sum_{0<\gamma\le T_0}
\operatorname{Li}_*((x/d)^\rho)
+A(x/d)+E_d,
\]
where one \(T_0\in[x^2,2x^2]\), selected from the zero set independently of \(d\), satisfies
\[
\sum_{d\le K}|E_d|\ll\sqrt x\log^A x.
\]
Then add the floor/midpoint corrections separately.

Without this insertion, \(S(x,K)=o(x)\) is not proved in this document. It does not affect the independently defined \(\mathcal M\)-bound.

## 5. Novelty audit: YES, ALREADY KNOWN

Answer to question 5: **YES as a consequence; NO as a logical equivalence.**

The pointwise Vinogradov–Korobov PNT bound gives
\[
|R(t)|\ll
t\exp\!\left(
-c(\log t)^{3/5}(\log\log t)^{-1/5}
\right).
\]
Uniformly for \(d\le K\le\kappa_+\sqrt x\),
\[
x/d\ge\sqrt x/\kappa_+.
\]
Therefore
\[
\begin{aligned}
|S(x,K)|
&\le\sum_{d\le K}|R(\lfloor x/d\rfloor)|\\
&\ll x\sum_{d\le K}\frac1d
 \exp\!\left[-c'
 (\log x)^{3/5}(\log\log x)^{-1/5}\right]\\
&\ll x\log x\,
 \exp\!\left[-c'
 (\log x)^{3/5}(\log\log x)^{-1/5}\right]\\
&=o(x).
\end{aligned}
\]

Thus \(S(x,K)=o(x)\) is not a new unconditional result. The moment proof supplies gate consistency and an explicit all-zero realization, not new PNT-strength analytic control. The standalone truncated convolution estimate is not established to be equivalent to the pointwise VK estimate.

## 6. Hidden-input audit

- RH-strength input: none.
- Line-only enumeration: none.
- Off-line zeros: retained through \(\beta\).
- Multiplicity: retained through \(N(T)\).
- Zero-density misuse: none; only total counting is used.
- \(55.241\) convention error: none.
- Monotonicity reversal: none.
- Discarded lower prime-power harmonics: none.
- Branch error: none after the mandatory explicit connection formula.
- Fatal step for \(\mathcal M=o(\sqrt x)\): none.
- Unproved step for \(S=o(x)\): common-height uniform truncation at Step 6.

Codex session ID: 019fe819-be06-7442-9058-2f2b2560abfa
Resume in Codex: codex resume 019fe819-be06-7442-9058-2f2b2560abfa
