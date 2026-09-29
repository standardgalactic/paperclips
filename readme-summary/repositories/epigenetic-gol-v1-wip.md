# epigenetic-gol-v1-wip

Below is an analysis of the provided text focusing on its structure, purpose, and key points related to biological realism in the context of the described project. The content has been organized for clarity and coherence:

### Project Overview

- **Purpose**: The project aims to explore evolved gene sequence interpreters using a simplified evolutionary algorithm framework. It is not intended to model or simulate cellular biology in a realistic manner but rather to investigate how an evolved program can interpret genetic sequences.

### Key Features

1. **Nested Evolution Architecture**:
   - Unlike natural evolution, which progresses continuously and dynamically, this project uses discrete generations for species evolution.
   - This abstraction simplifies the problem of evolving complex biological systems without needing a fully realistic model of continuous development and interaction among cells.

2. **Division of Components**:
   - The separation into `PhenotypeProgram`, `Genotype`, and `make_phenotype` is not biologically accurate but serves to simplify the implementation.
   - These components resemble concepts like methylation or hox genes in a loose sense, providing an interesting parallel without being directly modeled after natural systems.

3. **Gene Bias Concept**:
   - Inspired by canalization in biology, gene bias constrains phenotypic diversity by ensuring certain critical behaviors are maintained across generations.
   - This differs from the natural process where genetic pathways interconnect to buffer against mutations affecting essential functions.

### Biological Realism Considerations

- **Simplified Representation**: The project's design abstracts away many complexities of real cellular biology, such as continuous development and interaction among multiple cells in a multicellular organism.
- **Development Process**: Unlike living organisms that develop dynamically over time with ongoing interactions between genetic pathways, the project simulates development all at once from an initial state defined by the `PhenotypeProgram`.
- **Fitness Function & Selection**:
  - In nature, fitness and selection are not governed by explicit functions but arise from survival and reproductive success.
  - The project uses a more deterministic approach where fitness is implicitly determined by the evolutionary framework's rules.

### Execution Requirements

- **Hardware**: Requires a CUDA-enabled GPU with sufficient memory (e.g., RTX a5000) due to large memory requirements and computational intensity.
- **Software Dependencies**:
  - Python 3.10 or compatible versions.
  - Libraries such as pybind11, CUDA development tools, nvcomp library, along with common data analysis and visualization packages like NumPy, Pandas, Matplotlib, etc.

### Execution Scripts

- **run_experiments.py**: Executes all experiments defined in `experiments.experiment_list` and visualizes results using `visualize_results.py`.
- **visualize_results.py**: Generates tables, simulation videos, and charts summarizing the outcomes of the experiments.
- **benchmark.py**: Measures runtime performance of the inner loop and compares it across different runs for optimization purposes.
- **trace_species_evolution.py**: Runs a few generations of species evolution to produce detailed summaries of each run's progression.

### Biological Realism Summary

The project is an abstract exploration rather than a direct simulation of biological systems. It leverages concepts from cellular biology (like methylation and hox genes) in a simplified manner but does not aim for realistic modeling of development, fitness determination, or genetic regulation as they occur naturally in organisms.

This structured breakdown should help clarify the intentions behind the project's design choices and its departure from true biological realism.
