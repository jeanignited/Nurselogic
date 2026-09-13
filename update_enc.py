import io

with io.open('src/main/webapp/views/dashboard.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

c = c.replace("Receta M\u00E9dica", "Receta Medica")
c = c.replace("abrir\u00E1 en una nueva pesta\u00F1a", "abrira en una nueva pestana")
c = c.replace("Mdica", "Medica")
c = c.replace("abrir en una nueva pestaa", "abrira en una nueva pestana")

with io.open('src/main/webapp/views/dashboard.jsp', 'w', encoding='utf-8') as f:
    f.write(c)
print("Updated encoding safely")
