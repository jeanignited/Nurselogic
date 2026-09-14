import io
import re

with io.open('src/main/webapp/includes/modals.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

old_html = '''<div class="mb-3">
             <label class="form-label small text-secondary">Fecha y Hora</label>
             <input type="datetime-local" id="citaFechaHora" name="fechaHora" class="form-control" required autocomplete="off">
          </div>'''

new_html = '''<div class="row g-2 mb-3">
             <div class="col-6">
                 <label class="form-label small text-secondary">Fecha</label>
                 <input type="date" name="fecha" class="form-control" required autocomplete="off">
             </div>
             <div class="col-6">
                 <label class="form-label small text-secondary">Hora</label>
                 <input type="time" name="hora" class="form-control" required autocomplete="off">
             </div>
          </div>'''

c = c.replace(old_html, new_html)

with io.open('src/main/webapp/includes/modals.jsp', 'w', encoding='utf-8') as f:
    f.write(c)

print("Updated modals.jsp")
