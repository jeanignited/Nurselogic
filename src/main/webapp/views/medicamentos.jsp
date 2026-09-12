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
%>
        <div id="medicamentos" class="vista-activa d-none">

            <div class="d-flex justify-content-between align-items-center mb-4 flex-wrap gap-2">

                <h3 class="m-0 fw-bold"><i class="bi bi-capsule me-2" style="color: #10b981;"></i>Inventario Farmacológico Viva</h3>

                <div class="d-flex gap-2 align-items-center">

                    <a href="exportCsv?tipo=medicamentos" class="btn btn-outline-success text-nowrap rounded-pill px-3 py-2 shadow-sm" title="Descargar Excel/CSV"><i class="bi bi-file-earmark-spreadsheet-fill me-1"></i>Exportar</a>

                    <% if(canManageStock) { %>

                    <button type="button" class="btn btn-success" onclick="abrirModalMedicamento()"><i class="bi bi-plus-circle me-2"></i>Registrar Fármaco</button>

                    <% } %>

                </div>

            </div>

            

            <% if(canSellStock) { %>

            <!-- Módulo de Farmacia - Despacho -->

            <div class="form-section p-4 mb-5 border-start border-success border-4" style="background: rgba(16, 185, 129, 0.05);">

                <h5 class="fw-bold mb-3" style="color: #10b981;"><i class="bi bi-shop me-2"></i>Módulo de Despacho (Farmacia)</h5>

                <p class="text-secondary small mb-3">Busque el paciente por número de cédula para ver su receta y observaciones médicas vigentes.</p>

                <div class="input-group mb-4" style="max-width: 500px;">

                    <input type="text" id="cedulaFarmaciaBuscador" class="form-control" placeholder="Ingrese Cédula del Paciente (10 dígitos)" maxlength="10" oninput="this.value = this.value.replace(/[^0-9]/g, '');" onkeydown="if(event.key === 'Enter') buscarRecetaFarmacia()" autocomplete="off">

                    <button class="btn btn-success px-4" type="button" onclick="buscarRecetaFarmacia()"><i class="bi bi-search me-2"></i>Buscar Receta</button>

                </div>

                

                <div id="recetaFarmaciaContainer" class="d-none">

                    <div class="card bg-transparent border-success mb-3" style="border-style: dashed !important;">

                        <div class="card-header border-success bg-transparent d-flex justify-content-between align-items-center">

                            <h6 class="mb-0 fw-bold text-success"><i class="bi bi-file-medical-fill me-2"></i>Receta Médica Encontrada</h6>

                            <span class="badge bg-success rounded-pill" id="estadoRecetaBadge">VIGENTE</span>

                        </div>

                        <div class="card-body">

                            <div class="row">

                                <div class="col-md-6 mb-3">

                                    <small class="text-secondary fw-semibold">Paciente:</small>

                                    <div class="fw-bold fs-5" id="farmaciaPacienteNombre"></div>

                                </div>

                                <div class="col-md-6 mb-3">

                                    <small class="text-secondary fw-semibold">Fecha de Emisión:</small>

                                    <div id="farmaciaFechaCita"></div>

                                </div>

                            </div>

                            <hr class="border-secondary opacity-25">

                            <small class="text-secondary fw-semibold">Detalle de la Receta (Medicamentos y Dosis):</small>

                            <div class="mt-2 p-3 rounded" style="background: rgba(0,0,0,0.2); white-space: pre-wrap;" id="farmaciaRecetaContenido"></div>

                            <div class="mt-3 pt-3 border-top border-secondary d-flex justify-content-between align-items-center flex-wrap gap-2">

                                <div>

                                    <span class="badge bg-success rounded-pill px-3 py-2 fs-6"><i class="bi bi-check-circle-fill me-1"></i>Factura Registrada</span>

                                </div>

                                <button type="button" class="btn btn-success rounded-pill px-4 fw-bold shadow-sm" onclick="completarVentaReceta()"><i class="bi bi-receipt me-2"></i>Completar Venta y Ver en Reporte de Ventas</button>

                            </div>

                        </div>

                    </div>

                </div>

                <div id="recetaFarmaciaNotFound" class="alert alert-warning d-none">

                    <i class="bi bi-exclamation-triangle-fill me-2"></i> No se encontró ninguna receta vigente para esta cédula.

                </div>

            </div>

            <% } %>



            <% 

                List<Map<String, String>> medsCheck = (List<Map<String, String>>) request.getAttribute("listaMedicamentos");

                int medCriticos = 0;

                if (medsCheck != null) {

                    for(Map<String, String> mc : medsCheck) {

                        try { if(Integer.parseInt(mc.get("stock")) < 10) medCriticos++; } catch(Exception ex){}

                    }

                }

                if (medCriticos > 0) {

            %>

            <div class="alert alert-danger d-flex align-items-center mb-4" role="alert" style="background: rgba(239, 68, 68, 0.15); border: 1px solid #ef4444; color: #fca5a5;">

                <i class="bi bi-exclamation-octagon-fill flex-shrink-0 me-3 fs-4"></i>

                <div>

                    <strong>Alerta de Bodega Clínica:</strong> Se han detectado <b><%= medCriticos %></b> medicamento(s) con stock crítico (inferior a 10 unidades). Se requiere reposición urgente.

                </div>

            </div>

            <% } %>



            <div class="mb-3 position-relative" style="max-width: 400px;">

                <i class="bi bi-search position-absolute top-50 start-0 translate-middle-y ms-3 text-secondary"></i>

                <input type="text" id="buscadorMedicamentos" class="form-control ps-5 form-control-sm" style="border: var(--glass-border); border-radius: 20px;" placeholder="Buscar fármaco o estado de bodega..." onkeyup="filtrarMedicamentos()" autocomplete="off">

            </div>

            <div class="form-section p-0">

                <div class="table-responsive">

                    <table id="tablaMedicamentos" class="table table-dark-custom table-hover m-0">

                        <thead>

                            <tr>

                                <th>Medicamento</th>

                                <th>Precio Base</th>

                                <th>Nivel de Stock</th>

                                <th>Estado de Bodega</th>

                                <% if(canManageStock || canSellStock) { out.print("<th>Ajuste Rápido de Stock</th>"); } %>

                            </tr>

                        </thead>

                        <tbody>

                            <% 

                                if (medsCheck == null || medsCheck.isEmpty()) {

                                    out.print("<tr><td colspan='" + (canManageStock || canSellStock ? "5" : "4") + "' class='text-center py-5 text-secondary'><i class='bi bi-box-seam me-2 fs-4 d-block mb-2'></i>Bodega vacía.</td></tr>");

                                } else {

                                    for(Map<String, String> m : medsCheck) {

                                        int st = 0;

                                        double pr = 0.0;

                                        try { st = Integer.parseInt(m.get("stock")); } catch(Exception e){}

                                        try { pr = Double.parseDouble(m.get("precio")); } catch(Exception e){}

                                        

                                        String badgeClass = "bg-success";

                                        String estadoText = "Óptimo";

                                        String icon = "bi-check-circle";

                                        if (st <= 0) { badgeClass = "bg-danger text-white"; estadoText = "AGOTADO"; icon = "bi-x-octagon-fill"; }

                                        else if (st < 10) { badgeClass = "bg-danger"; estadoText = "CR�TICO"; icon = "bi-exclamation-triangle-fill"; }

                                        else if (st <= 25) { badgeClass = "bg-warning text-dark"; estadoText = "Bajo"; icon = "bi-exclamation-circle"; }



                                        out.print("<tr>");

                                        out.print("<td class='fw-bold fs-6'>" + m.get("nombre") + "</td>");

                                        out.print("<td class='text-info fw-semibold'>$" + String.format("%.2f", pr) + "</td>");

                                        out.print("<td><span class='badge " + badgeClass + " rounded-pill px-3 py-2 fs-6'>" + st + " uds</span></td>");

                                        out.print("<td><span class='text-theme'><i class='bi " + icon + " me-1'></i> " + estadoText + "</span></td>");

                                        if (canManageStock || canSellStock) {

                                            out.print("<td>");

                                            out.print("<div class='btn-group' role='group'>");

                                            if (canSellStock) {

                                                out.print("<button class='btn btn-sm btn-outline-danger' title='Disminuir 1 ud (Venta)' onclick=\"abrirModalVenta(" + m.get("id") + ", '" + m.get("nombre") + "', " + m.get("precio") + ", " + m.get("stock") + ")\" " + (st <= 0 ? "disabled" : "") + "><i class='bi bi-dash-lg'></i> Facturar Venta</button>");

                                            }

                                            if (canManageStock) {

                                                out.print("<button class='btn btn-sm btn-outline-success' title='Ingreso +10 uds' onclick=\"ajustarStockMed(" + m.get("id") + ", 10)\"><i class='bi bi-plus-lg'></i> +10</button>");

                                            }

                                            out.print("</div>");

                                            out.print("</td>");

                                        }

                                        out.print("</tr>");

                                    }

                                }

                            %>

                        </tbody>

                    </table>

                </div>

            </div>

        </div>






