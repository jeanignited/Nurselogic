import os, re
for root, dirs, files in os.walk('src/main/webapp'):
    for file in files:
        if file.endswith('.jsp'):
            with open(os.path.join(root, file), 'r', encoding='utf-8', errors='ignore') as f:
                c = f.read()
            for i, line in enumerate(c.split('\n')):
                if 'confirm(' in line or 'alert(' in line:
                    print(f"{file}:{i+1}: {line.strip()}")
