# Radiative Switch Computation Laboratory

This directory provides a simulation-oriented computational framework for **Radiative Switch Computation: Computation as Containment**.

The laboratory models coupled phase-change radiative switches as hybrid thermal dynamical systems whose thermal regulation and computation are identical physical processes. The emphasis is not on digital control, but on the evolution of admissible trajectories through coupled thermal fields.

The computational cycle is

Environment
    ↓
Absorption
    ↓
Phase Transition
    ↓
Radiative Exchange
    ↓
Cooling
    ↓
Constraint Satisfaction
    ↓
Updated Thermal Field
    ↓
Environment

The primitive object is the field state

x = (T, φ, H, R, C)

where

T = temperature field

φ = phase state of each PCM element

H = hysteresis state

R = radiative coupling network

C = conductive coupling network

---

## Simulation Philosophy

The accompanying essay develops the theoretical foundations of xylomorphic computation.

This laboratory provides numerical implementations suitable for experimentation and visualization.

Whenever the paper introduces an idealized model, the laboratory distinguishes

Paper Model
    ↓
Simulation Refinement

where numerical approximations, discretization, and implementation assumptions are made explicit.

The simulations are intended to reproduce qualitative behavior rather than serve as engineering design software.

---

## Laboratory Structure

common.py
    Shared configuration, utilities, metrics, visualization, and archiving

01_single_pcm_switch.py
    Individual phase-change switch

02_threshold_arrays.py
    Heterogeneous threshold populations

03_hysteresis_memory.py
    Memory through thermal hysteresis

04_conductive_coupling.py
    Local thermal diffusion

05_radiative_coupling.py
    Long-range radiative interaction

06_hybrid_fields.py
    Combined conductive and radiative fields

07_constraint_relaxation.py
    Gradient-flow relaxation

08_performative_vs_representational.py
    Readout and projection experiments

09_house_simulator.py
    Whole-building thermal computation

10_temporal_modes.py
    Continuous, terminal, and accumulative dynamics

11_legibility.py
    Residue and trajectory reconstruction

12_field_scaling.py
    Large coupled-field simulations

13_optimization.py
    Design-space exploration

radiative-switch-laboratory.ipynb
    Primary executable laboratory notebook

radiative-switch-design-studio.ipynb
    Interactive design notebook

---

## Experiment Interface

Every experiment exposes

run_experiment(config)

which returns

ExperimentResult

containing

config

history

metrics

snapshots (optional)

The notebook assumes every experiment follows this common interface.

---

## Dependency Structure

Single Switch
    ↓
Threshold Arrays
    ↓
Hysteresis
    ↓
Conductive Coupling
    ↓
Radiative Coupling
    ↓
Hybrid Fields
    ↓
Constraint Relaxation
    ↓
Readout
    ↓
House Simulation
    ↓
Temporal Modes
    ↓
Legibility
    ↓
Scaling
    ↓
Optimization

Each experiment depends only upon concepts introduced previously.

---

## Mathematical Style

The laboratory uses Unicode mathematical notation throughout.

Examples include

ẋ = F(x)

ẋ = −∇E(x)

φ̇ = G(T,φ)

ΔE = Qin − Qout

Tᵢ

Wᵢⱼ

Hₐ(x)

‖x‖₂

x ∈ Ω

This notation renders correctly on GitHub, VS Code, terminals, and Jupyter notebooks without requiring MathJax.

---

## Reproducibility

Every experiment uses a common ExperimentConfig providing

seed

dt

steps

metadata

Results can be archived using

save_result(result, output_directory)

from common.py.

---

## Notebook

Primary notebook

`labs/radiative-switch/radiative-switch-laboratory.ipynb`

Optional notebook

`labs/radiative-switch/radiative-switch-design-studio.ipynb`

---

## Running

From the repository root

```bash
# Run required laboratory notebooks
scripts/manage.sh notebooks required

# Include optional notebooks
scripts/manage.sh notebooks all

# Execute only this laboratory
jupyter nbconvert \
  --to notebook \
  --execute \
  labs/radiative-switch/radiative-switch-laboratory.ipynb \
  --output-dir /tmp
```

---

## Dependencies

Python ≥ 3.10

NumPy

Matplotlib

Jupyter

ipywidgets (design studio only)

The notebook follows the same progression as the mathematical essay, introducing one computational layer at a time before combining them into coupled radiative-field simulations.
