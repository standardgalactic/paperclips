# plenum-ascent

Summary:

The Plenum Ascent repository provides a minimal WebGL2 prototype designed for creating a Descent-style cockpit experience within an RSVP (Rapid Serial Visual Presentation) universe. Its core features include:

- A fully immersive 3D starfield visible in all directions.
- True six degrees of freedom (6DoF) flight mechanics, allowing users to move dynamically through the simulated space.
- Star labeling using a dataset derived from the Stars! planet list, rendered on a CRT‑green overlay for historical authenticity.
- No compilation step; the project is built entirely with pure ES modules, WebGL2 graphics API, and two separate canvases for rendering.

Controls are straightforward: `W`/`S` manage forward/backward thrust, `A`/`D` handle left/right strafing, `R`/`F` control vertical ascent/descent, arrow keys adjust pitch/yaw, and `Q`/`E` provide roll maneuvers. The toggle key `X` switches the visibility of star labels.

To run locally, start a simple HTTP server with:

```bash
python -m http.server 8000
```

Then access the application at:

```text
http://localhost:8000
```

Upon loading, users will see green‑colored stars, can navigate freely in all spatial directions, and have planet names overlaid on nearby stars for contextual identification.

KEYWORDS:
Plenum Ascent, WebGL2, Descent-style cockpit, RSVP universe, 6DoF flight, starfield rendering, Stars! dataset, CRT overlay, ES modules, HTTP server.
