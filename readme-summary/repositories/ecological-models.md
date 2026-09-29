# ecological-models

**Summary**

URBS (Urban Policy Field Simulator) models a city as a lattice‑based field system rather than a collection of independent variables. Each district evolves through three interacting fields:

- **Φ (Structural Potential)** – represents infrastructure, housing, health, and environmental quality.
- **v (Flow Field)** – governs population and economic activity movement along gradients of Φ − S.
- **S (Entropy / Collapse Pressure)** – measures systemic failure and instability; high S indicates breakdown of services.

The simulator produces emergent urban patterns such as stable cores, peripheral decay, migration flows, and potential systemic collapse. Users can adjust global policy levers (housing, environmental regulation, healthcare, infrastructure, redistribution, security) which bias Φ’s evolution and indirectly affect S and flow dynamics. The system is deterministic aside from optional stochastic migration.

Running URBS requires only the HTML file; it includes controls for stepping, resetting, loading scenarios, adjusting policy sliders, and inspecting field layers via view tabs. Metrics tracked include total population, average wellbeing, Gini coefficient (inequality), environmental health, and collapse pressure.

URBS is intended as an experimental tool to explore how constraint, flow, and entropy interact in complex socio‑economic systems, not a predictive model of real cities.

**KEYWORDS:** ecological models, urban dynamics simulator, scalar vector entropy framework, lattice field system, policy sandbox, emergent patterns, structural potential, collapse pressure, simulation metrics.
