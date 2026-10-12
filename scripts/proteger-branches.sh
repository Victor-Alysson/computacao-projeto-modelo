#!/usr/bin/env bash
# Uso: ./scripts/proteger-branches.sh dono/repositorio
set -euo pipefail
REPO="$1"
for BRANCH in main develop; do
  gh api -X PUT "repos/$REPO/branches/$BRANCH/protection" --input - <<JSON
{
  "required_status_checks": {"strict": true, "contexts": ["build"]},
  "enforce_admins": true,
  "required_pull_request_reviews": {"required_approving_review_count": 1, "require_code_owner_reviews": true},
  "restrictions": null,
  "allow_force_pushes": false,
  "allow_deletions": false
}
JSON
  echo "Protegida: $BRANCH"
done
