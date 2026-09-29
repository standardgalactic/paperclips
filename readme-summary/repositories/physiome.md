# physiome

**Summary**

The *Physiome* repository provides an admissibility‑ and repair‑driven whole‑body physiology simulator written in Rust with a pure functional core. Unlike traditional homeostasis models (e.g., HumMod), Physiome treats each physiological variable as having its own **admissibility boundary**, a range of acceptable values that the rest of the body respects. When a variable exceeds its boundary, specialized **repair operators** (pure state transitions) are invoked to restore balance via mechanisms such as baroreflex, RAAS, thermoregulation, etc.

Key design features include:

- **Independent subsystem clocks**: Cardiovascular, renal, hepatic, gastrointestinal, nervous (autonomic), immune, hematologic, endocrine, metabolic, respiratory, thermal, microcirculation, lymphatic, musculoskeletal, integumentary, and skeletal modules run on their own time scales.
- **Domain‑independent traits**:
  - `ObservableBoundary` exposes current variables and admissible ranges for uniform iteration by the repair engine.
  - `Continuation` defines each subsystem’s desired advancement interval (`interval`) and how to advance it (`advance`), allowing the scheduler in `step_until` to progress the fastest‑due subsystem next, avoiding a single global timestep.
- **Repair operators** are data structures (name, predicate for violations, pure state transition). Adding new corrective pathways requires only adding a new `RepairOp`; core logic remains unchanged.
- **Cross‑subsystem coupling** occurs solely through the shared `PhysiologicalState`, preventing direct module calls and ensuring that dependencies like hematologic coagulation responding to hepatic clotting factors or immune fever responses affecting thermal core temperature are handled safely.

The repository contains 17 implemented subsystems, each with its own admissible ranges, at least one repair operator, and an independent clock. Running examples (infection scenario, hemorrhage, heat stress, metabolic challenge, endocrine stress) demonstrate reproducible physiological responses from a healthy baseline, while tests enforce baseline admissibility, specification/coupling contracts, and scenario‑level invariants.

**Status**: This is an early architectural sketch; the full project rationale, detailed implementation, experimental validation (including bugs fixed during development), and roadmap to a complete organ‑system specification are documented in `docs/physiome.tex`.

**KEYWORDS:**
Physiology simulator
Rust functional core
Admissibility boundaries
Repair operators
Subsystem independent clocks
Cross‑subsystem coupling via PhysiologicalState
Whole-body modeling
Early architectural sketch
Experimental validation roadmap
