import io
import re

with io.open('src/main/webapp/includes/scripts.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

m = re.search(r'function abrirModalVerDiagnostico\(paciente, btnEl\).*?m\.show\(\);\s*\}\s*\}', c, re.DOTALL)
if m:
    old_code = m.group(0)
    new_code = r'''function abrirModalVerDiagnostico(paciente, btnEl) {
    document.getElementById('verDiagPaciente').innerText = paciente;
    let rawDiag = btnEl.getAttribute('data-diagnostico');
    if (rawDiag) {
        let cleanDiag = rawDiag.replace(/'C/g, 'C');
        let vals = { talla: '--', peso: '--', imc: '--', fc: '--', pa: '--', fr: '--', sato2: '--', temp: '--', glasgow: '--' };
        
        let regex = /(FC|PA|FR|Temp|IMC|Glasgow|SpO2|SatO2|Talla|Peso):\s*([^\n]+)\n?/gi;
        let match;
        let restText = cleanDiag;
        
        while ((match = regex.exec(cleanDiag)) !== null) {
            let key = match[1].toLowerCase();
            let val = match[2].trim();
            if (key === 'sato2' || key === 'spo2') vals.sato2 = val;
            else if (key === 'temp') vals.temp = val;
            else if (vals[key] !== undefined) vals[key] = val;
            restText = restText.replace(match[0], '');
        }
        
        restText = restText.replace('--- Signos Vitales ---', '').trim();
        
        let finalHtml = `
            <div class="d-flex justify-content-between align-items-center mb-3">
                <h6 class="fw-bold text-primary m-0"><i class="bi bi-heart-pulse-fill text-danger me-2"></i>Evaluaci\u00F3n Cl\u00EDnica (\u00DAltima Consulta)</h6>
            </div>
            <div class="table-responsive">
                <table class="table table-bordered table-dark-custom mb-0" style="background: rgba(255,255,255,0.02); border-color: rgba(255,255,255,0.1);">
                    <tbody>
                        <tr>
                            <td class="fw-bold text-secondary" style="width: 30%;"><i class="bi bi-person-bounding-box me-2 text-info"></i>Antropometr\u00EDa</td>
                            <td class="fw-semibold text-light">${vals.talla} / ${vals.peso} <span class="ms-2 badge bg-secondary">IMC: ${vals.imc}</span></td>
                        </tr>
                        <tr>
                            <td class="fw-bold text-secondary"><i class="bi bi-thermometer-half me-2 text-warning"></i>Temperatura</td>
                            <td class="fw-bold text-warning">${vals.temp}</td>
                        </tr>
                        <tr>
                            <td class="fw-bold text-secondary"><i class="bi bi-heart-pulse-fill me-2 text-danger"></i>Presi\u00F3n Arterial</td>
                            <td class="fw-bold text-info">${vals.pa}</td>
                        </tr>
                        <tr>
                            <td class="fw-bold text-secondary"><i class="bi bi-activity me-2 text-success"></i>Pulso / Sat. O2</td>
                            <td class="fw-bold text-success">${vals.fc} / ${vals.sato2}</td>
                        </tr>
                        <tr>
                            <td class="fw-bold text-secondary"><i class="bi bi-lungs me-2 text-secondary"></i>Frec. Respiratoria</td>
                            <td class="fw-bold text-light">${vals.fr}</td>
                        </tr>
                        <tr>
                            <td class="fw-bold text-secondary"><i class="bi bi-eye me-2 text-primary"></i>Escala Glasgow</td>
                            <td class="fw-bold text-light">${vals.glasgow}</td>
                        </tr>
                        <tr>
                            <td class="fw-bold text-secondary"><i class="bi bi-clipboard2-pulse me-2 text-info"></i>Diagn\u00F3stico Cl\u00EDnico</td>
                            <td class="fw-normal text-light" style="white-space: pre-wrap;">${restText}</td>
                        </tr>
                    </tbody>
                </table>
            </div>`;
            
        document.getElementById('verDiagTexto').innerHTML = finalHtml;
    } else {
        document.getElementById('verDiagTexto').innerText = 'No hay diagn\u00F3stico registrado.';
    }
    document.getElementById('verDiagReceta').innerText = btnEl.getAttribute('data-receta') || 'No aplica';
    
    var mEl = document.getElementById('modalVerDiagnostico');
    if(mEl) {
        var m = bootstrap.Modal.getInstance(mEl) || new bootstrap.Modal(mEl);
        m.show();
    }
}'''
    c = c.replace(old_code, new_code)
    with io.open('src/main/webapp/includes/scripts.jsp', 'w', encoding='utf-8') as f:
        f.write(c)
    print("Replaced abrirModalVerDiagnostico")
else:
    print("Not found")
