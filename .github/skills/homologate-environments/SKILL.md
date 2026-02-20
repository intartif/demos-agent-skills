---
name: homologate-environments
description: Homologa workflows de GitHub Actions entre ambientes de desarrollo y producción, asegurando que los de producción solo difieran en la ausencia de jobs de escaneo, pruebas, formateo o linters.
license: Apache-2.0
compatibility: [claude, vscode-copilot, cursor]
metadata:
  domain: cicd
  skill_id: cicd.workflows.homologate-environments
---

# cicd.workflows.homologate-environments

## Cuándo usar
- Al validar o corregir workflows de GitHub Actions para homologar ambientes dev/prod.
- Cuando se requiera asegurar que el workflow de producción solo difiere en la ausencia de jobs prohibidos.
- Para aplicar políticas de seguridad y estabilidad en CI/CD.

## Entradas
- Workflow de desarrollo (ruta YAML, debe tener sufijo `-dev`).
- Workflow de producción (ruta YAML, debe tener sufijo `-prod`).

## Salidas
- Reporte de diferencias no permitidas y sugerencias de fixes para homologar el workflow de producción.

## Pasos
1. Busca los workflows de desarrollo con sufijo `-dev` en el repositorio.
2. **Antes de cualquier análisis, revisión o corrección, se debe solicitar explícitamente al usuario qué workflows de desarrollo (sufijo `-dev`) desea analizar** (todas o selección específica). No continuar hasta recibir respuesta.
3. Buscar y validar que el workflow indicado en el paso anterior tenga su workflow para producción con sufijo `-prod`. Si no existe, reportar error y sugerir crear el workflow de producción basado en el de desarrollo.
4. Comparar ambos workflows:
  - Jobs prohibidos en prod: lint, test, snyk, sonar, fortify, prettier, coverage, scan, semgrep, format, type-check, snyk-scan, unit-test o jobs propios de escaneo o pruebas del flujo de CI.
  - El resto de jobs, steps y configuración deben ser idénticos.
  - Los jobs que deben estar obligatorios en producción son los relacionados con el despliegue, release, build, deploy o similares.
  - El workflow de desarrollo (`-dev`) NUNCA debe modificarse. Cualquier ajuste o fix se debe aplicar únicamente al workflow de producción (`-prod`).
5. Mostrar obligatoriamente un reporte y para ello debo usar el formato de salida definido en la sección "Formato de salida (OBLIGATORIO)". Debo reportar diferencias no permitidas y sugerir fixes. 
6. Solicitar confirmación antes de aplicar fixes automáticos (si aplica), dejando claro que solo el workflow de producción será modificado.


## **Formato de salida (OBLIGATORIO)**
Debo mostrar el reporte en Markdown con:
## WORKFLOW DE PRODUCCIÓN (mostrar la ruta completa del archivo)
### Detalles de cada hallazgo (tipo semáforo, mensaje descriptivo)
### Por cada hallazgo debo mostrar en un bloque de Codigo el antes/después (solo si aplica)


## Checklist de calidad
- [ ] Detecta claves y estructura YAML inválida.
- [ ] Valida sufijo `-prod` en workflow de producción.
- [ ] Marca como error jobs prohibidos en prod.
- [ ] Reporta advertencias y errores en formato Actions.
- [ ] Permite integración en pipelines CI/CD.
- [ ] Ejecuta tests automáticos sobre el script.


## Estructura recomendada para el skill:
- ./.github/skills/homologate-environments/SKILL.md
- Código fuente del skill en ./.github/skills/homologate-environments/scripts/
- Tests y ejemplos en ./.github/skills/homologate-environments/scripts/
- Documentación en ./docs/homologate-environments.md

## Ejemplo de uso
```bash
python .github/skills/homologate-environments/scripts/homologar.py angular-cicd-reusable.yml angular-cicd-reusable-prod.yml
```

## Referencias
- .github/skills/homologate-environments/scripts/homologar.py
- .github/skills/homologate-environments/scripts/test_homologar.py
- docs/homologate-environments.md