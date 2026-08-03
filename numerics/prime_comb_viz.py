#!/usr/bin/env python3
"""Prime-comb reconstruction of the Moebius function on 1,...,W.

The visualization uses the intended prime-candidate interpretation:

    J_0(1) = +1,
    J_0(n) = -1 for 2 <= n <= W.

An untouched -1 means that no smaller prime has hit the site, so the site is
still a prime candidate. A prime p never acts on itself. It acts only on proper
multiples 2p, 3p, ... <= W:

* if p^2 divides n, kill the site permanently by setting it to 0;
* on the first proper-prime hit, leave the initial -1 unchanged;
* on every later distinct-prime hit, flip the surviving sign.

Therefore only primes p <= floor(W/2) can act. Every prime p > W/2 has no
proper multiple inside the block and is exactly inert. After the final active
prime, the state is exactly mu(n), and the signed sum is M(W).

For p > sqrt(W), no p^2-kill is possible. Writing K = floor(W/p), the proper
multiples are kp for 2 <= k <= K and the exact tail identity is

    C_p = sum_{k=2}^K mu(k) = M(K) - 1,
    Delta B_p = -2 C_p = 2(1 - M(K)).

This program is diagnostic and expository. It is not a proof certificate.
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
RED = "#D62728"
ORANGE = "#FF8C00"
BLACK = "#111111"
DIVIDER = "#B0B0B0"
PADDING = "#E6E6E6"


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
    """Compute mu(1),...,mu(limit) independently by a linear sieve."""
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


def mertens_prefix(mu_true: np.ndarray) -> np.ndarray:
    """Return an array M with M[k] = sum_{n<=k} mu(n), including M[0]=0."""
    return np.concatenate(([0], np.cumsum(mu_true, dtype=int)))


# ---------------------------------------------------------------------------
# Frame construction
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class Frame:
    state: np.ndarray
    phase: str
    prime: Optional[int]
    first_hit: np.ndarray
    flipped: np.ndarray
    killed: np.ndarray
    label: str
    title: str
    signed_sum: int
    agreement_mu: int
    white_count: int
    first_hit_count: int
    flipped_count: int
    killed_count: int
    flip_channel_mass_before: int
    kill_channel_mass_before: int
    delta_signed_sum: int
    tail_k: Optional[int]
    tail_expected_channel: Optional[int]


def build_frames(limit: int, mu_true: np.ndarray) -> tuple[list[Frame], list[int]]:
    """Build the intended prime-candidate comb using only p <= floor(W/2)."""
    numbers = np.arange(1, limit + 1)
    empty = np.zeros(limit, dtype=bool)
    M = mertens_prefix(mu_true)

    def snapshot(
        state: np.ndarray,
        phase: str,
        prime: Optional[int],
        first_hit: np.ndarray,
        flipped: np.ndarray,
        killed: np.ndarray,
        label: str,
        title: str,
        **extra: int | None,
    ) -> Frame:
        return Frame(
            state=state.copy(),
            phase=phase,
            prime=prime,
            first_hit=first_hit.copy(),
            flipped=flipped.copy(),
            killed=killed.copy(),
            label=label,
            title=title,
            signed_sum=int(state.sum()),
            agreement_mu=int(np.count_nonzero(state == mu_true)),
            white_count=int(np.count_nonzero(state == 0)),
            first_hit_count=int(np.count_nonzero(first_hit)),
            flipped_count=int(np.count_nonzero(flipped)),
            killed_count=int(np.count_nonzero(killed)),
            flip_channel_mass_before=int(extra.get("flip_channel_mass_before", 0) or 0),
            kill_channel_mass_before=int(extra.get("kill_channel_mass_before", 0) or 0),
            delta_signed_sum=int(extra.get("delta_signed_sum", 0) or 0),
            tail_k=extra.get("tail_k"),
            tail_expected_channel=extra.get("tail_expected_channel"),
        )

    # Prime-candidate seed: 1 is exceptional; every n >= 2 starts at -1.
    state = np.full(limit, -1, dtype=int)
    state[0] = 1

    # hit[n-1] means that some proper prime divisor has already acted on n.
    hit = np.zeros(limit, dtype=bool)
    hit[0] = True

    frames = [
        snapshot(
            state,
            "seed",
            None,
            empty,
            empty,
            empty,
            "seed",
            "Prime-candidate seed: J0(1)=+1 and J0(n)=-1 for n>=2",
        )
    ]

    active_bound = limit // 2
    comb_primes = get_primes_upto(active_bound)
    assert len(set(comb_primes)) == len(comb_primes), "a prime is used at most once"

    for p in comb_primes:
        alive = state != 0
        proper_multiple = (numbers >= 2 * p) & (numbers % p == 0)

        # Square divisibility kills permanently. The first non-square proper hit
        # identifies a composite but does not alter the initial -1. Only later
        # distinct-prime hits flip the sign.
        killed = alive & proper_multiple & (numbers % (p * p) == 0)
        first_hit = alive & proper_multiple & ~hit & ~killed
        flipped = alive & proper_multiple & hit & ~killed

        before = int(state.sum())
        kill_mass = int(state[killed].sum())
        flip_mass = int(state[flipped].sum())

        state[killed] = 0
        state[flipped] *= -1
        hit[proper_multiple] = True

        delta = int(state.sum()) - before
        assert delta == -kill_mass - 2 * flip_mass, (
            f"channel accounting failed at p={p}: "
            f"delta={delta}, kill_mass={kill_mass}, flip_mass={flip_mass}"
        )

        tail_k: Optional[int] = None
        tail_expected_channel: Optional[int] = None
        if p > math.isqrt(limit):
            tail_k = limit // p
            tail_expected_channel = int(M[tail_k] - 1)
            assert not np.any(killed), f"p={p}>sqrt(W) unexpectedly killed a site"
            assert flip_mass == tail_expected_channel, (
                f"tail identity failed at p={p}: C_p={flip_mass}, "
                f"M(floor(W/p))-1={tail_expected_channel}"
            )
            assert delta == -2 * tail_expected_channel

        frames.append(
            snapshot(
                state,
                "comb",
                p,
                first_hit,
                flipped,
                killed,
                str(p),
                f"Active prime p={p}: proper multiples only (2p,3p,...<=W)",
                flip_channel_mass_before=flip_mass,
                kill_channel_mass_before=kill_mass,
                delta_signed_sum=delta,
                tail_k=tail_k,
                tail_expected_channel=tail_expected_channel,
            )
        )

    # Exact endpoint and structural invariants.
    assert np.array_equal(state, mu_true), "comb path did not land exactly on mu"

    all_primes = get_primes_upto(limit)
    inert_primes = [p for p in all_primes if p > active_bound]
    for p in inert_primes:
        assert state[p - 1] == -1 == mu_true[p - 1]

    expected = 1 + len(comb_primes)
    assert len(frames) == expected
    return frames, inert_primes


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


def write_metrics_csv(
    frames: list[Frame], target_sum: int, active_bound: int, path: Path
) -> None:
    """Write the complete active-prime path for independent inspection."""
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(
            [
                "frame",
                "phase",
                "prime",
                "active_prime_bound_floor_W_over_2",
                "signed_sum",
                "target_MW",
                "distance_to_MW",
                "agreement_with_mu",
                "white_count",
                "first_hit_sites",
                "flipped_sites",
                "killed_sites",
                "flip_channel_mass_before",
                "kill_channel_mass_before",
                "delta_signed_sum",
                "tail_K_floor_W_over_p",
                "tail_expected_Cp_MK_minus_1",
            ]
        )
        for index, frame in enumerate(frames):
            writer.writerow(
                [
                    index,
                    frame.phase,
                    "" if frame.prime is None else frame.prime,
                    active_bound,
                    frame.signed_sum,
                    target_sum,
                    abs(frame.signed_sum - target_sum),
                    frame.agreement_mu,
                    frame.white_count,
                    frame.first_hit_count,
                    frame.flipped_count,
                    frame.killed_count,
                    frame.flip_channel_mass_before,
                    frame.kill_channel_mass_before,
                    frame.delta_signed_sum,
                    "" if frame.tail_k is None else frame.tail_k,
                    "" if frame.tail_expected_channel is None else frame.tail_expected_channel,
                ]
            )


def render_outputs(
    limit: int,
    grid_width: int,
    frames: list[Frame],
    inert_primes: list[int],
    mu_true: np.ndarray,
    output_dir: Path,
    fps: int,
    dpi: int,
    hold_seconds: float,
) -> tuple[Path, Path, Path, Path]:
    output_dir.mkdir(parents=True, exist_ok=True)

    gif_path = output_dir / f"prime_comb_mobius_W{limit}_fixed.gif"
    final_png_path = output_dir / f"prime_comb_mobius_W{limit}_fixed_final.png"
    path_png_path = output_dir / f"prime_comb_mobius_W{limit}_fixed_path.png"
    csv_path = output_dir / f"prime_comb_mobius_W{limit}_fixed_metrics.csv"

    active_bound = limit // 2
    target_sum = int(mu_true.sum())
    write_metrics_csv(frames, target_sum, active_bound, csv_path)

    true_grid = padded_grid(mu_true, grid_width)
    gap = 2

    cmap = ListedColormap([STEELBLUE, WHITE, CYAN])
    cmap.set_bad(PADDING)
    norm = plt.Normalize(-1.5, 1.5)

    legend_handles = [
        Patch(facecolor=STEELBLUE, edgecolor=BLACK, label="-1"),
        Patch(facecolor=WHITE, edgecolor=BLACK, label="0 (square factor)"),
        Patch(facecolor=CYAN, edgecolor=BLACK, label="+1"),
        Line2D(
            [0],
            [0],
            marker="s",
            linestyle="none",
            markerfacecolor="none",
            markeredgecolor=ORANGE,
            markeredgewidth=1.8,
            markersize=8,
            label="First proper-prime hit (no sign change)",
        ),
        Line2D(
            [0],
            [0],
            marker="o",
            linestyle="none",
            markerfacecolor="none",
            markeredgecolor=RED,
            markeredgewidth=1.8,
            markersize=8,
            label="Later distinct-prime hit (sign flip)",
        ),
        Line2D(
            [0],
            [0],
            marker="x",
            linestyle="none",
            color=BLACK,
            markeredgewidth=1.8,
            markersize=8,
            label="Square-factor kill",
        ),
    ]

    labels = [f.label for f in frames]
    sums = np.array([f.signed_sum for f in frames], dtype=int)
    agreements = np.array([f.agreement_mu for f in frames], dtype=int)
    distances = np.abs(sums - target_sum)
    count = len(frames)

    sum_low = min(int(sums.min()), target_sum)
    sum_high = max(int(sums.max()), target_sum)
    span = max(sum_high - sum_low, 1)
    metric_high = max(int(agreements.max()), int(distances.max()), 1)

    stride = max(1, count // 12)
    last = count - 1
    ticks = [i for i in range(0, count, stride) if last - i >= stride]
    ticks.append(last)

    fig = plt.figure(figsize=(16, 10.8))
    fig.set_dpi(dpi)
    gs = fig.add_gridspec(2, 2, height_ratios=[3.25, 1.35], hspace=0.64, wspace=0.22)
    ax_grid = fig.add_subplot(gs[0, :])
    ax_sum = fig.add_subplot(gs[1, 0])
    ax_agree = fig.add_subplot(gs[1, 1])
    footer = fig.text(0.5, 0.012, "", ha="center", va="bottom", fontsize=10, color="#333333")

    def overlay_mask(axis, mask: np.ndarray, marker: str, color: str, size: float) -> None:
        if not np.any(mask):
            return
        rows, cols = np.where(padded_mask(mask, grid_width))
        if marker == "x":
            axis.scatter(cols, rows, marker=marker, s=size, color=color, linewidths=1.6)
        else:
            axis.scatter(
                cols,
                rows,
                marker=marker,
                s=size,
                facecolors="none",
                edgecolors=color,
                linewidths=1.7,
            )

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

        overlay_mask(ax_grid, frame.first_hit, "s", ORANGE, 50)
        overlay_mask(ax_grid, frame.flipped, "o", RED, 50)
        overlay_mask(ax_grid, frame.killed, "x", BLACK, 46)

        ax_grid.axvline(grid_width + (gap - 1) / 2, linewidth=1.5, color=DIVIDER)
        ax_grid.axis("off")

        ax_grid.text(
            0.24,
            -0.035,
            "Prime-candidate comb state",
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
                f"first hits={frame.first_hit_count}, flips={frame.flipped_count}, "
                f"kills={frame.killed_count}, C_p={frame.flip_channel_mass_before:+d}, "
                f"Delta B={frame.delta_signed_sum:+d}"
            )
            if frame.tail_k is not None:
                operation_line += (
                    f"; tail check: K=floor(W/p)={frame.tail_k}, "
                    f"C_p=M(K)-1={frame.tail_expected_channel:+d}"
                )
        else:
            operation_line = (
                "untouched -1 means prime candidate; primes never hit themselves"
            )

        ax_grid.set_title(
            f"{frame.title}\n"
            f"Only primes p <= floor(W/2)={active_bound} are active; "
            f"{len(inert_primes)} primes above W/2 are inert\n"
            f"B={frame.signed_sum:+d}, M({limit})={target_sum:+d}, "
            f"|B-M(W)|={abs(frame.signed_sum-target_sum)}, "
            f"agreement with mu={frame.agreement_mu}/{limit}\n"
            f"{operation_line}",
            fontsize=12.8,
            pad=18,
        )
        ax_grid.legend(
            handles=legend_handles,
            loc="upper center",
            bbox_to_anchor=(0.5, -0.13),
            ncol=3,
            frameon=True,
            fontsize=8.8,
            handlelength=1.4,
            columnspacing=1.25,
        )

    def style_axis(axis) -> None:
        axis.set_xlim(-0.6, count - 0.4)
        axis.set_xticks(ticks)
        axis.set_xticklabels([labels[i] for i in ticks], rotation=45, ha="right")
        axis.set_xlabel("Active prime just applied")
        axis.grid(True, alpha=0.25)

    def draw_paths(index: int) -> None:
        x = np.arange(index + 1)

        ax_sum.clear()
        ax_sum.plot(x, sums[: index + 1], marker="o", markersize=3, color="#1F5FA8")
        ax_sum.axhline(
            target_sum,
            linestyle="--",
            linewidth=1.3,
            color="#C0392B",
            label=f"target M({limit})={target_sum:+d}",
        )
        ax_sum.set_title("Signed sum along the active-prime path")
        ax_sum.set_ylabel("B")
        ax_sum.set_ylim(sum_low - 0.08 * span, sum_high + 0.34 * span)
        style_axis(ax_sum)
        ax_sum.legend(loc="upper right", fontsize=8.5, framealpha=0.9)

        ax_agree.clear()
        ax_agree.plot(
            x,
            agreements[: index + 1],
            marker="o",
            markersize=3,
            color="#2E8B57",
            label="agreement with mu",
        )
        ax_agree.plot(
            x,
            distances[: index + 1],
            marker=".",
            markersize=3,
            color="#C0392B",
            label="|B-M(W)|",
        )
        ax_agree.set_title("Exact endpoint; no monotonicity assumed")
        ax_agree.set_ylabel("Count / distance")
        ax_agree.set_ylim(-0.04 * metric_high, 1.30 * metric_high)
        style_axis(ax_agree)
        ax_agree.legend(loc="upper left", fontsize=8.5, framealpha=0.9)

    def update(index: int):
        frame = frames[index]
        draw_grid(frame)
        draw_paths(index)
        current = "-" if frame.prime is None else str(frame.prime)
        footer.set_text(
            f"phase={frame.phase} | active prime={current} | whites={frame.white_count} | "
            f"first hits={frame.first_hit_count} | flips={frame.flipped_count} | "
            f"kills={frame.killed_count}"
        )
        return []

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

    # Final exact-state comparison.
    final = frames[-1]
    fig_final, ax_final = plt.subplots(figsize=(15, 8.4))
    ax_final.imshow(
        np.ma.masked_invalid(
            combine_grids(padded_grid(final.state, grid_width), true_grid, gap=gap)
        ),
        cmap=cmap,
        norm=norm,
        interpolation="none",
        aspect="equal",
    )
    ax_final.axvline(grid_width + (gap - 1) / 2, linewidth=1.5, color=DIVIDER)
    ax_final.axis("off")
    ax_final.set_title(
        f"Exact endpoint after active primes p <= floor({limit}/2)={active_bound}\n"
        f"The state is mu(n): agreement={final.agreement_mu}/{limit}, "
        f"B={final.signed_sum:+d}=M({limit}); primes p>{active_bound} are inert",
        fontsize=15,
        pad=18,
    )
    for x_pos, text in (
        (0.24, "Prime-candidate comb state"),
        (0.76, "Exact Moebius mu(n)"),
    ):
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
    fig_path, axes = plt.subplots(2, 1, figsize=(13, 8.5), sharex=True)
    x_all = np.arange(count)
    axes[0].plot(x_all, sums, marker="o", markersize=3, color="#1F5FA8")
    axes[0].axhline(
        target_sum,
        linestyle="--",
        linewidth=1.3,
        color="#C0392B",
        label=f"M({limit})={target_sum:+d}",
    )
    axes[0].set_ylabel("Signed sum B")
    axes[0].set_title(
        f"Corrected prime-candidate comb: only p <= floor(W/2)={active_bound} act"
    )
    axes[0].grid(True, alpha=0.25)
    axes[0].legend(loc="best")

    axes[1].plot(
        x_all,
        agreements,
        marker="o",
        markersize=3,
        color="#2E8B57",
        label="agreement with mu",
    )
    axes[1].plot(
        x_all,
        distances,
        marker=".",
        markersize=3,
        color="#C0392B",
        label="|B-M(W)|",
    )
    axes[1].set_ylabel("Count / distance")
    axes[1].set_xlabel("Active prime just applied")
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
            "Animate the corrected prime-candidate comb for mu(1),...,mu(W), "
            "using only active primes p <= floor(W/2)."
        )
    )
    parser.add_argument("--limit", type=int, default=210, help="Block endpoint W (default: 210).")
    parser.add_argument(
        "--grid-width", type=int, default=15, help="Cells per grid row (default: 15)."
    )
    parser.add_argument("--fps", type=int, default=2, help="GIF frames per second (default: 2).")
    parser.add_argument("--dpi", type=int, default=80, help="GIF render dpi (default: 80).")
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

    if args.limit < 2:
        parser.error("--limit must be at least 2")
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
    frames, inert_primes = build_frames(args.limit, mu_true)

    gif_path, final_png_path, path_png_path, csv_path = render_outputs(
        limit=args.limit,
        grid_width=args.grid_width,
        frames=frames,
        inert_primes=inert_primes,
        mu_true=mu_true,
        output_dir=args.output_dir,
        fps=args.fps,
        dpi=args.dpi,
        hold_seconds=args.hold_seconds,
    )

    target_sum = int(mu_true.sum())
    active = [f for f in frames if f.phase == "comb"]
    active_primes = [f.prime for f in active]
    sums = [f.signed_sum for f in active]
    distances = [abs(value - target_sum) for value in sums]
    monotone = all(a <= b for a, b in zip(sums, sums[1:])) or all(
        a >= b for a, b in zip(sums, sums[1:])
    )
    killing_frames = [f for f in active if f.killed_count]
    last_white = killing_frames[-1].prime if killing_frames else None
    tail_frames = [f for f in active if f.tail_k is not None]
    tail_delta = sum(f.delta_signed_sum for f in tail_frames)

    print("Generated files:")
    for path in (gif_path, final_png_path, path_png_path, csv_path):
        print(f"  {path}")
    print()
    print(f"Block W                       : {args.limit}")
    print(f"Active prime bound floor(W/2): {args.limit // 2}")
    print(f"Active primes                 : {len(active_primes)}")
    print(f"Last active prime             : {active_primes[-1] if active_primes else None}")
    print(f"Inert primes above W/2        : {len(inert_primes)}")
    print(f"First/last inert prime        : "
          f"{(inert_primes[0], inert_primes[-1]) if inert_primes else None}")
    print(f"Last prime to create white    : {last_white}")
    print()
    print(f"Exact endpoint agreement      : {frames[-1].agreement_mu}/{args.limit}")
    print(f"Final B                       : {frames[-1].signed_sum:+d}")
    print(f"M(W)                          : {target_sum:+d}")
    print(f"Tail delta for sqrt(W)<p<=W/2 : {tail_delta:+d}")
    print(f"Max |B-M(W)| on active path   : {max(distances) if distances else 0}")
    print(f"Signed-sum path monotone      : {monotone}")


if __name__ == "__main__":
    main()
