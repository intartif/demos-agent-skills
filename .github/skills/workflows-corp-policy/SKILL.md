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
- [ ] Permisos explícitos y mínimos en todos los workflows.
- [ ] Acciones y versiones validadas contra allowlist.
- [ ] Runners aprobados y triggers correctos.
- [ ] Secrets y env seguros.
- [ ] Artifacts y SARIF correctamente gestionados.
- [ ] Naming y metadatos consistentes.
- [ ] Timeouts y matrices definidos donde aplica.
- [ ] Todos los archivos de workflows y actions reusables deben usar la extensión `.yml` (no `.yaml`).

## **Formato de salida (OBLIGATORIO)**
Debo mostrar el reporte en Markdown con:
## WORKFLOW ANALIZADO (mostrar la ruta completa del archivo)
### Detalles de cada hallazgo (tipo semáforo, mensaje descriptivo)
### Por cada hallazgo debo mostrar en un bloque de Codigo el antes/después (solo si aplica)

## Ejemplos
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