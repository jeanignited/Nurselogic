import io

with io.open('src/main/webapp/views/dashboard.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

# First, remove my old diagnostic DOMContentLoaded that had typeof cambiarVista
c = c.replace('''document.addEventListener("DOMContentLoaded", function() {
    if(typeof cambiarVista === 'function') {
        cambiarVista('vista-inicio');
    }
    if(typeof switchPacienteTab === 'function') {
        switchPacienteTab('vista-inicio');
    }
});''', '')

# Remove the // from initPacienteParticles
c = c.replace('// document.addEventListener("DOMContentLoaded", initPacienteParticles);', 'document.addEventListener("DOMContentLoaded", initPacienteParticles);')

# Also, ensure dashboard_paciente doesn't get hidden by the global script.
# Actually, the user just says to inject their snippet. So let's do exactly that.
target = 'function switchPacienteTab(tabId) {'
injection = '''
document.addEventListener("DOMContentLoaded", function() {
    let dash = document.getElementById('dashboard_paciente');
    if (dash) {
        dash.classList.remove('d-none');
        dash.style.display = 'block';
        dash.style.opacity = '1';
    }
    let vistaInicioPaciente = document.getElementById('vista-inicio');
    if(vistaInicioPaciente) {
        vistaInicioPaciente.classList.remove('d-none');
        vistaInicioPaciente.style.display = 'block';
    }
});
'''

c = c.replace(target, injection + target)

with io.open('src/main/webapp/views/dashboard.jsp', 'w', encoding='utf-8') as f:
    f.write(c)

print("Updated dashboard.jsp with specific DOMContentLoaded")
