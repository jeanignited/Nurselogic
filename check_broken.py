import os, io, re

for root, dirs, files in os.walk('src/main/webapp'):
    for file in files:
        if file.endswith('.jsp'):
            filepath = os.path.join(root, file)
            with io.open(filepath, 'r', encoding='windows-1252', errors='ignore') as f:
                content = f.read()
            if '% autocomplete="off">' in content:
                print(f"BROKEN: {filepath}")
