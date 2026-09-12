import os, io

words = {
    'C\xc7\xb8dula': 'Cédula',
    'C\x8f\x81dula': 'Cédula',
    'C\xe3\xa9dula': 'Cédula',
    'C\xc3\x83\xc2\xa9dula': 'Cédula',
    'CÃ©dula': 'Cédula',
    'C\ufffddula': 'Cédula',
    
    'Evaluaci\xc3\x83\xc2\xb3n': 'Evaluación',
    'Evaluaci\xc7\xabn': 'Evaluación',
    'Evaluaci\ufffdn': 'Evaluación',
    'EvaluaciÃ³n': 'Evaluación',
    
    'Cl\xc3\x83\xc2\xadnica': 'Clínica',
    'Cl\xc7\xadnica': 'Clínica',
    'Cl\ufffdnica': 'Clínica',
    'ClÃ\xadnica': 'Clínica',
    
    '\xc3\x83\xc2\x9altima': 'Última',
    '\xc7\x9altima': 'Última',
    '\ufffdltima': 'Última',
    'Ã\x9altima': 'Última',
    
    '35 \xc3\x82\xc2\xb0C': '35 °C',
    '\xc3\x82\xc2\xb0C': '°C',
    'Â°C': '°C',
    '\ufffdC': '°C',
    
    'Antropom\xc3\x83\xc2\xa9trica': 'Antropométrica',
    'Antropom\xc7\xa9trica': 'Antropométrica',
    'Antropom\ufffdtrica': 'Antropométrica',
    'AntropomÃ©trica': 'Antropométrica',
    
    'Observaci\xc3\x83\xc2\xb3n': 'Observación',
    'ObservaciÃ³n': 'Observación',
    'Observaci\ufffdn': 'Observación',
    
    'ciruj\xc3\x83\xc2\xada': 'cirugía',
    'ciruj\ufffda': 'cirugía',
    
    'a\xc3\x83\xc2\xb1os': 'años',
    'a\xc7\xb1os': 'años',
    'a\ufffdos': 'años',
    
    '\xc3\x82\xc2\xbf': '¿',
    '\xc2\xbf': '¿',
    '\ufffd': 'í' # Risky, but lets just replace known bad substrings
}

def fix_file(filepath):
    with io.open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        c = f.read()
    
    orig = c
    c = c.replace('C\u01f8dula', 'Cédula')
    c = c.replace('C\ufffddula', 'Cédula')
    c = c.replace('CÃ©dula', 'Cédula')
    
    c = c.replace('Evaluaci\u01ebn', 'Evaluación')
    c = c.replace('Evaluaci\ufffdn', 'Evaluación')
    c = c.replace('EvaluaciÃ³n', 'Evaluación')
    
    c = c.replace('Cl\u01ednica', 'Clínica')
    c = c.replace('Cl\ufffdnica', 'Clínica')
    c = c.replace('ClÃnica', 'Clínica')
    
    c = c.replace('\u019altima', 'Última')
    c = c.replace('\ufffdltima', 'Última')
    c = c.replace('Ã\x9altima', 'Última')
    c = c.replace('Ãšltima', 'Última')
    
    c = c.replace('Â°C', '°C')
    c = c.replace('\ufffdC', '°C')
    
    c = c.replace('Antropom\u01e9trica', 'Antropométrica')
    c = c.replace('Antropom\ufffdtrica', 'Antropométrica')
    c = c.replace('AntropomÃ©trica', 'Antropométrica')
    
    c = c.replace('Observaci\u01ebn', 'Observación')
    c = c.replace('Observaci\ufffdn', 'Observación')
    c = c.replace('ObservaciÃ³n', 'Observación')
    
    c = c.replace('a\u01b1os', 'años')
    c = c.replace('a\ufffdos', 'años')
    c = c.replace('aÃ±os', 'años')
    
    c = c.replace('\u012bgica', 'lógica')
    c = c.replace('L\u012bgica', 'Lógica')
    
    c = c.replace('Contrase\u01b1a', 'Contraseña')
    c = c.replace('Contrase\ufffda', 'Contraseña')
    
    c = c.replace('M\u01e9dico', 'Médico')
    c = c.replace('M\ufffddico', 'Médico')
    
    c = c.replace('\u01f8xito', 'éxito')
    c = c.replace('\ufffdxito', 'éxito')
    
    c = c.replace('Acci\u01ebn', 'Acción')
    c = c.replace('acci\u01ebn', 'acción')
    
    c = c.replace('Direcci\u01ebn', 'Dirección')
    c = c.replace('direcci\u01ebn', 'dirección')
    
    c = c.replace('C\u01ebdigo', 'Código')
    c = c.replace('c\u01ebdigo', 'código')

    if c != orig:
        with io.open(filepath, 'w', encoding='utf-8') as f:
            f.write(c)
        print(f"Fixed words in {filepath}")

for root, dirs, files in os.walk('src/main/webapp'):
    for file in files:
        if file.endswith('.jsp'):
            fix_file(os.path.join(root, file))

