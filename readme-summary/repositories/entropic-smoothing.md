# entropic-smoothing

Summary:

The Entropic Smoothing repository implements a technique for progressively smoothing a deterministic noise field applied to identical radial strata of a 3D model. The deformation amplitude follows an exponential decay (`initial_roughness * exp(-decay_rate * stratum)`) so that higher strata become smoother without altering the underlying construction. A Blender script (`generate.py`) reproduces this effect, producing a blend file and PNG frames; if `ffmpeg` is available, it also outputs an H.264 video. The upper dome animation demonstrates the transition from initial roughness to near-smoothness while keeping other elements (footprint, camera, lighting) constant for direct comparison across frames. Preset parameters are defined in JSON files, allowing reproducible results via a fixed seed.

KEYWORDS:
Entropic Smoothing, noise field, exponential decay, Blender 3.0, render script, metadata JSON, PNG frames, H.264 MP4, deterministic construction, visual reconstruction, preset parameters.
