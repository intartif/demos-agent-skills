---
name: workflows-corp-policy
description: "Valida patrones y estándares corporativos en workflows de GitHub Actions (.github/workflows). Reporta incumplimientos y sugiere fixes."
license: MIT
---

# Objetivo
Garantizar que los workflows existentes cumplen con los **estándares corporativos** definidos por la organización (seguridad, consistencia, mantenibilidad y prácticas de GitHub Actions).

# Alcance
- Archivos: `.github/workflows/*.yml|*.yaml`
- Validaciones (configurables vía `config/patterns.yml`):
  - **Permisos de GITHUB_TOKEN**: declarar `permissions` explícitas y mínimo privilegio (por workflow o por job). [1](https://dev.to/nickytonline/creating-your-first-github-copilot-extension-a-step-by-step-guide-28g0)
  - **Acciones y versiones**: `uses: owner/repo@ref` contra allowlist corporativa (majors permitidos, pin SHA opcional). [1](https://dev.to/nickytonline/creating-your-first-github-copilot-extension-a-step-by-step-guide-28g0)
  - **Runners**: `runs-on` dentro de una lista aprobada (e.g., `ubuntu-latest`, `self-hosted` etiquetados).
  - **Triggers**: presencia/ausencia de eventos (`on:`), uso de `workflow_call` en reutilizables si aplica. [2](https://docs.github.com/en/copilot/how-tos/configure-custom-instructions/add-repository-instructions)
  - **Política de secretos**: evitar `secrets` en texto plano; requerir `secrets:` o `env` inyectado desde variables seguras. [1](https://dev.to/nickytonline/creating-your-first-github-copilot-extension-a-step-by-step-guide-28g0)
  - **Artifacts y SARIF**: uso correcto de `upload-artifact` / `codeql-action/upload-sarif` cuando existan steps de análisis. [1](https://dev.to/nickytonline/creating-your-first-github-copilot-extension-a-step-by-step-guide-28g0)
  - **Matriz y timeouts**: `strategy.matrix` (si se usa) y `timeout-minutes` definidos en jobs críticos. [1](https://dev.to/nickytonline/creating-your-first-github-copilot-extension-a-step-by-step-guide-28g0)
  - **Nombres y metadatos**: `name` de workflow y jobs consistente; `env` global vs job.
  - **Caching**: uso de `actions/cache` con claves estables (si aplica). [1](https://dev.to/nickytonline/creating-your-first-github-copilot-extension-a-step-by-step-guide-28g0)

# Cómo decide este skill
1. **Descubrimiento**: Lista workflows y parsea YAML (sin ejecutar).
2. **Catálogo corporativo**:
   - `config/patterns.yml`: reglas (obligatorias, recomendadas, prohibidas) con mensajes y severidades.
   - `config/actions-allowlist.yml`: acciones aprobadas y versiones mínimas/recomendadas (major/SHA).
3. **Análisis**:
   - Valida estructura y claves soportadas por el modelo de GitHub Actions (workflow, jobs, steps, permissions, env, strategy…). [1](https://dev.to/nickytonline/creating-your-first-github-copilot-extension-a-step-by-step-guide-28g0)
   - Para workflows reutilizables, verifica `on: workflow_call` e inputs/secrets/outputs. [2](https://docs.github.com/en/copilot/how-tos/configure-custom-instructions/add-repository-instructions)
4. **Reporte**:
   - Emite anotaciones por archivo/línea:
     - `ERROR`: incumplimiento de política obligatoria.
     - `WARNING`: recomendación corporativa.
     - `INFO`: sugerencias de mejora.
   - Propone **fixes** (snippet YAML) cuando proceda.
5. **Opcional – Autofix guiado**:
   - Actualiza `permissions`, corrige `runs-on`, cambia `uses` a la versión mayor aprobada, inserta `timeout-minutes`, etc. (solo si el usuario lo autoriza).

# Archivos de configuración

## `config/patterns.yml` (ejemplo)
```yaml
permissions:
  required: true
  defaultAtWorkflow:
    # Exigir permissions explícitos al nivel de workflow
    enforce: true
    # Plantilla de mínimos (ajusta según tu seguridad)
    template:
      contents: read
      pull-requests: read

runners:
  allow:
    - "ubuntu-latest"
    - "ubuntu-22.04"
    - "self-hosted:linux:x64:secure-group"
  denyMessage: "Runner no permitido. Usa uno de: ubuntu-latest, ubuntu-22.04 o etiqueta corporativa."

actions:
  requireAllowlist: true
  branchRefWarning: true        # warning si ref es branch (p.ej., main)
  pinToMajorOrSha: "major"      # opciones: major|sha|either

timeouts:
  jobDefaultMinutes: 30
  requireTimeoutFor:
    - "build"
    - "test"
    - "deploy"

triggers:
  mustInclude:
    - "pull_request"
  mustNotInclude:
    - "schedule" # prohibido salvo excepciones

naming:
  workflowName:
    pattern: "^[A-Z][A-Za-z0-9 .-]{3,60}$"
    message: "Usa un nombre capitalizado y descriptivo (4–60 chars)."
  jobId:
    pattern: "^[a-z0-9-]{3,30}$"
    message: "job.id en kebab-case (3–30 chars)."

artifacts:
  requireCodeScanningUpload: true  # si detecta *.sarif en steps previos

env:
  forbidPlainSecretsLike:
    - "AWS_"
    - "AZURE_"
  message: "Nunca declares secretos en env; usa 'secrets:' o variables a nivel repo/org."