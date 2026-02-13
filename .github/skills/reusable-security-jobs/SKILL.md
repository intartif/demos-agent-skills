---
name: reusable-security-jobs
description: Agrega y parametriza jobs de análisis (Sonar, Snyk, Fortify) en un workflow reusable de GitHub Actions, subiendo resultados en SARIF.
license: Apache-2.0
compatibility: [claude, vscode-copilot, cursor]
metadata:
   domain: cicd
   skill_id: cicd.security.reusable-security-jobs
---

# cicd.security.reusable-security-jobs

## Cuándo usar
- Cuando el usuario pida agregar Sonar/Snyk/Fortify a un repositorio.
- Cuando se requiera un workflow reusable invocable desde varios repos.
- Cuando se necesite subir SARIF a Code Scanning.

## Entradas
- Lenguaje(s) del proyecto.
- Preferencia de workflow reusable o jobs sueltos.
- Secrets requeridos para cada herramienta (SONAR_TOKEN, SNYK_TOKEN, FORTIFY_AUTH_TOKEN, etc).
- Parámetros de configuración para cada análisis (project_key, organization, etc).

## Salidas
- Workflow reusable `.github/workflows/reusable-ci-security.yml`.
- Jobs modulares para Sonar, Snyk, Fortify.
- Configuración lista para subir resultados SARIF.

## Pasos
1. Detectar lenguaje(s) y existencia de workflows.
2. Copiar o insertar los templates necesarios según preferencia.
3. Solicitar y parametrizar los datos mínimos para cada herramienta.
4. Ajustar inputs y secrets en el reusable y el caller.
5. Explicar dónde ver los resultados y cómo configurar quality gates.

## Checklist de calidad
- [ ] Permisos mínimos y explícitos (`security-events: write`).
- [ ] Inputs y secrets correctamente parametrizados.
- [ ] Jobs modulares y reutilizables.
- [ ] SARIF correctamente subido a Code Scanning.
- [ ] Documentación de configuración y resultados.

## Ejemplos
**Entrada**
- Herramienta: Snyk
- Lenguaje: node

**Salida**
- Workflow reusable con job de Snyk y subida de SARIF.

**Entrada**
- Herramienta: SonarCloud y Fortify
- Lenguaje: java

**Salida**
- Workflow reusable con jobs de SonarCloud y Fortify, ambos subiendo SARIF.

## Referencias
- templates/reusable-ci-security.yml
- templates/job-sonar.yml
- templates/job-snyk.yml
- templates/job-fortify.yml
