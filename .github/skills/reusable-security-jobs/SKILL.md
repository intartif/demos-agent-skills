---
name: reusable-security-jobs
description: "Agrega y parametriza jobs de análisis (Sonar, Snyk, Fortify) en un workflow reusable de GitHub Actions, subiendo resultados en SARIF."
license: MIT
---

# Objetivo
Facilitar que el agente inserte, parametrice y/o actualice un workflow reusable de seguridad y calidad de código.

# Cuándo usar
- Cuando el usuario pida "agrega Sonar/Snyk/Fortify a este repo".
- Cuando quiera un workflow reusable invocable desde varios repos.
- Cuando pida subir SARIF a Code Scanning.

# Procedimiento
1. **Detectar** lenguaje(s) y si existe `.github/workflows/`:
   - Si no existe el reusable, **copiar** `templates/reusable-ci-security.yml` a `.github/workflows/reusable-ci-security.yml`.
   - Si el usuario prefiere jobs sueltos, **insertar** los de `templates/job-*.yml` en el workflow existente.
2. **Pedir datos mínimos** según herramienta:
   - **SonarCloud**: `sonar_project_key`, `sonar_organization`, `SONAR_TOKEN` (secret).
   - **SonarQube**: `sonar_host_url`, `sonar_project_key`, `SONAR_TOKEN` (secret).
   - **Snyk**: `SNYK_TOKEN` (secret).
   - **Fortify**: `FORTIFY_URL`, `FORTIFY_AUTH_TOKEN`, `FORTIFY_PROJECT_ID` (secrets).
3. **Ajustar inputs** del reusable (`language`, `build_command`, flags `*_enabled`) y **añadir secrets** en el `uses` llamador.
4. **Explicar** dónde ver resultados:
   - **Security → Code scanning alerts** (SARIF).
5. **Opcional**: configurar “quality gates” que fallen el job (p. ej., Snyk `--severity-threshold=high`).

# Recursos del skill (copiar/pegar)
- `templates/reusable-ci-security.yml` (workflow reusable con toggles)
- `templates/job-sonar.yml`, `templates/job-snyk.yml`, `templates/job-fortify.yml` (jobs modulares)

# Consideraciones
- Respeta permisos mínimos: `security-events: write` para subir SARIF.
- Para Fortify on-prem (ScanCentral) suele convenir runner self-hosted con herramientas preinstaladas.
- Este skill no gestiona secretos; instruye al usuario a crearlos en GitHub.