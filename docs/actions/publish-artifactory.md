<div style="display: flex; justify-content: space-between; align-items: flex-start;">
  <hr style="width: 60%; margin-top: 32px; margin-bottom: 0; border: 1px solid #ccc;">
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/09/NTT-Data-Logo.svg/960px-NTT-Data-Logo.svg.png" alt="NTT Data Logo" width="110" align="right" style="margin-left: 16px; margin-bottom: 0;"/>
</div>

<p align="right"><sub>Generado por NTT DATA</sub></p>

# 🚀 publish-artifactory — Reusable Action

---

## 📝 Descripción
Publish artifacts to JFrog Artifactory using jfrog-cli.

> Esta acción define su metadata en `action.yml` (inputs/outputs/runs).  
> Para **composite actions**, el bloque `runs.using: composite` agrupa múltiples steps y requiere `shell` por step.

---

## 🧩 Inputs
| Nombre | Requerido | Default | Descripción |
|---|:---:|---|---|
| `artifact-path` | ✅ | — | Path to artifact(s) to publish (glob allowed) |
| `repo` | ✅ | — | Artifactory repo target |

---

## 📤 Outputs
_No define outputs._

---

## Ejemplo de uso

```yaml
- name: publish-artifactory step
  uses: <owner>/<repo>/actions/publish-artifactory@<ref>
  with:
    artifact-path: <value>
    repo: <value>
  env:
    ARTIFACTORY_URL: ${{ secrets.ARTIFACTORY_URL }}
    ARTIFACTORY_USER: ${{ secrets.ARTIFACTORY_USER }}
    ARTIFACTORY_API_KEY: ${{ secrets.ARTIFACTORY_API_KEY }}
```

---

**NTT DATA Confidential**