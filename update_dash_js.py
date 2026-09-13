import io

with io.open('src/main/webapp/views/dashboard.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

# 1. Add id="contenedor-agendar"
c = c.replace('<div class="form-section mt-0 h-100 d-flex flex-column">', '<div id="contenedor-agendar" class="form-section mt-0 h-100 d-flex flex-column">')

# 2. Update the jumbotron button to use the new ID
c = c.replace("document.getElementById('formAgendar').scrollIntoView({behavior: 'smooth'})", "document.getElementById('contenedor-agendar').scrollIntoView({behavior: 'smooth'})")

# 3. Update switchPacienteTab function
old_func = '''function switchPacienteTab(tabId) {
                const vistas = ['vista-inicio', 'vista-citas', 'vista-resultados', 'vista-recetas'];
                vistas.forEach(v => {
                    const el = document.getElementById(v);
                    if (el) el.classList.add('d-none');
                });
                const seleccionada = document.getElementById(tabId);
                if (seleccionada) seleccionada.classList.remove('d-none');
            }'''

new_func = '''function switchPacienteTab(tabId, elementoClickeado) {
                const vistas = ['vista-inicio', 'vista-citas', 'vista-resultados', 'vista-recetas'];
                vistas.forEach(v => {
                    const el = document.getElementById(v);
                    if (el) el.classList.add('d-none');
                });
                const seleccionada = document.getElementById(tabId);
                if (seleccionada) seleccionada.classList.remove('d-none');

                if (elementoClickeado) {
                    const parent = elementoClickeado.closest('ul.nav');
                    if(parent) {
                        parent.querySelectorAll('.nav-link').forEach(link => link.classList.remove('active'));
                    } else {
                        document.querySelectorAll('.sidebar .nav-link').forEach(link => link.classList.remove('active'));
                    }
                    elementoClickeado.classList.add('active');
                }
            }'''

c = c.replace(old_func, new_func)

with io.open('src/main/webapp/views/dashboard.jsp', 'w', encoding='utf-8') as f:
    f.write(c)
print("Updated dashboard.jsp")
