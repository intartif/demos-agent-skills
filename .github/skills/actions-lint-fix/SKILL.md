---
name: actions-lint-fix
description: Revisa, lintea y corrige actions reusables de GitHub Actions: formato, claves válidas, y validación de versiones de acciones (e.g., detectar 'uses: actions/checkout@v15' y sugerir @v6 o pin a SHA). Valida claves requeridas 'inputs' y 'runs'.
license: Apache-2.0
compatibility: [claude, vscode-copilot, cursor]
metadata:
  domain: cicd
  skill_id: cicd.workflows.actions-lint-fix
---

# cicd.workflows.actions-lint-fix

## Cuándo usar
- Al validar o corregir actions reusables YAML de GitHub Actions en `actions/**/*.yml` o `actions/**/*.yaml`.
- Cuando se requiera asegurar versionado correcto de acciones (`uses:`).
- Para aplicar políticas de seguridad y estabilidad en CI/CD.
- Al integrar validaciones automáticas en pipelines o PRs.

## Entradas
- Antes de iniciar el análisis, siempre se solicita al usuario que indique qué actions se va a analizar. Puede elegir todas las actions del repositorio o seleccionar archivos específicos.
- Ruta raíz del repositorio (por defecto: `.`).
- Actions reusables en `actions/**/*.yml` o `actions/**/*.yaml`.

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
2. **Antes de cualquier análisis, solicitar explícitamente al usuario qué actions desea analizar** (todas o selección específica). No continuar hasta recibir respuesta.
3. Ejecutar lint estructural sobre las actions reusables seleccionadas usando:
    - `yamllint` para validar sintaxis y estilo YAML.
    - `act` para simular la ejecución de las actions localmente.
    - Si la action ejecuta scripts `.sh`, validar cada uno con:
       - `shellcheck` para análisis estático de shell scripts.
       - `bash -n` para validación de sintaxis bash.
4. Validar claves requeridas y prohibidas:
   - Requeridas: `name`, `description`, `inputs`, `runs` en la raíz.
   - Prohibidas: `on`, `jobs` en la raíz.
5. Validar estructura de yml (`uses:`) usando:
   - `scripts/validate-yml-structure.sh` (requiere `jq`).
6. Validar versiones de acciones (`uses:`) usando:
   - `scripts/fix-actions-versions.sh` (requiere `jq`).
7. Corregir versiones irreales/no soportadas con:
   - `scripts/fix-actions-versions.sh`.
8. Mostrar obligatoriamente un reporte y para ello debo usar el formato de salida definido en la sección "Formato de salida (OBLIGATORIO)".
9. Al finalizar el reporte, solicitar al usuario si desea aplicar los cambios encontrados.
10. Si el usuario acepta, aplicar los fixes automáticamente.

## **Formato de salida (OBLIGATORIO)**
Debo mostrar el reporte en Markdown con:
## ACTION ANALIZADO (mostrar la ruta completa del archivo)
### Datos del action reusable (usar la carpeta del action. Por ejemplo: si la ruta es: actions/mi-action/action.yml el nombre a mostrar es mi-action)
### Resumen de hallazgos (número de errores, advertencias, mejoras)
### Detalles de cada hallazgo (tipo, mensaje)
#### Por cada hallazgo debo mostrar en un bloque de Codigo el antes/después (si aplica)


## Checklist de calidad
- [ ] Detecta claves y estructura YAML inválida.
- [ ] Valida claves requeridas: `name`, `description`, `inputs`, `runs`.
- [ ] Marca como error claves prohibidas: `on`, `jobs` en la raíz.
- [ ] Extrae y valida todos los `uses:`.
- [ ] Aplica política de versiones mínimas/recomendadas.
- [ ] Corrige versiones irreales/no soportadas.
- [ ] Reporta advertencias y errores en formato Actions.
- [ ] Permite integración en pipelines CI/CD.
- [ ] Ejecuta `yamllint` sobre las actions.
- [ ] Ejecuta `act` para simular actions.
- [ ] Ejecuta `shellcheck` y `bash -n` sobre scripts `.sh` referenciados.

## Ejemplos

**Entrada**
- Action sin clave `name`, `description`, `inputs` o `runs` en la raíz

**Salida**
🔴 [error] Falta la clave requerida 'name', 'description', 'inputs' o 'runs' en la raíz de la action.

**Entrada**
- Action con `on` o `jobs` en la raíz

**Salida**
🔴 [error] Clave no permitida 'on' o 'jobs' en la raíz de una action reusable.

**Entrada**
- Action con `uses: actions/checkout@main`

**Salida**
🟠 [warning] Acción actions/checkout@main no está permitida.
Sugerencia: reemplaza por actions/checkout@v6 o pin a SHA permitido.

Fragmento a modificar en actions/mi-action/action.yml:
- uses: actions/checkout@main
+ uses: actions/checkout@v6

¿Deseas aplicar este cambio?

## Referencias
- scripts/fix-actions-versions.sh
- config/actions-versions.json
- [GitHub Actions: Versioning Best Practices](https://github.blog/ai-and-ml/github-copilot/how-to-maximize-github-copilots-agentic-capabilities/)
- [Copilot Extensions Guide](https://resources.github.com/learn/pathways/copilot/extensions/building-your-first-extension/)
- [YouTube: Actions Versioning](https://www.youtube.com/watch?v=0ObW2ERZYgA)
- [Lint YAML Workflows](https://dev.to/nickytonline/creating-your-first-github-copilot-extension-a-step-by-step-guide-28g0)
