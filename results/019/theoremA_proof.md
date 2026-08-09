# Theorem A (repaired)

Let
\[
R(u)=\pi(u)-\operatorname{Li}(u),
\qquad
\Phi(x)=(\log x)^{3/5}(\log\log x)^{-1/5}.
\]
Suppose \(y\asymp \sqrt x\) and
\[
K=\left\lfloor\frac{x}{y+1}\right\rfloor .
\]
Then, for every \(\varepsilon>0\), there is \(x_0(\varepsilon)\) such that, for \(x\ge x_0(\varepsilon)\),
\[
\boxed{
\left|
\sum_{d\le K}\mu(d)\,
R\!\left(\left\lfloor\frac{x}{d}\right\rfloor\right)
\right|
\le
x\exp\!\left(-(1-\varepsilon)c_0\Phi(x)\right),
}
\]
where \(c_0\) is the Korobov–Vinogradov PNT constant in the normalization specified below.

The proof is unconditional.

## 1. The precise Vinogradov–Korobov input

Write
\[
D(V)=(\log(V+3))^{2/3}(\log_2(V+3))^{1/3},
\qquad
\log_2 u=\max(1,\log\log u).
\]

We use the following standard consequence of the Vinogradov–Korobov estimate.

**VK input.** There is \(a_*>0\) such that, for every fixed \(0<a<a_*\), the region
\[
\Re s\ge 1-\frac{a}{D(V)},\qquad |\Im s|\le V,
\tag{1.1}
\]
is zero-free, apart from the pole of \(\zeta\) at \(s=1\), and throughout every such fixed interior region
\[
\frac1{\zeta(s)}\ll (\log(V+3))^A,
\tag{1.2}
\]
and
\[
\frac{\zeta'}{\zeta}(s)+\frac1{s-1}
\ll(\log(V+3))^A
\tag{1.3}
\]
for some absolute \(A\), with the singularity in (1.3) interpreted removably at \(s=1\).

This package follows from the Vinogradov–Korobov estimate and the standard zero-detection argument: Iwaniec–Kowalski, *Analytic Number Theory*, Corollary 8.28 and Theorem 8.29; equivalently Titchmarsh–Heath-Brown, Theorems 3.10 and 3.11 combined with (6.19.2). The latter source explicitly derives the zero-free region and bounds for \(1/\zeta\) and \(\zeta'/\zeta\) from the VK bound ([Titchmarsh–Heath-Brown, pp. 58–60 and 134–135](https://sites.math.rutgers.edu/~zeilberg/EM18/TitchmarshZeta.pdf)). Ford’s Theorem 1 gives a modern explicit form of the same zero-free region ([Ford, Theorem 1](https://arxiv.org/abs/1910.08205)).

For a working constant \(a<a_*\), put
\[
c(a)=a^{3/5}\left(\frac53\right)^{1/5}.
\tag{1.4}
\]
Indeed, if
\[
\log T=c(a)\Phi(X),
\tag{1.5}
\]
then
\[
\frac{a\log X}
 {(\log(2T+3))^{2/3}(\log_2(2T+3))^{1/3}}
 =(c(a)+o(1))\Phi(X).
\tag{1.6}
\]

We define \(c_0\) as the supremum of the constants \(c(a)\) supplied by the chosen VK normalization. Since the theorem contains \(1-\varepsilon\), we always choose a fixed interior \(a<a_*\) satisfying
\[
c(a)>(1-\varepsilon/10)c_0.
\tag{1.7}
\]
Thus no assertion at an unattained endpoint is made.

## 2. Two quantitative Perron estimates

We use the standard truncated Perron kernel
\[
P_T(v)=\frac1{2\pi i}
\int_{c-iT}^{c+iT}\frac{v^s}{s}\,ds.
\]
For \(c>0\),
\[
P_T(v)=\mathbf 1_{v>1}
+O\!\left(
v^c\min\left(1,\frac1{T|\log v|}\right)
\right),
\tag{2.1}
\]
away from \(v=1\). This is Montgomery–Vaughan, Corollary 5.3, or Titchmarsh–Heath-Brown, Lemmas 3.12 and 3.19 ([the latter at pp. 61 and 69](https://sites.math.rutgers.edu/~zeilberg/EM18/TitchmarshZeta.pdf)).

### Lemma 2.1: outer Perron truncation

Let \(X=N+\tfrac12\), \(N\in\mathbb N\), let \(2\le K\le X\), and put
\[
F_K(s)=\sum_{d\le K}\frac{\mu(d)}{d^s},
\qquad
c=1+\frac1{\log X}.
\]
For \(3\le T\le X\),
\[
\sum_{d\le K}\mu(d)J(X/d)
=
\frac1{2\pi i}
\int_{c-iT}^{c+iT}
F_K(s)\log\zeta(s)\frac{X^s}{s}\,ds
+O\!\left(\frac{X(\log X)^2}{T}\right),
\tag{2.2}
\]
where
\[
J(u)=\sum_{n\le u}\frac{\Lambda(n)}{\log n}.
\]

**Proof.** For \(\Re s>1\),
\[
F_K(s)\log\zeta(s)
=
\sum_{m\ge1}\frac{a_K(m)}{m^s},
\quad
a_K(m)=
\sum_{\substack{dn=m\\d\le K\\n\ge2}}
\mu(d)\frac{\Lambda(n)}{\log n}.
\tag{2.3}
\]
Moreover
\[
|a_K(m)|
\le
\sum_{n\mid m}\frac{\Lambda(n)}{\log n}
=
\sum_{p^j\mid m}\frac1j
\ll\log(2m).
\tag{2.4}
\]
Since \(X\) is a half-integer, \(|X-m|\ge\tfrac12\) for every integer \(m\). Applying (2.1), the error is at most
\[
\sum_{m\ge1}|a_K(m)|
\left(\frac Xm\right)^c
\min\left(1,\frac1{T|\log(X/m)|}\right).
\tag{2.5}
\]

For \(X/2\le m\le2X\),
\[
|\log(X/m)|\asymp\frac{|X-m|}{X}.
\]
Terms with \(|X-m|\le X/T\) contribute
\[
\ll \frac XT\log X,
\]
and the remaining terms in this range contribute
\[
\ll
\frac XT\log X
\sum_{1\le j\le X}\frac1{j+1/2}
\ll\frac{X(\log X)^2}{T}.
\]
For \(m<X/2\) or \(m>2X\), \(|\log(X/m)|\gg1\); using \(c-1=1/\log X\),
\[
X^c\sum_{m\ge1}\frac{\log(2m)}{m^c}
\ll X(\log X)^2.
\]
This proves (2.2). ∎

### Lemma 2.2: the regularized logarithmic-integral kernel

Define
\[
L_0(u)=\int_1^u\frac{1-v^{-1}}{\log v}\,dv.
\tag{2.6}
\]
The integrand has removable value \(1\) at \(v=1\). For \(\Re s>1\),
\[
G(s):=\log\frac{s}{s-1}
=
\int_1^\infty
\frac{1-v^{-1}}{\log v}\,v^{-s}\,dv.
\tag{2.7}
\]
Furthermore,
\[
\sum_{d\le K}\mu(d)L_0(X/d)
=
\frac1{2\pi i}
\int_{c-iT}^{c+iT}
F_K(s)G(s)\frac{X^s}{s}\,ds
+O\!\left(\frac{X(\log X)^2}{T}\right).
\tag{2.8}
\]

**Proof.** Substituting \(v=e^w\) gives
\[
\int_1^\infty
\frac{1-v^{-1}}{\log v}v^{-s}\,dv
=
\int_0^\infty
\frac{e^{-(s-1)w}-e^{-sw}}{w}\,dw
=\log\frac{s}{s-1}
\]
by Frullani’s integral.

Apply (2.1) after interchanging the absolutely convergent \(v\)- and \(s\)-integrals. For \(z=X/d\), the individual error is
\[
\ll
\int_1^\infty
\frac{1-v^{-1}}{\log v}
\left(\frac zv\right)^c
\min\left(1,\frac1{T|\log(z/v)|}\right)dv.
\tag{2.9}
\]
In \(z/2\le v\le2z\), split at \(|v-z|=z/T\) and use
\[
|\log(z/v)|\asymp |v-z|/z.
\]
This gives \(O(z\log(2T)/T)\). Outside that range the logarithm is bounded away from zero, and integration using \(c-1=1/\log X\) gives
\[
O\!\left(\frac{z\log\log(3z)}T\right).
\]
Since \(X/d\ge X/K\asymp\sqrt X\),
\[
\sum_{d\le K}\frac{X/d}{T}
\bigl(\log(2T)+\log\log X\bigr)
\ll\frac{X(\log X)^2}{T}.
\]
This proves (2.8). ∎

Subtracting (2.8) from (2.2), we obtain
\[
\sum_{d\le K}\mu(d)
\bigl(J(X/d)-L_0(X/d)\bigr)
=
\frac1{2\pi i}
\int_{c-iT}^{c+iT}
F_K(s)H(s)\frac{X^s}{s}\,ds
+O\!\left(\frac{X(\log X)^2}{T}\right),
\tag{2.10}
\]
where
\[
H(s)=\log\zeta(s)-\log\frac{s}{s-1}
=\log\!\left(\zeta(s)\frac{s-1}{s}\right).
\tag{2.11}
\]

The function
\[
\zeta(s)\frac{s-1}{s}
\]
has a removable nonzero value \(1\) at \(s=1\). In any simply connected VK zero-free rectangle lying in \(\Re s>0\), it is analytic and nonvanishing, so (2.11) defines a single analytic branch. From (1.2)–(1.3),
\[
H(s),\quad \frac{H(s)}{\zeta(s)}
\ll(\log(V+3))^{A_1}
\tag{2.12}
\]
uniformly in a fixed interior VK region. Near \(s=1\), this follows from the removability of \(H\); away from \(1\), integrate
\[
H'(s)=\frac{\zeta'}{\zeta}(s)+\frac1{s-1}-\frac1s
\]
along a horizontal segment to \(\Re s>1\).

## 3. Completion of the Möbius polynomial

This is the load-bearing completion lemma.

### Lemma 3.1

Let \(3\le T\le K\), put
\[
U=K+\tfrac12,
\qquad
\Delta=\frac{a}{D(2T)},
\qquad
\sigma=1-\alpha\Delta,
\qquad
\eta=(1-\alpha)\Delta,
\tag{3.1}
\]
where \(0<\alpha<1\). Uniformly for
\[
z=\sigma+it,\qquad |t|\le T,
\]
one has
\[
\boxed{
F_K(z)=\frac1{\zeta(z)}+E_K(z)
}
\tag{3.2}
\]
with
\[
E_K(z)\ll
B_TU^{-\eta}\log\!\left(2+\frac T\eta\right)
+
B_T\frac{U^{\alpha\Delta}}{T\log U}
+
\frac{U^{\alpha\Delta}\log(2U)}T,
\tag{3.3}
\]
where
\[
B_T\ll(\log(2T+3))^A.
\]

In particular,
\[
E_K(z)
\ll
(\log(KT))^{A_2}
\left(
K^{-(1-\alpha)\Delta}
+\frac{K^{\alpha\Delta}}T
\right).
\tag{3.4}
\]

**Proof.** Set
\[
b=1-\sigma+\frac1{\log U}
=\alpha\Delta+\frac1{\log U}.
\tag{3.5}
\]
Then
\[
\Re(z+b)=1+\frac1{\log U}>1,
\]
so
\[
\frac1{\zeta(z+w)}
=\sum_{n\ge1}\frac{\mu(n)}{n^{z+w}}
\tag{3.6}
\]
converges absolutely on \(\Re w=b\).

Truncated Perron at the inner height \(T\) gives
\[
F_K(z)
=
\frac1{2\pi i}
\int_{b-iT}^{b+iT}
\frac{U^w}{w\zeta(z+w)}\,dw
+O(E_{\rm in}),
\tag{3.7}
\]
where
\[
E_{\rm in}\ll
\sum_{n\ge1}n^{-\sigma}
\left(\frac Un\right)^b
\min\left(1,\frac1{T|\log(U/n)|}\right).
\tag{3.8}
\]
Because \(U=K+\tfrac12\), the inequality \(n<U\) is exactly \(n\le K\), and \(|U-n|\ge\tfrac12\).

Since \(\sigma+b=1+1/\log U\), splitting (3.8) into
\[
n<U/2,\qquad U/2\le n\le2U,\qquad n>2U
\]
gives
\[
E_{\rm in}\ll
\frac{U^{1-\sigma}\log(2U)}T
=
\frac{U^{\alpha\Delta}\log(2U)}T.
\tag{3.9}
\]
Indeed, in the middle range,
\[
|\log(U/n)|\asymp |U-n|/U,
\]
and summing over half-integer distances gives a harmonic factor \(\log(2U)\); the outer ranges follow from
\[
\sum_{n>U}n^{-1-1/\log U}\ll\log U.
\]

Move the \(w\)-contour to \(\Re w=-\eta\). Every point \(q=z+w\) in the resulting rectangle satisfies
\[
|\Im q|\le |t|+T\le2T
\tag{3.10}
\]
and
\[
\Re q\ge \sigma-\eta
=1-\alpha\Delta-(1-\alpha)\Delta
=1-\Delta.
\tag{3.11}
\]
Thus the entire rectangle lies in one zero-free region defined at the doubled height \(2T\). This is the reason for using \(\Delta=\delta(2T)\), rather than a pointwise width depending on \(t\).

The only pole crossed is \(w=0\), arising from \(1/w\), and
\[
\operatorname*{Res}_{w=0}
\frac{U^w}{w\zeta(z+w)}
=\frac1{\zeta(z)}.
\tag{3.12}
\]
The point \(z+w=1\) is harmless: \(1/\zeta\) has a zero there.

On the new vertical side,
\[
\begin{aligned}
\int_{-T}^{T}
\left|
\frac{U^{-\eta+iv}}
 {(-\eta+iv)\zeta(z-\eta+iv)}
\right|\,dv
&\ll
B_TU^{-\eta}
\int_{-T}^{T}\frac{dv}{\sqrt{\eta^2+v^2}}\\
&\ll
B_TU^{-\eta}
\log\!\left(2+\frac T\eta\right).
\end{aligned}
\tag{3.13}
\]
Each horizontal side contributes
\[
\begin{aligned}
\ll
\frac{B_T}{T}
\int_{-\eta}^{b}U^u\,du
&\ll
B_T\frac{U^b}{T\log U}\\
&\ll
B_T\frac{U^{\alpha\Delta}}{T\log U}.
\end{aligned}
\tag{3.14}
\]
Equations (3.7), (3.9), and (3.12)–(3.14) prove (3.2)–(3.3). ∎

The positive term \(K^{\alpha\Delta}/T\) in (3.3) is indispensable. Omitting it is not justified by truncated Perron.

## 4. Uniformity of the doubled-height contour

Choose
\[
\alpha=1-\frac1{\log\log X}
\tag{4.1}
\]
and
\[
\log T=c(a)\Phi(X).
\tag{4.2}
\]
For large \(X\),
\[
T=X^{o(1)}\le K\asymp X^{1/2}.
\]
Set
\[
\Delta=\frac{a}{D(2T)}.
\tag{4.3}
\]
Then
\[
\Delta\log X=(c(a)+o(1))\Phi(X),
\tag{4.4}
\]
because
\[
\log\log(2T)=\left(\frac35+o(1)\right)\log\log X.
\]

Replacing \(T\) by \(2T\) changes \(D(T)\) by a factor \(1+o(1)\), and therefore causes no loss in the constant in (4.4). More importantly, the definition using \(2T\) gives a single width valid for every inner point \(z+w\), including those for which \(t\) and \(\Im w\) have the same sign. No local-width assertion is used.

Also,
\[
\log K=\frac12\log X+O(1)
\tag{4.5}
\]
because \(K\asymp\sqrt X\).

## 5. The exact \(s=1\) residue cancellation

Although the final \(\pi\)-argument is most cleanly written with \(H(s)\), the exact pole cancellation in the original \(\psi\)-form is as follows.

Let
\[
A_\psi(X,K)=
\sum_{d\le K}\mu(d)
\left(\psi(X/d)-\frac Xd\right).
\tag{5.1}
\]
The outer Perron formula gives
\[
\sum_{d\le K}\mu(d)\psi(X/d)
=
\frac1{2\pi i}
\int_{c-iT}^{c+iT}
F_K(s)\left(-\frac{\zeta'}{\zeta}(s)\right)
\frac{X^s}{s}\,ds
+O\!\left(\frac{X(\log X)^2}{T}\right).
\tag{5.2}
\]
When the contour is moved to
\[
\Re s=\sigma=1-\alpha\Delta,
\]
the only singularity crossed is \(s=1\). Since
\[
-\frac{\zeta'}{\zeta}(s)
=\frac1{s-1}+O(1),
\]
its residue is exactly
\[
\operatorname*{Res}_{s=1}
F_K(s)\left(-\frac{\zeta'}{\zeta}(s)\right)
\frac{X^s}{s}
=
XF_K(1)
=
X\sum_{d\le K}\frac{\mu(d)}d.
\tag{5.3}
\]
This cancels, term for term and without estimation, the explicitly subtracted quantity
\[
X\sum_{d\le K}\frac{\mu(d)}d.
\tag{5.4}
\]

After completion,
\[
F_K(s)\left(-\frac{\zeta'}{\zeta}(s)\right)
=
-\frac{\zeta'(s)}{\zeta(s)^2}
+
E_K(s)\left(-\frac{\zeta'}{\zeta}(s)\right),
\tag{5.5}
\]
and
\[
-\frac{\zeta'}{\zeta^2}
=\left(\frac1\zeta\right)'.
\tag{5.6}
\]
Thus no estimate for \(\sum_{d\le K}\mu(d)/d\) enters the argument.

The horizontal sides are
\[
\ll \frac{X(\log X)^{A_3}}T.
\tag{5.7}
\]
Indeed, for \(\sigma\le u\le c\),
\[
|F_K(u+iT)|
\le
\sum_{d\le K}d^{-u}
\ll
K^{\max(1-u,0)}\log(2K),
\]
and
\[
X^uK^{1-u}=K(X/K)^u
\]
is increasing in \(u\), while \(X^c\asymp X\).

The same estimates used below therefore give
\[
A_\psi(X,K)
\ll_\varepsilon
X\exp\!\left(-(1-\varepsilon)c_0\Phi(X)\right).
\tag{5.8}
\]

## 6. The centered \(J\)-sum

Return to (2.10). Move its contour from \(\Re s=c\) to
\[
\Re s=\sigma=1-\alpha\Delta.
\tag{6.1}
\]

There is no singularity at \(s=1\): subtracting \(G(s)\) has replaced the logarithmic singularity of \(\log\zeta(s)\) by the analytic function
\[
H(s)=\log\!\left(\zeta(s)\frac{s-1}{s}\right).
\]
This is the logarithmic counterpart of the exact residue cancellation in Section 5.

The two horizontal sides contribute
\[
\ll \frac{X(\log X)^{A_4}}T
\tag{6.2}
\]
by the same estimate as (5.7), now using \(H(s)\ll(\log T)^{A_1}\).

On the vertical side, insert Lemma 3.1:
\[
F_K(s)H(s)
=
\frac{H(s)}{\zeta(s)}+E_K(s)H(s).
\tag{6.3}
\]
Consequently,
\[
\begin{aligned}
\int_{\sigma-iT}^{\sigma+iT}
F_K(s)H(s)\frac{X^s}{s}\,ds
\ll (\log X)^{A_5}\bigg(
&X^\sigma\\
&+X^\sigma K^{-\eta}\\
&+X^\sigma\frac{K^{\alpha\Delta}}T
\bigg).
\end{aligned}
\tag{6.4}
\]
Here the integral of \(1/|s|\) contributes only \(O(\log(2T))\), already absorbed into the polylogarithmic factor.

The three exponential factors are, using (4.4)–(4.5),
\[
X^\sigma
=
X\exp\!\left(-\alpha\Delta\log X\right)
=
X\exp\!\left(
-(\alpha c(a)+o(1))\Phi(X)
\right),
\tag{6.5}
\]
\[
\begin{aligned}
X^\sigma K^{-\eta}
&=
X\exp\!\left(
-\alpha\Delta\log X
-(1-\alpha)\Delta\log K
\right)\\
&=
X\exp\!\left(
-\left(\frac{1+\alpha}{2}c(a)+o(1)\right)\Phi(X)
\right),
\end{aligned}
\tag{6.6}
\]
and
\[
\begin{aligned}
X^\sigma\frac{K^{\alpha\Delta}}T
&=
X\exp\!\left(
-\alpha\Delta(\log X-\log K)-\log T
\right)\\
&=
X\exp\!\left(
-\left(1+\frac{\alpha}{2}+o(1)\right)c(a)\Phi(X)
\right).
\end{aligned}
\tag{6.7}
\]
The last expression is stronger than the required bound.

The outer Perron error and both outer horizontal sides satisfy
\[
\frac{X(\log X)^{A_6}}T
=
X\exp\!\left(
-(c(a)+o(1))\Phi(X)
\right).
\tag{6.8}
\]

Because
\[
\alpha=1-\frac1{\log\log X}=1-o(1)
\]
and every fixed power of \(\log X\) is
\[
\exp(o(\Phi(X))),
\]
(2.10) and (6.2)–(6.8) yield
\[
\boxed{
\sum_{d\le K}\mu(d)
\bigl(J(X/d)-L_0(X/d)\bigr)
\ll_\varepsilon
X\exp\!\left(
-(1-\varepsilon/3)c_0\Phi(X)
\right).
}
\tag{6.9}
\]

This is the final product-form contour estimate. The full constant comes from \(X^\sigma\), while the completed Möbius factor never reintroduces the loss \(K^{1-\sigma}\).

## 7. The \(\pi\)-to-\(\psi\) bridge

The passage from \(J\) to \(\pi\) accounts for prime powers. For \(u\ge3\),
\[
J(u)-\pi(u)
=
\sum_{\substack{p^m\le u\\m\ge2}}\frac1m.
\tag{7.1}
\]
Using the elementary Chebyshev bound \(\pi(v)\ll v/\log(2v)\), or just \(\pi(v)\le v\),
\[
J(u)-\pi(u)\ll \sqrt u\,\log(2u).
\tag{7.2}
\]
Therefore
\[
\begin{aligned}
\sum_{d\le K}|J(X/d)-\pi(X/d)|
&\ll
\sqrt X\log X
\sum_{d\le K}d^{-1/2}\\
&\ll
\sqrt{XK}\log X\\
&\ll X^{3/4}\log X.
\end{aligned}
\tag{7.3}
\]
This is the announced \(x^{3/4}\log x\) cost. The sharper \(O(X^{3/4})\) bound is available, but is unnecessary.

This is legitimately a \(\pi\)-to-\(\psi\) bridge: \(J\) is the logarithmically weighted Stieltjes integral of \(\psi\),
\[
J(u)=\int_{2^-}^{u}\frac{d\psi(v)}{\log v},
\]
and (7.1) removes the prime-power part of that measure.

Next,
\[
L_0(u)-\operatorname{Li}(u)
=
-\log\log u+C_{\operatorname{Li}},
\tag{7.4}
\]
for \(u\ge3\), where the constant depends only on the conventional additive normalization of \(\operatorname{Li}\). This follows by differentiating:
\[
L_0'(u)-\operatorname{Li}'(u)
=-\frac1{u\log u}.
\]
Hence
\[
\sum_{d\le K}
|L_0(X/d)-\operatorname{Li}(X/d)|
\ll K\log\log X
\ll X^{1/2}\log\log X.
\tag{7.5}
\]

Both (7.3) and (7.5) are negligible compared with
\[
X\exp\!\left(-(1-\varepsilon)c_0\Phi(X)\right),
\tag{7.6}
\]
because \(\Phi(X)=o(\log X)\).

## 8. Floors and completion of the proof

Let
\[
N=\lfloor x\rfloor,\qquad X=N+\tfrac12.
\]
For every integer \(d\ge1\),
\[
\left\lfloor\frac{x}{d}\right\rfloor
=
\left\lfloor\frac Nd\right\rfloor
=
\left\lfloor\frac Xd\right\rfloor.
\tag{8.1}
\]
Since \(J\) and \(\pi\) are step functions supported on integers,
\[
J(X/d)=J\!\left(\left\lfloor\frac{x}{d}\right\rfloor\right),
\qquad
\pi(X/d)=\pi\!\left(\left\lfloor\frac{x}{d}\right\rfloor\right).
\tag{8.2}
\]

Moreover, because
\[
\left\lfloor\frac{x}{d}\right\rfloor
\ge \frac{x}{K}-1\asymp\sqrt x,
\]
the mean-value theorem gives
\[
\left|
\operatorname{Li}(X/d)
-
\operatorname{Li}\!\left(\left\lfloor\frac{x}{d}\right\rfloor\right)
\right|
\ll\frac1{\log x}.
\tag{8.3}
\]
Summing (8.3) over \(d\le K\) costs
\[
O\!\left(\frac K{\log x}\right)
=O\!\left(\frac{\sqrt x}{\log x}\right).
\tag{8.4}
\]

Combining (6.9), (7.3), (7.5), and (8.4) gives
\[
\begin{aligned}
\left|
\sum_{d\le K}\mu(d)
R\!\left(\left\lfloor\frac{x}{d}\right\rfloor\right)
\right|
\ll_\varepsilon\;&
X\exp\!\left(
-(1-\varepsilon/3)c_0\Phi(X)
\right)\\
&+X^{3/4}\log X
+X^{1/2}\log\log X.
\end{aligned}
\tag{8.5}
\]
Since \(X=x+O(1)\),
\[
\Phi(X)=\Phi(x)+o(1),
\]
and the last two terms are absorbed into the first with any fixed loss in the exponent. Finally, the implied constant in (8.5) is absorbed by replacing \(\varepsilon/3\) with \(\varepsilon\) and increasing \(x_0(\varepsilon)\). Thus
\[
\left|
\sum_{d\le K}\mu(d)
R\!\left(\left\lfloor\frac{x}{d}\right\rfloor\right)
\right|
\le
x\exp\!\left(
-(1-\varepsilon)c_0\Phi(x)
\right)
\]
for all \(x\ge x_0(\varepsilon)\). This proves Theorem A. ∎

## Weakest step

The weakest step is the normalization transfer in Section 1: the symbol \(c_0\) must refer to the constant obtained from one specified VK zero-free-region normalization, with the reciprocal and logarithmic-derivative bounds uniform on a fixed interior region. If \(c_0\) is instead defined as an unattained supremum over all normalizations, the proof establishes every smaller constant—exactly the stated \((1-\varepsilon)c_0\)—but not the endpoint \(c_0\) itself. All Perron truncations, doubled-height bookkeeping, the \(s=1\) cancellation, and the \(\pi\)-bridge were proved explicitly above rather than being included in this convention.

Codex session ID: 019fe7af-203e-7410-8a0c-51f29b478fff
Resume in Codex: codex resume 019fe7af-203e-7410-8a0c-51f29b478fff
