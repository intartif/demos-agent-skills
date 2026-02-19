#!/usr/bin/env bash
set -euo pipefail
ROOT="${1:-.}"

# Mapeo de acciones a versiones recomendadas (clave:acción valor:versión)
RECOMMENDED_LIST="actions/checkout v6"

# Reemplaza refs mayores irreales (>99) o no existentes por el recomendado
found_files=0
while IFS= read -r -d '' f; do
  found_files=1
  content="$(<"$f")"
  changed="$content"
  # Para cada acción conocida, aplica el fix
  for pair in $RECOMMENDED_LIST; do
    k="${pair%% *}"
    rec="${pair##* }"
    # Detecta k@v<number> con número "extraño" (>=10) o explícitamente v15
    changed="$(perl -0777 -pe "s#(uses:\s*${k}(?:/[\w._-]+)?@)v(\d{2,}|15)\b#\${1}${rec}#g" <<<"$changed")"
  done
  if [[ "$changed" != "$content" ]]; then
    echo "Autofix: $f"
    printf "%s" "$changed" > "$f"
  fi
done < <(find "$ROOT/.github/workflows" -type f \( -name '*.yml' -o -name '*.yaml' \) -print0)

# Si no se encontraron archivos, no fallar
if [[ "$found_files" -eq 0 ]]; then
  exit 0
fi