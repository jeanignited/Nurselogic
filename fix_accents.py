import os, io

replacements = {
    b'\xc3\x83\xc2\xa1': b'\xc3\xa1', # 
    b'\xc3\x83\xc2\xa9': b'\xc3\xa9', # 
    b'\xc3\x83\xc2\xad': b'\xc3\xad', # 
    b'\xc3\x83\xc2\xb3': b'\xc3\xb3', # 
    b'\xc3\x83\xc2\xba': b'\xc3\xba', # 
    b'\xc3\x83\xc2\xb1': b'\xc3\xb1', # 
    b'\xc3\x83\xc2\x81': b'\xc3\x81', # 
    b'\xc3\x83\xc2\x89': b'\xc3\x89', # 
    b'\xc3\x83\xc2\x8d': b'\xc3\x8d', # 
    b'\xc3\x83\xc2\x93': b'\xc3\x93', # 
    b'\xc3\x83\xc2\x9a': b'\xc3\x9a', # 
    b'\xc3\x83\xc2\x91': b'\xc3\x91', # 
    b'\xc3\x82\xc2\xb0': b'\xc2\xb0', # degree
    b'\xc3\x82\xc2\xbf': b'\xc2\xbf', # inverted question
}

def fix_file(filepath):
    with io.open(filepath, 'rb') as f:
        c = f.read()
    
    orig = c
    for bad, good in replacements.items():
        c = c.replace(bad, good)
        
    if c != orig:
        with io.open(filepath, 'wb') as f:
            f.write(c)
        print(f"Fixed {filepath}")

for root, dirs, files in os.walk('src/main/webapp'):
    for file in files:
        if file.endswith('.jsp'):
            fix_file(os.path.join(root, file))

