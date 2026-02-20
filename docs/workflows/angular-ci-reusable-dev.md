<div style="display: flex; justify-content: space-between; align-items: flex-start;">
  <hr style="width: 60%; margin-top: 32px; margin-bottom: 0; border: 1px solid #ccc;">
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/09/NTT-Data-Logo.svg/960px-NTT-Data-Logo.svg.png" alt="NTT Data Logo" width="110" align="right" style="margin-left: 16px; margin-bottom: 0;"/>
</div>

<p align="right"><sub>Generado por NTT DATA</sub></p>

# 🚀 Angular CI Reusable — Reusable Workflow

---

## 📝 Descripción
Reusable workflow para CI/CD de aplicaciones Angular. Se invoca con `workflow_call` y expone entradas/secretos/outputs para ser consumidos desde otros repos o workflows.

> Este workflow está diseñado para ser llamado con **`on: workflow_call`**. Usa **inputs** y **secrets** definidos en el bloque `on.workflow_call` y puede exponer **outputs** a su caller.  
> https://docs.github.com/en/actions/how-tos/reuse-automations/reuse-workflows

---

## 🧩 Inputs
| Nombre | Tipo | Requerido | Default | Descripción |
|---|---|:---:|---|---|
| `branch` | `string` | ✅ | — | Branch del código a desplegar |
| `app-version` | `string` | ✅ | — | Versión de la aplicación (semver) |
| `environment` | `string` | ✅ | — | Entorno de destino (dev, qa, staging, production) |
| `node-version` | `string` | — | 18 | Versión de Node.js |
| `angular-version` | `string` | — | 18 | Versión de Angular CLI |
| `run-unit-tests` | `boolean` | — | true | Ejecutar tests unitarios |
| `run-e2e-tests` | `boolean` | — | false | Ejecutar tests e2e |
| `run-lint` | `boolean` | — | true | Ejecutar análisis de código (lint) |
| `generate-coverage` | `boolean` | — | false | Generar reporte de coverage |
| `production-mode` | `boolean` | — | true | Build en modo producción |
| `clear-cache` | `boolean` | — | false | Limpiar caché antes del build |
| `create-backup` | `boolean` | — | false | Crear backup antes del despliegue |
| `health-check` | `boolean` | — | true | Ejecutar health check post-deployment |
| `issue-number` | `number` | — | 0 | Número del issue que disparó el workflow |
| `triggered-by` | `string` | — | automation | Usuario que disparó el deployment |

---

## 🔐 Secrets
| Nombre | Requerido | Descripción |
|---|:---:|---|
| `NPM_TOKEN` | — | Token de NPM para paquetes privados |
| `DEPLOY_TOKEN` | ✅ | Token para el despliegue |
| `AWS_ACCESS_KEY_ID` | — | AWS Access Key ID |
| `AWS_SECRET_ACCESS_KEY` | — | AWS Secret Access Key |
| `SLACK_WEBHOOK` | — | Webhook de Slack para notificaciones |
| `SONAR_TOKEN` | — | Token de SonarQube |

---

## 📤 Outputs
| Nombre | Descripción |
|---|---|
| `build-version` | Versión del build generado |
| `build-size` | Tamaño del build en MB |
| `test-results` | Resultado de los tests |

---

## 🛠️ Jobs
### `setup` — Setup and Validation

- Validación de inputs y generación de cache key para dependencias.

### `checkout` — Checkout and Setup

- Checkout del código, setup de Node.js, instalación de dependencias y Angular CLI, configuración de NPM y cache.

### `lint` — Code Quality Analysis

- Análisis de código con ESLint y SonarQube.

### `format` — Format

- Formateo de código fuente.

### `type-check` — Type Check

- Verificación de tipos con TypeScript o Angular build.

### `test` — Unit Tests

- Ejecución de tests unitarios, generación y subida de coverage, publicación de resultados.

### `e2e` — E2E Tests

- Ejecución de tests end-to-end con Playwright o Cypress, subida de screenshots de errores.

### `build` — Build Angular Application

- Build de la aplicación Angular, análisis y optimización del tamaño, generación de versión y subida de artefactos.

### `backup` — Create Backup

- Creación de backup del deployment actual en AWS si corresponde.

### `health-check` — Post-Deployment Health Check

- Espera de estabilización, ejecución de health checks y smoke tests.

### `notify` — Send Notifications

- Notificaciones a Slack sobre el resultado del despliegue.
