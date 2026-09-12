# -*- coding: utf-8 -*-
import os, io

def fix_file(filepath):
    with io.open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        c = f.read()
    
    orig = c
    c = c.replace(u'C\u01f8dula', u'Cédula')
    c = c.replace(u'C\ufffddula', u'Cédula')
    c = c.replace(u'CÃ©dula', u'Cédula')
    
    c = c.replace(u'Evaluaci\u01ebn', u'Evaluación')
    c = c.replace(u'Evaluaci\ufffdn', u'Evaluación')
    c = c.replace(u'EvaluaciÃ³n', u'Evaluación')
    
    c = c.replace(u'Cl\u01ednica', u'Clínica')
    c = c.replace(u'Cl\ufffdnica', u'Clínica')
    c = c.replace(u'ClÃnica', u'Clínica')
    
    c = c.replace(u'\u019altima', u'Última')
    c = c.replace(u'\ufffdltima', u'Última')
    c = c.replace(u'Ã\x9altima', u'Última')
    c = c.replace(u'Ãšltima', u'Última')
    
    c = c.replace(u'Â°C', u'°C')
    c = c.replace(u'\ufffdC', u'°C')
    
    c = c.replace(u'Antropom\u01e9trica', u'Antropométrica')
    c = c.replace(u'Antropom\ufffdtrica', u'Antropométrica')
    c = c.replace(u'AntropomÃ©trica', u'Antropométrica')
    
    c = c.replace(u'Observaci\u01ebn', u'Observación')
    c = c.replace(u'Observaci\ufffdn', u'Observación')
    c = c.replace(u'ObservaciÃ³n', u'Observación')
    
    c = c.replace(u'a\u01b1os', u'años')
    c = c.replace(u'a\ufffdos', u'años')
    c = c.replace(u'aÃ±os', u'años')
    
    c = c.replace(u'\u012bgica', u'lógica')
    c = c.replace(u'L\u012bgica', u'Lógica')
    
    c = c.replace(u'Contrase\u01b1a', u'Contraseña')
    c = c.replace(u'Contrase\ufffda', u'Contraseña')
    c = c.replace(u'ContraseÃ±a', u'Contraseña')
    
    c = c.replace(u'M\u01e9dico', u'Médico')
    c = c.replace(u'M\ufffddico', u'Médico')
    c = c.replace(u'MÃ©dico', u'Médico')
    
    c = c.replace(u'\u01f8xito', u'éxito')
    c = c.replace(u'\ufffdxito', u'éxito')
    
    c = c.replace(u'Acci\u01ebn', u'Acción')
    c = c.replace(u'acci\u01ebn', u'acción')
    
    c = c.replace(u'Direcci\u01ebn', u'Dirección')
    c = c.replace(u'direcci\u01ebn', u'dirección')
    
    c = c.replace(u'C\u01ebdigo', u'Código')
    c = c.replace(u'c\u01ebdigo', u'código')

    if c != orig:
        with io.open(filepath, 'w', encoding='utf-8') as f:
            f.write(c)
        print("Fixed words in " + filepath)

for root, dirs, files in os.walk('src/main/webapp'):
    for file in files:
        if file.endswith('.jsp'):
            fix_file(os.path.join(root, file))

