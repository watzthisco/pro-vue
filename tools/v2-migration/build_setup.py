#!/usr/bin/env python3
"""Build the Version 2.0 Setup-Instructions.docx from the v1.5 version."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import docx
from docxlib import replace_range, find_style_model
import labcontent as C

ROOT = '/home/user/pro-vue'
SRC = os.path.join(ROOT, 'presentation/Version 1.5/Setup-Instructions.docx')
DST = os.path.join(ROOT, 'presentation/Version 2.0/Setup-Instructions.docx')

doc = docx.Document(SRC)
models = {s: find_style_model(doc, s) for s in
          ['Normal', 'Heading 1', 'Heading 2', 'LabNL', 'LabNL Sub', 'LabNL Code',
           'List Paragraph']}

# The SETUP block was written for the lab manual and uses a Note style the
# standalone setup document does not define; fold those into LabNL Sub.
items = [(('LabNL Sub' if style == 'Note' else style), text)
         for style, text in C.SETUP]

replace_range(doc, 0, 29, items, models)
doc.save(DST)
print('wrote', DST, '-', len(doc.paragraphs), 'paragraphs')
