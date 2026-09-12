# -*- coding: utf-8 -*-
import os, io

def fix_file(filepath):
    with io.open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        c = f.read()
    
    orig = c
    c = c.replace(u'C\u01f8dula', u'C\xe9dula')
    c = c.replace(u'C\ufffddula', u'C\xe9dula')
    c = c.replace(u'C\xc3\xa9dula', u'C\xe9dula') # é
    
    c = c.replace(u'Evaluaci\u01ebn', u'Evaluaci\xf3n')
    c = c.replace(u'Evaluaci\ufffdn', u'Evaluaci\xf3n')
    c = c.replace(u'Evaluaci\xc3\xb3n', u'Evaluaci\xf3n') # ó
    
    c = c.replace(u'Cl\u01ednica', u'Cl\xednica')
    c = c.replace(u'Cl\ufffdnica', u'Cl\xednica')
    c = c.replace(u'Cl\xc3\xadnica', u'Cl\xednica') # í
    
    c = c.replace(u'\u019altima', u'\xdaltima')
    c = c.replace(u'\ufffdltima', u'\xdaltima')
    c = c.replace(u'\xc3\x9altima', u'\xdaltima') # Ú
    
    c = c.replace(u'\xc3\x82\xc2\xb0C', u'\xb0C') # °C
    c = c.replace(u'\ufffdC', u'\xb0C')
    
    c = c.replace(u'Antropom\u01e9trica', u'Antropom\xe9trica')
    c = c.replace(u'Antropom\ufffdtrica', u'Antropom\xe9trica')
    c = c.replace(u'Antropom\xc3\xa9trica', u'Antropom\xe9trica')
    
    c = c.replace(u'Observaci\u01ebn', u'Observaci\xf3n')
    c = c.replace(u'Observaci\ufffdn', u'Observaci\xf3n')
    c = c.replace(u'Observaci\xc3\xb3n', u'Observaci\xf3n')
    
    c = c.replace(u'a\u01b1os', u'a\xf1os')
    c = c.replace(u'a\ufffdos', u'a\xf1os')
    c = c.replace(u'a\xc3\xb1os', u'a\xf1os') # ñ
    
    c = c.replace(u'\u012bgica', u'l\xf3gica')
    c = c.replace(u'L\u012bgica', u'L\xf3gica')
    
    c = c.replace(u'Contrase\u01b1a', u'Contrase\xf1a')
    c = c.replace(u'Contrase\ufffda', u'Contrase\xf1a')
    c = c.replace(u'Contrase\xc3\xb1a', u'Contrase\xf1a')
    
    c = c.replace(u'M\u01e9dico', u'M\xe9dico')
    c = c.replace(u'M\ufffddico', u'M\xe9dico')
    c = c.replace(u'M\xc3\xa9dico', u'M\xe9dico')
    
    c = c.replace(u'\u01f8xito', u'\xe9xito')
    c = c.replace(u'\ufffdxito', u'\xe9xito')
    
    c = c.replace(u'Acci\u01ebn', u'Acci\xf3n')
    c = c.replace(u'acci\u01ebn', u'acci\xf3n')
    
    c = c.replace(u'Direcci\u01ebn', u'Direcci\xf3n')
    c = c.replace(u'direcci\u01ebn', u'direcci\xf3n')
    
    c = c.replace(u'C\u01ebdigo', u'C\xf3digo')
    c = c.replace(u'c\u01ebdigo', u'c\xf3digo')

    if c != orig:
        with io.open(filepath, 'w', encoding='utf-8') as f:
            f.write(c)
        print("Fixed words in " + filepath)

for root, dirs, files in os.walk('src/main/webapp'):
    for file in files:
        if file.endswith('.jsp'):
            fix_file(os.path.join(root, file))

