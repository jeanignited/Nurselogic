# -*- coding: utf-8 -*-
import io

with io.open('src/main/webapp/includes/modals.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

old_glasgow = '''<!-- Tab Glasgow -->
                  <div class="tab-pane fade" id="glasgow" role="tabpanel">
                      <div class="d-flex justify-content-between align-items-center mb-3 p-3 rounded" style="background: rgba(0,0,0,0.2); border: 1px solid var(--theme-color);">
                          <h6 class="m-0 text-info fw-bold">Puntaje Total Glasgow:</h6>
                          <span id="glasgowTotal" class="badge bg-primary fs-5 px-3">15 / 15</span>
                          <span id="glasgowDesc" class="fw-bold text-success">Normal</span>
                      </div>'''

new_glasgow = '''<!-- Tab Glasgow -->
                  <div class="tab-pane fade" id="glasgow" role="tabpanel">
                      <div class="d-flex justify-content-between align-items-center mb-2">
                          <label class="form-label small text-secondary fw-semibold mb-0">Evaluaci\u00F3n Glasgow</label>
                          <div class="form-check form-switch">
                              <input class="form-check-input" type="checkbox" id="glasgowCheckAtender" onchange="toggleGlasgow('Atender')">
                              <label class="form-check-label text-muted small" for="glasgowCheckAtender">No aplica / No evaluado</label>
                          </div>
                      </div>
                      <div id="glasgowContainerAtender">
                          <div class="d-flex justify-content-between align-items-center mb-3 p-3 rounded" style="background: rgba(0,0,0,0.2); border: 1px solid var(--theme-color);">
                              <h6 class="m-0 text-info fw-bold">Puntaje Total Glasgow:</h6>
                              <span id="glasgowTotal" class="badge bg-primary fs-5 px-3">15 / 15</span>
                              <span id="glasgowDesc" class="fw-bold text-success">Normal</span>
                          </div>'''

c = c.replace(old_glasgow, new_glasgow)

# Also need to close the div for glasgowContainerAtender
# It is right before the Diagnostico tab. Let's find it.
old_end = '''                          </div>
                      </div>
                  </div>
  
                  <!-- Tab Diagnstico & Receta -->'''

new_end = '''                          </div>
                      </div>
                      </div>
                  </div>
  
                  <!-- Tab Diagn\u00F3stico & Receta -->'''

c = c.replace(old_end, new_end)
# Replace potential decoding issues with literal
c = c.replace('<!-- Tab Diagnstico & Receta -->', '<!-- Tab Diagn\u00F3stico & Receta -->')
c = c.replace('<!-- Tab Diagn\u00F3stico & Receta -->', new_end.replace('<!-- Tab Diagn\u00F3stico & Receta -->', '<!-- Tab Diagn\u00F3stico & Receta -->'))

with io.open('src/main/webapp/includes/modals.jsp', 'w', encoding='utf-8') as f:
    f.write(c)
