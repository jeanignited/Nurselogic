import os, io
for root, dirs, files in os.walk('src/main/webapp'):
    for file in files:
        if file.endswith('.jsp'):
            with io.open(os.path.join(root, file), 'rb') as f:
                c = f.read()
                if b'\xc3\x83' in c:
                    print(f"Double encoded found in: {file}")
