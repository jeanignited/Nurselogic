# -*- coding: utf-8 -*-
import re
import glob

fixes = [
    (r'Creaci[^a-zA-Z0-9\s]+n', 'Creación'),
    (r'cat[^a-zA-Z0-9\s]+logos', 'catálogos'),
    (r't[^a-zA-Z0-9\s]+ mismo', 'tú mismo'),
    (r'Admisi[^a-zA-Z0-9\s]+n', 'Admisión'),
    (r'Descripci[^a-zA-Z0-9\s]+n', 'Descripción'),
    (r'Patolog[^a-zA-Z0-9\s]+as', 'Patologías'),
    (r'F&aacute;rmacol[^a-zA-Z0-9\s]+gico', 'Farmacológico'),
    (r'Traumatolog[^a-zA-Z0-9\s]+a', 'Traumatología'),
    (r'Patolog[^a-zA-Z0-9\s]+a', 'Patología'),
    (r'musculoesquel[^a-zA-Z0-9\s]+tico', 'musculoesquelético'),
    (r'Al[^a-zA-Z0-9\s]+rgeno', 'Alérgeno'),
    (r'Est[^a-zA-Z0-9\s]+ndar', 'Estándar'),
    (r'[^a-zA-Z0-9\s]+rea Hospitalaria', 'Área Hospitalaria'),
    (r'ELECTR[^a-zA-Z0-9\s]+NICA', 'ELECTRÓNICA'),
    (r'DESCRIPCI[^a-zA-Z0-9\s]+N', 'DESCRIPCIÓN'),
    (r'Cl[^a-zA-Z0-9\s]+nica', 'Clínica')
]

files = glob.glob('src/main/webapp/includes/modals.jsp')
for path in files:
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()
    
    for pattern, repl in fixes:
        text = re.sub(pattern, repl, text)
        
    with open(path, 'w', encoding='utf-8') as f:
        f.write(text)
