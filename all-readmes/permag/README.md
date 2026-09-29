# PerMag

**Per-monitor magnification for Windows.**

PerMag is an experimental Windows magnifier written in Rust. Its goal is to let each physical monitor have its own independent magnification level.

For example:

```text
Monitor 1                         Monitor 2
┌─────────────────────┐           ┌─────────────────────┐
│                     │           │                     │
│   movie at 1.0×     │           │   browser at 2.0×   │
│                     │           │                     │
│   untouched         │           │   magnified         │
│                     │           │                     │
└─────────────────────┘           └─────────────────────┘
```

The important distinction is that magnification belongs to a **monitor**, not to the global virtual desktop.

PerMag is currently a prototype and is not yet ready for normal use.

## Goals

PerMag is being designed around a few core requirements:

* independent magnification state for every physical monitor;
* pointer-anchored fractional zoom;
* natural pointer movement across differently magnified monitors;
* arbitrary Windows monitor layouts, including negative coordinates and partial shared edges;
* ordinary application mouse-wheel behavior remains intact;
* a monitor at `1.0×` should have no PerMag capture/rendering path at all.

The intended default zoom gesture is:

```text
Ctrl + Alt + Mouse Wheel
```

This leaves application shortcuts such as `Ctrl+Wheel` untouched.

## Current state

The portable geometry and input model is implemented and tested.

Live Windows experiments have demonstrated:

* monitor enumeration and arbitrary desktop topology;
* low-level physical mouse observation;
* transformed pointer movement at 2× and 2.25×;
* transitions between magnified and unmagnified monitors;
* release of PerMag pointer ownership on a 1× monitor;
* creation and placement of a full-monitor overlay on either physical display.

The graphics path is now under development.

See [STATUS.md](STATUS.md) for detailed milestone status, experimental results, architecture notes, and remaining work.

## Architecture

The intended graphics path is:

```text
Windows Graphics Capture
          │
          ▼
    D3D11 texture
          │
          ▼
  viewport crop/scale
          │
          ▼
     DXGI overlay
          │
          ▼
   physical monitor
```

The portable core maintains the authoritative viewport geometry. The Windows graphics layer will consume that state rather than implementing a separate magnification model.

At `1.0×`, the eventual goal is to remove the overlay and capture path entirely for that monitor.

## Source layout

```text
src/
├── bin/
│   ├── win_observe.rs   # Win32 input observations
│   ├── win_overlay.rs   # overlay experiments
│   └── win_pointer.rs   # live transformed pointer
├── input.rs
├── lib.rs
├── monitor.rs
├── state.rs
├── viewport.rs
└── win.rs

tests/
├── common/
├── input.rs
├── state.rs
├── topology.rs
└── viewport.rs
```

The programs under `src/bin/` are currently development probes. They preserve empirical Windows tests that are difficult to represent as ordinary unit tests.

## Building

The portable core can be tested normally with Cargo:

```bash
cargo test
```

Windows-specific probes require the native Windows MSVC Rust toolchain.

When working with the source tree through WSL, build artifacts should be placed on the Windows filesystem. For example, from a Visual Studio Developer PowerShell:

```powershell
$env:CARGO_TARGET_DIR = "C:\Users\nateg\permag-target"
$env:CARGO_INCREMENTAL = "0"

cargo check
```

Individual probes can then be run with commands such as:

```powershell
cargo run --bin win_observe
cargo run --bin win_pointer
cargo run --bin win_overlay
```

These are diagnostic programs, not the final PerMag application.

## Status

PerMag is experimental software under active development.

The current work is establishing the Windows graphics path:

1. final overlay behavior;
2. D3D11/DXGI presentation;
3. Windows Graphics Capture;
4. viewport crop and magnification;
5. integration with the existing transformed-pointer system.

For the complete development state and test results, see **[STATUS.md](STATUS.md)**.

## Central invariant

> **Magnification is a property of a monitor, not of the desktop.**

A monitor at 1× should behave as though PerMag is not touching it.

