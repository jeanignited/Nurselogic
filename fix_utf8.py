import os
import glob

def reverse_double_utf8(path):
    with open(path, 'rb') as f:
        content = f.read()
    try:
        # Ignore BOM if present
        if content.startswith(b'\xef\xbb\xbf'):
            content = content[3:]
        text = content.decode('utf-8')
    except Exception as e:
        print(f"Skipping {path}: not valid utf-8")
        return
        
    try:
        # This reverses the Windows-1252 to UTF-8 corruption
        original_bytes = text.encode('cp1252')
    except Exception as e:
        print(f"Skipping {path}: not pure double-encoded cp1252")
        return
    
    try:
        original_text = original_bytes.decode('utf-8')
    except Exception as e:
        print(f"Skipping {path}: original wasn't valid utf-8")
        return
        
    with open(path, 'w', encoding='utf-8') as f:
        f.write(original_text)
    print(f"Fixed {path}")

files = glob.glob('src/main/webapp/views/*.jsp') + glob.glob('src/main/webapp/includes/*.jsp')
for f in files:
    reverse_double_utf8(f)
