import os, io

def fix_broken(filepath):
    with io.open(filepath, 'r', encoding='windows-1252', errors='ignore') as f:
        content = f.read()
    
    original = content
    content = content.replace('% autocomplete="off">"', '%>" autocomplete="off"')
    content = content.replace('% autocomplete="off">>', '%>>" autocomplete="off"')
    
    if content != original:
        with io.open(filepath, 'w', encoding='windows-1252') as f:
            f.write(content)
        print(f"Fixed {filepath}")

for root, dirs, files in os.walk('src/main/webapp'):
    for file in files:
        if file.endswith('.jsp'):
            fix_broken(os.path.join(root, file))
