---
title: Reusable Workflow: others-cicd-dev
logo: https://www.nttdata.com/etc.clientlibs/nttdata/clientlibs/clientlib-site/resources/images/logo-nttdata.svg
---

# Reusable CI/CD Pipeline (others-cicd-dev)

![NTT DATA](https://www.nttdata.com/etc.clientlibs/nttdata/clientlibs/clientlib-site/resources/images/logo-nttdata.svg)

## Descripción
Workflow reusable para CI/CD multi-stack (Node.js, Java Maven/Gradle) con análisis de calidad, seguridad, build y despliegue. Parametrizable por entorno y con outputs reutilizables.

## Ubicación
`.github/workflows/others-cicd-reusable-dev.yml`

## Inputs
- `environment` (requerido): Entorno objetivo.
- `ref` (opcional): Git ref a checkout.
- `run-sonar` (opcional): Ejecutar SonarQube (bool).
- `run-snyk` (opcional): Ejecutar Snyk (bool).
- `deploy-enabled` (opcional): Habilitar despliegue (bool).

## Secrets
- `SONAR_TOKEN`: Token SonarQube.
- `SNYK_TOKEN`: Token Snyk.
- `DEPLOY_TOKEN`: Token de despliegue.

## Outputs
- `version`: Versión de la app.
- `app-name`: Nombre de la app.
- `deployment-url`: URL de despliegue.

## Jobs principales
- `prepare`: Extrae metadatos y prepara el entorno.
- `sonar-scan`: Análisis SonarQube (condicional).
- `snyk-scan`: Análisis Snyk (condicional).
- `build`: Build multi-stack (Node, Maven, Gradle).
- `deploy`: Despliegue y health check (condicional).

## Ejemplo de uso
```yaml
jobs:
  call-others-cicd:
    uses: ./.github/workflows/others-cicd-reusable-dev.yml
    with:
      environment: "dev"
      run-sonar: true
      run-snyk: true
      deploy-enabled: true
    secrets:
      SONAR_TOKEN: ${{ secrets.SONAR_TOKEN }}
      SNYK_TOKEN: ${{ secrets.SNYK_TOKEN }}
      DEPLOY_TOKEN: ${{ secrets.DEPLOY_TOKEN }}
```

## Notas
- Soporta Node.js, Maven y Gradle.
- Incluye lógica condicional para jobs de análisis y despliegue.
- Cumple estándares DevSecOps.
- Generado automáticamente por agent skills.

---
**NTT DATA Confidential**
