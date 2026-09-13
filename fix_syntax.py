import io

with io.open('src/main/webapp/includes/scripts.jsp', 'r', encoding='utf-8', errors='ignore') as f:
    c = f.read()

c = c.replace('};\n\n};\n\n// Inicializar estado del dropdown si es que existe', '};\n\n// Inicializar estado del dropdown si es que existe')

with io.open('src/main/webapp/includes/scripts.jsp', 'w', encoding='utf-8') as f:
    f.write(c)

print("Fixed syntax error")
