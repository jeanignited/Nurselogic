import io

with io.open('src/main/webapp/views/agenda.jsp', 'r', encoding='windows-1252') as f:
    c = f.read()

c = c.replace("class='badge badge-especialidad px-3 py-1'", "class='badge text-body px-3 py-1'")

with io.open('src/main/webapp/views/agenda.jsp', 'w', encoding='windows-1252') as f:
    f.write(c)
