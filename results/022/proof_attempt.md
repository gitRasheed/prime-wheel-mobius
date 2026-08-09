PROOF-COMPLETE

Quantitative result proved:
\[
\boxed{
\mathcal M(x,K,T)
\ll_{\kappa_+}
x^{1/4}
+\sqrt x(\log x)^2e^{-h(x)}
}
\]
uniformly for
\[
\kappa_-\sqrt x\le K\le\kappa_+\sqrt x,
\qquad x^2\le T\le2x^2,
\]
where
\[
h(x):=
\frac{\log x}
{4\cdot55.241\,
 (\log(2x^2))^{2/3}
 (\log\log(2x^2))^{1/3}}.
\]
Since \(h(x)\asymp(\log x/\log\log x)^{1/3}\),
\[
(\log x)^2e^{-h(x)}\longrightarrow0.
\]
Thus
\[
\boxed{\mathcal M(x,K,T)=o(\sqrt x)}
\]
unconditionally and uniformly. No fixed power saving is obtained.

## 1. Conventions

[STANDARD] Let \(J_0(u)\) and \(\pi_0(u)\) denote the midpoint versions of the Riemann prime-power counter and prime counter. Let
\[
\operatorname{Li}_*(u^\rho)
 =\operatorname{Ei}(\rho\log u)-i\pi
 \qquad(\Im\rho>0)
\]
be the conjugate-symmetric asymptotic branch used in [the record-018 implementation](/mnt/d/Projects/prime-wheel-mobius/results/018/k2/k2_zerosum.py:18). This branch qualification is essential: the principal branch contains an additive \(i\pi\), whose absolute value could not be summed over zeros.

[STANDARD] For a nontrivial zero \(\rho=\beta+i\gamma\),
\[
0<\beta<1,\qquad \gamma>0.
\]
All zero sums below count multiplicity.

Take \(x\) sufficiently large, depending only on \(\kappa_+\), so that for \(d\le K\),
\[
u_d:=\frac xd\ge\frac{\sqrt x}{\kappa_+}\ge3,
\]
and, writing \(L=\log x\),
\[
\log u_d\ge\frac L4,\qquad
1+\log K\le L.
\tag{1.1}
\]

## 2. Honest trivial scale

[NONTRIVIAL-BUT-KNOWN — complex exponential-integral asymptotics, NIST DLMF §6.12(i)] Uniformly for nontrivial zeros and \(u\) sufficiently large,
\[
\left|\operatorname{Li}_*(u^\rho)\right|
\le
\frac{2u^\beta}{|\rho|\log u}.
\tag{2.1}
\]
This follows from
\[
-E_1(-z)=\frac{e^z}{z}\left(1+O(|z|^{-1})\right),
\qquad z=\rho\log u,
\]
on the relevant fixed sector. The asymptotic expansion and sectorial remainder control are recorded in [DLMF 6.12.1](https://dlmf.nist.gov/6.12).

[NEW-BUT-PROVED-HERE] Using only \(\beta<1\), (1.1), and
\[
\sum_{d\le K}\frac1d\le1+\log K,
\]
gives
\[
\begin{aligned}
|G_{x,K}(\rho)|
&\le \frac2{|\rho|}
 \sum_{d\le K}\frac{x/d}{\log(x/d)}\\
&\le \frac{8x}{|\rho|}.
\end{aligned}
\tag{2.2}
\]

[NONTRIVIAL-BUT-KNOWN — Riemann–von Mangoldt formula] If \(N(U)\) counts zeros with \(0<\gamma\le U\), with multiplicity, then
\[
N(U)=\frac{U}{2\pi}\log\frac{U}{2\pi}
-\frac{U}{2\pi}+O(\log(U+2)).
\]
Partial summation therefore gives an absolute \(D>0\) such that
\[
\sum_{0<\gamma\le T}\frac1\gamma
\le D\log^2(T+2).
\tag{2.3}
\]

[NEW-BUT-PROVED-HERE] Equations (2.2)–(2.3), together with \(T\le2x^2\), give
\[
2x^{-1/2}\sum_{0<\gamma\le T}|G_{x,K}(\rho)|
\ll \sqrt x(\log x)^2.
\tag{2.4}
\]

Component (a), proved below, contributes \(O(x^{1/4})\). Hence the honest trivial estimate is
\[
\boxed{\mathcal M(x,K,T)\ll_{\kappa_+}
\sqrt x(\log x)^2+x^{1/4}.}
\tag{2.5}
\]

## 3. Component (a): the full \(C_{x,K}\)

[STANDARD — Riemann explicit formula and Möbius inversion] With the repo normalization,
\[
J_0(u)-\operatorname{Li}(u)
=
-2\Re\sum_{\gamma>0}\operatorname{Li}_*(u^\rho)+A(u),
\tag{3.1}
\]
where \(A(u)\) is the constant/trivial-zero/archimedean contribution. Also,
\[
\pi_0(u)
=
\sum_{1\le m\le\log_2u}
\frac{\mu(m)}mJ_0(u^{1/m}).
\tag{3.2}
\]
Consequently the exact secondary term can be written
\[
C_0(u)
=
A(u)+
\sum_{2\le m\le\log_2u}
\frac{\mu(m)}mJ_0(u^{1/m}).
\tag{3.3}
\]
This packages all lower prime-power zero harmonics inside the arithmetic function \(J_0\); none has been discarded.

[STANDARD] The archimedean term is bounded for \(u\ge3\). In the usual normalization its nonconstant part has the form
\[
\int_u^\infty
\frac{dv}{v(v^2-1)\log v},
\]
whose absolute value is at most
\[
\frac9{16\log3}\,u^{-2}.
\]
Let \(B_A\) be the absolute value of the fixed normalization constant plus \(9/(144\log3)\). Then
\[
|A(u)|\le B_A\qquad(u\ge3).
\tag{3.4}
\]
Thus \(B_A\) is explicitly absorbable from the chosen \(\operatorname{Li}\) normalization.

[NEW-BUT-PROVED-HERE] Directly from the definition,
\[
0\le J_0(v)
=\sum_{p^a\le v}\frac1a
\le v
\qquad(v\ge2).
\tag{3.5}
\]
Therefore
\[
\begin{aligned}
\sum_{2\le m\le\log_2u}\frac1mJ_0(u^{1/m})
&\le\frac12\sqrt u+
u^{1/3}\sum_{3\le m\le\log_2u}\frac1m\\
&\le\frac12\sqrt u+
u^{1/3}(1+\log\log_2u).
\end{aligned}
\tag{3.6}
\]
For an absolute, effective \(u_0\),
\[
1+\log\log_2u\le u^{1/6}\qquad(u\ge u_0).
\]
Hence
\[
|C_0(u)|\le B_C\sqrt u,
\qquad
B_C:=B_A+\frac32.
\tag{3.7}
\]

[NEW-BUT-PROVED-HERE] It follows that
\[
\begin{aligned}
|C_{x,K}|
&\le\sum_{d\le K}|C_0(x/d)|\\
&\le B_C\sqrt x\sum_{d\le K}d^{-1/2}\\
&\le2B_C\sqrt{xK}\\
&\le2B_C\sqrt{\kappa_+}\,x^{3/4}.
\end{aligned}
\tag{3.8}
\]
Thus
\[
\boxed{
x^{-1/2}|C_{x,K}|
\le2B_C\sqrt{\kappa_+}\,x^{1/4}
=o(\sqrt x).
}
\tag{3.9}
\]

Component (a) is complete, including every higher prime-power and archimedean term.

## 4. Uniform payment for off-line zeros

[NONTRIVIAL-BUT-KNOWN — Vinogradov–Korobov zero-free region] Mossinghoff–Trudgian–Yang, Theorem 1.1, proves unconditionally that for \(|\gamma|\ge3\), a zero \(\beta+i\gamma\) satisfies
\[
1-\beta>
\frac1{55.241(\log|\gamma|)^{2/3}
                 (\log\log|\gamma|)^{1/3}}.
\tag{4.1}
\]
See [Explicit zero-free regions for the Riemann zeta-function](https://link.springer.com/article/10.1007/s40993-023-00498-y).

[STANDARD] The finitely many zeros with \(0<\gamma<3\), if any, have
\[
1-\beta\ge\eta_0>0.
\]
Because the right side below tends to zero, increasing \(x_0\) absorbs this finite range.

Define
\[
\eta(x):=
\frac1{55.241(\log(2x^2))^{2/3}
                 (\log\log(2x^2))^{1/3}}.
\tag{4.2}
\]

[NEW-BUT-PROVED-HERE] Since \(0<\gamma\le T\le2x^2\), monotonicity in (4.1) gives, uniformly over every zero in the target sum,
\[
\beta\le1-\eta(x).
\tag{4.3}
\]
For \(u_d=x/d\), (1.1) therefore gives
\[
u_d^\beta
=u_d\,e^{-(1-\beta)\log u_d}
\le
u_d\,e^{-\eta(x)L/4}
=u_d e^{-h(x)}.
\tag{4.4}
\]

[NEW-BUT-PROVED-HERE] Insert (4.4) into the exact branch estimate (2.1):
\[
\begin{aligned}
|G_{x,K}(\rho)|
&\le
\frac{2e^{-h(x)}}{|\rho|}
\sum_{d\le K}\frac{x/d}{\log(x/d)}\\
&\le
\frac{8xe^{-h(x)}}{|\rho|}.
\end{aligned}
\tag{4.5}
\]
No cancellation in \(\mu(d)\) has been assumed.

[NEW-BUT-PROVED-HERE] Sum (4.5) using (2.3):
\[
\begin{aligned}
2x^{-1/2}\sum_{0<\gamma\le T}|G_{x,K}(\rho)|
&\le
16\sqrt x\,e^{-h(x)}
\sum_{0<\gamma\le T}\frac1\gamma\\
&\ll
\sqrt x(\log x)^2e^{-h(x)}.
\end{aligned}
\tag{4.6}
\]
Finally,
\[
h(x)
\sim
\frac1{4\cdot55.241\cdot2^{2/3}}
\left(\frac{\log x}{\log\log x}\right)^{1/3}.
\tag{4.7}
\]
Hence \(h(x)/\log\log x\to\infty\), so
\[
(\log x)^2e^{-h(x)}\to0.
\tag{4.8}
\]
Thus
\[
\boxed{
2x^{-1/2}\sum_{0<\gamma\le T}|G_{x,K}(\rho)|
=o(\sqrt x).
}
\tag{4.9}
\]

## 5. The off-line-zero crux

[NEW-BUT-PROVED-HERE] The \(x^{\beta-1/2}\) weight has not been suppressed. Equation (4.4) pays it through
\[
(x/d)^\beta=(x/d)(x/d)^{-(1-\beta)}.
\]
At the final normalized scale,
\[
\frac{2x^{-1/2}\sum_{\gamma\le T}|G_{x,K}(\rho)|}
{\sqrt x}
\ll
e^{-h(x)}(\log x)^2
\longrightarrow0.
\tag{5.1}
\]

This resolves the distinction identified in record 021:

- A fixed zero \(\beta=1/2+\delta\) is fatal for a polylogarithmic normalized gate because its natural factor \(x^{\beta-1/2}=x^\delta\) grows.
- It is not fatal for the rung-0 target because \(\beta<1\), hence
  \[
  x^{\beta-1/2}=o(x^{1/2}).
  \]
- Zeros whose heights grow with \(x\) are uniformly handled by (4.3)–(4.5).

[NEW-BUT-PROVED-HERE] A refined zero-density estimate \(N(\sigma,T)\) is unnecessary. The total density supplied by Riemann–von Mangoldt suffices because the zero-free region gives the same \(e^{-h(x)}\) factor to every zero in the permitted height range. Multiplicity is already included in (2.3). This is precisely why density suffices at the \(o(\sqrt x)\) normalized scale but did not repair the polylogarithmic gate.

## 6. Completion and implication for \(S(x,K)\)

[NEW-BUT-PROVED-HERE] Combining (3.9) and (4.6),
\[
\mathcal M(x,K,T)
\le
2B_C\sqrt{\kappa_+}\,x^{1/4}
+C_Z\sqrt x(\log x)^2e^{-h(x)}
\tag{6.1}
\]
for an absolute, explicitly absorbable Riemann–von Mangoldt constant \(C_Z\). Dividing by \(\sqrt x\) and using (4.8),
\[
\boxed{\mathcal M(x,K,T)=o(\sqrt x)}
\]
uniformly in both \(K\) and \(T\). The proof only uses \(\kappa_+\); uniformity in \(\kappa_-\) is automatic.

[NONTRIVIAL-BUT-KNOWN — truncated Riemann explicit formula] Choose a standard admissible height \(T_0\in[x^2,2x^2]\), away from zero ordinates, in the record-021 explicit-formula identity. Its truncation, midpoint, and floor errors are
\[
E_{T_0}(x,K)\ll\sqrt x(\log x)^A=o(x)
\]
for some fixed \(A\). Since the proved moment estimate is uniform in \(T\), it applies at this admissible \(T_0\). Therefore
\[
\begin{aligned}
|S(x,K)|
&\le |C_{x,K}|
 +2\sum_{0<\gamma\le T_0}|G_{x,K}(\rho)|
 +|E_{T_0}(x,K)|\\
&=\sqrt x\,\mathcal M(x,K,T_0)+o(x)\\
&=o(x).
\end{aligned}
\]
Hence
\[
\boxed{S(x,K)=o(x).}
\]

## 7. Stretch verdict and adversarial audit

[STANDARD] The established factor
\[
e^{-c(\log x/\log\log x)^{1/3}}
\]
is subpower. It does not imply
\[
\mathcal M\ll x^{1/2-\delta}
\]
for any fixed \(\delta>0\). Stretch goal not reached.

[NEW-BUT-PROVED-HERE] Adversarial checks:

- No RH or line-only enumeration occurs.
- Off-line zeros retain their full \(\beta\)-weight.
- Multiplicity is retained.
- No Möbius cancellation is assumed in either \(C_{x,K}\) or \(G_{x,K}\).
- Higher prime powers are included through exact Möbius inversion.
- The branch-dependent additive \(i\pi\) is removed before absolute values.
- Only the upper limits \(K\le\kappa_+\sqrt x\) and \(T\le2x^2\) are used.
- No exceptional-height or averaged-\(x\) argument is used.
- The density step is total zero counting, not an unsupported assertion about off-line zeros.

No blocking object remains for rung 0.

## 8. Kernel-formalization requirements

A later Lean record needs:

1. Midpoint definitions of \(J_0,\pi_0,\operatorname{Li}_*\), including the asymptotic branch.
2. Exact finite Möbius inversion (3.2) and the decomposition (3.3).
3. Elementary formal bounds (3.5)–(3.9).
4. A formal complex-\(E_1\) sector estimate implying (2.1).
5. Formal statements of the explicit Vinogradov–Korobov region and Riemann–von Mangoldt counting formula.
6. The uniform asymptotic calculation (4.2)–(4.9).
7. A selected admissible truncation height for the final explicit-formula bridge.

Current status remains informal until items 4–5 and the truncation theorem are kernel-available.

Codex session ID: 019fe811-c7cb-7223-bf33-fe6a3bd4908f
Resume in Codex: codex resume 019fe811-c7cb-7223-bf33-fe6a3bd4908f
