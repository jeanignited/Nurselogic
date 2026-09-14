import io
import re

with io.open('src/main/webapp/includes/scripts.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

new_funcs = '''function calcularIMC(prefix) {
    let estInput = document.getElementById(prefix + 'estatura') || document.getElementById(prefix + 'estatura_input');
    let pesoInput = document.getElementById(prefix + 'peso') || document.getElementById(prefix + 'peso_input');
    let valEl = document.getElementById(prefix + 'imcValor');
    let estEl = document.getElementById(prefix + 'imcEstado');
    
    if (!estInput || !pesoInput || !valEl || !estEl) return;
    
    let e = parseFloat(estInput.value);
    let p = parseFloat(pesoInput.value);
    
    if (e > 0 && p > 0) {
        let imc = (p / (e * e)).toFixed(1);
        valEl.innerText = imc;
        let estado = 'Normal'; let bg = 'bg-success';
        if (imc < 18.5) { estado = 'Bajo peso'; bg = 'bg-warning text-dark'; }
        else if (imc >= 25 && imc < 30) { estado = 'Sobrepeso'; bg = 'bg-warning text-dark'; }
        else if (imc >= 30) { estado = 'Obesidad'; bg = 'bg-danger'; }
        estEl.innerText = estado;
        estEl.className = 'badge ms-3 px-3 py-2 rounded-pill ' + bg;
    } else {
        valEl.innerText = '0.0';
        estEl.innerText = 'Sin datos';
        estEl.className = 'badge bg-secondary ms-3 px-3 py-2 rounded-pill';
    }
}

function evaluarVitales() {
    let inputs = [
        { id: 'fc_input', badge: 'fc_badge', parse: parseInt, eval: v => v < 60 ? ["Bradicardia", "bg-warning text-dark"] : v > 100 ? ["Taquicardia", "bg-danger"] : ["Normal", "bg-success"] },
        { id: 'fr_input', badge: 'fr_badge', parse: parseInt, eval: v => v < 12 ? ["Bradipnea", "bg-warning text-dark"] : v > 20 ? ["Taquipnea", "bg-danger"] : ["Normal", "bg-success"] },
        { id: 'sat_input', badge: 'sat_badge', parse: parseInt, eval: v => v < 90 ? ["Hipoxia Severa", "bg-danger"] : v < 95 ? ["Hipoxia Leve", "bg-warning text-dark"] : ["Normal", "bg-success"] },
        { id: 'temp_input', badge: 'temp_badge', parse: parseFloat, eval: v => v < 36.5 ? ["Hipotermia", "bg-info text-dark"] : v > 37.5 ? ["Fiebre", "bg-danger"] : ["Normal", "bg-success"] }
    ];

    inputs.forEach(item => {
        let el = document.getElementById(item.id) || document.getElementById('atender_' + item.id);
        let b = document.getElementById(item.badge) || document.getElementById('atender_' + item.badge);
        if (el && el.value && b) {
            let res = item.eval(item.parse(el.value));
            b.innerText = res[0];
            b.className = "badge mt-1 w-100 p-2 text-wrap " + res[1];
        }
    });

    // Presi\u00F3n Arterial
    let pa = document.getElementById('pa_input') || document.getElementById('atender_pa_input');
    let pa_b = document.getElementById('pa_badge') || document.getElementById('atender_pa_badge');
    if (pa && pa.value && pa.value.includes('/') && pa_b) {
        let sist = parseInt(pa.value.split('/')[0]);
        let res = sist < 90 ? ["Hipotensi\u00F3n", "bg-warning text-dark"] : sist > 140 ? ["Hipertensi\u00F3n", "bg-danger"] : ["Normal", "bg-success"];
        pa_b.innerText = res[0];
        pa_b.className = "badge mt-1 w-100 p-2 text-wrap " + res[1];
    }
}
'''

c = re.sub(r'function evaluarVitales\(\) \{.*?(?=function calcularGlasgow)', new_funcs, c, flags=re.DOTALL)

with io.open('src/main/webapp/includes/scripts.jsp', 'w', encoding='utf-8') as f:
    f.write(c)
