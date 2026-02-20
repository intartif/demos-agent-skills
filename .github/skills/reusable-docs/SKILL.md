---
name: reusable-docs
description: Genera documentación estandarizada para workflows o actions reusable de github actions (on: workflow_call) y reusable actions (action.yml), guardando el resultado en ./docs/actions o ./docs/workflows según corresponda.
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
- Uno o más archivos Markdown en `./docs/actions/` o `./docs/workflows/` con la documentación generada, según el tipo de archivo analizado.
- (Opcional) Índice actualizado en `docs/README.md`.

## Pasos
1. **Antes de cualquier análisis, preguntar al usuario si desea generar documentación de workflows o de actions.**
2. **Según la respuesta, buscar todos los archivos de workflows ubicados en `.github/workflows/` o actions ubicados en `actions/` (action.yml).**
3. **Solicitar explícitamente al usuario que seleccione el o los archivos para los que desea generar documentación** (todas o selección específica). No se debe poder continuar sin esta selección.
   - Si el elemento seleccionado ya cuenta con su archivo de documentación correspondiente en `docs/actions/` o `docs/workflows/`, se debe pedir confirmación obligatoria al usuario antes de sobrescribir o versionar dicho archivo. No se debe continuar sin esta confirmación explícita.
4. **Según la respuesta del usuario en el paso 1, seleccionar la plantilla de documentación correspondiente, ubicadas en la carpeta `templates`.** Para los workflows se usa `README.workflow.md.gotmpl`, para las actions se usa `README.action.md.gotmpl`. No se debe continuar sin esta selección explícita.
   - **Leer el contenido completo del archivo de plantilla con la herramienta de lectura de archivos.** No se debe generar ningún contenido de documentación sin antes haber leído y cargado la plantilla. El archivo leído es la única fuente válida para definir la estructura, secciones y formato del documento de salida.
5. Usar exclusivamente el contenido leído de la plantilla para renderizar la documentación. No agregar ni omitir secciones respecto a la plantilla.
6. Extraer y normalizar metadatos relevantes.
7. Guardar el archivo en `./docs/actions/` si es una action reusable, o en `./docs/workflows/` si es un workflow reusable, siguiendo la convención de nombres.
8. (Opcional) Actualizar índice en `docs/README.md`.

## Checklist de calidad
- [ ] Documentación clara y completa.
- [ ] Inputs y outputs ordenados y descritos.
- [ ] Jobs y steps listados y explicados.
- [ ] Uso y versionado documentados.
- [ ] Índice actualizado si corresponde.
- [ ] La estructura del documento generado corresponde exactamente a la plantilla leída (sección por sección).
- [ ] No se usó ninguna sección que no exista en la plantilla.
- [ ] No se omitió ninguna sección obligatoria de la plantilla.

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

