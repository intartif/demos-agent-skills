---
title: Reusable Workflow: react-cicd-prod
logo: ../.github/skills/reusable-docs/templates/NTT-Data-Logo.svg
---

# React CI/CD Reusable (Producción)

<img src="../.github/skills/reusable-docs/templates/NTT-Data-Logo.svg" alt="NTT DATA" width="180"/>

## Descripción
Workflow reusable para CI/CD de proyectos React en ambiente de producción, con jobs condicionales y parametrización por inputs. Permite build y despliegue seguro, con cierre automático de issues.

## Ubicación
`.github/workflows/react-cicd-reusable-prod.yml`

## Inputs
- `branch` (requerido): Rama objetivo.
- `apply-build` (requerido): Ejecutar build (string).
- `apply-deploy` (requerido): Ejecutar deploy (string).
- `issue-id` (requerido): Identificador de issue.
- `creator` (requerido): Usuario creador.

## Jobs principales
- `assign-issue`: Asigna y comenta issue.
- `build`: Build del proyecto.
- `deploy`: Deploy a GitHub Pages (condicional).
- `close-issue`: Cierra/comenta issue según resultado.

## Ejemplo de uso
```yaml
jobs:
  call-react-cicd-prod:
    uses: ./.github/workflows/react-cicd-reusable-prod.yml
    with:
      branch: 'main'
      apply-build: 'Sí'
      apply-deploy: 'Sí'
      issue-id: '123'
      creator: 'usuario'
```

## Notas
- Incluye lógica condicional para ejecución de jobs.
- Cumple estándares DevSecOps.
- Generado automáticamente por agent skills.

---
**NTT DATA Confidential**
