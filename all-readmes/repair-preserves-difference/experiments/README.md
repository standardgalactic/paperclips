# Experiments Documentation

This directory contains concrete operationalizations of the "repair preserves difference" theoretical proposition across multiple domains.

## Experiment Overview

Each experiment compares two approaches:

1. **Baseline**: Repair that homogenizes (resets to canonical/uniform state)
2. **Intervention**: Repair that preserves differences (maintains distinctiveness)

## Available Experiments

### Python Experiments

#### 01_string_repair.py
**Domain**: String corruption and recovery  
**Question**: Does repair that preserves distinctiveness between corrupted strings lead to greater state diversity?

- **Baseline**: All repairs reset to single canonical string
- **Intervention**: Repairs preserve difference patterns between strings
- **Measurements**: State persistence, recovery cost, violations, reachable states

```bash
python experiments/01_string_repair.py
```

#### 02_network_repair.py
**Domain**: Network node failure and recovery  
**Question**: Does difference-preserving repair affect network robustness?

- **Baseline**: Failed nodes repair to identical state
- **Intervention**: Repaired nodes maintain distinctions from neighbors
- **Measurements**: Network connectivity, repair operations, state diversity

```bash
python experiments/02_network_repair.py
```

#### 05_population_dynamics.py
**Domain**: Population replacement over time  
**Question**: Does replacement that preserves trait diversity lead to different population dynamics?

- **Baseline**: Replace deaths with "average" individuals
- **Intervention**: Replace with individuals preserving trait variance
- **Measurements**: Trait variance persistence, population collapses, state diversity

```bash
python experiments/05_population_dynamics.py
```

### Bash Experiments

#### 03_file_repair.sh
**Domain**: File system corruption and repair  
**Question**: Does file repair that preserves file-specific characteristics maintain greater diversity?

- **Baseline**: Repair all files using single template
- **Intervention**: Repair preserving file-specific patterns
- **Measurements**: Content diversity, generic vs specific patterns

```bash
bash experiments/03_file_repair.sh
```

#### 04_process_repair.sh
**Domain**: Process failure and restart  
**Question**: Does recovery that preserves process distinctions lead to observable diversity?

- **Baseline**: Failed processes restart with identical configuration
- **Intervention**: Processes restart preserving their original configurations
- **Measurements**: Configuration diversity, log patterns

```bash
bash experiments/04_process_repair.sh
```

#### 06_database_repair.sh
**Domain**: Database consistency repair  
**Question**: Does repair preserving record-specific patterns maintain greater data diversity?

- **Baseline**: Repair inconsistencies with canonical values
- **Intervention**: Repair preserving record identity and patterns
- **Measurements**: Value diversity across fields

```bash
bash experiments/06_database_repair.sh
```

## Running All Experiments

```bash
# Run all Python experiments
for exp in experiments/*.py; do
    echo "=========================================="
    echo "Running: $exp"
    echo "=========================================="
    python "$exp"
    echo ""
done

# Run all Bash experiments
for exp in experiments/*.sh; do
    echo "=========================================="
    echo "Running: $exp"
    echo "=========================================="
    bash "$exp"
    echo ""
done
```

## Interpreting Results

Each experiment reports:

- **Persistence**: How well the system maintains diversity over time
- **Recovery cost**: Resource consumption during repair
- **Violations**: Invalid/collapsed states reached
- **Reachable states**: Unique configurations explored

### Expected Patterns

If "repair preserves difference" is operationally meaningful:

- ✓ Intervention should show **greater state diversity** than baseline
- ✓ Intervention might have **similar or higher recovery cost**
- ✓ Intervention should reach **more unique configurations**

### Null Result

If no systematic difference appears, this suggests:

1. The operationalization poorly captures the theoretical proposition
2. The domain doesn't exhibit the predicted behavior
3. The proposition has no consequence under these conditions

## Failure Criteria

The experiments fail to support the hypothesis if:

1. No consistent difference between baseline and intervention
2. Observed differences depend entirely on arbitrary implementation choices
3. A simpler mechanism accounts for the same observations

## Extension

To add new experiments:

1. Create `experiments/NN_domain_name.{py,sh}`
2. Implement baseline and intervention functions
3. Measure: persistence, recovery_cost, violations, reachable_states
4. Compare and interpret results
5. Update this README

## Generated Scaffold

These experiments were designed to make the theoretical proposition "repair preserves difference" inspectable and falsifiable through concrete implementations.
