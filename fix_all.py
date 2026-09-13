# -*- coding: utf-8 -*-
import io, re

for fname in ['src/main/webapp/includes/modals.jsp', 'src/main/webapp/includes/scripts.jsp']:
    with io.open(fname, 'r', encoding='utf-8') as f:
        c = f.read()

    # Reemplazar escapes literales de \x por sus caracteres reales en UTF-8
    c = c.replace('\\xf3', '\u00F3') # ó
    c = c.replace('\\xe1', '\u00E1') # á
    c = c.replace('\\xe9', '\u00E9') # é
    c = c.replace('\\xed', '\u00ED') # í
    c = c.replace('\\xfa', '\u00FA') # ú
    c = c.replace('\\xf1', '\u00F1') # ñ
    c = c.replace('\\xd3', '\u00D3') # Ó
    c = c.replace('\\xbf', '\u00BF') # ¿
    c = c.replace('\\xa1', '\u00A1') # ¡
    
    with io.open(fname, 'w', encoding='utf-8') as f:
        f.write(c)

print("Fixed JSP syntax in all files")
