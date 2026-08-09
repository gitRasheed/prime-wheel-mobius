#!/usr/bin/env python3
"""kill-test wave 2 (record 008), script B: agent7 renewal-vs-raw template
discrimination, rerun at X in 1e8-1e9 (wave 1 found the templates degenerate
below ~1e7).

Convention pinned to wave-1 t1_packets.py (RHLean PrimeWheelCoconductorGram):
  field  f = mu on (L_k, U_k], zero-padded on Z/Q_k
  window g_n = 1_{(L,X_n]} - rho_n 1_{(L,U]},  rho_n = (X_n - L)/Q_k
  packet A_q(X_n) = (1/Q) sum_{m,m'} mu(m) g_n(m') c_q(m'-m)
  conductor-normalized amplitude P_q = (Q/q) A_q
                                    = (1/q) sum_{a,b} F_q(a) c_q(b-a) G_q(b)
  F_q(a) = sum_{m in (L,U], m = a (q)} mu(m),  G_q(b) = cntX(b) - rho cntU(b)
Templates: renewal (X/q)^{1/2} vs raw per-character discrepancy
  Dpsi(X;q) = max_{gcd(b,q)=1} |psi(X;q,b) - X/phi(q)|.
Kill (proposer): "If the small-q amplitudes of H track the raw discrepancy
scale ... the renewal core is dead."
"""
import numpy as np, math, csv, json, os, time, resource, sys
from multiprocessing import Pool

PRIM = [1, 2, 6, 30, 210, 2310, 30030, 510510, 9699690, 223092870, 6469693230]
XCAP = 1_000_000_000
SRC = os.path.expanduser("~/work/killtests")
OUT = os.path.expanduser("~/work/killtests2")
os.makedirs(OUT, exist_ok=True)
NPROC = 14
MOD = 44100                       # 2^2 3^2 5^2 7^2; every q below divides it
QLIST = [2, 3, 4, 5, 6, 7, 9, 10, 12, 14, 15, 20, 21, 25, 28, 30, 35, 49,
         63, 105, 210, 225, 441]
SEG = 25_000_000
t0 = time.time()
def log(*a): print(f"[{time.time()-t0:7.1f}s]", *a, flush=True)

mu = np.load(os.path.join(SRC, "fw_mu.npy"), mmap_mode="r")
M = np.load(os.path.join(SRC, "fw_M_i32.npy"), mmap_mode="r")
pi_ = np.load(os.path.join(SRC, "fw_pi_i32.npy"), mmap_mode="r")
Li = np.load(os.path.join(SRC, "fw_Li_f64.npy"), mmap_mode="r")
assert M[6] == -1 and M[8] == -2 and M[30] == -3, "Mertens checkpoints"
assert abs((float(pi_[8] - pi_[6]) - float(Li[8] - Li[6]))
           - (1.0 - float(Li[8] - Li[6]))) < 1e-12, "E(6,8)"
log("hard asserts OK")

for q in QLIST:
    assert MOD % q == 0, q


def primes_upto(n):
    s = np.ones(n + 1, dtype=bool); s[:2] = False
    for p in range(2, math.isqrt(n) + 1):
        if s[p]: s[p * p:: p] = False
    return np.flatnonzero(s).astype(np.int64)


def phi_of(fac):
    r = 1
    for p, e in fac.items(): r *= (p - 1) * p ** (e - 1)
    return r


def factor(m):
    f = {}; d = 2
    while d * d <= m:
        while m % d == 0: f[d] = f.get(d, 0) + 1; m //= d
        d += 1
    if m > 1: f[m] = f.get(m, 0) + 1
    return f


def cq_vec(q):
    """Ramanujan sum c_q(j) for j = 0..q-1, exact ints."""
    qfac = factor(q)
    out = np.zeros(q, dtype=np.int64)
    for j in range(q):
        g = math.gcd(j, q) if j else q
        m = q // g
        mfac = factor(m)
        if any(e > 1 for e in mfac.values()):
            out[j] = 0
        elif mfac:
            out[j] = (-1) ** len(mfac) * phi_of(qfac) // phi_of(mfac)
        else:
            out[j] = phi_of(qfac)
    return out


CQ = {q: cq_vec(q) for q in QLIST}
PHI = {q: phi_of(factor(q)) for q in QLIST}
# sanity: sum_{j} c_q(j) = 0 for q > 1
for q in QLIST:
    assert CQ[q].sum() == 0, q
assert list(CQ[6]) == [2, 1, -1, -2, -1, 1], list(CQ[6])
log("Ramanujan sums OK")


def block_ns(k):
    L, U = PRIM[k], PRIM[k + 1]
    n_lo = math.isqrt(L + 1)
    while (n_lo + 1) ** 2 - 1 <= L: n_lo += 1
    n_hi = math.isqrt(U + 1) - 1
    while (n_hi + 2) ** 2 - 1 <= U: n_hi += 1
    n_cap = math.isqrt(XCAP + 1) - 1
    while (n_cap + 2) ** 2 - 1 <= XCAP: n_cap += 1
    return n_lo, min(n_hi, n_cap)


def fold_add(F, seg, lo):
    n = len(seg)
    pad = (-n) % MOD
    if pad:
        seg = np.concatenate([seg, np.zeros(pad, dtype=seg.dtype)])
    S = seg.reshape(-1, MOD).sum(axis=0, dtype=np.int64)
    F += np.roll(S, lo % MOD)


# ---------------- phase 1: residue-class Mobius sums per block ----------------
U9 = PRIM[10]
SMALL = primes_upto(math.isqrt(U9))
log(f"{len(SMALL)} primes <= isqrt(U_9) = {math.isqrt(U9)}")


def mu_seg_fold(lo):
    hi = min(lo + SEG, U9 + 1)
    n = hi - lo
    m = np.ones(n, dtype=np.int8)
    res = np.arange(lo, hi, dtype=np.int64)
    if lo == 0: m[0] = 0
    for p in SMALL:
        p = int(p)
        st = ((lo + p - 1) // p) * p - lo
        m[st::p] *= -1
        res[st::p] //= p
        p2 = p * p
        st2 = ((lo + p2 - 1) // p2) * p2 - lo
        m[st2::p2] = 0
    m[(res > 1) & (m != 0)] *= -1
    del res
    ok = None
    if hi <= XCAP + 1:                      # verify against the wave-1 exact sieve
        ref = np.load(os.path.join(SRC, "fw_mu.npy"), mmap_mode="r")[lo:hi]
        ok = bool(np.array_equal(m, np.asarray(ref)))
    F = np.zeros(MOD, dtype=np.int64)
    m64 = m.astype(np.int64)
    fold_add(F, m64, lo)
    return lo, hi, F, int(m64.sum()), ok


FMOD = {}
for k in [4, 5, 6, 7, 8]:
    L, U = PRIM[k], PRIM[k + 1]
    F = np.zeros(MOD, dtype=np.int64)
    for lo in range(L + 1, U + 1, SEG):
        hi = min(lo + SEG, U + 1)
        fold_add(F, np.asarray(mu[lo:hi]).astype(np.int64), lo)
    assert F.sum() == int(M[U]) - int(M[L]), (k, F.sum(), int(M[U]) - int(M[L]))
    FMOD[k] = F
    log(f"k={k}: residue sums built, total = {F.sum()} = M(U)-M(L) OK")

CACHE = os.path.join(OUT, "b_F9.npy")
L9 = PRIM[9]
if os.path.exists(CACHE):
    FMOD[9] = np.load(CACHE)
    log(f"k=9: loaded cached residue sums (verified on the run that built them);"
        f" total = {FMOD[9].sum()}")
else:
  log("k=9: segmented mu sieve over (223092870, 6469693230] -- heavy phase")
  jobs = list(range(L9 + 1, U9 + 1, SEG))
  F9 = np.zeros(MOD, dtype=np.int64)
  tot9 = 0
  ver = []                     # (lo, hi, segment mu-sum) for verified segments
  with Pool(NPROC) as pool:
    for lo, hi, F, s, ok in pool.imap_unordered(mu_seg_fold, jobs, chunksize=1):
        F9 += F; tot9 += s
        if ok is not None:
            assert ok, f"mu sieve MISMATCH vs fw_mu at segment [{lo},{hi})"
            ver.append((lo, hi, s))
  FMOD[9] = F9
  ver.sort()
  assert ver[0][0] == L9 + 1
  for i in range(1, len(ver)):
    assert ver[i][0] == ver[i - 1][1], "verified segments not contiguous"
  cap = ver[-1][1] - 1
  part = sum(v[2] for v in ver)
  log(f"k=9 done: {len(ver)} segments byte-identical to fw_mu (prefix (L9,{cap}]);"
      f" sum mu over that prefix = {part} (expected M({cap})-M(L9) = "
      f"{int(M[cap]) - int(M[L9])}); sum mu over (L9,U9] = {tot9}")
  assert part == int(M[cap]) - int(M[L9])
  assert F9.sum() == tot9
  np.save(CACHE, F9)

np.savez(os.path.join(OUT, "b_Fmod.npz"), **{f"k{k}": FMOD[k] for k in FMOD})

# ---------------- phase 2: packet amplitudes P_q ----------------
def wheel_Q_log10(k):
    U = PRIM[k + 1]
    ps = primes_upto(math.isqrt(U))
    return 2.0 * float(np.log10(ps.astype(np.float64)).sum())


def picks(k, cnt=16):
    lo, hi = block_ns(k)
    ns = np.unique(np.round(np.exp(np.linspace(math.log(lo), math.log(hi), cnt))
                            ).astype(np.int64))
    return [int(v) for v in ns]


def Pq_at(k, X, q, rho=0.0):
    """conductor-normalized packet amplitude P_q = (Q/q) A_q at window end X."""
    L, U = PRIM[k], PRIM[k + 1]
    Fq = FMOD[k].reshape(MOD // q, q).sum(axis=0)
    b = np.arange(q, dtype=np.int64)
    cntX = (X - b) // q - (L - b) // q
    cntU = (U - b) // q - (L - b) // q
    Gv = (cntX - rho * cntU).astype(np.float64)
    c = CQ[q]
    idx = (b[None, :] - b[:, None]) % q
    return float(Fq.astype(np.float64) @ (c[idx].astype(np.float64) @ Gv)) / q


# --- cross-check against wave-1 t1_smallq.csv (same convention, k=6,7) ---
nx = 0
maxrel = 0.0
try:
    with open(os.path.join(SRC, "t1_smallq.csv")) as fh:
        for rec in csv.DictReader(fh):
            k = int(rec["k"]); q = int(rec["q"])
            if k not in (6, 7) or q not in QLIST: continue
            X = int(rec["X"]); ref = float(rec["P_q"])
            got = Pq_at(k, X, q)
            den = max(abs(ref), 1.0)
            maxrel = max(maxrel, abs(got - ref) / den)
            nx += 1
    log(f"wave-1 cross-check: {nx} (k,n,q) packet amplitudes reproduced, "
        f"max rel dev {maxrel:.3e}")
    assert maxrel < 1e-9
except FileNotFoundError:
    log("wave-1 t1_smallq.csv not found; cross-check skipped")

# --- exact q-periodicity of P_q in X (rho underflows to 0 for k >= 4) ---
per = {}
for k in [4, 5, 6, 7, 8, 9]:
    L = PRIM[k]
    for q in QLIST:
        vals = [Pq_at(k, L + 1 + t, q) for t in range(3 * q + 1)]
        ok = all(abs(vals[t] - vals[t + q]) < 1e-9 * max(1.0, abs(vals[t]))
                 for t in range(2 * q + 1))
        per[(k, q)] = (ok, len(set(round(v, 9) for v in vals)),
                       max(abs(v) for v in vals))
        assert ok, f"P_q NOT q-periodic in X at k={k} q={q}"
log(f"P_q is exactly q-periodic in X for all {len(per)} (k,q) pairs tested "
    f"(k=4..9); amplitude envelope recorded")

rowsP = []
for k in [6, 7, 8, 9]:
    L, U = PRIM[k], PRIM[k + 1]
    lQ = wheel_Q_log10(k)
    for n in picks(k):
        X = (n + 1) ** 2 - 1
        lrho = math.log10(X - L) - lQ
        rho = 0.0 if lrho < -280 else 10 ** lrho
        for q in QLIST:
            Pq = Pq_at(k, X, q, rho)
            rowsP.append([k, n, X, q, Pq, abs(Pq), math.sqrt(X / q), lrho])
log(f"packet amplitudes: {len(rowsP)} rows")

# ---------------- phase 3: raw per-character discrepancy Dpsi ----------------
log("extracting primes <= 1e9 and prime powers")
prs = []
for lo in range(0, XCAP, 50_000_000):
    hi = min(lo + 50_000_000, XCAP)
    d = np.asarray(pi_[lo + 1:hi + 1], np.int64) - np.asarray(pi_[lo:hi], np.int64)
    prs.append(np.flatnonzero(d).astype(np.int64) + lo + 1)
prs = np.concatenate(prs)
assert len(prs) == 50847534, len(prs)
extra_v, extra_l = [], []
for p in prs[prs <= math.isqrt(XCAP)]:
    p = int(p); pe = p * p
    while pe <= XCAP:
        extra_v.append(pe); extra_l.append(math.log(p)); pe *= p
PP = np.concatenate([prs, np.array(extra_v, dtype=np.int64)])
LP = np.concatenate([np.log(prs.astype(np.float64)),
                     np.array(extra_l, dtype=np.float64)])
o = np.argsort(PP, kind="stable")
PP = PP[o]; LP = LP[o]
del prs, extra_v, extra_l, o
log(f"{len(PP)} prime powers <= 1e9; psi(1e9) = {LP.sum():.1f} (expect ~1e9)")
assert abs(LP.sum() - XCAP) < 5e4, LP.sum()

SAMPLES = sorted({(k, n, (n + 1) ** 2 - 1) for k in [6, 7, 8, 9] for n in picks(k)},
                 key=lambda t: t[2])


def dpsi_q(q):
    res = (PP % q).astype(np.int32)
    out = []
    for (k, n, X) in SAMPLES:
        iX = int(np.searchsorted(PP, X, side="right"))
        ps = np.bincount(res[:iX], weights=LP[:iX], minlength=q)
        cop = np.array([math.gcd(bb, q) == 1 for bb in range(q)])
        dev = ps[cop] - X / PHI[q]
        out.append((k, n, X, q, float(np.max(np.abs(dev))),
                    float(np.sqrt(np.mean(dev ** 2)))))
    return out


with Pool(min(NPROC, len(QLIST))) as pool:
    dres = pool.map(dpsi_q, QLIST)
DPSI = {}
for blockres in dres:
    for (k, n, X, q, mx, rms) in blockres:
        DPSI[(n, q)] = (mx, rms)
log("Dpsi done")

# ---------------- phase 4: join + slopes ----------------
rows = []
for r in rowsP:
    k, n, X, q, Pq, aPq, renew, lrho = r
    mx, rms = DPSI[(n, q)]
    rows.append([k, n, X, q, Pq, aPq, renew, mx, rms, aPq / renew,
                 aPq / max(mx, 1e-30), lrho])
with open(os.path.join(OUT, "b_smallq.csv"), "w", newline="") as fh:
    w = csv.writer(fh)
    w.writerow(["k", "n", "X", "q", "P_q", "abs_P_q", "sqrt_X_over_q", "Dpsi_max",
                "Dpsi_rms", "ratio_renewal", "ratio_rawdisc", "log10_rho"])
    w.writerows(rows)

A = np.array([[r[2], r[3], r[5], r[6], r[7], r[8]] for r in rows], float)
summ = {"per_q": {}}
for q in QLIST:
    m = A[:, 1] == q
    x = A[m, 0]; ap = A[m, 2]; rn = A[m, 3]; dp = A[m, 4]
    hi = x >= 1e7
    nz = ap > 0
    summ["per_q"][q] = dict(
        slope_absPq_all=float(np.polyfit(np.log(x[nz]), np.log(ap[nz]), 1)[0]),
        slope_absPq_hi=float(np.polyfit(np.log(x[hi & nz]), np.log(ap[hi & nz]), 1)[0]),
        slope_Dpsi_all=float(np.polyfit(np.log(x), np.log(dp), 1)[0]),
        slope_Dpsi_hi=float(np.polyfit(np.log(x[hi]), np.log(dp[hi]), 1)[0]),
        ratio_renewal_hi_mean=float(np.mean(ap[hi] / rn[hi])),
        ratio_rawdisc_hi_mean=float(np.mean(ap[hi] / dp[hi])),
        ratio_renewal_top=float(ap[x == x.max()][0] / rn[x == x.max()][0]),
        ratio_rawdisc_top=float(ap[x == x.max()][0] / dp[x == x.max()][0]),
    )
# q-profile at the top few samples: renewal predicts d log|P_q| / d log q = -1/2
xs_top = sorted(set(A[:, 0]))[-5:]
qprof = {}
for xv in xs_top:
    m = A[:, 0] == xv
    q = A[m, 1]; ap = A[m, 2]; dp = A[m, 4]
    nz = ap > 0
    qprof[int(xv)] = dict(
        slope_absPq_vs_q=float(np.polyfit(np.log(q[nz]), np.log(ap[nz]), 1)[0]),
        slope_Dpsi_vs_q=float(np.polyfit(np.log(q), np.log(dp), 1)[0]),
        slope_renewal_vs_q=-0.5,
        corr_logP_logDpsi=float(np.corrcoef(np.log(ap[nz]), np.log(dp[nz]))[0, 1]),
        corr_logP_logrenew=float(np.corrcoef(np.log(ap[nz]),
                                             np.log(A[m, 3][nz]))[0, 1]),
    )
summ["q_profile_top_samples"] = qprof

# --- amplitude envelope per (block, q): P_q depends only on X mod q ---
env = {}
for k in [4, 5, 6, 7, 8, 9]:
    L, U = PRIM[k], PRIM[k + 1]
    Xtop = U if k < 9 else 999950883
    for q in QLIST:
        ok, ndist, amp = per[(k, q)]
        env[f"k{k}_q{q}"] = dict(
            q_periodic=bool(ok), n_distinct_values=int(ndist), amp_max=float(amp),
            amp_over_sqrt_U_over_q=float(amp / math.sqrt(U / q)),
            amp_over_sqrt_blocklen_over_q=float(amp / math.sqrt((U - L) / q)),
            amp_over_Dpsi_top=float(amp / max(DPSI.get((picks(k)[-1], q), (1.0,))[0], 1e-30))
            if k in (6, 7, 8, 9) else None,
            U=U, sqrt_U_over_q=math.sqrt(U / q))
summ["amplitude_envelope"] = env
summ["envelope_growth"] = {}
for q in QLIST:
    ks = [4, 5, 6, 7, 8, 9]
    us = [math.log(PRIM[k + 1]) for k in ks]
    am = [math.log(max(env[f"k{k}_q{q}"]["amp_max"], 1e-30)) for k in ks]
    summ["envelope_growth"][q] = dict(
        slope_logAmp_vs_logU=float(np.polyfit(us, am, 1)[0]),
        amp_by_block={k: env[f"k{k}_q{q}"]["amp_max"] for k in ks})
summ["_meta"] = dict(script="kt2_b.py", wall_s=time.time() - t0,
                     peak_rss_gb=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6,
                     n_samples=len(SAMPLES), qlist=QLIST,
                     rho_note="rho_k = (X-L)/Q_k underflows to 0 for k>=4 "
                              "(log10 rho <= -280); recorded per row as log10_rho")
with open(os.path.join(OUT, "b_summary.json"), "w") as fh:
    json.dump(summ, fh, indent=1, default=float)
log("summary: " + json.dumps(summ["q_profile_top_samples"], indent=1))
for q in [2, 3, 5, 6, 15, 30, 105, 210]:
    s = summ["per_q"][q]
    log(f"q={q}: slope|P| hi={s['slope_absPq_hi']:+.3f} slopeDpsi hi={s['slope_Dpsi_hi']:+.3f}"
        f" |P|/renewal={s['ratio_renewal_top']:.3f} |P|/Dpsi={s['ratio_rawdisc_top']:.3f}")
log(f"done; wall={time.time()-t0:.1f}s peak RSS="
    f"{resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6:.2f} GB")
