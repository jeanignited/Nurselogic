import io

def fix_double_encoding(filepath):
    with io.open(filepath, 'rb') as f:
        c = f.read()
    
    if b'\xc3\x83' in c:
        print(f"Fixing {filepath}")
        # decode as utf-8, then encode as latin-1, then it's proper utf-8!
        text = c.decode('utf-8')
        raw_bytes = text.encode('windows-1252')
        # write it back
        with io.open(filepath, 'wb') as f:
            f.write(raw_bytes)

import os
for root, dirs, files in os.walk('src/main/webapp'):
    for file in files:
        if file.endswith('.jsp'):
            fix_double_encoding(os.path.join(root, file))

