from __future__ import annotations
import re, csv, datetime, subprocess
from pathlib import Path
from .utilities import norm_name, sha256, rel

REQUIRED=[
'01. Locked scope for the guide.md','02. Detailed build plan.md','03. Page-by-page copy plan.md','04. Complete copy deck — Part 1.md','05. Complete copy deck — Part 2.md','06. Complete copy deck — Part 3.md','07. Complete copy deck — Part 4.md','08. Complete copy deck — Part 5.md','09. Complete copy deck — Part 6.md','10. Screenshot capture and annotation plan.md','11. Platform-difference and master-guide integration map.md','12. Word production and publishing plan.md','13. Supplemental support package.md','BCBSKS_Master_Brand_Kit.md','BCBSKS-ID-Prompt-Guide-v4.0.md']
IMG_EXT={'.png','.jpg','.jpeg','.gif','.svg','.bmp','.tif','.tiff'}

def git(cmd, root):
    try: return subprocess.check_output(['git']+cmd,cwd=root,text=True,stderr=subprocess.STDOUT).strip()
    except Exception as e: return f'UNAVAILABLE: {e}'

def discover(root:Path):
    files=[p for p in root.rglob('*') if p.is_file() and '.git' not in p.parts and '__pycache__' not in p.parts and p.suffix != '.pyc' and not (len(p.relative_to(root).parts) >= 2 and p.relative_to(root).parts[0] == 'build' and p.relative_to(root).parts[1] == 'output')]
    by={norm_name(p.name):p for p in files}
    found={name:by.get(norm_name(name)) for name in REQUIRED}
    image_files=[p for p in files if p.suffix.lower() in IMG_EXT]
    logo=None
    brand=found.get('BCBSKS_Master_Brand_Kit.md')
    if brand:
        txt=brand.read_text('utf-8',errors='ignore')
        for p in image_files:
            if 'logo' in p.name.casefold() or p.name in txt:
                logo=p; break
    media_refs=[]
    pat=re.compile(r'!\[[^\]]*\]\(([^)]+)\)|<img[^>]+src=["\']([^"\']+)',re.I)
    basename={p.name.casefold():[] for p in files}
    for p in files: basename.setdefault(p.name.casefold(),[]).append(p)
    for md in [p for p in files if p.suffix.lower()=='.md']:
        txt=md.read_text('utf-8',errors='ignore')
        for m in pat.finditer(txt):
            orig=m.group(1) or m.group(2); base=Path(orig).name.casefold(); matches=basename.get(base,[])
            media_refs.append({'source':rel(md,root),'original':orig,'resolved':rel(matches[0],root) if len(matches)==1 else '', 'status':'resolved' if len(matches)==1 else 'missing-or-ambiguous'})
    inv=[]
    req_paths=set(p for p in found.values() if p)
    for p in sorted(files):
        purpose='required source' if p in req_paths else ('media asset' if p.suffix.lower() in IMG_EXT else 'repository file')
        inv.append({'path':rel(p,root),'file_type':p.suffix.lower() or 'none','purpose':purpose,'required':'yes' if p in req_paths else 'no','found':'yes','size':p.stat().st_size,'sha256':sha256(p),'used_as':purpose})
    return found, image_files, logo, media_refs, inv
