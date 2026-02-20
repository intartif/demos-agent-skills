<div style="display: flex; justify-content: space-between; align-items: flex-start;">
  <hr style="width: 60%; margin-top: 32px; margin-bottom: 0; border: 1px solid #ccc;">
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/09/NTT-Data-Logo.svg/960px-NTT-Data-Logo.svg.png" alt="NTT Data Logo" width="110" align="right" style="margin-left: 16px; margin-bottom: 0;"/>
</div>

<p align="right"><sub>Generado por NTT DATA</sub></p>

# 🔐 vault-secrets — Reusable Action

---

## 📝 Descripción
Read a secret from Vault KV v2 and expose it as output (masked). Composite action para obtener secretos de HashiCorp Vault y exponerlos como output seguro en GitHub Actions.

> Esta acción define su metadata en `action.yml` (inputs/outputs/runs).  
> Para **composite actions**, el bloque `runs.using: composite` agrupa múltiples steps y requiere `shell` por step.

---

## 📥 Inputs
| Nombre         | Requerido | Default | Descripción                                      |
|---------------|:---------:|--------|--------------------------------------------------|
| `secret-path` | ✅        | —      | Ruta KV v2 en Vault (ej: secret/data/my/path)     |
| `json-key`    | ✅        | —      | Clave dentro del JSON data.data a extraer         |

---

## 📤 Outputs
| Nombre         | Descripción |
|---------------|-------------|
| `vault_secret`| Valor del secreto extraído (masked) |

---

## 🧩 Ejemplo de uso
```yaml
- name: Vault secret step
  uses: ./actions/vault-secrets/action.yml
  with:
    secret-path: "secret/data/my/path"
    json-key: "mykey"
  env:
    VAULT_ADDR: ${{ secrets.VAULT_ADDR }}
    VAULT_TOKEN: ${{ secrets.VAULT_TOKEN }}
```

---
**NTT DATA Confidential**
