# Magnetic Fluidic Computing: Formal Mathematics for Simulation

This directory turns the mathematical ideas in *Magnetic Fluidic Computing: Circulation, Admissibility, and the Architecture of Trajectory* into a simulation-oriented mathematical specification suitable for Python and Jupyter notebooks.

The machine is treated as a closed circulation system

Dock → Compute → Heat → Eject → Cool → Return → Dock

where pods move continuously through a routing network under the influence of magnetic, hydraulic, thermal, and scheduling fields.

The primitive object is not a processor or memory location but an admissible trajectory

τ : t ↦ x(t)

through state space.

Memory is represented as recurrent trajectories,

τ₁ ≈ τ₂,

rather than fixed storage locations.

Accessibility entropy measures the richness of future motion

Hₐ(x) = −Σ pᵢ(x) log pᵢ(x),

while machine identity is associated with persistent circulation patterns rather than individual physical pods.

---

## Simulation Philosophy

The source paper develops a theoretical description of magnetic-fluidic computation.

These notes instead provide numerical models suitable for simulation.

Whenever the paper presents an idealized mathematical statement, the laboratory distinguishes

Paper Model
    ↓
Simulation Refinement

where the refinement makes assumptions explicit, introduces numerical approximations, and produces equations that can be integrated using ordinary differential equation solvers.

The refinement supplements the theory rather than replacing it.

---

## Dependency Structure

State Space
    ↓
Forces and Routing
    ↓
Thermal Cycle
    ↓
Trajectory Memory
    ↓
Accessibility
    ↓
Geometry
    ↓
Collective Dynamics
    ↓
Agency and Attractors

Each stage depends only upon the previous mathematical layer.

---

## Mathematical Style

Throughout the laboratory we use Unicode mathematical notation rather than LaTeX.

Examples include

ẋ = F(x,u)

ẍ = M⁻¹F

τ = (x₀,x₁,…,xₙ)

Hₐ = −Σ pᵢ log pᵢ

ΔE = Q − W

∇E

λ₁ ≥ λ₂ ≥ ⋯ ≥ λₙ

x ∈ Ω

A ⊂ B

‖x‖₂

This notation renders correctly in GitHub, Jupyter notebooks, terminals, VS Code, and plain text editors without requiring MathJax.

---

## Notebook

Primary notebook

/home/runner/work/bash-functions/bash-functions/labs/magnetic-fluidic-mathematics/magnetic_fluidic_computing_lab.ipynb

---

## Running

From the repository root

```bash
scripts/manage.sh notebooks required

jupyter nbconvert \
  --to notebook \
  --execute \
  labs/magnetic-fluidic-mathematics/magnetic_fluidic_computing_lab.ipynb \
  --output-dir /tmp
```

The notebook follows the same dependency order as the mathematical notes.

Each section introduces one layer of the model before numerical experiments are performed.

Simulation code should import definitions incrementally rather than implementing the complete machine simultaneously.
