import io
import re

with io.open('src/main/webapp/views/dashboard.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

old_diag = '''                        <div class="col-md-12">
                            <label class="form-label small text-secondary fw-semibold">Diagn\u00F3stico Cl\u00EDnico Preliminar</label>
                            <textarea name="diagnosticoClinico" class="form-control" rows="3" placeholder="Ej: Paciente presenta dolor abdominal..."></textarea>
                        </div>'''

new_diag = '''                        <div class="col-md-12">
                            <label class="form-label small text-secondary fw-semibold">Diagn\u00F3stico Cl\u00EDnico Preliminar</label>
                            <textarea name="diagnosticoClinico" class="form-control mb-3" rows="3" placeholder="Describa el diagn\u00F3stico, s\u00EDntomas y observaciones..."></textarea>
                            <label class="form-label small text-secondary fw-semibold">Receta M\u00E9dica / Prescripci\u00F3n (Opcional)</label>
                            <textarea name="receta" class="form-control" rows="3" placeholder="Medicamentos, dosis y recomendaciones..."></textarea>
                        </div>'''

c = c.replace(old_diag, new_diag)

with io.open('src/main/webapp/views/dashboard.jsp', 'w', encoding='utf-8') as f:
    f.write(c)
