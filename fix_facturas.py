import io, re

with io.open('src/main/webapp/views/facturas.jsp', 'r', encoding='windows-1252') as f:
    c = f.read()

filters_html = '''
    <div class="d-flex flex-column flex-md-row justify-content-between align-items-md-center mb-4 gap-3">
        <h3 class="m-0 fw-bold"><i class="bi bi-receipt me-2 text-primary"></i>Historial de Facturacion</h3>
        <div class="d-flex align-items-center gap-2">
            <div class="position-relative">
                <i class="bi bi-search position-absolute top-50 start-0 translate-middle-y ms-3 text-secondary"></i>
                <input type="text" id="buscadorFacturas" class="form-control ps-5" placeholder="Buscar por cdula o cliente..." onkeyup="filtrarFacturas()">
            </div>
            <input type="date" id="filtroFechaFactura" class="form-control" onchange="filtrarFacturas()" title="Filtrar por fecha">
        </div>
    </div>
'''

c = re.sub(r'<div class="d-flex flex-column flex-md-row justify-content-between align-items-md-center mb-4 gap-3">\s*<h3 class="m-0 fw-bold"><i class="bi bi-receipt me-2 text-primary"></i>Historial de Facturacion</h3>\s*</div>', filters_html, c)

script_html = '''
<script>
function filtrarFacturas() {
    let inputTxt = document.getElementById('buscadorFacturas').value.toLowerCase();
    let inputDate = document.getElementById('filtroFechaFactura').value;
    let table = document.getElementById('tablaFacturas');
    let trs = table.getElementsByTagName('tr');
    
    for (let i = 1; i < trs.length; i++) {
        let tdCliente = trs[i].getElementsByTagName('td')[2];
        let tdFecha = trs[i].getElementsByTagName('td')[1];
        if (tdCliente && tdFecha) {
            let txtValue = tdCliente.textContent || tdCliente.innerText;
            let dateValue = tdFecha.textContent || tdFecha.innerText; // "YYYY-MM-DD HH:MM"
            
            let matchTxt = txtValue.toLowerCase().indexOf(inputTxt) > -1;
            let matchDate = inputDate === "" || dateValue.startsWith(inputDate);
            
            if (matchTxt && matchDate) {
                trs[i].style.display = "";
            } else {
                trs[i].style.display = "none";
            }
        }
    }
}
</script>
'''
if 'function filtrarFacturas' not in c:
    c = c + script_html

with io.open('src/main/webapp/views/facturas.jsp', 'w', encoding='windows-1252') as f:
    f.write(c)
