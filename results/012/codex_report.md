## 1. EXACT SETUP

Let

\[
e(t):=e^{2\pi i t},\qquad
M(d):=\sum_{m\le d}\mu(m),\qquad
X_n:=(n+1)^2-1=n(n+2).
\]

Fix integers \(N\ge1\), \(1\le H\le N\), \(D\ge1\), and a cutoff \(y\ge2\). Put

\[
\mathcal D_D:=\{d\in\mathbb Z:D<d\le2D,\ d\le X_N/(y+1)\}.
\]

For \(x\ge1\), define

\[
B_d(x):=\left\lfloor\frac{x}{d}\right\rfloor,\qquad
A_d(x):=\max\left(y,\left\lfloor\frac{x}{d+1}\right\rfloor\right),
\]

and, matching the numerical convention used by this program,

\[
\Delta_d(x):=
\bigl(\pi(B_d(x))-\pi(A_d(x))\bigr)
-\bigl(\operatorname{Li}(B_d(x))-\operatorname{Li}(A_d(x))\bigr).
\]

Thus \(\Delta_d(x)\) is the PNT-centered prime discrepancy on

\[
A_d(x)<p\le B_d(x).
\]

The windowed second moment is

\[
\mathcal S_{N,H,D}
:=
\sum_{0\le r<H}
\left|
\sum_{d\in\mathcal D_D}M(d)\Delta_d(X_{N+r})
\right|^2.
\]

Since \(M(d)\) and \(\Delta_d\) are real,

\[
\mathcal S_{N,H,D}
=
\sum_{d,d'\in\mathcal D_D}M(d)M(d')
\sum_{0\le r<H}
\Delta_d(X_{N+r})\Delta_{d'}(X_{N+r}).
\]

Hence the divisor off-diagonal is exactly

\[
\mathcal O_{N,H,D}
=
\sum_{\substack{d,d'\in\mathcal D_D\\d\ne d'}}
M(d)M(d')
\sum_{0\le r<H}
\Delta_d(X_{N+r})\Delta_{d'}(X_{N+r}).
\]

There is an important formulation caveat. **[proved inline]** The raw function \(x\mapsto\Delta_d(x)\) is not periodic modulo \(d\): its endpoints and prime counts grow with \(x\). Therefore it cannot, globally and exactly, equal a finite sum \(\sum_{a\bmod d}c_d(a)e(ax/d)\), since every such sum is \(d\)-periodic. Records 005, 010, and 011 do not specify the Vaughan/Heath–Brown decomposition that is supposed to produce such packets.

The strongest honest formulation is consequently packetwise. Suppose a chosen decomposition and completion gives

\[
\Delta_d(X_n)=K_d(n)+R_d(n),
\]

where \(K_d\) is a completed \(d\)-periodic packet and \(R_d\) contains all other packets and completion errors. Finite Fourier inversion then gives exactly

\[
K_d(n)=\sum_{a=0}^{d-1}\gamma_d(a)e\!\left(\frac{aX_n}{d}\right)
      =\sum_{a=0}^{d-1}c_d(a)e\!\left(\frac{a(n+1)^2}{d}\right),
\]

where

\[
c_d(a):=\gamma_d(a)e(-a/d).
\]

**[standard-with-citation]** This is ordinary finite Fourier inversion/completion; see Iwaniec–Kowalski, *Analytic Number Theory*, §12.2, “Completing methods” ([book PDF](https://unina2.on-line.it/sebina/repository/catalogazione/documenti/Iwaniec%2C%20Kowalski%20-%20Analytic%20Number%20Theory.pdf)).

The completed-packet contribution to the off-diagonal is therefore

\[
\sum_{\substack{d,d'\in\mathcal D_D\\d\ne d'}}
M(d)M(d')
\sum_{a\bmod d}\sum_{a'\bmod d'}
c_d(a)\overline{c_{d'}(a')}
\sum_{0\le r<H}
e\!\left(
\left(\frac ad-\frac{a'}{d'}\right)(N+r+1)^2
\right).
\]

This is exactly where the requested quadratic phase occurs.

For a tuple \(T=(d,d',a,a')\), put

\[
h(T):=ad'-a'd,\qquad L(T):=dd'.
\]

When \(h(T)\ne0\), let

\[
g(T):=\gcd(|h(T)|,L(T)),\qquad
b(T):=\frac{h(T)}{g(T)},\qquad
q(T):=\frac{L(T)}{g(T)}.
\]

Then

\[
\frac ad-\frac{a'}{d'}=\frac{b(T)}{q(T)},
\qquad
\gcd(b(T),q(T))=1,
\]

and the inner sum is

\[
\sum_{0\le r<H}
e\!\left(\frac{b(T)}{q(T)}(N+r+1)^2\right).
\]

All later conclusions concern this completed-packet index set. A support-sensitive theorem involving the actual nonzero \(c_d(a)\) would require the missing explicit decomposition.

## 2. THE MAP

For \(q\ge2\) and \(w\in\mathbb Z/q\mathbb Z\), define

\[
R_q(w):=\{\xi\in\mathbb Z/q\mathbb Z:\xi^2\equiv w\pmod q\},
\qquad
\rho_q(w):=|R_q(w)|.
\]

For a reduced phase \(b/q\), the phase at \(x=N+r+1\) is \(e(bx^2/q)\). Because \(b\) is invertible modulo \(q\),

\[
e(bx^2/q)=e(bw/q)
\quad\Longleftrightarrow\quad
x^2\equiv w\pmod q.
\]

Thus the roots of

\[
\xi^2\equiv w\pmod q
\]

parameterize sample residues \(N+r+1\bmod q\) having a fixed phase value. They do not parameterize the divisor-frequency tuples.

For each fixed \(r\), the maximally informative natural tuple-to-root map is

\[
\Phi_r(d,d',a,a')
=
\left(
q(T);
\ b(T),\
w_r(T),\
\xi_r(T)
\right),
\]

where

\[
\xi_r(T):=N+r+1\pmod {q(T)},\qquad
w_r(T):=\xi_r(T)^2\pmod {q(T)}.
\]

Here \((b,w,\xi)\) is the “root datum,” with \(\xi\in R_q(w)\). Including \(b\) makes fibers smaller than omitting it, so this is the favorable formulation for a bounded-fiber claim.

Before applying \(\Phi_r\), remove:

- \(d=d'\), the divisor diagonal;
- \(h(T)=0\), equivalently \(a/d=a'/d'\), the zero-frequency locus;
- tuples whose completed coefficient \(c_d(a)c_{d'}(a')\) vanishes, if that support is known;
- an explicitly declared major-arc set \(q(T)\le Q_0\), if desired.

One may also exclude \(a=0\), \(a'=0\), and require

\[
\gcd(a,d)=\gcd(a',d')=1.
\]

The negative theorem below survives all these additional restrictions and survives removal of every fixed major-arc range \(q\le Q_0\).

## 3. FIBER THEOREM

### Correct root-count statement

Let \(\omega(q)\) be the number of distinct prime divisors of \(q\).

**Theorem A [proved inline].** For \(q\ge1\):

\[
\rho_q(w)\le
\begin{cases}
2^{\omega(q)},&q\text{ squarefree},\\[2mm]
2^{\omega(q)},&q\text{ odd and }\gcd(w,q)=1,\\[2mm]
2^{\omega(q)+1},&\gcd(w,q)=1,\\[2mm]
2^{\omega(q)+1}\sqrt{\gcd(w,q)},&\text{without additional hypotheses}.
\end{cases}
\]

Proof:

1. **[proved inline] CRT step.** If \(q=\prod p^\nu\), the Chinese remainder bijection sends a root modulo \(q\) to an independent tuple of roots modulo the \(p^\nu\). Hence

   \[
   \rho_q(w)=\prod_{p^\nu\parallel q}\rho_{p^\nu}(w).
   \]

2. **[proved inline] Odd-prime unit roots.** If \(p\) is odd and \(x,y\) are unit roots of \(z^2\equiv w\pmod {p^\nu}\), then
   \(p^\nu\mid(x-y)(x+y)\). Since \(p\) cannot divide both \(x-y\) and \(x+y\), either \(x\equiv y\) or \(x\equiv-y\pmod {p^\nu}\). Thus there are at most two unit roots.

3. **[proved inline] The 2-adic unit case.** Modulo \(2\) there is at most one unit root, modulo \(4\) at most two, and modulo \(2^\nu\), \(\nu\ge3\), at most four. Indeed, for two odd roots \(x,y\), the valuations of \(x-y\) and \(x+y\) cannot both exceed \(1\); from \(2^\nu\mid(x-y)(x+y)\) one obtains \(y\equiv\pm x\pmod {2^{\nu-1}}\), producing at most the four lifts \(x,-x,x+2^{\nu-1},-x+2^{\nu-1}\).

4. **[proved inline] Nonunit roots.** Put

   \[
   t=\min(v_p(w),\nu).
   \]

   If \(t<\nu\) is odd, there are no roots. If \(t=2s<\nu\), write \(x=p^sy\); every unit root modulo \(p^{\nu-2s}\) has \(p^s\) lifts modulo \(p^{\nu-s}\). Hence

   \[
   \rho_{p^\nu}(w)\le
   \begin{cases}
   2p^{t/2},&p\text{ odd},\\
   4\cdot2^{t/2},&p=2.
   \end{cases}
   \]

   If \(w\equiv0\pmod {p^\nu}\), then \(p^{\lceil\nu/2\rceil}\mid x\), giving \(p^{\lfloor\nu/2\rfloor}\le p^{\nu/2}\) roots. Multiplying the local estimates gives the uniform bound.

5. **[proved inline] Specializations.** For coprime \(w\), all \(t=0\); the odd local factors contribute at most \(2\), while the 2-part contributes at most \(4\). If \(q\) is squarefree, each prime modulus contributes at most two roots even when \(p\mid w\). This proves all four displayed bounds.

These are correct bounds for sample residues. They are not fiber bounds for divisor-frequency tuples.

### Actual fiber theorem: unboundedness

Define

\[
\mathcal F_D(b,q)
:=
\left\{
(d,d',a,a'):
\begin{array}{l}
D<d,d'\le2D,\quad d\ne d',\\
1\le a<d,\quad1\le a'<d',\\
\gcd(a,d)=\gcd(a',d')=1,\\
a/d-a'/d'=b/q
\end{array}
\right\}.
\]

**Theorem B [proved inline].** For every fixed major-arc cutoff \(Q_0\), there exist a fixed reduced fraction \(1/q\), with \(q>Q_0\), and arbitrarily large \(D\) for which

\[
|\mathcal F_D(1,q)|\longrightarrow\infty.
\]

Consequently neither \(\rho_q(w)\) nor
\(2^{\omega(q)+1}\sqrt{\gcd(w,q)}\) bounds the fibers of \(\Phi_r\).

Proof:

1. **[proved inline] Choice beyond the major arcs.** Choose an integer \(t\ge2\) with

   \[
   q:=t(t+1)>Q_0.
   \]

2. **[proved inline] Explicit tuples.** For every integer \(\ell\ge1\), set

   \[
   m=q\ell-1,\quad
   d=(t+1)m,\quad d'=tm,\quad
   a=(t+1)\ell+1,\quad a'=1.
   \]

   Direct calculation gives

   \[
   \frac ad-\frac{a'}{d'}
   =
   \frac{ta-(t+1)}{t(t+1)m}
   =
   \frac{t(t+1)\ell-1}{qm}
   =
   \frac1q.
   \]

3. **[proved inline] No degeneracy.** Both frequencies are nonzero and \(d\ne d'\). Moreover,

   \[
   a\equiv1\pmod {t+1},\qquad ta-m=t+1.
   \]

   Therefore \(\gcd(a,t+1)=1\) and every common divisor of \(a\) and \(m\) divides \(t+1\), so \(\gcd(a,m)=1\). Hence \(\gcd(a,d)=1\); also \(\gcd(a',d')=1\).

4. **[proved inline] Many tuples in one dyadic block.** Both \(d,d'\) lie in \((D,2D]\) whenever

   \[
   \frac Dt<m=q\ell-1\le\frac{2D}{t+1}.
   \]

   The corresponding interval for \(\ell\) has length

   \[
   \frac{D(t-1)}{q^2}.
   \]

   It therefore contains at least \(D(t-1)/q^2-1\) integers. Thus

   \[
   |\mathcal F_D(1,q)|
   \ge \frac{D(t-1)}{q^2}-1,
   \]

   which is unbounded with \(D\), while \(q\) remains fixed.

5. **[proved inline] Root data cannot repair the fiber.** For fixed \(q,b,w\), there are only \(\rho_q(w)\) roots. Any assignment of these tuples to those roots has a fiber of size at least
   \(|\mathcal F_D(1,q)|/\rho_q(w)\), which tends to infinity. Even allowing \(w\) to vary gives only the \(q\) data \((w,\xi)=(\xi^2,\xi)\), so some fiber is at least \(|\mathcal F_D(1,q)|/q\).

This proves genuine fiber growth, including beyond every fixed major-arc cutoff and after imposing primitive, nonzero frequencies.

## 4. VERIFICATION

### (a) The counterexample moduli

For \(q=8\),

\[
x^2\bmod8=(0,1,4,1,0,1,4,1)
\quad(x=0,\ldots,7).
\]

Thus

\[
R_8(0)=\{0,4\},\quad
R_8(1)=\{1,3,5,7\},\quad
R_8(4)=\{2,6\}.
\]

In particular,

\[
\rho_8(1)=4>2^{\omega(8)}=2.
\]

The naive bound fails. Since \(\gcd(1,8)=1\), the corrected arbitrary-\(q\) coprime bound is

\[
2^{\omega(8)+1}=4,
\]

and is sharp.

For \(q=9\),

\[
x^2\bmod9=(0,1,4,0,7,7,0,4,1).
\]

Thus

\[
R_9(0)=\{0,3,6\},
\]

so

\[
\rho_9(0)=3>2^{\omega(9)}=2.
\]

Again the naive bound fails. The uniform corrected bound gives

\[
2^{\omega(9)+1}\sqrt{\gcd(0,9)}
=4\sqrt9=12,
\]

which holds. For comparison, \(R_9(1)=\{1,8\}\), and the sharper odd, coprime bound \(2^{\omega(9)}=2\) is exact.

### (b) Exact fiber enumeration

I used the declared block

\[
D=8,\qquad \mathcal D_8=\{9,10,\ldots,16\},
\]

with

\[
N=20,\qquad H=8,\qquad N+r+1=21,\ldots,28.
\]

The arithmetic was exact integer arithmetic: every ordered tuple with \(d\ne d'\), \(0\le a<d\), and \(0\le a'<d'\) was reduced using integer gcd, the zero difference was discarded, and tuples were grouped by the exact pair \((q,b)\). No repository file was created. All \(M(d)\) for \(9\le d\le16\) are nonzero, so no divisor disappears merely from its Mertens weight.

Results:

| Quantity | Exact result |
|---|---:|
| Nonzero ordered tuples | 8,616 |
| Distinct \((q,b)\) fibers | 2,402 |
| Largest reduced denominator | 240 |
| Maximum fiber | 43 |
| Labels attaining maximum | \((q,b)=(6,\pm1)\) |
| Maximum fiber at \(q=8\) | 17 |
| Maximum fiber at \(q=9\) | 15 |

For the maximal \(q=6\) fiber, the window comparison is:

| \(N+r+1\) | \(w=(N+r+1)^2\bmod6\) | \(\rho_6(w)\) | Corrected uniform bound | Tuple fiber |
|---:|---:|---:|---:|---:|
| 21 | 3 | 1 | \(8\sqrt3\) | 43 |
| 22 | 4 | 2 | \(8\sqrt2\) | 43 |
| 23 | 1 | 2 | \(8\) | 43 |
| 24 | 0 | 1 | \(8\sqrt6\) | 43 |
| 25 | 1 | 2 | \(8\) | 43 |
| 26 | 4 | 2 | \(8\sqrt2\) | 43 |
| 27 | 3 | 1 | \(8\sqrt3\) | 43 |
| 28 | 4 | 2 | \(8\sqrt2\) | 43 |

At the first sample \(x=21\):

- \(q=8,w=1\): root bound \(4\), but maximum tuple fiber \(17\);
- \(q=9,w=0\): uniform root bound \(12\), but maximum tuple fiber \(15\).

Thus even the corrected root bounds do not bound the enumerated tuple fibers. They bound the number of sample roots, exactly as Theorem A says.

As a robustness check, imposing \(a,a'>0\) and individual primitivity leaves 2,888 tuples and 1,390 outputs; the largest small-block fiber is already \(6\), attained at \(q=6\) and \(q=30\). Theorem B proves that these primitive fibers subsequently grow without bound.

## 5. THE SIZE QUESTION

Let \(g_0=\gcd(d,d')\). Since \(g_0\mid ad'-a'd\),

\[
q(T)\mid\frac{dd'}{g_0}=\operatorname{lcm}(d,d').
\]

Therefore **[proved inline]**

\[
q(T)\le\operatorname{lcm}(d,d')\le dd'\le4D^2.
\]

This quadratic bound is sharp in scale. Take

\[
d=2D-1,\qquad d'=2D,\qquad a=a'=1.
\]

The denominators are coprime and

\[
\frac1{2D-1}-\frac1{2D}
=
\frac1{2D(2D-1)},
\]

so

\[
q=2D(2D-1)=4D^2-2D.
\]

For the enumerated block \(D=8\), this gives the observed maximum \(q=15\cdot16=240\).

Hence the denominators are:

- bounded by \(4D^2\);
- not bounded by \(O(D)\);
- capable of reaching order \(D^2\);
- genuinely unbounded as \(D\to\infty\);
- not proved to divide any prime-wheel torus modulus or to occupy a small packet-conductor range.

This does not feed the parent proposal’s Heath–Brown step at the claimed \(D\)-scale. Heath–Brown’s Theorem 1 averages real characters over positive odd squarefree moduli \(m\le M\), with a cost involving \(M+N\); replacing the intended modulus scale \(D\) by the actual possible scale \(D^2\) is a material loss, not notation. The present \(q\)'s may also be even or nonsquarefree, and no derivation has converted their additive quadratic phases into the required real-character family. See D. R. Heath-Brown, “A mean value estimate for real character sums,” *Acta Arithmetica* 72 (1995), Theorem 1 ([journal record](https://www.impan.pl/en/publishing-house/journals-and-series/acta-arithmetica/all/72/3/108575/a-mean-value-estimate-for-real-character-sums)).

## 6. VERDICT LINE

MAP-FAILS (for any fixed major-arc cutoff, choose \(q=t(t+1)\) beyond it and the primitive tuples \(m=q\ell-1,\ d=(t+1)m,\ d'=tm,\ a=(t+1)\ell+1,\ a'=1\); their common difference is \(1/q\) and their fiber grows at least linearly in \(D\)).

Angle G2’s proposed transfer is not viable in its present form: quadratic roots control repetitions of the sampling residue, not multiplicities of divisor-frequency pairs, and the actual conductors reach order \(D^2\). The next gate should be the \(H=1\) exponent-flow audit; it is cheaper and more decisive than further completion work because it tests whether any repaired dispersion architecture can contract the Mertens exponent after the claimed bounded-fiber mechanism has been removed.

Codex session ID: 019fe724-d1b2-7622-8355-897ea60ecafe
Resume in Codex: codex resume 019fe724-d1b2-7622-8355-897ea60ecafe
