---
name: reusable-docs
description: Genera documentación estandarizada para reusable workflows (on: workflow_call) y reusable actions (action.yml) y la guarda en ./docs/.
license: Apache-2.0
compatibility: [claude, vscode-copilot, cursor]
metadata:
   domain: docs
   skill_id: docs.reusable-docs
---

# docs.reusable-docs

## Cuándo usar
- Cuando se requiera documentar un reusable workflow o action.
- Al crear o modificar archivos `action.yml` o workflows con `workflow_call`.
- Cuando se solicite una plantilla de README para Actions/Workflows.

## Entradas
- Ruta del archivo workflow o action.
- (Opcional) Preferencia de sobrescribir o versionar si el archivo ya existe.

## Salidas
- Uno o más archivos Markdown en `./docs/` con la documentación generada.
- (Opcional) Índice actualizado en `docs/README.md`.

## Pasos
1. Detectar si es action o reusable workflow.
2. Extraer y normalizar metadatos relevantes.
3. Renderizar usando la plantilla adecuada de `templates/`.
4. Guardar el archivo en `./docs/` siguiendo la convención de nombres.
5. (Opcional) Actualizar índice en `docs/README.md`.

## Checklist de calidad
- [ ] Documentación clara y completa.
- [ ] Inputs y outputs ordenados y descritos.
- [ ] Jobs y steps listados y explicados.
- [ ] Uso y versionado documentados.
- [ ] Índice actualizado si corresponde.

## Ejemplos
**Entrada**
- Ruta: .github/workflows/ci.yml

**Salida**
- docs/ci.md

**Entrada**
- Ruta: ./actions/ci/action.yml

**Salida**
- docs/ci.action.md

## Referencias
- templates/README.workflow.md.gotmpl
- templates/README.action.md.gotmpl
- docs/README.md

