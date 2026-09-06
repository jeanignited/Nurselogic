<%@ page pageEncoding="UTF-8" %>
<%@ page import="java.util.List,java.util.Map" %>
<%@ page import="com.nurselogic.model.*" %>
<%
    boolean isAdmin        = Boolean.TRUE.equals(request.getAttribute("isAdmin"));
    boolean isPaciente     = Boolean.TRUE.equals(request.getAttribute("isPaciente"));
    boolean isFarmaceutico = Boolean.TRUE.equals(request.getAttribute("isFarmaceutico"));
    boolean permPac        = Boolean.TRUE.equals(request.getAttribute("permPac"));
    boolean permMed        = Boolean.TRUE.equals(request.getAttribute("permMed"));
    boolean permCat        = Boolean.TRUE.equals(request.getAttribute("permCat"));
    boolean canSellStock   = Boolean.TRUE.equals(request.getAttribute("canSellStock"));
    boolean canManageStock = Boolean.TRUE.equals(request.getAttribute("canManageStock"));
    boolean permCitas      = Boolean.TRUE.equals(request.getAttribute("permCitas"));
    boolean permUsuarios   = Boolean.TRUE.equals(request.getAttribute("permUsuarios"));
    String correoLogueado  = (String) request.getAttribute("correoLogueado");
    String rolUsuario      = (String) request.getAttribute("rolUsuario");
%><%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%@ page import="java.util.List" %>
<%@ page import="java.util.Map" %>
<%@ page import="com.nurselogic.model.Factura" %>
<%@ page import="com.nurselogic.model.FacturaDetalle" %>

<div id="facturas" class="vista-activa d-none">
    <div class="d-flex flex-column flex-md-row justify-content-between align-items-md-center mb-4 gap-3">
        <h3 class="m-0 fw-bold"><i class="bi bi-receipt me-2 text-primary"></i>Historial de Facturacion</h3>
        <div class="d-flex align-items-center gap-2" style="width: 100%; max-width: 450px;">
            <div class="position-relative flex-grow-1">
                <i class="bi bi-search position-absolute top-50 start-0 translate-middle-y ms-3 text-secondary"></i>
                <input type="text" id="buscadorFacturas" class="form-control ps-5" placeholder="Buscar factura..." onkeyup="filtrarFacturas()">
            </div>
            <a href="exportCsv?tipo=facturas" class="btn btn-outline-success text-nowrap rounded-pill px-3 py-2 shadow-sm" title="Descargar Excel/CSV"><i class="bi bi-file-earmark-spreadsheet-fill me-1"></i>Exportar</a>
        </div>
    </div>
    
    <div class="formÃ¡section p-0 overflow-hidden mt-3 shadow-lg" style="border: var(--glass-border);">
        <div class="table-responsive">
            <table class="table table-dark-custom table-hover m-0" id="tablaFacturas">
                <thead style="background: rgba(255,255,255,0.02);">
                    <tr>
                        <th class="ps-4">ID</th>
                        <th>Fecha y Hora</th>
                        <th>Cliente</th>
                        <th>Detalle</th>
                        <th>Total</th>
                    </tr>
                </thead>
                <tbody>
                    <%
                        List<Factura> facturas = (List<Factura>) request.getAttribute("listaFacturas");
                        if(facturas != null && !facturas.isEmpty()) {
                            for(Factura f : facturas) {
                                out.print("<tr>");
                                out.print("<td class='ps-4 fw-bold'>FAC-" + String.format("%05d", f.getId()) + "</td>");
                                out.print("<td>" + f.getFechaEmision().toString().replace("T", " ").substring(0, 16) + "</td>");
                                out.print("<td>" + f.getClienteNombre() + "</td>");
                                
                                StringBuilder detalles = new StringBuilder();
                                if(f.getDetalles() != null) {
                                    for(FacturaDetalle d : f.getDetalles()) {
                                        detalles.append(d.getCantidad()).append("x ").append(d.getMedicamento().getNombre()).append(" ($").append(String.format("%.2f", d.getSubtotal())).append(")<br>");
                                    }
                                }
                                out.print("<td style='font-size: 0.85rem;'>" + detalles.toString() + "</td>");
                                out.print("<td class='text-success fw-bold'>$" + String.format("%.2f", f.getTotal()) + "</td>");
                                out.print("</tr>");
                            }
                        } else {
                            out.print("<tr><td colspan='5' class='text-center py-5 text-secondary'><i class='bi bi-inbox me-2 fs-4 d-block mb-2'></i>No hay facturas registradas.</td></tr>");
                        }
                    %>
                </tbody>
            </table>
        </div>
    </div>
</div>
<script>
    function filtrarFacturas() {
        let input = document.getElementById("buscadorFacturas");
        let filter = input.value.toUpperCase();
        let table = document.getElementById("tablaFacturas");
        let tr = table.getElementsByTagName("tr");
        
        for (let i = 1; i < tr.length; i++) {
            let visible = false;
            let tds = tr[i].getElementsByTagName("td");
            for (let j = 0; j < tds.length; j++) {
                if (tds[j]) {
                    if (tds[j].innerHTML.toUpperCase().indexOf(filter) > -1) {
                        visible = true;
                        break;
                    }
                }
            }
            if (visible) {
                tr[i].style.display = "";
            } else {
                tr[i].style.display = "none";
            }
        }
    }
</script>







