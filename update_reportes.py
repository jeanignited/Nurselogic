import io
import re

with io.open('src/main/webapp/views/reportes.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

# Add the switch and update HTML
new_html = """            <div class="d-flex gap-2">
                <div class="form-check form-switch d-flex align-items-center me-3">
                    <input class="form-check-input mt-0 me-2" type="checkbox" role="switch" id="switchOcultarResueltosTI" checked onchange="filtrarTicketsTI()" style="cursor:pointer; transform: scale(1.2);">
                    <label class="form-check-label text-theme fw-semibold" for="switchOcultarResueltosTI" style="cursor:pointer;">Ocultar tickets atendidos/cerrados</label>
                </div>
                <select id="filtroNivelTI" class="form-select bg-dark text-white rounded-pill px-3 shadow-sm border-0" style="border: 1px solid rgba(255,255,255,0.1) !important;" onchange="filtrarTicketsTI()">"""

c = c.replace("""            <div class="d-flex gap-2">
                <select id="filtroNivelTI" class="form-select bg-dark text-white rounded-pill px-3 shadow-sm border-0" style="border: 1px solid rgba(255,255,255,0.1) !important;" onchange="filtrarTicketsTI()">""", new_html)

# Add data-estado to ticket-card
c = c.replace("""<div class="col-md-6 col-lg-4 ticket-card" data-nivel="<%= alerta.toLowerCase() %>">""", """<div class="col-md-6 col-lg-4 ticket-card" data-nivel="<%= alerta != null ? alerta.toLowerCase() : "" %>" data-estado="<%= estado != null ? estado.toLowerCase() : "" %>">""")

# Rewrite filtrarTicketsTI
old_js = """function filtrarTicketsTI() {
    let select = document.getElementById('filtroUrgencia');
    if(!select) return;
    let filter = select.value;
    let table = document.getElementById('tablaTicketsTI');
    if(!table) return;
    let trs = table.getElementsByTagName('tr');
    
    for (let i = 1; i < trs.length; i++) {
        let tdUrgencia = trs[i].getElementsByTagName('td')[3];
        if (tdUrgencia) {
            let txtValue = tdUrgencia.textContent || tdUrgencia.innerText;
            if (filter === "Todos" || txtValue.indexOf(filter) > -1) {
                trs[i].style.display = "";
            } else {
                trs[i].style.display = "none";
            }
        }
    }
}"""

new_js = """function filtrarTicketsTI() {
    let select = document.getElementById('filtroNivelTI');
    let switchOcultar = document.getElementById('switchOcultarResueltosTI');
    if(!select || !switchOcultar) return;
    
    let filterNivel = select.value.toLowerCase();
    let hideResolved = switchOcultar.checked;
    
    let cards = document.querySelectorAll('.ticket-card');
    
    cards.forEach(card => {
        let nivel = card.getAttribute('data-nivel') || "";
        let estado = card.getAttribute('data-estado') || "";
        
        let showNivel = (filterNivel === 'todos' || nivel.includes(filterNivel) || (filterNivel === 'critico' && nivel.includes('cr')));
        
        let isResolved = estado.includes('cerrado') || estado.includes('atendido') || estado.includes('resuelto');
        let showEstado = hideResolved ? !isResolved : true;
        
        if(showNivel && showEstado) {
            card.style.display = 'block';
        } else {
            card.style.display = 'none';
        }
    });
}

document.addEventListener("DOMContentLoaded", function() {
    filtrarTicketsTI();
});"""

c = c.replace(old_js, new_js)

with io.open('src/main/webapp/views/reportes.jsp', 'w', encoding='utf-8') as f:
    f.write(c)

print("Updated reportes.jsp with T.I. Filter logic.")
