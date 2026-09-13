# -*- coding: utf-8 -*-
import io

with io.open('src/main/webapp/views/dashboard.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

start_str = '<!-- Contenedor de Datos Clinicos -->'
start_idx = c.find(start_str)
end_str = '<% } %>'
end_idx = c.find(end_str, start_idx)

if start_idx != -1 and end_idx != -1:
    new_block = u'''            <!-- Contenedor de Datos Clinicos -->
            <div class="card border-0 mb-5 rounded-4 shadow-sm" style="background: var(--bg-panel); overflow: hidden;">
                <!-- Header -->
                <div class="card-header border-0 px-3 py-3" style="background: rgba(16, 185, 129, 0.05); border-bottom: 1px solid rgba(16, 185, 129, 0.1) !important;">
                    <h5 class="mb-0 fw-bold text-theme d-flex align-items-center">
                        <div class="bg-success bg-opacity-10 rounded-circle p-2 me-2 d-flex align-items-center justify-content-center" style="width: 40px; height: 40px;">
                            <i class="bi bi-clipboard2-pulse-fill text-success fs-4"></i>
                        </div>
                        Mis Datos Cl&iacute;nicos
                    </h5>
                </div>
                
                <div class="card-body p-3 p-md-4">
                    <!-- Datos Personales -->
                    <div class="row g-4 mb-4">
                        <div class="col-md-3">
                            <label class="text-muted small fw-semibold mb-1"><i class="bi bi-person me-2"></i>Nombres Completos</label>
                            <div class="fw-bold fs-5 text-theme"><%= miHC.getNombres() %> <%= miHC.getApellidos() %></div>
                        </div>
                        <div class="col-md-3">
                            <label class="text-muted small fw-semibold mb-1"><i class="bi bi-card-text me-2"></i>C&eacute;dula</label>
                            <div class="fw-bold fs-5 text-theme"><%= miHC.getCedula() %></div>
                        </div>
                        <div class="col-md-3">
                            <label class="text-muted small fw-semibold mb-1"><i class="bi bi-calendar3 me-2"></i>Fecha de Nacimiento</label>
                            <div class="fw-bold fs-5 text-theme"><%= (miHC.getFechaNacimiento() != null) ? miHC.getFechaNacimiento() : "Sin registrar" %></div>
                        </div>
                        <div class="col-md-3">
                            <label class="text-muted small fw-semibold mb-1"><i class="bi bi-clock-history me-2"></i>&Uacute;ltima Actualizaci&oacute;n</label>
                            <div class="fw-bold fs-5 text-theme"><%= java.time.LocalDate.now().toString() %></div>
                        </div>
                    </div>

                    <!-- Signos Vitales -->
                    <div class="row g-3">
                        <div class="col-md-3">
                            <div class="p-3 rounded-4 text-center h-100 border-0" style="background: rgba(0,0,0,0.02); box-shadow: inset 0 0 40px rgba(13, 110, 253, 0.05);">
                                <i class="bi bi-rulers text-primary mb-2 d-block" style="font-size: 2.2rem;"></i>
                                <label class="text-muted small fw-semibold mb-1">Estatura</label>
                                <div class="fw-bolder fs-4 text-theme"><%= miHC.getEstatura() %><span class="fs-6 fw-normal ms-1 text-muted">m</span></div>
                            </div>
                        </div>
                        <div class="col-md-3">
                            <div class="p-3 rounded-4 text-center h-100 border-0" style="background: rgba(0,0,0,0.02); box-shadow: inset 0 0 40px rgba(255, 193, 7, 0.05);">
                                <i class="bi bi-speedometer2 text-warning mb-2 d-block" style="font-size: 2.2rem;"></i>
                                <label class="text-muted small fw-semibold mb-1">Peso</label>
                                <div class="fw-bolder fs-4 text-theme"><%= miHC.getPeso() %><span class="fs-6 fw-normal ms-1 text-muted">kg</span></div>
                            </div>
                        </div>
                        <div class="col-md-3">
                            <div class="p-3 rounded-4 text-center h-100 border-0" style="background: rgba(0,0,0,0.02); box-shadow: inset 0 0 40px rgba(220, 53, 69, 0.05);">
                                <i class="bi bi-activity text-danger mb-2 d-block" style="font-size: 2.2rem;"></i>
                                <label class="text-muted small fw-semibold mb-1">Presi&oacute;n</label>
                                <div class="fw-bolder fs-4 text-theme"><%= (miHC.getPresionArterial() != null && !miHC.getPresionArterial().trim().isEmpty()) ? miHC.getPresionArterial() : "--" %></div>
                            </div>
                        </div>
                        <div class="col-md-3">
                            <div class="p-3 rounded-4 text-center h-100 border-0" style="background: rgba(0,0,0,0.02); box-shadow: inset 0 0 40px rgba(25, 135, 84, 0.05);">
                                <i class="bi bi-thermometer-half text-success mb-2 d-block" style="font-size: 2.2rem;"></i>
                                <label class="text-muted small fw-semibold mb-1">Temperatura</label>
                                <div class="fw-bolder fs-4 text-theme"><%= miHC.getTemperatura() %><span class="fs-6 fw-normal ms-1 text-muted">&deg;C</span></div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            '''
    c = c[:start_idx] + new_block + c[end_idx:]

    with io.open('src/main/webapp/views/dashboard.jsp', 'w', encoding='utf-8') as f:
        f.write(c)
    print("Dashboard UI refined successfully.")
else:
    print("Block not found!")
