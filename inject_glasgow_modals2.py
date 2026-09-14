import io
import re

with io.open('src/main/webapp/includes/modals.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

pattern = r'(<!-- Tab Glasgow -->\s*<div class="tab-pane fade" id="glasgow" role="tabpanel">\s*)(<div class="d-flex justify-content-between align-items-center mb-3 p-3 rounded" style="background: rgba\(0,0,0,0\.2\); border: 1px solid var\(--theme-color\);">)'
replacement = r'''\1<div class="d-flex justify-content-between align-items-center mb-2">
                          <label class="form-label small text-secondary fw-semibold mb-0">Evaluaci\u00F3n Glasgow</label>
                          <div class="form-check form-switch">
                              <input class="form-check-input" type="checkbox" id="glasgowCheckAtender" onchange="toggleGlasgow('Atender')">
                              <label class="form-check-label text-muted small" for="glasgowCheckAtender">No aplica / No evaluado</label>
                          </div>
                      </div>
                      <div id="glasgowContainerAtender">
                          \2'''
c = re.sub(pattern, replacement, c)

# Add closing div to glasgowContainerAtender
pattern_end = r'(<option value="1">1 - Sin respuesta</option>\s*</select>\s*</div>\s*</div>\s*</div>)'
replacement_end = r'\1\n                      </div>'
c = re.sub(pattern_end, replacement_end, c)

with io.open('src/main/webapp/includes/modals.jsp', 'w', encoding='utf-8') as f:
    f.write(c)
