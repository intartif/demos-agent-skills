---
name: conventional-commits
description: Genera mensajes de commit con el estándar Conventional Commits y guía la validación con commitlint.
license: Apache-2.0
compatibility: [claude, vscode-copilot, cursor]
metadata:
   domain: git
   skill_id: git.commits.conventional-commits
---

# git.commits.conventional-commits

## Cuándo usar
- Al escribir un mensaje de commit.
- Al preparar un PR y querer revisar los mensajes en el rango `BASE..HEAD`.

## Entradas
- `type`: tipo de commit (feat, fix, docs, style, refactor, perf, test, build, ci, chore, revert)
- `scope`: alcance opcional (kebab-case)
- `subject`: resumen imperativo (≤72 chars)
- `body`: descripción opcional
- `BREAKING CHANGE`: nota opcional

## Salidas
- Mensaje de commit formateado.
- Comando para validar rango de commits con commitlint.

## Pasos
1. Solicitar los campos necesarios al usuario.
2. Generar el mensaje en formato Conventional Commits.
3. Validar mentalmente contra las reglas de commitlint.
4. Proponer comando para validar rango de commits si se solicita.
5. Sugerir alternativas de subject si excede 72 caracteres.

## Checklist de calidad
- [ ] El tipo es válido y está en minúsculas.
- [ ] El scope es opcional y en kebab-case.
- [ ] El subject es imperativo y ≤72 caracteres.
- [ ] No termina en punto.
- [ ] Incluye body y BREAKING CHANGE si aplica.

## Ejemplos
**Entrada**
- type: feat
- scope: api
- subject: add pagination to list endpoints

**Salida**
- feat(api): add pagination to list endpoints

**Entrada**
- type: refactor
- scope: auth
- subject: replace legacy jwt library
- body: Migrate to `@acme/jwt2` for security updates.
- BREAKING CHANGE: token claims shape changed (see MIGRATION.md).

**Salida**
- refactor(auth): replace legacy jwt library
- Migrate to `@acme/jwt2` for security updates.
- BREAKING CHANGE: token claims shape changed (see MIGRATION.md).

## Referencias
- commitlint.config.js (reglas exactas)
- examples/messages.md (más ejemplos)
- https://www.conventionalcommits.org/
---
