# Batch 14

**Project Overview**

The repository you’re looking at is a **scaffold for ZebraTube**, an ecosystem that consists of four main components:

| Component | Primary Function |
|-----------|-------------------|
| **zebra‑core** | Crawls text sources, extracts a *canonical semantic graph* (via exactly one LLM call), and manages projection scripts. |
| **zebra‑agent** | Acts as a local capability & interest scanner to power personalized task recommendation engines. |
| **zebratube‑api** | Provides the backend via FastAPI for API-driven interactions, handling video metadata, authentication, playback control, etc. |
| **zebratube‑web** | Contains the React/Vite frontend UI that displays project maps and other visualizations on `http://localhost:3000`. |

The README explicitly states that this is an **incomplete scaffold**, meant to be extended into a fully functional prototype rather than a production‑ready product.

---

### Core Design Principles

1. **Canonical Semantic Graph**  
   - Represents the text’s underlying constraints without collapsing ambiguity.  
   - *Ambiguity nodes* are treated as first‑class objects, preserving “underdetermination”.

2. **Predation‑Resistant Field**  
   - The system preserves textual ambiguity so that interpretations remain open until sufficient constraints resolve them.

3. **Constraint Simulator**  
   - Meaning emerges from local propagation of activation along typed edges (e.g., `causes`, `resolves`), analogous to reaction‑diffusion dynamics in a zebra’s stripe pattern.

4. **Deterministic Python Processing**  
   - All downstream steps after the initial LLM extraction are deterministic, ensuring reproducibility and scalability.

---

### Key Concepts & Keywords

- **Canonical Semantic Graph**: A graph that captures every possible interpretation of the text.
- **Task Economy**: Bounties calculated by a point formula (scarcity × assembly weight) to prevent redundant work.
- **Ten Zebra Verbs**: Commands for extraction, projection, scripting, crawling, wiki generation, serving, searching, diffing, person graphing, and rendering visualizations.
- **Philosophy**: Rejects single‑realization interpretations; treats texts as multi‑potential structures that scale to collaborative production.

**Keywords**

`zebratube`, `distributed compiler`, `semantic graph`, `task economy`, `media production pipeline`, `recursive corpus expansion`, `textual ambiguity preservation`.

---

### How to Get Started

1. **Run Docker Services**
   ```bash
   docker-compose up postgres redis
   ```

2. **Install Dependencies & Start API**
   ```bash
   pip install -e .
   uvicorn app.main:app --reload
   ```

3. **Launch Web UI**  
   Open `http://localhost:3000` – the project appears on the homepage map.

4. **Ingest a Repository**
   ```bash
   ollama serve &
   ./zebra/zebra crawl ~/my-project --stem myproject
   ./zebra/zebra scripts --stem myproject

   python3 -m app.workers.ingest \
     --project-slug myproject \
     --zebra-dir    data \
     --stem         myproject
   ```

5. **Contributors can start producing media**  
   Rendered pieces feed back into the pipeline via `zebra recycle`.

---

### Detailed Technical Summary

- **LLM Extraction**: Exactly one call to a local LLM (e.g., Ollama) extracts the canonical semantic graph from any textual input.
- **Projection Modules**: The extracted graph is then projected into ten distinct interpretive outputs:
  - Film storyboard
  - Constraint diagram
  - Ambiguity diffusion animation
  - Concept field map
  - Timeline visualization
  - Character state visualizations
  - Sonic arc representation
  - Rhetorical structure
  - Logical skeleton

- **Node & Edge Types**  
  The graph includes eight node types (`entities`, `events`, `relations`, `claims`, `ambiguities`, `transformations`, `timeline`, `themes`) and typed edge labels (e.g., `causes`, `resolves`).

- **Architecture Diagram**: Shows the flow from text → LLM extraction → canonical graph → ten projection modules, emphasizing deterministic downstream processing.

---

### Development Status

The repository is intentionally left as a **scaffold**. It provides:

- Installation instructions for required packages (`requests`, `matplotlib`, `networkx`, optional embeddings & MIDI libraries).
- CLI commands (`zebra extract`, `zebra project`, `zebra render`, `zebra simulate`) that operate on pre‑extracted canonical graphs stored in `data/canonical/`.
- Projection aliases mapping short names to full output types (e.g., `ambiguity` → `ambiguity_diffusion`).

Future work will likely involve:

- Full implementation of each projection module.
- Integration with a user interface for interactive exploration.
- Additional plugins or extensions following defined registration tables.

---

### Keywords Summary

```
text analysis
semantic graph
LLM extraction (single call)
predation‑resistant field
ambiguity nodes
constraint propagation
reaction diffusion dynamics
film storyboard
constraint diagram
ambiguity diffusion animation
concept field map
timeline visualization
character state vectors
sonic arc representation
rhetorical structure
logical skeleton
CLI project render simulate
Python deterministic processing
Ollama local LLM server
networkx graph schema
```

---

**Bottom Line**

`zebragraph` (or ZebraTube) is a **predation‑resistant text analysis engine** that preserves textual ambiguity, uses exactly one LLM call to produce a canonical semantic graph, and then projects this constraint field into multiple visual and narrative representations. It’s designed for collaborative production of media from ambiguous texts while ensuring deterministic downstream processing.

Feel free to ask if you need deeper details on any specific component or how to extend the project!
