import RHLean.Analysis.PrimeWheelArithmeticSpectrum
import RHLean.Analysis.PrimeWheelCompleteSpectrum
import RHLean.Analysis.PrimeWheelConductorGram
import RHLean.Analysis.PrimeWheelExplicitCriterion
import RHLean.Analysis.PrimorialWheelMertensTransfer

noncomputable section

namespace RHLean.Analysis

open RHLean.Arithmetic

/-- The harmonic criterion for the concrete primorial family is exactly the global Mertens-energy criterion. -/
theorem primorialWheel_harmonicNonconcentration_iff_mertensEnergy :
    PrimeWheelHarmonicNonconcentration primorialWheelFamily ↔
      MertensEnergyBoundedStatement := by
  exact (primeWheelHarmonicNonconcentration_iff_residualBounded
    primorialWheelFamily
    (canonicalPrimeWheelTorusCertificates primorialWheelFamily)).trans
      primorialWheel_residualBounded_iff_mertensEnergy

/-- Public endpoint: the explicit pinned Dirichlet estimate is exactly the global Mertens-energy criterion. -/
theorem primorialWheel_dirichletNonconcentration_iff_mertensEnergy :
    PrimorialWheelDirichletNonconcentration ↔
      MertensEnergyBoundedStatement := by
  exact primorialWheelDirichletNonconcentration_iff_harmonic.trans
    primorialWheel_harmonicNonconcentration_iff_mertensEnergy

/-- Public conditional RH endpoint. The only argument is the classical Mertens/RH criterion. -/
theorem primorialWheel_dirichletNonconcentration_iff_riemannHypothesis
    (criterion : MertensEnergyBoundedStatement ↔ RiemannHypothesisStatement) :
    PrimorialWheelDirichletNonconcentration ↔
      RiemannHypothesisStatement := by
  exact primorialWheel_dirichletNonconcentration_iff_mertensEnergy.trans criterion

/-- One-direction form used when proving the remaining maximal nonconcentration estimate. -/
theorem riemannHypothesis_of_primorialWheelDirichletNonconcentration
    (criterion : MertensEnergyBoundedStatement ↔ RiemannHypothesisStatement)
    (hnc : PrimorialWheelDirichletNonconcentration) :
    RiemannHypothesisStatement :=
  (primorialWheel_dirichletNonconcentration_iff_riemannHypothesis criterion).mp hnc

end RHLean.Analysis
