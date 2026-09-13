# -*- coding: utf-8 -*-
import io
import re

with io.open('src/main/webapp/views/dashboard.jsp', 'r', encoding='utf-8', errors='ignore') as f:
    c = f.read()

# Pattern captures from '<!-- Contenedor de Datos Clinicos -->' to the closing </div> before '<% } %>'
pattern = r'<!-- Contenedor de Datos Clinicos -->.*?</div>\s*</div>\s*</div>\s*</div>'
# Let's be very specific:
pattern = r'<!-- Contenedor de Datos Clinicos -->\s*<div class="form-section mt-0 mb-4 border-start border-4 border-success">.*?</div>\s*</div>\s*</div>'
# Wait, the structure is:
# <div class="form-section...">
#   <h5>...</h5>
#   <div class="row...">
#     <div class="col-md-4">...</div>
#     ...
#   </div>
# </div>
# So it is just one </div> for the row, and one </div> for the form-section.
pattern = r'<!-- Contenedor de Datos Clinicos -->.*?</div>\s*</div>\s*</div>'
# Let's use string manipulation to be 100% safe.

start_str = '<!-- Contenedor de Datos Clinicos -->'
start_idx = c.find(start_str)

end_str = '<% } %>'
# Find the FIRST <% } %> after start_idx
end_idx = c.find(end_str, start_idx)

if start_idx != -1 and end_idx != -1:
    new_block = u'''            <!-- Contenedor de Datos Clinicos -->
            <div class="card border-0 mb-5 rounded-4 shadow" style="background: var(--bg-panel); overflow: hidden;">
                <!-- Header -->
                <div class="card-header border-0 px-4 py-3" style="background: rgba(16, 185, 129, 0.05); border-bottom: 1px solid rgba(16, 185, 129, 0.1) !important;">
                    <h4 class="mb-0 fw-bold text-theme d-flex align-items-center">
                        <i class="bi bi-clipboard2-pulse-fill text-success fs-3 me-3"></i>
                        Mis Datos Cl&iacute;nicos
                    </h4>
                </div>
                
                <div class="card-body p-4 p-md-5">
                    <!-- Datos Personales -->
                    <div class="row g-4 mb-5">
                        <div class="col-md-3">
                            <label class="text-secondary small fw-semibold text-uppercase tracking-wide mb-1"><i class="bi bi-person me-2"></i>Nombres Completos</label>
                            <div class="fw-bold fs-5 text-theme"><%= miHC.getNombres() %> <%= miHC.getApellidos() %></div>
                        </div>
                        <div class="col-md-3">
                            <label class="text-secondary small fw-semibold text-uppercase tracking-wide mb-1"><i class="bi bi-card-text me-2"></i>C&eacute;dula</label>
                            <div class="fw-bold fs-5 text-theme"><%= miHC.getCedula() %></div>
                        </div>
                        <div class="col-md-3">
                            <label class="text-secondary small fw-semibold text-uppercase tracking-wide mb-1"><i class="bi bi-calendar3 me-2"></i>Fecha de Nacimiento</label>
                            <div class="fw-bold fs-5 text-theme"><%= (miHC.getFechaNacimiento() != null) ? miHC.getFechaNacimiento() : "Sin registrar" %></div>
                        </div>
                        <div class="col-md-3">
                            <label class="text-secondary small fw-semibold text-uppercase tracking-wide mb-1"><i class="bi bi-clock-history me-2"></i>&Uacute;ltima Actualizaci&oacute;n</label>
                            <div class="fw-bold fs-5 text-theme"><%= java.time.LocalDate.now().toString() %></div>
                        </div>
                    </div>

                    <!-- Signos Vitales -->
                    <div class="row g-4">
                        <div class="col-md-3">
                            <div class="p-4 rounded-4 text-center h-100 shadow-sm" style="background: rgba(0,0,0,0.03); border: 1px solid rgba(0,0,0,0.05);">
                                <i class="bi bi-rulers text-primary mb-3 d-block" style="font-size: 2.5rem;"></i>
                                <label class="text-secondary small fw-bold text-uppercase mb-1">Estatura</label>
                                <div class="fw-bolder fs-4 text-theme"><%= miHC.getEstatura() %><span class="fs-6 fw-normal ms-1 text-secondary">m</span></div>
                            </div>
                        </div>
                        <div class="col-md-3">
                            <div class="p-4 rounded-4 text-center h-100 shadow-sm" style="background: rgba(0,0,0,0.03); border: 1px solid rgba(0,0,0,0.05);">
                                <i class="bi bi-speedometer2 text-warning mb-3 d-block" style="font-size: 2.5rem;"></i>
                                <label class="text-secondary small fw-bold text-uppercase mb-1">Peso</label>
                                <div class="fw-bolder fs-4 text-theme"><%= miHC.getPeso() %><span class="fs-6 fw-normal ms-1 text-secondary">kg</span></div>
                            </div>
                        </div>
                        <div class="col-md-3">
                            <div class="p-4 rounded-4 text-center h-100 shadow-sm" style="background: rgba(0,0,0,0.03); border: 1px solid rgba(0,0,0,0.05);">
                                <i class="bi bi-activity text-danger mb-3 d-block" style="font-size: 2.5rem;"></i>
                                <label class="text-secondary small fw-bold text-uppercase mb-1">Presi&oacute;n</label>
                                <div class="fw-bolder fs-4 text-theme"><%= (miHC.getPresionArterial() != null && !miHC.getPresionArterial().trim().isEmpty()) ? miHC.getPresionArterial() : "--" %></div>
                            </div>
                        </div>
                        <div class="col-md-3">
                            <div class="p-4 rounded-4 text-center h-100 shadow-sm" style="background: rgba(0,0,0,0.03); border: 1px solid rgba(0,0,0,0.05);">
                                <i class="bi bi-thermometer-half text-success mb-3 d-block" style="font-size: 2.5rem;"></i>
                                <label class="text-secondary small fw-bold text-uppercase mb-1">Temperatura</label>
                                <div class="fw-bolder fs-4 text-theme"><%= miHC.getTemperatura() %><span class="fs-6 fw-normal ms-1 text-secondary">&deg;C</span></div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            '''
    
    # We slice out the old block and insert the new one
    # Note: we should leave <% } %> alone since it closes the if(miHC!=null)
    # The end_idx is exactly at '<% } %>'
    c = c[:start_idx] + new_block + c[end_idx:]

    with io.open('src/main/webapp/views/dashboard.jsp', 'w', encoding='utf-8') as f:
        f.write(c)
    print("Successfully replaced clinical data block.")
else:
    print("Could not find boundaries.")
