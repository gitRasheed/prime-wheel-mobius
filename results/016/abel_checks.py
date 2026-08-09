#!/usr/bin/env python3
"""record 016 support checks.

(A) Li float64 error budget: the framework array fw_Li_f64 is a per-unit-interval
    2-point Gauss-Legendre cumulative sum of 1/log t anchored at 2.  Reference:
    li_2(x) = int_2^x dt/log t = int_{log 2}^{log x} e^u/u du, evaluated in
    np.longdouble (80-bit) by composite 10-point Gauss-Legendre on a fine
    u-partition.  Reports max |array - reference| over log-spaced checkpoints.

(B) Convention cross-check: recompute E(y,x) = sum_{d<=K} M(d) Delta_d at every
    sample of record 006's t7_agent6.csv (blocks k=6,7,8) and compare.
"""
import numpy as np, math, json, os, csv

FW = os.path.expanduser("~/work/killtests")
OUT = os.path.expanduser("~/work/abel")
os.makedirs(OUT, exist_ok=True)
PRIM = [1, 2, 6, 30, 210, 2310, 30030, 510510, 9699690, 223092870, 6469693230]

nodes, weights = np.polynomial.legendre.leggauss(10)
nodes = nodes.astype(np.longdouble)
weights = weights.astype(np.longdouble)

def li2_ref(x, panels_per_unit_u=400):
    """int_2^x dt/log t in longdouble via u = log t."""
    u0 = np.longdouble(math.log(2.0))
    u1 = np.longdouble(np.log(np.longdouble(x)))
    npan = max(64, int(float(u1 - u0) * panels_per_unit_u))
    edges = u0 + (u1 - u0) * (np.arange(npan + 1, dtype=np.longdouble) / npan)
    lo, hi = edges[:-1], edges[1:]
    mid = 0.5 * (lo + hi)
    half = 0.5 * (hi - lo)
    u = mid[:, None] + half[:, None] * nodes[None, :]
    f = np.exp(u) / u
    return float((half[:, None] * weights[None, :] * f).sum())

def main():
    Li = np.load(os.path.join(FW, "fw_Li_f64.npy"), mmap_mode="r")
    pi = np.load(os.path.join(FW, "fw_pi_i32.npy"), mmap_mode="r")
    M = np.load(os.path.join(FW, "fw_M_i32.npy"), mmap_mode="r")

    # sanity of the reference itself: li(10^9) - li(2) ~ 50849234.96 - 1.04516378
    ref9 = li2_ref(10 ** 9)
    out = dict(ref_li2_1e9=ref9, known_li_1e9_minus_li_2=50849234.9601 - 1.0451637801)

    pts = sorted(set(
        [int(round(v)) for v in np.exp(np.linspace(math.log(10), math.log(1e9), 60))]
        + [10 ** j for j in range(1, 10)]
        + [math.isqrt(PRIM[k + 1]) + 1 for k in (6, 7, 8, 9)]
        + [PRIM[k] for k in range(3, 10)]))
    rows = []
    for t in pts:
        if t < 3 or t > 10 ** 9:
            continue
        r = li2_ref(t)
        a = float(Li[t])
        rows.append((t, a, r, a - r, (a - r) / max(abs(r), 1e-300)))
    with open(os.path.join(OUT, "li_error.csv"), "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["t", "Li_array", "Li_reference_longdouble", "abs_err", "rel_err"])
        for t, a, r, e, re_ in rows:
            w.writerow([t, f"{a:.9f}", f"{r:.9f}", f"{e:.6e}", f"{re_:.3e}"])
    errs = np.array([abs(r[3]) for r in rows])
    out["li_max_abs_error"] = float(errs.max())
    out["li_max_abs_error_at_t"] = int(rows[int(np.argmax(errs))][0])
    out["li_max_rel_error"] = float(max(abs(r[4]) for r in rows))
    out["li_n_checkpoints"] = len(rows)
    out["li_abs_error_at_1e9"] = float(Li[10 ** 9] - ref9)

    # (B) convention cross-check against record 006 t7_agent6.csv
    p = os.path.join(FW, "t7_agent6.csv")
    diffs = []
    if os.path.exists(p):
        with open(p) as fh:
            for row in csv.DictReader(fh):
                k = int(row["k"])
                if k not in (6, 7, 8):
                    continue
                n = int(row["n"]); x = (n + 1) ** 2 - 1
                assert x == int(row["X"]), (x, row["X"])
                y = math.isqrt(PRIM[k + 1]) + 1
                K = x // (y + 1)
                d = np.arange(1, K + 1, dtype=np.int64)
                b = x // d
                Rb = pi[b].astype(np.float64) - Li[b]
                Ra = np.empty(K); Ra[:K - 1] = Rb[1:]
                Ra[K - 1] = float(pi[y]) - float(Li[y])
                E = float(np.dot(M[d].astype(np.float64), Rb - Ra))
                diffs.append(abs(E - float(row["E"])))
    out["t7_crosscheck_rows"] = len(diffs)
    out["t7_crosscheck_max_abs_diff_E"] = float(max(diffs)) if diffs else None

    with open(os.path.join(OUT, "abel_checks.json"), "w") as fh:
        json.dump(out, fh, indent=1)
    print(json.dumps(out, indent=1))

if __name__ == "__main__":
    main()
