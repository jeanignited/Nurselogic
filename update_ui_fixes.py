import io
import re

# 1. Update reportes.jsp (Layout and onchange)
with io.open('src/main/webapp/views/reportes.jsp', 'r', encoding='utf-8') as f:
    rep = f.read()

# Update container to include w-100
rep = rep.replace('<div class="d-flex justify-content-between align-items-center mb-4 flex-wrap gap-3">', '<div class="d-flex flex-wrap justify-content-between align-items-center gap-3 w-100 mb-4">')

# Update onchange
rep = rep.replace('id="switchOcultarResueltosTI" checked onchange="filtrarTicketsTI()"', 'id="switchOcultarResueltosTI" checked onchange="filtrarTicketsTI(this.checked)"')

# Remove existing script in reportes.jsp to move it to scripts.jsp
# (The user wants the logic in scripts.jsp, so I'll just remove the old function if it exists)
old_js = """function filtrarTicketsTI(checked) {
    let select = document.getElementById('filtroNivelTI');
    let switchOcultar = document.getElementById('switchOcultarResueltosTI');
    
    let filterNivel = select ? select.value.toLowerCase() : 'todos';
    let hideResolved = (typeof checked === 'boolean') ? checked : (switchOcultar ? switchOcultar.checked : true);
    
    let cards = document.querySelectorAll('.ticket-card');
    
    cards.forEach(card => {
        let nivel = (card.getAttribute('data-nivel') || "").toLowerCase();
        let estado = (card.getAttribute('data-estado') || "").toLowerCase();
        let textContent = (card.innerText || card.textContent).toLowerCase();
        
        let showNivel = (filterNivel === 'todos' || nivel.includes(filterNivel) || (filterNivel === 'critico' && nivel.includes('cr')));
        
        let isResolved = estado.includes('cerrado') || estado.includes('atendido') || estado.includes('resuelto') || textContent.includes('cerrado') || textContent.includes('atendido') || textContent.includes('resuelto');
        let showEstado = hideResolved ? !isResolved : true;
        
        if (showNivel && showEstado) {
            card.style.display = '';
        } else {
            card.style.display = 'none';
        }
    });
}"""

rep = rep.replace(old_js, "")

with io.open('src/main/webapp/views/reportes.jsp', 'w', encoding='utf-8') as f:
    f.write(rep)


# 2. Update scripts.jsp (SweetAlert colors and the new function)
with io.open('src/main/webapp/includes/scripts.jsp', 'r', encoding='utf-8') as f:
    scripts = f.read()

# Fix mostrarAlertaSoporte
old_swal = """function mostrarAlertaSoporte() {
    let isDark = document.body.classList.contains('dark-mode') || (document.documentElement.getAttribute('data-bs-theme') !== 'light' && document.documentElement.getAttribute('data-bs-theme') === 'dark');
    let isLight = document.documentElement.getAttribute('data-bs-theme') === 'light' || (!isDark && !document.body.classList.contains('dark-mode'));
    Swal.fire({
        title: '\u00bfNecesitas ayuda con NurseLogic?',
        html: 'Si tienes problemas con tu cuenta, dudas sobre tu historial m\u00e9dico o experimentas alg\u00fan error, escr\u00edbenos a:<br><br><b>nurselogicsoporte@gmail.com</b><br><br>Nuestro equipo te contactar\u00e1 a la brevedad.',
        icon: 'info',
        background: document.body.classList.contains('dark-mode') ? '#1e293b' : (isLight ? '#ffffff' : '#1e293b'),
        color: document.body.classList.contains('dark-mode') ? '#ffffff' : (isLight ? '#000000' : '#ffffff'),
        confirmButtonText: 'Entendido',
        confirmButtonColor: 'var(--accent)'
    });
}"""

# Fallback pattern if previous script fails to find it exactly
import re
scripts = re.sub(r'function mostrarAlertaSoporte\(\) \{[\s\S]*?\}\);[\s\n]*\}', """function mostrarAlertaSoporte() {
    Swal.fire({
        title: '\u00bfNecesitas ayuda con NurseLogic?',
        html: 'Si tienes problemas con tu cuenta, dudas sobre tu historial m\u00e9dico o experimentas alg\u00fan error, escr\u00edbenos a:<br><br><b>nurselogicsoporte@gmail.com</b><br><br>Nuestro equipo te contactar\u00e1 a la brevedad.',
        icon: 'info',
        background: document.body.classList.contains('dark-mode') ? '#1e293b' : '#ffffff',
        color: document.body.classList.contains('dark-mode') ? '#ffffff' : '#000000',
        confirmButtonText: 'Entendido',
        confirmButtonColor: 'var(--accent)'
    });
}""", scripts)

# Add filtrarTicketsTI
new_filtrar = """
function filtrarTicketsTI(checked) {
    let cards = document.querySelectorAll('.ticket-card');
    cards.forEach(card => {
        let content = (card.innerHTML || card.innerText || "").toLowerCase();
        let isResolved = content.includes('cerrado') || content.includes('resuelto') || content.includes('atendido');
        
        if (checked && isResolved) {
            card.style.display = 'none';
        } else {
            card.style.display = 'block';
        }
    });
}
</script>"""

scripts = scripts.replace('</script>', new_filtrar)

with io.open('src/main/webapp/includes/scripts.jsp', 'w', encoding='utf-8') as f:
    f.write(scripts)

print("Modificaciones realizadas con exito.")
