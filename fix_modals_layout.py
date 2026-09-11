import io, re

with io.open('src/main/webapp/includes/modals.jsp', 'r', encoding='windows-1252') as f:
    c = f.read()

# We need to find the START of the new modal, and the END of the old modal fragments.
# The new modal starts with: <!-- Modal Ficha Clinica y Diagnostico Inteligente -->
# The old modal ended just before: <!-- Modal Ver Factura -->

start_marker = '<!-- Modal Ficha Clinica y Diagnostico Inteligente -->'
end_marker = '<!-- Modal Ver Factura -->'

if start_marker in c and end_marker in c:
    before = c[:c.find(start_marker)]
    after = c[c.find(end_marker):]
    
    new_ficha = '''<!-- Modal Ficha Clinica y Diagnostico Inteligente -->
<div class="modal fade" id="modalFichaClinica" tabindex="-1" aria-hidden="true">
  <div class="modal-dialog modal-dialog-centered modal-lg">
    <div class="modal-content text-theme" style="background: var(--bg-panel); backdrop-filter: blur(15px); border: var(--glass-border);">
      <div class="modal-header border-0 pb-0">
        <div>
          <h4 class="modal-title fw-bold text-info"><i class="bi bi-file-earmark-medical me-2"></i>Ficha Mdica Integral</h4>
          <h5 class="fw-bold m-0 mt-1 text-light" id="fichaNombre">---</h5>
          <small class="text-secondary" id="fichaInfo">Cdula: -- | Nacimiento: -- | Sexo: --</small>
        </div>
        <button type="button" class="btn-close btn-close-white align-self-start" onclick="cerrarModalFicha()"></button>
      </div>
      <div class="modal-body p-4">
        
        <div class="d-flex justify-content-between align-items-center mb-3">
            <h6 class="fw-bold text-primary m-0"><i class="bi bi-heart-pulse-fill text-danger me-2"></i>Evaluación Clínica (Última)</h6>
            <span class="badge bg-secondary py-2 px-3" id="fichaFechaActualizacion"><i class="bi bi-calendar3 me-1"></i> Fecha: --</span>
        </div>
        
        <div class="table-responsive">
            <table class="table table-bordered table-dark-custom mb-4" style="background: rgba(255,255,255,0.02); border-color: rgba(255,255,255,0.1);">
                <tbody>
                    <tr>
                        <td class="fw-bold text-secondary" style="width: 25%;"><i class="bi bi-person-bounding-box me-2 text-info"></i>Antropometría</td>
                        <td id="fichaEstPeso" class="fw-semibold text-light">-- / --</td>
                    </tr>
                    <tr>
                        <td class="fw-bold text-secondary"><i class="bi bi-thermometer-half me-2 text-warning"></i>Temperatura</td>
                        <td id="fichaTemp" class="fw-bold text-warning">-- C</td>
                    </tr>
                    <tr>
                        <td class="fw-bold text-secondary"><i class="bi bi-heart-pulse-fill me-2 text-danger"></i>Presión Arterial</td>
                        <td id="fichaPresion" class="fw-bold text-info">--</td>
                    </tr>
                    <tr>
                        <td class="fw-bold text-secondary"><i class="bi bi-activity me-2 text-success"></i>Pulso / Sat. O2</td>
                        <td id="fichaFcSat" class="fw-bold text-success">-- / --</td>
                    </tr>
                    <tr>
                        <td class="fw-bold text-secondary"><i class="bi bi-virus me-2" style="color: #c084fc;"></i>Enfermedades</td>
                        <td id="fichaEnfermedades" class="text-light">Ninguna</td>
                    </tr>
                    <tr>
                        <td class="fw-bold text-secondary"><i class="bi bi-exclamation-triangle-fill me-2 text-danger"></i>Alergias</td>
                        <td id="fichaAlergias" class="fw-bold text-danger">Ninguna</td>
                    </tr>
                </tbody>
            </table>
        </div>

        <h6 class="fw-bold text-info mb-3"><i class="bi bi-cpu me-1"></i>Inteligencia Clínica</h6>
        <div id="fichaAlertasContenedor">
          <!-- Contenido generado dinmicamente -->
        </div>
      </div>

      <div class="modal-footer border-0 pt-0">
        <button type="button" class="btn btn-outline-warning rounded-pill px-4" onclick="editarPacienteDesdeFicha()"><i class="bi bi-pencil-square me-1"></i>Editar Paciente</button>
        <button type="button" class="btn btn-secondary rounded-pill px-4" onclick="cerrarModalFicha()">Cerrar</button>
      </div>
    </div>
  </div>
</div>
'''
    
    c = before + new_ficha + after

    with io.open('src/main/webapp/includes/modals.jsp', 'w', encoding='windows-1252') as f:
        f.write(c)
    print("Fixed!")
else:
    print("Markers not found!")
