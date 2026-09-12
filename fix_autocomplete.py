import os, io, re

def process_file(filepath):
    with io.open(filepath, 'r', encoding='windows-1252', errors='ignore') as f:
        content = f.read()
    
    original = content
    # For <form ...>
    # We want to add autocomplete="off" if it doesn't exist
    content = re.sub(r'(<form\b(?![^>]*\bautocomplete=)[^>]*?)>', r'\1 autocomplete="off">', content, flags=re.IGNORECASE)
    
    # For <input ... type="text|password|email|number" ...>
    content = re.sub(r'(<input\b(?![^>]*\bautocomplete=)[^>]*?)>', r'\1 autocomplete="off">', content, flags=re.IGNORECASE)

    if content != original:
        with io.open(filepath, 'w', encoding='windows-1252') as f:
            f.write(content)
        print(f"Updated {filepath}")

for root, dirs, files in os.walk('src/main/webapp'):
    for file in files:
        if file.endswith('.jsp'):
            process_file(os.path.join(root, file))

print("Done.")
