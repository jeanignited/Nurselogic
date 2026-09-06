import os
import glob

def fix_with_replace(path):
    with open(path, 'rb') as f:
        content = f.read()
    if content.startswith(b'\xef\xbb\xbf'):
        content = content[3:]
    text = content.decode('utf-8')
    
    # Replace U+FFFD with a question mark so it can be encoded
    text = text.replace('\ufffd', '?')
    
    original_bytes = text.encode('latin1', errors='replace')
    
    try:
        original_text = original_bytes.decode('utf-8')
    except Exception as e:
        # Fallback if still not valid utf-8
        original_text = original_bytes.decode('latin1')
        
    with open(path, 'w', encoding='utf-8') as f:
        f.write(original_text)
    print(f"Fixed {path} with replacements")

fix_with_replace('src/main/webapp/views/medicamentos.jsp')
fix_with_replace('src/main/webapp/includes/modals.jsp')
