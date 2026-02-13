#!/usr/bin/env bash
set -euo pipefail
ROOT="${1:-.}"

# Mapea acciones a su major recomendado
declare -A RECOMMENDED=(
  ["actions/checkout"]="v6"
)

# Reemplaza refs mayores irreales (>99) o no existentes por el recomendado
while IFS= read -r -d '' f; do
  content="$(<"$f")"
  changed="$content"
  for k in "${!RECOMMENDED[@]}"; do
    rec="${RECOMMENDED[$k]}"
    # Detecta k@v<number> con número "extraño" (>=10) o explícitamente v15
    changed="$(perl -0777 -pe "s#(uses:\\s*${k}(?:/[\\w._-]+)?@)v(\\d{2,}|15)\\b#\${1}${rec}#g" <<<"$changed")"
  done
  if [[ "$changed" != "$content" ]]; then
    echo "Autofix: $f"
    printf "%s" "$changed" > "$f"
  fi
done < <(find "$ROOT/.github/workflows" -type f \( -name '*.yml' -o -name '*.yaml' \) -print0)