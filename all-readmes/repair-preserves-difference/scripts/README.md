# Scripts Directory

Automation and analysis tools for running and interpreting the "repair preserves difference" experiments.

## Available Scripts

### run_all_experiments.sh

**Purpose**: Execute all experiments and generate comprehensive summary report

**Usage**:
```bash
bash scripts/run_all_experiments.sh
```

**Output**:
- Creates timestamped directory: `results/run_YYYYMMDD_HHMMSS/`
- Saves individual experiment outputs: `*_output.txt`
- Generates summary report: `SUMMARY.md`

**Features**:
- Runs all Python experiments (`.py`)
- Runs all Bash experiments (`.sh`)
- Captures full output from each experiment
- Extracts key results and interpretations
- Creates unified summary with conclusions

**Example**:
```bash
$ bash scripts/run_all_experiments.sh

Repair Preserves Difference - Experiment Suite
==============================================================
Repository: repair-preserves-difference
Run timestamp: 20260811_204500
Results directory: results/run_20260811_204500

PYTHON EXPERIMENTS
==============================================================
Running: 01_string_repair.py
...

Summary report generated: results/run_20260811_204500/SUMMARY.md
```

---

### test_experiments.py

**Purpose**: Quickly validate that all experiments execute without errors

**Usage**:
```bash
python scripts/test_experiments.py
```

**Output**:
- Pass/fail status for each experiment
- Summary of total passed/failed
- Exit code 0 if all pass, 1 if any fail

**Features**:
- Runs each experiment with 30-second timeout
- Captures errors without verbose output
- Suitable for CI/CD pipelines
- Fast validation before full run

**Example**:
```bash
$ python scripts/test_experiments.py

Testing All Experiments
======================================================================
Found 6 experiments

Testing 01_string_repair.py... ✓ PASS
Testing 02_network_repair.py... ✓ PASS
Testing 03_file_repair.sh... ✓ PASS
Testing 04_process_repair.sh... ✓ PASS
Testing 05_population_dynamics.py... ✓ PASS
Testing 06_database_repair.sh... ✓ PASS

======================================================================
SUMMARY
======================================================================
  ✓ PASS  01_string_repair.py
  ✓ PASS  02_network_repair.py
  ✓ PASS  03_file_repair.sh
  ✓ PASS  04_process_repair.sh
  ✓ PASS  05_population_dynamics.py
  ✓ PASS  06_database_repair.sh

Total: 6/6 passed
```

---

### analyze_results.py

**Purpose**: Parse experiment outputs and generate comparative analysis

**Usage**:
```bash
# Analyze most recent run
python scripts/analyze_results.py

# Analyze specific run
python scripts/analyze_results.py results/run_20260811_204500
```

**Output**:
- Comparative table across all experiments
- Overall summary statistics
- Saves analysis to `ANALYSIS.txt`

**Features**:
- Extracts measurements from output files
- Calculates deltas between baseline and intervention
- Counts supporting vs null results
- Determines overall conclusion

**Example**:
```bash
$ python scripts/analyze_results.py

Analyzing results from: results/run_20260811_204500

================================================================================
EXPERIMENT COMPARISON SUMMARY
================================================================================

## 01_string_repair
--------------------------------------------------------------------------------
Metric                          Baseline    Intervention          Δ
Persistence (states)                1.00           35.00     +34.00
Recovery cost (avg)                12.40            2.73      -9.67

Interpretation:
  ✓ Repair that preserves difference maintains greater state diversity

...

================================================================================
OVERALL SUMMARY
================================================================================

Total experiments: 6
Supporting hypothesis: 5
Null results: 1
Ambiguous: 0

✓ Majority of experiments support 'repair preserves difference'

Analysis saved to: results/run_20260811_204500/ANALYSIS.txt
```

---

## Workflow Examples

### Development workflow
```bash
# 1. Make changes to experiments
vim experiments/01_string_repair.py

# 2. Quick validation
python scripts/test_experiments.py

# 3. Full experimental run
bash scripts/run_all_experiments.sh

# 4. Analyze results
python scripts/analyze_results.py
```

### Quick check workflow
```bash
# Test one experiment
python experiments/01_string_repair.py

# Validate all work
python scripts/test_experiments.py
```

### Research workflow
```bash
# Full run with timestamp
bash scripts/run_all_experiments.sh

# Review summary
cat results/run_*/SUMMARY.md | tail -50

# Detailed analysis
python scripts/analyze_results.py

# Compare runs
ls -lt results/
diff results/run_*/ANALYSIS.txt
```

### CI/CD workflow
```bash
# In CI pipeline
python scripts/test_experiments.py || exit 1
bash scripts/run_all_experiments.sh
python scripts/analyze_results.py
```

---

## Script Dependencies

### Python scripts require:
- Python 3.7+
- Standard library only (no external packages)

### Bash scripts require:
- Bash 4.0+
- Standard Unix utilities: `grep`, `sed`, `awk`, `wc`, `sort`

---

## Customization

### Adding new analysis

Edit `analyze_results.py` to add custom visualizations:

```python
def custom_metric(results: List[Dict]) -> str:
    # Your analysis logic
    return formatted_output
```

### Modifying run behavior

Edit `run_all_experiments.sh` to:
- Filter which experiments run
- Change output format
- Add pre/post-processing steps

### Extending tests

Edit `test_experiments.py` to:
- Adjust timeout values
- Add validation checks
- Include custom test suites

---

## Output Structure

After running experiments:

```
results/
└── run_20260811_204500/
    ├── SUMMARY.md                    # Generated summary report
    ├── ANALYSIS.txt                  # Parsed analysis
    ├── 01_string_repair_output.txt   # Individual outputs
    ├── 02_network_repair_output.txt
    ├── 03_file_repair_output.txt
    ├── 04_process_repair_output.txt
    ├── 05_population_dynamics_output.txt
    └── 06_database_repair_output.txt
```

---

## Troubleshooting

### "No results found"
Run experiments first:
```bash
bash scripts/run_all_experiments.sh
```

### "Timeout exceeded"
Increase timeout in `test_experiments.py`:
```python
timeout=60  # Increase from 30
```

### "Permission denied"
Make scripts executable:
```bash
chmod +x scripts/*.py scripts/*.sh
```

### Parse errors in analysis
Check that experiment output format matches expected structure:
- Measurement tables with "baseline" and "intervention" columns
- "INTERPRETATION:" section with results

---

## Contributing

When adding new scripts:

1. Place in `scripts/` directory
2. Make executable: `chmod +x scripts/new_script.sh`
3. Add documentation to this README
4. Follow naming convention: `action_target.{py,sh}`
5. Include usage examples
