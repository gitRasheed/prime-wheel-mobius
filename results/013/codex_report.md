The \(H=1\) route does not contract. Even granting the most favorable version of the conjectured QSRD estimate—ignoring the failed fibers and pretending conductors remain harmless—the self-map is

\[
\boxed{F_0(\sigma)=\frac58+\frac{\sigma}{4}},
\]

and

\[
F_0(\sigma)-\sigma
=\frac58-\frac{3\sigma}{4}
\ge \frac14
\qquad (0<\sigma\le\tfrac12).
\]

The true \(q\asymp D^2\) conductor and unbounded fibers only worsen this.

## 1. Normalization and inductive input

Write

\[
x=X_N=N(N+2)\asymp N^2,\qquad
T_D(n):=\sum_{D<d\le2D}M(d)\Delta_d(X_n).
\]

The requested inductive hypothesis is

\[
E_\sigma(D):=\sum_{d\le D}M(d)^2
\ll_\varepsilon D^{1+2\sigma+\varepsilon}.
\]

Hence

\[
\|M\|_{2,(D,2D]}
\le E_\sigma(2D)^{1/2}
\ll_\varepsilon D^{1/2+\sigma+\varepsilon}.
\tag{1}
\]

Status: **[proved algebraically from the stated input]**.

The parent’s \(D^{3/2}\) term is exactly (1) at the classical near-trivial exponent \(\sigma=1\):

\[
D^{1/2+\sigma}\big|_{\sigma=1}=D^{3/2}.
\]

Thus the only sigma-sensitive replacement consistent with the parent’s stated “Mertens enters through \(\ell^2\)” architecture is

\[
D^{3/2}\rightsquigarrow D^{1/2+\sigma}.
\tag{2}
\]

Status: **[conjectured architecture step]**. QSRD itself was never proved, and no decomposition was supplied showing linear dependence on this norm.

## 2. Optimistic \(H=1\) self-map

Grant the strongest favorable sigma-dependent QSRD:

\[
\sum_{r<H}|T_D(N+r)|^2
\ll_\varepsilon
N^{2+\varepsilon}
\left(H+D^{1/2+\sigma}\right).
\tag{3}
\]

This deliberately charges:

- no true-conductor penalty;
- no fiber penalty;
- no completion-coefficient or remainder loss.

At \(H=1\), the critical reciprocal range is \(D\asymp N\). Therefore

\[
|T_N(N)|^2
\ll N^{2+\varepsilon}N^{1/2+\sigma}
=N^{5/2+\sigma+\varepsilon}.
\]

Taking square roots,

\[
|T_N(N)|
\ll N^{5/4+\sigma/2+\varepsilon}.
\]

Since \(x\asymp N^2\),

\[
N^{5/4+\sigma/2}
=x^{\,5/8+\sigma/4},
\]

so

\[
\boxed{F_0(\sigma)=\frac58+\frac{\sigma}{4}}.
\tag{4}
\]

The fixed point is

\[
F_0(\sigma)=\sigma
\iff \frac58=\frac{3\sigma}{4}
\iff \sigma=\frac56.
\]

Thus even if the intended bootstrap were started from the classical \(\sigma=1\), it could at best iterate toward \(5/6\), not \(1/2\). On the specified interval \(0<\sigma\le1/2\), it strictly expands by at least \(1/4\).

For comparison, retaining the parent’s original \(D^{3/2}\) gives

\[
|T_N(N)|^2\ll N^{7/2+\varepsilon},
\qquad
|T_N(N)|\ll N^{7/4+\varepsilon}
=x^{7/8+\varepsilon}.
\tag{5}
\]

That is the explicit surviving \(D^{3/2}\)-loss kill condition.

Status of (3): **[conjectured]**. Status of (4)–(5): **[proved exponent arithmetic conditional on (3)/QSRD]**.

## 3. Completion and conductor losses

### \(H=1\) completion

For every reduced \(b/q\),

\[
\left|\sum_{0\le r<1}
e\!\left(\frac bq(N+r+1)^2\right)\right|=1.
\tag{6}
\]

Therefore quadratic completion supplies exactly \(q^0\): no loss if the trivial bound is used, but also no cancellation.

Status: **[proved exactly]**.

The standard incomplete quadratic estimate is

\[
\ll \min\left\{H,\frac{H}{\sqrt q}+\sqrt q\log(2q)\right\},
\]

up to the harmless even-\(q\) factor \(\sqrt{\gcd(2b,q)}\le\sqrt2\). At \(H=1\), its completed form is worse than (6). Finite completion and Gauss sums are standard; see Iwaniec–Kowalski, §§3.4 and 12.2, [Analytic Number Theory](https://unina2.on-line.it/sebina/repository/catalogazione/documenti/Iwaniec%2C%20Kowalski%20-%20Analytic%20Number%20Theory.pdf).

Status: **[standard-with-citation]**.

### True conductor

Record 012 proves sharply that

\[
q\le4D^2,\qquad q\asymp D^2\ \text{is attained}.
\tag{7}
\]

See [codex_report.md](/mnt/d/Projects/prime-wheel-mobius/results/012/codex_report.md:454).

Suppose the character-polynomial length is \(L=N^\ell\) when \(D=N\). Heath–Brown’s quadratic large sieve has cost \(Q+L\), up to \((QL)^\varepsilon\), for the required odd squarefree real-character family. Replacing the parent’s intended \(Q=D\) by \(Q=D^2\) therefore multiplies the second moment by

\[
R_{\rm HB}
=\frac{D^2+L}{D+L}
=N^{\,\max(2,\ell)-\max(1,\ell)+o(1)}.
\tag{8}
\]

This adds one quarter of that exponent to the resulting \(x\)-exponent. The conditional self-map becomes

\[
\boxed{
F_{\rm HB}(\sigma;\ell)
=
\frac58+\frac{\sigma}{4}
+\frac{\max(2,\ell)-\max(1,\ell)}{4}.
}
\tag{9}
\]

For the raw reciprocal prime scale \(L\asymp x/D\asymp N\), so \(\ell=1\). Then

\[
R_{\rm HB}\asymp D,
\qquad
\boxed{F_{\rm HB}(\sigma)=\frac78+\frac{\sigma}{4}}.
\tag{10}
\]

Indeed,

\[
|T_N(N)|^2
\ll N^2N^{1/2+\sigma}N
=N^{7/2+\sigma},
\]

hence

\[
|T_N(N)|
\ll N^{7/4+\sigma/2}
=x^{7/8+\sigma/4}.
\]

Heath–Brown’s inequality is **[standard-with-citation]**; see Theorem 1 of [“A mean value estimate for real character sums”](https://www.impan.pl/en/publishing-house/journals-and-series/acta-arithmetica/all/72/3/108575/a-mean-value-estimate-for-real-character-sums). Its application here is **[conjectured/unavailable]**: the arising \(q\) can be even or nonsquarefree, and no conversion from the additive quadratic packets to the theorem’s real-character family has been proved.

If one instead falls back to the generic additive large sieve, its cost is \(L+Q^2\). With \(Q=D^2\) and \(L=D=N\), this is \(D^4\), versus the parent’s \(D\)-scale cost, an extra \(D^3\) in the second moment. Formally this gives

\[
F_{\rm add}(\sigma)
=\frac58+\frac{\sigma}{4}+\frac34
=\frac{11}{8}+\frac{\sigma}{4}.
\tag{11}
\]

The additive large-sieve inequality is **[standard-with-citation]**; its application is **[blocked by the missing packet coefficient model]**.

## 4. Failed-fiber loss

Let a regrouping by common frequency have maximal fiber

\[
B_D\ll D^{\beta+\varepsilon}.
\]

Cauchy–Schwarz over a fiber multiplies the second moment by \(D^\beta\), hence adds \(D^{\beta/2}\) to amplitude and \(\beta/4\) to the exponent in \(x\). The general critical-range map is therefore

\[
\boxed{
F(\sigma;\ell,\beta)
=
\frac58+\frac{\sigma}{4}
+\frac{\max(2,\ell)-\max(1,\ell)}4
+\frac{\beta}{4}.
}
\tag{12}
\]

Record 012’s explicit primitive fibers grow \(\gg D\) at fixed \(q\). Therefore any uniform absolute-fiber-count implementation must have

\[
\beta\ge1.
\tag{13}
\]

Status: **[proved in record 012]**.

With raw \(L\asymp N\), the true conductor and absolute fiber accounting give

\[
F(\sigma;1,\beta)
=\frac78+\frac{\sigma}{4}+\frac{\beta}{4}
\ge\frac98+\frac{\sigma}{4}.
\tag{14}
\]

Avoiding this \(\beta/4\) loss would require cancellation among the coefficients inside each growing fiber. No such statement exists.

Status of that proposed cancellation: **[conjectured]**.

## 5. Windowed route

Put

\[
H=N^\eta,\qquad D=N^\delta,
\qquad 0\le\eta,\delta\le1.
\]

From the favorable sigma-QSRD (3),

\[
\mathcal S_{N,H,D}
\ll
N^{2+\max\{\eta,\delta(1/2+\sigma)\}+\varepsilon}.
\tag{15}
\]

The desired window scale is

\[
HN^{2+\varepsilon}=N^{2+\eta+\varepsilon}.
\]

Thus the excess second-moment exponent is

\[
\boxed{
\Lambda_0(\sigma,\delta,\eta)
=
\left[\delta\left(\frac12+\sigma\right)-\eta\right]_+.
}
\tag{16}
\]

The favorable window closes only when

\[
\delta\left(\frac12+\sigma\right)\le\eta.
\tag{17}
\]

For the original \(D^{3/2}\) loss, equivalently \(\sigma=1\),

\[
\Lambda_{\rm original}
=\left[\frac{3\delta}{2}-\eta\right]_+,
\]

so

\[
D\le H^{2/3}.
\tag{18}
\]

At the advertised minimum \(H=N^{3/4}\), this is only

\[
D\le N^{1/2}.
\]

Therefore the parent’s restricted window lemma is arithmetically consistent, but the separate claim that summing it over every \(D\le N\) closes the full window is unsupported: the critical ranges \(N^{1/2}<D\le N\) remain.

### Window completion range

For \(q=N^\alpha\), the completed quadratic kernel has exponent

\[
\min\left\{
\eta,\,
\max\left(\eta-\frac\alpha2,\frac\alpha2\right)
\right\}.
\]

At the worst allowed conductor \(q\asymp D^2\), \(\alpha=2\delta\), so this becomes

\[
\min\{\eta,\max(\eta-\delta,\delta)\}.
\tag{19}
\]

There is no nontrivial window cancellation when

\[
\delta\ge\eta.
\tag{20}
\]

Status: **[standard completion bound plus proved substitution \(q\asymp D^2\)]**.

### Window with the true Heath–Brown conductor cost

At raw prime length

\[
L\asymp \frac{x}{D}=N^{2-\delta},
\]

the extra second-moment conductor exponent is

\[
r(\delta)
=
\max(2\delta,2-\delta)-\max(\delta,2-\delta)
=[3\delta-2]_+.
\tag{21}
\]

Thus, even granting the unproved real-character conversion and no fiber loss,

\[
\boxed{
\Lambda_{\rm HB}
=
\left[
\delta\left(\frac12+\sigma\right)
+[3\delta-2]_+
-\eta
\right]_+.
}
\tag{22}
\]

A nontrivial window route requires both

\[
\delta\left(\frac12+\sigma\right)+[3\delta-2]_+\le\eta,
\qquad
\delta<\eta.
\tag{23}
\]

For \(H=N^{3/4}\), this permits at most

\[
\delta\le
\min\left\{
\frac34,\,
\frac{11}{14+4\sigma}
\right\}.
\tag{24}
\]

Examples:

\[
\sigma=\frac12:\quad \delta\le\frac{11}{16},
\]

while as \(\sigma\downarrow0\), completion itself caps the range at \(\delta<3/4\).

For the critical \(D=N\), \(\delta=1\), the true-conductor off-diagonal exponent is

\[
\frac12+\sigma+[3-2]
=\frac32+\sigma.
\]

Since every permitted window has \(\eta\le1\),

\[
\frac32+\sigma-\eta
\ge\frac12+\sigma>0.
\tag{25}
\]

So even the maximal window \(H=N\) does not cover \(D=N\) under the corrected conductor bookkeeping. A fiber-count loss would add \(\beta\delta\) inside (22), making the range smaller still.

## 6. Loss ledger

| Term | Exponent effect | Status |
|---|---:|---|
| Inductive Mertens norm | \(D^{1/2+\sigma}\) | **proved from input** |
| Original degenerate norm | \(D^{3/2}\) at \(\sigma=1\) | **stated by parent; QSRD conjectured** |
| \(H=1\) quadratic phase | exactly \(1\), hence no gain | **proved** |
| Even-\(q\) Gauss factor | at most \(\sqrt2\) | **standard-with-citation** |
| Completion logarithm | \(\log q\ll D^\varepsilon\) | **standard** |
| True conductor | \(q\le4D^2\), sharp | **proved in 012** |
| Heath–Brown scale correction | \(R_{\rm HB}=(D^2+L)/(D+L)\) | **standard inequality; application conjectured** |
| Generic additive sieve | \(L+D^4\) | **standard inequality; application blocked** |
| Fiber multiplicity | \(+\beta/4\) in \(F\) | **algebraic; \(\beta=0\) refuted** |
| Cancellation inside fibers | would remove \(\beta\) | **conjectured, unstated** |
| Packet coefficient norms | needed to apply either sieve | **missing/conjectured** |
| Remainders \(R_d\) from completion | no bound supplied | **missing/conjectured** |
| Additive phase \(\to\) real character | required for Heath–Brown | **conjectured, presently absent** |
| Dyadic summation | \((\log N)^{O(1)}\subset N^\varepsilon\) | **standard** |
| Full-torus gain | none permitted; \(q\) is not a proved small torus packet | **ruled out by 012/modulus obstacle** |

The missing packet details prevent any of these displayed QSRD inequalities from being a theorem. They do not block the verdict: the deliberately optimistic map (4), which suppresses all those extra losses, already expands throughout the specified interval.

**NEUTRAL-OR-EXPANDS — decisive inequality: \(\displaystyle F_0(\sigma)-\sigma=\frac58-\frac{3\sigma}{4}\ge\frac14>0\) for every \(0<\sigma\le\frac12\); with the true \(q\asymp D^2\) scale, \(\displaystyle F_{\rm HB}(\sigma)=\frac78+\frac{\sigma}{4}\) is worse.**

Codex session ID: 019fe75d-8579-7f50-8cac-0eb562bcdb0a
Resume in Codex: codex resume 019fe75d-8579-7f50-8cac-0eb562bcdb0a
