import io
import re

with io.open('src/main/webapp/views/dashboard.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

# Replace encoding line
c = re.sub(r'<%@ page pageEncoding="UTF-8" %>', '<%@ page contentType="text/html; charset=UTF-8" pageEncoding="UTF-8" %>', c, count=1)

# Switch checked
c = c.replace('<input class="form-check-input" type="checkbox" id="switchOcultarHistorial">', '<input class="form-check-input" type="checkbox" id="switchOcultarHistorial" checked>')

# Medico null patch (Citas)
old_med_citas = '<%= cita.get("medico") %>'
new_med = '<%= (cita.get("medico") == null || cita.get("medico").equals("null") || cita.get("medico").trim().isEmpty()) ? "<span class=\\\"text-muted fst-italic\\\">Por asignar</span>" : cita.get("medico") %>'
c = c.replace(old_med_citas, new_med)

# Medico null patch (Resultados)
old_med_res = '<%= res.get("medico") %>'
new_med_res = '<%= (res.get("medico") == null || res.get("medico").equals("null") || res.get("medico").trim().isEmpty()) ? "<span class=\\\"text-muted fst-italic\\\">Por asignar</span>" : res.get("medico") %>'
c = c.replace(old_med_res, new_med_res)

# Medico null patch (Recetas)
old_med_rec = '<%= rec.get("medico") %>'
new_med_rec = '<%= (rec.get("medico") == null || rec.get("medico").equals("null") || rec.get("medico").trim().isEmpty()) ? "<span class=\\\"text-muted fst-italic\\\">Por asignar</span>" : rec.get("medico") %>'
c = c.replace(old_med_rec, new_med_rec)

# Recetas detalles reales
# Changing Diagnostico to Receta details
old_rec_diag = '<th class="py-3 px-4 fw-semibold text-secondary">Diagn&oacute;stico</th>'
new_rec_diag = '<th class="py-3 px-4 fw-semibold text-secondary">Medicamento / Indicaciones</th>'
c = c.replace(old_rec_diag, new_rec_diag)

old_rec_det = '<td class="py-3 px-4"><%= rec.get("diagnostico") %></td>'
new_rec_det = '<td class="py-3 px-4"><%= (rec.get("receta") != null && !rec.get("receta").equals("null")) ? rec.get("receta") : rec.get("diagnostico") %></td>'
c = c.replace(old_rec_det, new_rec_det)

# JS switch filter
old_js_end = '});\n        </script>'
new_js = '''
                const switchCitas = document.getElementById('switchOcultarHistorial');
                if(switchCitas) {
                    function filtrarHistorial() {
                        const tbody = document.querySelector('#vista-citas tbody');
                        if(!tbody) return;
                        const trs = tbody.querySelectorAll('tr');
                        trs.forEach(tr => {
                            const txt = tr.textContent.toUpperCase();
                            if (txt.includes('ATENDIDO') || txt.includes('CANCELADO') || txt.includes('DESPACHADO')) {
                                if (switchCitas.checked) {
                                    tr.classList.add('d-none');
                                } else {
                                    tr.classList.remove('d-none');
                                }
                            }
                        });
                    }
                    switchCitas.addEventListener('change', filtrarHistorial);
                    filtrarHistorial();
                }
            });
        </script>'''
c = c.replace(old_js_end, new_js)

with io.open('src/main/webapp/views/dashboard.jsp', 'w', encoding='utf-8') as f:
    f.write(c)

print("dashboard.jsp updated.")
