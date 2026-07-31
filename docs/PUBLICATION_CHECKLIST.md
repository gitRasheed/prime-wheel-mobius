# Publication checklist

Before publishing or cutting a release:

- [ ] Copy the contents of `export/public-repo/` to the new repository root.
- [ ] Choose and add an explicit software/content license.
- [ ] Confirm the paper title, author line, version date, DOI/SSRN link, and preferred citation.
- [ ] Compile `paper/seeded_prime_comb_harmonic_reduction.tex` and optionally commit the resulting PDF.
- [ ] Confirm the Section 7 link resolves to `numerics/primorial_block_validation.py`.
- [ ] Run `cd formalization && lake build RHLean --wfail`.
- [ ] Run `cd formalization && bash scripts/audit_assumptions.sh`.
- [ ] Run the finite validation and analytic gate commands in `numerics/README.md`.
- [ ] Confirm `results/SOURCE_SHA256SUMS.txt` and `results/SHA256SUMS.txt` are produced by the numerical workflow.
- [ ] Confirm all GitHub Actions checks are green.
- [ ] Add the final paper URL or DOI to the repository README and citation metadata when available.
- [ ] Keep the two open inputs described exactly as in `docs/THEOREM_STATUS.md`.

Do not describe the repository as an unconditional proof of RH unless both the maximal nonconcentration estimate and the classical Lean Mertens/RH connection have been supplied and checked.
