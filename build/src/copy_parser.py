from __future__ import annotations
import re
from pathlib import Path
# Matches "Page 7" and mapped ranges such as "Pages 5–6".
PAGE_RE=re.compile(r'(?im)^\s*#{1,6}\s*Pages?\s+(\d+)(?:\s*[–—-]\s*(\d+))?\b(?![^\n]*:)[^\n]*$')
def parse_pages(paths):
    pages=[]; seen={}; errors=[]
    for path in paths:
        txt=Path(path).read_text('utf-8',errors='ignore')
        ms=list(PAGE_RE.finditer(txt))
        if not txt.strip(): errors.append(f'Empty copy deck: {path}')
        for i,m in enumerate(ms):
            start=m.start(); end=ms[i+1].start() if i+1<len(ms) else len(txt)
            block=txt[start:end].strip()
            a=int(m.group(1)); b=int(m.group(2) or a)
            for n in range(a,b+1):
                page_block=block if a==b else re.sub(r'(?im)^\s*#{1,6}\s*Pages?\s+\d+\s*[–—-]\s*\d+\b[^\n]*$', f'## Page {n} — continued mapped range {a}–{b}', block, count=1)
                if n in seen: errors.append(f'Duplicate Page {n}: {seen[n]} and {path}')
                seen[n]=str(path); pages.append({'number':n,'source':str(path),'markdown':page_block})
    missing=[n for n in range(1,126) if n not in seen]
    if missing: errors.append('Missing pages: '+', '.join(map(str,missing)))
    order=[p['number'] for p in pages]
    if order != list(range(1,126)): errors.append('Page order is not continuous 1-125')
    return pages, errors
