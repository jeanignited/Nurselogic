import io
with io.open('src/main/webapp/views/medicamentos.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

bad_java = 'm.get(\\"id\\")'
good_java = 'm.get("id")'

c = c.replace(bad_java, good_java)

with io.open('src/main/webapp/views/medicamentos.jsp', 'w', encoding='utf-8') as f:
    f.write(c)
print("Fixed m.get id syntax")
