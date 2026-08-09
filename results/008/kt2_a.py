#!/usr/bin/env python3
"""kill-test wave 2 (record 008), script A.

Implements, at pinned square samples X_n = (n+1)^2 - 1 under the verified
kernel conventions (L_k = primorial(k), U_k = primorial(k+1),
y_k = isqrt(U_k)+1, d = 1..x//(y+1), b_d = x//d, a_d = max(y, x//(d+1)),
Delta_d = (pi(b)-pi(a)) - (Li(b)-Li(a)), E = sum_d M(d) Delta_d):

  T-A6K3  agent6 Kill 3: diagonal  Diag(x) = sum_d M(d)^2 Delta_d^2
          and off-diagonal dispersion Off(x) = sum_{d!=d'} M(d)M(d')Delta_d Delta_d'
          = E(x)^2 - Diag(x).  Kill: empirical exponent in x clearly above ~1.2.
  T-A1a   agent1 (a): principal-character / square-moduli locus
          S_sq(x) = sum_{m^2} M(m^2) Delta_{m^2}(x).
          Kill: grows with a fixed sign at exponent visibly above 1/2.
  T-A1b   agent1 (b): dyadic-block sums B_j = sum_{2^j <= d < 2^{j+1}} M(d)Delta_d
          and their correlation matrix.  Kill: blocks strongly positively
          correlated (no cancellation across the d-family).
  T-A8    agent8: window (r < H) variance of E(X_{N+r}) decomposed by dyadic d.
          Kill: >= 90% of window-centered variance in d > N^{1-o(1)}.
          Secondary: Weyl sums sum_{r<H} e(X_{N+r}(1/d - 1/e)) over prime pairs
          d,e in (N/2,N], near-primorial vs mid-block windows.

Arrays are the wave-1 framework (read-only, never modified).
"""
import numpy as np, math, csv, json, os, time, resource, itertools
from multiprocessing import Pool

PRIM = [1, 2, 6, 30, 210, 2310, 30030, 510510, 9699690, 223092870, 6469693230]
XCAP = 1_000_000_000          # framework arrays stop here
SRC = os.path.expanduser("~/work/killtests")
OUT = os.path.expanduser("~/work/killtests2")
os.makedirs(OUT, exist_ok=True)
NPROC = 14
t0 = time.time()
def log(*a): print(f"[{time.time()-t0:7.1f}s]", *a, flush=True)

M = np.load(os.path.join(SRC, "fw_M_i32.npy"), mmap_mode="r")
pi = np.load(os.path.join(SRC, "fw_pi_i32.npy"), mmap_mode="r")
Li = np.load(os.path.join(SRC, "fw_Li_f64.npy"), mmap_mode="r")

# ---- hard asserts required of every wave-2 script ----
assert M[6] == -1 and M[8] == -2 and M[30] == -3, "Mertens checkpoints"
_E68 = float(pi[8] - pi[6]) - float(Li[8] - Li[6])       # y=6, x=8: only d=1
assert abs(_E68 - (1.0 - float(Li[8] - Li[6]))) < 1e-12, "E(6,8)"
assert M[210] == -1 and M[2310] == -1 and M[30030] == 16
assert pi[100_000_000] == 5761455 and pi[1_000_000_000] == 50847534
log("hard asserts OK: M(6)=-1 M(8)=-2 M(30)=-3, E(6,8)=1-(Li(8)-Li(6))")


def block_ns(k):
    L, U = PRIM[k], PRIM[k + 1]
    n_lo = math.isqrt(L + 1)
    while (n_lo + 1) ** 2 - 1 <= L: n_lo += 1
    n_hi = math.isqrt(U + 1) - 1
    while (n_hi + 2) ** 2 - 1 <= U: n_hi += 1
    n_cap = math.isqrt(XCAP + 1) - 1
    while (n_cap + 2) ** 2 - 1 <= XCAP: n_cap += 1
    return n_lo, min(n_hi, n_cap)


def yk(k):
    return math.isqrt(PRIM[k + 1]) + 1


G = {}
JMAX = 16


def recip(x, y):
    dmax = x // (y + 1)
    d = np.arange(1, dmax + 1, dtype=np.int64)
    b = x // d
    a = np.maximum(y, x // (d + 1))
    ok = a < b
    return d[ok], b[ok], a[ok], dmax


def delta_at(d, b, a):
    pid = pi[b].astype(np.int64) - pi[a].astype(np.int64)
    Lid = Li[b] - Li[a]
    return pid, pid.astype(np.float64) - Lid


def per_sample(n):
    y = G["y"]
    x = (n + 1) ** 2 - 1
    d, b, a, dmax = recip(x, y)
    Mi = M[d].astype(np.int64)
    pid, Pid = delta_at(d, b, a)
    Md = Mi.astype(np.float64)
    w = Md * Pid
    E = float(w.sum())
    Diag = float((w * w).sum())
    Off = E * E - Diag
    Diag_int = int(((Mi * pid) ** 2).sum())          # exact-integer analogue
    # --- agent1 (a): square moduli d = m^2 ---
    mm = np.arange(1, math.isqrt(dmax) + 1, dtype=np.int64)
    sq = mm * mm
    bs = x // sq
    as_ = np.maximum(y, x // (sq + 1))
    okq = as_ < bs
    sq, bs, as_ = sq[okq], bs[okq], as_[okq]
    _, Psq = delta_at(sq, bs, as_)
    Msq = M[sq].astype(np.float64)
    wsq = Msq * Psq
    Ssq = float(wsq.sum())
    Ssq_abs = float(np.abs(wsq).sum())
    # --- agent1 (b): dyadic blocks ---
    jj = (np.frexp(d.astype(np.float64))[1] - 1).astype(np.int64)
    Bv = np.bincount(jj, weights=w, minlength=JMAX)[:JMAX]
    sumabs = float(np.abs(Bv).sum())
    sumabs_terms = float(np.abs(w).sum())
    return (n, x, dmax, len(d), E, Diag, Off, Diag_int, Ssq, Ssq_abs,
            len(sq), sumabs, Bv, sumabs_terms)


def run_blocks(ks):
    rows_all = {}
    for k in ks:
        y = yk(k)
        G["y"] = y
        lo, hi = block_ns(k)
        ns = list(range(lo, hi + 1))
        log(f"k={k}: L={PRIM[k]} U={PRIM[k+1]} y={y} samples n={lo}..{hi} ({len(ns)})"
            f" X={(lo+1)**2-1}..{(hi+1)**2-1}")
        with Pool(NPROC) as pool:
            rows = pool.map(per_sample, ns, chunksize=16)
        rows_all[k] = rows
        with open(os.path.join(OUT, f"a_samples_k{k}.csv"), "w", newline="") as fh:
            w = csv.writer(fh)
            w.writerow(["n", "X", "dmax", "n_d", "E", "Diag", "Off", "Diag_int",
                        "S_sq", "S_sq_abs", "n_sq", "sum_abs_Bj",
                        "sum_abs_terms"] + [f"B{j}" for j in range(JMAX)])
            for r in rows:
                w.writerow(list(r[:12]) + [r[13]] + [f"{v:.6g}" for v in r[12]])
        log(f"  k={k} done")
    return rows_all


# =====================================================================
log("=== part 1: per-sample sweeps (agent6 kill3, agent1 a+b) ===")
KS = [6, 7, 8, 9]
rows_all = run_blocks(KS)

summary = {}
# ---- agent6 kill 3 ----
a6 = {}
allx, allD, allO = [], [], []
for k in KS:
    R = rows_all[k]
    x = np.array([r[1] for r in R], float)
    D = np.array([r[5] for r in R], float)
    O = np.array([r[6] for r in R], float)
    E = np.array([r[4] for r in R], float)
    allx.append(x); allD.append(D); allO.append(O)
    sD = float(np.polyfit(np.log(x), np.log(D), 1)[0])
    mo = np.abs(O) > 0
    sO = float(np.polyfit(np.log(x[mo]), np.log(np.abs(O[mo])), 1)[0])
    a6[k] = dict(
        n_samples=len(R),
        x_range=[float(x.min()), float(x.max())],
        slope_logDiag=sD, slope_logAbsOff=sO,
        Diag_over_x_mean=float(np.mean(D / x)),
        Diag_over_x_first=float(D[0] / x[0]), Diag_over_x_last=float(D[-1] / x[-1]),
        absOff_over_x_mean=float(np.mean(np.abs(O) / x)),
        absOff_over_x_last=float(np.abs(O[-1]) / x[-1]),
        Off_positive_frac=float(np.mean(O > 0)),
        E2_over_x_mean=float(np.mean(E * E / x)),
        Off_over_Diag_mean=float(np.mean(O / D)),
    )
X = np.concatenate(allx); Dg = np.concatenate(allD); Of = np.concatenate(allO)
a6["global"] = dict(
    slope_logDiag=float(np.polyfit(np.log(X), np.log(Dg), 1)[0]),
    slope_logAbsOff=float(np.polyfit(np.log(X[np.abs(Of) > 0]),
                                     np.log(np.abs(Of[np.abs(Of) > 0])), 1)[0]),
    slope_block_mean_Diag=float(np.polyfit(
        [math.log(np.mean(allx[i])) for i in range(len(KS))],
        [math.log(np.mean(allD[i])) for i in range(len(KS))], 1)[0]),
    slope_block_mean_absOff=float(np.polyfit(
        [math.log(np.mean(allx[i])) for i in range(len(KS))],
        [math.log(np.mean(np.abs(allO[i]))) for i in range(len(KS))], 1)[0]),
)
summary["agent6_kill3"] = a6
log("agent6 kill3: " + json.dumps(a6["global"], indent=1))

# ---- agent1 (a) ----
a1a = {}
for k in KS:
    R = rows_all[k]
    x = np.array([r[1] for r in R], float)
    S = np.array([r[8] for r in R], float)
    Sa = np.array([r[9] for r in R], float)
    E = np.array([r[4] for r in R], float)
    ms = np.abs(S) > 0
    a1a[k] = dict(
        n_terms_range=[int(min(r[10] for r in R)), int(max(r[10] for r in R))],
        mean_S_sq=float(S.mean()), median_S_sq=float(np.median(S)),
        pos_frac=float(np.mean(S > 0)),
        mean_abs_S=float(np.abs(S).mean()),
        slope_log_absS=float(np.polyfit(np.log(x[ms]), np.log(np.abs(S[ms])), 1)[0]),
        mean_absS_over_sqrtx=float(np.mean(np.abs(S) / np.sqrt(x))),
        max_absS_over_sqrtx=float(np.max(np.abs(S) / np.sqrt(x))),
        mean_S_over_sqrtx=float(np.mean(S / np.sqrt(x))),
        mean_absS_over_absE=float(np.mean(np.abs(S) / np.maximum(np.abs(E), 1e-30))),
        mean_absS_over_Ssqabs=float(np.mean(np.abs(S) / np.maximum(Sa, 1e-30))),
        t_stat_mean_S_over_sqrtx=float(np.mean(S / np.sqrt(x)) /
                                       (np.std(S / np.sqrt(x)) / math.sqrt(len(S)))),
    )
xs = np.concatenate([np.array([r[1] for r in rows_all[k]], float) for k in KS])
Ss = np.concatenate([np.array([r[8] for r in rows_all[k]], float) for k in KS])
m = np.abs(Ss) > 0
a1a["global"] = dict(
    slope_log_absS=float(np.polyfit(np.log(xs[m]), np.log(np.abs(Ss[m])), 1)[0]),
    slope_block_mean_absS=float(np.polyfit(
        [math.log(np.mean([r[1] for r in rows_all[k]])) for k in KS],
        [math.log(np.mean([abs(r[8]) for r in rows_all[k]])) for k in KS], 1)[0]),
    slope_block_mean_signedS=float(np.polyfit(
        [math.log(np.mean([r[1] for r in rows_all[k]])) for k in KS],
        [math.log(max(abs(np.mean([r[8] for r in rows_all[k]])), 1e-30)) for k in KS], 1)[0]),
    block_mean_signed=[float(np.mean([r[8] for r in rows_all[k]])) for k in KS],
)
summary["agent1_a_square_locus"] = a1a
log("agent1(a): " + json.dumps(a1a["global"], indent=1))

# ---- agent1 (b) ----
a1b = {}
for k in KS:
    R = rows_all[k]
    x = np.array([r[1] for r in R], float)
    B = np.stack([r[12] for r in R])                   # (nsamples, JMAX)
    E = np.array([r[4] for r in R], float)
    sa = np.array([r[11] for r in R], float)
    keep = np.flatnonzero(B.std(axis=0) > 0)
    Bk = B[:, keep]
    Cr = np.corrcoef(Bk.T)
    Bn = Bk / np.sqrt(x)[:, None]                      # scale-detrended
    Crn = np.corrcoef(Bn.T)
    off = ~np.eye(len(keep), dtype=bool)
    # per-sample sign structure
    sgn_agree = np.mean([np.mean(np.sign(b[keep]) == np.sign(e))
                         for b, e in zip(B, E)])
    a1b[k] = dict(
        dyadic_js=[int(j) for j in keep],
        d_ranges=[[int(2 ** j), int(2 ** (j + 1) - 1)] for j in keep],
        mean_offdiag_corr=float(Cr[off].mean()),
        max_offdiag_corr=float(Cr[off].max()), min_offdiag_corr=float(Cr[off].min()),
        pos_offdiag_frac=float(np.mean(Cr[off] > 0)),
        mean_offdiag_corr_detrended=float(Crn[off].mean()),
        pos_offdiag_frac_detrended=float(np.mean(Crn[off] > 0)),
        mean_cancel_ratio_absE_over_sumabsB=float(np.mean(np.abs(E) / np.maximum(sa, 1e-30))),
        mean_cancel_ratio_absE_over_sum_abs_terms=float(
            np.mean(np.abs(E) / np.maximum(np.array([r[13] for r in R]), 1e-30))),
        var_E_over_sum_var_Bj=float(E.var() / Bk.var(axis=0).sum()),
        n_dyadic_blocks=int(len(keep)),
        sqrt_n_dyadic=float(math.sqrt(len(keep))),
        mean_sign_agreement_with_E=float(sgn_agree),
        mean_abs_Bj=[float(np.abs(B[:, j]).mean()) for j in keep],
    )
    with open(os.path.join(OUT, f"a_dyadic_corr_k{k}.csv"), "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["j"] + [f"j{int(j)}" for j in keep])
        for i, j in enumerate(keep):
            w.writerow([int(j)] + [f"{v:.5f}" for v in Cr[i]])
        w.writerow([])
        w.writerow(["detrended (B_j / sqrt(x))"])
        w.writerow(["j"] + [f"j{int(j)}" for j in keep])
        for i, j in enumerate(keep):
            w.writerow([int(j)] + [f"{v:.5f}" for v in Crn[i]])
summary["agent1_b_dyadic_corr"] = a1b
log("agent1(b) k=9: " + json.dumps(a1b[9], indent=1))

# =====================================================================
log("=== part 2: agent8 window variance mass location ===")


def window_run(k, N, H, tag):
    y = yk(k)
    G["y"] = y
    ns = list(range(N, N + H))
    assert (ns[-1] + 1) ** 2 - 1 <= XCAP
    with Pool(NPROC) as pool:
        rows = pool.map(per_sample, ns, chunksize=8)
    B = np.stack([r[12] for r in rows])
    E = np.array([r[4] for r in rows], float)
    dmax = int(rows[-1][2])
    Bc = B - B.mean(axis=0)
    Ec = E - E.mean()
    var = float(np.mean(Ec * Ec))
    contrib = np.mean(Bc * Ec[:, None], axis=0) / var       # sums to 1 exactly
    own = np.mean(Bc * Bc, axis=0) / var
    keep = [j for j in range(JMAX) if B[:, j].std() > 0 or abs(B[:, j]).max() > 0]
    rec = dict(tag=tag, k=k, N=N, H=H, y=y,
               X_first=(N + 1) ** 2 - 1, X_last=(N + H) ** 2 - 1,
               dmax_first=int(rows[0][2]), dmax_last=dmax,
               window_mean_E=float(E.mean()), window_var_E=var,
               sqrt_var_over_N2=float(math.sqrt(var) / N ** 2),
               abs_mean_E_over_N2=float(abs(E.mean()) / N ** 2),
               dyadic=[dict(j=j, d_lo=2 ** j, d_hi=min(2 ** (j + 1) - 1, dmax),
                            contrib_frac=float(contrib[j]), own_var_frac=float(own[j]))
                       for j in keep],
               contrib_sum=float(contrib.sum()))
    # cumulative tail fractions: variance carried by d > T
    def tail(T):
        j0 = int(math.floor(math.log2(max(T, 1)))) + 1
        return float(contrib[j0:].sum()), int(2 ** j0)
    for name, T in [("d>N", N), ("d>N^0.95", N ** 0.95), ("d>N^0.9", N ** 0.9),
                    ("d>N^0.8", N ** 0.8), ("d>dmax/2", dmax / 2),
                    ("d>dmax/4", dmax / 4), ("d>dmax/8", dmax / 8),
                    ("d>sqrt(x)/2", math.sqrt((N + 1) ** 2 - 1) / 2)]:
        f, thr = tail(T)
        rec[f"varfrac_{name}"] = f
        rec[f"thr_{name}"] = thr
    with open(os.path.join(OUT, f"a8_window_{tag}.csv"), "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["n", "X", "dmax", "E"] + [f"B{j}" for j in range(JMAX)])
        for r, e in zip(rows, E):
            w.writerow([r[0], r[1], r[2], f"{e:.6f}"] + [f"{v:.6g}" for v in r[12]])
    return rec


N_A = 30000
H_A = math.ceil(N_A ** (2.0 / 3.0))
lo9, hi9 = block_ns(9)
N_B = 14935 - math.ceil(14935 ** (2.0 / 3.0)) + 1        # top-of-block-8 window
H_B = math.ceil(14935 ** (2.0 / 3.0))
w8 = []
w8.append(window_run(9, N_A, H_A, "midblock9_N30000"))
log("window A: " + json.dumps({k: v for k, v in w8[-1].items() if k != "dyadic"}, indent=1))
w8.append(window_run(8, N_B, H_B, "topblock8_N%d" % N_B))
log("window B: " + json.dumps({k: v for k, v in w8[-1].items() if k != "dyadic"}, indent=1))
w8.append(window_run(9, lo9, H_A, "boundary9_N%d" % lo9))
log("window C: " + json.dumps({k: v for k, v in w8[-1].items() if k != "dyadic"}, indent=1))
summary["agent8_window_variance"] = w8

# ---- agent8 secondary: quadratic Weyl sums over prime pairs ----
log("=== part 3: agent8 secondary Weyl-sum check ===")
PRIMES_SMALL = None


def primes_upto(n):
    s = np.ones(n + 1, dtype=bool); s[:2] = False
    for p in range(2, math.isqrt(n) + 1):
        if s[p]: s[p * p:: p] = False
    return np.flatnonzero(s).astype(np.int64)


def weyl_check(N, H, tag, npairs=20000, seed=12345):
    ps = primes_upto(N)
    ps = ps[ps > N // 2]
    rng = np.random.default_rng(seed)
    idx = rng.integers(0, len(ps), size=(npairs, 2))
    idx = idx[idx[:, 0] != idx[:, 1]]
    r = np.arange(H, dtype=np.int64)
    Xr = (N + r + 1) ** 2 - 1
    out = []
    for i1, i2 in idx:
        d = int(ps[i1]); e = int(ps[i2])
        q = d * e
        h = e - d
        t = (Xr % q) * (h % q) % q
        S = np.exp(2j * math.pi * t / q).sum()
        out.append((d, e, q, abs(S)))
    A = np.array([o[3] for o in out])
    Q = np.array([o[2] for o in out], float)
    return dict(tag=tag, N=N, H=H, n_primes=int(len(ps)), n_pairs=len(out),
                mean_absS_over_H=float((A / H).mean()),
                median_absS_over_H=float(np.median(A / H)),
                p90_absS_over_H=float(np.quantile(A / H, 0.9)),
                max_absS_over_H=float((A / H).max()),
                frac_absS_gt_half_H=float(np.mean(A > H / 2)),
                mean_absS_over_sqrtH=float((A / math.sqrt(H)).mean()),
                mean_q=float(Q.mean()), H2_over_meanq=float(H * H / Q.mean()))


weyl = [weyl_check(lo9, H_A, "boundary9_N%d" % lo9),
        weyl_check(N_A, H_A, "midblock9_N30000"),
        weyl_check(22000, H_A, "midblock9_N22000")]
for w in weyl: log("weyl: " + json.dumps(w))
summary["agent8_secondary_weyl"] = weyl

summary["_meta"] = dict(
    script="kt2_a.py", wall_s=time.time() - t0,
    peak_rss_gb=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6,
    conventions="L_k=primorial(k), U_k=primorial(k+1), y=isqrt(U)+1, X_n=(n+1)^2-1,"
                " d<=x//(y+1), b=x//d, a=max(y,x//(d+1)), Delta=(pi(b)-pi(a))-(Li(b)-Li(a))",
    float_note="pi/M/Delta integer parts exact (int64); Li float64",
)
with open(os.path.join(OUT, "a_summary.json"), "w") as fh:
    json.dump(summary, fh, indent=1, default=float)
log("wrote a_summary.json")
log(f"done; wall={time.time()-t0:.1f}s peak RSS="
    f"{resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6:.2f} GB")
