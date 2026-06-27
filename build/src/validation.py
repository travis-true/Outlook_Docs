from pathlib import Path
from zipfile import ZipFile
from docx import Document

def validate_docx(path):
    checks=[]
    try:
        Document(path); checks.append(('pass','DOCX opens with python-docx'))
    except Exception as e: checks.append(('fail',f'DOCX open failed: {e}'))
    try:
        with ZipFile(path) as z:
            names=set(z.namelist())
            for req in ['word/document.xml','docProps/core.xml','word/styles.xml']:
                checks.append(('pass' if req in names else 'fail', f'{req} exists'))
            xml=z.read('word/document.xml').decode('utf-8',errors='ignore')
            checks.append(('pass' if 'TOC' in xml else 'fail','TOC field exists'))
            checks.append(('pass' if 'PAGE' in xml or any('footer' in n for n in names) else 'fail','page-number/footer parts exist'))
    except Exception as e: checks.append(('fail',f'ZIP validation failed: {e}'))
    return checks
