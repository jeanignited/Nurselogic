import io
import re

with io.open('src/main/webapp/views/dashboard.jsp', 'r', encoding='latin-1') as f:
    c = f.read()

new_dashboard_header = '''        <div id="dashboard" class="vista-activa position-relative" style="min-height: 80vh; overflow: hidden; border-radius: 12px; padding: 20px;">
            <canvas id="dashboardParticles" class="position-absolute w-100 h-100" style="top:0; left:0; z-index:-1; pointer-events: none; opacity: 0.6;"></canvas>
            
            <div class="mb-5 text-center" style="animation: fadeInDown 0.8s ease-out;">
                <h2 class="fw-bold text-white mb-2" style="font-size: 2.5rem; letter-spacing: -0.5px;">Bienvenido, <span style="color: #38bdf8;"><%= (request.getAttribute("correoLogueado") != null ? request.getAttribute("correoLogueado").toString().split("@")[0] : "Admin") %></span></h2>
                <p class="text-secondary fs-5">Este es el resumen de actividad de tu centro m\u00e9dico hoy.</p>
            </div>
'''
c = c.replace('<div id="dashboard" class="vista-activa">', new_dashboard_header)

with io.open('src/main/webapp/views/dashboard.jsp', 'w', encoding='latin-1') as f:
    f.write(c)
print('Added welcome header and canvas (latin-1)')
