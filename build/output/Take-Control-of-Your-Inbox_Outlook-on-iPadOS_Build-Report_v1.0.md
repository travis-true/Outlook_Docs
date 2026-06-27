# Build report

- Repository URL: UNAVAILABLE: Command '['git', 'config', '--get', 'remote.origin.url']' returned non-zero exit status 1.
- Active branch: work
- Commit SHA: 34b25b85033fcda6fefd9ca120e502683d4bd42a
- Working-tree status before/at build: `binary-output cleanup changes in progress; repository clean after commit`
- Build date/time: 2026-06-27T13:46:49.715701Z
- Mapped pages: 125
- Rendered page count: Not available
- Brand status: UNBRANDED-DRAFT structural proof; approved BCBSKS logo asset not found.

## Required source inventory
See `build/output/Take-Control-of-Your-Inbox_Outlook-on-iPadOS_Source-Inventory_v1.0.csv`.

## Media references
3 Markdown/HTML image references found. Missing or ambiguous: 3.

## Page parse
Pages 1-125 parsed exactly once in order.

## Validation
- PASS: All required source files were found
- PASS: Pages 1-125 were found exactly once and in order
- PASS: word/document.xml exists
- PASS: docProps/core.xml exists
- PASS: word/styles.xml exists
- PASS: word/header1.xml exists
- PASS: word/footer1.xml exists
- PASS: TOC field exists
- PASS: Page number field exists
- WARN: python-docx open check unavailable/failed: No module named 'docx'
- FAIL: Approved BCBSKS logo asset not found; DOCX is unbranded structural proof

## Render validation
Rendering unavailable; LibreOffice not found.

## Page overflow
Word pagination must be updated and checked in desktop Word after fields are refreshed. No approved copy was intentionally removed or shrunk below configured style minimums.

## Version-control delivery note

The generated DOCX exists locally after running the build, but `build/output/*.docx` and `build/output/*.pdf` are ignored so PR creation does not fail on unsupported binary files. Re-run `python build/build_ipados_guide.py` to recreate the DOCX after checkout.
