import io
import re

with io.open('src/main/webapp/views/dashboard.jsp', 'r', encoding='latin-1') as f:
    c = f.read()

# Instead of exact match, let's use regex to find the block to replace
pattern = r'<div id="dashboard" class="vista-activa position-relative" style="min-height: 80vh; overflow: hidden; border-radius: 12px; padding: 20px;">\s*<canvas id="dashboardParticles".*?</canvas>\s*<div class="mb-5 text-center".*?</div>'

new_dashboard_header = '''<div id="dashboard" class="vista-activa position-relative" style="min-height: 80vh; overflow: visible; border-radius: 12px; padding: 20px;">
            <div class="mb-5 text-center" style="animation: fadeInDown 0.8s ease-out;">
                <%
                    String nombreBienvenida = (String) session.getAttribute("nombres");
                    if(nombreBienvenida != null && !nombreBienvenida.trim().isEmpty() && !nombreBienvenida.contains("null")) {
                        nombreBienvenida = nombreBienvenida.trim().split(" ")[0];
                    } else {
                        nombreBienvenida = "Usuario";
                    }
                %>
                <h2 class="fw-bold text-theme mb-2" style="font-size: 2.5rem; letter-spacing: -0.5px;">Bienvenido, <span style="color: #38bdf8;"><%= nombreBienvenida %></span></h2>
                <p class="text-secondary fs-5">Este es el resumen de actividad de tu centro m&eacute;dico hoy.</p>
            </div>'''

c = re.sub(pattern, new_dashboard_header, c, flags=re.DOTALL)

with io.open('src/main/webapp/views/dashboard.jsp', 'w', encoding='utf-8') as f:
    f.write(c)

print('Updated dashboard.jsp with dynamic name and HTML entity for e acute')
