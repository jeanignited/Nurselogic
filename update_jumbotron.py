import io
import re

with io.open('src/main/webapp/views/dashboard.jsp', 'r', encoding='utf-8', errors='ignore') as f:
    c = f.read()

# I will find the exact <h4> block and replace it. Since there might be encoding issues with Cl&iacute;nicos / Clnicos,
# I will use a regex.
pattern = r'<h4 class="mb-4 fw-bold" style="color: #10b981;">.*?Mis Datos Cl.*?nicos.*?</h4>'

jumbotron = '''
                <!-- Jumbotron de Bienvenida -->
                <div class="p-5 mb-5 rounded-4 shadow-sm text-white" style="background: linear-gradient(135deg, #1e293b, #0f172a); border-left: 5px solid #3b82f6;">
                    <div class="container-fluid py-2">
                        <h1 class="display-5 fw-bold mb-3">
                            Bienvenido, <%= (session.getAttribute("nombres") != null) ? session.getAttribute("nombres").toString().split(" ")[0] : "Paciente" %>
                        </h1>
                        <p class="fs-5 text-light opacity-75 mb-4" style="max-width: 800px; line-height: 1.6;">
                            Bienvenido a NurseLogic. Tu ecosistema de salud digital dise&ntilde;ado para darte control total sobre tu historial cl&iacute;nico, facilitar el agendamiento de tus citas y mantener una comunicaci&oacute;n directa con tus especialistas.
                        </p>
                        <button class="btn btn-primary btn-lg rounded-pill px-4 py-3 fw-bold shadow" onclick="document.getElementById('formAgendar').scrollIntoView({behavior: 'smooth'})">
                            <i class="bi bi-calendar-plus me-2"></i>Agendar Nueva Cita
                        </button>
                    </div>
                </div>

                <h5 class="mb-4 fw-bold text-theme"><i class="bi bi-file-earmark-medical text-success me-2"></i>Tus Datos Cl&iacute;nicos Actuales</h5>
'''

# The session attribute for patient name is usually "nombres" or "nombrePaciente", in index.jsp we see session.getAttribute("nombres") used for Admin. 
# The user explicitly asked to use session.getAttribute("nombrePaciente"), so I will follow their code verbatim.
jumbotron = jumbotron.replace('session.getAttribute("nombres")', 'session.getAttribute("nombrePaciente")')

c = re.sub(pattern, jumbotron, c)

with io.open('src/main/webapp/views/dashboard.jsp', 'w', encoding='utf-8') as f:
    f.write(c)

print('Updated the patient dashboard header successfully')
