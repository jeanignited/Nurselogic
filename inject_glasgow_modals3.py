# -*- coding: utf-8 -*-
import io

with io.open('src/main/webapp/includes/modals.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

old_str = '<!-- Tab Glasgow -->\n                <div class="tab-pane fade" id="glasgow" role="tabpanel">\n                    <div class="d-flex justify-content-between align-items-center mb-3 p-3 rounded" style="background: rgba(0,0,0,0.2); border: 1px solid var(--theme-color);">'

new_str = '''<!-- Tab Glasgow -->
                <div class="tab-pane fade" id="glasgow" role="tabpanel">
                    <div class="d-flex justify-content-between align-items-center mb-2">
                        <label class="form-label small text-secondary fw-semibold mb-0">Evaluaci\u00F3n Glasgow</label>
                        <div class="form-check form-switch">
                            <input class="form-check-input" type="checkbox" id="glasgowCheckAtender" onchange="toggleGlasgow('Atender')">
                            <label class="form-check-label text-muted small" for="glasgowCheckAtender">No aplica / No evaluado</label>
                        </div>
                    </div>
                    <div id="glasgowContainerAtender">
                        <div class="d-flex justify-content-between align-items-center mb-3 p-3 rounded" style="background: rgba(0,0,0,0.2); border: 1px solid var(--theme-color);">'''

if old_str in c:
    c = c.replace(old_str, new_str)
    
    old_end = '                                <option value="1">1 - Sin respuesta</option>\n                            </select>\n                        </div>\n                    </div>\n                </div>'
    new_end = '                                <option value="1">1 - Sin respuesta</option>\n                            </select>\n                        </div>\n                    </div>\n                    </div>\n                </div>'
    c = c.replace(old_end, new_end)
    
    with io.open('src/main/webapp/includes/modals.jsp', 'w', encoding='utf-8') as f:
        f.write(c)
    print("Success")
else:
    print("Not found")
