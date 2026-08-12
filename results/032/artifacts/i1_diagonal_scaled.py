"""Record 032a: scaled I1 mu^2-diagonal probe (k=1 Gram objects at canonical pins).

Objects (same conventions as pilot_i1_diagonal.py, vectorized over t):
  ensemble y in (Y, 2Y], canonical pin x_y = (y+1)^2 - 1, window t in [0, y] (W = y+1)
  S(y, x)  = sum_{d <= floor(x/(y+1))} mu(d) * R(floor(x/d))
  R(t)     = pi(t) - Li(t),  Li via base-2 midpoint quadrature (differences-only):
             Li(n) = sum_{k=2}^{n-1} 1/log(k+0.5), Li(2)=0
  E2(Y)    = sum_{y,t} S(y, x_y - t)^2
  D(Y)     = sum_{y,t} sum_{d<=K} mu(d)^2 R(floor(n/d))^2   (sign-blind diagonal)
  mean/var window split: sum_t S^2 = (y+1)*Sbar^2 + sum_t (S - Sbar)^2

Note: for n = x_y - t with 0 <= t <= y, floor(n/(y+1)) = y for every t
(n = y(y+1) + (y - t)), so the d-truncation K = y is constant across the window.

Frozen predictions under test (audit 029, i1-viability fatal #1):
  P1: D(Y) exponent in [3.7, 4]      (Y^{2+4theta}/log-type; RH-strength diagonal)
  P2: E2/D bounded away from 1        (pilot: ~0.17)
  P3: DC/mean block carries ~99% of window energy
Kill condition (CONTRADICTS-AUDIT): E2/D -> 1 with the diagonal subdominant.

Falsification-grade numerics only.
"""
import math, sys, time
import numpy as np

CAP_SECONDS = 2100.0          # ~35 min compute cap
YS = [32, 48, 64, 96, 128, 192, 256, 384, 512, 768, 1024, 1536, 2048]
CSV = "/tmp/claude-1000/-mnt-d-Projects-prime-wheel-mobius/0d31eddd-16a5-4696-aef4-2949c1ddd542/scratchpad/i1_diagonal_scaled.csv"

T_START = time.time()
XMAX = (2 * YS[-1] + 1) ** 2  # max n needed if all levels run

# ---- sieves: primality, Moebius, R = pi - Li ------------------------------
t0 = time.time()
isp = np.ones(XMAX + 1, dtype=bool)
isp[:2] = False
mu = np.ones(XMAX + 1, dtype=np.int8)
for p in range(2, int(math.isqrt(XMAX)) + 1):
    if isp[p]:
        isp[p * p :: p] = False
        mu[p::p] = -mu[p::p]
        mu[p * p :: p * p] = 0
# fix sign for numbers with one prime factor > sqrt(XMAX)
prod = np.ones(XMAX + 1, dtype=np.int64)
for p in range(2, int(math.isqrt(XMAX)) + 1):
    if isp[p]:
        pk = p
        while pk <= XMAX:
            prod[pk::pk] *= p
            pk *= p
nn = np.arange(XMAX + 1, dtype=np.int64)
big = prod < nn
mu[big] = -mu[big]
mu[0] = 0
del prod, nn, big

# self-check mu against direct factorization on a sample
def mu_direct(n):
    if n == 1:
        return 1
    m, cnt = n, 0
    d = 2
    while d * d <= m:
        if m % d == 0:
            m //= d
            if m % d == 0:
                return 0
            cnt += 1
        d += 1
    if m > 1:
        cnt += 1
    return (-1) ** cnt
rng = np.random.default_rng(29032)
for n in np.concatenate(([1, 2, 4, 6, 30, 210, XMAX], rng.integers(1, XMAX, 200))):
    assert mu[int(n)] == mu_direct(int(n)), f"mu mismatch at {n}"

PI = np.cumsum(isp, dtype=np.int64)
tt = np.arange(2, XMAX + 1, dtype=np.float64)
LI = np.zeros(XMAX + 1, dtype=np.float64)
LI[2:] = np.concatenate(([0.0], np.cumsum(1.0 / np.log(tt[:-1] + 0.5))))
R = PI.astype(np.float64) - LI
del PI, LI, tt, isp
print("sieves to %d: %.1fs" % (XMAX, time.time() - t0), flush=True)

# ---- main loop -------------------------------------------------------------
hdr = ("Y", "E2", "D", "E2_over_D", "meanblock", "varblock", "dc_share", "secs")
print("%6s %16s %16s %10s %16s %14s %9s %8s" % hdr, flush=True)
rows = []
last_t = last_Y = None
for Y in YS:
    # runtime guard: project next level cost ~ (Y/lastY)^3 * last level time
    if last_t is not None:
        proj = last_t * (Y / last_Y) ** 3
        if time.time() - T_START + proj > CAP_SECONDS:
            print("cap: skipping Y=%d (projected %.0fs, elapsed %.0fs)"
                  % (Y, proj, time.time() - T_START), flush=True)
            break
    t0 = time.time()
    E2 = Dg = MB = VB = 0.0
    for y in range(Y + 1, 2 * Y + 1):
        xy = (y + 1) ** 2 - 1
        assert xy // (y + 1) == (xy - y) // (y + 1) == y  # constant truncation
        ds = np.arange(1, y + 1, dtype=np.int64)
        w = mu[ds].astype(np.float64)
        sel = w != 0.0
        d2 = ds[sel].astype(np.int32)          # squarefree d only (mu^2 = 1)
        w2 = w[sel]
        n = (xy - np.arange(0, y + 1, dtype=np.int64)).astype(np.int32)
        idx = n[:, None] // d2[None, :]        # (y+1) x #sf matrix
        vals = R[idx]
        S = vals @ w2
        E2 += float(S @ S)
        Dg += float(np.einsum("ij,ij->", vals, vals))
        Sb = S.mean()
        MB += (y + 1) * Sb * Sb
        VB += float((S - Sb) @ (S - Sb))
        del idx, vals
    secs = time.time() - t0
    dc = MB / (MB + VB)
    rows.append((Y, E2, Dg, E2 / Dg, MB, VB, dc, secs))
    print("%6d %16.1f %16.1f %10.4f %16.1f %14.1f %9.5f %8.1f"
          % rows[-1], flush=True)
    last_t, last_Y = secs, Y

# ---- fits & CSV ------------------------------------------------------------
arr = np.array([r[:7] for r in rows])
lY = np.log(arr[:, 0])
fits = {}
for j, name in ((1, "E2"), (2, "D"), (4, "meanblock"), (5, "varblock")):
    full = np.polyfit(lY, np.log(arr[:, j]), 1)[0]
    tail = np.polyfit(lY[-5:], np.log(arr[-5:, j]), 1)[0]
    fits[name] = (full, tail)
    print("exponent %-9s ~ Y^%.3f  (last-5: Y^%.3f)" % (name, full, tail),
          flush=True)
# successive-level local slopes for D and E2
for j, name in ((1, "E2"), (2, "D")):
    loc = np.diff(np.log(arr[:, j])) / np.diff(lY)
    print("local slopes %-3s: %s" % (name, " ".join("%.3f" % v for v in loc)),
          flush=True)

with open(CSV, "w") as f:
    f.write("Y,E2,D,E2_over_D,meanblock,varblock,dc_share,secs\n")
    for r in rows:
        f.write("%d,%.6e,%.6e,%.6f,%.6e,%.6e,%.6f,%.1f\n" % r)
    f.write("# exponent fits (full, last-5): " +
            "; ".join("%s=%.3f,%.3f" % (k, v[0], v[1])
                      for k, v in fits.items()) + "\n")
print("total %.1fs; CSV -> %s" % (time.time() - T_START, CSV), flush=True)
