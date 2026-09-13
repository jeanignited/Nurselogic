import io
with io.open('src/main/webapp/includes/scripts.jsp', 'r', encoding='utf-8') as f:
    c = f.read()
idx = c.find('function verFichaClinica')
if idx != -1:
    print(c[idx:idx+1500])
else:
    print("Not found")
