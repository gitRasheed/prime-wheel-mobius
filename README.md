# Prime-Wheel Möbius

Public companion repository for **Seeded Prime-Comb Dynamics and the Finite Harmonic Reduction of Primorial-Block Möbius Sums**.


## Contents

- `paper/` - current manuscript source and build notes.
- `formalization/` - standalone Lean 4 project pinned to Lean/mathlib `v4.24.0`.
- `numerics/` - finite primorial-block validation and analytic falsification gates.
- `docs/` - theorem status, source provenance, and publication checklist.
- `.github/workflows/` - Lean verification and numerical reproducibility.

## Mathematical boundary

The formalization proves the exact chain

```text
explicit pinned Dirichlet estimate
<-> harmonic nonconcentration
<-> finite wheel residual bound
<-> global Mertens-energy bound.
```

It does **not** claim an unconditional proof of the Riemann Hypothesis. Two inputs remain explicit:

1. the maximal pinned Dirichlet/nonconcentration estimate;
2. the classical theorem connecting the stated Mertens-energy bound to Mathlib's Riemann Hypothesis proposition.

See [`docs/THEOREM_STATUS.md`](docs/THEOREM_STATUS.md).

## Lean build

```bash
cd formalization
lake update
lake build RHLean --wfail
bash scripts/audit_assumptions.sh
```

## Paper

The compiled manuscript is available as [`paper/seeded_prime_comb_harmonic_reduction.pdf`](paper/seeded_prime_comb_harmonic_reduction.pdf).

The LaTeX source is [`paper/seeded_prime_comb_harmonic_reduction.tex`](paper/seeded_prime_comb_harmonic_reduction.tex).

## Numerical reproduction

The deterministic validation program used in Section 7 is [`numerics/primorial_block_validation.py`](numerics/primorial_block_validation.py).

See [`numerics/README.md`](numerics/README.md) for exact commands, status boundaries, and generated hash manifests.
