# -*- coding: utf-8 -*-
import re
import glob

fixes = {
    r'Cardiolog.*?a': 'Cardiología',
    r'Pediatr.*?a': 'Pediatría',
    r'Ginecolog.*?a': 'Ginecología',
    r'Dermatolog.*?a': 'Dermatología',
    r'Gastroenterolog.*?a': 'Gastroenterología',
    r'Neurolog.*?a': 'Neurología',
    r'Odontolog.*?a': 'Odontología',
    r'Diagn.*?stico': 'Diagnóstico',
    r'Informaci.*?n': 'Información',
    r'Gesti.*?n': 'Gestión',
    r'Acci.*?n': 'Acción',
    r'F.*?rmula': 'Fórmula'
}

files = glob.glob('src/main/webapp/views/*.jsp') + glob.glob('src/main/webapp/includes/*.jsp')
for path in files:
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()
    
    for k, v in fixes.items():
        text = re.sub(k, v, text)
        
    with open(path, 'w', encoding='utf-8') as f:
        f.write(text)
