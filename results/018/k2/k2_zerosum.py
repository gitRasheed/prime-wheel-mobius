#!/usr/bin/env python3
"""results/018 test K2 -- zero-sum reconstruction of the Abel sum, and THE
decisive inter-zero-cancellation (overshoot) measurement.  Cluster Z.

Standing conventions (record 016 / abel_main.py):
    blocks   L_k = primorial(k),  U_k = primorial(k+1)
    samples  x = X_n = (n+1)^2 - 1  in (L_k, U_k]
    y_k      = isqrt(U_k) + 1        (the block's y, NOT isqrt(x))
    K        = x // (y_k + 1)
    R(m)     = pi(m) - Li(m),  Li = framework array = int_2^m dt/log t
    S(x)     = sum_{d<=K} mu(d) R(floor(x/d))

Two zero-coordinate faces at rho = 1/2 + i*gamma:
    F_K(rho) = sum_{d<=K} mu(d) d^{-rho}                      (psi face)
    G_K(rho) = sum_{d<=K} mu(d) li((x/d)^rho), li(u^rho):=Ei(rho log u)
                                                              (pi-Li face)
  NOTE on branch: this code uses the conjugate-symmetric asymptotic branch
  Ei(z) ~ e^z/z * sum m!/z^m.  mpmath's ei(z) equals it + i*pi for Im z > 0;
  the difference cancels in every rho/rho-bar pair sum, so -2 Re G_K is
  branch independent.  The mpmath cross-check below adds i*pi*M(K) back.

Reconstruction (pi-Li face, the coordinate S actually lives in):
    S_T   = -2 Re sum_{0<gamma<=T} G_K(rho)                   (raw truncation)
    S_T^C = -2 Re sum_{0<gamma<=T} (1-gamma/T) G_K(rho)       (Riesz/Cesaro)
    target S_real = sum_{d<=K} mu(d)(pi(x/d) - Li(x/d))   [real argument]
                  = S(x) - sum_{d<=K} mu(d)(Li(x/d) - Li(floor(x/d)))
    predicted smooth offset  C_K = sum_{d<=K} mu(d) * C(x/d),
    C(u) = li(2) - log 2 + sum_{n>=2} (mu(n)/n) J(u^{1/n});  resid -> -C_K.

DECISIVE (absolute-value recombination over zeros vs the true |S|):
    overshoot_psi(x) = [2 sum_{0<gamma<=Tmax}|F_K(rho)| x^(1/2)/|rho|]/|S(x)|
    overshoot_li(x)  = [2 sum_{0<gamma<=Tmax}|G_K(rho)|]           /|S(x)|

Arithmetic model: exact int64 for mu/M/pi; float64 framework Li (builder's
declared budget 9.2e-4 abs); complex128 zero sums with np.longdouble phase
accumulation; mpmath dps=30 cross-checks.  Range x <= 1e9, K <= 12431,
5000 zeros (T_max = 5447.86; declared primary T = gamma_2000 = 2515.29).
"""
import os, sys, csv, json, math, time
import numpy as np
from multiprocessing import Pool

KT = os.path.expanduser("~/work/killtests")
OUT = os.path.expanduser("~/work/zeros")
NZ_DECLARED = 2000
EI_TERMS = 20
LI2 = 1.045163780117492785
TWO_PI_LD = np.longdouble("6.28318530717958647692528676655900577")
ENS_PER_DECADE = 48
t0 = time.time()


def log(*a):
    print(f"[{time.time()-t0:8.1f}s]", *a, flush=True)


PRIM = [1, 2, 6, 30, 210, 2310, 30030, 510510, 9699690, 223092870, 6469693230]

# exact endpoints recorded by record 016 (work/abel/abel_endpoints.csv)
ABEL_S = {999999: -6.071901902, 9998243: -206.846986938,
          99999999: -363.471579088, 999950883: 1359.190582607}


def block_of(x):
    for k in range(1, 10):
        if PRIM[k] < x <= PRIM[k + 1]:
            return k
    raise ValueError(x)


def pinned_sample(cap):
    n1 = math.isqrt(cap + 1)
    while n1 * n1 - 1 > cap:
        n1 -= 1
    return n1 * n1 - 1


def load_arrays():
    mu = np.load(f"{KT}/fw_mu.npy", mmap_mode="r")
    M = np.load(f"{KT}/fw_M_i32.npy", mmap_mode="r")
    pi = np.load(f"{KT}/fw_pi_i32.npy", mmap_mode="r")
    Li = np.load(f"{KT}/fw_Li_f64.npy", mmap_mode="r")
    # HARD ASSERTS (mandated in every script)
    assert M[6] == -1, f"M(6)={M[6]}"
    assert M[8] == -2, f"M(8)={M[8]}"
    assert M[30] == -3, f"M(30)={M[30]}"
    c = np.cumsum(np.asarray(mu[:31], dtype=np.int64))
    assert c[6] == -1 and c[8] == -2 and c[30] == -3, "mu-cumsum checkpoints"
    assert pi[30] == 10 and pi[10**9] == 50847534, "pi checkpoints"
    assert M[10**9] == -222 and M[10**8] == 1928, "Mertens checkpoints"
    return mu, M, pi, Li


def li_arr_real(t, Li):
    """Array-consistent Li(t) = int_2^t ds/log s for real t >= 3."""
    m = np.floor(t).astype(np.int64)
    fr = t - m
    return np.asarray(Li[m], dtype=np.float64) + fr / np.log(m + fr / 2.0)


def ei_prefactor(z, terms=EI_TERMS):
    """e^{-z} Ei(z) = (1/z) sum_{m<terms} m!/z^m  (asymptotic; |z| >> terms)."""
    inv = 1.0 / z
    s = np.ones_like(z)
    term = np.ones_like(z)
    for m in range(1, terms):
        term = term * (m * inv)
        s = s + term
    return s * inv


def cis_ld(theta_ld):
    """exp(i*theta) from a longdouble phase, returned as complex128."""
    th = theta_ld - TWO_PI_LD * np.rint(theta_ld / TWO_PI_LD)
    return np.cos(th).astype(np.float64) + 1j * np.sin(th).astype(np.float64)


def core(x, mu, M, pi, Li, gam_ld):
    """Everything at one x: S, S_real, F_K, G_K over all cached zeros."""
    k = block_of(x)
    y = math.isqrt(PRIM[k + 1]) + 1
    K = x // (y + 1)
    d = np.arange(1, K + 1, dtype=np.int64)
    mud = np.asarray(mu[1:K + 1], dtype=np.int64)
    nz = mud != 0
    d_nz = d[nz]
    mu_i = mud[nz]
    mu_f = mu_i.astype(np.float64)
    q = x // d_nz

    pi_part = int(np.sum(mu_i * np.asarray(pi[q], dtype=np.int64)))
    Li_q = np.asarray(Li[q], dtype=np.float64)
    Li_part = float(np.sum(mu_i.astype(np.longdouble) * Li_q.astype(np.longdouble)))
    S = pi_part - Li_part
    tr = x / d_nz.astype(np.float64)
    delta = li_arr_real(tr, Li) - Li_q
    floor_corr = float(np.sum(mu_i.astype(np.longdouble) * delta.astype(np.longdouble)))

    logd = np.log(d_nz.astype(np.longdouble))
    L_ld = np.log(np.longdouble(x)) - logd
    L = L_ld.astype(np.float64)
    amp = d_nz.astype(np.float64) ** -0.5
    root = np.exp(0.5 * L)

    NG = len(gam_ld)
    F = np.empty(NG, dtype=np.complex128)
    G = np.empty(NG, dtype=np.complex128)
    wF = (mu_f * amp)[None, :]
    for j0 in range(0, NG, 64):
        g_ld = gam_ld[j0:j0 + 64][:, None]
        gf = g_ld.astype(np.float64)
        F[j0:j0 + 64] = (cis_ld(-g_ld * logd[None, :]) * wF).sum(axis=1)
        z = (0.5 * L)[None, :] + 1j * (gf * L[None, :])
        ez = root[None, :] * cis_ld(g_ld * L_ld[None, :])
        G[j0:j0 + 64] = (ei_prefactor(z) * ez * mu_f[None, :]).sum(axis=1)

    # predicted smooth offset
    mu_small = np.asarray(mu[:64], dtype=np.int64)
    MK = int(M[K])
    off_pred = MK * (LI2 - math.log(2.0))
    for n in range(2, 64):
        if mu_small[n] == 0:
            continue
        v = np.exp(L / n)
        sel = v >= 2.0
        if not sel.any():
            break
        Jv = li_arr_real(v[sel], Li) + LI2 - math.log(2.0)
        off_pred += (mu_small[n] / n) * float(np.sum(mu_f[sel] * Jv))

    return dict(x=x, k=k, y=y, K=K, MK=MK, nnz=int(len(d_nz)), S=S,
                pi_part=pi_part, Li_part=Li_part, floor_corr=floor_corr,
                S_real=S - floor_corr, off_pred=off_pred,
                d_nz=d_nz, mu_i=mu_i, F=F, G=G, minz=math.hypot(0.5, float(gam_ld[0])) * float(L.min()))


def derive(c, gam, NG):
    """Cumulative reconstruction + absolute-recombination quantities."""
    x, S, G, F = c["x"], c["S"], c["G"], c["F"]
    rho_abs = np.hypot(0.5, gam)
    contrib = -2.0 * np.real(G)
    S_T = np.cumsum(contrib)
    resid = S_T - c["S_real"]
    S_T_ces = S_T - np.cumsum(gam * contrib) / gam
    resid_ces = S_T_ces - c["S_real"]
    cum_li = np.cumsum(2.0 * np.abs(G))
    cum_psi = np.cumsum(2.0 * np.abs(F) * math.sqrt(x) / rho_abs)
    return contrib, S_T, resid, S_T_ces, resid_ces, cum_li, cum_psi


def summarize(c, gam, NG):
    contrib, S_T, resid, S_T_ces, resid_ces, cum_li, cum_psi = derive(c, gam, NG)

    def at(n):
        i = n - 1
        return dict(n_zeros=n, T=float(gam[i]), S_T=float(S_T[i]),
                    S_T_cesaro=float(S_T_ces[i]), resid=float(resid[i]),
                    resid_cesaro=float(resid_ces[i]),
                    abs_li=float(cum_li[i]), abs_psi=float(cum_psi[i]),
                    overshoot_li=float(cum_li[i] / abs(c["S"])),
                    overshoot_psi=float(cum_psi[i] / abs(c["S"])),
                    abs_li_over_sqrtx=float(cum_li[i] / math.sqrt(c["x"])),
                    abs_psi_over_sqrtx=float(cum_psi[i] / math.sqrt(c["x"])))

    half = int(0.5 * NG)
    out = {k: c[k] for k in ("x", "k", "y", "K", "MK", "nnz", "S", "pi_part",
                             "Li_part", "floor_corr", "S_real", "off_pred", "minz")}
    out.update(absS_over_sqrtx=abs(c["S"]) / math.sqrt(c["x"]),
               sqrt_x=math.sqrt(c["x"]), log_x=math.log(c["x"]),
               mean_absF=float(np.mean(np.abs(c["F"]))),
               offset_fit_raw=float(np.mean(resid[half:])),
               offset_sd_raw=float(np.std(resid[half:])),
               offset_fit_cesaro=float(np.mean(resid_ces[half:])),
               offset_sd_cesaro=float(np.std(resid_ces[half:])),
               at=[at(n) for n in (100, 500, 1000, NZ_DECLARED, NG) if n <= NG])
    return out, (contrib, S_T, resid, S_T_ces, resid_ces, cum_li, cum_psi)


# ------------------------------------------------------------------ ensemble
_G = {}


def _init():
    _G["arr"] = load_arrays()
    _G["gam"] = np.load(os.path.join(OUT, "zeros_gamma_ld.npy"))


def _job(x):
    mu, M, pi, Li = _G["arr"]
    gam_ld = _G["gam"]
    c = core(x, mu, M, pi, Li, gam_ld)
    gam = gam_ld.astype(np.float64)
    s, _ = summarize(c, gam, len(gam))
    return s


def main():
    mu, M, pi, Li = load_arrays()
    log("arrays loaded; HARD ASSERTS M(6)=-1 M(8)=-2 M(30)=-3 OK")
    with open(os.path.join(OUT, "zeros_gamma_dps30.txt")) as f:
        gstr = [ln.strip() for ln in f if ln.strip()]
    gam_ld = np.array([np.longdouble(s) for s in gstr])
    np.save(os.path.join(OUT, "zeros_gamma_ld.npy"), gam_ld)
    gam = gam_ld.astype(np.float64)
    NG = len(gam_ld)
    log(f"{NG} zeros, gamma_1={gstr[0]}, T_max={gstr[-1]}")

    from mpmath import mp, mpc, mpf, ei
    mp.dps = 30
    results = []
    for cap in (10**6, 10**7, 10**8, 10**9):
        x = pinned_sample(cap)
        c = core(x, mu, M, pi, Li, gam_ld)
        log(f"=== x={x} k={c['k']} y={c['y']} K={c['K']} nnz={c['nnz']} "
            f"S={c['S']:.6f} |S|/sqrt(x)={abs(c['S'])/math.sqrt(x):.5f} minz={c['minz']:.0f}")
        # abel cross-check (record 016 endpoints)
        assert abs(c["S"] - ABEL_S[x]) < 1e-6, \
            f"abel mismatch at x={x}: {c['S']} vs {ABEL_S[x]}"
        s, arrs = summarize(c, gam, NG)
        s["abel_S_recorded"] = ABEL_S[x]
        s["abel_S_diff"] = c["S"] - ABEL_S[x]

        # ---- mpmath cross-check (F exact; G with the +i*pi*M(K) branch shift)
        dl = [int(v) for v in c["d_nz"]]
        ml = [int(v) for v in c["mu_i"]]
        idxF = np.unique(np.linspace(0, NG - 1, 20).astype(int))
        idxG = np.unique(np.linspace(0, NG - 1, 8).astype(int))
        eF = eG = 0.0
        for i in idxF:
            rho = mpc(mpf(1) / 2, mp.mpf(gstr[i]))
            fv = complex(mp.fsum(m * mp.power(dd, -rho) for dd, m in zip(dl, ml)))
            eF = max(eF, abs(fv - c["F"][i]) / abs(fv))
        lx = mp.log(mp.mpf(x))
        for i in idxG:
            rho = mpc(mpf(1) / 2, mp.mpf(gstr[i]))
            gv = complex(mp.fsum(m * ei(rho * (lx - mp.log(dd))) for dd, m in zip(dl, ml)))
            mine = c["G"][i] + 1j * math.pi * c["MK"]
            eG = max(eG, abs(gv - mine) / abs(gv))
        s["mpmath_check"] = dict(nF=int(len(idxF)), nG=int(len(idxG)),
                                 worst_rel_err_F=eF, worst_rel_err_G=eG,
                                 digits_F=-math.log10(eF) if eF else 99.0,
                                 digits_G=-math.log10(eG) if eG else 99.0)
        log(f"    mpmath: F {eF:.2e} ({-math.log10(eF):.1f} dig)  "
            f"G {eG:.2e} ({-math.log10(eG) if eG else 99:.1f} dig)")

        # ---- per-x CSV
        contrib, S_T, resid, S_T_ces, resid_ces, cum_li, cum_psi = arrs
        csvp = os.path.join(OUT, f"k2_zeros_x{x}.csv")
        with open(csvp, "w", newline="") as fh:
            w = csv.writer(fh)
            w.writerow(["j", "gamma", "absF_K", "argF_K", "absG_K", "argG_K",
                        "contrib", "S_T", "resid_T", "S_T_cesaro",
                        "resid_cesaro", "cum_abs_li", "cum_abs_psi"])
            for j in range(NG):
                w.writerow([j + 1, gstr[j], f"{abs(c['F'][j]):.12e}",
                            f"{np.angle(c['F'][j]):.9f}", f"{abs(c['G'][j]):.12e}",
                            f"{np.angle(c['G'][j]):.9f}", f"{contrib[j]:.9e}",
                            f"{S_T[j]:.9e}", f"{resid[j]:.9e}",
                            f"{S_T_ces[j]:.9e}", f"{resid_ces[j]:.9e}",
                            f"{cum_li[j]:.9e}", f"{cum_psi[j]:.9e}"])
        s["csv"] = csvp
        a = s["at"][-1]
        log(f"    OVERSHOOT@Tmax psi={a['overshoot_psi']:.4g} li={a['overshoot_li']:.4g}"
            f"  resid/|S| raw={resid[-1]/abs(c['S']):+.3f} ces={resid_ces[-1]/abs(c['S']):+.3f}"
            f"  off_pred={c['off_pred']:.2f} off_fit_ces={s['offset_fit_cesaro']:.2f}"
            f" (sd {s['offset_sd_cesaro']:.2f})")
        results.append(s)

    # ---------------- robustness ensemble: 48 square samples per decade
    log(f"ensemble: {ENS_PER_DECADE} square samples per decade, 14 procs")
    ens_x = {}
    for cap in (10**6, 10**7, 10**8, 10**9):
        n1 = math.isqrt(cap + 1)
        while n1 * n1 - 1 > cap:
            n1 -= 1
        ens_x[cap] = [m * m - 1 for m in range(n1 - ENS_PER_DECADE + 1, n1 + 1)]
    flat = [(cap, x) for cap in ens_x for x in ens_x[cap]]
    with Pool(14, initializer=_init) as pool:
        rows = pool.map(_job, [x for _, x in flat], chunksize=1)
    ens = {}
    for (cap, x), r in zip(flat, rows):
        ens.setdefault(cap, []).append(r)
    log("ensemble done")

    ens_csv = os.path.join(OUT, "k2_ensemble.csv")
    with open(ens_csv, "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["cap", "x", "k", "y", "K", "MK", "S", "absS_over_sqrtx",
                    "S_real", "resid_cesaro_Tmax", "off_pred",
                    "abs_li_Tmax", "abs_psi_Tmax", "overshoot_li_Tmax",
                    "overshoot_psi_Tmax", "overshoot_li_T2000",
                    "overshoot_psi_T2000", "mean_absF"])
        for cap in sorted(ens):
            for r in ens[cap]:
                aT = r["at"][-1]
                a2 = next(a for a in r["at"] if a["n_zeros"] == NZ_DECLARED)
                w.writerow([cap, r["x"], r["k"], r["y"], r["K"], r["MK"],
                            f"{r['S']:.9f}", f"{r['absS_over_sqrtx']:.9f}",
                            f"{r['S_real']:.9f}", f"{aT['resid_cesaro']:.6f}",
                            f"{r['off_pred']:.6f}", f"{aT['abs_li']:.6e}",
                            f"{aT['abs_psi']:.6e}", f"{aT['overshoot_li']:.6f}",
                            f"{aT['overshoot_psi']:.6f}", f"{a2['overshoot_li']:.6f}",
                            f"{a2['overshoot_psi']:.6f}", f"{r['mean_absF']:.6f}"])

    def pick(r, key, n):
        return next(a[key] for a in r["at"] if a["n_zeros"] == n)

    ens_stats = {}
    for cap in sorted(ens):
        rs = ens[cap]
        st = dict(cap=cap, n=len(rs),
                  x_min=min(r["x"] for r in rs), x_max=max(r["x"] for r in rs),
                  rms_absS_over_sqrtx=float(np.sqrt(np.mean(
                      [r["absS_over_sqrtx"] ** 2 for r in rs]))),
                  median_absS=float(np.median([abs(r["S"]) for r in rs])),
                  rms_S=float(np.sqrt(np.mean([r["S"] ** 2 for r in rs]))))
        for key, n, tag in (("overshoot_li", NG, "li_Tmax"),
                            ("overshoot_psi", NG, "psi_Tmax"),
                            ("overshoot_li", NZ_DECLARED, "li_T2000"),
                            ("overshoot_psi", NZ_DECLARED, "psi_T2000")):
            v = np.array([pick(r, key, n) for r in rs])
            st[f"median_overshoot_{tag}"] = float(np.median(v))
            st[f"q25_overshoot_{tag}"] = float(np.percentile(v, 25))
            st[f"q75_overshoot_{tag}"] = float(np.percentile(v, 75))
        for key, n, tag in (("abs_li", NG, "li_Tmax"), ("abs_psi", NG, "psi_Tmax"),
                            ("abs_li", NZ_DECLARED, "li_T2000"),
                            ("abs_psi", NZ_DECLARED, "psi_T2000")):
            st[f"median_absrecomb_over_sqrtx_{tag}"] = float(np.median(
                [pick(r, key, n) / r["sqrt_x"] for r in rs]))
        # rms-normalised overshoot: absolute recombination vs the block-typical |S|
        for tag, n, key in (("li_Tmax", NG, "abs_li"), ("psi_Tmax", NG, "abs_psi"),
                            ("li_T2000", NZ_DECLARED, "abs_li"),
                            ("psi_T2000", NZ_DECLARED, "abs_psi")):
            num = float(np.median([pick(r, key, n) for r in rs]))
            st[f"overshoot_vs_rmsS_{tag}"] = num / st["rms_S"]
        st["mean_absF"] = float(np.median([r["mean_absF"] for r in rs]))
        ens_stats[str(cap)] = st

    def fit_pow(xs, ys):
        lx = np.log(np.asarray(xs, float))
        ly = np.log(np.abs(np.asarray(ys, float)))
        A = np.vstack([lx, np.ones_like(lx)]).T
        sol, *_ = np.linalg.lstsq(A, ly, rcond=None)
        pred = A @ sol
        den = float(np.sum((ly - ly.mean()) ** 2))
        return dict(exponent=float(sol[0]), prefactor=float(np.exp(sol[1])),
                    r2=1.0 - float(np.sum((ly - pred) ** 2)) / den if den > 0 else 1.0,
                    x=list(map(float, xs)), values=list(map(float, ys)))

    caps = sorted(ens)
    xmid = [float(np.median([r["x"] for r in ens[c]])) for c in caps]
    fits = {}
    for tag in ("li_Tmax", "psi_Tmax", "li_T2000", "psi_T2000"):
        fits[f"median_overshoot_{tag}"] = fit_pow(
            xmid, [ens_stats[str(c)][f"median_overshoot_{tag}"] for c in caps])
        fits[f"overshoot_vs_rmsS_{tag}"] = fit_pow(
            xmid, [ens_stats[str(c)][f"overshoot_vs_rmsS_{tag}"] for c in caps])
        fits[f"absrecomb_over_sqrtx_{tag}"] = fit_pow(
            xmid, [ens_stats[str(c)][f"median_absrecomb_over_sqrtx_{tag}"] for c in caps])
    fits["rms_absS_over_sqrtx"] = fit_pow(
        xmid, [ens_stats[str(c)]["rms_absS_over_sqrtx"] for c in caps])
    fits["mean_absF_K"] = fit_pow(xmid, [ens_stats[str(c)]["mean_absF"] for c in caps])
    # pinned-sample (declared) fits
    for key, n, tag in (("overshoot_psi", NG, "psi_Tmax"), ("overshoot_li", NG, "li_Tmax"),
                        ("overshoot_psi", NZ_DECLARED, "psi_T2000"),
                        ("overshoot_li", NZ_DECLARED, "li_T2000")):
        fits[f"pinned_overshoot_{tag}"] = fit_pow(
            [r["x"] for r in results], [pick(r, key, n) for r in results])

    summary = dict(
        record="results/018 K2 (zero-sum reconstruction; settles cluster Z)",
        generated=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        conventions=dict(
            blocks="L_k=primorial(k), U_k=primorial(k+1)",
            samples="x = largest (n+1)^2-1 <= cap (pinned); ensemble = 48 consecutive square samples below cap",
            y="y_k = isqrt(U_k)+1", K="K = x//(y_k+1)",
            R="R(m)=pi(m)-Li(m); Li = int_2^m ds/log s (framework array)",
            S="S(x)=sum_{d<=K} mu(d) R(floor(x/d))",
            F="F_K(rho)=sum_{d<=K} mu(d) d^{-rho}",
            G="G_K(rho)=sum_{d<=K} mu(d) li((x/d)^rho), li(u^rho)=Ei(rho log u), conjugate-symmetric branch",
            S_T="S_T = -2 Re sum_{0<gamma<=T} G_K(rho); Cesaro = Riesz (1-gamma/T) weight",
            overshoot_psi="2 sum_{0<gamma<=T}|F_K(rho)| x^(1/2)/|rho| / |S(x)|",
            overshoot_li="2 sum_{0<gamma<=T}|G_K(rho)| / |S(x)|"),
        precision=dict(
            mu_M_pi="exact integers (int64 accumulation)",
            Li="float64 framework array; builder's declared budget 9.2e-4 abs",
            zeros="mpmath.zetazero at mp.dps=30 (>=25 significant digits), first 5000",
            zero_sums="complex128 with np.longdouble phase accumulation (phase error < 1e-14 rad)",
            Ei=f"asymptotic series, {EI_TERMS} terms, |z| >= 110 => truncation < 1e-20 relative",
            cross_checks="mpmath dps=30 at 20 zeros (F) / 8 zeros (G) per x; S vs record 016 abel_endpoints.csv"),
        range=dict(x_max=10**9, K_max=12431, n_zeros=NG, T_max=float(gam[-1]),
                   T_declared=float(gam[NZ_DECLARED - 1])),
        per_x_pinned=results, ensemble_stats=ens_stats, fits=fits,
        ensemble_csv=ens_csv)
    with open(os.path.join(OUT, "k2_summary.json"), "w") as f:
        json.dump(summary, f, indent=2, default=float)
    log("wrote k2_summary.json")
    print(json.dumps({k: fits[k] for k in sorted(fits)}, indent=2, default=float))
    print(json.dumps(ens_stats, indent=2, default=float))


if __name__ == "__main__":
    main()
