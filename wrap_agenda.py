import io

with io.open('src/main/webapp/views/agenda.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

old_start = '%>        <div id="agenda"'
new_start = '%>        <% if(!isPaciente) { %>\n        <div id="agenda"'

c = c.replace(old_start, new_start)

# append closing brace at the end
c = c.rstrip() + '\n        <% } %>\n'

with io.open('src/main/webapp/views/agenda.jsp', 'w', encoding='utf-8') as f:
    f.write(c)
print("Updated agenda.jsp")
