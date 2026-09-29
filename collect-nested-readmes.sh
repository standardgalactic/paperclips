#!/usr/bin/env bash
set -uo pipefail

OWNER="${1:-standardgalactic}"
OUTDIR="${2:-all-readmes}"

mkdir -p "$OUTDIR"

echo "Collecting ALL READMEs from $OWNER repositories..."
echo "Output: $OUTDIR/"
echo

total=0
saved=0
failed=0

# Enumerate all owned, non-fork repositories.
while IFS=$'\t' read -r repo branch; do
    [[ -z "$repo" || -z "$branch" ]] && continue

    ((total++))
    printf 'Scanning %s/%s ...\n' "$OWNER" "$repo"

    # Get the complete recursive tree.
    if ! paths="$(
        gh api \
            "/repos/$OWNER/$repo/git/trees/$branch?recursive=1" \
            --jq '
                .tree[]
                | select(.type == "blob")
                | select(.path | split("/")[-1] | test("^README(\\..*)?$"; "i"))
                | .path
            ' 2>/dev/null
    )"; then
        echo "  WARNING: could not read tree"
        ((failed++))
        continue
    fi

    if [[ -z "$paths" ]]; then
        echo "  no READMEs"
        continue
    fi

    while IFS= read -r path; do
        [[ -z "$path" ]] && continue

        outfile="$OUTDIR/$repo/$path"
        mkdir -p "$(dirname "$outfile")"

        # Existing root READMEs from your first run need not be downloaded again.
        if [[ -s "$outfile" ]]; then
            printf '  exists: %s\n' "$path"
            continue
        fi

        if gh api \
            -H "Accept: application/vnd.github.raw+json" \
            "/repos/$OWNER/$repo/contents/$path?ref=$branch" \
            > "$outfile" 2>/dev/null
        then
            printf '  -> %s\n' "$outfile"
            ((saved++))
        else
            printf '  WARNING: could not download %s\n' "$path"
            rm -f "$outfile"
            ((failed++))
        fi

    done <<< "$paths"

done < <(
    gh api --paginate \
        "/users/$OWNER/repos?per_page=100&type=owner&sort=full_name" \
        --jq '.[] | select(.fork == false) |
              [.name, .default_branch] | @tsv'
)

echo
echo "Done."
echo "Repositories scanned: $total"
echo "New READMEs saved:    $saved"
echo "Failures:             $failed"
echo "Output:               $OUTDIR"
