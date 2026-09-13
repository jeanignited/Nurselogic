import io
with io.open('src/main/webapp/includes/scripts.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

idx = c.find('borrarCatalogo')
print("borrarCatalogo at", idx)
