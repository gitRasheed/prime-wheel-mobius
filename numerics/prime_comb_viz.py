import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.colors import ListedColormap
from matplotlib.patches import Patch
from matplotlib.lines import Line2D

# ------------------------------------------------------------
# Arithmetic core
# ------------------------------------------------------------

def get_primes_upto(n):
    if n < 2:
        return []
    sieve = np.ones(n + 1, dtype=bool)
    sieve[:2] = False
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            sieve[i * i:n + 1:i] = False
    return [i for i, flag in enumerate(sieve) if flag]

def compute_mobius(limit):
    mu = [1] * (limit + 1)
    spf = np.arange(limit + 1)
    for i in range(2, int(limit**0.5) + 1):
        if spf[i] == i:
            for j in range(i * i, limit + 1, i):
                if spf[j] == j:
                    spf[j] = i
    for i in range(2, limit + 1):
        p = int(spf[i])
        mu[i] = 0 if (i // p) % p == 0 else -mu[i // p]
    return np.array(mu, dtype=int)

def u_p(n, p):
    if n % (p * p) == 0:
        return 0
    if n % p == 0:
        return -1
    return 1

# ------------------------------------------------------------
# Primorial block setup
# ------------------------------------------------------------

W = 210
grid_width = 15
grid_height = W // grid_width
y = int(np.floor(np.sqrt(W)))
primes = get_primes_upto(y)
mu_true = compute_mobius(W)[1:]

def to_grid(arr):
    return arr.reshape((grid_height, grid_width))

true_grid = to_grid(mu_true)

# ------------------------------------------------------------
# Build evolving states
# ------------------------------------------------------------

state = np.full(W, -1, dtype=int)
frames = [(to_grid(state.copy()), "Phase 0: Seed field  Jf₀ = −1", None)]

for p in primes:
    state = np.array(
        [state[n - 1] * u_p(n, p) for n in range(1, W + 1)],
        dtype=int
    )
    frames.append((to_grid(state.copy()), f"Phase 1: Apply local operator T_{p}", None))

# Identify fully y-smooth squarefree sites directly from divisibility,
# without consulting mu_true for the correction set.
smooth_core_indices = []
for n in range(1, W + 1):
    temp = n
    squarefree = True
    for p in primes:
        if temp % (p * p) == 0:
            squarefree = False
            break
        while temp % p == 0:
            temp //= p
    if squarefree and temp == 1:
        smooth_core_indices.append(n - 1)

correction_mask = np.zeros((grid_height, grid_width), dtype=bool)
for idx in smooth_core_indices:
    correction_mask[idx // grid_width, idx % grid_width] = True

frames.append((
    to_grid(state.copy()),
    "Phase 2: Smooth-core correction sites highlighted",
    correction_mask
))

corrected_state = state.copy()
for idx in smooth_core_indices:
    corrected_state[idx] = -corrected_state[idx]

assert np.array_equal(corrected_state, mu_true)
frames.append((
    to_grid(corrected_state),
    "Phase 3: Exact Möbius recovery",
    None
))

# ------------------------------------------------------------
# Side-by-side layout and legend
# ------------------------------------------------------------

# Requested colors:
# -1 = steelblue, 0 = white, +1 = cyan, correction markers = red
cmap = ListedColormap(["#4682B4", "#FFFFFF", "#00FFFF"])
cmap.set_bad("#E6E6E6")
norm = plt.Normalize(-1.5, 1.5)

gap = 2
combined_width = grid_width * 2 + gap

def combine_grids(left, right):
    combined = np.full((grid_height, combined_width), np.nan, dtype=float)
    combined[:, :grid_width] = left
    combined[:, grid_width + gap:] = right
    return combined

legend_handles = [
    Patch(facecolor="#4682B4", edgecolor="black", label="−1"),
    Patch(facecolor="#FFFFFF", edgecolor="black", label="0  (square factor)"),
    Patch(facecolor="#00FFFF", edgecolor="black", label="+1"),
    Line2D(
        [0], [0],
        marker="o",
        linestyle="none",
        markerfacecolor="none",
        markeredgecolor="red",
        markeredgewidth=2,
        markersize=9,
        label="Fully smooth squarefree site corrected in Phase 2",
    ),
]

gif_path = "prime_comb_side_by_side_steelblue_cyan_red.gif"
png_path = "prime_comb_side_by_side_steelblue_cyan_red_final.png"

fig, ax = plt.subplots(figsize=(15, 7.8))

def decorate_axes(ax, phase_title, matches):
    ax.axis("off")
    divider_x = grid_width + (gap - 1) / 2
    ax.axvline(divider_x, linewidth=1.5)

    ax.text(
        (grid_width - 1) / 2,
        -1.05,
        "Prime-comb state",
        ha="center",
        va="bottom",
        fontsize=13,
        fontweight="bold",
    )
    ax.text(
        grid_width + gap + (grid_width - 1) / 2,
        -1.05,
        "Exact Möbius μ(n)",
        ha="center",
        va="bottom",
        fontsize=13,
        fontweight="bold",
    )
    ax.set_title(
        f"{phase_title}\nAgreement with exact μ: {matches}/{W}",
        fontsize=15,
        pad=18,
    )
    ax.legend(
        handles=legend_handles,
        loc="upper center",
        bbox_to_anchor=(0.5, -0.06),
        ncol=4,
        frameon=True,
        fontsize=10,
        handlelength=1.4,
        columnspacing=1.5,
    )

def update(frame_idx):
    ax.clear()
    left_grid, phase_title, mask = frames[frame_idx]
    combined = combine_grids(left_grid, true_grid)

    im = ax.imshow(
        np.ma.masked_invalid(combined),
        cmap=cmap,
        norm=norm,
        interpolation="none",
        aspect="equal",
    )

    if mask is not None:
        rows, cols = np.where(mask)
        ax.scatter(
            cols,
            rows,
            marker="o",
            s=52,
            facecolors="none",
            edgecolors="red",
            linewidths=2,
        )

    matches = int(np.count_nonzero(left_grid.ravel() == mu_true))
    decorate_axes(ax, phase_title, matches)
    return [im]

ani = animation.FuncAnimation(
    fig,
    update,
    frames=len(frames),
    interval=1200,
    repeat_delay=2000,
)
ani.save(gif_path, writer=animation.PillowWriter(fps=1))
plt.close(fig)

# Final static frame too
final_combined = combine_grids(to_grid(corrected_state), true_grid)
fig_final, ax_final = plt.subplots(figsize=(15, 7.8))
ax_final.imshow(
    np.ma.masked_invalid(final_combined),
    cmap=cmap,
    norm=norm,
    interpolation="none",
    aspect="equal",
)
decorate_axes(
    ax_final,
    "Exact agreement after smooth-core correction",
    W,
)
fig_final.savefig(png_path, dpi=170, bbox_inches="tight")
plt.close(fig_final)

print("Generated files:")
print(gif_path)
print(png_path)
print(f"Frames: {len(frames)}")
print(f"Primes used: {primes}")
print(f"Correction sites: {len(smooth_core_indices)}")