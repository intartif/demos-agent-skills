---
name: workflows-lint-fix
description: Revisa y corrige los errores de sintaxis de los workflows reusables: formato, claves válidas, y validación de versiones de acciones (e.g., detectar 'uses: actions/checkout@v15' y sugerir @v6 o pin a SHA), ubicado en .github/workflows/*
license: Apache-2.0
compatibility: [claude, vscode-copilot, cursor]
metadata:
  domain: cicd
  skill_id: cicd.workflows.workflows-lint-fix
---

# cicd.workflows.workflows-lint-fix


## Cuándo usar
- Al validar o corregir workflows reusables YAML de GitHub Actions en `.github/workflows/`.
- Cuando se requiera asegurar versionado correcto de acciones (`uses:`).
- Para aplicar políticas de seguridad y estabilidad en CI/CD.
- Al integrar validaciones automáticas en pipelines o PRs.

## Entradas
- Antes de iniciar el análisis, siempre se solicita al usuario que indique qué workflows en `.github/workflows` se va a analizar. Puede elegir todas las workflows reusables del repositorio o seleccionar archivos específicos.
- Ruta raíz del repositorio (por defecto: `.`).
- Workflows reusables en `.github/workflows/*.yml` o `.yaml`.

## Salidas
- Reporte de errores, advertencias y mejoras sobre versionado, sintaxis y estructura, categorizados con alertas tipo semáforo:
  - 🔴 error
  - 🟠 warning
  - 🟡 mejora
- Para cada fix sugerido, se incluye un fragmento YAML antes/después mostrando el cambio concreto (por ejemplo, reemplazo de versión de acción).
- Antes de modificar archivos, se pide confirmación al usuario, mostrando el snippet y el archivo impactado.
- Corrección automática de versiones irreales/no soportadas.
- Mensajes de warning/error en formato GitHub Actions (`::warning`, `::error`).

## Pasos
1. **Chequeo previo de dependencias**: Antes de cualquier análisis, validar que las siguientes herramientas estén instaladas y disponibles en el entorno:
  - `yamllint`
  - `act`
  - `shellcheck`
  - `jq`
  Si alguna no está instalada o no es ejecutable, mostrar al usuario el comando recomendado para instalarla (por ejemplo: `pip install yamllint`, `brew install act`, `brew install shellcheck`, `brew install jq`).
  Ofrecer la opción de instalar automáticamente la dependencia si el usuario lo autoriza.
  Si el usuario acepta, ejecutar el comando de instalación y continuar; si no, detener el análisis y mostrar el mensaje correspondiente.
2. **Antes de cualquier análisis, solicitar explícitamente al usuario qué workflows desea analizar** (todas o selección específica). No continuar hasta recibir respuesta.
3. Ejecutar lint estructural sobre los workflows reusables en `.github/workflows` usando:
  - `yamllint` para validar sintaxis, estilo YAML y corregir automáticamente el espaciado/tabulado incorrecto (estructura y alineación de indentación).
  - Revisar y corregir el espaciado/tabulado en todos los archivos `.yml` o `.yaml` dentro de `.github/workflows` para asegurar que cumplen con la estructura YAML estándar (2 espacios por nivel, sin tabs).
  - `act` para simular la ejecución de los workflows localmente.
  - Si el workflow ejecuta scripts `.sh`, validar cada uno con:
    - `shellcheck` para análisis estático de shell scripts.
    - `bash -n` para validación de sintaxis bash.
4. Validar claves requeridas y prohibidas:
  - Requeridas: `on`, `jobs` en la raíz.
  - Prohibidas: `inputs`, `runs` en la raíz.
5. Validar versiones de acciones (`uses:`) usando:
  - `scripts/validate-yml-structure.sh` (requiere `jq`).
6. Validar versiones de acciones (`uses:`) usando:
  - `scripts/fix-actions-versions.sh` (requiere `jq`).
7. Corregir versiones irreales/no soportadas con:
  - `scripts/fix-actions-versions.sh`.
8. Mostrar obligatoriamente un reporte al usuario con un formato de salida definido en la sección "Formato de salida (OBLIGATORIO)".
9. Al finalizar el reporte, solicitar al usuario si desea aplicar los cambios encontrados.
10. Si el usuario acepta, aplicar los fixes automáticamente.

## **Formato de salida (OBLIGATORIO)**
Debo mostrar el reporte en Markdown con:
## WORKFLOW ANALIZADO (mostrar la ruta completa del archivo)
### Resumen de yamllint (si aplica)
### Resumen de act (si aplica)
### Resumen de shellcheck (si aplica)
### Resumen de bash -n (si aplica)
### Resultado de ejecución del script fix-actions-versions.sh (si aplica)


## Checklist de calidad
- [ ] Detecta claves y estructura YAML inválida.
- [ ] Valida claves requeridas: `on`, `jobs`.
- [ ] Marca como error claves prohibidas: `inputs`, `runs` en la raíz.
- [ ] Extrae y valida todos los `uses:`.
- [ ] Aplica política de versiones mínimas/recomendadas.
- [ ] Corrige versiones irreales/no soportadas.
- [ ] Reporta advertencias y errores en formato Actions.
- [ ] Permite integración en pipelines CI/CD.
- [ ] Ejecuta `yamllint` sobre los workflows.
- [ ] Ejecuta `act` para simular workflows.
- [ ] Ejecuta `shellcheck` y `bash -n` sobre scripts `.sh` referenciados.


## Ejemplos
**Entrada**
- Workflow sin clave `on` o `jobs` en la raíz

**Salida**
🔴 [error] Falta la clave requerida 'on' o 'jobs' en la raíz del workflow.

**Entrada**
- Workflow con `inputs` o `runs` en la raíz

**Salida**
🔴 [error] Clave no permitida 'inputs' o 'runs' en la raíz de un workflow.

**Entrada**
- Workflow con `uses: actions/checkout@v15`

**Salida**
🔴 [error] Acción actions/checkout@v15 no está permitida.
Sugerencia: reemplaza por actions/checkout@v6

Fragmento a modificar en .github/workflows/ci.yml:
- uses: actions/checkout@v15
+ uses: actions/checkout@v6

¿Deseas aplicar este cambio?

## Referencias
- scripts/fix-actions-versions.sh
- config/actions-versions.json
- [GitHub Actions: Versioning Best Practices](https://github.blog/ai-and-ml/github-copilot/how-to-maximize-github-copilots-agentic-capabilities/)
- [Copilot Extensions Guide](https://resources.github.com/learn/pathways/copilot/extensions/building-your-first-extension/)
- [YouTube: Actions Versioning](https://www.youtube.com/watch?v=0ObW2ERZYgA)
- [Lint YAML Workflows](https://dev.to/nickytonline/creating-your-first-github-copilot-extension-a-step-by-step-guide-28g0)
