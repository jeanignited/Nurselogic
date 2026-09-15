import io
import re

with io.open('src/main/webapp/includes/sidebar.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

new_cards = """            <% if(isPaciente) { %>
            <div class="px-3 mt-auto texto-nav mb-2">
                <div class="card bg-dark text-white border-secondary mb-2 rounded-3 shadow-sm" style="border: 1px solid rgba(255,255,255,0.1) !important;">
                    <div class="card-body p-3">
                        <h6 class="card-title fw-bold text-info mb-1"><i class="bi bi-info-circle me-1"></i>Centro de Ayuda</h6>
                        <p class="card-text small text-secondary mb-2" style="font-size: 0.75rem;">\u00bfTienes dudas con tu cita o historial? Cont\u00e1ctanos.</p>
                        <button class="btn btn-sm btn-primary w-100 rounded-pill fw-semibold" onclick="mostrarAlertaSoporte()">Contactar Soporte</button>
                    </div>
                </div>
                <div class="card bg-dark text-white border-secondary rounded-3 shadow-sm" style="border: 1px solid rgba(255,255,255,0.1) !important;">
                    <div class="card-body p-3 text-center">
                        <h6 class="card-title fw-bold text-danger mb-0"><i class="bi bi-telephone-fill me-1"></i>Emergencias</h6>
                        <h3 class="text-danger fw-bold m-0 mt-1" style="letter-spacing: 2px;">911</h3>
                    </div>
                </div>
            </div>
            <li class="nav-item pb-4"><a class="nav-link" href="login.jsp">
                <i class="bi bi-box-arrow-left" style="color: #ef4444;"></i><span class="texto-nav">Cerrar Sesion</span>
            </a></li>
            <% } else { %>
            <li class="nav-item mt-auto pt-4 pb-4"><a class="nav-link" href="login.jsp">
                <i class="bi bi-box-arrow-left" style="color: #ef4444;"></i><span class="texto-nav">Cerrar Sesion</span>
            </a></li>
            <% } %>"""

c = c.replace("""            <li class="nav-item mt-auto pt-4 pb-4"><a class="nav-link" href="login.jsp">
                <i class="bi bi-box-arrow-left" style="color: #ef4444;"></i><span class="texto-nav">Cerrar Sesion</span>
            </a></li>""", new_cards)

with io.open('src/main/webapp/includes/sidebar.jsp', 'w', encoding='utf-8') as f:
    f.write(c)

print("Updated sidebar.jsp")
