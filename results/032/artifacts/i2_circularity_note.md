# Record 032b — I2 DC/AC circularity probe, scaled run

**Date:** 2026-08-12. **Script:** `i2_circularity_scaled.py` (this directory; scales
`pilot_i2_circularity.py`, value-identical at x = 1e6 on the pilot's 16 pins).
**Data:** `i2_circularity_scaled.csv`.

## Question

Audit 029 (review `i2-viability`, fatal finding #1) asserts the I2 DC/AC isolation is
circular: |V_0 − A_q| ≪ q^{1+ε} holds **unconditionally** (023's affine modulus even
gives O(q) directly), so bounding the DC mean A_q at the rung-1 precision q^{1+ε} is
the same statement as bounding V_0 = S(y, X) itself. This probe scales the numerical
check of that claim.

## Objects

Canonical pins q (40 log-spaced values, 16 ≤ q ≤ 10000), X = q² − 1, y = q − 1.

- V_t = S(q−1, X−t) = Σ_{d ≤ K_t} μ(d) R(⌊(X−t)/d⌋), with K_t = ⌊(X−t)/q⌋ = q − 1
  constant across the window 0 ≤ t ≤ q − 1 (asserted at every pin).
- R(t) = π(t) − Li₂(t), Li₂ by midpoint quadrature (only differences of R enter).
- A_q = q⁻¹ Σ_{t<q} V_t (DC mean); c_q(X−t) = V_t − V_{t+1} for 0 ≤ t ≤ q − 2
  (increment; range restricted per audit minor finding — no V_q is invoked).

## Scale and run

Sieve to x = 1e8 (largest pin q = 10000, X = 99 999 999). Runtime 70 s, peak RSS
1.69 GB (the pilot's dead-code int64 arrays and full-range μ sieve were removed:
μ is only ever indexed at d ≤ q − 1 ≤ 9999, so it is sieved to 10⁴ exactly; the
R table is built as a float64 cumsum with the Li₂ midpoint cumsum subtracted in
4M-element chunks).

## Frozen predictions vs outcome

| quantity | frozen prediction | pilot (x=1e6) | scaled (x=1e8) | verdict |
|---|---|---|---|---|
| \|V_0 − A_q\| fit exponent | ≤ 1 | 0.60–0.72 | **0.505** (Theil–Sen 0.516; bin-max envelope 0.643) | holds |
| Σ_t \|c_q(X−t)\| fit exponent | ~ 1 + o(1) | 0.97–0.98 | **0.978** (Theil–Sen 0.979; tail half 0.974) | holds |
| kill: gap exponent clearly > 1 | — | not triggered | **not triggered** | no kill |

Robustness (gap is a noisy one-sample-per-pin quantity, values scatter 1.4–59.5
among neighboring large pins, so several fits are reported):

- OLS on all 40 pins: 0.505. Theil–Sen: 0.516. Upper envelope (max gap in 6
  geometric bins): 0.643. Tail-half OLS: 0.319 (unstable, small-sample; quoted
  only to show the tail does not bend upward).
- gap/√q: median 0.209, max 0.875 over all 40 pins — consistent with a
  square-root-fluctuation scale, i.e. even *below* the audit's unconditional O(q).
- gap/q for q ≥ 1000: max 0.0158. The DC/AC "reduction" precision q^{1+ε} exceeds
  the observed |V_0 − A_q| by two to three orders of magnitude at the top of range.
- csum/q lies in [0.496, 0.652] across all pins and drifts to ≈ 0.50 at large q:
  Σ_t |c_q| ≈ q/2, squarely q^{1+o(1)}.

## Reading

The scaled data supports the audit's circularity finding and is if anything
stronger than the audit needs: the audit's argument only requires the
unconditional |V_0 − A_q| ≪ q^{1+ε} (or 023's O(q)); the observed gap sits near
q^{1/2}, far below both. At every measured pin, knowing A_q to precision q^{1+ε}
determines V_0 to the same precision and vice versa — the DC "principal mode"
carries the entire content of the Abel-face partial sum at rung-1 precision.
Nothing in the window structure (the c_q increments) creates room between the
two statements: the total increment mass across the window is ≈ q/2, itself at
the q^{1+o(1)} scale.

Caveats. (i) This is a numerical probe at pins up to q = 10⁴; it cannot rule out
asymptotic regime change, but the kill condition (gap exponent clearly above 1)
required the opposite trend and the trend is flat-to-downward. (ii) The gap
exponent ~0.5 is itself an RH-flavored observation (square-root cancellation in
the window average) and should NOT be quoted as evidence for any bound — only the
comparison against the q^{1+ε} precision scale matters for the circularity claim.
(iii) Li₂ is midpoint quadrature as in the pilot; only differences of R across
the window enter the gap, so quadrature convention cannot affect the conclusion.
