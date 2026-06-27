# Supplemental assets local build

## High-level overview

This repository includes a conflict-safe local builder for the Outlook on iPadOS supplemental asset package. It generates local DOCX, XLSX, CSV, SRT, TXT, Markdown, and ZIP deliverables under `build/output/supplemental-assets/` without fabricating screenshots, videos, logos, SharePoint links, shortcuts, or approvals.

## Architectural diagram concepts

Source Markdown files feed the Python builder. The builder writes printable Word assets, video production folders, forms implementation files, validation reports, publication blockers, and a final local ZIP package.

```text
Repository Markdown sources
  -> build/build_supplemental_assets_real.py
  -> build/output/supplemental-assets/
     -> 01-printable-word-assets/
     -> 02-video-production-package/
     -> 03-forms-implementation-package/
     -> 04-validation-reports/
     -> Take-Control-of-Your-Inbox_Outlook-iPadOS_Supplemental-Assets_v1.0.zip
```

## Step-by-step setup

1. From the repository root, install dependencies when network access is available:

   ```bash
   python3 -m pip install -r build/requirements.txt
   ```

2. Run the conflict-safe local builder:

   ```bash
   python3 build/build_supplemental_assets_real.py
   ```

3. Review validation results:

   ```bash
   cat build/output/supplemental-assets/04-validation-reports/validation-results.csv
   ```

4. Review publication blockers:

   ```bash
   cat build/output/supplemental-assets/04-validation-reports/publication-blockers.md
   ```

## Common Gotchas

- Binary DOCX, XLSX, PDF, ZIP, and MP4 files are generated locally and ignored by Git.
- Do not fabricate MP4 recordings. Record videos only from a managed company iPad with dummy content.
- Do not fabricate SharePoint links, Microsoft Forms deployment results, support links, screenshots, shortcuts, logos, or approvals.
- If `python-docx` or `openpyxl` cannot be installed, the builder still creates local OOXML files with its fallback writer and records dependency warnings in validation results.
