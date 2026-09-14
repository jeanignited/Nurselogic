import io
import re

with io.open('src/main/webapp/includes/modals.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

# I will inject it inside the tab-pane for Signos Vitales in modalAtenderCita.
# Currently it looks like:
# <!-- Tab Signos Vitales -->
# <div class="tab-pane fade show active" id="vitales" role="tabpanel">
#     <div class="row g-3">
#         <div class="col-md-4">
#             <label class="form-label small text-secondary">Frecuencia Card&iacute;aca (lpm)</label>

html_to_inject = '''<!-- Tab Signos Vitales -->
                  <div class="tab-pane fade show active" id="vitales" role="tabpanel">
                      
                      <div class="row g-3 mb-4">
                          <div class="col-md-6">
                              <label class="form-label small text-secondary">Enfermedades Preexistentes</label>
                              <select name="enfermedad" id="atender_enfermedad" class="form-select" multiple size="4">
                                  <option value="Ninguna">Ninguna</option>
                                  <% 
                                      List<Map<String, String>> enf_mod = (List<Map<String, String>>) request.getAttribute("listaEnfermedades");
                                      if(enf_mod != null) {
                                          for(Map<String, String> e : enf_mod) {
                                              out.print("<option value='" + e.get("nombre") + "'>" + e.get("nombre") + "</option>");
                                          }
                                      }
                                  %>
                              </select>
                          </div>
                          <div class="col-md-6">
                              <label class="form-label small text-secondary">Alergias Conocidas</label>
                              <select name="alergias" id="atender_alergias" class="form-select" multiple size="4">
                                  <option value="Ninguna">Ninguna</option>
                                  <% 
                                      List<Map<String, String>> ale_mod = (List<Map<String, String>>) request.getAttribute("listaAlergias");
                                      if(ale_mod != null) {
                                          for(Map<String, String> a : ale_mod) {
                                              out.print("<option value='" + a.get("nombre") + "'>" + a.get("nombre") + " (" + a.get("gravedad") + ")</option>");
                                          }
                                      }
                                  %>
                              </select>
                          </div>
                      </div>

                      <h6 class="text-theme pb-2 mb-3" style="border-bottom: 1px solid rgba(255,255,255,0.1);"><i class="bi bi-person-bounding-box me-2 text-primary"></i>Evaluaci\u00F3n Antropom\u00E9trica (IMC)</h6>
                      <div class="row g-3 mb-4 align-items-center">
                          <div class="col-md-3">
                              <label class="form-label small text-secondary">Estatura (m)</label>
                              <input type="text" id="atender_estatura_input" name="estatura" class="form-control" maxlength="4" oninput="formatearEstatura(this)" placeholder="Ej: 1.85" autocomplete="off">
                          </div>
                          <div class="col-md-3">
                              <label class="form-label small text-secondary">Peso (kg)</label>
                              <input type="text" id="atender_peso_input" name="peso" class="form-control" maxlength="5" oninput="formatearPeso(this)" placeholder="Ej: 75.5" autocomplete="off">
                          </div>
                          <div class="col-md-6">
                              <div class="d-flex align-items-center p-2 rounded" style="background: rgba(0,0,0,0.1); border: 1px solid rgba(255,255,255,0.1);">
                                  <i class="bi bi-calculator text-primary fs-3 me-3"></i>
                                  <div>
                                      <div class="small text-secondary mb-1">Resultado IMC</div>
                                      <span id="atender_imcValor" class="fw-bold text-theme fs-4">0.0</span>
                                      <span id="atender_imcEstado" class="badge bg-secondary ms-2">Sin datos</span>
                                  </div>
                              </div>
                          </div>
                      </div>

                      <h6 class="text-theme pb-2 mb-3" style="border-bottom: 1px solid rgba(255,255,255,0.1);"><i class="bi bi-heart-pulse text-danger me-2"></i>Signos Vitales</h6>
                      <div class="row g-3">'''

c = re.sub(r'<!-- Tab Signos Vitales -->\s*<div class="tab-pane fade show active" id="vitales" role="tabpanel">\s*<div class="row g-3">', html_to_inject, c)

with io.open('src/main/webapp/includes/modals.jsp', 'w', encoding='utf-8') as f:
    f.write(c)
