# Homologar workflows por ambiente

Este documento describe el skill `homologar-workflows-ambiente`.

## Objetivo
Homologar workflows de GitHub Actions entre ambientes de desarrollo y producción, asegurando que los de producción solo difieran en la ausencia de jobs de escaneo, pruebas, formateo o linters.

## Reglas
- El workflow de producción debe tener el sufijo `-prod`.
- Los jobs prohibidos en producción incluyen: lint, test, snyk, sonar, fortify, prettier, coverage, scan, semgrep.
- El resto de la configuración debe ser idéntica.

## Uso
1. Proporciona el workflow de desarrollo.
2. Proporciona el workflow de producción a homologar.
3. Ejecuta el script `homologar.py`.

## Output
- Diferencias detectadas.
- Sugerencias de fixes.

## Ejemplo
```
python homologar.py angular-cicd-reusable.yml angular-cicd-reusable-prod.yml
```

## Tests
Ejecuta `test_homologar.py` para validar el skill.

---

> Documentación generada automáticamente.
