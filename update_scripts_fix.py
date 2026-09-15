import io
import re

with io.open('src/main/webapp/includes/scripts.jsp', 'r', encoding='utf-8') as f:
    scripts = f.read()

# Fix SweetAlert dynamic check for this app (using data-bs-theme attribute)
old_swal = """function mostrarAlertaSoporte() {
    Swal.fire({
        title: '\u00bfNecesitas ayuda con NurseLogic?',
        html: 'Si tienes problemas con tu cuenta, dudas sobre tu historial m\u00e9dico o experimentas alg\u00fan error, escr\u00edbenos a:<br><br><b>nurselogicsoporte@gmail.com</b><br><br>Nuestro equipo te contactar\u00e1 a la brevedad.',
        icon: 'info',
        background: document.body.classList.contains('dark-mode') ? '#1e293b' : '#ffffff',
        color: document.body.classList.contains('dark-mode') ? '#ffffff' : '#000000',
        confirmButtonText: 'Entendido',
        confirmButtonColor: 'var(--accent)'
    });
}"""

new_swal = """function mostrarAlertaSoporte() {
    let isDark = document.documentElement.getAttribute('data-bs-theme') === 'dark';
    Swal.fire({
        title: '\u00bfNecesitas ayuda con NurseLogic?',
        html: 'Si tienes problemas con tu cuenta, dudas sobre tu historial m\u00e9dico o experimentas alg\u00fan error, escr\u00edbenos a:<br><br><b>nurselogicsoporte@gmail.com</b><br><br>Nuestro equipo te contactar\u00e1 a la brevedad.',
        icon: 'info',
        background: isDark ? '#1e293b' : '#ffffff',
        color: isDark ? '#ffffff' : '#000000',
        confirmButtonText: 'Entendido',
        confirmButtonColor: 'var(--accent)'
    });
}"""

scripts = scripts.replace(old_swal, new_swal)

# Fix filtrarTicketsTI
old_filtrar = """function filtrarTicketsTI(checked) {
    if (typeof checked === 'undefined') {
        let switchEl = document.getElementById('switchOcultarResueltosTI');
        checked = switchEl ? switchEl.checked : true;
    }
    
    let select = document.getElementById('filtroNivelTI');
    let filterNivel = select ? select.value.toLowerCase() : 'todos';
    
    let cards = document.querySelectorAll('.ticket-card');
    cards.forEach(card => {
        let nivel = (card.getAttribute('data-nivel') || "").toLowerCase();
        let content = (card.innerHTML || card.innerText || "").toLowerCase();
        let isResolved = content.includes('cerrado') || content.includes('resuelto') || content.includes('atendido');
        
        let showNivel = (filterNivel === 'todos' || nivel.includes(filterNivel) || (filterNivel === 'critico' && nivel.includes('cr')));
        let showEstado = checked ? !isResolved : true;
        
        if (showNivel && showEstado) {
            card.style.display = 'block'; // o ''
        } else {
            card.style.display = 'none';
        }
    });
}"""

new_filtrar = """function filtrarTicketsTI(checked) {
    if (typeof checked === 'undefined') {
        let switchEl = document.getElementById('switchOcultarResueltosTI');
        checked = switchEl ? switchEl.checked : true;
    }
    
    let select = document.getElementById('filtroNivelTI');
    let filterNivel = select ? select.value.toLowerCase() : 'todos';
    
    let cards = document.querySelectorAll('.ticket-card');
    cards.forEach(card => {
        let nivel = (card.getAttribute('data-nivel') || "").toLowerCase();
        let estado = (card.getAttribute('data-estado') || "").toLowerCase();
        
        let isResolved = estado === 'cerrado' || estado === 'resuelto' || estado === 'atendido';
        
        let showNivel = (filterNivel === 'todos' || nivel.includes(filterNivel) || (filterNivel === 'critico' && nivel.includes('cr')));
        let showEstado = checked ? !isResolved : true;
        
        if (showNivel && showEstado) {
            card.style.display = 'block';
        } else {
            card.style.display = 'none';
        }
    });
}"""

scripts = scripts.replace(old_filtrar, new_filtrar)

with io.open('src/main/webapp/includes/scripts.jsp', 'w', encoding='utf-8') as f:
    f.write(scripts)
