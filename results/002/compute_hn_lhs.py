#!/usr/bin/env python3
"""Diagnostic 002: first computation of the eq:HN left side.

Pure Python 3 stdlib. Deterministic. See results/002/002.md for the
declared method and numerics-channel scope. Definitions follow
paper/seeded_prime_comb_harmonic_reduction.tex verbatim:

  u_p(a)  = +1 if p∤a ; −1 if p|a, p²∤a ; 0 if p²|a
  σ_k(n)  = −∏_{p≤y_k} u_p(n mod p²),  y_k = ⌊√W_k⌋
  s_k(n)  = 1 iff n squarefree and P⁺(n) ≤ y_k
  c_k(n)  = σ_k(n)·s_k(n)                     (1 ≤ n ≤ W_k)
  Q_k     = ∏_{p≤y_k} p² ;  m_k = ⌊W_k/Q_k⌋+1 ;  𝒬_k = m_k·Q_k
  F_k(n)  = σ_k(n mod Q_k) − 2·c_k^0(n)        on Z/𝒬_k
  F̂(r)   = (1/𝒬)·Σ_n F(n)·e(−rn/𝒬)
  b_k(r)  = F̂_k(r)·e(r(L_k+1)/𝒬_k),  L_k = W_{k-1}
  D_N(θ)  = Σ_{j=0}^{N−1} e(jθ)
  identity (kernel-proved):  Σ_r b_k(r)·D_N(r/𝒬_k) = M(L_k+N) − M(L_k)
"""

import cmath
import csv
import math
import os
import time

HERE = os.path.dirname(os.path.abspath(__file__))

PRIMORIALS = [1, 2, 6, 30, 210, 2310, 30030, 510510, 9699690]  # W_0..W_8
W8 = PRIMORIALS[8]

# Paper Section-7 table: k -> (max|R_k|, maximizing x)
PAPER_TABLE = {
    2: (2, 5), 3: (2, 13), 4: (5, 95), 5: (15, 1637),
    6: (71, 24185), 7: (274, 355733), 8: (1085, 6481601),
}


def primes_upto(n):
    if n < 2:
        return []
    s = bytearray([1]) * (n + 1)
    s[0:2] = b"\x00\x00"
    for p in range(2, int(n ** 0.5) + 1):
        if s[p]:
            s[p * p:: p] = bytearray(len(range(p * p, n + 1, p)))
    return [i for i in range(2, n + 1) if s[i]]


def mobius_sieve_exact(n):
    """Exact Möbius sieve: tracks the product of found prime factors."""
    mu = [1] * (n + 1)
    mu[0] = 0
    prod = [1] * (n + 1)
    for p in primes_upto(int(n ** 0.5)):
        for m in range(p, n + 1, p):
            mu[m] = -mu[m]
            prod[m] *= p
        pp = p * p
        for m in range(pp, n + 1, pp):
            mu[m] = 0
    for m in range(2, n + 1):
        if mu[m] != 0 and prod[m] < m:
            mu[m] = -mu[m]  # one unseen prime factor > sqrt(n)
    del prod
    return mu


def write_csv(name, header, rows):
    with open(os.path.join(HERE, name), "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(header)
        w.writerows(rows)


def svg_loglog(name, title, series, guides, xlabel, ylabel):
    """Minimal hand-rolled log2-log2 SVG line plot.

    series: list of (label, color, [(x, y), ...]) with x, y > 0.
    guides: list of (label, color, slope, anchor_x, anchor_y) drawn as
            straight lines in log2 space through the anchor.
    """
    W, H, ML, MB, MT, MR = 640, 420, 56, 44, 28, 16
    pts_all = [p for _, _, pts in series for p in pts]
    xs = [math.log2(x) for x, _ in pts_all]
    ys = [math.log2(y) for _, y in pts_all if y > 0]
    x0, x1 = min(xs), max(xs)
    y0, y1 = min(ys) - 0.5, max(ys) + 0.5
    for _, _, slope, ax, ay in guides:
        for X in (x0, x1):
            Y = math.log2(ay) + slope * (X - math.log2(ax))
            y0, y1 = min(y0, Y), max(y1, Y)

    def px(x):
        return ML + (x - x0) / (x1 - x0) * (W - ML - MR)

    def py(y):
        return H - MB - (y - y0) / (y1 - y0) * (H - MB - MT)

    out = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
           f'font-family="sans-serif" font-size="11">',
           f'<rect width="{W}" height="{H}" fill="white"/>',
           f'<text x="{W/2:.0f}" y="16" text-anchor="middle" '
           f'font-size="13">{title}</text>']
    # axes + integer log2 ticks
    for t in range(math.ceil(x0), math.floor(x1) + 1, max(1, (math.floor(x1) - math.ceil(x0)) // 8 + 1)):
        out.append(f'<line x1="{px(t):.1f}" y1="{H-MB}" x2="{px(t):.1f}" '
                   f'y2="{MT}" stroke="#eee"/>')
        out.append(f'<text x="{px(t):.1f}" y="{H-MB+14}" '
                   f'text-anchor="middle">2^{t}</text>')
    for t in range(math.ceil(y0), math.floor(y1) + 1, max(1, (math.floor(y1) - math.ceil(y0)) // 8 + 1)):
        out.append(f'<line x1="{ML}" y1="{py(t):.1f}" x2="{W-MR}" '
                   f'y2="{py(t):.1f}" stroke="#eee"/>')
        out.append(f'<text x="{ML-6}" y="{py(t)+4:.1f}" '
                   f'text-anchor="end">2^{t}</text>')
    out.append(f'<rect x="{ML}" y="{MT}" width="{W-ML-MR}" '
               f'height="{H-MB-MT}" fill="none" stroke="#999"/>')
    out.append(f'<text x="{W/2:.0f}" y="{H-8}" text-anchor="middle">{xlabel}</text>')
    out.append(f'<text x="14" y="{H/2:.0f}" text-anchor="middle" '
               f'transform="rotate(-90 14 {H/2:.0f})">{ylabel}</text>')
    legend_y = MT + 14
    for label, color, slope, ax, ay in guides:
        lx0, lx1 = x0, x1
        ly0 = math.log2(ay) + slope * (lx0 - math.log2(ax))
        ly1 = math.log2(ay) + slope * (lx1 - math.log2(ax))
        out.append(f'<line x1="{px(lx0):.1f}" y1="{py(ly0):.1f}" '
                   f'x2="{px(lx1):.1f}" y2="{py(ly1):.1f}" stroke="{color}" '
                   f'stroke-dasharray="5,4"/>')
        out.append(f'<text x="{ML+8}" y="{legend_y}" fill="{color}">{label}</text>')
        legend_y += 14
    for label, color, pts in series:
        d = " ".join(f'{px(math.log2(x)):.1f},{py(math.log2(y)):.1f}'
                     for x, y in pts if y > 0)
        out.append(f'<polyline points="{d}" fill="none" stroke="{color}" '
                   f'stroke-width="1.5"/>')
        out.append(f'<text x="{ML+8}" y="{legend_y}" fill="{color}">{label}</text>')
        legend_y += 14
    out.append("</svg>")
    with open(os.path.join(HERE, name), "w") as fh:
        fh.write("\n".join(out))


# ---------------------------------------------------------------- part 1

def part1(mu):
    print("part 1: exact maximal profile k=2..8", flush=True)
    summary = []
    for k in range(2, 9):
        L, Wk = PRIMORIALS[k - 1], PRIMORIALS[k]
        H = Wk - L
        R = 0
        runmax = 0
        best = (0, 0)          # (max|R|, x)
        # exact sup ratios kept as integer pairs: sup^2 = num/den,
        # compared by cross-multiplication (no floats in the loop)
        pin_num, pin_den = 0, 1
        blk_num, blk_den = 0, 1
        arg_pinned = arg_block = 0
        envelope = []          # (N, runmax) at each new max
        step = max(1, H // 2000)
        curve = []
        for N in range(1, H + 1):
            R += mu[L + N]
            a = abs(R)
            if a > runmax:
                runmax = a
                envelope.append((N, a))
            if a > best[0]:
                best = (a, L + N)
            if a:
                aa = a * a
                if aa * pin_den > pin_num * (L + N):
                    pin_num, pin_den, arg_pinned = aa, L + N, N
                if aa * blk_den > blk_num * N:
                    blk_num, blk_den, arg_block = aa, N, N
            if N % step == 0 or N == H:
                curve.append((N, R, runmax))
        ok = PAPER_TABLE[k] == best
        summary.append({
            "k": k, "L": L, "W": Wk, "H": H,
            "maxR": best[0], "arg_x": best[1],
            "sup_pinned": math.sqrt(pin_num / pin_den), "argN_pinned": arg_pinned,
            "sup_block": math.sqrt(blk_num / blk_den), "argN_block": arg_block,
            "R_end": R, "paper_match": ok,
        })
        write_csv(f"profile_k{k}.csv", ["N", "R", "runmax_absR"], curve)
        svg_loglog(
            f"profile_k{k}.svg",
            f"k={k}: running max |R_k(L_k+N)| (= eq:HN LHS), block (W_{k-1}, W_{k}]",
            [(f"runmax |R_{k}|", "#c0392b", envelope)],
            [("(L_k+N)^1/2 (pinned eq:HN scale)", "#2980b9", 0.5, 1, math.sqrt(L + 1)),
             ("N^1/2 (in-block scale)", "#27ae60", 0.5, 1, 1.0)],
            "N", "max |R|")
        print(f"  k={k}: max|R|={best[0]} at x={best[1]} "
              f"(paper match: {ok}); sup|R|/sqrt(L+N)={summary[-1]['sup_pinned']:.6f}; "
              f"sup|R|/sqrt(N)={summary[-1]['sup_block']:.6f}; R(W_k)={R}", flush=True)
    write_csv("profile_summary.csv",
              ["k", "L", "W", "H", "max_absR", "arg_x", "sup_ratio_pinned",
               "argN_pinned", "sup_ratio_block", "argN_block", "R_end",
               "paper_match"],
              [[s["k"], s["L"], s["W"], s["H"], s["maxR"], s["arg_x"],
                f"{s['sup_pinned']:.9f}", s["argN_pinned"],
                f"{s['sup_block']:.9f}", s["argN_block"], s["R_end"],
                s["paper_match"]] for s in summary])
    return summary


# ---------------------------------------------------------------- part 2

def sigma_table(ps, Q):
    """σ(n) for n in Z/Q as exact ints."""
    tab = []
    for n in range(Q):
        v = -1
        for p in ps:
            a = n % (p * p)
            if a % (p * p) == 0:
                v = 0
                break
            if a % p == 0:
                v = -v
        tab.append(v)
    return tab


def part2(mu):
    print("part 2: spectral verification k=2,3", flush=True)
    results = {}
    for k in (2, 3):
        L, Wk = PRIMORIALS[k - 1], PRIMORIALS[k]
        H = Wk - L
        y = math.isqrt(Wk)
        ps = primes_upto(y)
        Q = 1
        for p in ps:
            Q *= p * p
        m = Wk // Q + 1
        QQ = m * Q
        sig = sigma_table(ps, Q)
        # smooth core sites: squarefree, P+(n) <= y, 1 <= n <= Wk
        smooth = []
        for n in range(1, Wk + 1):
            if mu[n] == 0:
                continue
            x = n
            for p in ps:
                while x % p == 0:
                    x //= p
            if x == 1:
                smooth.append(n)
        F = [0] * QQ
        for n in range(QQ):
            F[n] = sig[n % Q]
        for n in smooth:
            F[n] -= 2 * sig[n % Q]
        # exact embedding check: F(n) == mu(n) on 1..Wk
        embed_ok = all(F[n] == mu[n] for n in range(1, Wk + 1))
        # DFT (float64)
        e = [cmath.exp(-2j * cmath.pi * t / QQ) for t in range(QQ)]
        Fh = []
        for r in range(QQ):
            s = 0j
            for n in range(QQ):
                if F[n]:
                    s += F[n] * e[(r * n) % QQ]
            Fh.append(s / QQ)
        b = [Fh[r] * cmath.exp(2j * cmath.pi * r * (L + 1) / QQ)
             for r in range(QQ)]
        # Parseval
        lhsP = sum(v * v for v in F)
        rhsP = QQ * sum(abs(z) ** 2 for z in Fh)
        parseval_err = abs(lhsP - rhsP)
        # raw-comb l1 identity on Z/Q
        sh = []
        eQ = [cmath.exp(-2j * cmath.pi * t / Q) for t in range(Q)]
        for r in range(Q):
            s = 0j
            for n in range(Q):
                if sig[n]:
                    s += sig[n] * eQ[(r * n) % Q]
            sh.append(s / Q)
        l1 = sum(abs(z) for z in sh)
        l1_pred = 1.0
        for p in ps:
            l1_pred *= 2 * (p - 1) * (2 * p - 1) / (p * p)
        # identity check for every N: incremental D_N update
        R = 0
        D = [0j] * QQ           # D_0 = 0
        ph = [cmath.exp(2j * cmath.pi * r / QQ) for r in range(QQ)]
        cur = [1.0 + 0j] * QQ   # e(N*r/QQ) for N=0
        max_err = 0.0
        for N in range(1, H + 1):
            for r in range(QQ):
                D[r] += cur[r]
                cur[r] *= ph[r]
            S = sum(b[r] * D[r] for r in range(QQ))
            R += mu[L + N]
            max_err = max(max_err, abs(S - R))
        results[k] = dict(Q=Q, m=m, QQ=QQ, embed_ok=embed_ok,
                          parseval_err=parseval_err, l1=l1, l1_pred=l1_pred,
                          max_identity_err=max_err, n_smooth=len(smooth))
        print(f"  k={k}: QQ={QQ} embed_ok={embed_ok} "
              f"max identity err={max_err:.3e} parseval_err={parseval_err:.3e} "
              f"l1={l1:.9f} vs pred {l1_pred:.9f}", flush=True)
        if k == 3:
            write_csv("spectrum_k3.csv", ["r", "abs_b", "re_b", "im_b"],
                      [[r, f"{abs(b[r]):.12e}", f"{b[r].real:.12e}",
                        f"{b[r].imag:.12e}"] for r in range(QQ)])
            # conductor grouping: q = QQ / gcd(r, QQ)
            cond = {}
            for r in range(QQ):
                q = QQ // math.gcd(r, QQ)
                c = cond.setdefault(q, [0, 0.0, 0.0])
                c[0] += 1
                c[1] += abs(b[r])
                c[2] += abs(b[r]) ** 2
            write_csv("conductor_energy_k3.csv",
                      ["conductor_q", "n_freqs", "l1_mass", "l2_energy"],
                      [[q, c[0], f"{c[1]:.12e}", f"{c[2]:.12e}"]
                       for q, c in sorted(cond.items())])
            top = sorted(range(QQ), key=lambda r: -abs(b[r]))[:16]
            write_csv("top_coefficients_k3.csv",
                      ["r", "conductor_q", "abs_b"],
                      [[r, QQ // math.gcd(r, QQ), f"{abs(b[r]):.12e}"]
                       for r in top])
            pts = sorted((QQ // math.gcd(r, QQ), abs(b[r]))
                         for r in range(1, QQ) if abs(b[r]) > 1e-15)
            svg_loglog("spectrum_k3.svg",
                       "k=3: |b_3(r)| by conductor q = 900/gcd(r,900)",
                       [("|b_3(r)| (each nonzero r)", "#8e44ad", pts)],
                       [], "conductor q", "|b(r)|")
    return results


# ---------------------------------------------------------------- part 3

def part3():
    print("part 3: dense-spectrum feasibility", flush=True)
    rows = []
    for k in range(2, 9):
        Wk = PRIMORIALS[k]
        y = math.isqrt(Wk)
        ps = primes_upto(y)
        Q = 1
        for p in ps:
            Q *= p * p
        m = Wk // Q + 1
        QQ = m * Q
        rows.append([k, Wk, y, len(ps), Q if Q < 10**18 else f"~1e{len(str(Q))-1}",
                     m, len(str(QQ)),
                     "dense-feasible" if QQ <= 10**7 else
                     ("structured-only (CRT tensor + smooth set)" if QQ <= 10**10
                      else "infeasible dense")])
        print(f"  k={k}: y={y} pi(y)={len(ps)} digits(QQ)={len(str(QQ))}", flush=True)
    write_csv("feasibility.csv",
              ["k", "W_k", "y_k", "pi_y", "Q_k", "m_k", "digits_QQ", "verdict"],
              rows)
    return rows


def main():
    t0 = time.time()
    print("sieving Möbius to", W8, flush=True)
    mu = mobius_sieve_exact(W8)
    assert [mu[i] for i in range(1, 11)] == [1, -1, -1, 0, -1, 1, -1, 0, 0, 1]
    print(f"  sieve done in {time.time()-t0:.1f}s", flush=True)
    s1 = part1(mu)
    s2 = part2(mu)
    s3 = part3()
    with open(os.path.join(HERE, "summary.md"), "w") as fh:
        fh.write("# Diagnostic 002 — machine summary\n\n")
        fh.write("Generated by compute_hn_lhs.py (deterministic). "
                 "See 002.md for scope.\n\n## Part 1 (exact)\n\n")
        fh.write("| k | max|R| | at x | paper match | sup |R|/√(L+N) | sup |R|/√N | R(W_k) |\n|---|---|---|---|---|---|---|\n")
        for s in s1:
            fh.write(f"| {s['k']} | {s['maxR']} | {s['arg_x']} | "
                     f"{s['paper_match']} | {s['sup_pinned']:.6f} | "
                     f"{s['sup_block']:.6f} | {s['R_end']} |\n")
        fh.write("\n## Part 2 (float64 DFT)\n\n")
        for k, r in s2.items():
            fh.write(f"- k={k}: 𝒬={r['QQ']}, embed_ok={r['embed_ok']}, "
                     f"max identity error={r['max_identity_err']:.3e}, "
                     f"Parseval err={r['parseval_err']:.3e}, "
                     f"ℓ¹(raw)={r['l1']:.9f} vs predicted {r['l1_pred']:.9f}, "
                     f"#smooth sites={r['n_smooth']}\n")
        fh.write("\n## Part 3 (feasibility)\n\nSee feasibility.csv.\n")
    print(f"total {time.time()-t0:.1f}s", flush=True)


if __name__ == "__main__":
    main()
