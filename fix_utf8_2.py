import os
import glob

def reverse_double_utf8(path):
    with open(path, 'rb') as f:
        content = f.read()
    try:
        if content.startswith(b'\xef\xbb\xbf'):
            content = content[3:]
        text = content.decode('utf-8')
    except Exception as e:
        return
        
    try:
        # Use latin1 instead of cp1252 to avoid Undefined mapping errors
        original_bytes = text.encode('latin1')
    except Exception as e:
        print(f"Skipping {path}: not pure double-encoded latin1")
        return
    
    try:
        original_text = original_bytes.decode('utf-8')
    except Exception as e:
        print(f"Skipping {path}: original wasn't valid utf-8")
        return
        
    with open(path, 'w', encoding='utf-8') as f:
        f.write(original_text)
    print(f"Fixed {path}")

files = ['src/main/webapp/views/dashboard.jsp', 'src/main/webapp/views/medicamentos.jsp', 'src/main/webapp/includes/modals.jsp']
for f in files:
    reverse_double_utf8(f)
