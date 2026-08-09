#!/usr/bin/env python3
"""K2 step 1: cache the first NZ nontrivial zeta zero ordinates to >= 25 digits.

mpmath.zetazero(n) at mp.dps = 30, parallelised over 14 processes.
Output: work/zeros/zeros_gamma_dps30.txt  (one 30-digit decimal per line,
        line j = gamma_j, j = 1..NZ)
        work/zeros/zeros_gamma_f64.npy    (float64 view for the numerics)
"""
import os, sys, time, math
import numpy as np
from multiprocessing import Pool

NZ = int(os.environ.get("NZ", "2000"))
DPS = 30
OUT = os.path.expanduser("~/work/zeros")
os.makedirs(OUT, exist_ok=True)
t0 = time.time()


def log(*a):
    print(f"[{time.time()-t0:8.1f}s]", *a, flush=True)


def hard_asserts():
    """M(6) = -1, M(8) = -2, M(30) = -3 -- standing boundary asserts."""
    mu = np.load(os.path.expanduser("~/work/killtests/fw_mu.npy"), mmap_mode="r")
    M = np.cumsum(np.asarray(mu[:31], dtype=np.int64))
    assert M[6] == -1, f"M(6) = {M[6]} != -1"
    assert M[8] == -2, f"M(8) = {M[8]} != -2"
    assert M[30] == -3, f"M(30) = {M[30]} != -3"
    Mi = np.load(os.path.expanduser("~/work/killtests/fw_M_i32.npy"), mmap_mode="r")
    assert Mi[6] == -1 and Mi[8] == -2 and Mi[30] == -3, "fw_M_i32 checkpoint fail"


def chunk(args):
    lo, hi = args
    from mpmath import mp, zetazero
    mp.dps = DPS
    out = []
    for n in range(lo, hi):
        z = zetazero(n)
        out.append((n, mp.nstr(z.imag, 28, strip_zeros=False)))
    return out


def main():
    hard_asserts()
    log(f"hard asserts OK; computing {NZ} zeros at dps={DPS}")
    # interleaved chunks so cost (grows with n) balances across workers
    NPROC = 14
    bounds = []
    step = 25
    for lo in range(1, NZ + 1, step):
        bounds.append((lo, min(lo + step, NZ + 1)))
    res = {}
    with Pool(NPROC) as pool:
        done = 0
        for out in pool.imap_unordered(chunk, bounds):
            for n, s in out:
                res[n] = s
            done += len(out)
            if done % 200 < step:
                log(f"  {done}/{NZ} zeros")
    lines = [res[n] for n in range(1, NZ + 1)]
    with open(os.path.join(OUT, "zeros_gamma_dps30.txt"), "w") as f:
        f.write("\n".join(lines) + "\n")
    g = np.array([float(s) for s in lines], dtype=np.float64)
    assert np.all(np.diff(g) > 0), "zero ordinates not increasing"
    np.save(os.path.join(OUT, "zeros_gamma_f64.npy"), g)
    log(f"wrote {NZ} zeros; gamma_1 = {lines[0]}, gamma_{NZ} = {lines[-1]}")
    # sanity against the classical first few
    for i, v in [(0, 14.134725141734693), (1, 21.022039638771555),
                 (2, 25.010857580145688), (9, 49.773832477672302)]:
        assert abs(g[i] - v) < 1e-9, f"gamma_{i+1} = {g[i]} != {v}"
    log("classical checkpoints OK")


if __name__ == "__main__":
    main()
