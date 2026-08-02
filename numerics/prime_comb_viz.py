#!/usr/bin/env python3
"""Seeded prime-comb Moebius reconstruction over a complete wheel block.

One continuous path, each prime used exactly once, and nothing after the last
prime.

    Frame 0        uniform seed J_0(n) = s, with s = -1 by default.
    Frames 1..46   apply the square-sensitive local operator, one prime at a
                   time, for every prime p <= W:

                       u_p(n) = 0   if p^2 | n        (kill channel)
                               -1   if p || n         (flip channel)
                                1   if p does not divide n,

                   updating J <- J * u_p. White sites appear exactly when p^2 | n
                   and are permanent, since zero is absorbing under a
                   multiplicative operator. For W = 210 every white site is in
                   place by p = 13, because 17^2 > 210, but the later primes keep
                   acting on the surviving signs.

Every n <= W is W-smooth, so after the last prime the state is exactly

    sigma(n) = s * mu(s_W(n)) = s * mu(n),        B = s * M(W),

and the path ends there. With s = -1 the limit is -mu, the exact negative of the
target; with --seed +1 it is mu itself. Either way the object on display is the
prime-by-prime path B_j and its distance from that limit, which is what a bound
has to control. Neither the signed sum nor the agreement count is monotone.

Diagnostic and expository only. Not a Lean certificate and not a proof.
"""

from __future__ import annotations

import argparse
import csv
import math
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

import matplotlib

matplotlib.use("Agg")
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap
from matplotlib.lines import Line2D
from matplotlib.patches import Patch


STEELBLUE = "#4682B4"
WHITE = "#FFFFFF"
CYAN = "#00FFFF"
RED = "red"


# ---------------------------------------------------------------------------
# Arithmetic
# ---------------------------------------------------------------------------


def get_primes_upto(n: int) -> list[int]:
    """Return all primes <= n by a simple sieve."""
    if n < 2:
        return []

    sieve = np.ones(n + 1, dtype=bool)
    sieve[:2] = False
    for p in range(2, math.isqrt(n) + 1):
        if sieve[p]:
            sieve[p * p : n + 1 : p] = False
    return np.flatnonzero(sieve).astype(int).tolist()


def compute_mobius(limit: int) -> np.ndarray:
    """Compute mu(1), ..., mu(limit) independently by a linear sieve."""
    mu = np.zeros(limit + 1, dtype=int)
    mu[1] = 1
    primes: list[int] = []
    is_composite = np.zeros(limit + 1, dtype=bool)

    for n in range(2, limit + 1):
        if not is_composite[n]:
            primes.append(n)
            mu[n] = -1

        for p in primes:
            value = n * p
            if value > limit:
                break
            is_composite[value] = True
            if n % p == 0:
                mu[value] = 0
                break
            mu[value] = -mu[n]

    return mu[1:]


# ---------------------------------------------------------------------------
# Frame construction
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class Frame:
    state: np.ndarray
    phase: str
    prime: Optional[int]
    flipped: np.ndarray
    label: str
    title: str
    signed_sum: int
    agreement_mu: int
    agreement_neg_mu: int
    white_count: int
    killed_count: int
    flipped_count: int
    channel_mass_before: int
    delta_signed_sum: int


def build_frames(limit: int, mu_true: np.ndarray, seed: int) -> list[Frame]:
    """Seed uniformly, then comb every prime p <= limit exactly once."""
    numbers = np.arange(1, limit + 1)
    empty = np.zeros(limit, dtype=bool)

    def snapshot(state, phase, prime, flipped, label, title, **extra) -> Frame:
        return Frame(
            state=state.copy(),
            phase=phase,
            prime=prime,
            flipped=flipped.copy(),
            label=label,
            title=title,
            signed_sum=int(state.sum()),
            agreement_mu=int(np.count_nonzero(state == mu_true)),
            agreement_neg_mu=int(np.count_nonzero(state == -mu_true)),
            white_count=int(np.count_nonzero(state == 0)),
            killed_count=extra.get("killed_count", 0),
            flipped_count=int(np.count_nonzero(flipped)),
            channel_mass_before=extra.get("channel_mass_before", 0),
            delta_signed_sum=extra.get("delta_signed_sum", 0),
        )

    state = np.full(limit, seed, dtype=int)
    frames = [snapshot(state, "seed", None, empty, "seed",
                       f"Seed: uniform J0(n) = {seed:+d}")]

    comb_primes = get_primes_upto(limit)
    assert len(set(comb_primes)) == len(comb_primes), "a prime is only used once"

    for p in comb_primes:
        alive = state != 0
        kill = alive & (numbers % (p * p) == 0)
        flip = alive & ~kill & (numbers % p == 0)

        before = int(state.sum())
        kill_mass = int(state[kill].sum())
        flip_mass = int(state[flip].sum())

        state[kill] = 0
        state[flip] *= -1

        delta = int(state.sum()) - before
        # Kills remove their mass outright; flips reverse theirs.
        assert delta == -kill_mass - 2 * flip_mass, f"channel accounting failed at p={p}"

        frames.append(
            snapshot(
                state,
                "comb",
                p,
                flip,
                str(p),
                f"Prime comb p = {p}: kill p^2 | n, flip p || n",
                killed_count=int(np.count_nonzero(kill)),
                channel_mass_before=flip_mass,
                delta_signed_sum=delta,
            )
        )

    # After every prime has acted once the state is exactly seed * mu.
    assert np.array_equal(state, seed * mu_true), "comb path did not land on seed * mu"

    expected = 1 + len(comb_primes)
    assert len(frames) == expected, f"expected {expected} frames, built {len(frames)}"
    return frames


# ---------------------------------------------------------------------------
# Grid helpers
# ---------------------------------------------------------------------------


def padded_grid(values: np.ndarray, width: int) -> np.ndarray:
    """Pad a 1-D array with NaN and reshape it for display."""
    height = math.ceil(values.size / width)
    padded = np.full(height * width, np.nan, dtype=float)
    padded[: values.size] = values
    return padded.reshape(height, width)


def padded_mask(mask: np.ndarray, width: int) -> np.ndarray:
    """Pad a Boolean mask with False and reshape it for display."""
    height = math.ceil(mask.size / width)
    padded = np.zeros(height * width, dtype=bool)
    padded[: mask.size] = mask
    return padded.reshape(height, width)


def combine_grids(left: np.ndarray, right: np.ndarray, gap: int = 2) -> np.ndarray:
    """Place two equally shaped grids side by side with a NaN divider gap."""
    rows, cols = left.shape
    combined = np.full((rows, cols * 2 + gap), np.nan, dtype=float)
    combined[:, :cols] = left
    combined[:, cols + gap :] = right
    return combined


# ---------------------------------------------------------------------------
# Output
# ---------------------------------------------------------------------------


def write_metrics_csv(frames: list[Frame], target_sum: int, seed: int, path: Path) -> None:
    """Write the entire path for independent inspection."""
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(
            [
                "frame",
                "phase",
                "prime",
                "signed_sum",
                "target_MX",
                "limit_sum",
                "distance_to_limit",
                "agreement_with_limit",
                "white_count",
                "killed_sites",
                "flipped_sites",
                "flip_channel_mass_before",
                "delta_signed_sum",
            ]
        )
        for index, frame in enumerate(frames):
            writer.writerow(
                [
                    index,
                    frame.phase,
                    "" if frame.prime is None else frame.prime,
                    frame.signed_sum,
                    target_sum,
                    seed * target_sum,
                    abs(frame.signed_sum - seed * target_sum),
                    frame.agreement_neg_mu if seed == -1 else frame.agreement_mu,
                    frame.white_count,
                    frame.killed_count,
                    frame.flipped_count,
                    frame.channel_mass_before,
                    frame.delta_signed_sum,
                ]
            )


def render_outputs(
    limit: int,
    grid_width: int,
    frames: list[Frame],
    mu_true: np.ndarray,
    output_dir: Path,
    fps: int,
    dpi: int,
    hold_seconds: float,
    seed: int,
) -> tuple[Path, Path, Path, Path]:
    output_dir.mkdir(parents=True, exist_ok=True)

    gif_path = output_dir / f"prime_comb_mobius_W{limit}.gif"
    final_png_path = output_dir / f"prime_comb_mobius_W{limit}_final.png"
    path_png_path = output_dir / f"prime_comb_mobius_W{limit}_path.png"
    csv_path = output_dir / f"prime_comb_mobius_W{limit}_metrics.csv"

    target_sum = int(mu_true.sum())
    limit_sum = seed * target_sum
    limit_name = 'mu' if seed == 1 else '-mu'
    write_metrics_csv(frames, target_sum, seed, csv_path)

    true_grid = padded_grid(mu_true, grid_width)
    gap = 2

    cmap = ListedColormap([STEELBLUE, WHITE, CYAN])
    cmap.set_bad("#E6E6E6")
    norm = plt.Normalize(-1.5, 1.5)

    legend_handles = [
        Patch(facecolor=STEELBLUE, edgecolor="black", label="-1"),
        Patch(facecolor=WHITE, edgecolor="black", label="0 (square factor)"),
        Patch(facecolor=CYAN, edgecolor="black", label="+1"),
        Line2D(
            [0],
            [0],
            marker="o",
            linestyle="none",
            markerfacecolor="none",
            markeredgecolor=RED,
            markeredgewidth=2,
            markersize=8,
            label="Sites flipped by the current prime",
        ),
    ]

    labels = [f.label for f in frames]
    sums = np.array([f.signed_sum for f in frames], dtype=int)
    agree_mu = np.array([f.agreement_mu for f in frames], dtype=int)
    agree_limit = np.array(
        [f.agreement_neg_mu if seed == -1 else f.agreement_mu for f in frames], dtype=int
    )
    count = len(frames)

    sum_low = min(int(sums.min()), limit_sum)
    sum_high = max(int(sums.max()), limit_sum)
    span = max(sum_high - sum_low, 1)
    agree_high = max(int(agree_limit.max()), int(np.abs(sums - limit_sum).max()))

    stride = max(1, count // 12)
    last = count - 1
    ticks = [i for i in range(0, count, stride) if last - i >= stride]
    ticks.append(last)

    fig = plt.figure(figsize=(16, 10.5))
    fig.set_dpi(dpi)
    gs = fig.add_gridspec(2, 2, height_ratios=[3.2, 1.35], hspace=0.62, wspace=0.22)
    ax_grid = fig.add_subplot(gs[0, :])
    ax_sum = fig.add_subplot(gs[1, 0])
    ax_agree = fig.add_subplot(gs[1, 1])
    footer = fig.text(0.5, 0.012, "", ha="center", va="bottom", fontsize=10, color="#333333")

    def draw_grid(frame: Frame) -> None:
        ax_grid.clear()
        combined = combine_grids(padded_grid(frame.state, grid_width), true_grid, gap=gap)

        ax_grid.imshow(
            np.ma.masked_invalid(combined),
            cmap=cmap,
            norm=norm,
            interpolation="none",
            aspect="equal",
        )

        if frame.flipped_count:
            rows, cols = np.where(padded_mask(frame.flipped, grid_width))
            ax_grid.scatter(
                cols,
                rows,
                marker="o",
                s=48,
                facecolors="none",
                edgecolors=RED,
                linewidths=1.8,
            )

        ax_grid.axvline(grid_width + (gap - 1) / 2, linewidth=1.5)
        ax_grid.axis("off")

        ax_grid.text(
            0.24,
            -0.035,
            "Seeded prime-comb state",
            transform=ax_grid.transAxes,
            ha="center",
            va="top",
            fontsize=13,
            fontweight="bold",
        )
        ax_grid.text(
            0.76,
            -0.035,
            "Exact Moebius mu(n)",
            transform=ax_grid.transAxes,
            ha="center",
            va="top",
            fontsize=13,
            fontweight="bold",
        )

        if frame.phase == "comb":
            operation_line = (
                f"killed={frame.killed_count}, flipped={frame.flipped_count}, "
                f"C_p before flip={frame.channel_mass_before:+d}, "
                f"Delta B={frame.delta_signed_sum:+d}"
            )
        else:
            operation_line = f"uniform seed on all {limit} sites; no prime has acted yet"

        ax_grid.set_title(
            f"{frame.title}\n"
            f"B={frame.signed_sum:+d}, limit {limit_name} has B={limit_sum:+d}, "
            f"|B-limit|={abs(frame.signed_sum - limit_sum)}, "
            f"agreement with {limit_name}="
            f"{frame.agreement_neg_mu if seed == -1 else frame.agreement_mu}/{limit}\n"
            f"{operation_line}",
            fontsize=13.5,
            pad=18,
        )
        ax_grid.legend(
            handles=legend_handles,
            loc="upper center",
            bbox_to_anchor=(0.5, -0.13),
            ncol=4,
            frameon=True,
            fontsize=9.5,
            handlelength=1.4,
            columnspacing=1.4,
        )

    def style_axis(axis) -> None:
        axis.set_xlim(-0.6, count - 0.4)
        axis.set_xticks(ticks)
        axis.set_xticklabels([labels[i] for i in ticks], rotation=45, ha="right")
        axis.set_xlabel("Prime just applied")
        axis.grid(True, alpha=0.25)

    def draw_paths(index: int) -> None:
        x = np.arange(index + 1)

        ax_sum.clear()
        ax_sum.plot(x, sums[: index + 1], marker="o", markersize=3, color="#1f5fa8")
        ax_sum.axhline(
            limit_sum,
            linestyle="--",
            linewidth=1.3,
            color="#c0392b",
            label=f"limit: B = {limit_sum:+d}",
        )
        ax_sum.set_title("Signed sum along the prime path")
        ax_sum.set_ylabel("B")
        ax_sum.set_ylim(sum_low - 0.08 * span, sum_high + 0.34 * span)
        style_axis(ax_sum)
        ax_sum.legend(loc="upper right", fontsize=8.5, framealpha=0.9)

        ax_agree.clear()
        ax_agree.plot(
            x,
            agree_limit[: index + 1],
            marker="o",
            markersize=3,
            color="#2e8b57",
            label=f"agreement with {limit_name}",
        )
        ax_agree.plot(
            x,
            np.abs(sums[: index + 1] - limit_sum),
            marker=".",
            markersize=3,
            color="#c0392b",
            label="|B - limit|",
        )
        ax_agree.set_title("No monotonicity is assumed")
        ax_agree.set_ylabel("Count / distance")
        ax_agree.set_ylim(-0.04 * agree_high, 1.30 * agree_high)
        style_axis(ax_agree)
        ax_agree.legend(loc="upper left", fontsize=8.5, framealpha=0.9)

    def update(index: int):
        frame = frames[index]
        draw_grid(frame)
        draw_paths(index)
        phase_name = {
            "seed": "seed",
            "comb": "prime comb",
        }[frame.phase]
        current = "-" if frame.prime is None else str(frame.prime)
        footer.set_text(
            f"phase = {phase_name}   |   white sites = {frame.white_count}   |   "
            f"current prime = {current}   |   killed = {frame.killed_count}   |   "
            f"flipped = {frame.flipped_count}"
        )
        return []

    # Hold the exact final frame by repeating it: PillowWriter has one duration
    # for every frame, so the dwell has to come from repeated indices.
    hold_repeats = max(1, round(hold_seconds * fps))
    sequence = list(range(len(frames))) + [len(frames) - 1] * (hold_repeats - 1)

    ani = animation.FuncAnimation(
        fig,
        update,
        frames=sequence,
        interval=max(1, int(1000 / fps)),
        repeat_delay=2200,
        blit=False,
    )
    ani.save(gif_path, writer=animation.PillowWriter(fps=fps))
    plt.close(fig)

    # Final exact state.
    final = frames[-1]
    fig_final, ax_final = plt.subplots(figsize=(15, 7.8))
    ax_final.imshow(
        np.ma.masked_invalid(
            combine_grids(padded_grid(final.state, grid_width), true_grid, gap=gap)
        ),
        cmap=cmap,
        norm=norm,
        interpolation="none",
        aspect="equal",
    )
    ax_final.axvline(grid_width + (gap - 1) / 2, linewidth=1.5)
    ax_final.axis("off")
    ax_final.set_title(
        f"After every prime p <= {limit} has acted once: the state is exactly "
        f"{limit_name}(n)\n"
        f"agreement={agree_limit[-1]}/{limit}, B={final.signed_sum:+d} = "
        f"{'' if seed == 1 else '-'}M({limit})",
        fontsize=15,
        pad=18,
    )
    for x_pos, text in ((0.24, "Seeded prime-comb state"), (0.76, "Exact Moebius mu(n)")):
        ax_final.text(
            x_pos,
            -0.035,
            text,
            transform=ax_final.transAxes,
            ha="center",
            va="top",
            fontsize=13,
            fontweight="bold",
        )
    ax_final.legend(
        handles=legend_handles[:3],
        loc="upper center",
        bbox_to_anchor=(0.5, -0.13),
        ncol=3,
        frameon=True,
        fontsize=10,
    )
    fig_final.savefig(final_png_path, dpi=170, bbox_inches="tight")
    plt.close(fig_final)

    # Static path diagnostic.
    fig_path, axes = plt.subplots(2, 1, figsize=(13, 8), sharex=True)
    x_all = np.arange(count)
    axes[0].plot(x_all, sums, marker="o", markersize=3, color="#1f5fa8")
    axes[0].axhline(
        limit_sum,
        linestyle="--",
        linewidth=1.3,
        color="#c0392b",
        label=f"limit: B = {limit_sum:+d}",
    )
    axes[0].set_ylabel("Signed sum B")
    axes[0].set_title("Seeded prime-comb path: exact endpoint, non-monotone route")
    axes[0].grid(True, alpha=0.25)
    axes[0].legend(loc="best")

    axes[1].plot(
        x_all, agree_limit, marker="o", markersize=3, color="#2e8b57",
        label=f"agreement with {limit_name}"
    )
    axes[1].plot(
        x_all, np.abs(sums - limit_sum), marker=".", markersize=3, color="#c0392b",
        label="|B - limit|"
    )
    axes[1].set_ylabel("Count / distance")
    axes[1].set_xlabel("Prime just applied")
    axes[1].grid(True, alpha=0.25)
    axes[1].legend(loc="best")

    path_stride = max(1, count // 16)
    positions = [i for i in range(0, count, path_stride) if last - i >= path_stride]
    positions.append(last)
    axes[1].set_xticks(positions)
    axes[1].set_xticklabels([labels[i] for i in positions], rotation=45, ha="right")
    fig_path.tight_layout()
    fig_path.savefig(path_png_path, dpi=170, bbox_inches="tight")
    plt.close(fig_path)

    return gif_path, final_png_path, path_png_path, csv_path


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Animate the seeded prime-comb reconstruction of mu over a complete "
            "wheel block: uniform seed, then every prime exactly once."
        )
    )
    parser.add_argument("--limit", type=int, default=210, help="Wheel block W (default: 210).")
    parser.add_argument(
        "--grid-width", type=int, default=15, help="Cells per grid row (default: 15)."
    )
    parser.add_argument("--fps", type=int, default=2, help="GIF frames per second (default: 2).")
    parser.add_argument("--dpi", type=int, default=80, help="GIF render dpi (default: 80).")
    parser.add_argument(
        "--seed",
        type=int,
        choices=(-1, 1),
        default=-1,
        help="Uniform seed value. -1 (default) ends at -mu; +1 ends at mu.",
    )
    parser.add_argument(
        "--hold-seconds",
        type=float,
        default=2.0,
        help="Dwell on the exact final frame, in seconds (default: 2.0).",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("."),
        help="Directory for generated GIF, PNG, and CSV files.",
    )
    args = parser.parse_args()

    if args.limit < 4:
        parser.error("--limit must be at least 4")
    if args.grid_width < 1:
        parser.error("--grid-width must be at least 1")
    if args.fps < 1:
        parser.error("--fps must be at least 1")
    if args.dpi < 20:
        parser.error("--dpi must be at least 20")
    if args.hold_seconds < 0:
        parser.error("--hold-seconds must not be negative")
    return args


def main() -> None:
    args = parse_args()
    mu_true = compute_mobius(args.limit)
    frames = build_frames(args.limit, mu_true, args.seed)

    gif_path, final_png_path, path_png_path, csv_path = render_outputs(
        limit=args.limit,
        grid_width=args.grid_width,
        frames=frames,
        mu_true=mu_true,
        output_dir=args.output_dir,
        fps=args.fps,
        dpi=args.dpi,
        hold_seconds=args.hold_seconds,
        seed=args.seed,
    )

    target_sum = int(mu_true.sum())
    limit_sum = args.seed * target_sum
    comb = [f for f in frames if f.phase == "comb"]
    sums = [f.signed_sum for f in comb]
    monotone = all(a <= b for a, b in zip(sums, sums[1:])) or all(
        a >= b for a, b in zip(sums, sums[1:])
    )
    distances = [abs(value - limit_sum) for value in sums]
    last_white = next(f.prime for f in reversed(comb) if f.killed_count)
    hold_repeats = max(1, round(args.hold_seconds * args.fps))
    final_agreement = (
        frames[-1].agreement_neg_mu if args.seed == -1 else frames[-1].agreement_mu
    )

    print("Generated files:")
    for path in (gif_path, final_png_path, path_png_path, csv_path):
        print(f"  {path}")
    print()
    print(f"Frames: {len(frames)}  (1 seed + {len(comb)} primes, each used once)")
    print(f"  GIF holds the final frame {hold_repeats / args.fps:.1f}s")
    print(f"White (square-factor) sites : {frames[-1].white_count}")
    print(f"Squarefree support          : {args.limit - frames[-1].white_count}")
    print(f"Last prime to create white  : {last_white}")
    print()
    print(f"State after the last prime  : {'mu' if args.seed == 1 else '-mu'}, "
          f"agreement {final_agreement}/{args.limit}")
    print(f"  B = {frames[-1].signed_sum:+d}   (limit {limit_sum:+d})")
    print()
    print(f"Max |B - limit| along the path : {max(distances)}")
    print(f"Signed-sum path monotone       : {monotone}")


if __name__ == "__main__":
    main()
