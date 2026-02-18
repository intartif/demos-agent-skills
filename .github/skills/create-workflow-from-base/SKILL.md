---
name: create-workflow-from-base
description: Genera y mantiene un workflow reusable de CI/Sec/Build/Deploy a partir de la plantilla corporativa, parametrizado por tecnología y con deploy opcional.
license: Apache-2.0
compatibility: [claude, vscode-copilot, cursor]
metadata:
  domain: cicd
  skill_id: cicd.workflows.create-workflow-from-base
---

# cicd.workflows.create-workflow-from-base

## Cuándo usar
- Cuando se necesite publicar o actualizar el reusable corporativo en `org/workflows` o un repo de plataforma.
- Cuando un equipo requiera un pipeline estándar para múltiples stacks con mínima configuración.

## Entradas
- `inputs.tech`: tecnología (`python`, `typescript`, `kotlin`, `swift`, `java`, `dotnet`, `go`, `node`)
- `inputs.runner`: runner (por defecto `ubuntu-latest`, permite `macos-latest` para iOS/Swift)
- `build_cmd`: comando de build (opcional)
- `deploy_cmd`: comando de deploy (opcional)
- `run_deploy`: activar/desactivar deploy
- Secrets para Sonar, Snyk, Deploy (opt-in)

## Salidas
- YAML del reusable listo para usar
- Ejemplos de caller
- Mensajes claros si faltan secretos

## Pasos
1. Crear o actualizar el archivo en `templates/reusable-ci-security-build-deploy.yml` con la plantilla base y parámetros.
2. Seleccionar comandos por defecto según tecnología si no se proveen.
3. Respetar `run_deploy` para activar/desactivar el job de deploy.
4. No exponer secretos ni ecos en claro; hacer skip si faltan tokens.
5. Entregar YAML y ejemplos de uso.

## Checklist de calidad
- [ ] Usa pin de actions por versión mayor.
- [ ] Permisos mínimos y explícitos.
- [ ] Comandos por defecto según tecnología.
- [ ] Mensajes claros ante falta de secretos.
- [ ] Ejemplo de caller incluido.

## Ejemplos
**Entrada**
- tech: typescript
- sonar_project_key: org:app

**Salida**
- YAML reusable con steps de build y Sonar.

**Entrada**
- tech: python
- run_deploy: false

**Salida**
- YAML reusable sin job de deploy.

## Referencias
- templates/reusable-ci-security-build-deploy.yml
- examples/caller-example.yml