import Mathlib

open scoped ArithmeticFunction.Moebius BigOperators

noncomputable section

namespace RHLean.Analysis

/-- The complex-valued Mertens summatory function, including the harmless `mu(0) = 0` term. -/
def mertensSummatory (x : ℕ) : ℂ :=
  Finset.sum (Finset.range (x + 1)) fun m => (((μ m : ℤ) : ℂ))

@[simp] theorem mertensSummatory_zero : mertensSummatory 0 = 0 := by
  simp [mertensSummatory]

/-- The squared Mertens growth criterion at critical exponent one. -/
def MertensEnergyBoundedStatement : Prop :=
  ∀ ε : ℝ, 0 < ε →
    ∃ C : ℝ, 0 ≤ C ∧
      ∀ x : ℕ,
        ‖mertensSummatory x‖ ^ 2 ≤
          C * Real.rpow ((x + 1 : ℕ) : ℝ) (1 + ε)

end RHLean.Analysis
