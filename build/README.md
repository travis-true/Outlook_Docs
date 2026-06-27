# Outlook on iPadOS guide build

Run from the repository root:

```bash
python build/build_ipados_guide.py
```

The build uses only repository-local Markdown and media assets. Generated deliverables are written to `build/output/`.

## Version-control note

The DOCX/PDF deliverables are generated locally in `build/output/` and are intentionally ignored by Git because the PR system does not support binary files. Re-run the build command after checkout to recreate them. The Markdown/CSV reports remain reviewable text artifacts.
