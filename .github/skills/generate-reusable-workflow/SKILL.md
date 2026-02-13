---
name: generate-reusable-workflow
description: Genera y mantiene un workflow reusable de CI/Sec/Build/Deploy a partir de la plantilla corporativa, parametrizado por tecnología y con deploy opcional.
license: MIT
---

# Objetivo
Crear o actualizar un workflow reusable estándar llamado **reusable-ci-security-build-deploy** que incluya:
- Preparación y metadatos de la app.
- Build parametrizable por tecnología o comando provisto.
- Scans de Sonar y Snyk (opt-in por secretos/inputs).
- Deploy opcional (enable/disable).
- Buenas prácticas (pin de actions por versión mayor, `set -euo pipefail`, permisos mínimos).

# Cuándo usar este skill
- Cuando se necesite publicar/actualizar el reusable corporativo en `org/workflows` o un repo de plataforma.
- Cuando un equipo requiera un pipeline estándar para múltiples stacks con mínima configuración.

# Instrucciones para el agente
1. **Crear/actualizar** el archivo en: `templates/reusable-ci-security-build-deploy.yml` con la versión más reciente de la plantilla base, extendida con:
   - `inputs.tech` (string) para indicar la tecnología (`python`, `typescript`, `kotlin`, `swift`, `java`, `dotnet`, `go`, `node`).
   - `inputs.runner` (string) para elegir el runner (default `ubuntu-latest`, permitir `macos-latest` para iOS/Swift si lo piden).
   - Resolución de `build_cmd` / `deploy_cmd`:
     - Si el usuario **no** provee `build_cmd`, **auto-seleccionar** un comando por defecto según `tech`.
     - Si el usuario **no** provee `deploy_cmd`, usar valor por defecto.
   - Mantener y respetar `run_deploy` para activar o desactivar el job `deploy`.

2. **No exponer secretos** ni ecos en claro. Si faltan tokens (Sonar/Snyk/Deploy), los steps deben hacer **graceful skip** con mensajes claros.

3. **Entregables**:
   - El YAML del reusable listo para pegar.
   - (Opcional) Ejemplos de *caller* que lo usen con `uses: org/workflows/.github/workflows/reusable-ci-security-build-deploy.yml@v1`.

4. **Convenciones**:
   - `name: reusable-ci-security-build-deploy`
   - `actions/checkout@v4`
   - `permissions: contents: read` global y permisos mínimos adicionales solo donde se necesiten.
   - `runs-on: ${{ inputs.runner }}` con default `ubuntu-latest`.

# Inferencia de comandos por tecnología (si no se especifican)
- **node/typescript**: `npm ci && npm run build`
- **python**: `pip install -U pip && pip install -r requirements.txt && pytest -q`
- **java**: `mvn -B -ntp clean package`
- **dotnet**: `dotnet restore && dotnet build --configuration Release && dotnet test --no-build`
- **go**: `go mod download && go build ./... && go test ./...`
- **kotlin**: `./gradlew build`
- **swift**: `swift build && swift test`

# Ejemplos de prompts
- "Crea el reusable con tech=typescript y sonar_project_key=org:app"
- "Genera el caller para python con run_deploy=false"
- "Actualiza el reusable para correr en macos-latest (swift)"