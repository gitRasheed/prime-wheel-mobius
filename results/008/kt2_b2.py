#!/usr/bin/env python3
"""kill-test wave 2 (record 008), script B2: convention-sensitivity check for
agent7 (b).

Under the kernel-extracted convention Q_k = (U_k//P+1)P with P = prod_{p<=sqrt U} p^2,
rho_n = (X_n - L)/Q_k underflows to 0 (record 006 "modulus-magnitude obstacle"),
which is what makes P_q exactly q-periodic in X.  agent7's own text says
"Q_k the repo's minimal admissible modulus > 6*U_k".  This script recomputes the
amplitudes under Q = 6*U_k (rho = (X-L)/(6 U)) to check that the verdict is not
an artifact of the modulus convention.
"""
import numpy as np, math, json, csv, os, time
PRIM = [1, 2, 6, 30, 210, 2310, 30030, 510510, 9699690, 223092870, 6469693230]
XCAP = 1_000_000_000
SRC = os.path.expanduser("~/work/killtests")
OUT = os.path.expanduser("~/work/killtests2")
MOD = 44100
QLIST = [2, 3, 5, 6, 10, 15, 30]          # agent7's own small-q set
t0 = time.time()
def log(*a): print(f"[{time.time()-t0:6.1f}s]", *a, flush=True)

mu = np.load(os.path.join(SRC, "fw_mu.npy"), mmap_mode="r")
M = np.load(os.path.join(SRC, "fw_M_i32.npy"), mmap_mode="r")
pi_ = np.load(os.path.join(SRC, "fw_pi_i32.npy"), mmap_mode="r")
Li = np.load(os.path.join(SRC, "fw_Li_f64.npy"), mmap_mode="r")
assert M[6] == -1 and M[8] == -2 and M[30] == -3
assert abs((float(pi_[8] - pi_[6]) - float(Li[8] - Li[6]))
           - (1.0 - float(Li[8] - Li[6]))) < 1e-12
log("hard asserts OK")


def factor(m):
    f = {}; d = 2
    while d * d <= m:
        while m % d == 0: f[d] = f.get(d, 0) + 1; m //= d
        d += 1
    if m > 1: f[m] = f.get(m, 0) + 1
    return f


def phi_of(f):
    r = 1
    for p, e in f.items(): r *= (p - 1) * p ** (e - 1)
    return r


def cq_vec(q):
    qf = factor(q); out = np.zeros(q, dtype=np.int64)
    for j in range(q):
        g = math.gcd(j, q) if j else q
        m = q // g; mf = factor(m)
        out[j] = 0 if any(e > 1 for e in mf.values()) else (
            (-1) ** len(mf) * phi_of(qf) // phi_of(mf) if mf else phi_of(qf))
    return out


CQ = {q: cq_vec(q) for q in QLIST}
SEG = 25_000_000
FMOD = {}
for k in [6, 7, 8]:
    L, U = PRIM[k], PRIM[k + 1]
    F = np.zeros(MOD, dtype=np.int64)
    for lo in range(L + 1, U + 1, SEG):
        hi = min(lo + SEG, U + 1)
        seg = np.asarray(mu[lo:hi]).astype(np.int64)
        pad = (-len(seg)) % MOD
        if pad: seg = np.concatenate([seg, np.zeros(pad, dtype=np.int64)])
        F += np.roll(seg.reshape(-1, MOD).sum(axis=0, dtype=np.int64), lo % MOD)
    assert F.sum() == int(M[U]) - int(M[L])
    FMOD[k] = F
FMOD[9] = np.load(os.path.join(OUT, "b_F9.npy"))
log("residue sums ready (k=9 from cache built by kt2_b.py)")


def Pq_at(k, X, q, rho):
    L, U = PRIM[k], PRIM[k + 1]
    Fq = FMOD[k].reshape(MOD // q, q).sum(axis=0)
    b = np.arange(q, dtype=np.int64)
    G = ((X - b) // q - (L - b) // q) - rho * ((U - b) // q - (L - b) // q)
    idx = (b[None, :] - b[:, None]) % q
    return float(Fq.astype(np.float64) @ (CQ[q][idx].astype(np.float64)
                                          @ G.astype(np.float64))) / q


def block_ns(k):
    L, U = PRIM[k], PRIM[k + 1]
    lo = math.isqrt(L + 1)
    while (lo + 1) ** 2 - 1 <= L: lo += 1
    hi = math.isqrt(U + 1) - 1
    while (hi + 2) ** 2 - 1 <= U: hi += 1
    cap = math.isqrt(XCAP + 1) - 1
    while (cap + 2) ** 2 - 1 <= XCAP: cap += 1
    return lo, min(hi, cap)


rows = []
res = {}
for k in [6, 7, 8, 9]:
    L, U = PRIM[k], PRIM[k + 1]
    lo, hi = block_ns(k)
    ns = np.unique(np.round(np.exp(np.linspace(math.log(lo), math.log(hi), 24))
                            ).astype(np.int64))
    for q in QLIST:
        xs, a6, a0 = [], [], []
        for n in ns:
            X = int(n + 1) ** 2 - 1
            p6 = Pq_at(k, X, q, (X - L) / (6.0 * U))
            p0 = Pq_at(k, X, q, 0.0)
            xs.append(X); a6.append(abs(p6)); a0.append(abs(p0))
            rows.append([k, int(n), X, q, p0, p6, math.sqrt(X / q)])
        xs = np.array(xs, float); a6 = np.array(a6); a0 = np.array(a0)
        nz6 = a6 > 0; nz0 = a0 > 0
        res[f"k{k}_q{q}"] = dict(
            slope_absP_Qkernel=float(np.polyfit(np.log(xs[nz0]), np.log(a0[nz0]), 1)[0])
            if nz0.sum() > 2 else None,
            slope_absP_Q6U=float(np.polyfit(np.log(xs[nz6]), np.log(a6[nz6]), 1)[0]),
            mean_ratio_renewal_Q6U=float(np.mean(a6 / np.sqrt(xs / q))),
            top_ratio_renewal_Q6U=float(a6[-1] / math.sqrt(xs[-1] / q)),
            mean_absP_Q6U=float(a6.mean()), mean_absP_Qkernel=float(a0.mean()))
with open(os.path.join(OUT, "b2_convention.csv"), "w", newline="") as fh:
    w = csv.writer(fh)
    w.writerow(["k", "n", "X", "q", "P_q_rho0_kernelQ", "P_q_rho_Q6U", "sqrt_X_over_q"])
    w.writerows(rows)
# q-slopes under Q = 6U at the top sample of each block
qs = np.array(QLIST, float)
qslope = {}
for k in [6, 7, 8, 9]:
    v = [res[f"k{k}_q{q}"]["mean_absP_Q6U"] for q in QLIST]
    qslope[k] = float(np.polyfit(np.log(qs), np.log(np.array(v)), 1)[0])
summ = dict(per_k_q=res, qslope_meanabsP_Q6U_vs_q=qslope,
            note="renewal template predicts d log|P_q| / d log X = +0.5 and "
                 "d log|P_q| / d log q = -0.5")
with open(os.path.join(OUT, "b2_summary.json"), "w") as fh:
    json.dump(summ, fh, indent=1, default=float)
for k in [6, 7, 8, 9]:
    for q in QLIST:
        r = res[f"k{k}_q{q}"]
        log(f"k={k} q={q:2d}: X-slope |P| (Q=6U) {r['slope_absP_Q6U']:+.3f} "
            f"(kernel-Q {r['slope_absP_Qkernel']}) mean|P|/renewal(6U) "
            f"{r['mean_ratio_renewal_Q6U']:.3f}")
log("q-slopes of mean|P| under Q=6U: " + json.dumps(qslope))
log(f"done wall={time.time()-t0:.1f}s")
