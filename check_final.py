import io
with io.open('src/main/webapp/views/dashboard.jsp', 'r', encoding='utf-8') as f:
    for line in f:
        if 'simularAperturaDocumento' in line or 'alert(' in line:
            print(line.strip())
