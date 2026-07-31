# Source provenance

This export was assembled from `OVVO-Financial/RH_Lean`. The exact arithmetic and Fourier theorem files below retain their checked provenance from merged commit:

`f6110ca00b27a0a329a0f74db8b7747ad4bae234`

The paper and numerical-path update was prepared from sandbox commit:

`0376191574fa46ae9eea3c0e6a9f9372ad23576f`

## Exact merged source modules

### Arithmetic

- `RHLean/Arithmetic/BooleanCubeCancellation.lean`
- `RHLean/Arithmetic/TruncatedBooleanCube.lean`
- `RHLean/Arithmetic/PrimeProductCubeFrontier.lean`
- `RHLean/Arithmetic/PrimeFaceMoebius.lean`
- `RHLean/Arithmetic/PrimesUpToFrontier.lean`
- `RHLean/Arithmetic/PrimeWheelFiniteSystem.lean`
- `RHLean/Arithmetic/PrimorialWheelScale.lean`
- `RHLean/Arithmetic/PrimeWheelMobiusRecovery.lean`
- `RHLean/Arithmetic/PrimorialWheelPrefixIdentity.lean`
- `RHLean/Arithmetic/PrimorialWheelScaleGrowth.lean`

### Analysis

- `RHLean/Analysis/FiniteTorusFourierPairing.lean`
- `RHLean/Analysis/PrimeWheelFourierReduction.lean`
- `RHLean/Analysis/PrimeWheelTorusRealization.lean`
- `RHLean/Analysis/PrimeWheelJointSpectrum.lean`
- `RHLean/Analysis/PrimeWheelArithmeticSpectrum.lean`
- `RHLean/Analysis/PrimeWheelCompleteSpectrum.lean`
- `RHLean/Analysis/PrimeWheelHarmonicCriterion.lean`
- `RHLean/Analysis/PrimeWheelConductorGram.lean`
- `RHLean/Analysis/PrimeWheelDirichletResponse.lean`
- `RHLean/Analysis/PrimeWheelExplicitCriterion.lean`
- `RHLean/Analysis/PrimorialWheelMertensTransfer.lean`

## Public adapters

The export replaces two sandbox-coupled bridge modules with minimal public adapters at the same module paths:

- `RHLean/Analysis/SquarePrefixMertensBridge.lean` defines only the Mertens summatory function and squared growth criterion required by the exact reduction.
- `RHLean/Analysis/PrimeWheelRHBridge.lean` names Mathlib's `RiemannHypothesis` proposition and keeps the classical Mertens/RH theorem as an explicit argument.

`RHLean/Analysis/PublicPrimeWheelReduction.lean` exposes the final public theorem without a caller-supplied primorial bridge.

## Paper provenance

- Current manuscript: `paper/seeded_prime_comb_harmonic_reduction.tex`.
- Manuscript SHA-256 at export assembly: `8f02277dd763774f1c4859c64c52157aa7a4323ffb4fc861b192ad3ab2617a72`.
- Public repository: `https://github.com/OVVO-Financial/prime-wheel-mobius`.
- Section 7 links directly to `numerics/primorial_block_validation.py`.

## Numerical provenance

- The validation program was renamed from `squared_space_reproducibility_v3.py` to `primorial_block_validation.py` without changing its bytes.
- Reused Git blob SHA for the renamed program: `98ad192eb59c1ad9cf31ab8cdbfc43cf0f8497ed`.
- `analytic_kill_gates.py` was updated only where necessary to load the renamed program.
- The numerical workflow records source SHA-256 values in `results/SOURCE_SHA256SUMS.txt`.
- The numerical workflow hashes every generated result artifact in `results/SHA256SUMS.txt`.
- Generated archive hashes can change when filenames, metadata, or output paths change; the validation program's content identity is recorded separately by the preserved Git blob SHA.

## Dependency pin

- Lean: `v4.24.0`
- Mathlib: `v4.24.0`
