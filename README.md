# Prime-Wheel Möbius

Public companion repository for **Seeded Prime-Comb Dynamics and the Finite Harmonic Reduction of Primorial-Block Möbius Sums**.

## Visualization

An exact deterministic reconstruction of the Möbius field on the fourth primorial block

$$W_4 = 2\cdot 3\cdot 5\cdot 7 = 210 .$$

The left panel evolves prime by prime; the right panel is the fixed target $\mu(n)$.

<p align="center">
  <img src="numerics/prime_comb.gif" alt="Prime-by-prime Möbius reconstruction" width="800">
</p>

### Construction

Seed every site uniformly, then apply one operator per prime $p \le W_4$, each prime exactly once, in increasing order:

$$
J_0(n) = s,
\qquad
J \longleftarrow J \cdot u_p,
\qquad
u_p(n) =
\begin{cases}
0 & p^2 \mid n, \\
-1 & p \, \| \, n, \\
1 & p \nmid n.
\end{cases}
$$

White sites are not initialized. They are created by the first branch, and since $0$ is absorbing under a multiplicative operator no later prime can revive one. After the last prime with $p^2 \le W_4$ the support is frozen and equals the squarefree set; for $W_4 = 210$ that prime is $13$. The six primes $p \le \sqrt{210}$ both whiten and orient; the other forty only orient.

### Terminal state

Let $s_y(n)$ denote the $y$-smooth part of $n$. Admitting every prime up to $y$ gives

$$\sigma_y(n) = s \, \mu\big(s_y(n)\big).$$

Every $n \le W$ is $W$-smooth, so at $y = W$ the smooth part is $n$ itself and

$$\sigma(n) = s\,\mu(n), \qquad B = s\,M(W).$$

The default seed $s=-1$ has limit $-\mu$; `--seed +1` makes the primes alone land on $\mu$.

### Endpoint alignment is a tautology

Every $n \le W$ has all of its prime factors $\le W$, so its $W$-rough part is $1$ and $\sigma(n) = s\mu(n)$ pointwise. Nothing about the distribution of the primes is used — the cutoff simply exceeds the block.

The sharp form is a statement about prefixes, not blocks. With $q_1(y)$ the least prime above $y$, the reconstruction agrees with $\mu$ at

$$\text{every } x < q_1(y)^2,$$

and fails at $x = q_1(y)^2$, the least integer carrying two $y$-rough prime factors. Endpoint agreement is the case $y = W$. It therefore measures nothing: below $q_1(y)^2$ agreement is automatic.

### The path

The endpoints are pinned; the route between them is not, and the route is the object of interest. Each prime moves the signed sum by

$$B_j = B_{j-1} - 2\,C_j,$$

where $C_j$ is the signed mass on that prime's flip channel before it acts. On $W_4 = 210$ with $s = -1$, so limit $B = +1$:

| after prime | $B$ | distance to limit | sites agreeing |
|---|---:|---:|---:|
| seed | $-210$ | $211$ | $64$ |
| $2$ | $-52$ | $53$ | $106$ |
| $13$ | $+1$ | $0$ | $116$ |
| $67$ | $-37$ | $38$ | $175$ |
| $199$ | $+1$ | $0$ | $210$ |

The path is not monotone: it is already exact at $p = 13$, leaves to distance $38$ at $p = 67$, and returns at $p = 199$. And signed-sum agreement is not pointwise agreement: at $p = 13$ the sum is exact while $94$ sites are still wrong. What the animation shows is terminal exactness, not convergence.

Final inventory, with the $81$ white sites contributing nothing:

$$Q(210) = 129, \qquad N_+(210) = 64, \qquad N_-(210) = 65, \qquad M(210) = -1 .$$

## What has to be bounded

The lower-left curve is not a diagnostic. After the primes up to $y$ have acted, the signed sum is exactly

$$
B(y) = \sum_{n \le W} \sigma_y(n) =: A_y(W),
$$

so the animation plots $y \mapsto A_y(W)$, and its endpoint is $A_W(W) = s\,M(W)$. The Mertens function is the last value of the curve.

The two classical targets are statements about that endpoint as $W$ varies:

$$
\mathsf{PNT} \iff M(x) = o(x),
\qquad
\mathsf{RH} \iff M(x) = O_\varepsilon\big(x^{1/2+\varepsilon}\big) \ \text{ for every } \varepsilon > 0 .
$$

The reconstruction settles neither, because the endpoint is pinned by a tautology and the route to it is unconstrained.

## Bounding it for arbitrary $x$

Take the cutoff $y$ free of $x$ and let $r_y(n) = n / s_y(n)$ be the rough part. With

$$
A_y(x) = \sum_{n \le x} \sigma_y(n),
\qquad
C_y(x) = \sum_{\substack{n \le x \\ r_y(n) = 1}} \sigma_y(n),
\qquad
D_y(x) = \sum_{\substack{n \le x \\ \Omega(r_y(n)) \ge 2}} \sigma_y(n)\big(1 + \mu(r_y(n))\big),
$$

one has, for every real $x \ge 1$ and every $y \ge 1$,

$$
M(x) = A_y(x) - 2\,C_y(x) - D_y(x).
$$

This is a re-expression of $\mu(n) = \mu(s_y(n))\,\mu(r_y(n))$ and carries no arithmetic content by itself. Its use is that $D_y(x) = 0$ exactly when $x < q_1(y)^2$, so on a completed wheel it reduces to the reconstruction above, and everywhere else it isolates the whole discrepancy.

Three quantities are unconditional and explicit for arbitrary $x$:

$$
\Big| A_y(x) + x \prod_{p \le y}\Big(1 - \frac{1}{p}\Big)^{2} \Big| \le 4^{\pi(y)},
\qquad
C_y(x) = 0 \quad \text{for } x \ge \prod_{p \le y} p,
$$

$$
\sum_{a \bmod Q(y)} \big|\widehat{\sigma_y}(a)\big| = \prod_{p \le y} 2(p-1)(2p-1),
$$

the last over the square-sensitive period $Q(y) = \prod_{p \le y} p^{2}$, which is the wheel the state is actually periodic under — not a primorial.

### The explicit target

Fix any $y \ge 2$. Once $x \ge \prod_{p \le y} p$ the smooth core is complete, $C_y(x) = 0$, and both remaining errors are constants in $x$, so the identity collapses to

$$
M(x) + D_y(x) = -\,x \prod_{p \le y}\Big(1 - \frac{1}{p}\Big)^{2} + O_y(1).
$$

Therefore, for every fixed $y$,

$$
\mathsf{PNT} \iff D_y(x) = -\,x \prod_{p \le y}\Big(1 - \frac{1}{p}\Big)^{2} + o(x),
$$

$$
\mathsf{RH} \iff D_y(x) = -\,x \prod_{p \le y}\Big(1 - \frac{1}{p}\Big)^{2} + O_\varepsilon\big(x^{1/2+\varepsilon}\big).
$$

So $D_y$ is not an error term waiting to be absorbed: it has to reproduce the seeded main term to within the target accuracy. At $x = 10^6$ the ratio of $\max|D_y|$ to that main term is $1.001$ through $1.008$ for $y = 2,\dots,17$.

### Why the regimes do not meet

| requirement | condition | threshold |
|---|---|---|
| reconstruction exact, $D_y = 0$ | $q_1(y)^2 > x$ | $y \asymp \sqrt{x}$ |
| wheel completable | $4^{\pi(y)} \le x$ | $y \asymp \log x \log\log x$ |
| smooth core complete, $C_y = 0$ | $\prod_{p \le y} p \le x$ | $y \asymp \log x$ |

At $x = 10^6$ the largest completable cutoff is $y = 23$ while the exact cutoff is $y = 997$. The gap is exponential in $\pi(y)$, so sharpening the completion error does not close it. At the exact end $D_y$ vanishes but $A_y$ and $C_y$ are individually as deep as $M(x)$.

The construction redistributes the difficulty exactly. Bounding $D_y$ for $\log x < y < \sqrt{x}$ is the open problem.

## Contents

* `paper/` — manuscript source and build notes.
* `formalization/` — standalone Lean 4 project pinned to Lean/mathlib `v4.24.0`.
* `numerics/` — finite primorial-block validation, exact reconstruction programs, and analytic falsification gates.
* `docs/` — theorem status, source provenance, and publication checklist.
* `.github/workflows/` — Lean verification and numerical reproducibility.

## Mathematical boundary

The formalization proves the exact chain

```text
explicit pinned Dirichlet estimate
<-> harmonic nonconcentration
<-> finite wheel residual bound
<-> global Mertens-energy bound.
```

It does **not** claim an unconditional proof of the Riemann Hypothesis. Two inputs remain explicit: the maximal pinned Dirichlet/nonconcentration estimate, and the classical theorem connecting the stated Mertens-energy bound to Mathlib's Riemann Hypothesis proposition.

The visualization is an exact finite reconstruction of $\mu$ and nothing more. It does not show that the intermediate sums contract, that $M(X) = o(X)$, or that an RH-scale estimate holds. Endpoint agreement is forced by the cutoff and is not evidence about the path, and the identities above are exact but tautological — each re-expresses the target rather than reducing it.

See [`docs/THEOREM_STATUS.md`](docs/THEOREM_STATUS.md).

## Lean build

```bash
cd formalization
lake update
lake build RHLean --wfail
bash scripts/audit_assumptions.sh
```

## Paper

Compiled manuscript: [`paper/seeded_prime_comb_harmonic_reduction.pdf`](paper/seeded_prime_comb_harmonic_reduction.pdf) — source [`paper/seeded_prime_comb_harmonic_reduction.tex`](paper/seeded_prime_comb_harmonic_reduction.tex).

## Numerical reproduction

```bash
python3 numerics/primorial_block_validation.py
python3 numerics/prime_comb_viz.py --limit 210 --output-dir numerics
python3 numerics/prime_comb_viz.py --limit 210 --seed +1
```

See [`numerics/README.md`](numerics/README.md) for exact commands, status boundaries, generated artifacts, and hash manifests.
