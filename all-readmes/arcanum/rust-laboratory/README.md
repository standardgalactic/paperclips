# Rust Laboratory

A collection of small, self-contained Rust programs demonstrating the core features of the Rust programming language.

Each lesson lives in its own directory and contains a single `main.rs` file that can be compiled independently using the Rust compiler.

## Compiling a Single Lesson

Change into the lesson directory and compile it with `rustc`:

```bash
cd 01-hello
rustc main.rs -o lesson
./lesson
```

On Windows the executable will be named `lesson.exe`.

## Building Every Lesson

To compile and run every lesson in the repository:

```bash
for d in */ ; do
    if [[ -f "$d/main.rs" ]]; then
        echo
        echo "========================================"
        echo "$d"
        echo "========================================"

        (
            cd "$d"
            rustc main.rs -o lesson &&
            ./lesson
        )
    fi
done
```

## Compile Check

To verify that every lesson compiles without running the executables:

```bash
for d in */ ; do
    [[ -f "$d/main.rs" ]] || continue

    echo "Compiling $d"

    (
        cd "$d"
        rustc main.rs -o lesson
    )
done
```

## Cleaning Up

Remove the generated executables after compiling:

Linux / macOS / Git Bash:

```bash
find . -type f -name lesson -delete
```

Windows executables:

```bash
find . -type f -name lesson.exe -delete
```

## Repository Structure

Each lesson is designed to be independent and focuses on a single topic. Most examples are intended to be compiled directly with the standard Rust compiler and rely only on the Rust standard library.

Typical layout:

```text
01-hello/
    main.rs
    README.md

02-variables/
    main.rs
    README.md

...

30-projects/
    main.rs
    README.md
```

The lessons are intended to be explored sequentially, but each directory can also be studied independently.

