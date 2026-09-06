import sys

with open('src/main/webapp/includes/scripts.jsp', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove the incorrectly appended text at the end
# The appended text starts with "// Evaluacion de Signos Vitales"
if "// Evaluacion de Signos Vitales" in content:
    idx = content.rfind("// Evaluacion de Signos Vitales")
    # Also find where </script> is BEFORE that text
    end_script_idx = content.rfind("</script>", 0, idx)
    
    clean_content = content[:end_script_idx] # everything inside the script block
    
    js = '''
// Evaluacion de Signos Vitales
function evaluarVitales() {
    const fc = parseInt(document.getElementById('fc_input').value);
    const pa = document.getElementById('pa_input').value;
    const fr = parseInt(document.getElementById('fr_input').value);
    const sat = parseInt(document.getElementById('sat_input').value);
    const temp = parseFloat(document.getElementById('temp_input').value);

    let fcBadge = document.getElementById('fc_badge');
    if (!isNaN(fc)) {
        if (fc < 60) { fcBadge.className = 'badge mt-1 w-100 p-2 text-wrap bg-warning text-dark'; fcBadge.innerText = 'Bradicardia'; }
        else if (fc > 100) { fcBadge.className = 'badge mt-1 w-100 p-2 text-wrap bg-danger'; fcBadge.innerText = 'Taquicardia'; }
        else { fcBadge.className = 'badge mt-1 w-100 p-2 text-wrap bg-success'; fcBadge.innerText = 'Normal'; }
    } else { fcBadge.className = 'badge mt-1 w-100 p-2 text-wrap bg-secondary'; fcBadge.innerText = 'Esperando...'; }

    let paBadge = document.getElementById('pa_badge');
    if (pa && pa.includes('/')) {
        let parts = pa.split('/');
        let sist = parseInt(parts[0]);
        let diast = parseInt(parts[1]);
        if (!isNaN(sist) && !isNaN(diast)) {
            if (sist < 90 || diast < 60) { paBadge.className = 'badge mt-1 w-100 p-2 text-wrap bg-warning text-dark'; paBadge.innerText = 'Hipotensión'; }
            else if (sist > 130 || diast > 80) { paBadge.className = 'badge mt-1 w-100 p-2 text-wrap bg-danger'; paBadge.innerText = 'Hipertensión'; }
            else { paBadge.className = 'badge mt-1 w-100 p-2 text-wrap bg-success'; paBadge.innerText = 'Normal'; }
        }
    } else { paBadge.className = 'badge mt-1 w-100 p-2 text-wrap bg-secondary'; paBadge.innerText = 'Esperando...'; }

    let frBadge = document.getElementById('fr_badge');
    if (!isNaN(fr)) {
        if (fr < 12) { frBadge.className = 'badge mt-1 w-100 p-2 text-wrap bg-warning text-dark'; frBadge.innerText = 'Bradipnea'; }
        else if (fr > 20) { frBadge.className = 'badge mt-1 w-100 p-2 text-wrap bg-danger'; frBadge.innerText = 'Taquipnea'; }
        else { frBadge.className = 'badge mt-1 w-100 p-2 text-wrap bg-success'; frBadge.innerText = 'Normal'; }
    } else { frBadge.className = 'badge mt-1 w-100 p-2 text-wrap bg-secondary'; frBadge.innerText = 'Esperando...'; }

    let satBadge = document.getElementById('sat_badge');
    if (!isNaN(sat)) {
        if (sat < 95) { satBadge.className = 'badge mt-1 w-100 p-2 text-wrap bg-danger'; satBadge.innerText = 'Hipoxia'; }
        else { satBadge.className = 'badge mt-1 w-100 p-2 text-wrap bg-success'; satBadge.innerText = 'Normal'; }
    } else { satBadge.className = 'badge mt-1 w-100 p-2 text-wrap bg-secondary'; satBadge.innerText = 'Esperando...'; }

    let tempBadge = document.getElementById('temp_badge');
    if (!isNaN(temp)) {
        if (temp < 36.5) { tempBadge.className = 'badge mt-1 w-100 p-2 text-wrap bg-info text-dark'; tempBadge.innerText = 'Hipotermia'; }
        else if (temp > 37.5) { tempBadge.className = 'badge mt-1 w-100 p-2 text-wrap bg-danger'; tempBadge.innerText = 'Fiebre'; }
        else { tempBadge.className = 'badge mt-1 w-100 p-2 text-wrap bg-success'; tempBadge.innerText = 'Normal'; }
    } else { tempBadge.className = 'badge mt-1 w-100 p-2 text-wrap bg-secondary'; tempBadge.innerText = 'Esperando...'; }
}

function calcularGlasgow() {
    const o = parseInt(document.getElementById('g_ocular').value);
    const v = parseInt(document.getElementById('g_verbal').value);
    const m = parseInt(document.getElementById('g_motora').value);
    const t = o + v + m;
    document.getElementById('glasgowTotal').innerText = t + ' / 15';
    let desc = document.getElementById('glasgowDesc');
    if (t === 15) { desc.innerText = 'Normal'; desc.className = 'fw-bold text-success'; }
    else if (t >= 13) { desc.innerText = 'Trauma Leve'; desc.className = 'fw-bold text-warning'; }
    else if (t >= 9) { desc.innerText = 'Trauma Moderado'; desc.className = 'fw-bold text-warning'; }
    else { desc.innerText = 'Trauma Grave (Coma)'; desc.className = 'fw-bold text-danger'; }
}

function prepararYEnviarConsulta() {
    let diag = document.getElementById('diagnosticoFinal');
    let baseDiag = diag.value.split('\\n--- Signos Vitales ---')[0];
    
    let vitalesStr = "\\n--- Signos Vitales ---\\n" +
        "FC: " + document.getElementById('fc_input').value + " lpm\\n" +
        "PA: " + document.getElementById('pa_input').value + "\\n" +
        "FR: " + document.getElementById('fr_input').value + " rpm\\n" +
        "SatO2: " + document.getElementById('sat_input').value + "%\\n" +
        "Temp: " + document.getElementById('temp_input').value + " °C\\n" +
        "Glasgow: " + document.getElementById('glasgowTotal').innerText;
        
    diag.value = baseDiag + vitalesStr;
    document.getElementById('formAtenderCita').submit();
}
'''
    new_content = clean_content + js + "\n</script>\n"
    with open('src/main/webapp/includes/scripts.jsp', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Fixed scripts.jsp")
else:
    print("Could not find appended text")
