<!-- Logo corporativo NTT DATA -->
<p align="right"><img src="../../templates/NTT-Data-Logo.svg" alt="NTT DATA Logo" width="120"/></p>

# Action reusable: `sast-semgrep`

**Descripción:**
> Run Semgrep SAST and upload SARIF if available.

---

## Inputs
| Nombre | Descripción | Requerido | Default |
|--------|-------------|-----------|---------|
| rules  | Ruta a reglas o --config argument | No | "" |

## Outputs
| Nombre | Descripción |
|--------|-------------|
| report | Archivo SARIF generado por semgrep (semgrep-report.json) |

## Jobs y Steps
1. **Checkout**: Clona el repositorio usando `actions/checkout@v4`.
2. **Install semgrep**: Instala la herramienta Semgrep vía pip.
3. **Run semgrep**: Ejecuta Semgrep con la configuración indicada y genera el reporte SARIF.
4. **Upload SARIF (if available)**: Sube el archivo SARIF generado usando `github/codeql-action/upload-sarif@v2`.

---

<p align="center"><sub>Documentación generada automáticamente · NTT DATA</sub></p>
