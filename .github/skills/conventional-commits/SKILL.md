---
name: conventional-commits
description: "Genera mensajes de commit con el estándar Conventional Commits y guía la validación con commitlint."
license: MIT
---

# Objetivo
Ayudar a crear mensajes de commit consistentes (Conventional Commits) y a validar el rango de commits en PR usando commitlint.

# Cuándo usar
- Al escribir un mensaje de commit.
- Al preparar un PR y querer revisar los mensajes en el rango `BASE..HEAD`.

# Procedimiento (paso a paso)
1. Si el usuario pide "genera el commit", **pregunta por**:
   - `type` (feat|fix|docs|style|refactor|perf|test|build|ci|chore|revert)
   - `scope` (opcional, kebab-case: p.ej. `api`, `infra`, `docs`)
   - `subject` (imperativo, ≤72 chars)
   - (opcional) `body` y `BREAKING CHANGE:` si aplica.
2. Genera el mensaje en este formato:
   - `type(scope): subject`
   - incluir `body` y `BREAKING CHANGE:` según corresponda.
3. Valida mentalmente contra las reglas del archivo `commitlint.config.js` de este skill.
4. Si el usuario lo solicita, **prepara** el comando para lint de rango en PR:
   - `npx commitlint --from <BASE> --to <HEAD> --verbose`
5. Presenta 2–3 alternativas de `subject` concisas y sugiere mejoras si excede 72 chars.

# Reglas clave (resumen)
- `type` debe ser uno de: feat, fix, docs, style, refactor, perf, test, build, ci, chore, revert.
- `scope` en kebab-case (o vacío).
- `subject` en tono imperativo y minúsculas (o sentence-case corta).
- Evitar punto final en `subject`.

# Ejemplos
**Correcto**
- `feat(api): add pagination to list endpoints`
- `fix(app): handle null id in customer mapper`
- `refactor: extract date utils from order service`

**Con breaking change**
- `refactor(auth): replace legacy jwt library`
- _Body:_ "Migrate to `@acme/jwt2` for security updates."
- _Footer:_ `BREAKING CHANGE: token claims shape changed (see MIGRATION.md).`

# Recursos del skill
- `commitlint.config.js` (reglas exactas)
- `examples/messages.md` (más ejemplos)

# Limitaciones y notas
- Este skill **no ejecuta** herramientas por sí mismo. Se limita a generar/validar mensajes y a proponer comandos/archivos de configuración.
- Para enforcement en CI, combina con un workflow de commitlint en PR.