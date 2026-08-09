#!/usr/bin/env python3
"""K2 follow-up: T-dependence of the absolute-value recombination over zeros,
and the extrapolation to the truncation heights a valid explicit formula needs.

Model tested:  2 sum_{0<gamma<=T} |G_K(rho)|  =  c_li(x) * sqrt(x) * Sigma(T),
               2 sum_{0<gamma<=T} |F_K(rho)| sqrt(x)/|rho| = c_psi(x)*sqrt(x)*Sigma(T),
with Sigma(T) = sum_{0<gamma<=T} 2/|rho|  (exactly known: ~ log^2(T/2pi)/(2pi)).
If c is flat in T the extrapolation to T = sqrt(x)log^3 x and T = x is principled.
Hard asserts M(6)=-1, M(8)=-2, M(30)=-3 retained.
"""
import os, csv, json, math
import numpy as np

OUT = os.path.expanduser("~/work/zeros")
KT = os.path.expanduser("~/work/killtests")

M = np.load(f"{KT}/fw_M_i32.npy", mmap_mode="r")
assert M[6] == -1 and M[8] == -2 and M[30] == -3, "HARD ASSERT failed"

gam = np.array([float(s) for s in open(f"{OUT}/zeros_gamma_dps30.txt")])
rho = np.hypot(0.5, gam)
Sig = np.cumsum(2.0 / rho)                       # sum over +-gamma of 1/|rho|

XS = [999999, 9998243, 99999999, 999950883]
rep = {"sigma_T": {"T_2515": float(Sig[1999]), "T_5448": float(Sig[-1]),
                   "riemann_vonmangoldt_log2_over_2pi_at_Tmax":
                       math.log(gam[-1] / (2 * math.pi)) ** 2 / (2 * math.pi)},
       "per_x": {}}

for x in XS:
    rows = list(csv.DictReader(open(f"{OUT}/k2_zeros_x{x}.csv")))
    cum_li = np.array([float(r["cum_abs_li"]) for r in rows])
    cum_psi = np.array([float(r["cum_abs_psi"]) for r in rows])
    resid_c = np.array([float(r["resid_cesaro"]) for r in rows])
    resid_r = np.array([float(r["resid_T"]) for r in rows])
    contrib = np.array([float(r["contrib"]) for r in rows])
    sx = math.sqrt(x)
    c_li = cum_li / (sx * Sig)
    c_psi = cum_psi / (sx * Sig)
    idx = [99, 499, 999, 1999, 2999, 3999, 4999]
    d = dict(
        x=x, sqrt_x=sx, log_x=math.log(x),
        c_li_at=[[float(gam[i]), float(c_li[i])] for i in idx],
        c_psi_at=[[float(gam[i]), float(c_psi[i])] for i in idx],
        c_li_last_decade_mean=float(np.mean(c_li[2500:])),
        c_psi_last_decade_mean=float(np.mean(c_psi[2500:])),
        signed_over_absolute=float(abs(np.sum(contrib)) / np.sum(np.abs(contrib))),
        resid_cesaro_at=[[float(gam[i]), float(resid_c[i])] for i in idx],
        resid_raw_at=[[float(gam[i]), float(resid_r[i])] for i in idx],
    )
    # extrapolation of the absolute bound to the heights a valid formula needs
    lx = math.log(x)
    for name, T in (("T_sqrtx_log3x", math.sqrt(x) * lx ** 3), ("T_x", float(x))):
        S_T = math.log(T / (2 * math.pi)) ** 2 / (2 * math.pi)
        d[f"extrap_abs_li_over_sqrtx_{name}"] = d["c_li_last_decade_mean"] * S_T
        d[f"extrap_abs_psi_over_sqrtx_{name}"] = d["c_psi_last_decade_mean"] * S_T
        d[f"Sigma_{name}"] = S_T
    rep["per_x"][str(x)] = d

# 016 block-level |S| scale (authoritative denominators)
ab = json.load(open(os.path.expanduser("~/work/abel/abel_report.json")))


def dig(o, key, out):
    if isinstance(o, dict):
        for k, v in o.items():
            if k == key and isinstance(v, (int, float)):
                out.append(v)
            else:
                dig(v, key, out)
    elif isinstance(o, list):
        for v in o:
            dig(v, key, out)


blocks = {}
for k, v in (ab.get("blocks") or ab.get("per_block") or {}).items() \
        if isinstance(ab.get("blocks") or ab.get("per_block"), dict) else []:
    blocks[k] = v
rep["abel_report_keys"] = list(ab.keys())
rep["abel_absS_over_sqrtx"] = {}
for k in ("6", "7", "8", "9", 6, 7, 8, 9):
    node = None
    for cand in ("blocks", "per_block", "by_block", "block"):
        if isinstance(ab.get(cand), dict) and str(k) in ab[cand]:
            node = ab[cand][str(k)]
    if node:
        got = []
        dig(node, "rms_absS_over_sqrtx", got)
        if not got:
            dig(node, "absS_over_sqrtx", got)
        if got:
            rep["abel_absS_over_sqrtx"][str(k)] = got[:4]

json.dump(rep, open(f"{OUT}/k2_tprofile.json", "w"), indent=2, default=float)

for x in XS:
    d = rep["per_x"][str(x)]
    print(f"x={x}  sqrt(x)={d['sqrt_x']:.1f}  log x={d['log_x']:.2f}")
    print("   c_li(T) :", "  ".join(f"{T:7.0f}:{c:.4f}" for T, c in d["c_li_at"]))
    print("   c_psi(T):", "  ".join(f"{T:7.0f}:{c:.3f}" for T, c in d["c_psi_at"]))
    print(f"   signed/absolute over zeros = {d['signed_over_absolute']:.5f}")
    print(f"   extrap abs_li/sqrt(x): T=sqrt(x)log^3x -> "
          f"{d['extrap_abs_li_over_sqrtx_T_sqrtx_log3x']:.1f}   T=x -> "
          f"{d['extrap_abs_li_over_sqrtx_T_x']:.1f}")
    print("   resid_cesaro:", "  ".join(f"{T:7.0f}:{r:+.1f}" for T, r in d["resid_cesaro_at"]))
print("\nSigma(T): T=2515 ->", rep["sigma_T"]["T_2515"], " T=5448 ->", rep["sigma_T"]["T_5448"])
print("abel_report top-level keys:", rep["abel_report_keys"][:20])
print("abel |S|/sqrt(x) by block:", json.dumps(rep["abel_absS_over_sqrtx"]))
