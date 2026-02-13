
---
name: workflows-lint-fix
description: Lintea y corrige workflows de GitHub Actions: formato, claves inválidas, y validación de versiones de acciones (e.g., detectar 'uses: actions/checkout@v15' y sugerir @v6 o pin a SHA).
license: Apache-2.0
compatibility: [claude, vscode-copilot, cursor]
metadata:
  domain: cicd
  skill_id: cicd.workflows.workflows-lint-fix
---

# cicd.workflows.workflows-lint-fix

## Cuándo usar
- Al validar o corregir workflows YAML de GitHub Actions.
- Cuando se requiera asegurar versionado correcto de acciones (`uses:`).
- Para aplicar políticas de seguridad y estabilidad en CI/CD.
- Al integrar validaciones automáticas en pipelines o PRs.

## Entradas
- Ruta raíz del repositorio (por defecto: `.`).
- Workflows en `.github/workflows/*.yml` o `.yaml`.
- (Opcional) Configuración de versiones mínimas/recomendadas (`config/actions-versions.json`).


## Salidas
- Reporte de errores y advertencias sobre versionado y estructura, categorizados con alertas tipo semáforo:
  - 🔴 error
  - 🟠 warning
  - 🟡 mejora
- Para cada fix sugerido, se incluye un fragmento YAML antes/después mostrando el cambio concreto (por ejemplo, reemplazo de versión de acción).
- Antes de modificar archivos, se pide confirmación al usuario, mostrando el snippet y el archivo impactado.
- Corrección automática de versiones irreales/no soportadas.
- Mensajes de warning/error en formato GitHub Actions (`::warning`, `::error`).

## Pasos
1. Ejecutar lint estructural sobre los workflows.
2. Validar versiones de acciones (`uses:`) usando:
  - `scripts/validate-actions-versions.sh` (requiere `jq`).
3. Corregir versiones irreales/no soportadas con:
  - `scripts/fix-actions-versions.sh`.
4. Reportar advertencias y errores según política.

## Checklist de calidad
- [ ] Detecta claves y estructura YAML inválida.
- [ ] Extrae y valida todos los `uses:`.
- [ ] Aplica política de versiones mínimas/recomendadas.
- [ ] Corrige versiones irreales/no soportadas.
- [ ] Reporta advertencias y errores en formato Actions.
- [ ] Permite integración en pipelines CI/CD.


## Ejemplos
**Entrada**
- Workflow con `uses: actions/checkout@v15`

**Salida**
🔴 [error] Acción actions/checkout@v15 no está permitida.
Sugerencia: reemplaza por actions/checkout@v6

Fragmento a modificar en .github/workflows/ci.yml:
- uses: actions/checkout@v15
+ uses: actions/checkout@v6

¿Deseas aplicar este cambio?

**Entrada**
- Workflow con `uses: actions/checkout@main`

**Salida**
🟠 [warning] Acción actions/checkout@main no está permitida.
Sugerencia: reemplaza por actions/checkout@v6 o pin a SHA permitido.

Fragmento a modificar en .github/workflows/ci.yml:
- uses: actions/checkout@main
+ uses: actions/checkout@v6

¿Deseas aplicar este cambio?

**Salida**
- Error, sugerir `@v6`.

## Referencias
- scripts/validate-actions-versions.sh
- scripts/fix-actions-versions.sh
- config/actions-versions.json
- [GitHub Actions: Versioning Best Practices](https://github.blog/ai-and-ml/github-copilot/how-to-maximize-github-copilots-agentic-capabilities/)
- [Copilot Extensions Guide](https://resources.github.com/learn/pathways/copilot/extensions/building-your-first-extension/)
- [YouTube: Actions Versioning](https://www.youtube.com/watch?v=0ObW2ERZYgA)
- [Lint YAML Workflows](https://dev.to/nickytonline/creating-your-first-github-copilot-extension-a-step-by-step-guide-28g0)
