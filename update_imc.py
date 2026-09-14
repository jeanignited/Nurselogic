import io
import re

with io.open('src/main/webapp/views/dashboard.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

c = c.replace('oninput="formatearEstatura(this)"', 'oninput="formatearEstatura(this); calcularIMC(\\\'\\\')"')
c = c.replace('oninput="formatearPeso(this)"', 'oninput="formatearPeso(this); calcularIMC(\\\'\\\')"')

with io.open('src/main/webapp/views/dashboard.jsp', 'w', encoding='utf-8') as f:
    f.write(c)

with io.open('src/main/webapp/includes/modals.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

c = c.replace('oninput="formatearEstatura(this)"', 'oninput="formatearEstatura(this); calcularIMC(\\\'atender_\\\')"')
c = c.replace('oninput="formatearPeso(this)"', 'oninput="formatearPeso(this); calcularIMC(\\\'atender_\\\')"')

with io.open('src/main/webapp/includes/modals.jsp', 'w', encoding='utf-8') as f:
    f.write(c)

# Add function to scripts.jsp
with io.open('src/main/webapp/includes/scripts.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

imc_func = '''function calcularIMC(prefix) {
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
'''
if 'function calcularIMC' not in c:
    c = c.replace('function evaluarVitales() {', imc_func + '\nfunction evaluarVitales() {')
    with io.open('src/main/webapp/includes/scripts.jsp', 'w', encoding='utf-8') as f:
        f.write(c)
