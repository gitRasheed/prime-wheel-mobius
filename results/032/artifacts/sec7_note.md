# sec.7 replication — record 032c (numbers only)

Replication of the route-doc sec.7 measurement ("Measured answer to that question",
CURRENT_PROOF_ROUTE.md, `main`) from the upstream probe scripts
`scripts/probes/{mobius.py, routeB.py, routeB_dense.py}` (copied read-only from
`main` into `scratchpad/sec7/`), run with python3.12 / numpy 2.4.5.

## What was run

| run | script | grid | wall time | peak RSS |
|---|---|---|---|---|
| A | `routeB_dense.py 1e7 240` (unmodified) | 240-pt log grid, x in [1e4, 1e7] | ~8 s | small |
| B | `routeB_dense.py 5e7 240` (unmodified) | 240-pt log grid, x in [1e4, 5e7] | 51 s | 2.00 GB |
| C | `routeB.py 5e7` (unmodified) | coarse checkpoints 1e4..3e7 | 14 s | small |
| D | `sec7_csv_driver.py 1e8 240` | 240-pt log grid, x in [1e4, 1e8] | 76 s | 2.49 GB |

Run D is the sec.7-recorded configuration (240-point logarithmic grid to x = 1e8).
The driver reuses upstream code verbatim (`sieve_mu`, the `Li` series, and the
`measure()` body of `routeB_dense.py`); the only change is a memory-blocked build of
the Li midpoint-quadrature table (numerically identical summands; verified against
the upstream `Li` series to 5.5e-12 relative on the same four difference checks,
vs. the script's 1e-10 assertion). The driver's summary output at 1e7 and 5e7 agrees
with the unmodified `routeB_dense.py` to every printed digit (all exponents, medians,
correlations identical), so run D is a faithful extension.

Internal consistency: `C - 2E = M(x)` held exactly at every checkpoint in run C
(the script's built-in assertion), and the Li-table difference check passed in
every run.

## Headline numbers at the recorded scale (run D, x = 1e8, fits over x >= 1e5)

| quantity | route-doc sec.7 | replicated (run D) |
|---|---|---|
| `sum_d |E_d|` (triangle bound) exponent | 0.678 | 0.6780 |
| sub-range triangle fits | 0.635, 0.648, 0.706, 0.677 | 0.6347, 0.6483, 0.7058, 0.6771 |
| signed `|E^rec|` exponent | ~0.51 | 0.5145 |
| median `|E| / (sum|E_d|/sqrt(D))` | 1.43 | 1.428 |
| log-log correlation of `|E|` vs `sum|E_d|/sqrt(D)` | 0.78 | 0.7774 |
| median saving factor `sum|E_d| / |E|` | 24.9x | 24.9x (median ratio 0.04017) |
| required saving stated in doc | ~x^0.18 | (0.678 - 0.5 = 0.178) |

Every number recorded in sec.7 reproduces from the upstream scripts.

## Derived saving exponent (the audit's arithmetic)

With D = floor(x/y) ~ sqrt(x), so D^a = x^(a/2):

| run | triangle exp | signed exp | saving exp (triangle - signed) | as power of D |
|---|---|---|---|---|
| A (to 1e7) | 0.6484 | 0.4864 | x^0.1620 | D^0.324 |
| B (to 5e7) | 0.6722 | 0.4703 | x^0.2019 | D^0.404 |
| D (to 1e8) | 0.6780 | 0.5145 | x^0.1635 | D^0.327 |

Using the doc's own rounded figures 0.678 and 0.51: x^0.168 = D^0.336.

Reference points on the same scale:

- full square-root cancellation over the D fibres = sqrt(D) = D^0.5 = x^0.25;
- required saving stated in sec.7 = x^0.18;
- exponent of `sum_d|E_d|/sqrt(D)` (the full-sqrt(D)-cancellation prediction),
  run D: 0.4277, i.e. the signed exponent 0.5145 exceeds the prediction's
  exponent by 0.087 over x in [1e5, 1e8].

So at the recorded scale, the measured exponent gap between the triangle bound and
the signed sum is x^0.1635 = D^0.327 (run D; x^0.162-0.202 = D^0.324-0.404 across
runs), against sqrt(D) = x^0.25 for full square-root cancellation and x^0.18 for
the doc's stated requirement. The 5e7 run is the only one whose gap (x^0.202)
exceeds 0.18; the 1e7 and 1e8 runs sit below it. The signed-exponent fit is the
unstable ingredient (0.4864 / 0.4703 / 0.5145 across runs A/B/D; sub-range fits in
run D range 0.366-0.598), while the triangle exponent is stable (0.648-0.678).

Ratio dispersion at 1e8: `|E| / (sum|E_d|/sqrt(D))` has median 1.428, mean 1.643,
range [0.042, 5.467].

## Coarse checkpoints (run C, routeB.py 5e7, largest x)

| x | D | M(x) | E = T - Bulk | sum_d |E_d| | saving | \|E\|/sqrt(x) |
|---|---|---|---|---|---|---|
| 1e7 | 3160 | 1037 | -565.76 | 10937.9 | 19.3x | 0.1789 |
| 3e7 | 5475 | -1157 | 1166.47 | 23791.4 | 20.4x | 0.2130 |

## Files

- `sec7_replication.csv` — 720 per-x rows (240 per run A/B/D grid; `run_xmax` column),
  columns: x, D, M(x), E^rec, sum|E_d|, C^PNT, sum|E_d|/sqrt(D), |E|/sqrt(x),
  |E|/(sum|E_d|/sqrt(D)), saving factor.
- `sec7/dense_1e7.log`, `sec7/dense_5e7.log`, `sec7/dense_1e8.log`, `sec7/routeB_5e7.log`
  — full script outputs.
- `sec7/sec7_csv_driver.py` — the run-D driver (upstream code reused verbatim except
  the blocked Li-table build).
