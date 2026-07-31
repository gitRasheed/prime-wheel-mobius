# Paper

The current manuscript is:

```text
seeded_prime_comb_harmonic_reduction.tex
```

It is titled **Seeded Prime-Comb Dynamics and the Finite Harmonic Reduction of Primorial-Block Möbius Sums**.

Compile from this directory with:

```bash
latexmk -pdf seeded_prime_comb_harmonic_reduction.tex
```

A standard TeX installation should provide `fontenc`, `inputenc`, `lmodern`, `microtype`, `geometry`, the AMS packages, `booktabs`, `array`, `longtable`, `enumitem`, `xcolor`, `hyperref`, `cleveref`, `fancyhdr`, and `lastpage`.

The source contains clickable links to the public Lean theorem files after the corresponding proofs. Section 7 links directly to:

```text
../numerics/primorial_block_validation.py
```

The numerical computations are evidence and implementation checks; they are not premises of the formal theorem chain.
