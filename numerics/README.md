# Numerical reproducibility

The numerical programs are deterministic diagnostics and implementation checks. They are not theorem premises and do not prove the remaining maximal nonconcentration estimate.

Install the pinned Python dependencies:

```bash
python -m pip install -r requirements.txt
```

## Finite primorial-block validation

This is the program linked directly from Section 7 of the paper:

```bash
python primorial_block_validation.py \
  --nmax 4096 \
  --out results/primorial_block_validation
```

The implementation is byte-for-byte identical to the file previously named `squared_space_reproducibility_v3.py`; only its repository path changed. Its reused Git blob SHA is:

```text
98ad192eb59c1ad9cf31ab8cdbfc43cf0f8497ed
```

The historical module docstring is retained unchanged to preserve byte-level provenance.

## Analytic falsification gates

```bash
python analytic_kill_gates.py \
  --nmax 4096 \
  --boundary-mmax 2048 \
  --rmax 240 \
  --cutoff 60 \
  --lambda-high 16 \
  --out results/analytic_kill_gates
```

These gates test exact identities and search for finite-range failure modes. Passing them is not a proof of the open theorem.

## Hash record

The numerical GitHub Actions workflow writes:

- `results/SOURCE_SHA256SUMS.txt` for the two Python source files;
- `results/SHA256SUMS.txt` for the generated numerical artifacts.

The generated archive hash can change when paths, metadata, or output files change. The main validation program's content identity is separately preserved by the Git blob SHA above.
