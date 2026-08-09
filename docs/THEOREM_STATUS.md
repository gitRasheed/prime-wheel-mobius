# Formal theorem status

## Proved in Lean

The exported project proves:

1. the seeded square-sensitive prime-wheel operator and exact pointwise Möbius recovery on synchronized primorial blocks;
2. every-prefix residual identity;
3. lossless finite-torus embedding and exact DFT pairing;
4. raw-minus-twice-smooth joint-spectrum decomposition;
5. explicit raw arithmetic and squarefree-divisor smooth-core coefficients;
6. pinned start phase times finite Dirichlet kernel;
7. full frequency-frequency and conductor-pair Gram identities, retaining all off-diagonal terms;
8. complete-wheel local sum, CRT mass product, and tensor spectrum identities;
9. exact equivalence between the explicit Dirichlet nonconcentration statement, the harmonic statement, the primorial residual statement, and the global Mertens-energy statement.

The public theorem is:

```lean
theorem primorialWheel_dirichletNonconcentration_iff_mertensEnergy :
    PrimorialWheelDirichletNonconcentration ↔
      MertensEnergyBoundedStatement
```

## Deliberately open

The export does not claim a proof of:

```lean
PrimorialWheelDirichletNonconcentration
```

This is the remaining maximal nonconcentration estimate.

The classical endpoint is also supplied explicitly rather than hidden:

```lean
MertensEnergyBoundedStatement ↔ RiemannHypothesisStatement
```

Given that classical theorem, the exported project proves:

```lean
theorem primorialWheel_dirichletNonconcentration_iff_riemannHypothesis
    (criterion : MertensEnergyBoundedStatement ↔ RiemannHypothesisStatement) :
    PrimorialWheelDirichletNonconcentration ↔ RiemannHypothesisStatement
```

## Foundations

The development uses standard Lean/Mathlib classical foundations and noncomputable definitions. The repository audit rejects `sorry`, `admit`, and project-local top-level `axiom` or `constant` declarations.
