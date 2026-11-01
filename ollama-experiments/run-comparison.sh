#!/usr/bin/env bash
set -euo pipefail
script_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
for style in json prose json-steps; do
    bash "$script_dir/granite-audit-tests/run.sh" --style "$style" "$@"
done
