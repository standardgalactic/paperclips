# logical-connectives

Summary:

The **logical-connectives** repository provides an interactive field guide to all Boolean functions of two inputs, represented as vertices of a four-dimensional hypercube (Q₄). Each of the sixteen possible truth tables corresponds to one vertex, forming a rank structure 1‑4‑6‑4‑1. The README describes how every connective is defined by a unique canonical four-bit output, from which an index card, description, truth table, and live evaluator are generated. This alignment ensures that explanations match executable behavior.

The project includes a dependency-free site (`docs/`) accessible via `docs/index.html` or served locally at `/docs/`. A test script (`tests/connectives.test.mjs`) verifies the catalogue’s completeness. The documentation complements *The Geometry of Expressibility: Logic at the Corners of a Continuous Relational Space*, originally titled *From NAND to Xanadu*, with the full LaTeX manuscript available in `essay/geometry-of-expressibility.tex`. It also discusses extensions from Q₄ to Q₅, indicating how additional coordinates relate to three-input Boolean functions (2⁸ = 256 vertices forming Q₈).

KEYWORDS:
logical connectives
Boolean functions
hypercube Q4
rank structure
interactive catalogue
NAND Xanadu
continuous relational space
LaTeX manuscript
