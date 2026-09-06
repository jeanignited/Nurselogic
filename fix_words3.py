# -*- coding: utf-8 -*-
import re
import glob

fixes = [
    (r'n[^a-zA-Z0-9\s]+mero', 'número'),
    (r'N[^a-zA-Z0-9\s]+mero', 'Número'),
    (r'c[^a-zA-Z0-9\s]+dula', 'cédula'),
    (r'C[^a-zA-Z0-9\s]+dula', 'Cédula'),
    (r'm[^a-zA-Z0-9\s]+dic[oa]s?', lambda m: 'médic' + m.group(0)[-2:] if m.group(0).endswith('s') else 'médic' + m.group(0)[-1]),
    (r'M[^a-zA-Z0-9\s]+dic[oa]s?', lambda m: 'Médic' + m.group(0)[-2:] if m.group(0).endswith('s') else 'Médic' + m.group(0)[-1]),
    (r'd[^a-zA-Z0-9\s]+gitos', 'dígitos'),
    (r'R[^a-zA-Z0-9\s]+pido', 'Rápido'),
    (r'r[^a-zA-Z0-9\s]+pido', 'rápido'),
    (r'M[^a-zA-Z0-9\s]+dulo', 'Módulo'),
    (r'm[^a-zA-Z0-9\s]+dulo', 'módulo'),
    (r'f[^a-zA-Z0-9\s]+rmaco', 'fármaco'),
    (r'F[^a-zA-Z0-9\s]+rmaco', 'Fármaco'),
    (r'T[^a-zA-Z0-9\s]+cnico', 'Técnico'),
    (r't[^a-zA-Z0-9\s]+cnico', 'técnico'),
    (r'Estad[^a-zA-Z0-9\s]+sticas', 'Estadísticas'),
    (r'Anal[^a-zA-Z0-9\s]+tica', 'Analítica'),
    (r'Cl[^a-zA-Z0-9\s]+nicas?', lambda m: 'Clínica' + ('s' if m.group(0).endswith('s') else '')),
    (r'cl[^a-zA-Z0-9\s]+nicas?', lambda m: 'clínica' + ('s' if m.group(0).endswith('s') else '')),
    (r'din[^a-zA-Z0-9\s]+mico', 'dinámico'),
    (r'ocupaci[^a-zA-Z0-9\s]+n', 'ocupación'),
    (r'Gesti[^a-zA-Z0-9\s]+n', 'Gestión'),
    (r'Acci[^a-zA-Z0-9\s]+n', 'Acción'),
    (r'acci[^a-zA-Z0-9\s]+n', 'acción'),
    (r'Contrase[^a-zA-Z0-9\s]+a', 'Contraseña'),
    (r'A[^a-zA-Z0-9\s]+adir', 'Añadir'),
    (r'\bA[^a-zA-Z0-9\s]+o\b', 'Año'),
    (r'Pacientes Registrados', 'Pacientes Registrados'),
    (r'M[^a-zA-Z0-9\s]+s', 'Más'),
    (r'm[^a-zA-Z0-9\s]+s', 'más'),
    (r'd[^a-zA-Z0-9\s]+as', 'días'),
    (r'D[^a-zA-Z0-9\s]+as', 'Días'),
    (r'Atenci[^a-zA-Z0-9\s]+n', 'Atención'),
    (r'Evaluaci[^a-zA-Z0-9\s]+n', 'Evaluación'),
    (r'Presi[^a-zA-Z0-9\s]+n', 'Presión'),
    (r'Configuraci[^a-zA-Z0-9\s]+n', 'Configuración'),
    (r'Sesi[^a-zA-Z0-9\s]+n', 'Sesión'),
    (r'sesi[^a-zA-Z0-9\s]+n', 'sesión'),
    (r'Gr[^a-zA-Z0-9\s]+ficos?', lambda m: 'Gráfico' + ('s' if m.group(0).endswith('s') else '')),
    (r'gr[^a-zA-Z0-9\s]+ficos?', lambda m: 'gráfico' + ('s' if m.group(0).endswith('s') else '')),
    (r'D[^a-zA-Z0-9\s]+a', 'Día'),
    (r'd[^a-zA-Z0-9\s]+a', 'día'),
    (r'\b[^a-zA-Z0-9\s]ptimo\b', 'Óptimo'),
    (r'Cr[^a-zA-Z0-9\s]+tico', 'Crítico'),
    (r'cr[^a-zA-Z0-9\s]+tico', 'crítico'),
    (r'T[^a-zA-Z0-9\s]+rmica', 'Térmica'),
    (r't[^a-zA-Z0-9\s]+rmica', 'térmica'),
    (r'ox[^a-zA-Z0-9\s]+geno', 'oxígeno'),
    (r'Par[^a-zA-Z0-9\s]+metros', 'Parámetros'),
    (r'reducci[^a-zA-Z0-9\s]+n', 'reducción')
]

files = glob.glob('src/main/webapp/views/*.jsp') + glob.glob('src/main/webapp/includes/*.jsp')
for path in files:
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()
    
    for pattern, repl in fixes:
        text = re.sub(pattern, repl, text)
        
    with open(path, 'w', encoding='utf-8') as f:
        f.write(text)
