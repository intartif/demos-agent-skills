#!/usr/bin/env bash
set -euo pipefail

ROOT="${1:-.}"
CONFIG="${2:-skills/workflows-lint-fix/config/actions-versions.json}"

if ! command -v jq >/dev/null 2>&1; then
  echo "ERROR: jq es requerido." >&2
  exit 2
fi

fail=0

# Busca líneas uses: owner/repo(@ref) en workflows
grep -RIn --include='*.yml' --include='*.yaml' -E '^\s*uses:\s*[A-Za-z0-9._-]+/[A-Za-z0-9._-]+(/[^@]+)?@[^ ]+' "$ROOT" | while IFS=: read -r file line content; do
  uses="$(sed -E 's/^\s*uses:\s*//;s/#.*$//' <<<"$content" | xargs)"
  # owner/repo(/path)?@ref
  owner_repo="$(sed -E 's/@.*$//' <<<"$uses")"
  ref="$(sed -E 's/^.*@//' <<<"$uses")"

  # Extrae solo owner/repo para el catálogo
  owner_repo_key="$(sed -E 's|/.*$||;s|$|/|;s|/|/|;:a;s|/[^/]+/|/|;ta' <<<"$owner_repo")"
  # Truco: owner/repo/path -> owner/repo
  owner_repo_key="$(cut -d/ -f1-2 <<<"$owner_repo")"

  if jq -e --arg k "$owner_repo_key" '.[$k]' "$CONFIG" >/dev/null; then
    recMajor="$(jq -r --arg k "$owner_repo_key" '.[$k].recommendedMajor' "$CONFIG")"
    minMajor="$(jq -r --arg k "$owner_repo_key" '.[$k].minMajor' "$CONFIG")"
  else
    # Sin política conocida → solo advertir ramas
    if [[ ! "$ref" =~ ^v[0-9]+$ && ! "$ref" =~ ^[0-9a-f]{7,40}$ ]]; then
      echo "::warning file=$file,line=$line::$owner_repo usa '$ref'. Evita ramas; usa un tag mayor (@vN) o SHA."
    fi
    continue
  fi

  # SHA → ok
  if [[ "$ref" =~ ^[0-9a-f]{7,40}$ ]]; then
    continue
  fi

  # Major/tag/branch
  if [[ "$ref" =~ ^v([0-9]+) ]]; then
    major="${BASH_REMATCH[1]}"
    if (( major < minMajor )); then
      echo "::error file=$file,line=$line::$owner_repo usa '$ref' (< v$minMajor soportado). Recom: '$recMajor'."
      fail=1
    fi
  else
    echo "::warning file=$file,line=$line::$owner_repo usa '$ref' (rama/etiqueta no mayor). Recom: '$recMajor' o pin a SHA."
  fi
done

exit $fail