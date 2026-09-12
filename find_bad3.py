# -*- coding: utf-8 -*-
import io, os, re

patterns = [r'M\Wdico', r'Cl\Wnica', r'N\Wmero', r'Tel\Wfono', r'A\Wadir', r'A\Wo']
for root, dirs, files in os.walk('src/main/webapp'):
    for file in files:
        if file.endswith('.jsp'):
            with io.open(os.path.join(root, file), 'r', encoding='utf-8', errors='ignore') as f:
                c = f.read()
            for p in patterns:
                matches = re.findall(p, c)
                for m in matches:
                    if len(m.encode('utf-8')) <= len(m): # If it's ascii or broken, it will be 1 byte instead of 2 for utf-8
                        pass
                        # print("File " + file + " has " + repr(m))
