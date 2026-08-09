RESULT 023 — ANALYTIC DIAGNOSTIC  
SCOPE: [023 declaration](/mnt/d/Projects/prime-wheel-mobius/results/023/023.md), [020 provenance](/mnt/d/Projects/prime-wheel-mobius/results/020/020.md), [022 unconditional input](/mnt/d/Projects/prime-wheel-mobius/results/022/022.md).

## Q1 — D2 / FLOOR–Li JUMPS

NEW-BUT-PROVED-HERE [UNCONDITIONAL]. Put \(n=x+1\), \(K=\lfloor x/(y+1)\rfloor\). For \(h=1\),

\[
J(x):=\sum_{d\le K}\left|\Li_*\!\left(\Big\lfloor\frac{x+1}{d}\Big\rfloor\right)
-\Li_*\!\left(\Big\lfloor\frac{x}{d}\Big\rfloor\right)\right|
=
\sum_{\substack{d\mid n\\d\le K}}
\int_{n/d-1}^{n/d}\frac{du}{\log u}.
\]

Proof: \(\lfloor(x+1)/d\rfloor-\lfloor x/d\rfloor=1\) iff \(d\mid x+1\), otherwise it is \(0\). On the Abel support \(n/d\ge y+2\), so \(\Li_*\) is increasing.

NEW-BUT-PROVED-HERE [UNCONDITIONAL]. At \(y=\lfloor\sqrt x\rfloor\),

\[
\frac{\tau_{\le K}(x+1)}{\log(x+1)}
\le J(x)
\le \frac{\tau_{\le K}(x+1)}{\log(y+1)},
\]

and \(\tau_{\le K}(x+1)=\tfrac12\tau(x+1)+O(1)\). Proof: bound the unit integral between \(1/\log(n/d)\) and \(1/\log(n/d-1)\); divisor pairing \(d\leftrightarrow n/d\) supplies half the divisors below \(\sqrt n\), with at most the central divisor lost.

NEW-BUT-PROVED-HERE [UNCONDITIONAL]. Dyadic average:

\[
\frac1X\sum_{X\le x<2X}J(x)=\log 2+o(1).
\]

Proof: interchange \(n=dm\), \(d\le m\), \(X<n\le2X\). The main term is

\[
\sum_{d\le\sqrt X}\frac{1}{d\log(X/d)}
=\int_0^{1/2}\frac{du}{1-u}+o(1)
=\log2+o(1).
\]

The strip \(\sqrt X<d\le\sqrt{2X}\), endpoint floors, and replacement of the unit \(\Li\)-integral by \(1/\log m\) contribute \(o(1)\).

NONTRIVIAL-BUT-KNOWN (citation) [UNCONDITIONAL]. Wigert’s maximal-order theorem gives

\[
\max_{n\le X}\log\tau(n)
=(\log2+o(1))\frac{\log X}{\log\log X}.
\]

Hence along an extremal sequence,

\[
J(x)=\frac{1}{\log x}
 \exp\!\left((\log2+o(1))\frac{\log x}{\log\log x}\right),
\]

up to constant factors. This exceeds \((\log x)^A\) for every fixed \(A\). Citation: [Elsholtz–Technau–Technau, statement of Wigert’s theorem](https://arxiv.org/abs/1709.04799).

STANDARD [UNCONDITIONAL]. Therefore:

- average weighted floor–Li cost per step: \(O(1)\);
- average unweighted divisor count: \(\asymp\log K\);
- worst absolute one-step cost: \(x^{o(1)}/\log x\), not polylogarithmic;
- record 020’s \(K/\log y\asymp\sqrt x/\log x\) is extremely crude on stable one-step increments.

NEW-BUT-PROVED-HERE [UNCONDITIONAL]. Uniform cumulative replacement:

\[
\sum_{d\le K}
\left(\Big\lfloor\frac{x+h}{d}\Big\rfloor-\Big\lfloor\frac{x}{d}\Big\rfloor\right)
\le hH_K+K.
\]

Proof:

\[
\Big\lfloor\frac{x+h}{d}\Big\rfloor-\Big\lfloor\frac{x}{d}\Big\rfloor
\le \frac hd+1;
\]

sum over \(d\le K\).

NEW-BUT-PROVED-HERE [UNCONDITIONAL]. For frozen support,

\[
|S_y(x+h)-S_y(x)|
\le
\left(1+\frac{H_K}{\log(y+1)}\right)h
+\frac{K}{\log(y+1)}.
\tag{A}
\]

At \(K\sim y\sim\sqrt x\), the slope is \(2+o(1)\) and the intercept is \(y/\log y=o(y)\).

STANDARD [UNCONDITIONAL]. A global mean over starting points cannot feed the pinned excursion theorem. The correct replacement is the uniform affine modulus (A), valid from the actual pin.

OPEN. A polylogarithmic bound for the actual signed one-step increment, retaining the \(\mu(d)\)-cancellation, is not ruled out by Wigert. What is ruled out is obtaining it from the absolute floor-jump majorant used in record 020.

## Q2 — D3 / SUPPORT GROWTH

NEW-BUT-PROVED-HERE [UNCONDITIONAL]. For \(h=1\), support grows exactly when

\[
x\equiv y\pmod{y+1},
\]

a density \(1/(y+1)\) set for fixed \(y\). If \(x+1=(K+1)(y+1)\), the inserted term is exactly

\[
\mu(K+1)R(y+1).
\]

STANDARD [UNCONDITIONAL]. The blanket statement “support growth needs PNT-strength input” is false if “kill” means \(o(y)\) at an \(H\asymp y\) excursion. Elementary Chebyshev bounds give

\[
\pi(y)\ll\frac y{\log y},
\qquad
\Li_*(y)\ll\frac y{\log y},
\qquad
R(y)\ll\frac y{\log y}=o(y).
\]

Thus one support insertion can already be absorbed into the affine intercept without PNT.

NONTRIVIAL-BUT-KNOWN (citation) [UNCONDITIONAL]. Vinogradov–Korobov strengthens this to

\[
R(t)\ll
t\exp\!\left(
-c(\log t)^{3/5}(\log\log t)^{-1/5}
\right).
\tag{VK}
\]

At \(t\asymp y\asymp\sqrt x\), one insertion costs

\[
\ll\sqrt x\exp\!\left(
-c'(\log x)^{3/5}(\log\log x)^{-1/5}
\right).
\]

Citations: [Korobov 1958](https://www.mathnet.ru/eng/rm7458), [Vinogradov 1958](https://m.mathnet.ru/eng/im3962).

STANDARD [UNCONDITIONAL]. Averaged per unit step, the support cost is

\[
\ll \frac{|R(y)|}{y+1};
\]

this is \(O(1/\log y)\) by Chebyshev and exponentially smaller by VK.

STANDARD [CONDITIONAL ON RH]. RH would give \(R(y)=O(y^{1/2}\log y)\), still not a polylogarithmic pointwise support bound. RH is neither needed for (VK) nor for the affine excursion-scale absorption.

NEW-BUT-PROVED-HERE [UNCONDITIONAL]. At the canonical square pin

\[
x_0=(y+1)^2-1,
\]

the current forward record-020 theorem is vacuous for every nonzero window: both hypotheses force \(W<1\).

NEW-BUT-PROVED-HERE [UNCONDITIONAL]. The backward interval is exactly stable:

\[
\left\lfloor\frac{x_0-t}{y+1}\right\rfloor=y
\qquad(0\le t\le y).
\]

Proof: \(x_0=y(y+1)+y\), so subtracting \(t\le y\) changes only the remainder. Therefore the canonical synchronized pin admits a length-\(y\) backward frozen-support excursion with no D3 term at all.

## Q3 — ASSEMBLY

NONTRIVIAL-BUT-KNOWN (citation) [UNCONDITIONAL]. Best absolute stable one-step envelope over \(x\le X\):

\[
C_{\mathrm{stable}}(X)
=
\frac{1}{\log X}
\exp\!\left((\log2+o(1))
\frac{\log X}{\log\log X}\right).
\]

This is the Wigert floor and is strictly between polylogarithmic and every fixed power of \(X\).

NONTRIVIAL-BUT-KNOWN (citation) [UNCONDITIONAL]. Including arbitrary forward support crossings and applying VK termwise gives the presently available absolute pointwise envelope

\[
C_{\mathrm{full}}(y,x)
\ll C_{\mathrm{stable}}(x)
+y\exp\!\left(
-c(\log y)^{3/5}(\log\log y)^{-1/5}
\right).
\]

At \(y\asymp\sqrt x\), the sparse support term dominates asymptotically. This improves \(\sqrt x/\log x\), but is not polylogarithmic.

NEW-BUT-PROVED-HERE [UNCONDITIONAL]. The rung-relevant object is instead

\[
|S_y(x_0\pm t)-S_y(x_0)|\le A_y t+B_y,
\]

with

\[
A_y=1+\frac{H_K}{\log(y+1)}=2+o(1),
\qquad
B_y=\frac K{\log(y+1)}
\]

on a stable side. If a support boundary is crossed, append either \(O(y/\log y)\) or the sharper VK cost to \(B_y\).

NEW-BUT-PROVED-HERE [UNCONDITIONAL]. Affine excursion lemma: if \(H=|f(x_0)|\), \(B<H/2\), and \(|f(x_0+t)-f(x_0)|\le At+B\), then

\[
|f(x_0+t)|\ge H/2
\quad\text{for}\quad
0\le t\le\frac{H/2-B}{A}.
\]

Proof: reverse triangle inequality gives \( |f(x_0+t)|\ge H-(At+B)\).

NEW-BUT-PROVED-HERE [UNCONDITIONAL REDUCTION]. At \(H\asymp y\asymp\sqrt x\), \(B_y=o(H)\), hence the backward canonical window has

\[
W\asymp H\asymp\sqrt x,
\]

and

\[
(H/2)^{2k}W
\ll
\sum_{t<W}|S_y(x_0-t)|^{2k}.
\]

Thus the intended \(H^{2k+1}\)-scale moment lower bound is recovered unconditionally on the increment side.

OPEN [CONDITIONAL CONSEQUENCE]. The required matching windowed moment upper bound remains open. No RH conclusion follows from this diagnostic alone.

NEW-BUT-PROVED-HERE [UNCONDITIONAL]. Record 020’s present formal theorem yields only \(W\asymp\log x\) at generic stable pins and yields \(W=0\) at canonical square endpoints. The backward affine extension changes the canonical result to \(W\asymp\sqrt x\).

OPEN. Uniform pointwise polylogarithmic Lipschitz control for the actual signed Abel face remains open. It is unnecessary for H1 once the theorem consumes an affine modulus.

## Q4 — KILL TEST / FORMALIZATION

NONTRIVIAL-BUT-KNOWN (citation) [UNCONDITIONAL KILL]. Cheapest decisive kill for the absolute pointwise-polylog claim: take \(x=n-1\) along a Wigert extremal sequence. Then

\[
J(x)\gg \frac{\tau(n)}{\log n}
\]

and \(J(x)>(\log x)^A\) for every fixed \(A\), eventually. No numerical experiment is needed.

NEW-BUT-PROVED-HERE [UNCONDITIONAL, NON-PROMOTING CHECK]. Exact finite regression passed for \(x<5000\), \(h\in\{1,2,3,\lfloor\sqrt x/4\rfloor\}\):

\[
F(x,1,K)=\#\{d\le K:d\mid x+1\},
\qquad
F(x,h,K)\le\sum_{d\le K}(h/d+1).
\]

Arithmetic model: exact integer floor counts; floating point used only for the real RHS. For \(n\le100000\), the largest truncated count observed was \(64\) at \(n=83160\), where \(\tau(n)=128\). Numerics promote nothing.

STANDARD [BOUNDED LEAN SCOPE]. Lean-formalizable at bounded effort:

- exact \(h=1\) divisor-jump identity;
- \(\lfloor(x+h)/d\rfloor-\lfloor x/d\rfloor\le h/d+1\);
- harmonic affine bound (A);
- abstract affine excursion and moment lemmas;
- backward versions of the record-020 theorems;
- exact square-pin stability for \(0\le t\le y\);
- exact support-growth decomposition.

NONTRIVIAL-BUT-KNOWN (citation) [NOT BOUNDED LEAN SCOPE]. Formalizing Chebyshev or VK from foundations is a separate analytic project. The bounded implementation should accept a discrepancy envelope \(E(y)\) as a typed hypothesis; the canonical backward theorem needs neither envelope.

STANDARD [FROZEN PLAN]. Replace “prove a polylog pointwise Lipschitz constant” by: prove the backward affine modulus with \(A_y=2+o(1)\), \(B_y\ll y/\log y\), then instantiate the affine moment transfer at square pins. Pointwise-polylog via absolute floor jumps is killed; the rung-relevant excursion survives.

PLAN-VIABLE

Codex session ID: 019fe81f-08cd-7461-b037-f6bd54bb2541
Resume in Codex: codex resume 019fe81f-08cd-7461-b037-f6bd54bb2541
