# repair-preserves-difference

**Summary**

The *repair-preserves-difference* repository contains automation and analysis tools for running a suite of experiments that test the hypothesis “repair preserves difference.” The core purpose is to execute all available Python and Bash experiment scripts, capture their full outputs, extract key results, and produce a comprehensive summary report (`SUMMARY.md`) in a timestamped `results/` directory. Supporting utilities include:

- **run_all_experiments.sh** – Executes every experiment (`.py` and `.sh` files), stores individual outputs as `_output.txt`, and generates the unified summary.
- **test_experiments.py** – Provides a fast validation that all experiments run without errors, useful for CI/CD pipelines.
- **analyze_results.py** – Parses the generated outputs to produce comparative analysis tables, overall statistics, and an `ANALYSIS.txt` file summarizing supporting vs. null results.

The repository is designed with clear workflow examples (development, quick check, research, CI/CD) and includes instructions for customization, troubleshooting common issues, and contribution guidelines. It relies only on standard Unix utilities and Python 3.7+, ensuring portability across environments.

**KEYWORDS:**
repair preserves difference experiments automation analysis summary results directory bash python scripts test_experiments analyze_results workflow development quick check research CI/CD dependency troubleshooting documentation naming convention.
