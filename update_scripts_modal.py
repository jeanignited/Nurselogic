import io
import re

with io.open('src/main/webapp/includes/scripts.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

# Replace the text assignment for verDiagTexto with parsed badges
old_func = "document.getElementById('verDiagTexto').innerText = btnEl.getAttribute('data-diagnostico');"

new_func = '''let rawDiag = btnEl.getAttribute('data-diagnostico');
if (rawDiag) {
    let formattedDiag = rawDiag.replace(/(FC:|PA:|FR:|Temp:|IMC:|Glasgow:|SpO2:|Talla:|Peso:)\s*([^\\n]+)/gi, '<span class="badge bg-secondary me-2 mb-2 px-3 py-2" style="font-size: 0.85rem;"><i class="bi bi-activity text-info me-1"></i> </span>');
    formattedDiag = formattedDiag.replace(/\\n/g, '<br>');
    document.getElementById('verDiagTexto').innerHTML = '<div class="card bg-dark border-secondary p-3 text-light" style="line-height: 1.8;">' + formattedDiag + '</div>';
} else {
    document.getElementById('verDiagTexto').innerText = '';
}'''

c = c.replace(old_func, new_func)

with io.open('src/main/webapp/includes/scripts.jsp', 'w', encoding='utf-8') as f:
    f.write(c)

print("scripts.jsp updated.")
