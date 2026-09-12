import io, re

with io.open('src/main/webapp/includes/modals.jsp', 'r', encoding='utf-8', errors='ignore') as f:
    c = f.read()

c = re.sub(r'Art\Wculos', 'Artículos', c)

with io.open('src/main/webapp/includes/modals.jsp', 'w', encoding='utf-8') as f:
    f.write(c)

print("Fixed Articulos")
