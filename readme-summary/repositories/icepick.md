# icepick

**Summary**

*Icepick* is a dual‑purpose toolset that converts any code repository into a navigable spatial environment (the “snapshot” side) and turns Vim’s motion commands into a 2D puzzle game where those motions act as operators over a discrete text manifold.  

- **Snapshot Tool (`icepick.sh`)** – Generates a flat, human‑readable file listing the directory tree and readable file contents, delimited by `FILE:` markers. The resulting snapshot can be loaded into a browser engine that parses it into rooms (directories), objects (files), and geometry derived from indentation depth and line length.  
- **3D Browser Engine (`index.html`)** – Renders snapshots in three modes: First‑person raycaster (FP) where file contents become architectural features, top‑down map view (2D), or a text‑mode listing (Terminal). Vim motions are implemented as operators; for example `dd` removes the current line, turning it into an open space.  
- **2D Puzzle Game (`icepick-2d.html`)** – A self‑contained HTML game teaching Vim commands by making them collectible operators over a spatial puzzle environment. Commands appear as glowing letters on the floor and must be collected before use. Terrain includes walls (`#`), boulders (`o`), fragile tiles (`*`), toggles (`=`), register tiles (`R`), etc., each representing constraints that guide movement.  
- **Design Philosophy** – Treats a codebase as a space where Vim’s motion algebra is a language for traversal; deletion corresponds to demolition, and levels are designed so that removing any mechanic makes the level unsolvable rather than harder.  

The repository contains scripts (`icepick.sh`, `main.js`, etc.) plus example snapshots, engine files, and the game HTML file. It is actively maintained with the 2D puzzle playable at a public URL; the 3D engine is functional but still in early stages (mode switching, mobile input, live round‑trip editing pending).  

**KEYWORDS:** icepick tool, codebase snapshot, spatial navigation, Vim motion operators, 2D puzzle game, first-person raycaster, text manifold, directory tree representation, binary file skipping, browser engine rendering modes.
