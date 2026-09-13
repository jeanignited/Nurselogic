import io

with io.open('src/main/webapp/views/dashboard.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

start_str = '<!-- Contenedor de Datos Clinicos -->'
start_idx = c.find(start_str)

if start_idx != -1:
    print(c[start_idx+1000:start_idx+2500])
else:
    print("Block not found!")
