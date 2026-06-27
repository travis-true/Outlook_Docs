# Outlook on iPadOS guide build

Run commands from the repository root.

## Build the main guide

```bash
python build/build_ipados_guide.py
```

The main guide build uses repository-local Markdown and media assets. Generated deliverables are written to `build/output/`.

## Build the supplemental asset package

```bash
python build/build_supplemental_assets.py
```

This command reads `13. Supplemental support package.md` and regenerates the supplemental package under `build/output/supplemental-assets/`.

Generated folders:

- `01-printable-word-assets/` — text-only `.docx.md` Word production sources plus `.pdf.md` PDF export stubs.
- `02-video-production-package/` — eight video package folders with script, caption placeholder, and manifest files.
- `03-forms-implementation-package/` — SharePoint/Microsoft Forms implementation notes and form schema.
- `04-validation-reports/` — source inventory, printable asset validation CSV, and summary validation report.

The build also writes `build/output/Take-Control-of-Your-Inbox_Outlook-iPadOS_Supplemental-Assets_v1.0.zip.md`. This is a text-only archive manifest. The intended production ZIP is not committed because binary files are not supported in this review workflow.

## Production handoff steps

1. Run `python build/build_supplemental_assets.py` from the repository root.
2. Review `build/output/supplemental-assets/04-validation-reports/supplemental-assets-validation-report.md`.
3. Use the `.docx.md` files in `01-printable-word-assets/` as the Word production sources on an approved production workstation.
4. Export PDFs from the approved Word originals only after review.
5. Record videos from a managed company iPad using dummy content; do not generate or fabricate MP4 files from the script placeholders.
6. Deploy the forms from the implementation package only in the approved SharePoint/Microsoft Forms environment.
7. Create the final ZIP outside the repo from the reviewed production files when binary packaging is allowed.

## No-fabrication rule

Do not fabricate screenshots, videos, logos, deployed forms, SharePoint resources, support links, keyboard shortcuts, PDF exports, ZIP archives, or approval results. The supplemental builder creates only text-based production sources, stubs, manifests, and validation reports.

## Version-control note

Binary DOCX/PDF/ZIP/MP4 deliverables are not committed. Re-run the build commands after checkout to recreate reviewable text artifacts. Markdown, CSV, JSON, and VTT files remain reviewable text artifacts.
