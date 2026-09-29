# history

**Summary**

The *history* repository contains Python scripts and associated Blender assets used to create visualizations that support research on **history‑based models of computation**. The core idea is that computation can be modeled as the extension, merging, and reduction of event histories—mirroring how data structures such as Directed Acyclic Graphs (DAGs) or CRDT convergence states evolve over time.

Key components include:

- `figure_factory.py` – entry point for Blender to build visualization scenes.
- Scene generators (`scenes_*.py`) that produce specific visualizations:
  - History DAGs
  - History lattices
  - Convergence structures of Conflict‑Free Replicated Data Types (CRDTs)
  - Entropy collapse dynamics
  - Constraint‑descent (Ising‑style) models

The repository also provides build scripts (`build_all.sh`, `run_blender.sh`) to generate rendered PNG images and Blender `.blend` files for further manipulation.

**Implementation status:** The repository is actively maintained with up‑to‑date figures, but some visualizations are still considered experimental prototypes. All generated outputs are intended as research artifacts rather than production tools.

**Relationships:** These visualizations complement the accompanying academic papers (e.g., *Following the Evaluator*, *Geometry of Cellular Possibility*) and provide concrete graphical evidence for concepts discussed in those documents.

**Keywords**

history, computation, event histories, Directed Acyclic Graphs, CRDT convergence, constraint dynamics, visualization, Blender, Python scripts, research artifacts.
