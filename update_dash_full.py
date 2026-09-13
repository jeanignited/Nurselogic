# -*- coding: utf-8 -*-
import io

with io.open('src/main/webapp/views/dashboard.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

# 1. Add filters to vista-citas
citas_header = '<h3 class="fw-bold mb-4" style="color: #f59e0b;"><i class="bi bi-calendar-event me-2"></i>Historial de Citas M&eacute;dicas</h3>'
citas_filters = '''<h3 class="fw-bold mb-4" style="color: #f59e0b;"><i class="bi bi-calendar-event me-2"></i>Historial de Citas M&eacute;dicas</h3>
            <div class="row mb-3 align-items-center">
                <div class="col-md-4">
                    <input type="date" class="form-control bg-dark text-white border-secondary" id="filtroFechaCitas" style="color-scheme: dark;">
                </div>
                <div class="col-md-8 text-md-end mt-3 mt-md-0 d-flex justify-content-md-end align-items-center">
                    <div class="form-check form-switch m-0">
                        <input class="form-check-input" type="checkbox" id="switchOcultarHistorial">
                        <label class="form-check-label text-muted ms-2" for="switchOcultarHistorial">Ocultar Historial (Atendidos / Cancelados)</label>
                    </div>
                </div>
            </div>'''
c = c.replace(citas_header, citas_filters)

# 2. Add vista-resultados and vista-recetas after vista-citas finishes
# Find the end of vista-citas, which is just before <script>
script_start = '<script>\\n            function switchPacienteTab(tabId) {'
if script_start not in c:
    script_start = '<script>\\n            function switchPacienteTab(tabId)'
# Let's use string finding
idx = c.find('<script>')
if idx != -1:
    idx2 = c.find('function switchPacienteTab', idx)
    if idx2 != -1:
        # We found the script. Let's insert before the <script> tag.
        script_idx = c.rfind('<script>', 0, idx2)

new_views = u'''
        <!-- VISTA RESULTADOS / EXAMENES -->
        <div id="vista-resultados" class="d-none">
            <h3 class="fw-bold mb-4" style="color: #a855f7;"><i class="bi bi-file-earmark-medical me-2"></i>Resultados y Ex&aacute;menes Cl&iacute;nicos</h3>
            <div class="row mb-3 align-items-center">
                <div class="col-md-4">
                    <input type="date" class="form-control bg-dark text-white border-secondary" id="filtroFechaResultados" style="color-scheme: dark;">
                </div>
            </div>
            <div class="card border-0 rounded-4 shadow-sm" style="background: var(--bg-panel); overflow: hidden;">
                <div class="card-body p-0">
                    <div class="table-responsive">
                        <table class="table table-borderless table-hover text-white align-middle mb-0" style="background: transparent;">
                            <thead style="background: rgba(0,0,0,0.2);">
                                <tr>
                                    <th class="py-3 px-4 fw-semibold text-secondary">Fecha</th>
                                    <th class="py-3 px-4 fw-semibold text-secondary">Tipo de Examen</th>
                                    <th class="py-3 px-4 fw-semibold text-secondary">M&eacute;dico Solicitante</th>
                                    <th class="py-3 px-4 fw-semibold text-secondary text-center">Acciones</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td colspan="4" class="text-center py-5 text-muted">No hay resultados registrados.</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        </div>

        <!-- VISTA MIS RECETAS -->
        <div id="vista-recetas" class="d-none">
            <h3 class="fw-bold mb-4" style="color: #10b981;"><i class="bi bi-capsule me-2"></i>Mis Recetas M&eacute;dicas</h3>
            <div class="row mb-3 align-items-center">
                <div class="col-md-4">
                    <input type="date" class="form-control bg-dark text-white border-secondary" id="filtroFechaRecetas" style="color-scheme: dark;">
                </div>
            </div>
            <div class="card border-0 rounded-4 shadow-sm" style="background: var(--bg-panel); overflow: hidden;">
                <div class="card-body p-0">
                    <div class="table-responsive">
                        <table class="table table-borderless table-hover text-white align-middle mb-0" style="background: transparent;">
                            <thead style="background: rgba(0,0,0,0.2);">
                                <tr>
                                    <th class="py-3 px-4 fw-semibold text-secondary">Fecha</th>
                                    <th class="py-3 px-4 fw-semibold text-secondary">Diagn&oacute;stico</th>
                                    <th class="py-3 px-4 fw-semibold text-secondary">M&eacute;dico</th>
                                    <th class="py-3 px-4 fw-semibold text-secondary text-center">Acciones</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td colspan="4" class="text-center py-5 text-muted">No hay recetas m&eacute;dicas registradas.</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        </div>

'''

new_script = u'''<script>
            function switchPacienteTab(tabId) {
                const vistas = ['vista-inicio', 'vista-citas', 'vista-resultados', 'vista-recetas'];
                vistas.forEach(v => {
                    const el = document.getElementById(v);
                    if (el) el.classList.add('d-none');
                });
                const seleccionada = document.getElementById(tabId);
                if (seleccionada) seleccionada.classList.remove('d-none');
            }

            document.addEventListener("DOMContentLoaded", function() {
                let today = new Date().toISOString().split('T')[0];
                const filtros = ['filtroFechaCitas', 'filtroFechaResultados', 'filtroFechaRecetas'];
                filtros.forEach(id => {
                    const input = document.getElementById(id);
                    if(input) input.setAttribute('max', today);
                });
            });
        </script>
'''

# Find the start of the old script and the end of the file/block
import re
pattern = r'<script>\s*function switchPacienteTab[\s\S]*?</script>'
c = re.sub(pattern, new_script, c)

c = c[:script_idx] + new_views + c[script_idx:]

with io.open('src/main/webapp/views/dashboard.jsp', 'w', encoding='utf-8') as f:
    f.write(c)

print("dashboard.jsp updated with new views and filters.")
