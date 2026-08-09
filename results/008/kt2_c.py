#!/usr/bin/env python3
"""kill-test wave 2 (record 008), script C: agent3 failure-signal (i).

agent3's kill test asks whether the s = 1 polar parts of C and 2E cancel:
"the residual grows like X or X/log X across the block instead of being o(X)".
The computable content of that signal is the size of H = C - 2E against X and
X/log X, at every pinned square sample in a block.

Exact O(dmax) evaluation (no sieve): every n <= 1e9 has at most one prime
factor > y (two would exceed y^2 = 6.47e9), so the y-rough integers n <= x are
exactly n = p*j with p prime > y and j <= dmax = x//(y+1) < y, uniquely, and
mu(pj) = -mu(j).  Hence, with Msm_y(x) = sum over y-smooth squarefree s <= x of
mu(s),
      Msm_y(x) = M(x) + sum_{j<=dmax} mu(j) (pi(x//j) - pi(y))       [exact int]
      Mplus(x) = Msm_y(x) + sum_d M(d) pi_d                          [wave-1 collapse]
      C(x) = Mplus(x) - 2 B(x),  B = sum_d M(d) Li_d
      E(x) = sum_d M(d) (pi_d - Li_d)
      H(x) = C - 2E = Msm_y(x) - sum_d M(d) pi_d                     [exact int]
Cross-checked against the wave-1 t7_agent6.csv values (Msm, C-2E) at k<=8.
"""
import numpy as np, math, csv, json, os, time, resource
from multiprocessing import Pool

PRIM = [1, 2, 6, 30, 210, 2310, 30030, 510510, 9699690, 223092870, 6469693230]
XCAP = 1_000_000_000
SRC = os.path.expanduser("~/work/killtests")
OUT = os.path.expanduser("~/work/killtests2")
NPROC = 14
t0 = time.time()
def log(*a): print(f"[{time.time()-t0:7.1f}s]", *a, flush=True)

mu = np.load(os.path.join(SRC, "fw_mu.npy"), mmap_mode="r")
M = np.load(os.path.join(SRC, "fw_M_i32.npy"), mmap_mode="r")
pi = np.load(os.path.join(SRC, "fw_pi_i32.npy"), mmap_mode="r")
Li = np.load(os.path.join(SRC, "fw_Li_f64.npy"), mmap_mode="r")
assert M[6] == -1 and M[8] == -2 and M[30] == -3, "Mertens checkpoints"
assert abs((float(pi[8] - pi[6]) - float(Li[8] - Li[6]))
           - (1.0 - float(Li[8] - Li[6]))) < 1e-12, "E(6,8)"
log("hard asserts OK")


def block_ns(k):
    L, U = PRIM[k], PRIM[k + 1]
    n_lo = math.isqrt(L + 1)
    while (n_lo + 1) ** 2 - 1 <= L: n_lo += 1
    n_hi = math.isqrt(U + 1) - 1
    while (n_hi + 2) ** 2 - 1 <= U: n_hi += 1
    n_cap = math.isqrt(XCAP + 1) - 1
    while (n_cap + 2) ** 2 - 1 <= XCAP: n_cap += 1
    return n_lo, min(n_hi, n_cap)


G = {}


def one(n):
    y = G["y"]
    x = (n + 1) ** 2 - 1
    dmax = x // (y + 1)
    j = np.arange(1, dmax + 1, dtype=np.int64)
    piy = int(pi[y])
    # Msm_y(x), exact integer
    Msm = int(M[x]) + int(np.dot(mu[j].astype(np.int64),
                                 pi[x // j].astype(np.int64) - piy))
    b = x // j
    a = np.maximum(y, x // (j + 1))
    ok = a < b
    d, b, a = j[ok], b[ok], a[ok]
    Md = M[d].astype(np.int64)
    pid = pi[b].astype(np.int64) - pi[a].astype(np.int64)
    Lid = Li[b] - Li[a]
    SMpi = int(np.dot(Md, pid))
    B = float(np.dot(Md.astype(np.float64), Lid))
    E = float(np.dot(Md.astype(np.float64), pid.astype(np.float64) - Lid))
    Mplus = Msm + SMpi
    C = float(Mplus) - 2.0 * B
    H = float(Msm - SMpi)                      # = C - 2E exactly
    resid = abs((C - 2.0 * E) - H)
    return (n, x, Msm, SMpi, Mplus, B, C, E, H, resid)


rows = {}
for k in [6, 7, 8, 9]:
    y = math.isqrt(PRIM[k + 1]) + 1
    G["y"] = y
    lo, hi = block_ns(k)
    ns = list(range(lo, hi + 1))
    with Pool(NPROC) as pool:
        r = pool.map(one, ns, chunksize=16)
    rows[k] = r
    log(f"k={k}: {len(r)} samples, y={y}, max float resid {max(v[9] for v in r):.3e}")

# cross-check against wave-1 t7_agent6.csv (read-only)
ref = {}
with open(os.path.join(SRC, "t7_agent6.csv")) as fh:
    for rec in csv.DictReader(fh):
        ref[int(rec["X"])] = (int(rec["Msm"]), float(rec["C_minus_2E"]),
                              float(rec["E"]), int(rec["Mplus"]))
nchk = 0
for k in [6, 7, 8]:
    for v in rows[k]:
        if v[1] in ref:
            rMsm, rH, rE, rMplus = ref[v[1]]
            assert v[2] == rMsm, (v[1], v[2], rMsm)
            assert v[4] == rMplus, (v[1], v[4], rMplus)
            assert abs(v[8] - rH) < 1e-6, (v[1], v[8], rH)
            assert abs(v[7] - rE) < 1e-6, (v[1], v[7], rE)
            nchk += 1
log(f"cross-check vs wave-1 t7_agent6.csv: {nchk} samples agree exactly "
    f"(Msm, Mplus integer-identical; C-2E and E to 1e-6)")

with open(os.path.join(OUT, "c_scalarface.csv"), "w", newline="") as fh:
    w = csv.writer(fh)
    w.writerow(["k", "n", "X", "Msm", "sum_M_pi", "Mplus", "B", "C", "E",
                "H=C-2E", "float_resid"])
    for k in [6, 7, 8, 9]:
        for v in rows[k]:
            w.writerow([k] + list(v))

summ = {}
for k in [6, 7, 8, 9]:
    v = rows[k]
    x = np.array([r[1] for r in v], float)
    H = np.array([r[8] for r in v], float)
    C = np.array([r[6] for r in v], float)
    E = np.array([r[7] for r in v], float)
    nz = np.abs(H) > 0
    summ[k] = dict(
        n=len(v), x_range=[float(x.min()), float(x.max())],
        mean_absH_over_x=float(np.mean(np.abs(H) / x)),
        max_absH_over_x=float(np.max(np.abs(H) / x)),
        mean_absH_over_x_over_logx=float(np.mean(np.abs(H) / (x / np.log(x)))),
        mean_absH_over_sqrtx=float(np.mean(np.abs(H) / np.sqrt(x))),
        max_absH_over_sqrtx=float(np.max(np.abs(H) / np.sqrt(x))),
        H_positive_frac=float(np.mean(H > 0)),
        mean_H_over_sqrtx=float(np.mean(H / np.sqrt(x))),
        slope_log_absH=float(np.polyfit(np.log(x[nz]), np.log(np.abs(H[nz])), 1)[0]),
        mean_absC_over_x=float(np.mean(np.abs(C) / x)),
        mean_absE_over_x=float(np.mean(np.abs(E) / x)),
        mean_absC_over_sqrtx=float(np.mean(np.abs(C) / np.sqrt(x))),
        mean_absE_over_sqrtx=float(np.mean(np.abs(E) / np.sqrt(x))),
        slope_log_absE=float(np.polyfit(np.log(x), np.log(np.abs(E)), 1)[0]),
        slope_log_absC=float(np.polyfit(np.log(x), np.log(np.abs(C)), 1)[0]),
        mean_absH_over_absC=float(np.mean(np.abs(H) / np.abs(C))),
    )
KS = [6, 7, 8, 9]
xs = np.concatenate([np.array([r[1] for r in rows[k]], float) for k in KS])
Hs = np.concatenate([np.array([r[8] for r in rows[k]], float) for k in KS])
nz = np.abs(Hs) > 0
summ["global"] = dict(
    slope_log_absH=float(np.polyfit(np.log(xs[nz]), np.log(np.abs(Hs[nz])), 1)[0]),
    slope_block_mean_absH=float(np.polyfit(
        [math.log(np.mean([r[1] for r in rows[k]])) for k in KS],
        [math.log(np.mean([abs(r[8]) for r in rows[k]])) for k in KS], 1)[0]),
    block_mean_absH_over_x=[summ[k]["mean_absH_over_x"] for k in KS],
    block_mean_absH_over_sqrtx=[summ[k]["mean_absH_over_sqrtx"] for k in KS],
)
summ["_meta"] = dict(script="kt2_c.py", wall_s=time.time() - t0,
                     peak_rss_gb=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6,
                     max_float_resid=max(max(v[9] for v in rows[k]) for k in KS),
                     crosschecked_samples=nchk)
with open(os.path.join(OUT, "c_summary.json"), "w") as fh:
    json.dump(summ, fh, indent=1, default=float)
log("summary: " + json.dumps(summ["global"], indent=1))
for k in KS:
    log(f"k={k}: |H|/x mean {summ[k]['mean_absH_over_x']:.3e}, "
        f"|H|/(x/log x) {summ[k]['mean_absH_over_x_over_logx']:.3e}, "
        f"|H|/sqrt(x) {summ[k]['mean_absH_over_sqrtx']:.3f}, "
        f"slope log|H| {summ[k]['slope_log_absH']:.3f}")
log(f"done; wall={time.time()-t0:.1f}s peak RSS="
    f"{resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6:.2f} GB")
