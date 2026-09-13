import os
for root, dirs, files in os.walk('src/main/webapp'):
    for f in files:
        if f.endswith('.jsp'):
            with open(os.path.join(root, f), 'r', encoding='utf-8', errors='ignore') as file:
                c = file.read()
                if 'verFichaClinica' in c:
                    print(f"Found in {f}")
