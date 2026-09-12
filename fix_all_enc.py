import os, io

for root, dirs, files in os.walk('src/main/webapp'):
    for file in files:
        if file.endswith('.jsp'):
            path = os.path.join(root, file)
            with io.open(path, 'r', encoding='utf-8', errors='ignore') as f:
                c = f.read()
            if 'pageEncoding="UTF-8"' not in c:
                c = '<%@ page pageEncoding="UTF-8" %>\n' + c
                with io.open(path, 'w', encoding='utf-8') as f:
                    f.write(c)
                print("Added to " + path)

