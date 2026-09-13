import io
with io.open('src/main/webapp/includes/modals.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

c = c.replace('<option value="Moderada">Moderada</option>', '<option value="Medio">Medio</option>')
c = c.replace('<option value="Severa">Severa</option>', '<option value="Alto">Alto</option>')

with io.open('src/main/webapp/includes/modals.jsp', 'w', encoding='utf-8') as f:
    f.write(c)

print("Fixed dropdown options")
