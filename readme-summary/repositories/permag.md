# permag

**Summary:**

PerMag is an experimental Windows magnifier written in Rust that enables each physical monitor to have its own independent magnification level (e.g., Monitor 1 can be set to 1.0× while Monitor 2 can be at 2.0×). It aims to provide pointer‑anchored fractional zoom, natural mouse movement across differently scaled monitors, and preserves ordinary application mouse‑wheel behavior on non‑magnified displays. The software currently functions as a prototype; it supports monitor enumeration, arbitrary desktop topologies, low‑level physical mouse observation, transformed pointer movement at various magnifications, and transitions between magnified and unmagnified states. It also includes the creation of a full‑monitor overlay that can be released on 1× monitors. The graphics path is being developed to capture Windows graphics via D3D11 textures, crop/scale them, and render onto physical displays. Building requires Cargo for unit tests and MSVC Rust toolchain for Windows-specific probes.

**KEYWORDS:**
PerMag
Windows magnifier
Rust
independent monitor magnification
fractional zoom
pointer movement across monitors
experimental prototype
D3D11 graphics capture
overlay implementation
STATUS.md documentation
