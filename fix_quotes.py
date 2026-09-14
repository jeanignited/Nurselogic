import io

with io.open('src/main/webapp/views/dashboard.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

c = c.replace('calcularIMC(\\\'\\\')', "calcularIMC('')")
c = c.replace('calcularIMC(\\\'atender_\\\')', "calcularIMC('atender_')")

with io.open('src/main/webapp/views/dashboard.jsp', 'w', encoding='utf-8') as f:
    f.write(c)

with io.open('src/main/webapp/includes/modals.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

c = c.replace('calcularIMC(\\\'\\\')', "calcularIMC('')")
c = c.replace('calcularIMC(\\\'atender_\\\')', "calcularIMC('atender_')")

with io.open('src/main/webapp/includes/modals.jsp', 'w', encoding='utf-8') as f:
    f.write(c)
