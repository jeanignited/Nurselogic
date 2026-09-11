import io, re

with io.open('src/main/webapp/views/reportes.jsp', 'r', encoding='windows-1252') as f:
    c = f.read()

# Add Urgency Filter
search_str = '<h5 class="fw-bold m-0"><i class="bi bi-headset me-2 text-warning"></i>Bandeja de Entrada - Soporte T.I.</h5>'
replace_str = '''<div class="d-flex justify-content-between align-items-center w-100">
    <h5 class="fw-bold m-0"><i class="bi bi-headset me-2 text-warning"></i>Bandeja de Entrada - Soporte T.I.</h5>
    <select id="filtroUrgencia" class="form-select form-select-sm w-auto" onchange="filtrarTicketsTI()">
        <option value="Todos">Todos los niveles</option>
        <option value="Baja">Prioridad Baja</option>
        <option value="Media">Prioridad Media</option>
        <option value="Alta">Prioridad Alta</option>
        <option value="Critica">Prioridad Crtica</option>
    </select>
</div>'''
c = c.replace(search_str, replace_str)

# Add Javascript for filtering
js_code = '''
<script>
function filtrarTicketsTI() {
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
}
function expandirDescTI(btn) {
    let div = btn.previousElementSibling;
    if (div.style.maxHeight === "none") {
        div.style.maxHeight = "40px";
        btn.innerHTML = "Ver ms";
    } else {
        div.style.maxHeight = "none";
        btn.innerHTML = "Ver menos";
    }
}
</script>
'''
if 'function filtrarTicketsTI' not in c:
    c = c + js_code

with io.open('src/main/webapp/views/reportes.jsp', 'w', encoding='windows-1252') as f:
    f.write(c)
