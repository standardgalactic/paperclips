# Neuroblox.jl

**Summary**

Neuroblox.jl is a Julia package tailored for computational neuroscience and psychiatry. It provides modular “blox” (building blocks) that represent individual neurons, neural mass models, and biomimetic control circuits using symbolic dynamic differential equations described via ModelingToolkit.jl. These blox can be assembled into large-scale brain dynamics simulations capable of handling spiking neuron activity, population-level modeling, and interactions with physiological systems. The package includes a user-friendly GUI for model assembly and automatically generates high-performance numerical ODE/SDE solvers for simulation. Parameter fitting to electrophysiological and neuroimaging data is performed using Turing.jl’s probabilistic modeling techniques (Hamilton‑Monte‑Carlo sampling and ADVI). Benchmark tests show simulation speeds exceeding 100× faster than comparable Python implementations like the Virtual Brain.

**KEYWORDS:** Neuroblox.jl, computational neuroscience, psychiatry, modular blox, symbolic dynamic differential equations, ModelingToolkit.jl, neural mass models (Jansen-Rit, Wilson-Cowan), Hodgkin-Huxley, IF, QIF, LIF neurons, control circuit elements, GUI for model assembly, simulation speed benchmark, 100× faster than Virtual Brain, Turing.jl probabilistic modeling.
