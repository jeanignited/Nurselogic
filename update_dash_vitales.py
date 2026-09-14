import io
import re

with io.open('src/main/webapp/views/dashboard.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

# I need to update the Signos Vitales section in formRegistroPaciente
old_vitales = '''<div class="row g-4">

                        <div class="col-md-3">

                            <label class="form-label small text-secondary fw-semibold">Temp (\\u00B0C)</label>

                            <input type="text" id="temp" name="temperatura" class="form-control" maxlength="4" oninput="formatearTemperatura(this)" placeholder="Ej: 36.5" required autocomplete="off">

                            <div id="alertaTemp" class="small mt-1 fw-bold text-danger d-none"></div>

                        </div>

                        <div class="col-md-3">

                            <label class="form-label small text-secondary fw-semibold">Presi\\u00F3n Arterial (Ej: 120/80)</label>

                            <input type="text" id="presion" name="presion" class="form-control" maxlength="7" oninput="formatearPresion(this)" pattern="\\d{2,3}/\\d{2,3}" title="Debe usar el formato 120/80" placeholder="Ej: 120/80" required autocomplete="off">

                        </div>

                        <div class="col-md-3">

                            <label class="form-label small text-secondary fw-semibold">Frec. Cardiaca (LPM)</label>

                            <input type="text" id="fc" name="fc" class="form-control" oninput="formatearFC(this)" placeholder="Ej: 80" required autocomplete="off">

                            <div id="alertaFc" class="small mt-1 fw-bold text-danger d-none"></div>

                        </div>

                        <div class="col-md-3">

                            <label class="form-label small text-secondary fw-semibold">Saturaci\\u00F3n O2 (%)</label>

                            <input type="text" id="sat" name="sat" class="form-control" oninput="formatearSat(this)" placeholder="Ej: 98" required autocomplete="off">

                            <div id="alertaSat" class="small mt-1 fw-bold text-danger d-none"></div>

                        </div>

                    </div>'''

new_vitales = '''<div class="row g-4">
                        <div class="col-md-4">
                            <label class="form-label small text-secondary fw-semibold">Temp (\\u00B0C)</label>
                            <input type="text" id="temp_input" name="temperatura" class="form-control" maxlength="4" oninput="formatearTemperatura(this); if(typeof evaluarVitales === 'function') evaluarVitales();" placeholder="Ej: 36.5" required autocomplete="off">
                            <div id="temp_badge" class="badge bg-secondary mt-1 w-100">Esperando...</div>
                        </div>
                        <div class="col-md-4">
                            <label class="form-label small text-secondary fw-semibold">Presi\\u00F3n Arterial (Sist/Diast)</label>
                            <input type="text" id="pa_input" name="presion" class="form-control" maxlength="7" oninput="formatearPresion(this); if(typeof evaluarVitales === 'function') evaluarVitales();" pattern="\\d{2,3}/\\d{2,3}" placeholder="Ej: 120/80" required autocomplete="off">
                            <div id="pa_badge" class="badge bg-secondary mt-1 w-100">Esperando...</div>
                        </div>
                        <div class="col-md-4">
                            <label class="form-label small text-secondary fw-semibold">Frec. Cardiaca (LPM)</label>
                            <input type="text" id="fc_input" name="fc" class="form-control" oninput="formatearFC(this); if(typeof evaluarVitales === 'function') evaluarVitales();" placeholder="Ej: 80" required autocomplete="off">
                            <div id="fc_badge" class="badge bg-secondary mt-1 w-100">Esperando...</div>
                        </div>
                        <div class="col-md-6">
                            <label class="form-label small text-secondary fw-semibold">Frec. Respiratoria (RPM)</label>
                            <input type="text" id="fr_input" name="fr" class="form-control" oninput="formatearFR(this); if(typeof evaluarVitales === 'function') evaluarVitales();" placeholder="Ej: 16" required autocomplete="off">
                            <div id="fr_badge" class="badge bg-secondary mt-1 w-100">Esperando...</div>
                        </div>
                        <div class="col-md-6">
                            <label class="form-label small text-secondary fw-semibold">Saturaci\\u00F3n O2 (%)</label>
                            <input type="text" id="sat_input" name="sat" class="form-control" oninput="formatearSat(this); if(typeof evaluarVitales === 'function') evaluarVitales();" placeholder="Ej: 98" required autocomplete="off">
                            <div id="sat_badge" class="badge bg-secondary mt-1 w-100">Esperando...</div>
                        </div>
                    </div>'''
# Using regex to replace the block
m = re.search(r'<div class="row g-4">\s*<div class="col-md-3">\s*<label class="form-label small text-secondary fw-semibold">Temp.*?</div>\s*</div>', c, re.DOTALL)
if m:
    c = c.replace(m.group(0), new_vitales)
    with io.open('src/main/webapp/views/dashboard.jsp', 'w', encoding='utf-8') as f:
        f.write(c)
    print("Dashboard vitales updated")
else:
    print("Vitales block not found in dashboard.jsp")
