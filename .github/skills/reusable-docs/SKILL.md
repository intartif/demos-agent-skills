---
name: reusable-docs
description: "Genera documentación estandarizada para reusable workflows (on: workflow_call) y reusable actions (action.yml) y la guarda en ./docs/."
license: MIT
---

# Objetivo
Producir un README claro y completo para:
- **Reusable workflows** colocados en `.github/workflows/*.yml` con `on: workflow_call`.
- **Reusable actions** (composite/JS/Docker) definidas por `action.yml`.

Guardar SIEMPRE los documentos generados en la carpeta **`./docs/`** del repositorio, creando la carpeta si no existe.

# Dónde escribir los archivos
- Carpeta destino: **`./docs/`**
- Convenciones de nombre:
  - Workflows: `docs/<workflow-file-sin-ext>.md`
    - Ej.: `.github/workflows/reusable-ci-security.yml` → `docs/reusable-ci-security.md`
  - Actions: `docs/<carpeta-o-action-name>.action.md`
    - Ej.: `./actions/ci/action.yml` → `docs/ci.action.md`
- Si ya existe un archivo con ese nombre:
  - Comportamiento por defecto: **sobrescribir** (idempotente).
  - Alternativa (si el usuario lo pide): **versionar** como `*.md` → `*-v2.md`, `*-v3.md`, etc.

# Cuándo activar
- El usuario pida: “documenta este reusable workflow/action”.
- Se editen/creen archivos `action.yml` o `*.yml` con `workflow_call`.
- Se solicite una plantilla de README para Actions/Workflows.

# Procedimiento
1. **Detectar el tipo**:
   - Si existe `action.yml` en la ruta proporcionada → **Action**.
   - Si el YAML contiene `on.workflow_call` → **Reusable workflow**.

2. **Extraer metadatos**:
   - **Workflow**: `name`, `on.workflow_call.inputs`, `on.workflow_call.secrets`, `on.workflow_call.outputs` (si existen), `jobs`, `steps` de cada job; `permissions`.
   - **Action**: `name`, `description`, `inputs` (id/desc/required/default), `outputs` (id/desc), `runs` (tipo, shells si composite), `branding` si aplica.

3. **Normalizar datos**:
   - Ordenar **inputs** alfabéticamente; marcar `required` y `default`.
   - Para **jobs/steps**, listar nombre (`name`), condiciones (`if`), `uses`/`run`, y artefactos relevantes (upload/download).
   - Resumir **permissions** mínimas y su razón (p. ej., `security-events: write` para subir SARIF).

4. **Renderizar** usando la plantilla adecuada de `templates/`:
   - Workflows → `templates/README.workflow.md.gotmpl`
   - Actions → `templates/README.action.md.gotmpl`

5. **Guardar en `./docs/`**:
   - Asegurarse de que la carpeta **exista**; crearla si falta.
   - Determinar el nombre del archivo destino según **convención** (sección “Dónde escribir los archivos”).
   - Escribir/actualizar el Markdown **en disco**.
   - Mostrar ruta final escrita (por ejemplo: `docs/reusable-ci-security.md`).

6. **(Opcional) Índice**:
   - Actualizar/crear `docs/README.md` con un índice enlazando los documentos generados (mantener orden alfabético).
   - Estructura sugerida:
     - `## Workflows`
     - `## Actions`

# Entregables
- Uno o más archivos **Markdown** en `./docs/` con secciones:
  1) Descripción  
  2) Inputs  
  3) Outputs  
  4) Jobs  
  5) Steps  
  6) Summary  
  7) Uso (caller / with / secrets)  
  8) Versionado y compatibilidad

# Mensajes tipo (interacción)
- “Pásame la **ruta** del workflow/action y genero la documentación en `./docs/`.”
- “¿Deseas **sobrescribir** o **versionar** si el archivo ya existe?”
- “¿Actualizo también el **índice** en `docs/README.md`?”

# Ejemplos de salida (nombres de archivo)
- Workflow `.github/workflows/ci.yml` → **`docs/ci.md`**
- Workflow `.github/workflows/reusable-ci-security.yml` → **`docs/reusable-ci-security.md`**
- Action `./actions/ci/action.yml` → **`docs/ci.action.md`**

# Notas de implementación
- Los templates ya incluyen todo el esquema de secciones; no necesitan cambios para la carpeta de salida.
- Este skill **no ejecuta** CI ni valida YAML; solo genera documentación a partir de la lectura de archivos y normalización de metadatos.
- Si el usuario trabaja con un monorepo, se recomienda mantener nombres **cortos y únicos** para evitar colisiones en `./docs/`.

# Limitaciones
- No se consultan metadatos externos; todo se infiere del YAML local (`action.yml` o workflow con `workflow_call`).
- No se traduce automáticamente; el contenido se genera en el idioma usado por el usuario al solicitar la documentación.