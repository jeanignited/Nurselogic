import io

with io.open('src/main/webapp/includes/scripts.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

c = c.replace('formData.append("id", id);', 'formData.append("idEnf", id);\n                    formData.append("idAle", id);')

with io.open('src/main/webapp/includes/scripts.jsp', 'w', encoding='utf-8') as f:
    f.write(c)

print("Fixed borrarCatalogo param name")
