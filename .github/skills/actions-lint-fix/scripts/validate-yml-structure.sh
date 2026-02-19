#!/usr/bin/env bash
set -euo pipefail

# Valida que los archivos YAML de actions y workflows tengan las propiedades requeridas
# - name (siempre)
# - description (siempre)
# - runs (en actions)
# - jobs (en workflows)
#
# Uso: ./validate-yml-structure.sh <ruta-raiz>

ROOT="${1:-.}"
fail=0

# Busca todos los YAML relevantes
find "$ROOT" \( -name '*.yml' -o -name '*.yaml' \) | while read -r file; do
  # Detecta si es action reusable (tiene 'runs:') o workflow (tiene 'jobs:')
  is_action=$(grep -E '^runs:' "$file" || true)
  is_workflow=$(grep -E '^jobs:' "$file" || true)

  # name obligatorio
  if ! grep -Eq '^name:' "$file"; then
    echo "::error file=$file::Falta la propiedad obligatoria 'name'"
    fail=1
  fi

  # description obligatorio
  if ! grep -Eq '^description:' "$file"; then
    echo "::error file=$file::Falta la propiedad obligatoria 'description'"
    fail=1
  fi

  # Si es action reusable, debe tener 'runs:'
  if [[ -n "$is_action" ]]; then
    if ! grep -Eq '^runs:' "$file"; then
      echo "::error file=$file::Un action reusable debe tener la propiedad 'runs'"
      fail=1
    fi
  fi

  # Si es workflow, debe tener 'jobs:'
  if [[ -n "$is_workflow" ]]; then
    if ! grep -Eq '^jobs:' "$file"; then
      echo "::error file=$file::Un workflow debe tener la propiedad 'jobs'"
      fail=1
    fi
  fi

done

exit $fail
