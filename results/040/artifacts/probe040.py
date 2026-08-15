#!/usr/bin/env python3
"""Record 040: independent replication of the three-slot transition-matrix
experiment. Uniformity check AND convergence rate. Numerics falsify, never
prove."""
import numpy as np
import json
import sys

N = int(sys.argv[1]) if len(sys.argv) > 1 else 10**8
BLOCK = 8 * 10**6

def primes_upto(n):
    s = np.ones(n + 1, dtype=bool)
    s[:2] = False
    for p in range(2, int(n**0.5) + 1):
        if s[p]:
            s[p*p::p] = False
    return np.nonzero(s)[0]

SMALL = primes_upto(int(N**0.5) + 1)
mu_all = np.zeros(N + 1, dtype=np.int8)

for lo in range(1, N + 1, BLOCK):
    hi = min(lo + BLOCK, N + 1)
    n = hi - lo
    mu = np.ones(n, dtype=np.int8)
    rem = np.arange(lo, hi, dtype=np.int64)
    for p in SMALL:
        p = int(p)
        start = ((lo + p - 1) // p) * p - lo
        if start >= n:
            continue
        mu[start::p] *= -1
        p2 = p * p
        start2 = ((lo + p2 - 1) // p2) * p2 - lo
        if start2 < n:
            mu[start2::p2] = 0
        idx = np.arange(start, n, p, dtype=np.int64)
        r = rem[idx]
        while True:
            m = r % p == 0
            if not m.any():
                break
            r[m] //= p
        rem[idx] = r
    mu[rem > 1] *= -1
    mu_all[lo:hi] = mu
print("sieve done", flush=True)

K_max = (N - 3) // 4 + 1  # cells k=0..K_max-1 need 4k+3 <= N
A = mu_all[1::4][:K_max].astype(np.int16)
B = mu_all[2::4][:K_max].astype(np.int16)
C = mu_all[3::4][:K_max].astype(np.int16)
states = ((A + 1) * 9 + (B + 1) * 3 + (C + 1)).astype(np.int8)
cumA = np.cumsum(A, dtype=np.int64)
cumB = np.cumsum(B, dtype=np.int64)
cumC = np.cumsum(C, dtype=np.int64)
absM = np.abs(cumA + cumB + cumC)
del mu_all, A, B, C

checkpoints = [c for c in
               (10**4, 10**5, 10**6, 5 * 10**6, 10**7, K_max) if c <= K_max]
checkpoints = sorted(set(checkpoints))
results = {"N": N, "K_max": int(K_max), "checkpoints": []}

for K in checkpoints:
    cur = states[:K]
    pair = cur[:-1].astype(np.int32) * 27 + cur[1:].astype(np.int32)
    joint = np.bincount(pair, minlength=729).astype(np.float64)
    joint /= joint.sum()
    marg = np.bincount(cur, minlength=27).astype(np.float64)
    marg /= marg.sum()
    indep = np.outer(marg, marg).ravel()
    tv_indep = float(0.5 * np.abs(joint - indep).sum())
    nz = [(i + 1) * 9 + (j + 1) * 3 + (kk + 1)
          for i in (-1, 1) for j in (-1, 1) for kk in (-1, 1)]
    mask = np.isin(cur[:-1], nz) & np.isin(cur[1:], nz)
    p8 = cur[:-1][mask].astype(np.int32) * 27 + cur[1:][mask].astype(np.int32)
    j8 = np.bincount(p8, minlength=729).astype(np.float64)
    sel = np.array([x * 27 + y for x in nz for y in nz])
    j8 = j8[sel]
    j8 /= j8.sum()
    tv_uniform8 = float(0.5 * np.abs(j8 - 1.0 / 64).sum())
    trip = (cur[:-2].astype(np.int64) * 729 + cur[1:-1].astype(np.int64) * 27
            + cur[2:].astype(np.int64))
    tc = np.bincount(trip, minlength=27**3).astype(np.float64)
    pj = (tc / tc.sum()).reshape(27, 27, 27)
    p_mid = pj.sum(axis=(0, 2))
    p_xm = pj.sum(axis=2)
    p_my = pj.sum(axis=0)
    with np.errstate(divide="ignore", invalid="ignore"):
        num = pj * p_mid[None, :, None]
        den = p_xm[:, :, None] * p_my[None, :, :]
        lr = np.where(pj > 0, np.log(np.where(pj > 0, num / den, 1.0)), 0.0)
    cmi = float((pj * lr).sum())
    mx = int(absM[:K].max())
    results["checkpoints"].append({
        "K": int(K),
        "tv_joint_vs_independent_27": tv_indep,
        "tv_pairs_vs_uniform_8x8": tv_uniform8,
        "cond_mutual_info_two_step": cmi,
        "W_a": int(cumA[K - 1]), "W_b": int(cumB[K - 1]),
        "W_c": int(cumC[K - 1]),
        "max_abs_M4K_up_to_K": mx,
        "max_abs_M_over_sqrt4K": mx / (4 * K) ** 0.5,
    })
    print(json.dumps(results["checkpoints"][-1]), flush=True)

cps = results["checkpoints"]
if len(cps) >= 3:
    Ks = np.array([c["K"] for c in cps], dtype=float)
    for key in ("tv_joint_vs_independent_27", "tv_pairs_vs_uniform_8x8",
                "cond_mutual_info_two_step"):
        ys = np.array([abs(c[key]) for c in cps], dtype=float)
        good = ys > 0
        if good.sum() >= 3:
            alpha = float(np.polyfit(np.log(Ks[good]), np.log(ys[good]), 1)[0])
            results[f"rate_exponent_{key}"] = alpha
print(json.dumps({k: v for k, v in results.items() if k != "checkpoints"}))
json.dump(results, open("probe040_results.json", "w"), indent=1)
print("DONE")
