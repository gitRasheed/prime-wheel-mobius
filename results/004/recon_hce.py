#!/usr/bin/env python3
"""Phase 1 recon (record 004): exact H_{k,n}, centered C and E, over all
complete-square samples in synchronized blocks k=2..8 (U_8 = W_9).

Implements the extracted computational spec verbatim:
  L_k = primorial(k), U_k = primorial(k+1), X_n = (n+1)^2 - 1
  P_k = prod_{p<=isqrt(U_k)} p^2,  Q_k = (U_k//P_k + 1)*P_k
  rho = (X_n - L_k)/Q_k          (exact Fraction for H; float in Center)
  H = [M(X)-M(L)] - rho*[M(U)-M(L)]                     (exact)
  y_k = isqrt(U_k) + 1
  Li(x) = int_2^x du/ln u  (Gauss-Legendre 2pt per unit interval)
  Mplus_y(x) = sum_{n<=x} prod_{p<=y} chi_p(n)
  B(y,x) = sum_{y<q<=x} (Li(q)-Li(q-1)) M(x//q)   [all integers q]
  E(y,x) = sum_{y<q<=x} (1_prime(q)-(Li(q)-Li(q-1))) M(x//q)
  C(y,x) = Mplus_y(x) - 2 B(y,x)
  Center_{k,n}[f] = (f(X)-f(L)) - rho*(f(U)-f(L))
  check: H == Center[C] - 2*Center[E]  (float tolerance; Li is float)
Reciprocal-d profile of E stored for a subsample of n per k.

Arithmetic model: exact int64/Fraction for mu, M, Mplus, H; float64 for
Li-derived quantities (B, E, C, centering) with residual H-identity
error reported per k. Deterministic.
"""
import numpy as np, math, csv, json, time, os, sys
sys.set_int_max_str_digits(2000000)
from fractions import Fraction
from multiprocessing import Pool

N = 223_092_870  # W_9 = U_8
PRIMORIALS = [1, 2, 6, 30, 210, 2310, 30030, 510510, 9699690, 223092870]
OUT = os.path.dirname(os.path.abspath(__file__))

t0 = time.time()
def log(*a): print(f"[{time.time()-t0:7.1f}s]", *a, flush=True)

log("loading mu, building M / primes / pi / Li arrays")
mu = np.load(os.path.join(OUT, "mu.npy"))
M = np.cumsum(mu.astype(np.int64))            # M[x] = Mertens(x)
assert M[6] == -1 and M[8] == -2 and M[30] == -3, "Mertens micro-check failed"

is_prime = np.ones(N + 1, dtype=bool); is_prime[:2] = False
for p in range(2, math.isqrt(N) + 1):
    if is_prime[p]:
        is_prime[p * p:: p] = False
pi = np.cumsum(is_prime.astype(np.int32)).astype(np.int64)

# Li[x] = int_2^x du/ln u ; Li[0]=Li[1]=Li[2]=0 (only diffs at args>=3 used)
c = 0.5 / math.sqrt(3.0)
m = np.arange(2, N, dtype=np.float64)
inc = 0.5 * (1.0 / np.log(m + 0.5 - c) + 1.0 / np.log(m + 0.5 + c))
Li = np.zeros(N + 1, dtype=np.float64)
Li[3:] = np.cumsum(inc); del m, inc
log("base arrays ready")

def primes_upto(y):
    s = np.ones(y + 1, dtype=bool); s[:2] = False
    for p in range(2, math.isqrt(y) + 1):
        if s[p]: s[p * p:: p] = False
    return np.nonzero(s)[0]

def quotient_BE(x, y):
    """(B(y,x), E(y,x)) via the kernel-proved reciprocal-d reindex."""
    dmax = x // (y + 1)
    if dmax < 1: return 0.0, 0.0, None
    d = np.arange(1, dmax + 1, dtype=np.int64)
    b = x // d
    a = np.maximum(y, x // (d + 1))
    ok = a < b
    d, b, a = d[ok], b[ok], a[ok]
    Md = M[d].astype(np.float64)
    limass = Li[b] - Li[a]
    pcount = (pi[b] - pi[a]).astype(np.float64)
    B = float(np.dot(limass, Md))
    E = float(np.dot(pcount - limass, Md))
    return B, E, (d, Md, pcount - limass)

# globals set per-k for worker processes (fork shares them copy-on-write)
G = {}
def sample_row(n):
    X = (n + 1) ** 2 - 1
    L, U, Q, y, rho_f = G["L"], G["U"], G["Q"], G["y"], G["rho_den"]
    rho = Fraction(X - L, Q)
    H_exact = Fraction(int(M[X] - M[L])) - rho * int(M[U] - M[L])
    BX, EX, _ = quotient_BE(X, y)
    CX = float(G["Mplus"][X]) - 2.0 * BX
    rf = float(rho)
    Cc = (CX - G["CL"]) - rf * (G["CU"] - G["CL"])
    Ec = (EX - G["EL"]) - rf * (G["EU"] - G["EL"])
    Hf = float(H_exact)
    return (n, X, H_exact.numerator, H_exact.denominator, Hf, Cc, Ec,
            abs(Cc - 2.0 * Ec - Hf))

results_summary = []
for k in range(2, 9):
    L, U = PRIMORIALS[k], PRIMORIALS[k + 1]
    ysq = math.isqrt(U)
    wheel_ps = [int(p) for p in primes_upto(ysq)]
    P = 1
    for p in wheel_ps: P *= p * p
    Q = (U // P + 1) * P
    y = ysq + 1
    log(f"k={k}: L={L} U={U} y={y} |wheel primes|={len(wheel_ps)} digits(Q)={len(str(Q))}")

    # all-plus comb cumulative Mplus_y on [0, U]
    site = np.ones(U + 1, dtype=np.int8); site[0] = 0
    for p in primes_upto(y):
        site[p:: p] *= -1
        site[p * p:: p * p] = 0
    Mplus = np.cumsum(site.astype(np.int64)); del site

    if k == 2:  # micro-example asserts from the extracted spec
        assert Mplus[6] == -1 and Mplus[8] == 0 and Mplus[30] == 3
        _, E68, _ = quotient_BE(8, 6)
        assert abs(E68 - (1.0 - (Li[8] - Li[6]))) < 1e-12

    BL, EL, _ = quotient_BE(L, y)
    BU, EU, _ = quotient_BE(U, y)
    G.update(L=L, U=U, Q=Q, y=y, rho_den=None, Mplus=Mplus,
             CL=float(Mplus[L]) - 2.0 * BL, CU=float(Mplus[U]) - 2.0 * BU,
             EL=EL, EU=EU)

    n_lo = math.isqrt(L + 1)          # smallest n with X_n > L
    while (n_lo + 1) ** 2 - 1 <= L: n_lo += 1
    n_hi = math.isqrt(U + 1) - 1
    while (n_hi + 2) ** 2 - 1 <= U: n_hi += 1
    ns = list(range(n_lo, n_hi + 1))
    log(f"  {len(ns)} square samples")

    with Pool(14) as pool:
        rows = pool.map(sample_row, ns, chunksize=64)

    if k == 2:
        r = dict(zip((row[0] for row in rows), rows))
        assert (r[2][2], r[2][3]) == (-224, 225), f"H(2,2) micro-check: {r[2]}"

    with open(os.path.join(OUT, f"samples_k{k}.csv"), "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["n", "X", "H_num", "H_den", "H", "C_centered",
                    "E_centered", "identity_err"])
        w.writerows(rows)

    Hs = np.array([r[4] for r in rows]); Cs = np.array([r[5] for r in rows])
    Es = np.array([r[6] for r in rows]); errs = np.array([r[7] for r in rows])
    Xs = np.array([r[1] for r in rows], dtype=np.float64)
    corr = float(np.corrcoef(Cs, Es)[0, 1]) if len(rows) > 2 else float("nan")
    sign_agree = float(np.mean(np.sign(Cs) == np.sign(Es)))
    canc = float(np.mean(np.abs(Cs - 2 * Es) / np.maximum(np.abs(Cs) + 2 * np.abs(Es), 1e-30)))
    ratio = np.abs(Hs) / np.sqrt(Xs)
    s = dict(k=k, L=L, U=U, y=y, n_samples=len(rows),
             max_abs_H=float(np.max(np.abs(Hs))),
             sup_H_over_sqrtX=float(np.max(ratio)),
             mean_H_over_sqrtX=float(np.mean(ratio)),
             corr_C_E=corr, sign_agreement=sign_agree,
             mean_cancellation_ratio=canc,
             max_identity_err=float(np.max(errs)))
    results_summary.append(s)
    log(f"  k={k}: max|H|={s['max_abs_H']:.3f} sup|H|/sqrtX={s['sup_H_over_sqrtX']:.4f} "
        f"corr(C,E)={corr:.4f} signAgree={sign_agree:.3f} "
        f"cancel={canc:.4f} maxIdErr={s['max_identity_err']:.2e}")

    # reciprocal-d profile for up to 12 evenly spaced samples
    with open(os.path.join(OUT, f"dprofile_k{k}.csv"), "w", newline="") as fh:
        w = csv.writer(fh); w.writerow(["n", "X", "d", "Md_weight", "discrepancy", "contribution"])
        for n in ns[:: max(1, len(ns) // 12)]:
            X = (n + 1) ** 2 - 1
            _, _, prof = quotient_BE(X, y)
            if prof is None: continue
            d, Md, disc = prof
            contrib = Md * disc
            keep = np.argsort(-np.abs(contrib))[:40]
            for i in sorted(keep):
                w.writerow([n, X, int(d[i]), int(Md[i]), f"{disc[i]:.6e}", f"{contrib[i]:.6e}"])
    del Mplus

with open(os.path.join(OUT, "summary.json"), "w") as fh:
    json.dump(results_summary, fh, indent=1)
log("done")
