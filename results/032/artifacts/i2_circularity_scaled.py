"""Record 032b: scaled I2 DC/AC circularity probe (scales pilot_i2_circularity.py).

Audit 029 (i2-viability, fatal #1): |V_0 - A_q| << q^{1+eps} holds unconditionally,
so bounding the DC mean A_q at precision q^{1+eps} IS bounding V_0 = S(y, X):
the DC/AC 'reduction' is circular at every rung-1 precision.

Objects (identical to pilot, canonical pins):
  q log-spaced, X = q^2 - 1, y = q - 1
  V_t = S(q-1, X-t) = sum_{d <= K_t} mu(d) R(floor((X-t)/d)),
      K_t = floor((X-t)/q) = q-1 constant for 0 <= t <= q-1 (asserted)
  R(t) = pi(t) - Li_2(t), Li_2 midpoint quadrature (differences only)
  A_q = q^{-1} sum_{t<q} V_t ;  c_q(X-t) = V_t - V_{t+1}, 0 <= t <= q-2

Frozen predictions (pilot at 1e6): |V_0 - A_q| ~ q^s with s <= 1 (pilot 0.60);
sum_t |c_q(X-t)| ~ q^{1+o(1)} (pilot 0.97). Kill: gap exponent clearly above 1.

Memory notes vs pilot: mu sieved only to qmax (mu is indexed at d <= q-1 only);
R built as float64 cumsum of prime indicator with the Li midpoint cumsum
subtracted in chunks (no full-length int64/temporary arrays). Peak ~1.0 GB at 1e8.
"""
import sys, math, time, csv
import numpy as np

XMAX = int(float(sys.argv[1])) if len(sys.argv) > 1 else 10**8
NPINS = int(sys.argv[2]) if len(sys.argv) > 2 else 40
OUT = sys.argv[3] if len(sys.argv) > 3 else None

t0 = time.time()
QMAX = math.isqrt(XMAX + 1)          # largest q with X = q^2 - 1 <= XMAX

# ---- mu up to QMAX (exact: sqrt-sieve + large-prime-factor sign flip) ----
M = QMAX
mu = np.ones(M + 1, dtype=np.int8)
isp_s = np.ones(M + 1, dtype=bool)
isp_s[:2] = False
prod = np.ones(M + 1, dtype=np.int64)
for p in range(2, math.isqrt(M) + 1):
    if isp_s[p]:
        isp_s[p * p::p] = False
        mu[p::p] = -mu[p::p]
        mu[p * p::p * p] = 0
        pk = p
        while pk <= M:
            prod[pk::pk] *= p
            pk *= p
n_s = np.arange(M + 1, dtype=np.int64)
big = prod < n_s                      # exactly one prime factor > sqrt(M), to power 1
mu[big] = -mu[big]
mu[0] = 0
Mch = np.cumsum(mu, dtype=np.int64)
assert Mch[10] == -1 and Mch[100] == 1 and Mch[1000] == 2, (Mch[10], Mch[100], Mch[1000])
del isp_s, prod, n_s, Mch

# ---- R(t) = pi(t) - Li_2(t) on [0, XMAX], float64, low-peak-memory ----
isp = np.ones(XMAX + 1, dtype=bool)
isp[:2] = False
for p in range(2, math.isqrt(XMAX) + 1):
    if isp[p]:
        isp[p * p::p] = False
print("prime sieve to %d: %.1fs" % (XMAX, time.time() - t0), flush=True)

R = np.cumsum(isp, dtype=np.float64)  # pi(t)
del isp
# Li_2 midpoint table, pilot convention: LI[t] = sum_{u=2}^{t-1} 1/log(u+0.5),
# LI[t] = 0 for t <= 2. Subtract in chunks with a running offset.
BLK = 1 << 22
running = 0.0
for lo in range(3, XMAX + 1, BLK):
    hi = min(lo + BLK - 1, XMAX)
    u = np.arange(lo - 1, hi, dtype=np.float64)          # u = t-1 for t in [lo, hi]
    block = running + np.cumsum(1.0 / np.log(u + 0.5))
    R[lo:hi + 1] -= block
    running = block[-1]
print("R table to %d: %.1fs" % (XMAX, time.time() - t0), flush=True)

# ---- pins ----
qs = np.unique(np.round(np.logspace(1.2, math.log10(QMAX), NPINS)).astype(int))
print("%d pins, q in [%d, %d]" % (len(qs), qs[0], qs[-1]), flush=True)
print("%8s %16s %16s %14s %14s %10s %10s" %
      ("q", "V0=S(y,X)", "A_q", "|V0-A_q|", "sum|c_q|", "gap/q", "csum/q"))
rows = []
TBLK = 1024
for q in qs:
    X = q * q - 1
    if X > XMAX:
        break
    ds = np.arange(1, q, dtype=np.int64)
    mud = mu[1:q].astype(np.float64)
    V = np.empty(q, dtype=np.float64)
    for lo in range(0, q, TBLK):
        t = np.arange(lo, min(lo + TBLK, q), dtype=np.int64)
        nvals = X - t
        assert nvals[-1] // q == q - 1 and nvals[0] // q == q - 1  # constant truncation
        idx = nvals[:, None] // ds[None, :]
        V[lo:lo + len(t)] = R[idx] @ mud
    A = V.mean()
    gap = abs(V[0] - A)
    c = V[:-1] - V[1:]                 # c_q(X-t), t = 0..q-2 (exact range per audit)
    csum = float(np.abs(c).sum())
    rows.append((int(q), int(X), float(V[0]), float(A), gap, csum))
    print("%8d %16.3f %16.3f %14.3f %14.3f %10.4f %10.4f"
          % (q, V[0], A, gap, csum, gap / q, csum / q), flush=True)

# ---- fits ----
arr = np.array([(r[0], r[4], r[5]) for r in rows], dtype=np.float64)
q_, gap_, csum_ = arr[:, 0], arr[:, 1], arr[:, 2]
mask = gap_ > 0
lg, lq = np.log(gap_[mask]), np.log(q_[mask])
s_gap = np.polyfit(lq, lg, 1)[0]
s_csum = np.polyfit(np.log(q_), np.log(csum_), 1)[0]
half = q_ >= math.sqrt(q_[0] * q_[-1])          # geometric top half
s_gap_t = np.polyfit(np.log(q_[mask & half]), np.log(gap_[mask & half]), 1)[0]
s_csum_t = np.polyfit(np.log(q_[half]), np.log(csum_[half]), 1)[0]
print("\nexponent fit |V0 - A_q| ~ q^%.3f  (tail half: q^%.3f)   [prediction <= 1]" % (s_gap, s_gap_t))
print("exponent fit sum_t|c_q| ~ q^%.3f  (tail half: q^%.3f)   [prediction ~ 1+o(1)]" % (s_csum, s_csum_t))
print("total: %.1fs" % (time.time() - t0))

if OUT:
    with open(OUT, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["q", "X", "V0", "A_q", "abs_V0_minus_Aq", "sum_abs_cq",
                    "gap_over_q", "csum_over_q"])
        for q, X, V0, A, gap, csum in rows:
            w.writerow([q, X, "%.6f" % V0, "%.6f" % A, "%.6f" % gap,
                        "%.6f" % csum, "%.6f" % (gap / q), "%.6f" % (csum / q)])
        w.writerow([])
        w.writerow(["# fit_exponent_gap_all", "%.4f" % s_gap])
        w.writerow(["# fit_exponent_gap_tail_half", "%.4f" % s_gap_t])
        w.writerow(["# fit_exponent_csum_all", "%.4f" % s_csum])
        w.writerow(["# fit_exponent_csum_tail_half", "%.4f" % s_csum_t])
        w.writerow(["# XMAX", XMAX])
    print("wrote", OUT)
