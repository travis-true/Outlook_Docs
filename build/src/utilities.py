from __future__ import annotations
import hashlib, unicodedata, re
from pathlib import Path

def norm_name(s:str)->str:
    return unicodedata.normalize('NFC', s).casefold().replace('—','-').replace('–','-')

def sha256(path:Path)->str:
    h=hashlib.sha256()
    with path.open('rb') as f:
        for b in iter(lambda:f.read(65536), b''): h.update(b)
    return h.hexdigest()

def rel(path:Path, root:Path)->str:
    return path.resolve().relative_to(root.resolve()).as_posix()

def strip_md(s:str)->str:
    s=re.sub(r'`([^`]+)`', r'\1', s)
    s=re.sub(r'\*\*([^*]+)\*\*', r'\1', s)
    s=re.sub(r'\*([^*]+)\*', r'\1', s)
    s=re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'\1 (\2)', s)
    return s.strip()
