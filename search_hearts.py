import os
for root, dirs, files in os.walk('.'):
    if '.git' in root or 'target' in root: continue
    for f in files:
        if f.endswith('.jsp') or f.endswith('.html') or f.endswith('.md'):
            try:
                with open(os.path.join(root, f), 'r', encoding='utf-8', errors='ignore') as file:
                    for line in file:
                        if 'bi-heart' in line:
                            print(f"{f}: {line.strip()}")
            except: pass
