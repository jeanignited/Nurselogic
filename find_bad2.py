# -*- coding: utf-8 -*-
import io, os, re

patterns = [r'M\Wdico', r'Cl\Wnica', r'N\Wmero', r'Tel\Wfono', r'A\Wadir', r'A\Wo', r'Men\W']
for root, dirs, files in os.walk('src/main/webapp'):
    for file in files:
        if file.endswith('.jsp'):
            with io.open(os.path.join(root, file), 'r', encoding='utf-8', errors='ignore') as f:
                c = f.read()
            for p in patterns:
                matches = re.findall(p, c)
                if matches:
                    bad = [m for m in matches if m not in ('Médico', 'Clínica', 'Número', 'Teléfono', 'Añadir', 'Año', 'Menú', 'Menos', 'M\xe9dico', 'Cl\xednica', 'N\xfamero', 'Tel\xe9fono', 'A\xf1adir', 'A\xf1o', 'Men\xfa')]
                    if bad:
                        print("File " + file + " has " + str(bad))
