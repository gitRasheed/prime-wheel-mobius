#!/usr/bin/env python3
"""
Deterministic reproducibility suite for the square-prefix squared-complex-space paper.

Outputs:
  run_summary.txt
  prefix_energy.csv
  prime_curve_decomposition.csv
  cofactor_cascade.csv
  dyadic_block_stats_*.csv
  dyadic_gram_*.csv
  major_arc_block_comparison_N4096.csv
  major_arc_regression.csv
  gram_spectrum_*.csv
  low_height_diagnostics.csv
  local_ratio_diagnostics.csv

All exact identities and energies use integer arithmetic. Floating point is used
only for normalized ratios, correlations, and the log-log diagnostic slope.
"""

from __future__ import annotations

import argparse
import cmath
import csv
import math
from pathlib import Path

import numpy as np
from numba import njit


@njit(cache=True)
def linear_sieve_mu_lpf(n: int):
    """Return mu, smallest prime factor, largest prime factor, and primes <= n."""
    spf = np.zeros(n + 1, dtype=np.int32)
    mu = np.zeros(n + 1, dtype=np.int8)
    primes = np.empty(max(16, n // 8), dtype=np.int32)
    pc = 0
    mu[1] = 1

    for i in range(2, n + 1):
        if spf[i] == 0:
            spf[i] = i
            primes[pc] = i
            pc += 1
            mu[i] = -1

        j = 0
        while j < pc:
            p = primes[j]
            v = p * i
            if v > n:
                break
            spf[v] = p
            if p == spf[i]:
                mu[v] = 0
                break
            mu[v] = -mu[i]
            j += 1

    lpf = np.zeros(n + 1, dtype=np.int32)
    lpf[1] = 1
    for i in range(2, n + 1):
        p = spf[i]
        rest = i // p
        previous = lpf[rest]
        lpf[i] = p if p > previous else previous

    return mu, spf, lpf, primes[:pc]


@njit(cache=True)
def compute_at_by_intervals(mu, lpf, nmax: int):
    """Compute A_n and T_n independently from source entry/transition intervals."""
    diff_a = np.zeros(nmax + 2, dtype=np.int64)
    diff_t = np.zeros(nmax + 2, dtype=np.int64)

    diff_a[1] += 1
    diff_a[nmax + 1] -= 1

    for m in range(2, len(mu)):
        muv = int(mu[m])
        if muv == 0:
            continue

        entry = int(math.sqrt(m))
        if entry > nmax:
            continue

        q = int(lpf[m])
        transition = q - 1

        smooth_start = entry if transition <= entry else transition
        if smooth_start <= nmax:
            diff_a[smooth_start] += muv
            diff_a[nmax + 1] -= muv

        if transition > entry:
            end = transition if transition <= nmax + 1 else nmax + 1
            diff_t[entry] += -muv
            diff_t[end] -= -muv

    a = np.cumsum(diff_a)[: nmax + 1]
    t = np.cumsum(diff_t)[: nmax + 1]
    return a, t


@njit(cache=True)
def exact_source_checks(mu, lpf, nmax: int):
    norm_violations = 0
    curve_violations = 0
    lifetime_violations = 0
    sources = 0

    for m in range(2, len(mu)):
        if mu[m] == 0:
            continue
        sources += 1
        q = int(lpf[m])
        c = m // q
        y2 = q * q - c * c
        rho2 = q * q + c * c

        if rho2 * rho2 != 4 * m * m + y2 * y2:
            norm_violations += 1
        if c * c * y2 != m * m - c**4:
            curve_violations += 1

        n = int(math.sqrt(m))
        if n <= nmax:
            lifetime = q - n - 1
            if lifetime < 0:
                lifetime = 0
            if y2 > 0 and q * lifetime > y2:
                lifetime_violations += 1
            if y2 <= 0 and lifetime != 0:
                lifetime_violations += 1

    return sources, norm_violations, curve_violations, lifetime_violations


@njit(cache=True)
def low_height_stats(mu, lpf, nmax: int, lambdas):
    k = len(lambdas)
    total_counts = np.zeros((k, nmax + 1), dtype=np.int32)
    odd_counts = np.zeros((k, nmax + 1), dtype=np.int32)
    even_counts = np.zeros((k, nmax + 1), dtype=np.int32)
    total_incidence = np.zeros((k, nmax + 1), dtype=np.int64)
    odd_incidence = np.zeros((k, nmax + 1), dtype=np.int64)
    even_incidence = np.zeros((k, nmax + 1), dtype=np.int64)

    for m in range(2, len(mu)):
        if mu[m] == 0:
            continue
        n = int(math.sqrt(m))
        if n < 1 or n > nmax:
            continue

        q = int(lpf[m])
        c = m // q
        abs_y2 = abs(q * q - c * c)
        lifetime = q - n - 1
        if lifetime < 0:
            lifetime = 0
        inc = 1 + lifetime
        is_odd = (m & 1) == 1

        for j in range(k):
            if abs_y2 <= 2.0 * lambdas[j] * n:
                total_counts[j, n] += 1
                total_incidence[j, n] += inc
                if is_odd:
                    odd_counts[j, n] += 1
                    odd_incidence[j, n] += inc
                else:
                    even_counts[j, n] += 1
                    even_incidence[j, n] += inc

    return (
        total_counts,
        odd_counts,
        even_counts,
        total_incidence,
        odd_incidence,
        even_incidence,
    )


@njit(cache=True)
def cofactor_block_bins(mu, lpf, nmax: int, levels: int):
    """
    Bin square-block increments by the smallest dyadic cofactor threshold 2^j
    containing c=m/Pplus(m). The m=1 source is added later as a constant 1.
    """
    bins = np.zeros((levels, nmax + 1), dtype=np.int64)
    max_c = 1

    for m in range(2, len(mu)):
        muv = int(mu[m])
        if muv == 0:
            continue
        n = int(math.sqrt(m))
        if n > nmax:
            continue
        q = int(lpf[m])
        c = m // q
        if c > max_c:
            max_c = c

        j = 0
        threshold = 1
        while threshold < c:
            threshold *= 2
            j += 1
        bins[j, n] += muv

    return bins, max_c




@njit(cache=True)
def cofactor_block_bins_high(mu, lpf, nmax: int, levels: int, lambda_high: float):
    """Square-block increments by dyadic cofactor block, restricted to |Y|>lambda*n."""
    bins = np.zeros((levels, nmax + 1), dtype=np.int64)
    for m in range(2, len(mu)):
        muv = int(mu[m])
        if muv == 0:
            continue
        n = int(math.sqrt(m))
        if n > nmax:
            continue
        q = int(lpf[m])
        c = m // q
        if abs(q * q - c * c) <= 2.0 * lambda_high * n:
            continue
        j = 0
        threshold = 1
        while threshold < c:
            threshold *= 2
            j += 1
        bins[j, n] += muv
    return bins


def block_label(j: int) -> str:
    if j == 0:
        return "c=1"
    return f"{1 << (j - 1)}<c<={1 << j}"


def write_dyadic_gram_outputs(out: Path, tag: str, block_vectors: np.ndarray,
                               checkpoints, mu: np.ndarray, max_observed_c: int):
    max_j = int(math.ceil(math.log2(max_observed_c)))
    vectors = block_vectors[: max_j + 1]
    labels = [block_label(j) for j in range(max_j + 1)]
    spectrum_rows = []
    comparison_rows = []

    for n in checkpoints:
        v = vectors[:, :n]
        gram = v @ v.T
        norms = np.diag(gram)
        prime = v[0]
        prime_norm = float(norms[0])
        cumulative = np.ones(n, dtype=np.int64)
        stats_rows = []

        for j, label in enumerate(labels):
            block = v[j]
            before = cumulative.copy()
            cumulative = before + block
            norm = int(norms[j])
            inner_prime = int(np.dot(prime, block))
            inner_before = int(np.dot(before, block))
            energy_before = int(np.dot(before, before))
            energy_after = int(np.dot(cumulative, cumulative))
            delta = energy_after - energy_before
            corr = float(inner_prime / (np.linalg.norm(prime) * np.linalg.norm(block))) if norm and norms[0] else float("nan")
            ratio_prime = float(-2 * inner_prime / norm) if norm else float("nan")
            ratio_before = float(-2 * inner_before / norm) if norm else float("nan")
            stats_rows.append([
                tag, n, j, label, int(block[-1]), norm, norm / n**3,
                inner_prime, inner_prime / n**3, corr, ratio_prime,
                inner_before, inner_before / n**3, ratio_before,
                delta, delta / n**3, energy_after, energy_after / n**3,
            ])

            if tag == "all" and n == checkpoints[-1]:
                lo = 1 if j == 0 else (1 << (j - 1)) + 1
                hi = 1 << j
                a_block = float(np.sum(mu[lo : hi + 1].astype(np.float64) /
                                       np.arange(lo, hi + 1, dtype=np.float64)))
                comparison_rows.append([
                    j, label, a_block, inner_prime / prime_norm,
                    norm / prime_norm, corr, delta / n**3, energy_after / n**3,
                ])

        write_csv(
            out / f"dyadic_block_stats_{tag}_N{n}.csv",
            ["sector", "N", "block_index", "cofactor_block", "block_endpoint_value",
             "block_norm2", "block_norm2_over_N3", "inner_prime_block",
             "inner_prime_block_over_N3", "corr_prime_block",
             "minus_2_inner_prime_over_block_norm2", "inner_cumulative_before_block",
             "inner_cumulative_before_over_N3", "minus_2_inner_before_over_block_norm2",
             "cascade_energy_delta", "cascade_energy_delta_over_N3",
             "cascade_energy_after", "cascade_energy_after_over_N3"],
            stats_rows,
        )

        if n == checkpoints[-1]:
            gram_rows = []
            for i in range(len(labels)):
                for j in range(len(labels)):
                    den = math.sqrt(float(norms[i]) * float(norms[j]))
                    corr = float(gram[i, j] / den) if den else float("nan")
                    gram_rows.append([
                        tag, n, i, labels[i], j, labels[j], int(gram[i, j]),
                        gram[i, j] / n**3, corr,
                    ])
            write_csv(
                out / f"dyadic_gram_{tag}_N{n}.csv",
                ["sector", "N", "i", "block_i", "j", "block_j",
                 "inner_product", "inner_product_over_N3", "correlation"],
                gram_rows,
            )

            for cutoff_j in (5, 6, 10, max_j):
                k = min(cutoff_j + 1, len(labels))
                vals = np.linalg.eigvalsh(gram[:k, :k])[::-1]
                spectrum_rows.append([
                    tag, n, 1 << (k - 1), k, vals[0] / vals.sum(),
                    vals[1] / vals[0] if k > 1 else 0.0,
                ])

    if comparison_rows:
        write_csv(
            out / f"major_arc_block_comparison_N{checkpoints[-1]}.csv",
            ["block_index", "cofactor_block", "A_block_sum_mu_over_c",
             "beta_hat_inner_over_prime_norm", "block_norm_ratio",
             "corr_prime", "cascade_energy_delta_over_N3", "V_after_over_N3"],
            comparison_rows,
        )
    write_csv(
        out / f"gram_spectrum_{tag}.csv",
        ["sector", "N", "cofactor_cutoff", "number_of_blocks",
         "top_eigenvalue_share", "lambda2_over_lambda1"],
        spectrum_rows,
    )


def worst_local_ratio(s_values: np.ndarray, base_n: int):
    squares = s_values.astype(np.int64) ** 2
    prefix = np.concatenate(([0], np.cumsum(squares, dtype=np.int64)))
    best_ratio = -1.0
    best_start = 0
    best_h = 0
    best_energy = 0

    h = 1
    while h <= base_n:
        last_start = 2 * base_n - h
        for start in range(base_n, last_start + 1):
            energy = int(prefix[start + h - 1] - prefix[start - 1])
            ratio = energy / (h * start * start)
            if ratio > best_ratio:
                best_ratio = ratio
                best_start = start
                best_h = h
                best_energy = energy
        h *= 2

    return best_ratio, best_start, best_h, best_energy


def major_arc_regression(primes: np.ndarray, lo: int = 2000, hi: int = 4000):
    """
    Small-modulus prime-phase regression test (manuscript Section
    "Small-modulus prime-phase regression test").

    Verifies, for every prime q in (lo, hi]:
      * q^2 = 1 (mod 24), exactly;
    then verifies, for the eight rational test frequencies
    alpha = p/12 quoted in the manuscript, that the coherent prime
    Weyl sum S_prime(alpha) = sum_q e(alpha * q^2 / 2) has |S_prime(alpha)|
    equal to the prime count exactly (up to floating tolerance), since
    q^2 = 24k+1 forces every term onto the single common phase e(alpha/2).

    Finally verifies the old-versus-corrected reduced Gauss factor at
    (a, r) = (1, 3): the naive sum over representatives mod r vanishes
    (an artifact of using a modulus on which the phase is not
    well-defined), while the corrected sum over units mod 2r has the
    expected unit magnitude.

    Returns a dict of summary scalars and a list of CSV rows.
    """
    qs = primes[(primes > lo) & (primes <= hi)].astype(np.int64)
    prime_count = int(qs.size)

    mod24 = np.mod(qs * qs, 24)
    mod24_violations = int(np.count_nonzero(mod24 != 1))

    test_alphas = [
        ("0", 0, 12, "1"),
        ("1/2", 6, 12, "e(1/4)"),
        ("1/3", 4, 12, "e(1/6)"),
        ("2/3", 8, 12, "e(1/3)"),
        ("1/4", 3, 12, "e(1/8)"),
        ("3/4", 9, 12, "e(3/8)"),
        ("1/6", 2, 12, "e(1/12)"),
        ("5/6", 10, 12, "e(5/12)"),
    ]

    rows = []
    rows.append([
        "prime_square_mod24", lo, hi, prime_count, mod24_violations,
        prime_count, "count",
    ])

    frequency_violations = 0
    tol = 1e-6
    for label, num, den, common_phase in test_alphas:
        alpha = num / den
        phases = np.exp(2j * np.pi * alpha * (qs.astype(np.float64) ** 2) / 2.0)
        s_alpha = complex(np.sum(phases))
        deviation = abs(abs(s_alpha) - prime_count)
        if deviation > tol:
            frequency_violations += 1
        rows.append([
            "toy_prime_resonance", label, common_phase, abs(s_alpha),
            prime_count, deviation, "magnitude",
        ])

    # Old (naive) reduced factor: sum over representatives mod r=3,
    # a=1 -- an artifact of a modulus on which the quadratic phase is
    # not well-defined. Expected to vanish.
    old_factor = sum(
        cmath.exp(2j * math.pi * (u * u) / 6.0) for u in (1, 2)
    )
    old_factor_abs = abs(old_factor)

    # Corrected reduced factor: sum over units mod 2r=6, normalized by
    # phi(6)=2. Expected unit magnitude.
    corrected_units = [u for u in range(6) if math.gcd(u, 6) == 1]
    corrected_sum = sum(
        cmath.exp(2j * math.pi * (u * u) / 6.0) for u in corrected_units
    )
    corrected_factor = corrected_sum / len(corrected_units)
    corrected_factor_abs = abs(corrected_factor)

    rows.append([
        "old_modulus_3_factor", "a=1,r=3", "sum_over_reps_mod_r",
        old_factor_abs, 0, old_factor_abs, "magnitude",
    ])
    rows.append([
        "corrected_modulus_6_factor", "a=1,r=3", "sum_over_units_mod_2r",
        corrected_factor_abs, 1, abs(corrected_factor_abs - 1), "magnitude",
    ])

    def snap(value: float) -> float:
        """Report a value that is within floating tolerance of an
        integer as that exact integer, matching the paper's exact-check
        convention; otherwise report the raw float unchanged."""
        nearest = round(value)
        return float(nearest) if abs(value - nearest) < 1e-9 else value

    summary = {
        "toy_prime_count": prime_count,
        "prime_square_mod24_violations": mod24_violations,
        "toy_prime_resonance_violations": frequency_violations,
        "old_modulus_3_factor_abs": snap(old_factor_abs),
        "corrected_modulus_6_factor_abs": snap(corrected_factor_abs),
    }
    return summary, rows


def write_csv(path: Path, header, rows):
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(header)
        writer.writerows(rows)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--nmax", type=int, default=4096)
    parser.add_argument("--out", type=Path, default=Path("."))
    args = parser.parse_args()

    nmax = args.nmax
    out = args.out
    out.mkdir(parents=True, exist_ok=True)
    xmax = (nmax + 1) ** 2 - 1

    mu, spf, lpf, primes = linear_sieve_mu_lpf(xmax)
    mertens = np.cumsum(mu, dtype=np.int32)

    is_prime = np.zeros(xmax + 1, dtype=np.int8)
    is_prime[primes] = 1
    prime_pi = np.cumsum(is_prime, dtype=np.int32)

    n_values = np.arange(1, nmax + 1, dtype=np.int64)
    x_values = (n_values + 1) ** 2 - 1
    s_values = mertens[x_values].astype(np.int64)
    pi_values = prime_pi[x_values].astype(np.int64)

    a_values, t_values = compute_at_by_intervals(mu, lpf, nmax)
    at_errors = a_values[1:] - t_values[1:] - s_values

    source_count, norm_bad, curve_bad, lifetime_bad = exact_source_checks(mu, lpf, nmax)

    checkpoints = [n for n in (128, 256, 512, 1024, 2048, 4096) if n <= nmax]

    prefix_rows = []
    prime_rows = []
    for n in checkpoints:
        s = s_values[:n]
        a = a_values[1 : n + 1]
        t = t_values[1 : n + 1]

        v = int(np.dot(s, s))
        va = int(np.dot(a, a))
        vt = int(np.dot(t, t))
        vat = int(np.dot(a, t))

        prime_curve = -pi_values[:n]
        other_curves = s - prime_curve
        v_prime = int(np.dot(prime_curve, prime_curve))
        v_other = int(np.dot(other_curves, other_curves))
        twice_cross = int(2 * np.dot(prime_curve, other_curves))
        corr = float(
            np.dot(prime_curve, other_curves)
            / (np.linalg.norm(prime_curve) * np.linalg.norm(other_curves))
        )

        prefix_rows.append(
            [n, int(x_values[n - 1]), int(s_values[n - 1]), v, v / n**3,
             va / n**3, vt / n**3, vat / n**3]
        )
        prime_rows.append(
            [n, int(pi_values[n - 1]), v / n**3, v_prime / n**3,
             v_other / n**3, twice_cross / n**3, v / v_prime, corr]
        )

    write_csv(
        out / "prefix_energy.csv",
        ["N", "X_N", "S_N", "V_total", "V_total_over_N3", "V_A_over_N3",
         "V_T_over_N3", "inner_A_T_over_N3"],
        prefix_rows,
    )
    write_csv(
        out / "prime_curve_decomposition.csv",
        ["N", "pi_X_N", "V_total_over_N3", "V_c1_over_N3",
         "V_c_ge_2_over_N3", "twice_cross_over_N3", "V_total_over_V_c1",
         "corr_c1_c_ge_2"],
        prime_rows,
    )

    # Dyadic cofactor cascade R_C(x)=1-sum_{c<=C} mu(c)[pi(x/c)-pi(Pplus(c))].
    max_possible_c = xmax // 2
    levels = int(math.ceil(math.log2(max_possible_c))) + 1
    bins, max_observed_c = cofactor_block_bins(mu, lpf, nmax, levels)
    cumulative_blocks = np.zeros(nmax + 1, dtype=np.int64)
    cascade_vectors = []
    thresholds = []
    for j in range(levels):
        cumulative_blocks += bins[j]
        threshold = 1 << j
        thresholds.append(threshold)
        cascade_vectors.append(1 + np.cumsum(cumulative_blocks[1:], dtype=np.int64))

    full_index = len(thresholds) - 1
    cascade_full_error = int(np.max(np.abs(cascade_vectors[full_index] - s_values)))

    cascade_rows = []
    for n in checkpoints:
        full_v = int(np.dot(s_values[:n], s_values[:n]))
        v1 = int(np.dot(cascade_vectors[0][:n], cascade_vectors[0][:n]))
        for j, threshold in enumerate(thresholds):
            r = cascade_vectors[j][:n]
            v = int(np.dot(r, r))
            cascade_rows.append(
                [n, threshold, int(r[n - 1]), v, v / n**3, v / v1, v / full_v]
            )

    write_csv(
        out / "cofactor_cascade.csv",
        ["N", "C", "R_C_X_N", "V_C", "V_C_over_N3", "V_C_over_V_1",
         "V_C_over_V_total"],
        cascade_rows,
    )

    # Dyadic cofactor Gram matrices and the high-sector restriction |Y|>16n.
    all_block_vectors = np.cumsum(bins[:, 1:], axis=1, dtype=np.int64)
    high_lambda = 16.0
    high_bins = cofactor_block_bins_high(mu, lpf, nmax, levels, high_lambda)
    high_block_vectors = np.cumsum(high_bins[:, 1:], axis=1, dtype=np.int64)
    write_dyadic_gram_outputs(out, "all", all_block_vectors, checkpoints, mu, max_observed_c)
    write_dyadic_gram_outputs(out, "high_lambda_16", high_block_vectors, checkpoints, mu, max_observed_c)

    lambdas = np.array([1.0, 2.0, 4.0, 8.0, 16.0], dtype=np.float64)
    (
        total_counts,
        odd_counts,
        even_counts,
        total_incidence,
        odd_incidence,
        even_incidence,
    ) = low_height_stats(mu, lpf, nmax, lambdas)

    low_rows = []
    start_n = 128 if nmax >= 128 else 1
    for j, lam in enumerate(lambdas):
        dmax = int(math.floor(lam))
        general_bound = 0 if lam <= 1.0 else dmax
        odd_bound = int(math.floor(lam / 2.0))
        even_bound = (dmax + 1) // 2
        lifetime_factor = 1 + 2 * lam

        low_rows.append(
            [
                lam, start_n, nmax,
                general_bound,
                int(total_counts[j, start_n:].max()),
                int(np.argmax(total_counts[j, start_n:]) + start_n),
                odd_bound,
                int(odd_counts[j, start_n:].max()),
                even_bound,
                int(even_counts[j, start_n:].max()),
                general_bound * lifetime_factor,
                int(total_incidence[j, start_n:].max()),
                int(np.argmax(total_incidence[j, start_n:]) + start_n),
                odd_bound * lifetime_factor,
                int(odd_incidence[j, start_n:].max()),
                even_bound * lifetime_factor,
                int(even_incidence[j, start_n:].max()),
            ]
        )

    write_csv(
        out / "low_height_diagnostics.csv",
        [
            "lambda", "n_min", "n_max", "general_count_bound",
            "observed_max_total_count", "n_at_max_total_count", "odd_count_bound",
            "observed_max_odd_count", "even_count_bound", "observed_max_even_count",
            "general_incidence_bound", "observed_max_total_incidence",
            "n_at_max_total_incidence", "odd_incidence_bound",
            "observed_max_odd_incidence", "even_incidence_bound",
            "observed_max_even_incidence",
        ],
        low_rows,
    )

    major_arc_summary, major_arc_rows = major_arc_regression(primes)
    write_csv(
        out / "major_arc_regression.csv",
        ["check", "param_1", "param_2", "value", "expected",
         "deviation_or_count", "kind"],
        major_arc_rows,
    )

    local_bases = [n for n in (128, 256, 512, 1024, 2048) if 2 * n <= nmax]
    local_rows = []
    for base in local_bases:
        ratio, start, h, energy = worst_local_ratio(s_values, base)
        local_rows.append([base, ratio, ratio / base**0.10, start, h, energy])

    slope = float("nan")
    if len(local_rows) >= 2:
        xx = np.log(np.array([row[0] for row in local_rows], dtype=np.float64))
        yy = np.log(np.array([row[1] for row in local_rows], dtype=np.float64))
        slope = float(np.polyfit(xx, yy, 1)[0])

    write_csv(
        out / "local_ratio_diagnostics.csv",
        ["dyadic_base_N", "worst_local_ratio", "ratio_over_N_0p10",
         "maximizing_start", "maximizing_H", "window_energy"],
        local_rows,
    )

    summary = f"""Square-prefix squared-complex-space reproducibility run v3
N_max: {nmax}
X_max: {xmax}
prime_count: {len(primes)}
squarefree_sources_m_ge_2: {source_count}
max_observed_canonical_cofactor: {max_observed_c}
max_dyadic_cofactor_threshold: {thresholds[-1]}

Exact checks
max_abs_S_minus_A_plus_T: {int(np.max(np.abs(at_errors)))}
nonzero_prefix_identity_errors: {int(np.count_nonzero(at_errors))}
norm_identity_violations: {norm_bad}
cofactor_curve_identity_violations: {curve_bad}
height_lifetime_violations: {lifetime_bad}
prime_square_mod24_violations_2000_4000: {major_arc_summary['prime_square_mod24_violations']}
old_modulus_3_factor_abs: {major_arc_summary['old_modulus_3_factor_abs']:g}
corrected_modulus_6_factor_abs: {major_arc_summary['corrected_modulus_6_factor_abs']:g}
cofactor_cascade_full_error: {cascade_full_error}

Local-ratio log-log slope: {slope:.12f}

Interpretation
R_C(x)=1-sum_{{c<=C}} mu(c)[pi(x/c)-pi(Pplus(c))].
At the largest dyadic threshold, R_C(X_n)=M(X_n) exactly for all tested n.
The c=1 curve alone has order N^5/log^2(N) energy; the cascade records how
successive cofactor scales cancel that coherent prime contribution.
Of {major_arc_summary['toy_prime_count']} primes in (2000,4000], all satisfy
q^2=1 (mod 24); all eight rational test frequencies in major_arc_regression.csv
match the coherent prediction |S_prime(alpha)|={major_arc_summary['toy_prime_count']}
({major_arc_summary['toy_prime_resonance_violations']} violations). The old
modulus-3 factor vanishes as an artifact of an ill-defined phase; the
corrected modulus-6 factor has unit magnitude.
"""
    (out / "run_summary.txt").write_text(summary, encoding="utf-8")
    print(summary)


if __name__ == "__main__":
    main()
