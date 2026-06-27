---
name: Generate Training Guide
description: Use this skill when asked to inspect a user-specified source code folder with static analysis and produce a comprehensive Markdown training tutorial saved under docs/training/.
---

# Generate Training Guide

Use this workflow to turn a code folder into a plain-English training guide for company employees who use Microsoft Outlook, Microsoft 365 Copilot, company-issued iPads, and work accounts.

## Inputs

- Require a user-specified source folder path.
- If the path is missing, ask for it before inspecting code.
- Keep all generated training files under `docs/training/`.

## Workflow

1. Inspect repository instructions first, especially `AGENTS.md` files that apply to `docs/training/`.
2. Confirm the source folder exists and identify its main languages, entry points, configuration files, routes, services, and dependencies using static inspection only.
3. Review code logic to identify:
   - Key user workflows and business processes.
   - Architecture and component relationships.
   - Setup, configuration, authentication, and environment requirements.
   - Outlook, Microsoft 365 Copilot, iPad, and work-account touchpoints when present or relevant.
   - Common gotchas, permissions issues, data-flow risks, and field-use limitations.
4. Create one front-end friendly Markdown tutorial in `docs/training/` with a clear, descriptive kebab-case filename.
5. Use plain, universal English for mixed skill levels. Avoid jargon where possible; define necessary technical terms.
6. Cite source files in the guide where helpful so maintainers can trace claims back to code.

## Required Tutorial Structure

Include these sections, in this order unless the user asks otherwise:

1. `# <Guide Title>`
2. `## High-level overview`
3. `## Architectural diagram concepts`
   - Describe diagram nodes and connections in text or Mermaid when useful.
   - Keep diagrams readable in Markdown renderers.
4. `## Step-by-step setup`
   - Include prerequisites, account assumptions, device notes, configuration, and verification steps.
5. `## Key workflows`
   - Explain the main workflows discovered from the source folder.
6. `## Common Gotchas`
   - Cover likely mistakes, permission problems, iPad constraints, Outlook/Copilot account issues, and operational risks.
7. `## Source reference`
   - List the most important inspected files and why they matter.

## Quality Bar

- Save only Markdown training output unless the user requests another artifact.
- Do not modify source code while generating the guide.
- Prefer concise tables, checklists, and numbered steps for front-end rendering.
- Make setup steps actionable for sales representatives, sales account associates, and field employees.
- State assumptions clearly when code does not reveal a detail.
- Run a lightweight check before finishing, such as confirming the output file exists and previewing its headings.
