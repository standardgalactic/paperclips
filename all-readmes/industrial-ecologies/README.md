# Industrial Ecologies

[Industrial Ecologies as Executable Arguments](https://standardgalactic.github.io/industrial-ecologies/industrial-ecologies.pdf)

[Rendering as Admissibility Check](https://standardgalactic.github.io/industrial-ecologies/admissibility-check.pdf)

Deterministic headless Blender simulations of factories, laboratories, food
processing, recycling, and ecological material cycles. The project treats every
facility as a coupled material–energy–water system: recovery paths are visible,
losses are named, and no waste stream disappears into an unmodeled sink.

## Render

```bash
bash experiments/render_all.sh experiments/output
```

Each simulator produces a PNG, a reusable `.blend` file, and a JSON sidecar
containing its nominal process metrics (see
[experiments/METRICS.md](experiments/METRICS.md) for the schema and a
per-scene reference). Blender 4.0 and 4.2+ are selected automatically. No
external assets or add-ons are required.

## Interfaces

[Nothing Vanishes](https://standardgalactic.github.io/industrial-ecologies/nothing-vanishes.html) — *Interactive Explorer*

[Output Visualizer](https://standardgalactic.github.io/industrial-ecologies/) *Live Demo*

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for how to add a new simulation.

## License

[MIT](LICENSE)
