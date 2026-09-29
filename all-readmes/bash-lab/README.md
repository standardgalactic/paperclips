# Bash Lab: Executable Micro-Labs for Shell Programming

A cluster of minimal, executable programs that teach Unix shell programming through composition and progressive refinement.

## Philosophy

Each program introduces **one principle** while reusing earlier ones. Programs begin absurdly small and compose into genuinely useful Unix tools.

## Progression

```
values → decisions → iteration → functions → files → 
streams → processes → composition → history → concurrency
```

## Structure

Each lab is:
- **Minimal**: One concept per program
- **Executable**: Run immediately without setup
- **Composable**: Builds on previous labs
- **Explanatory**: Code teaches through doing

## Labs

### The Smallest Programs

#### 01-hello-arguments
Introduces programs as transformations of input rather than static scripts.

```bash
./hello-arguments.sh README.md test.txt
```

Teaches: `$0`, `$1`, `$#`, `"$@"`

#### 02-variables-are-text
Explores quoting, whitespace, command substitution.

Teaches: Difference between `$x` and `"$x"`

#### 03-exit-means-something
Programs communicate through output **and status**.

```bash
./is-file.sh README.md && echo "exists"
```

Teaches: Exit codes, predicates, boolean composition

### Decisions and Repetition

#### 04-tiny-guessing-game
Basic control flow without excessive complexity.

Teaches: `read`, `if/elif`, arithmetic, loops

#### 05-fizzbuzz-without-fizzbuzz
Classifies integers by arbitrary divisibility rules.

Teaches: Loops, arithmetic expansion, modulo, conditionals

#### 06-file-classifier
Reports file type for each argument.

Teaches: `-f`, `-d`, `-x`, `-L` predicates, argument iteration

#### 07-retry
Runs a command until it succeeds.

```bash
./retry.sh curl https://example.com
```

Teaches: Loops, commands as arguments, exit status

### Functions and Decomposition

#### 08-mini-calculator
Simple arithmetic with function dispatch.

```bash
./calc.sh add 5 3
./calc.sh multiply 4 7
```

Teaches: Functions, argument routing, decomposition

#### 09-command-router
CLI subcommand architecture.

```bash
./lab.sh create foo
./lab.sh list
./lab.sh delete foo
```

Teaches: `case` statements, real CLI patterns

#### 10-configuration-layers
Precedence: defaults → environment → config → CLI.

Teaches: Configuration merging, precedence rules

### Files as State

#### 11-tiny-database
TSV-based CRUD with grep, cut, sort, awk.

```bash
./db.sh add alice 17
./db.sh get alice
./db.sh list
```

Teaches: Files as databases, text processing tools

#### 12-append-only-journal
Event log instead of mutable state.

```bash
./journal.sh "deployed v2.1"
./journal.sh query today
```

Teaches: Append-only patterns, events vs. state

#### 13-state-from-history
Event sourcing: replay log to compute current value.

Teaches: Event sourcing, derived state

### Streams and Composition

#### 14-uppercase
Transforms stdin to stdout.

Teaches: Filters, stream processing

#### 15-number-lines
Adds line numbers.

Teaches: Line-oriented processing

#### 16-contains
Retains matching lines.

Teaches: Filtering, pattern matching

#### 17-count
Counts input.

Teaches: Aggregation

#### 18-bad-pipeline
Deliberately corrupts pipeline with diagnostics to stdout.

Teaches: stdout vs. stderr (`>&2`)

### Processes and Concurrency

#### 19-background-farm
Launch jobs with `&`, collect PIDs, wait.

Teaches: Background processes, job control

#### 20-parallel-map
Concurrent execution over files.

Teaches: Parallelism, process management

#### 21-process-supervisor
Launch, monitor, restart on failure.

Teaches: Supervision, fault handling

#### 22-signal-laboratory
Trap signals, cleanup on exit.

```bash
trap cleanup EXIT
trap 'echo interrupted' INT
```

Teaches: Signal handling, cleanup guarantees

### Correctness and Defensive Programming

#### 23-quoting-gauntlet
Handle: `normal`, `two words`, `*.txt`, `-d`, `a;b`, newlines.

Teaches: Why quoting folklore exists, `"$@"`, `read -r`

#### 24-strict-mode
Investigate `set -e`, `set -u`, `pipefail` behavior.

Teaches: What strict mode guarantees (and doesn't)

#### 25-temporary-transaction
Generate to temp, validate, atomic move.

Teaches: Transactional patterns, atomicity

### Programs About Programs

#### 26-argument-logger
Record exact arguments received.

Teaches: Shell expansion observation

#### 27-environment-inspector
Show inherited environment, PID, working directory.

Teaches: Process context, environment

#### 28-path-explorer
Implement primitive `which`.

Teaches: How command resolution works

#### 29-tiny-make
Dependency-based incremental computation.

Teaches: Build systems, caching, dependencies

### Capstone: Tiny Unix

#### 30-tiny-shell
Miniature shell: tokenize, resolve PATH, execute, status, redirection, pipes.

Teaches: What actually happens when you type a command

## Usage

Each lab is standalone:

```bash
cd labs/01-hello-arguments
./hello-arguments.sh arg1 arg2 arg3
cat README.md  # Read explanation
```

Progressive composition:

```bash
cat words.txt | \
  ./14-uppercase.sh | \
  ./16-contains.sh BASH | \
  ./15-number-lines.sh | \
  ./17-count.sh
```

## Learning Path

1. Start with smallest programs (01-03)
2. Build control flow understanding (04-07)
3. Learn decomposition (08-10)
4. Master state management (11-13)
5. Understand composition (14-18)
6. Explore concurrency (19-22)
7. Practice defensive programming (23-25)
8. Meta-programming (26-29)
9. Capstone synthesis (30)

## Design Principles

**Minimal**: Each program teaches one concept

**Executable**: No build step, run immediately

**Progressive**: Later programs build on earlier ones

**Explanatory**: Code is the primary teaching material

**Realistic**: Patterns used in real Unix programming

## Why Bash?

Bash is unusually good for this because:
- Examples can begin absurdly small
- Compose into genuinely useful programs
- Teaches Unix philosophy through practice
- Shows how real systems work

## Practical Tools

Beyond the educational labs, this repository includes production-ready utilities:

### Typewriter Art (`typewriter.sh`, `typewriter-edge.sh`)

Convert images to weighted typewriter ASCII art using pure Bash/ImageMagick/awk pipelines.

```bash
./typewriter.sh photo.jpg 140 > portrait.txt
./typewriter-edge.sh landscape.jpg 160 > art.txt
```

**Key innovations:**
- Character repetition for probability weighting
- Edge-aware geometric character matching
- Deterministic (non-random) selection
- Pure Unix pipeline (no Python dependencies)

See `TYPEWRITER_ART.md` for full documentation.

### Repository Cleanup (`cleanup-malformed-repos.sh`)

Detect and remove malformed files created by repository cloning errors.

```bash
./cleanup-malformed-repos.sh --dry-run
./cleanup-malformed-repos.sh
```

Includes safe git cloning wrapper and pre-commit hooks. See `MALFORMED_CLEANUP_README.md`.

## Connection to Unix Philosophy

By the capstone, students understand:

> Programs don't need to know their future collaborators if they agree on an interface.

The curriculum teaches composition not as theory but as **lived experience**.
