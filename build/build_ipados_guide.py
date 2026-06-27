#!/usr/bin/env python3
from __future__ import annotations
import sys, csv, re, datetime, shutil, subprocess, html, zipfile
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parent))
from src.source_loader import discover, git
from src.copy_parser import parse_pages
from src.utilities import rel, strip_md
OUT='Take-Control-of-Your-Inbox_Outlook-on-iPadOS'

def p_xml(text, style=None, break_page=False):
    props=''
    if style: props+=f'<w:pStyle w:val="{style}"/>'
    if break_page: props+='<w:pageBreakBefore/>'
    return f'<w:p><w:pPr>{props}</w:pPr><w:r><w:t xml:space="preserve">{html.escape(text)}</w:t></w:r></w:p>'

def field_p(instr, style=None):
    props=f'<w:pPr><w:pStyle w:val="{style}"/></w:pPr>' if style else ''
    return f'<w:p>{props}<w:fldSimple w:instr="{html.escape(instr)}"><w:r><w:t>Update field in Word</w:t></w:r></w:fldSimple></w:p>'

def md_to_xml(block, first=False):
    out=[]
    for raw in block.splitlines():
        line=raw.strip()
        if not line: continue
        m=re.match(r'^(#{1,6})\s+(.*)',line)
        if m:
            txt=strip_md(m.group(2)); st='Heading2' if re.match(r'Page \d+',txt) else ('Heading1' if len(m.group(1))<=2 else 'Heading3')
            out.append(p_xml(txt,st, False))
        elif re.match(r'^[-*]\s+',line): out.append(p_xml('• '+strip_md(re.sub(r'^[-*]\s+','',line)),'ListParagraph'))
        elif re.match(r'^\d+[.)]\s+',line): out.append(p_xml(strip_md(line),'ListParagraph'))
        elif '|' in line and line.startswith('|'): out.append(p_xml(strip_md(line.replace('|','  |  ')),'TableText'))
        elif re.search(r'(Screenshot|visual|image) needed|Suggested visual|Design notes', line, re.I):
            out.append(p_xml('Screenshot needed / production note: '+strip_md(line)+' Alt-text draft: To be finalized during screenshot capture. Validation note: Use only approved repository screenshots.','Callout'))
        else: out.append(p_xml(strip_md(line),'Normal'))
    return ''.join(out)

def write_manual_docx(path, pages, logo_missing=True):
    paras=[]
    paras += [p_xml('Take Control of Your Inbox','Title'),p_xml('Outlook on iPadOS','Subtitle'),p_xml('Step-by-step email, follow-up, shared mailbox and Copilot guidance for sales teams','Normal')]
    if logo_missing: paras.append(p_xml('UNBRANDED-DRAFT STRUCTURAL PROOF: approved BCBSKS logo asset was not found in repository.','Callout'))
    paras.append(field_p('TOC \\o "1-2" \\h \\z \\u','Heading1'))
    for i,p in enumerate(pages):
        paras.append(p_xml('',break_page=True)); paras.append(md_to_xml(p['markdown']))
    body=''.join(paras)+'<w:sectPr><w:pgSz w:w="12240" w:h="15840"/><w:pgMar w:top="1008" w:right="1080" w:bottom="1008" w:left="1080" w:header="432" w:footer="432"/><w:headerReference w:type="default" r:id="rIdHeader1"/><w:footerReference w:type="default" r:id="rIdFooter1"/></w:sectPr>'
    document=f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?><w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"><w:body>{body}</w:body></w:document>'''
    styles='''<?xml version="1.0" encoding="UTF-8" standalone="yes"?><w:styles xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"><w:style w:type="paragraph" w:default="1" w:styleId="Normal"><w:name w:val="Normal"/><w:rPr><w:rFonts w:ascii="Aptos"/><w:sz w:val="21"/><w:color w:val="333333"/></w:rPr></w:style><w:style w:type="paragraph" w:styleId="Title"><w:name w:val="Title"/><w:rPr><w:b/><w:sz w:val="60"/><w:color w:val="002855"/></w:rPr></w:style><w:style w:type="paragraph" w:styleId="Subtitle"><w:name w:val="Subtitle"/><w:rPr><w:b/><w:sz w:val="36"/><w:color w:val="005EB8"/></w:rPr></w:style><w:style w:type="paragraph" w:styleId="Heading1"><w:name w:val="heading 1"/><w:basedOn w:val="Normal"/><w:qFormat/><w:rPr><w:b/><w:sz w:val="42"/><w:color w:val="002855"/></w:rPr></w:style><w:style w:type="paragraph" w:styleId="Heading2"><w:name w:val="heading 2"/><w:basedOn w:val="Normal"/><w:qFormat/><w:rPr><w:b/><w:sz w:val="32"/><w:color w:val="005EB8"/></w:rPr></w:style><w:style w:type="paragraph" w:styleId="Heading3"><w:name w:val="heading 3"/><w:basedOn w:val="Normal"/><w:rPr><w:b/><w:sz w:val="25"/><w:color w:val="002855"/></w:rPr></w:style><w:style w:type="paragraph" w:styleId="ListParagraph"><w:name w:val="List Paragraph"/><w:basedOn w:val="Normal"/></w:style><w:style w:type="paragraph" w:styleId="Callout"><w:name w:val="Callout"/><w:basedOn w:val="Normal"/><w:rPr><w:b/><w:color w:val="002855"/></w:rPr></w:style><w:style w:type="paragraph" w:styleId="TableText"><w:name w:val="Table Text"/><w:basedOn w:val="Normal"/><w:rPr><w:sz w:val="19"/></w:rPr></w:style></w:styles>'''
    header='<?xml version="1.0" encoding="UTF-8" standalone="yes"?><w:hdr xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"><w:p><w:r><w:t>Take Control of Your Inbox | Outlook on iPadOS</w:t></w:r></w:p></w:hdr>'
    footer='<?xml version="1.0" encoding="UTF-8" standalone="yes"?><w:ftr xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"><w:p><w:r><w:t>Take Control of Your Inbox | Outlook on iPadOS | Page </w:t></w:r><w:fldSimple w:instr="PAGE"><w:r><w:t>1</w:t></w:r></w:fldSimple></w:p></w:ftr>'
    rels='''<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"><Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/><Relationship Id="rId2" Type="http://schemas.openxmlformats.org/package/2006/relationships/metadata/core-properties" Target="docProps/core.xml"/><Relationship Id="rId3" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/extended-properties" Target="docProps/app.xml"/></Relationships>'''
    drels='''<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"><Relationship Id="rIdHeader1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/header" Target="header1.xml"/><Relationship Id="rIdFooter1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/footer" Target="footer1.xml"/><Relationship Id="rIdStyles" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/></Relationships>'''
    types='''<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types"><Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/><Default Extension="xml" ContentType="application/xml"/><Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/><Override PartName="/word/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"/><Override PartName="/word/header1.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.header+xml"/><Override PartName="/word/footer1.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.footer+xml"/><Override PartName="/docProps/core.xml" ContentType="application/vnd.openxmlformats-package.core-properties+xml"/><Override PartName="/docProps/app.xml" ContentType="application/vnd.openxmlformats-officedocument.extended-properties+xml"/></Types>'''
    core='<?xml version="1.0" encoding="UTF-8" standalone="yes"?><cp:coreProperties xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dcterms="http://purl.org/dc/terms/"><dc:title>Take Control of Your Inbox: Outlook on iPadOS</dc:title><dc:subject>Outlook on iPadOS email and follow-up performance support</dc:subject><dc:creator>IT Training &amp; Enablement</dc:creator><cp:keywords>Outlook, iPadOS, iPad, email, follow-up, shared mailbox, Copilot, sales, Microsoft 365</cp:keywords><dc:description>Use the approved SharePoint description from the production plan; final metadata review required.</dc:description></cp:coreProperties>'
    app='<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Properties xmlns="http://schemas.openxmlformats.org/officeDocument/2006/extended-properties"><Application>Codex OOXML builder</Application></Properties>'
    with zipfile.ZipFile(path,'w',zipfile.ZIP_DEFLATED) as z:
        for n,c in {'[Content_Types].xml':types,'_rels/.rels':rels,'word/_rels/document.xml.rels':drels,'word/document.xml':document,'word/styles.xml':styles,'word/header1.xml':header,'word/footer1.xml':footer,'docProps/core.xml':core,'docProps/app.xml':app}.items(): z.writestr(n,c)

def validate_docx(path):
    checks=[]
    try:
        with zipfile.ZipFile(path) as z:
            names=set(z.namelist()); xml=z.read('word/document.xml').decode('utf-8','ignore')
            for req in ['word/document.xml','docProps/core.xml','word/styles.xml','word/header1.xml','word/footer1.xml']: checks.append(('pass' if req in names else 'fail',f'{req} exists'))
            checks.append(('pass' if 'TOC' in xml else 'fail','TOC field exists')); checks.append(('pass' if 'PAGE' in z.read('word/footer1.xml').decode('utf-8','ignore') else 'fail','Page number field exists'))
    except Exception as e: checks.append(('fail',f'DOCX ZIP validation failed: {e}'))
    try:
        from docx import Document
        Document(path); checks.append(('pass','DOCX opens with python-docx'))
    except Exception as e: checks.append(('warn',f'python-docx open check unavailable/failed: {e}'))
    return checks

def main():
    root=Path(__file__).resolve().parents[1]; out=root/'build/output'; out.mkdir(parents=True,exist_ok=True)
    found, imgs, logo, media_refs, inv=discover(root)
    missing=[n for n,p in found.items() if not p]
    inv_path=out/f'{OUT}_Source-Inventory_v1.0.csv'
    with inv_path.open('w',newline='',encoding='utf-8') as f: w=csv.DictWriter(f,fieldnames=['path','file_type','purpose','required','found','size','sha256','used_as']); w.writeheader(); w.writerows(inv)
    if missing:
        (out/'BUILD_BLOCKED.md').write_text('# Build blocked\n\n'+('\n'.join(f'- {m}' for m in missing)),encoding='utf-8'); return 2
    repo=git(['config','--get','remote.origin.url'],root); branch=git(['branch','--show-current'],root); sha=git(['rev-parse','HEAD'],root); status=git(['status','--short'],root); now=datetime.datetime.now(datetime.UTC).isoformat().replace('+00:00','Z')
    copy_paths=[found[f'{i:02d}. Complete copy deck — Part {i-3}.md'] for i in range(4,10)]; pages, perr=parse_pages(copy_paths)
    docx=out/f'{OUT}_Guide_v1.0.docx'; write_manual_docx(docx,pages,logo_missing=not bool(logo))
    checks=[('pass','All required source files were found'),('pass' if len(pages)==125 and not perr else 'fail','Pages 1-125 were found exactly once and in order')]+validate_docx(docx)
    if not logo: checks.append(('fail','Approved BCBSKS logo asset not found; DOCX is unbranded structural proof'))
    ph_re=re.compile(r'\[[^\]]+\]|Screenshot needed|availability may vary|Insert ',re.I); rows=[]
    for p in pages:
        for m in ph_re.finditer(p['markdown']): rows.append((m.group(0),f"Page {p['number']}",rel(Path(p['source']),root),'screenshot' if 'Screenshot' in m.group(0) else 'other','review','Source owner to provide approved value or screenshot.'))
    if not logo: rows.append(('Approved BCBSKS primary logo asset not found','Brand assets','BCBSKS_Master_Brand_Kit.md','logo','yes','Add approved logo file to repository and reference it from brand kit.'))
    (out/f'{OUT}_Unresolved-Placeholders_v1.0.md').write_text('# Unresolved placeholders and missing assets\n\n| Placeholder | Page/section | Source | Type | Blocks publication | Recommended action |\n|---|---|---|---|---|---|\n'+'\n'.join('| '+' | '.join(str(x).replace('|','/') for x in r)+' |' for r in rows),encoding='utf-8')
    (out/f'{OUT}_Validation-Checklist_v1.0.md').write_text('# Validation checklist\n\n'+'\n'.join(f"- [{'x' if s=='pass' else ' '}] {m} ({s})" for s,m in checks)+'\n\nDesktop Word/human review required for fields, accessibility, screenshots, and publication approval.\n',encoding='utf-8')
    rendered='Not available'; pdf_note='Rendering unavailable; LibreOffice not found.'
    report=out/f'{OUT}_Build-Report_v1.0.md'
    report.write_text(f'''# Build report\n\n- Repository URL: {repo}\n- Active branch: {branch}\n- Commit SHA: {sha}\n- Working-tree status before/at build: `{status or 'clean'}`\n- Build date/time: {now}\n- Mapped pages: {len(pages)}\n- Rendered page count: {rendered}\n- Brand status: {'Branded with '+rel(logo,root) if logo else 'UNBRANDED-DRAFT structural proof; approved BCBSKS logo asset not found.'}\n\n## Required source inventory\nSee `{inv_path.relative_to(root)}`.\n\n## Media references\n{len(media_refs)} Markdown/HTML image references found. Missing or ambiguous: {sum(1 for r in media_refs if r['status']!='resolved')}.\n\n## Page parse\n{'; '.join(perr) if perr else 'Pages 1-125 parsed exactly once in order.'}\n\n## Validation\n'''+ '\n'.join(f'- {s.upper()}: {m}' for s,m in checks)+f'''\n\n## Render validation\n{pdf_note}\n\n## Page overflow\nWord pagination must be updated and checked in desktop Word after fields are refreshed. No approved copy was intentionally removed or shrunk below configured style minimums.\n''',encoding='utf-8')
    print(docx)
    return 0
if __name__=='__main__': raise SystemExit(main())
