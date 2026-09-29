# cosmic-cults

**Summary**

The *cosmic-cults/content-gen* repository provides an AI‑driven pipeline for generating 3D GLB models of game assets (units, buildings, leaders) specific to three factions in the broader **Cosmic Cults** project: the Crimson Covenant, Order of the Deep, and Void Seekers. It leverages Meshy’s text‑to‑3D API, using faction‑specific prompts that reflect each group’s thematic aesthetics—blood rituals/demonic power for the Crimson Covenant; Lovecraftian ocean horror with fish‑human hybrids for the Order of the Deep; and cosmic reality manipulation for the Void Seekers.

Key features include:

- **CLI commands** (`gen:list`, `gen:models`, `gen:models:dry`) to list, preview, or generate assets by faction, type, or specific ID.
- **Dry‑run mode** shows what would be generated without incurring API costs.
- **Preview vs. refined models**: low‑poly previews cost ~$0.10 each; high‑quality refined models (with PBR textures) cost ~$0.20 each.
- **Output structure**: generated GLB files are saved under `generated/models/` with accompanying manifest JSONs for tracking and state management.
- **Extensibility**: new assets can be added by defining their type in the game’s type definitions, creating corresponding prompts, and letting the manifest builder automatically include them.

The repository is designed to integrate directly with the main Cosmic Cults codebase via asset loaders that read from `public/models/`, ensuring generated models are ready for use in the game engine. It also includes troubleshooting guidance for common issues like missing API keys or rate‑limit errors, and outlines future enhancements such as animation generation and LOD optimization.

**KEYWORDS:**
cosmic-cults
content-gen
3D asset generation
Meshy API
AI text-to-3D
Crimson Covenant
Order of the Deep
Void Seekers
GLB models
preview vs refined
CLI commands
manifest builder
integration with game engine
future enhancements (animation, LOD)
