K1: **LEMMA-REPAIRED-THEOREM-SURVIVES** — after replacing the pointwise-height contour by a doubled-height, global-width contour. “Same constant” means every admissible interior KV constant \((1-\varepsilon)c_0\), not an unattained endpoint constant.

K7: **KNOWN** — the unspecified-\(c>0\) KV-strength bound follows immediately from the classical pointwise KV prime-number theorem. I did not find the sharper full-\(c_0\) truncated theorem stated verbatim in the named literature.

## K1. Corrected completion lemma

Put
\[
F_K(z)=\sum_{n\le K}\frac{\mu(n)}{n^z},\qquad X=K+\tfrac12,
\]
and define the usable Vinogradov–Korobov width
\[
\delta(V)=
 \frac{a}{(\log(V+3))^{2/3}
          (\log_2(V+3))^{1/3}},
\]
where \(a>0\) is chosen strictly inside a standard VK zero-free region and \(\log_2 u=\max(1,\log\log u)\).

The standard zero-free-region input is:

\[
\zeta(q)\ne0,\qquad
\frac1{\zeta(q)},\ \frac{\zeta'}{\zeta}(q)
 \ll (\log(V+3))^A
\]
uniformly for \(|\Im q|\le V\) and
\[
\Re q\ge 1-\delta(V),
\]
after shrinking \(a\) by an arbitrary fixed or slowly vanishing margin.  
**[standard-with-citation]** This is the usual quantitative consequence of the VK zero-free region; see [Ford, *Zero-free regions for the Riemann zeta function*](https://arxiv.org/abs/1910.08205) and Titchmarsh–Heath-Brown, Chapters III and XIV, in [*The Theory of the Riemann Zeta-Function*](https://sites.math.rutgers.edu/~zeilberg/EM18/TitchmarshZeta.pdf).

### Lemma

Let \(T\ge3\), \(2\le K\), and \(T\le K\). Set
\[
\Delta=\delta(2T),\qquad
\sigma=1-\alpha\Delta,\qquad
z=\sigma+it,\quad |t|\le T,
\]
where \(0<\alpha<1\), and put
\[
\eta=(1-\alpha)\Delta.
\]
Interpret \(\Delta\) as a working width lying slightly inside the available zero-free width, so that
\[
\Re q\ge1-\Delta,\quad |\Im q|\le2T
\]
has a margin of size \(\gg(1-\alpha)\Delta\). Then, uniformly for \(|t|\le T\),
\[
\boxed{
F_K(z)=\frac1{\zeta(z)}
 +O\!\left(
 B_T X^{-\eta}\log\frac{2T}{\eta}
 +B_T\frac{X^{\alpha\Delta}}{T\log X}
 +\frac{X^{\alpha\Delta}\log(2X)}{T}
 \right),
}
\]
where \(B_T\ll(\log(2T))^A(1-\alpha)^{-A}\).

Thus, when the \(X^{\alpha\Delta}/T\) terms are subordinate,
\[
F_K(z)=\frac1{\zeta(z)}
 +O\!\left(
 K^{-(1-\alpha)\Delta}
 (\log(2KT))^{A'}
 \right).
\]

The final display is not valid without the displayed \(K^{\alpha\Delta}/T\) conditions.

### Proof

1. Take
   \[
   b=1-\sigma+\frac1{\log X}
     =\alpha\Delta+\frac1{\log X}.
   \]
   Then \(\Re(z+b)=1+1/\log X>1\), so
   \[
   \frac1{\zeta(z+w)}
     =\sum_{n\ge1}\frac{\mu(n)}{n^{z+w}}
   \]
   converges absolutely on \(\Re w=b\).  
   **[proved-inline]**

2. Truncated Perron gives
   \[
   F_K(z)
   =\frac1{2\pi i}\int_{b-iT}^{b+iT}
      \frac{X^w}{w\zeta(z+w)}\,dw+O(E_P),
   \]
   with
   \[
   E_P\ll
   \sum_{n\ge1} n^{-\sigma}\left(\frac Xn\right)^b
   \min\!\left(1,\frac1{T|\log(X/n)|}\right).
   \]
   The use of \(X=K+\frac12\) removes the cutoff ambiguity at \(n=K\).  
   **[standard-with-citation]** This is Montgomery–Vaughan’s quantitative truncated Perron formula, Corollary 5.3; their Chapter 8 explicitly applies the same formula to \(1/\zeta\): [Montgomery–Vaughan, *Multiplicative Number Theory I*, Chapter 8](https://personal.science.psu.edu/rcv4/personal/Publications/MNTI/12.0_pp_244_281_Further_discussion_of_the_Prime_Number_Theorem.pdf).

3. Since \(\sigma+b=1+1/\log X\), split the Perron error into \(n<X/2\), \(X/2\le n\le2X\), and \(n>2X\). In the middle range,
   \[
   |\log(X/n)|\asymp |X-n|/X,
   \]
   and \(X\) is a half-integer, so summing over distances \(j+\frac12\) gives
   \[
   E_P\ll \frac{X^{1-\sigma}\log(2X)}T
        = \frac{X^{\alpha\Delta}\log(2X)}T.
   \]
   The two outer ranges give the same bound because
   \[
   \sum_{n>X}n^{-1-1/\log X}\ll\log X.
   \]
   **[proved-inline]**

4. Shift the \(w\)-contour from \(\Re w=b\) to \(\Re w=-\eta\). For every point of this rectangle,
   \[
   |\Im(z+w)|\le |t|+T\le2T
   \]
   and
   \[
   \Re(z+w)\ge1-\alpha\Delta-\eta=1-\Delta.
   \]
   Hence the entire rectangle lies in the single doubled-height zero-free region.  
   **[proved-inline]**

5. The only pole crossed is \(w=0\), from the Perron kernel \(1/w\). Its residue is
   \[
   \operatorname*{Res}_{w=0}
      \frac{X^w}{w\zeta(z+w)}
      =\frac1{\zeta(z)}.
   \]
   The point \(z+w=1\) is harmless: \(1/\zeta\) has a zero there, not a pole.  
   **[proved-inline]**

6. On the new vertical side,
   \[
   \int_{-T}^{T}
      \left|
      \frac{X^{-\eta+iv}}
           {(-\eta+iv)\zeta(z-\eta+iv)}
      \right|dv
   \ll B_TX^{-\eta}\log\frac{2T}{\eta}.
   \]
   **[proved-inline]**

7. Each horizontal side contributes
   \[
   \ll \frac{B_T}{T}
       \int_{-\eta}^{b}X^u\,du
   \ll B_T\frac{X^b}{T\log X}
   \ll B_T\frac{X^{\alpha\Delta}}{T\log X}.
   \]
   **[proved-inline]**

Combining steps 2–7 proves the lemma.

### Why the proposal’s original lemma is false

The proposed contour used the local width \(\delta(t)\), while the inner Perron shift has heights \(t+v\), \(|v|\le T\). Such a rectangle would require
\[
\alpha\delta(t)+\eta
 \le \min_{|v|\le T}\delta(t+v)
 =\delta(|t|+T).
\]
For bounded \(t\) and \(T\to\infty\), the right-hand side tends to zero while \(\delta(t)\) does not. Therefore the proposed uniform rectangle does not exist.  
**[proved-inline]**

Moreover, shifting without recording \(w=0\) necessarily misses \(1/\zeta(z)\). On the corrected global contour, at \(t=0\),
\[
\frac1{\zeta(1-\alpha\Delta)}
 =-\alpha\Delta+O(\Delta^2),
\]
whereas the claimed decaying remainder is exponentially smaller. Thus
\[
F_K(1-\alpha\Delta)\ll K^{-(1-\alpha)\Delta}\operatorname{polylog}
\]
is genuinely false in the parameter regime used by Theorem A.  
**[proved-inline]**

## Consequence for the \(\psi\)-sum

Let
\[
A_\psi(x,K)
 =\sum_{d\le K}\mu(d)
   \left(\psi(\lfloor x/d\rfloor)-\frac xd\right).
\]

Perron applied to
\[
F_K(s)\left(-\frac{\zeta'}{\zeta}(s)\right)
\]
crosses the pole at \(s=1\), with residue
\[
xF_K(1)=x\sum_{d\le K}\frac{\mu(d)}d.
\]
This cancels the explicitly subtracted main term.  
**[proved-inline]**

After completion,
\[
F_K(s)\left(-\frac{\zeta'}{\zeta}(s)\right)
 =
-\frac{\zeta'(s)}{\zeta(s)^2}
 +E_K(s)\left(-\frac{\zeta'}{\zeta}(s)\right),
\]
and
\[
-\frac{\zeta'}{\zeta^2}
 =\left(\frac1\zeta\right)'.
\]
The sign in the mapping’s informal expression should therefore be read as \(-\zeta'/\zeta^2\).  
**[proved-inline]**

Choose \(T\) as in the standard optimized KV proof, so that
\[
\min\{\log T,\Delta\log x\}
 \ge (1-o(1))c_0\Phi(x),
\quad
\Phi(x)=(\log x)^{3/5}(\log\log x)^{-1/5}.
\]
Replacing \(T\) by \(2T\) changes \(\Delta\) by \(1+o(1)\).  
**[standard-with-citation]** This is the usual VK contour optimization; see Ford and Titchmarsh–Heath-Brown above.

The terms are then:

\[
x^\sigma\operatorname{polylog}T
 \ll x e^{-\alpha\Delta\log x}\operatorname{polylog}x,
\]

\[
x^\sigma K^{-\eta}\operatorname{polylog}
 \le x e^{-\alpha\Delta\log x-\eta\log K}
       \operatorname{polylog},
\]

and, because \(K\le x^{1/2+o(1)}\),
\[
x^\sigma\frac{K^{\alpha\Delta}}T
 \le
 x\exp\!\left(
   -\alpha\Delta(\log x-\log K)-\log T
 \right)
 \le
 x\exp\!\left(
   -\tfrac12\alpha\Delta\log x-\log T+o(1)
 \right).
\]
The last term is stronger than the two balanced standard-PNT errors. The outer Perron and horizontal errors are
\[
\ll x(\log x)^A/T.
\]
**[proved-inline]**

Hence, for every \(\varepsilon>0\),
\[
A_\psi(x,K)
 \ll_\varepsilon
 x\exp\!\left(-(1-\varepsilon)c_0\Phi(x)\right).
\]

## Corrected Theorem A for \(R=\pi-\operatorname{Li}\)

The proposal’s sentence that the \(\pi\)-to-\(\psi\) integral term costs only \(O(x^{3/4}\log x)\) is not correct as written. The prime-power difference costs that much; the partial-summation integral does not disappear termwise.

The repair is to work with Riemann’s prime-power counter
\[
J(t)=\sum_{n\le t}\frac{\Lambda(n)}{\log n}
    =\sum_{p^m\le t}\frac1m,
\]
whose Dirichlet series is
\[
\log\zeta(s)=\sum_{n\ge2}
 \frac{\Lambda(n)}{\log n}\,n^{-s}.
\]
**[standard-with-citation]** See the standard inverse-Mellin construction in Titchmarsh–Heath-Brown and the displayed Dirichlet series discussion in [Riemann prime-power counting](https://en.wikipedia.org/wiki/Prime-counting_function#Other_prime-counting_functions).

Apply the same outer contour to
\[
F_K(s)\log\zeta(s).
\]
A keyhole around \(s=1\) contributes exactly
\[
\sum_{d\le K}\mu(d)\operatorname{Li}(x/d);
\]
this is the usual inverse-Mellin origin of the \(\operatorname{Li}\) main term, termwise multiplied by \(d^{-s}\). It cancels the subtracted main term.  
**[standard-with-citation]** This is Riemann’s standard \(J-\operatorname{Li}\) contour, with a finite Dirichlet polynomial multiplier.

On the remaining zero-free contour,
\[
F_K(s)\log\zeta(s)
 =
\frac{\log\zeta(s)}{\zeta(s)}
 +E_K(s)\log\zeta(s).
\]
Both \(\log\zeta\) and \(1/\zeta\) have only polylogarithmic size in the working region. The preceding error accounting is unchanged.  
**[proved-inline from the lemma and standard zero-free bounds]**

Finally,
\[
J(t)-\pi(t)
 =\sum_{m\ge2}\frac1m\pi(t^{1/m})
 \ll \sqrt t,
\]
so
\[
\sum_{d\le K}|J(x/d)-\pi(x/d)|
 \ll\sqrt x\sum_{d\le K}d^{-1/2}
 \ll \sqrt{xK}
 \ll x^{3/4}.
\]
Also,
\[
\operatorname{Li}(x/d)-\operatorname{Li}(\lfloor x/d\rfloor)
 \ll\frac1{\log(x/d)},
\]
whose sum is \(O(K/\log x)\). Both are negligible compared with the KV envelope.  
**[proved-inline]**

Therefore the corrected theorem is:

> For \(y\asymp\sqrt x\), \(K=\lfloor x/(y+1)\rfloor\), and every \(\varepsilon>0\),
> \[
> \boxed{
> \left|
> \sum_{d\le K}\mu(d)
> \bigl(\pi(\lfloor x/d\rfloor)
>       -\operatorname{Li}(\lfloor x/d\rfloor)\bigr)
> \right|
> \ll_\varepsilon
> x\exp\!\left(
> -(1-\varepsilon)c_0
> (\log x)^{3/5}(\log\log x)^{-1/5}
> \right).
> }
> \]

Here \(c_0\) must mean an admissible constant from one fixed VK contour normalization. If “\(c_0\)” means the supremum of all possible PNT constants, equality at that endpoint is not justified; only every smaller constant is.

The weakest step is the uniform keyhole-Perron implementation for \(F_K(s)\log\zeta(s)\), including its sharp-cutoff outer error. It is standard contour machinery, but it is the least completely off-the-shelf part of the proof. The repaired \(F_K\)-lemma itself is no longer the weak point.

For comparison, triangle inequality alone gives only
\[
x\exp\!\left(
 -(1-\varepsilon)2^{-3/5}c_0\Phi(x)
\right),
\]
since every \(x/d\ge x^{1/2+o(1)}\) and
\[
\Phi(\sqrt x)
 =(2^{-3/5}+o(1))\Phi(x).
\]

## K7. Literature audit

The strength class with an unspecified \(c>0\) is already known, regardless of whether this exact truncated expression has been named as a theorem:

\[
\sum_{d\le\sqrt x}
 \left|\mu(d)
   \bigl(\psi(x/d)-x/d\bigr)\right|
 \ll
 x\log x\,
 \exp\!\left(-c\,\Phi(\sqrt x)\right)
 \ll
 x\exp(-c'\Phi(x))
\]
for every \(c'<2^{-3/5}c\). This is an immediate corollary of the classical VK PNT estimate. Thus an unqualified “there exists \(c>0\)” result is not novel.

Specific checks:

- Montgomery–Vaughan explicitly discuss applying truncated Perron to \(1/\zeta\), derive Möbius/PNT equivalences, and record the full Möbius–\(\psi\) convolution identities in [Chapter 8](https://personal.science.psu.edu/rcv4/personal/Publications/MNTI/12.0_pp_244_281_Further_discussion_of_the_Prime_Number_Theorem.pdf).

- Tao’s 2015 notes display the relevant \(\sqrt x\)-hyperbola decomposition of \(\Lambda\) into a short \(\mu\)-sum and a complementary Mertens term. It is adjacent to this mechanism, though it does not state the full-constant Abel estimate: [Tao, *Probabilistic models and heuristics for the primes*](https://terrytao.wordpress.com/2015/01/04/254a-supplement-4-probabilistic-models-and-heuristics-for-the-primes-optional/).

- Ivić’s monograph is a standard source for the VK zero-free/PNT machinery, but I found no separately named theorem for this exact hyperbola-truncated sum: [Ivić, *The Riemann Zeta-Function*](https://store.doverpublications.com/products/9780486428130).

- Ramachandra’s cited volume concerns mean-value and omega theorems for \(\zeta\); I found no matching truncated \(\mu(d)\psi(x/d)\) estimate there: [Ramachandra, *Lectures on Mean-Value and Omega-Theorems*](https://mathweb.tifr.res.in/Documents/Publications/Lectures/tifr85.pdf).

- The “twisted Möbius sums” located in the search concern character or other external twists, not this moving hyperbola cutoff.

The completion
\[
F_K(z)=\frac1{\zeta(z)}+\text{shifted-contour error}
\]
is standard in method: it is precisely truncated Perron for \(1/\zeta(z+w)\), followed by crossing \(w=0\). What is not safe to quote without proof is the proposal’s particular local-width uniformity and its omission of \(K^{\alpha\Delta}/T\). The doubled-height formulation above supplies those missing details.

Codex session ID: 019fe794-7674-7532-ab53-da8126776cd0
Resume in Codex: codex resume 019fe794-7674-7532-ab53-da8126776cd0
