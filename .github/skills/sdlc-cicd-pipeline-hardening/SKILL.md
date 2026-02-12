---
name: sdlc-cicd-pipeline-hardening
description: Harden pipelines: signatures, provenance, approvals, gates.
license: Apache-2.0
compatibility:
  - claude
  - vscode-copilot
  - cursor
metadata:
  domain: sdlc
  skill_id: sdlc.cicd.pipeline_hardening
---
# sdlc.cicd.pipeline_hardening

## When to use
Use this skill when you need to: **Harden pipelines: add secrets, provenance, approvals, gates.**

## Inputs
- `pipeline_blueprint`
- `threats(optional)`

## Outputs
- `hardening_plan`
- `gates`

## Steps
1. Confirm the goal and constraints.
2. Gather missing context (ask concise questions if needed).
3. Produce the requested outputs in a structured format.
4. Highlight risks, assumptions, and next actions.

## Quality checklist
- The output is aligned to the stated inputs and constraints.
- The output is actionable and specific (no vague advice).
- Security/compliance considerations are called out when relevant.

## Examples
**Input**
- (Provide a short example request here)

**Output**
- (Provide an example response structure here)

## References
- See `references/` for supporting guidelines (if present).
