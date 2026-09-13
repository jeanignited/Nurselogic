# -*- coding: utf-8 -*-
import io

with io.open('src/main/webapp/views/dashboard.jsp', 'r', encoding='utf-8', errors='ignore') as f:
    c = f.read()

agendar_str = c.find('Agendar Cita M')
start_idx = c.rfind('<div class="row g-4">', 0, agendar_str)

offset = c.find('Introduce tus datos')
end_idx = c.find('</div>', offset)
end_idx = c.find('</div>', end_idx+1)
end_idx = c.find('</div>', end_idx+1)
end_idx = c.find('</div>', end_idx+1)
end_idx = c.find('</div>', end_idx+1) + 6

new_block = u'''<div class="row g-4 mb-4">
                <div class="col-md-7">
                    <div class="form-section mt-0 d-flex flex-column h-100 justify-content-between">
                        <div>
                            <h4 class="mb-4 fw-bold" style="color: #3b82f6;"><i class="bi bi-calendar-plus me-2"></i>Agendar Cita M&eacute;dica</h4>
                            <p class="text-secondary mb-4">Selecciona la especialidad, fecha y hora para programar tu consulta con nuestros especialistas.</p>
                            <form action="agendarCita" method="post" autocomplete="off">
                                <div class="mb-4">
                                    <label class="form-label small text-secondary fw-semibold">Especialidad</label>
                                    <input type="text" list="especialidades" name="especialidad" class="form-control form-control-lg border-secondary text-light" style="background: rgba(0,0,0,0.2);" placeholder="Buscar especialidad..." required autocomplete="off">
                                    <datalist id="especialidades">
                                        <%
                                            List<Map<String, String>> espMapPac = (List<Map<String, String>>) request.getAttribute("listaEspecialidadesMap");
                                            if(espMapPac != null && !espMapPac.isEmpty()) {
                                                for(Map<String, String> mEsp : espMapPac) {
                                                    out.print("<option value='" + mEsp.get("id") + "'>" + mEsp.get("descripcion") + "</option>");
                                                }
                                            } else {
                                                out.print("<option value='1'>Medicina General</option>");
                                                out.print("<option value='2'>Odontolog&iacute;a</option>");
                                                out.print("<option value='3'>Pediatr&iacute;a</option>");
                                                out.print("<option value='4'>Ginecolog&iacute;a</option>");
                                            }
                                        %>
                                    </datalist>
                                </div>

                                <div class="row g-4 mb-5">
                                    <div class="col-md-6">
                                        <label class="form-label small text-secondary fw-semibold">Fecha</label>
                                        <input type="date" name="fecha" class="form-control form-control-lg border-secondary text-light" style="background: rgba(0,0,0,0.2); color-scheme: dark;" min="<%= java.time.LocalDate.now().toString() %>" autocomplete="off" required>
                                    </div>
                                    <div class="col-md-6">
                                        <label class="form-label small text-secondary fw-semibold">Hora</label>
                                        <input type="time" name="hora" class="form-control form-control-lg border-secondary text-light" style="background: rgba(0,0,0,0.2); color-scheme: dark;" required autocomplete="off">
                                    </div>
                                </div>

                                <button type="submit" class="btn btn-primary w-100 py-3 fs-5 mt-auto"><i class="bi bi-check2-circle me-2"></i>CONFIRMAR CITA</button>
                            </form>
                        </div>
                    </div>
                </div>

                <div class="col-md-5">
                    <div class="form-section mt-0 d-flex flex-column h-100 justify-content-between">
                        <div>
                            <h4 class="mb-4 fw-bold" style="color: #10b981;"><i class="bi bi-calculator me-2"></i>Calculadora de IMC</h4>
                            <p class="text-secondary mb-4">Conoce tu &Iacute;ndice de Masa Corporal para un mejor seguimiento de tu salud.</p>
                            
                            <div class="mb-4">
                                <label class="form-label small text-secondary fw-semibold">Estatura (metros)</label>
                                <div class="input-group input-group-lg">
                                    <span class="input-group-text border-secondary text-primary border-end-0" style="background: rgba(0,0,0,0.3);"><i class="bi bi-rulers"></i></span>
                                    <input type="text" id="estatura_pac" class="form-control border-secondary text-light border-start-0" style="background: rgba(0,0,0,0.15);" maxlength="4" oninput="formatearEstatura_pac(this)" placeholder="Ej: 1.75" required autocomplete="off">
                                </div>
                            </div>
                            <div class="mb-5">
                                <label class="form-label small text-secondary fw-semibold">Peso (kg)</label>
                                <div class="input-group input-group-lg">
                                    <span class="input-group-text border-secondary text-warning border-end-0" style="background: rgba(0,0,0,0.3);"><i class="bi bi-speedometer2"></i></span>
                                    <input type="text" id="peso_pac" class="form-control border-secondary text-light border-start-0" style="background: rgba(0,0,0,0.15);" maxlength="5" oninput="formatearPeso_pac(this)" placeholder="Ej: 70.5" required autocomplete="off">
                                </div>
                            </div>
                        </div>

                        <div class="imc-box flex-column align-items-center justify-content-center text-center p-4 mt-auto rounded-4 shadow-sm" style="background: rgba(0,0,0,0.15); border: 1px dashed rgba(16,185,129,0.3);">
                            <div class="small text-secondary mb-2 fw-semibold text-uppercase tracking-wide">Tu Resultado IMC</div>
                            <span id="imcValor_pac" class="fw-bold mb-2" style="font-size: 3.5rem; line-height: 1; color: #10b981;">0.0</span>
                            <span id="imcEstado_pac" class="badge bg-secondary px-4 py-2 rounded-pill fs-6 mt-2">Introduce tus datos</span>
                        </div>
                    </div>
                </div>
            </div>'''

c = c[:start_idx] + new_block + c[end_idx:]

with io.open('src/main/webapp/views/dashboard.jsp', 'w', encoding='utf-8') as f:
    f.write(c)

print("Lower cards updated successfully.")
