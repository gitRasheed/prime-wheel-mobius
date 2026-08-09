#!/usr/bin/env python3
"""Run preregistered falsification gates for the unresolved analytic layer.

Gate 1 verifies the manuscript's exact half-square boundary error over dyadic
packet scales and measures cumulative dyadic growth.

Gate 2 inventories the exact formalized rational phase
    exp(2*pi*i*a*(q^2-c^2)/(2r))
on canonical squarefree channels in one square block, comparing modes below
and above the fixed denominator cutoff r=60.

Gate 3 measures scale growth of the strongest phase modes and compares the
Möbius weighting with constant and deterministically shuffled signs.

These are diagnostics. In particular, Gate 2 is a raw reduced-mode inventory,
not an orthogonal projection norm and therefore not a proof of a leakage bound.
"""

from __future__ import annotations

import argparse
import csv
import importlib.util
import json
import math
from pathlib import Path

import numpy as np


def load_repro_module(path: Path):
    spec = importlib.util.spec_from_file_location("primorial_block_validation", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Unable to load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def write_csv(path: Path, header: list[str], rows: list[list[object]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(header)
        writer.writerows(rows)


def half_square(k: int) -> int:
    return (k * k) // 2


def gate1_boundary(mu: np.ndarray, out: Path, mmax: int) -> dict:
    mu64 = mu.astype(np.int64)
    mu_prefix = np.cumsum(mu64, dtype=np.int64)

    kmax = (len(mu) - 4) // 4
    k = np.arange(kmax + 1, dtype=np.int64)
    cell = mu64[4 * k + 1] - mu64[2 * k + 1] + mu64[4 * k + 3]
    cell_prefix = np.concatenate((np.array([0], dtype=np.int64), np.cumsum(cell)))

    rows: list[list[object]] = []
    energies: list[float] = []
    scales: list[float] = []
    cumulative_energy = 0
    all_pass = True

    m = 16
    while m <= mmax:
        errors = np.empty(m, dtype=np.int64)
        for offset, u in enumerate(range(m, 2 * m)):
            x0 = half_square(u)
            x1 = half_square(u + m)
            raw = int(mu_prefix[x1] - mu_prefix[x0])
            lo = (x0 + 3) // 4
            hi = x1 // 4
            compressed = int(cell_prefix[hi] - cell_prefix[lo])
            errors[offset] = raw - compressed

        energy = int(np.dot(errors, errors))
        max_abs = int(np.max(np.abs(errors)))
        cumulative_energy += energy
        passed = max_abs <= 3 and energy <= 9 * m
        all_pass = all_pass and passed
        rows.append([
            m,
            max_abs,
            energy,
            energy / m,
            9 * m,
            cumulative_energy,
            cumulative_energy / (m ** 2),
            cumulative_energy / (m ** 2.5),
            int(passed),
        ])
        if energy > 0:
            scales.append(float(m))
            energies.append(float(energy))
        m *= 2

    slope = float("nan")
    if len(scales) >= 2:
        slope = float(np.polyfit(np.log(scales), np.log(energies), 1)[0])

    write_csv(
        out / "gate1_boundary_scaling.csv",
        [
            "M", "max_abs_error", "boundary_energy", "energy_over_M",
            "proved_upper_9M", "cumulative_dyadic_energy",
            "cumulative_over_M2", "cumulative_over_M2p5", "pass_exact_bound",
        ],
        rows,
    )
    return {
        "pass": bool(all_pass),
        "largest_scale": mmax,
        "effective_energy_exponent": slope,
        "cumulative_energy": cumulative_energy,
        "max_abs_error": max(int(row[1]) for row in rows),
        "max_energy_over_M": max(float(row[3]) for row in rows),
    }


def canonical_block(mu: np.ndarray, lpf: np.ndarray, n: int, lam: float):
    lo = n * n
    hi = (n + 1) * (n + 1)
    m = np.arange(lo, hi, dtype=np.int64)
    weights = mu[lo:hi].astype(np.int64)
    keep = weights != 0
    m = m[keep]
    weights = weights[keep]
    q = lpf[m].astype(np.int64)
    c = m // q
    y2 = q * q - c * c
    high = np.abs(y2) > 2.0 * lam * n
    return y2[high], weights[high], c[high], q[high]


def reduced_numerators(r: int) -> list[int]:
    return [a for a in range(r) if math.gcd(a, r) == 1]


def mode_inventory(y2: np.ndarray, weights: np.ndarray, rmax: int):
    rows: list[dict[str, object]] = []
    for r in range(1, rmax + 1):
        modulus = 2 * r
        residues = np.mod(y2, modulus).astype(np.int64)
        hist = np.bincount(residues, weights=weights, minlength=modulus)
        transform = np.fft.fft(hist)
        for a in reduced_numerators(r):
            value = complex(transform[a])
            rows.append({
                "a": a,
                "r": r,
                "abs_sum": abs(value),
                "energy": abs(value) ** 2,
                "real": value.real,
                "imag": value.imag,
            })
    return rows


def summarize_modes(rows: list[dict[str, object]], source_count: int, cutoff: int):
    nonzero = [row for row in rows if not (row["a"] == 0 and row["r"] == 1)]
    low = [row for row in nonzero if int(row["r"]) <= cutoff]
    tail = [row for row in nonzero if int(row["r"]) > cutoff]

    def stats(part):
        energies = np.array([float(row["energy"]) for row in part], dtype=float)
        magnitudes = np.array([float(row["abs_sum"]) for row in part], dtype=float)
        return {
            "mode_count": len(part),
            "total_raw_energy": float(energies.sum()),
            "mean_energy_per_mode": float(energies.mean()) if len(part) else 0.0,
            "max_abs_sum": float(magnitudes.max()) if len(part) else 0.0,
            "max_coherence": float(magnitudes.max() / source_count) if len(part) and source_count else 0.0,
            "median_coherence": float(np.median(magnitudes) / source_count) if len(part) and source_count else 0.0,
        }

    low_stats = stats(low)
    tail_stats = stats(tail)
    ratio = tail_stats["max_coherence"] / low_stats["max_coherence"] if low_stats["max_coherence"] > 0 else float("inf")
    mean_ratio = tail_stats["mean_energy_per_mode"] / low_stats["mean_energy_per_mode"] if low_stats["mean_energy_per_mode"] > 0 else float("inf")
    passed = ratio < 0.25 and mean_ratio < 0.25
    return {
        "low": low_stats,
        "tail": tail_stats,
        "tail_to_low_max_coherence": ratio,
        "tail_to_low_mean_energy": mean_ratio,
        "proxy_pass": bool(passed),
    }


def gate2_cutoff(mu, lpf, out: Path, n_values, lam: float, rmax: int, cutoff: int):
    summary: dict[str, object] = {}
    csv_rows: list[list[object]] = []
    top_rows: list[list[object]] = []

    for n in n_values:
        y2, weights, _, _ = canonical_block(mu, lpf, n, lam)
        rows = mode_inventory(y2, weights, rmax)
        stats = summarize_modes(rows, len(weights), cutoff)
        summary[str(n)] = {"high_squarefree_sources": int(len(weights)), **stats}

        by_r: dict[int, list[dict[str, object]]] = {}
        for row in rows:
            by_r.setdefault(int(row["r"]), []).append(row)
        cumulative = 0.0
        for r in range(1, rmax + 1):
            group = by_r[r]
            raw_energy = float(sum(float(row["energy"]) for row in group))
            mean_energy = raw_energy / len(group)
            max_abs = max(float(row["abs_sum"]) for row in group)
            cumulative += raw_energy
            csv_rows.append([n, len(weights), r, len(group), raw_energy, mean_energy, max_abs, max_abs / len(weights), cumulative])

        ranked = sorted(
            [row for row in rows if not (row["a"] == 0 and row["r"] == 1)],
            key=lambda row: float(row["abs_sum"]), reverse=True,
        )[:30]
        for rank, row in enumerate(ranked, start=1):
            top_rows.append([n, rank, row["a"], row["r"], row["abs_sum"], float(row["abs_sum"]) / len(weights), "low" if int(row["r"]) <= cutoff else "tail"])

    write_csv(out / "gate2_cutoff_sensitivity.csv", ["N", "high_squarefree_sources", "r", "reduced_mode_count", "raw_mode_energy", "mean_energy_per_mode", "max_abs_sum", "max_coherence", "cumulative_raw_energy"], csv_rows)
    write_csv(out / "gate2_top_modes.csv", ["N", "rank", "a", "r", "abs_sum", "coherence", "cutoff_region"], top_rows)
    return summary


def evaluate_fixed_mode(y2, weights, a: int, r: int) -> complex:
    angle = -2.0j * np.pi * a * np.mod(y2, 2 * r) / (2 * r)
    return complex(np.sum(weights * np.exp(angle)))


def gate3_scaling(mu, lpf, out: Path, n_values, lam: float, gate2_summary_path: Path):
    with gate2_summary_path.open("r", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        rows = [row for row in reader if int(row["N"]) == max(n_values)]
    rows.sort(key=lambda row: float(row["coherence"]), reverse=True)

    selected: list[tuple[int, int, str]] = []
    for region in ("low", "tail"):
        count = 0
        for row in rows:
            if row["cutoff_region"] != region:
                continue
            pair = (int(row["a"]), int(row["r"]), region)
            if pair not in selected:
                selected.append(pair)
                count += 1
            if count == 5:
                break

    rng = np.random.default_rng(20260724)
    output_rows: list[list[object]] = []
    mode_series: dict[tuple[int, int, str], list[tuple[float, float]]] = {mode: [] for mode in selected}

    for n in n_values:
        y2, weights, _, _ = canonical_block(mu, lpf, n, lam)
        ones = np.ones_like(weights)
        shuffled = rng.permutation(weights)
        for a, r, region in selected:
            v_mu = evaluate_fixed_mode(y2, weights, a, r)
            v_one = evaluate_fixed_mode(y2, ones, a, r)
            v_shuffle = evaluate_fixed_mode(y2, shuffled, a, r)
            output_rows.append([n, len(weights), a, r, region, abs(v_mu), abs(v_mu) / len(weights), abs(v_one), abs(v_one) / len(weights), abs(v_shuffle), abs(v_shuffle) / len(weights)])
            if abs(v_mu) > 0:
                mode_series[(a, r, region)].append((float(n), abs(v_mu)))

    slopes = []
    for (a, r, region), series in mode_series.items():
        slope = float("nan")
        if len(series) >= 2:
            slope = float(np.polyfit(np.log([x for x, _ in series]), np.log([y for _, y in series]), 1)[0])
        slopes.append({"a": a, "r": r, "region": region, "growth_exponent": slope})

    write_csv(out / "gate3_mode_scaling.csv", ["N", "source_count", "a", "r", "cutoff_region", "mobius_abs", "mobius_coherence", "constant_abs", "constant_coherence", "shuffled_abs", "shuffled_coherence"], output_rows)
    write_csv(out / "gate3_growth_exponents.csv", ["a", "r", "cutoff_region", "growth_exponent"], [[row["a"], row["r"], row["region"], row["growth_exponent"]] for row in slopes])
    return {"selected_modes": slopes}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--nmax", type=int, default=4096)
    parser.add_argument("--boundary-mmax", type=int, default=2048)
    parser.add_argument("--rmax", type=int, default=240)
    parser.add_argument("--cutoff", type=int, default=60)
    parser.add_argument("--lambda-high", type=float, default=16.0)
    parser.add_argument("--out", type=Path, default=Path("analytic_gate_results"))
    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)

    script_dir = Path(__file__).resolve().parent
    repro = load_repro_module(script_dir / "primorial_block_validation.py")

    max_half_square = half_square(3 * args.boundary_mmax) + 4
    max_square_prefix = (args.nmax + 1) ** 2 - 1
    sieve_max = max(max_half_square, max_square_prefix)
    mu, _spf, lpf, _primes = repro.linear_sieve_mu_lpf(sieve_max)

    gate1 = gate1_boundary(mu, args.out, args.boundary_mmax)
    n_values = [n for n in (256, 512, 1024, 2048, 4096) if n <= args.nmax]
    gate2 = gate2_cutoff(mu, lpf, args.out, n_values, args.lambda_high, args.rmax, args.cutoff)
    gate3 = gate3_scaling(mu, lpf, args.out, n_values, args.lambda_high, args.out / "gate2_top_modes.csv")

    terminal = gate2[str(max(n_values))]
    results = {
        "parameters": {"nmax": args.nmax, "boundary_mmax": args.boundary_mmax, "rmax": args.rmax, "fixed_cutoff": args.cutoff, "lambda_high": args.lambda_high, "sieve_max": sieve_max},
        "gate1_boundary": gate1,
        "gate2_cutoff_terminal": terminal,
        "gate2_all_scales": gate2,
        "gate3_scaling": gate3,
        "interpretation_limits": [
            "Gate 1 tests the explicitly defined half-square endpoint error E_{u,M}; it does not equal the full unresolved block forcing f_M.",
            "Gate 2 is a raw reduced-mode inventory, not an orthogonal projection leakage norm.",
            "Gate 3 is finite-scale evidence and does not prove or disprove an asymptotic theorem.",
        ],
    }
    (args.out / "gate_results.json").write_text(json.dumps(results, indent=2, sort_keys=True), encoding="utf-8")

    report = [
        "# Analytic kill-gate results", "",
        f"Parameters: Nmax={args.nmax}, boundary Mmax={args.boundary_mmax}, Rmax={args.rmax}, fixed cutoff={args.cutoff}, high threshold={args.lambda_high}n.", "",
        "## Gate 1 — half-square floor-boundary accumulation", "",
        f"Exact bound pass: **{gate1['pass']}**.",
        f"Maximum |E|: {gate1['max_abs_error']} (proved ceiling 3).",
        f"Largest boundary energy/M: {gate1['max_energy_over_M']:.6g} (proved ceiling 9).",
        f"Empirical boundary-energy exponent: {gate1['effective_energy_exponent']:.6f}.", "",
        "This gate addresses the manuscript's explicit endpoint error E_{u,M}, not the full unresolved forcing vector.", "",
        "## Gate 2 — fixed conductor cutoff proxy", "",
        f"At N={max(n_values)}, high squarefree sources: {terminal['high_squarefree_sources']}.",
        f"Tail/low maximum coherence ratio: {terminal['tail_to_low_max_coherence']:.6g}.",
        f"Tail/low mean mode-energy ratio: {terminal['tail_to_low_mean_energy']:.6g}.",
        f"Preregistered proxy pass: **{terminal['proxy_pass']}**.", "",
        "This is not the norm of an orthogonal major-arc projection. It asks the weaker falsification question: do comparably coherent reduced modes remain above r=60?", "",
        "## Gate 3 — strongest-mode scaling", "",
    ]
    for row in gate3["selected_modes"]:
        report.append(f"- (a,r)=({row['a']},{row['r']}) [{row['region']}]: fitted |sum| exponent {row['growth_exponent']:.6f}")
    report.extend(["", "Detailed Möbius/constant/shuffled comparisons are in gate3_mode_scaling.csv.", "", "## Hard conclusion boundary", "", "A failure of Gate 2 blocks any claim that the fixed r<=60 cutoff has empirically isolated all coherent rational modes. A pass would still not prove the leakage theorem. Gate 1 can pass while the full forcing estimate remains completely open."])
    (args.out / "gate_report.md").write_text("\n".join(report) + "\n", encoding="utf-8")
    print("\n".join(report))


if __name__ == "__main__":
    main()
