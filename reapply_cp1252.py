import io
import re

with io.open('src/main/webapp/views/dashboard.jsp', 'r', encoding='cp1252') as f:
    c = f.read()

new_dashboard_header = '''        <div id="dashboard" class="vista-activa position-relative" style="min-height: 80vh; overflow: visible; border-radius: 12px; padding: 20px;">
            <div class="mb-5 text-center" style="animation: fadeInDown 0.8s ease-out;">
                <%
                    String nombreBienvenida = (String) session.getAttribute("nombres");
                    if(nombreBienvenida != null && !nombreBienvenida.trim().isEmpty() && !nombreBienvenida.contains("null")) {
                        nombreBienvenida = nombreBienvenida.trim();
                    } else {
                        nombreBienvenida = "Usuario";
                    }
                %>
                <h2 class="fw-bold text-white mb-2" style="font-size: 2.5rem; letter-spacing: -0.5px;">Bienvenido, <span style="color: #38bdf8;"><%= nombreBienvenida %></span></h2>
                <p class="text-secondary fs-5">Este es el resumen de actividad de tu centro m&eacute;dico hoy.</p>
            </div>
'''

c = c.replace('<div id="dashboard" class="vista-activa">', new_dashboard_header)

with io.open('src/main/webapp/views/dashboard.jsp', 'w', encoding='cp1252') as f:
    f.write(c)

print('Re-applied welcome header using cp1252')
