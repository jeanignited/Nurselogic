import os
for root, dirs, files in os.walk('src/main/java/com/nurselogic/controller'):
    for f in files:
        if f.endswith('.java'):
            with open(os.path.join(root, f), 'r', encoding='utf-8', errors='ignore') as file:
                c = file.read()
                if 'eliminarFactura' in c:
                    print(f"Found in {f}")
