---
name: workflows-corp-policy
description: Valida patrones y estándares corporativos en workflows de GitHub Actions (.github/workflows). Reporta incumplimientos y sugiere fixes.
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
- Workflows YAML en `.github/workflows/*.yml` o `.yaml`.
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
1. Descubrir y parsear los workflows YAML.
2. Cargar reglas y allowlist corporativa.
3. Analizar estructura, claves y cumplimiento de políticas.
4. Emitir anotaciones y sugerencias de fixes.
5. (Opcional) Aplicar autofix guiado si el usuario lo autoriza.

## Checklist de calidad
- [ ] Permisos explícitos y mínimos en todos los workflows.
- [ ] Acciones y versiones validadas contra allowlist.
- [ ] Runners aprobados y triggers correctos.
- [ ] Secrets y env seguros.
- [ ] Artifacts y SARIF correctamente gestionados.
- [ ] Naming y metadatos consistentes.
- [ ] Timeouts y matrices definidos donde aplica.

## Ejemplos
**Entrada**
- Workflow con permisos globales ausentes.

**Salida**
🔴 [error] Falta permisos mínimos en .github/workflows/ci.yml
Sugerencia: agrega al inicio del workflow:

```yaml
permissions:
  contents: read
  pull-requests: read
```

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