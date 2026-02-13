---
name: workflows-lint-fix
description: "Lintea y corrige workflows de GitHub Actions: formato, claves inválidas, y validación de versiones de acciones (e.g., detectar 'uses: actions/checkout@v15' y sugerir @v6 o pin a SHA)."
license: MIT
---

# Objetivo

Proveer una capacidad automatizada para **revisar** y **corregir** archivos YAML de GitHub Actions en `.github/workflows/`, con foco en:

1) **Lint de sintaxis/estructura** (keys conocidas, `on`, `jobs`, `steps`, etc.).  
2) **Buenas prácticas de seguridad/estabilidad** (p. ej., evitar ramas en `uses:`).  
3) **Validación de versiones de acciones** → detectar referencias inválidas o no recomendadas, como `uses: actions/checkout@v15`, y proponer **major tag soportado** (p. ej., `@v6`) o **pin a SHA**.  
   - `actions/checkout` mantiene tags mayores (v4, v5, v6); `v15` no existe. [1](https://github.blog/ai-and-ml/github-copilot/how-to-maximize-github-copilots-agentic-capabilities/)[2](https://resources.github.com/learn/pathways/copilot/extensions/building-your-first-extension/)

> **Notas de referencia**  
> - **`actions/checkout`**: documentación y changelog oficiales (confirman versiones v4/v5/v6). [1](https://github.blog/ai-and-ml/github-copilot/how-to-maximize-github-copilots-agentic-capabilities/)  
> - **Buenas prácticas de versionado**: preferir **major tag** estable (`@vN`) o **SHA**; evitar `@latest` o ramas (`main/master`). [3](https://www.youtube.com/watch?v=0ObW2ERZYgA)

---

## Alcance del lint

- **Sintaxis y claves**: estructura de workflow (`name`, `on`, `permissions`, `env`, `jobs[].runs-on`, `jobs[].steps[]`, etc.). [4](https://dev.to/nickytonline/creating-your-first-github-copilot-extension-a-step-by-step-guide-28g0)
- **Acciones usadas**: extraer todos los `steps[].uses` con patrón `{owner}/{repo}(@|/path@){ref}`.  
- **Versiones**:  
  - **Permitido**:  
    - **SHA** (`@<40-hex>`): inmutable.  
    - **Major tag conocido** (p. ej., `@v6` para `actions/checkout`).  
  - **Warn**: `@branch` (e.g., `@main`, `@master`).  
  - **Error**: major inexistente o menor que el **mínimo** acordado por la org (e.g., `actions/checkout@v15` o `@v1` si tu mínima es `v4`).  
