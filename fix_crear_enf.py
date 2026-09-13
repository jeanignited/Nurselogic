import io
with io.open('src/main/webapp/includes/modals.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

c = c.replace('name="id" id="catIdEnf"', 'name="idEnf" id="catIdEnf"')

with io.open('src/main/webapp/includes/modals.jsp', 'w', encoding='utf-8') as f:
    f.write(c)

print("Fixed modalCrearEnfermedad params")
