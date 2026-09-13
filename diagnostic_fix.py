import io

with io.open('src/main/webapp/views/dashboard.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

# 1. Update vista-inicio inline styles
c = c.replace('<div id="vista-inicio" class="position-relative" style="z-index: 10;">', '<div id="vista-inicio" class="position-relative" style="z-index: 10; display: block !important; opacity: 1 !important; visibility: visible !important;">')

# 2. Comment out particles initialization
c = c.replace('document.addEventListener("DOMContentLoaded", initPacienteParticles);', '// document.addEventListener("DOMContentLoaded", initPacienteParticles);')

with io.open('src/main/webapp/views/dashboard.jsp', 'w', encoding='utf-8') as f:
    f.write(c)

print("Updated dashboard.jsp with diagnostic fixes")
