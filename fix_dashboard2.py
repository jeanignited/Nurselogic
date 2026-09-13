import io

with io.open('src/main/webapp/views/dashboard.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

# Remove the canvas from dashboard_paciente
old_canvas = '<canvas id="pacienteParticles" class="position-fixed w-100 h-100" style="top: 0; left: 0; z-index: -1; pointer-events: none; opacity: 0.6;"></canvas>'
c = c.replace(old_canvas, '')

# Inject the DOMContentLoaded force script near switchPacienteTab
target_script = '''function switchPacienteTab(tabId) {'''
injection = '''
document.addEventListener("DOMContentLoaded", function() {
    if(typeof cambiarVista === 'function') {
        cambiarVista('vista-inicio');
    }
    if(typeof switchPacienteTab === 'function') {
        switchPacienteTab('vista-inicio');
    }
});
'''

c = c.replace(target_script, injection + target_script)

with io.open('src/main/webapp/views/dashboard.jsp', 'w', encoding='utf-8') as f:
    f.write(c)

print("dashboard.jsp updated")
