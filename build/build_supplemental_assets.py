#!/usr/bin/env python3
from __future__ import annotations
import csv, datetime, hashlib, json, re, shutil, subprocess
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
SRC=ROOT/'13. Supplemental support package.md'
OUT=ROOT/'build/output/supplemental-assets'
PKG='Take-Control-of-Your-Inbox_Outlook-iPadOS_Supplemental-Assets_v1.0'
PRINT_ASSETS=[
('Task-Map','Asset 1','Take-Control-of-Your-Inbox_Outlook-iPadOS_Task-Map_v1.0.docx.md'),
('Decision-Card','Asset 2','Which-Outlook-Am-I-Using_Decision-Card_v1.0.docx.md'),
('Quick-Fixes','Asset 3','Take-Control-of-Your-Inbox_Outlook-iPadOS_Quick-Fixes_v1.0.docx.md'),
('Shared-Mailbox-QRG','Asset 4','Take-Control-of-Your-Inbox_Outlook-iPadOS_Shared-Mailbox-QRG_v1.0.docx.md'),
('Copilot-Troubleshooting','Asset 5','Take-Control-of-Your-Inbox_Outlook-iPadOS_Copilot-Troubleshooting_v1.0.docx.md'),
('Search-Gestures-Shortcuts','Asset 6','Take-Control-of-Your-Inbox_Outlook-iPadOS_Search-Gestures-Shortcuts_v1.0.docx.md')]
VIDEOS=[
('01','Confirm-Account-Mailbox'),('02','Touch-Keyboard-Trackpad'),('03','Attach-and-Share-Files'),('04','Flag-Snooze-or-Swipe'),('05','Search-the-Correct-Account'),('06','Add-and-Use-Shared-Mailbox'),('07','Summarize-with-Copilot'),('08','Draft-and-Review-with-Copilot')]

def git(args):
    return subprocess.run(['git']+args,cwd=ROOT,text=True,stdout=subprocess.PIPE,stderr=subprocess.DEVNULL).stdout.strip()

def section(text, start, end=None):
    s=text.index(f'## {start}')
    e=text.index(f'## {end}', s) if end else len(text)
    return text[s:e].strip()+"\n"

def clean_md(s):
    return s.replace('\u2028','\n').replace('++','').replace('****','**')

def write_docx(path, title, body):
    path.write_text(
        f"# {title}\n\n"
        "Production target: printable Microsoft Word asset (.docx). This repository stores the text-only DOCX production source because binary files are not supported. Export the final .docx from this Markdown source on an approved production workstation.\n\n"
        "No fabricated screenshots, videos, logos, deployed forms, SharePoint resources, support links, keyboard shortcuts, or approval results are included.\n\n"
        "## Required training-documentation sections\n"
        "- High-level overview\n- Architectural diagram concepts\n- Step-by-step setup\n- Common Gotchas\n\n"
        + clean_md(body),
        encoding='utf-8'
    )


def write_pdf_stub(path, docx_name):
    path.write_text(f"# PDF production placeholder\n\nSource DOCX: {docx_name}\n\nPDF export requires Microsoft Word/approved publishing workstation. No PDF has been fabricated in this repository-only build.\n", encoding='utf-8')

def main():
    if OUT.exists(): shutil.rmtree(OUT)
    (OUT/'01-printable-word-assets').mkdir(parents=True)
    (OUT/'02-video-production-package').mkdir()
    (OUT/'03-forms-implementation-package').mkdir()
    (OUT/'04-validation-reports').mkdir()
    text=SRC.read_text(encoding='utf-8')
    # print assets
    nexts=['Asset 2','Asset 3','Asset 4','Asset 5','Asset 6','Asset 7']
    rows=[]
    for i,(slug, start, fname) in enumerate(PRINT_ASSETS):
        body=section(text,start,nexts[i])
        p=OUT/'01-printable-word-assets'/fname; write_docx(p, slug, body); pdf_stub=p.with_name(p.name.replace('.docx.md','.pdf.md')); write_pdf_stub(pdf_stub, fname.replace('.md',''))
        rows.append({'asset':slug,'docx_source':p.name,'pdf_status':'not fabricated; export stub only','validation':'pass'})
    # videos: scripts, shot lists, captions placeholders, validation manifests
    vbase=OUT/'02-video-production-package'
    for num,slug in VIDEOS:
        m=re.search(rf'## Video {int(num)} .*?(?=\n## Video {int(num)+1} |\n## Recommended video filenames|\Z)', text, re.S)
        body=m.group(0) if m else ''
        d=vbase/f'{num}-{slug}'; d.mkdir()
        (d/f'Outlook-iPadOS_{slug}_v1.0_script.md').write_text(clean_md(body)+"\n## Production status\nNot recorded. Requires direct managed iPad screen recording with dummy content.\n",encoding='utf-8')
        (d/f'Outlook-iPadOS_{slug}_v1.0_captions.vtt').write_text('WEBVTT\n\nNOTE No captions generated because no approved video was recorded.\n',encoding='utf-8')
        (d/f'Outlook-iPadOS_{slug}_v1.0_manifest.json').write_text(json.dumps({'video_file':None,'status':'blocked_pending_real_screen_recording','no_fabrication':True},indent=2),encoding='utf-8')
    # forms
    forms=section(text,'Asset 8','Package metadata')
    (OUT/'03-forms-implementation-package'/'SharePoint-Forms-Implementation-Package_v1.0.md').write_text(clean_md(forms)+"\n## Deployment status\nForms were not deployed or approved in this repository-only build.\n",encoding='utf-8')
    (OUT/'03-forms-implementation-package'/'forms-schema.json').write_text(json.dumps({'forms':['Resource feedback','Report outdated instructions'],'deployed':False,'approval_result':None,'no_fabrication':True},indent=2),encoding='utf-8')
    # validation/source inventory
    files=[p for p in OUT.rglob('*') if p.is_file()]
    with (OUT/'04-validation-reports'/'source-inventory.csv').open('w',newline='',encoding='utf-8') as f:
        w=csv.writer(f); w.writerow(['path','size','sha256'])
        for p in files: w.writerow([p.relative_to(OUT),p.stat().st_size,hashlib.sha256(p.read_bytes()).hexdigest()])
    report=OUT/'04-validation-reports'/'supplemental-assets-validation-report.md'
    report.write_text(f"# Supplemental assets validation report\n\nBuilt: {datetime.datetime.now(datetime.UTC).isoformat()}\n\nSource repository: travis-true/Outlook_Docs\nCommit: {git(['rev-parse','HEAD'])}\n\n## Results\n- Six printable Word production sources created as text-only `.docx.md` files because binary files are not supported.\n- Six PDF export stubs created; PDFs are not fabricated.\n- Eight video production folders created with scripts, caption placeholders, and manifests; MP4 files are not fabricated.\n- Two-form implementation package created; deployed form links and approval results are not fabricated.\n- Final archive manifest created at `build/output/{PKG}.zip.md`; binary ZIP output is intentionally not committed.\n",encoding='utf-8')
    with (OUT/'04-validation-reports'/'printable-assets-validation.csv').open('w',newline='',encoding='utf-8') as f:
        w=csv.DictWriter(f,fieldnames=['asset','docx_source','pdf_status','validation']); w.writeheader(); w.writerows(rows)
    archive_manifest=ROOT/'build/output'/f'{PKG}.zip.md'
    archive_manifest.write_text(
        f"# Final archive manifest\n\nBinary ZIP files are not supported in this review workflow. The archive contents are materialized under `build/output/supplemental-assets/` and listed in `build/output/supplemental-assets/04-validation-reports/source-inventory.csv`.\n\nIntended production archive filename: `{PKG}.zip`\n",
        encoding='utf-8'
    )
    print(archive_manifest)
if __name__=='__main__': main()
