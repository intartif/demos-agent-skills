<div style="display: flex; justify-content: space-between; align-items: flex-start;">
  <hr style="width: 60%; margin-top: 32px; margin-bottom: 0; border: 1px solid #ccc;">
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/09/NTT-Data-Logo.svg/960px-NTT-Data-Logo.svg.png" alt="NTT Data Logo" width="110" align="right" style="margin-left: 16px; margin-bottom: 0;"/>
</div>

<p align="right"><sub>Generado por NTT DATA</sub></p>

# 🚀 validate-inputs — Reusable Action

---

## 📝 Descripción
Valida inputs requeridos y opcionales

> Esta acción define su metadata en `action.yml` (inputs/outputs/runs).  
> Para **composite actions**, el bloque `runs.using: composite` agrupa múltiples steps y requiere `shell` por step.

---

## 🧩 Inputs
| Nombre | Requerido | Default | Descripción |
|---|:---:|---|---|
| `app-name` | ✅ | — | Nombre de la aplicación |
| `version` | — | — | Versión (semver preferible) |
| `path` | — | — | Ruta que debe existir |

---

## 📤 Outputs
_No define outputs._

---

## Ejemplo de uso

```yaml
- name: validate-inputs step
  uses: <owner>/<repo>/actions/validate-inputs@<ref>
  with:
    app-name: <value>
    version: <value>
    path: <value>
  env:
    SONAR_TOKEN: ${{ secrets.SONAR_TOKEN }}
    SONAR_HOST_URL: ${{ secrets.SONAR_HOST_URL }}
```

---
**NTT DATA Confidential**
