# Flash Reluctance Laboratory

This directory turns the mathematical ideas behind flash-reluctance engines into a simulation-oriented mathematical specification suitable for Python and Jupyter notebooks.

The machine is treated as a coupled hybrid dynamical system in which thermal, electromagnetic, mechanical, and control processes evolve simultaneously.

Energy Flow

Electrical Input
        ↓
Thermal Core
        ↓
Flash Expansion
        ↓
Pressure Pulse
        ↓
Rotor Torque
        ↓
Electromagnetic Recovery
        ↓
Control
        ↓
Next Cycle

Rather than viewing the engine as independent subsystems, the laboratory models the complete machine as a single evolving state

x = (T, P, θ, ω, I, V, s, q)

where

T = thermal state

P = chamber pressure

θ = rotor angle

ω = angular velocity

I = motor current

V = supply voltage

s = controller state

q = chamber phase variables

---

## Simulation Philosophy

The accompanying paper develops an idealized mathematical description of flash-reluctance engines.

These notes provide simulation-safe numerical models suitable for Python implementations.

Whenever the paper presents an analytical model, the laboratory distinguishes

Paper Model
    ↓
Simulation Refinement

where the refinement makes numerical assumptions explicit while preserving the qualitative behavior.

---

## Contents

00_state_space.md
    Hybrid state variables, constraints, geometry

01_thermal_core.md
    Chamber and thermal recovery dynamics

02_flash_thermodynamics.md
    Injection, vaporization, pressure generation

03_pressure_and_torque.md
    Pressure-to-torque mappings

04_rotor_dynamics.md
    Mechanical equations of motion

05_reluctance_motor.md
    Electromagnetic torque production

06_control_systems.md
    Feedback control and scheduling

07_hybrid_energy.md
    Energy accounting across subsystems

08_operating_regimes.md
    Stable, oscillatory, stalled, and collapse regimes

09_stability_and_bifurcations.md
    Continuation methods and bifurcation analysis

10_optimization.md
    Performance optimization

11_uncertainty_and_manufacturing.md
    Manufacturing tolerance and robustness

12_experimental_invariants.md
    Numerical invariants and verification tests

flash_reluctance_laboratory.ipynb
    Primary executable laboratory notebook

---

## Dependency Structure

State Space
    ↓
Thermal Core
    ↓
Flash Thermodynamics
    ↓
Pressure Generation
    ↓
Rotor Dynamics
    ↓
Reluctance Motor
    ↓
Control Systems
    ↓
Hybrid Energy
    ↓
Operating Regimes
    ↓
Stability
    ↓
Optimization
    ↓
Uncertainty
    ↓
Experimental Invariants

Each layer depends only on the mathematics introduced above it.

---

## Mathematical Style

The laboratory uses Unicode mathematical notation throughout.

Examples include

ẋ = F(x,u)

Mẍ + Cẋ + Kx = τ

Ṗ = f(T,m)

ω̇ = τ/J

ΔE = Q − W

η = Pₒᵤₜ/Pᵢₙ

∇J(x)

λ₁ ≥ λ₂ ≥ ⋯ ≥ λₙ

x ∈ Ω

‖x‖₂

This notation renders correctly on GitHub, VS Code, terminals, and Jupyter notebooks without requiring MathJax.

---

## Notebook

Primary notebook

`labs/flash-reluctance-laboratory/flash_reluctance_laboratory.ipynb`

Optional notebooks

None

---

## Running

From the repository root

```bash
# Run required laboratory notebooks
scripts/manage.sh notebooks required

# Execute this laboratory
jupyter nbconvert \
  --to notebook \
  --execute \
  labs/flash-reluctance-laboratory/flash_reluctance_laboratory.ipynb \
  --output-dir /tmp
```

The notebook follows the same dependency order as the mathematical notes.

Each section introduces one mathematical layer before numerical experiments are performed. Simulation code should build the complete engine incrementally rather than implementing every subsystem simultaneously.
