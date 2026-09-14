# -*- coding: utf-8 -*-
import io
import re

with io.open('src/main/webapp/includes/scripts.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

m2 = re.search(r'function abrirModalVerDiagnosticoCama\(paciente, btnEl\).*?m\.show\(\);\s*\}\s*\}', c, re.DOTALL)

new_code_2 = r'''function abrirModalVerDiagnosticoCama(paciente, btnEl) {
    document.getElementById('verDiagPaciente').innerText = paciente;
    let rawDiag = btnEl.getAttribute('data-diagnostico');
    let recetaText = 'No aplica (Hospitalizaci\u00F3n)';
    if (!rawDiag) {
        document.getElementById('verDiagTexto').innerText = 'No hay diagn\u00F3stico';
        return;
    }
    
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
    
    let aiHtml = '';
    if (vals.pa && vals.pa !== '--') {
        let parts = vals.pa.split('/');
        if (parts.length === 2 && parseInt(parts[0]) >= 140) {
            aiHtml += '<div class="alert alert-warning py-2 mb-2 border-0" style="background: rgba(245,158,11,0.1);"><i class="bi bi-heart-pulse-fill me-2"></i>Hipertensi\u00F3n detectada. Monitorear signos vitales.</div>';
        }
    }
    if (aiHtml === '') {
        aiHtml = '<div class="alert alert-success py-2 mb-0 border-0" style="background: rgba(16,185,129,0.1);"><i class="bi bi-check-circle-fill me-2"></i>Par\u00E1metros estables. Ninguna alerta cl\u00EDnica urgente.</div>';
    }

    let finalHtml = `
    <div class="d-flex justify-content-between align-items-center mb-3">
        <h6 class="fw-bold text-primary m-0"><i class="bi bi-heart-pulse-fill text-danger me-2"></i>Evaluaci\u00F3n Cl\u00EDnica (Cama)</h6>
    </div>
    <div class="table-responsive">
        <table class="table table-bordered table-dark-custom mb-4" style="background: rgba(255,255,255,0.02); border-color: rgba(255,255,255,0.1);">
            <tbody>
                <tr>
                    <td class="fw-bold text-secondary" style="width: 30%;"><i class="bi bi-person-bounding-box me-2 text-info"></i>Antropometr\u00EDa</td>
                    <td class="fw-semibold text-light">\${vals.talla} / \${vals.peso} <span class="ms-2 badge bg-secondary">IMC: \${vals.imc}</span></td>
                </tr>
                <tr>
                    <td class="fw-bold text-secondary"><i class="bi bi-thermometer-half me-2 text-warning print-text-black"></i>Temperatura</td>
                    <td class="fw-bold text-warning print-text-black">\${vals.temp}</td>
                </tr>
                <tr>
                    <td class="fw-bold text-secondary"><i class="bi bi-heart-pulse-fill me-2 text-danger print-text-black"></i>Presi\u00F3n Arterial</td>
                    <td class="fw-bold text-info print-text-black">\${vals.pa}</td>
                </tr>
                <tr>
                    <td class="fw-bold text-secondary"><i class="bi bi-activity me-2 text-success print-text-black"></i>Pulso / Sat. O2</td>
                    <td class="fw-bold text-success print-text-black">\${vals.fc} / \${vals.sato2}</td>
                </tr>
                <tr>
                    <td class="fw-bold text-secondary"><i class="bi bi-lungs me-2 text-secondary"></i>Frec. Respiratoria</td>
                    <td class="fw-bold text-light">\${vals.fr}</td>
                </tr>
                <tr>
                    <td class="fw-bold text-secondary"><i class="bi bi-eye me-2 text-primary print-text-black"></i>Escala Glasgow</td>
                    <td class="fw-bold text-light">\${vals.glasgow}</td>
                </tr>
                <tr>
                    <td class="fw-bold text-secondary"><i class="bi bi-clipboard2-pulse me-2 text-info print-text-black"></i>Diagn\u00F3stico Cl\u00EDnico</td>
                    <td class="fw-normal text-light" style="white-space: pre-wrap;">\${restText}</td>
                </tr>
                <tr>
                    <td class="fw-bold text-secondary"><i class="bi bi-capsule me-2 text-success print-text-black"></i>Receta / Prescripci\u00F3n</td>
                    <td class="fw-normal text-light" style="white-space: pre-wrap;">\${recetaText}</td>
                </tr>
            </tbody>
        </table>
    </div>
    <h6 class="fw-bold text-info mb-3"><i class="bi bi-cpu me-2"></i>Inteligencia Cl\u00EDnica</h6>
    \${aiHtml}
    `;
    
    document.getElementById('verDiagTexto').innerHTML = finalHtml;
    
    var mEl = document.getElementById('modalVerDiagnostico');
    if(mEl) {
        var m = bootstrap.Modal.getInstance(mEl) || new bootstrap.Modal(mEl);
        m.show();
    }
}'''

c = c.replace(m2.group(0), new_code_2)

with io.open('src/main/webapp/includes/scripts.jsp', 'w', encoding='utf-8') as f:
    f.write(c)
print("Updated abrirModalVerDiagnosticoCama")
