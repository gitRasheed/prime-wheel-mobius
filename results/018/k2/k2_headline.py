#!/usr/bin/env python3
"""K2 headline: the overshoot table under three denominators and the growth fits.

Denominators for the decisive ratio (numerator = absolute-value recombination
over zeros at fixed height T):
  (a) |S(x)| at the declared pinned square sample          [literal, noisy]
  (b) median |S| over the block containing x  (record 016, exhaustive)
  (c) rms   |S| over the block containing x  (record 016, exhaustive)
Hard asserts M(6)=-1, M(8)=-2, M(30)=-3.
"""
import os, json, math
import numpy as np

OUT = os.path.expanduser("~/work/zeros")
KT = os.path.expanduser("~/work/killtests")
M = np.load(f"{KT}/fw_M_i32.npy", mmap_mode="r")
assert M[6] == -1 and M[8] == -2 and M[30] == -3, "HARD ASSERT failed"

S = json.load(open(f"{OUT}/k2_summary.json"))
TP = json.load(open(f"{OUT}/k2_tprofile.json"))
AB = json.load(open(os.path.expanduser("~/work/abel/abel_report.json")))["per_block"]

NZ = S["range"]["n_zeros"]


def fit(xs, ys):
    lx, ly = np.log(np.asarray(xs, float)), np.log(np.abs(np.asarray(ys, float)))
    A = np.vstack([lx, np.ones_like(lx)]).T
    sol, *_ = np.linalg.lstsq(A, ly, rcond=None)
    r = ly - A @ sol
    den = float(np.sum((ly - ly.mean()) ** 2))
    return dict(exponent=float(sol[0]), prefactor=float(np.exp(sol[1])),
                r2=1.0 - float(np.sum(r ** 2)) / den if den > 0 else 1.0)


rows = []
for r in S["per_x_pinned"]:
    x, k, sx = r["x"], str(r["k"]), r["sqrt_x"]
    blk = AB[k]["absS_over_sqrtx"]
    med_S = blk["median"] * sx
    rms_S = blk["rms"] * sx
    for tag, n in (("T2000", 2000), ("Tmax", NZ)):
        a = next(q for q in r["at"] if q["n_zeros"] == n)
        rows.append(dict(
            x=x, block=k, K=r["K"], T_tag=tag, T=a["T"], n_zeros=n,
            absS=abs(r["S"]), absS_over_sqrtx=r["absS_over_sqrtx"],
            block_median_absS=med_S, block_rms_absS=rms_S,
            block_median_absS_over_sqrtx=blk["median"],
            block_rms_absS_over_sqrtx=blk["rms"],
            abs_li=a["abs_li"], abs_psi=a["abs_psi"],
            abs_li_over_sqrtx=a["abs_li"] / sx, abs_psi_over_sqrtx=a["abs_psi"] / sx,
            OS_li_pinned=a["abs_li"] / abs(r["S"]),
            OS_psi_pinned=a["abs_psi"] / abs(r["S"]),
            OS_li_blockmed=a["abs_li"] / med_S, OS_psi_blockmed=a["abs_psi"] / med_S,
            OS_li_blockrms=a["abs_li"] / rms_S, OS_psi_blockrms=a["abs_psi"] / rms_S))

fits = {}
for tag in ("T2000", "Tmax"):
    sel = [r for r in rows if r["T_tag"] == tag]
    xs = [r["x"] for r in sel]
    for key in ("OS_li_pinned", "OS_psi_pinned", "OS_li_blockmed", "OS_psi_blockmed",
                "OS_li_blockrms", "OS_psi_blockrms",
                "abs_li_over_sqrtx", "abs_psi_over_sqrtx"):
        fits[f"{key}_{tag}"] = dict(values=[r[key] for r in sel], x=xs, **fit(xs, [r[key] for r in sel]))

# extrapolated (honest truncation heights) absolute bound / |S|
extra = []
for r in S["per_x_pinned"]:
    x, k, sx = r["x"], str(r["k"]), r["sqrt_x"]
    d = TP["per_x"][str(x)]
    blk = AB[k]["absS_over_sqrtx"]
    for name in ("T_sqrtx_log3x", "T_x"):
        extra.append(dict(x=x, height=name, Sigma=d[f"Sigma_{name}"],
                          abs_li_over_sqrtx=d[f"extrap_abs_li_over_sqrtx_{name}"],
                          abs_psi_over_sqrtx=d[f"extrap_abs_psi_over_sqrtx_{name}"],
                          OS_li_blockmed=d[f"extrap_abs_li_over_sqrtx_{name}"] / blk["median"],
                          OS_psi_blockmed=d[f"extrap_abs_psi_over_sqrtx_{name}"] / blk["median"]))
for name in ("T_sqrtx_log3x", "T_x"):
    sel = [e for e in extra if e["height"] == name]
    for key in ("abs_li_over_sqrtx", "OS_li_blockmed", "OS_psi_blockmed"):
        fits[f"extrap_{key}_{name}"] = dict(
            values=[e[key] for e in sel], x=[e["x"] for e in sel],
            **fit([e["x"] for e in sel], [e[key] for e in sel]))

# how much of the growth is explained purely by log x?
lg = [math.log(r["x"]) for r in S["per_x_pinned"]]
fits["log_x_reference"] = dict(values=lg, x=[r["x"] for r in S["per_x_pinned"]],
                               **fit([r["x"] for r in S["per_x_pinned"]], lg))
fits["log_x_sq_reference"] = dict(values=[v ** 2 for v in lg],
                                  x=[r["x"] for r in S["per_x_pinned"]],
                                  **fit([r["x"] for r in S["per_x_pinned"]], [v ** 2 for v in lg]))

out = dict(headline_rows=rows, extrapolated=extra, fits=fits,
           block_absS_scale={k: AB[k]["absS_over_sqrtx"] for k in AB},
           note=("numerator = absolute-value recombination over zeros at height T; "
                 "abs_li = 2*sum_{0<g<=T}|G_K(rho)| (pi-Li coordinate, the one S lives in); "
                 "abs_psi = 2*sum|F_K(rho)|x^{1/2}/|rho| (declared psi-coordinate form)"))
json.dump(out, open(f"{OUT}/k2_headline.json", "w"), indent=2, default=float)

hdr = f"{'x':>11} {'blk':>3} {'K':>6} {'T':>7} {'|S|':>9} {'medS':>9} {'A_li/vx':>8} {'A_psi/vx':>9} {'OSli_pin':>9} {'OSpsi_pin':>10} {'OSli_med':>9} {'OSpsi_med':>10}"
print(hdr)
for r in rows:
    print(f"{r['x']:>11} {r['block']:>3} {r['K']:>6} {r['T']:>7.0f} {r['absS']:>9.1f} "
          f"{r['block_median_absS']:>9.1f} {r['abs_li_over_sqrtx']:>8.3f} "
          f"{r['abs_psi_over_sqrtx']:>9.2f} {r['OS_li_pinned']:>9.1f} {r['OS_psi_pinned']:>10.1f} "
          f"{r['OS_li_blockmed']:>9.2f} {r['OS_psi_blockmed']:>10.1f}")
print("\nEXTRAPOLATED to honest truncation heights:")
for e in extra:
    print(f"  x={e['x']:>11} {e['height']:<15} Sigma={e['Sigma']:6.2f}  "
          f"A_li/sqrt(x)={e['abs_li_over_sqrtx']:6.2f}  OS_li(block median)={e['OS_li_blockmed']:7.1f}"
          f"  OS_psi={e['OS_psi_blockmed']:8.1f}")
print("\nFITS (exponent of x):")
for k in sorted(fits):
    f = fits[k]
    print(f"  {k:42s} exp={f['exponent']:+.4f} r2={f['r2']:.3f}  " +
          ", ".join(f"{v:.4g}" for v in f["values"]))
