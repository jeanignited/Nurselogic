# -*- coding: utf-8 -*-
import io
import re

with io.open('src/main/webapp/views/dashboard.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

new_block = u'''            <!-- Jumbotron de Bienvenida (Ahora por fuera de los Datos Clinicos) -->
            <div class="p-5 mb-5 rounded-4 shadow-sm text-white position-relative overflow-hidden" style="background: linear-gradient(135deg, #1e293b, #0f172a); border-left: 5px solid #3b82f6;">
                <!-- Marca de Agua -->
                <i class="bi bi-heart-pulse text-primary position-absolute" style="font-size: 15rem; opacity: 0.05; right: -2%; top: 50%; transform: translateY(-50%) rotate(-15deg); pointer-events: none;"></i>
                
                <div class="container-fluid py-2 position-relative" style="z-index: 2;">
                    <h1 class="display-5 fw-bold mb-3">
                        Bienvenido, <%= (miHC != null && miHC.getNombres() != null) ? miHC.getNombres().split(" ")[0] : "Paciente" %>
                    </h1>
                    <p class="fs-5 text-light opacity-75 mb-4" style="max-width: 800px; line-height: 1.6;">
                        Bienvenido a NurseLogic. Tu ecosistema de salud digital dise&ntilde;ado para darte control total sobre tu historial cl&iacute;nico, facilitar el agendamiento de tus citas y mantener una comunicaci&oacute;n directa con tus especialistas.
                    </p>
                    <button class="btn btn-primary btn-lg rounded-pill px-4 py-3 fw-bold shadow" onclick="document.getElementById('formAgendar').scrollIntoView({behavior: 'smooth'})">
                        <i class="bi bi-calendar-plus me-2"></i>Agendar Nueva Cita
                    </button>
                </div>
            </div>

            <!-- Contenedor de Datos Clinicos -->
            <div class="form-section mt-0 mb-4 border-start border-4 border-success">
                <h5 class="mb-4 fw-bold text-theme"><i class="bi bi-file-earmark-medical text-success me-2"></i>Tus Datos Cl&iacute;nicos Actuales</h5>'''

pattern = r'<div class="form-section mt-0 mb-4 border-start border-4 border-success">\s*<!-- Jumbotron de Bienvenida -->.*?Tus Datos Cl&iacute;nicos Actuales</h5>'

c = re.sub(pattern, new_block, c, flags=re.DOTALL)

with io.open('src/main/webapp/views/dashboard.jsp', 'w', encoding='utf-8') as f:
    f.write(c)

print("Updated dashboard with corrected Jumbotron placement and watermark.")
