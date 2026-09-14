import io
with io.open('src/main/webapp/includes/scripts.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

new_js = '''}

function toggleGlasgow(context) {
    let check = document.getElementById('glasgowCheck' + context);
    let container = document.getElementById('glasgowContainer' + context);
    if(check.checked) {
        container.style.opacity = '0.4';
        container.style.pointerEvents = 'none';
        if(context === 'Nuevo') {
            document.getElementById('glasgowInputNuevo').value = 'NA';
        } else {
            document.getElementById('glasgowTotal').innerText = 'NA';
        }
    } else {
        container.style.opacity = '1';
        container.style.pointerEvents = 'auto';
        if(context === 'Nuevo') {
            calcularGlasgowNuevo();
        } else {
            calcularGlasgow();
        }
    }
}

function calcularGlasgowNuevo() {
    let o = parseInt(document.getElementById('g_ocularNuevo').value);
    let v = parseInt(document.getElementById('g_verbalNuevo').value);
    let m = parseInt(document.getElementById('g_motoraNuevo').value);
    let total = o + v + m;
    let desc = "Normal";
    if (total <= 8) desc = "Trauma Grave";
    else if (total <= 12) desc = "Trauma Moderado";
    document.getElementById('glasgowTotalNuevo').innerText = total + " / 15 (" + desc + ")";
    document.getElementById('glasgowInputNuevo').value = total;
}'''

# find end of calcularGlasgow
import re
pattern = r'(desc\.className = "fw-bold text-success";\s*\}\s*)\}'
c = re.sub(pattern, r'\1' + new_js, c)

with io.open('src/main/webapp/includes/scripts.jsp', 'w', encoding='utf-8') as f:
    f.write(c)
