# -*- coding: utf-8 -*-
import io
import re

with io.open('src/main/webapp/includes/scripts.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

new_logic = '''let cleanDiag = rawDiag.replace(/Â°C/g, '°C');
    let vitalSignsHtml = '';
    let restText = cleanDiag;
    
    let regex = /(FC:|PA:|FR:|Temp:|IMC:|Glasgow:|SpO2:|Talla:|Peso:)\\s*([^\\n]+)\\n?/gi;
    let match;
    while ((match = regex.exec(cleanDiag)) !== null) {
         vitalSignsHtml += '<div class="col-md-4 col-6 mb-2"><i class="bi bi-activity text-info me-1"></i><span class="text-light fw-semibold">' + match[1] + '</span> <span class="text-light opacity-75">' + match[2] + '</span></div>';
         restText = restText.replace(match[0], '');
    }
    
    let finalHtml = '';
    if (vitalSignsHtml !== '') {
         finalHtml += '<div class="row mb-3">' + vitalSignsHtml + '</div><hr class="border-secondary opacity-25">';
    }
    finalHtml += restText.replace(/\\n/g, '<br>');
    document.getElementById('verDiagTexto').innerHTML = '<div class="card bg-dark border-secondary p-3 text-light" style="line-height: 1.8;">' + finalHtml + '</div>';'''

c = re.sub(r'let formattedDiag = rawDiag\.replace.*?</div>\';', lambda m: new_logic, c, flags=re.DOTALL)

with io.open('src/main/webapp/includes/scripts.jsp', 'w', encoding='utf-8') as f:
    f.write(c)

print("scripts.jsp replacement done.")
