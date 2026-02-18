---
name: generate-reusable-workflow
description: Permite crear un workflow reusable a partir de uno existente, seleccionando jobs y nombre final.
license: Apache-2.0
compatibility: [claude, vscode-copilot, cursor]
metadata:
   domain: cicd
   skill_id: cicd.workflows.generate-reusable-workflow
---

# cicd.workflows.generate-reusable-workflow

## Cuándo usar
- Cuando se requiera crear un workflow reusable basado en uno existente, seleccionando jobs específicos.
- Cuando se necesite personalizar un workflow a partir de una plantilla previa.

## Entradas
- `workflow_base`: nombre del workflow base a copiar.
- `jobs`: lista de jobs a incluir.
- `workflow_name`: nombre visible del nuevo workflow.
- `filename`: nombre del archivo YAML destino.

## Salidas
- YAML del workflow generado.
- Mensaje de confirmación y advertencia si el archivo existe.

## Pasos del Skill

1. **Listar workflows disponibles**
   - Se listan todos los workflows existentes en `.github/workflows/`.
   - El usuario debe seleccionar uno como base.

2. **Seleccionar jobs a incluir**
   - Se muestran los jobs definidos en el workflow base seleccionado.
   - El usuario debe seleccionar uno o más jobs a incluir en el nuevo workflow.

3. **Indicar nombre del nuevo workflow**
   - El usuario debe ingresar el nombre del nuevo workflow (tanto el nombre visible como el nombre de archivo YAML).

4. **Generar el nuevo workflow**
   - Se crea un nuevo archivo YAML en `.github/workflows/`.
   - El workflow generado incluye solo los jobs seleccionados.
   - Se agrega un comentario en la cabecera indicando que fue generado mediante agent skills.

## Checklist de calidad
- [ ] No sobrescribe workflows existentes.
- [ ] Permite seleccionar uno o más jobs.
- [ ] Permite definir nombre visible y archivo.
- [ ] Agrega comentario de generación por agent skills.
- [ ] Mensajes claros ante conflictos o errores.

## Ejemplos
**Entrada**
- workflow_base: build-and-test.yml
- jobs: [build, test]
- workflow_name: CI Build & Test
- filename: ci-build-test.yml

**Salida**
- YAML generado con los jobs seleccionados y comentario de generación.

**Entrada**
- workflow_base: deploy-app.yml
- jobs: [deploy]
- workflow_name: Deploy Only
- filename: deploy-only.yml

**Salida**
- YAML generado solo con el job deploy.

## Referencias
- .github/workflows/
- Ejemplo de comentario:
   ```yaml
   # Este workflow fue generado automáticamente mediante agent skills (generate-reusable-workflow)
   ```
