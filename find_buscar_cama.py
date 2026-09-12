import os
for root, dirs, files in os.walk('src/main/webapp'):
    for f in files:
        if f.endswith('.jsp') or f.endswith('.js'):
            with open(os.path.join(root, f), 'r', encoding='utf-8', errors='ignore') as file:
                c = file.read()
                if 'buscarPacienteCama' in c:
                    print(f"Found in {f}")
