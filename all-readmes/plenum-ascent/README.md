# Plenum Ascent – 6DoF Starfield Core

Minimal WebGL2 prototype for a Descent-style cockpit in an RSVP-style universe:

- 3D starfield in all directions
- True 6DoF flight (you actually move through the starfield)
- Star labels from a Stars!-style planet list, rendered on a CRT-green overlay
- No build step; pure ES modules + WebGL2 + two canvases

## Controls

- `W` / `S` – forward / backward
- `A` / `D` – strafe left / right
- `R` / `F` – thrust up / down
- Arrow keys – pitch / yaw
- `Q` / `E` – roll
- `X` – toggle labels

## Running locally

Serve from a simple HTTP server:

```bash
python -m http.server 8000
```

Then open:

```text
http://localhost:8000
```

You should immediately see green stars, be able to fly in all directions, and see planet names over nearby stars.
