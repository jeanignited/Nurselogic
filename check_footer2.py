import io

with io.open('src/main/webapp/includes/modals.jsp', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'id="modalVerDiagnostico"' in line:
        for j in range(i, len(lines)):
            if 'modal-footer' in lines[j]:
                for k in range(j-2, min(len(lines), j+8)):
                    print(f"{k+1}: {lines[k].strip()}")
                break
        break
