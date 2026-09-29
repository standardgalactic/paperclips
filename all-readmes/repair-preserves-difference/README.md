# Repair Preserves Difference

This repository is a small experimental investigation generated from a theoretical proposition. Its purpose is not to assume that the proposition is correct, but to turn it into something sufficiently explicit that consequences can be inspected, simulated, measured, criticized, or rejected.

[Microsecurity for Microprofessionals](https://standardgalactic.github.io/repair-preserves-difference/microsecurity-for-microprofessionals.pdf)

[Monotonic Continuation](https://standardgalactic.github.io/repair-preserves-difference/monotonic-continuation.pdf)

* [Slides](https://standardgalactic.github.io/repair-preserves-difference/Monotonic_Continuation.pdf)

[Executable Monotonic Continuation](https://standardgalactic.github.io/repair-preserves-difference/executable-monotonic-continuation.pdf)

[The North Setpoint](https://standardgalactic.github.io/repair-preserves-difference/north-setpoint.pdf)

[What Affect Permits](https://standardgalactic.github.io/repair-preserves-difference/what-affect-permits.pdf)

[Provenance Authorship](https://standardgalactic.github.io/repair-preserves-difference/provenance-authorship.pdf)

[The Right to Remain Unmediated](https://standardgalactic.github.io/repair-preserves-difference/right-to-remain-unmediated.pdf)

* [Architecting Human Agency](https://standardgalactic.github.io/repair-preserves-difference/Architecting_Human_Agency.pdf) — *Notes*

![](reference-guide.png)

**Domain:** General

**Theory seed:** `repair preserves difference`

## Research question

What observable consequences follow if "repair preserves difference" is treated as an operative principle in general?

## Working hypothesis

If "repair preserves difference" is structurally relevant to general, then systems organized around that principle should exhibit measurable differences in persistence, failure, recovery, or reachable state compared with an unconstrained baseline.

## Null hypothesis

Operationalizing "repair preserves difference" produces no systematic difference from the baseline model in the selected measurements.

## Operationalization

Introduce an explicit constraint or transformation representing "repair preserves difference" and compare the resulting trajectories with an otherwise equivalent baseline.

## Measurements

Measure persistence, divergence, recovery cost, state reachability, constraint violations, and sensitivity to perturbation.

## Experimental structure

The repository separates the conceptual seed from its operationalization. The
theory is recorded in `theory.md`; the proposed experiment is specified in
`experiment.md`; machine-readable project metadata is stored in
`project.json`; executable investigations belong in `experiments/`; raw or
generated observations belong in `data/`; and interpreted outputs belong in
`results/`.

The initial repository should therefore be understood as a conjecture made
executable rather than as a finished research result.

## Interactive Laboratory

**[→ Open the Observatory of Small Strange Machines](index.html)**

A single-file, dependency-free computational laboratory containing 7 interconnected experiments. Each experiment is both a computational artifact and a lens for observing the "repair preserves difference" hypothesis.

**Features:**
- Cellular automaton lab with mutable rules
- TARTAN field sandbox with multiple representations
- HYDRA distributed repair experiment
- MAGI interpretation engine
- RAT adversarial agent
- Base-3/2 arithmetic machine
- Yarncrawler recursive endofunctor visualization
- Complete terminal interface
- State history with branching
- Seeded world generation (reproducible)
- Export to JSON

**Quick start:**
```bash
open index.html              # Random seed
open index.html?seed=42      # Reproducible seed
```

See [OBSERVATORY.md](OBSERVATORY.md) for complete documentation.

---

## Running experiments

### Quick start

Run a single experiment:
```bash
python experiments/01_string_repair.py
bash experiments/03_file_repair.sh
```

Run all experiments and generate summary:
```bash
bash scripts/run_all_experiments.sh
```

Test that all experiments execute successfully:
```bash
python scripts/test_experiments.py
```

### Available experiments

Six concrete experiments operationalize "repair preserves difference":

1. **String Repair** (`01_string_repair.py`) - String corruption/recovery
2. **Network Repair** (`02_network_repair.py`) - Network node failure/recovery
3. **File Repair** (`03_file_repair.sh`) - File system corruption/repair
4. **Process Repair** (`04_process_repair.sh`) - Process failure/restart
5. **Population Dynamics** (`05_population_dynamics.py`) - Population replacement
6. **Database Repair** (`06_database_repair.sh`) - Database consistency repair

Each compares:
- **Baseline**: Repair that homogenizes (resets to canonical state)
- **Intervention**: Repair that preserves differences

See `experiments/README.md` for detailed documentation.

## Generated project

This repository was scaffolded by `genrepo`.

Generation does not constitute evidence for the theory. The purpose of the
generator is to reduce the cost of moving from an abstract proposition to an
inspectable experimental object.
