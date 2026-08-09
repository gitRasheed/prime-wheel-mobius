import Lake
open Lake DSL

package «PrimeWheelFormalization» where
  version := v!"1.0.0"

require mathlib from git
  "https://github.com/leanprover-community/mathlib4.git" @ "v4.24.0"

lean_lib RHLean
