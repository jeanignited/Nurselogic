import io
with io.open('src/main/webapp/views/dashboard.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

c = c.replace('<div id="dashboard_paciente" class="vista-activa position-relative" style="z-index: 10;">', '<div id="dashboard_paciente" class="position-relative" style="z-index: 10;">')

with io.open('src/main/webapp/views/dashboard.jsp', 'w', encoding='utf-8') as f:
    f.write(c)
print("Removed vista-activa from dashboard_paciente to protect it")
