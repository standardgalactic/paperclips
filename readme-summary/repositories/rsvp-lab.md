# rsvp-lab

**Summary**

The RSVP‑Lab repository provides a modular simulation environment for the **Relativistic Scalar‑Vector Plenum (RSVP)** field framework. It includes:

- Core dynamics (`operators/rsvp.py`) that handle scalar, vector, and plenum fields, with options for fractional Laplacian diffusion.
- Repair operators (`operators/clio.py`) such as standard smoothing, regulatory anisotropic fixes, sheaf gluing obstructions, identity constraints, and economic regulators.
- Semantic attractor handling (`operators/semantic.py`) that implements Coulomb potentials, basin maps, observer projections, and anisotropy indices.
- Topological analysis tools (`operators/topology.py`) for gluing obstructions, connected components, Euler characteristic, persistence diagrams, TARTAN tiling hierarchies, PCA embeddings, synchrony measures, and Gini‑type economic metrics.
- Cosmological extensions (`operators/cosmology.py`) that model Hubble expansion, coupled manifold evolution, extractive economy dynamics (capital/labour/precarity), and structure functions.

The repository is organized into a clear directory layout:

```
notebooks/          – interactive Jupyter notebook with 17 experimental cells
operators/          – Python modules for each component (rsvp.py, clio.py, semantic.py,
                     topology.py, cosmology.py)
data/               – storage for field snapshots (numpy files)
results/            – figures and animations generated during experiments
```

A typical workflow involves opening the notebook `notebooks/rsvp_field_laboratory.ipynb`, running baseline simulation cells to populate history arrays, then executing individual experiment cells in any order. Each cell demonstrates a distinct aspect of RSVP physics—phase metrics, gluing obstructions, TARTAN hierarchies, level‑set topology, semantic attractors, observer projections, fractional Laplacian scans, soliton collisions, Hubble expansion, coupled manifolds, and extractive economy.

Dependencies are minimal (NumPy, SciPy, Matplotlib, IPython) and the package runs entirely on CPU without requiring GPU acceleration. The README explicitly states that all simulations run in reasonable time on a modern laptop.

**KEYWORDS:**
rsvp lab
simulation environment
Relativistic Scalar-Vector Plenum
TARTAN recursive tiling
CLIO constraint repair
semantic attractors
topological metrics
cosmological extensions
fractional Laplacian
Hubble expansion
extractive economy
