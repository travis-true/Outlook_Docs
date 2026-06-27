# Outlook on iPadOS guide build

Run commands from the repository root. Use `python3` on macOS and in CI-like shells.

## Build the main guide

```bash
python3 build/build_ipados_guide.py
```

The main guide build uses repository-local Markdown and media assets. Generated deliverables are written to `build/output/`.

## Build the supplemental asset package

```bash
python3 build/build_supplemental_assets.py
```

This command reads these repository sources:

- `13. Supplemental support package.md`
- `BCBSKS-ID-Prompt-Guide-v4.0.md`
- `BCBSKS_Master_Brand_Kit.md`
- `10. Screenshot capture and annotation plan.md`, where relevant

Generated local outputs are written under `build/output/supplemental-assets/`.

Generated folders:

- `01-printable-word-assets/` — six editable binary `.docx` Word files.
- `02-video-production-package/` — eight production folders with DOCX AV scripts, DOCX storyboards, CSV shot lists, draft SRT captions, TXT transcript drafts, Markdown audio-description notes, and an XLSX production manifest.
- `03-forms-implementation-package/` — DOCX implementation guide, XLSX form specifications, XLSX SharePoint tracking schema, Markdown branching logic, Markdown workflow documentation, and accessibility checklist.
- `04-validation-reports/` — source inventory, validation results, publication blockers, and generated summary validation report.

The build also creates the local ZIP archive `build/output/supplemental-assets/Take-Control-of-Your-Inbox_Outlook-iPadOS_Supplemental-Assets_v1.0.zip`.

## Production handoff steps

1. Run `python3 build/build_supplemental_assets.py` from the repository root.
2. Review `build/output/supplemental-assets/04-validation-reports/validation-results.csv`.
3. Review `build/output/supplemental-assets/04-validation-reports/publication-blockers.md`.
4. Open the generated DOCX files locally and complete visual/layout review in Word.
5. Export PDF previews only from an approved local Word/PDF conversion workflow.
6. Record MP4 videos from a managed company iPad using dummy content; do not fabricate recordings.
7. Deploy forms only in the approved SharePoint/Microsoft Forms environment.
8. Use the generated ZIP for local handoff only after human review clears the blockers.

## No-fabrication rule

Do not fabricate screenshots, videos, logos, deployed forms, SharePoint resources, support links, keyboard shortcuts, PDF exports, MP4 recordings, or approval results. The supplemental builder reports missing production inputs as blockers instead of inventing them.

## Version-control note

Binary DOCX/XLSX/PDF/ZIP/MP4 deliverables are generated locally and ignored by Git. The repository commits the build system, requirements, README instructions, validation logic, and text reports. Re-run the build commands after checkout to recreate local binary artifacts.
