#!/usr/bin/env bash
set -uo pipefail

OWNER="${1:-standardgalactic}"
OUTDIR="${2:-all-readmes}"

mkdir -p "$OUTDIR"

echo "Collecting root READMEs from $OWNER source repositories..."
echo "Output: $OUTDIR/"
echo

# REST API: avoids gh repo list / GraphQL.
repos="$(
    gh api --paginate \
        "/users/$OWNER/repos?per_page=100&type=owner&sort=full_name" \
        --jq '.[] | select(.fork == false) | .name'
)"

total=0
saved=0
missing=0
failed=0

while IFS= read -r repo; do
    [[ -z "$repo" ]] && continue

    ((total++))
    printf 'Scanning %s/%s ...\n' "$OWNER" "$repo"

    # Ask GitHub for the repository's root README.
    if metadata="$(
        gh api \
            -H "Accept: application/vnd.github+json" \
            "/repos/$OWNER/$repo/readme" \
            2>/dev/null
    )"; then

        # Preserve the actual README filename:
        # README.md, README.rst, README.txt, etc.
        name="$(jq -r '.name' <<<"$metadata")"

        repodir="$OUTDIR/$repo"
        mkdir -p "$repodir"

        outfile="$repodir/$name"

        if gh api \
            -H "Accept: application/vnd.github.raw+json" \
            "/repos/$OWNER/$repo/readme" \
            > "$outfile" 2>/dev/null
        then
            printf '  -> %s\n' "$outfile"
            ((saved++))
        else
            printf '  WARNING: found README but could not download it\n'
            rm -f "$outfile"
            rmdir "$repodir" 2>/dev/null || true
            ((failed++))
        fi
    else
        printf '  no root README\n'
        ((missing++))
    fi
done <<< "$repos"

echo
echo "Done."
echo "Repositories scanned: $total"
echo "READMEs saved:       $saved"
echo "No README:           $missing"
echo "Failures:            $failed"
echo "Output directory:    $OUTDIR"