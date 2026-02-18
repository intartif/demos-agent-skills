---
name: workflows-corp-policy
description: Valida patrones y estándares corporativos en workflows y actions reusables de GitHub Actions (.github/workflows/, actions/). Reporta incumplimientos y sugiere fixes.
license: Apache-2.0
compatibility: [claude, vscode-copilot, cursor]
metadata:
  domain: cicd
  skill_id: cicd.workflows.workflows-corp-policy
---

# cicd.workflows.workflows-corp-policy

## Cuándo usar
- Cuando se requiera validar que los workflows cumplen con los estándares corporativos.
- Al integrar nuevos workflows o modificar existentes en `.github/workflows/`.

## Entradas
- Antes de iniciar el análisis, siempre se solicita al usuario que indique qué workflows analizar. Puede elegir todos los workflows del repositorio o seleccionar archivos específicos.
- Workflows reusables YAML en `.github/workflows/*.yml` o `.yaml`.
- Actions reusables YAML en `actions/**/*.yml` o `actions/**/*.yaml`.
- Configuración de patrones y allowlist (`config/patterns.yml`, `config/actions-allowlist.yml`).

## Salidas
- Reporte de errores, advertencias y sugerencias por archivo/línea, categorizados con alertas tipo semáforo:
  - 🔴 error
  - 🟠 warning
  - 🟡 mejora
- Para cada hallazgo, se incluye un fragmento YAML concreto a modificar, agregar o eliminar, mostrando contexto antes/después.
- Antes de aplicar cambios, se solicita confirmación al usuario, listando los archivos impactados y el tipo de cambio (agregar, modificar, eliminar).
- Propuestas de fixes YAML cuando corresponda.

## Pasos
1. **Antes de cualquier análisis, solicitar explícitamente al usuario qué workflows desea analizar** (todas o selección específica). No continuar hasta recibir respuesta.
2. Cargar reglas y allowlist corporativa.
3. Analizar estructura, claves y cumplimiento de políticas.
4. Mostrar obligatoriamente un reporte y para ello debo usar el formato de salida definido en la sección "Formato de salida (OBLIGATORIO)".
5. (Opcional) Aplicar autofix guiado si el usuario lo autoriza.

## Checklist de calidad
- [ ] Permisos explícitos y mínimos en todos los workflows (`permissions: contents: read, pull-requests: write`).
- [ ] Acciones reusables públicas deben usarse siempre con versión específica (no usar @main, @master, @v1, etc; solo tags fijos o SHA).
- [ ] Nomenclatura de archivos: solo kebab-case y extensión `.yml` (no `.yaml`).
- [ ] Nomenclatura de `id` de jobs y steps: solo kebab-case.
- [ ] Nomenclatura de `inputs`, `outputs`, `environments` y `secrets`: solo snake_case.
- [ ] Todos los `inputs` obligatorios deben estar definidos y documentados.
- [ ] Comandos shell no deben imprimir información innecesaria (evitar `set -x`, `env`, etc).
- [ ] Todo `echo` usado para logs debe anteponer el área `[DevSecOps]`, ejemplo: `echo "[DevSecOps] - variable: $var1"`.
- [ ] Solo se permite el runner `ubuntu-22.04`.
- [ ] Cada job debe usar `summary` para logs o reportes.
- [ ] Acciones y versiones validadas contra allowlist.
- [ ] Runners aprobados y triggers correctos.
- [ ] Secrets y env seguros.
- [ ] Artifacts y SARIF correctamente gestionados.
- [ ] Naming y metadatos consistentes.
- [ ] Timeouts y matrices definidos donde aplica.
- [ ] Todos los archivos de workflows y actions reusables deben usar la extensión `.yml` (no `.yaml`).
- [ ] Validar también los actions reusables en `actions/` bajo las mismas reglas.

## **Formato de salida (OBLIGATORIO)**
Debo mostrar el reporte en Markdown con:
## WORKFLOW ANALIZADO (mostrar la ruta completa del archivo)
### Detalles de cada hallazgo (tipo semáforo, mensaje descriptivo)
### Por cada hallazgo debo mostrar en un bloque de Codigo el antes/después (solo si aplica)

## Ejemplos

**Entrada**
- Uso de action reusable pública sin versión fija.
- Uso de permisos incorrectos o ausentes.
- Archivo con nombre o id fuera de nomenclatura.
- Uso de runner no permitido.
- Uso de echo sin área `[DevSecOps]`.
- Falta de summary en jobs.
- Inputs obligatorios ausentes.
- Uso de comandos shell que imprimen información innecesaria.
- Archivo reusable action o workflow con extensión `.yaml`.

**Salida**
🔴 [error] Uso de action reusable pública sin versión fija en .github/workflows/ci.yml
Sugerencia: usa una versión específica (tag o SHA) en la referencia:
```yaml
    uses: actions/checkout@v4
```

🔴 [error] Permisos incorrectos en .github/workflows/ci.yml
Sugerencia: usa solo los permisos mínimos requeridos:
```yaml
permissions:
  contents: read
  pull-requests: write
```

🔴 [error] Nombre de archivo/id fuera de nomenclatura en .github/workflows/Build_CI.yaml
Sugerencia: renombra a .github/workflows/build-ci.yml y usa ids en kebab-case.

🔴 [error] Uso de runner no permitido en .github/workflows/deploy.yml
Sugerencia: reemplaza el runner por `ubuntu-22.04`.
```yaml
  runs-on: ubuntu-22.04
```

🔴 [error] Uso de echo sin área [DevSecOps] en actions/sonar/action.yml
Sugerencia: reemplaza por:
```yaml
  run: echo "[DevSecOps] - variable: $var1"
```

🔴 [error] Falta de summary en job deploy de .github/workflows/deploy.yml
Sugerencia: agrega un paso que use `summary` para logs o reportes.

🔴 [error] Inputs obligatorios ausentes en actions/publish-artifactory/action.yml
Sugerencia: define y documenta los inputs requeridos.

🔴 [error] Comando shell imprime información innecesaria en .github/workflows/ci.yml
Sugerencia: elimina o ajusta el comando para evitar información sensible o innecesaria.

🔴 [error] Archivo actions/mi-action.yaml no cumple con la extensión requerida (.yml)
Sugerencia: renombra a actions/mi-action.yml
**Entrada**
- Workflow con permisos globales ausentes.
- Archivo reusable action o workflows con extensión `.yaml`.

**Salida**
🔴 [error] Falta permisos mínimos en .github/workflows/ci.yml
Sugerencia: agrega al inicio del workflow:

```yaml
permissions:
  contents: read
  pull-requests: read
```

🔴 [error] Archivo actions/mi-action.yaml no cumple con la extensión requerida (.yml)
Sugerencia: renombra a actions/mi-action.yml

¿Deseas aplicar este cambio en .github/workflows/ci.yml?

**Entrada**
- Workflow usando un runner no aprobado.

**Salida**
🔴 [error] Runner no permitido en .github/workflows/deploy.yml
Sugerencia: reemplaza el runner por uno aprobado (ubuntu-latest, ubuntu-22.04 o self-hosted:linux:x64:secure-group).

Fragmento a modificar:
```yaml
  runs-on: windows-latest
```

¿Deseas aplicar este cambio en .github/workflows/deploy.yml?

## Referencias
- config/patterns.yml
- config/actions-allowlist.yml