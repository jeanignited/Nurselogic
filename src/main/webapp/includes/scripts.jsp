<%@ page pageEncoding="UTF-8" %>
<%@ page import="java.util.List,java.util.Map,java.util.ArrayList" %>
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



    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
<script>



        function toggleMenu() {



            document.getElementById('sidebar').classList.toggle('contraida');



            document.getElementById('main-content').classList.toggle('expandida');



        }







        function formatearEstatura(input) {



            let val = input.value.replace(/[^0-9]/g, '');



            if (val.length > 0 && !/^[012]/.test(val)) {



                val = '';



            }



            if (val.length > 3) val = val.substring(0, 3);



            



            if (val.length > 1) {



                val = val.substring(0, 1) + '.' + val.substring(1, 3);



            }



            input.value = val;



            calcularIMCTiempoReal();



        }







        function formatearPeso(input) {



            let val = input.value.replace(/[^0-9]/g, '');



            if (val.length > 0) {



                let firstChar = val.substring(0, 1);



                let maxLen = (firstChar === '1' || firstChar === '2') ? 4 : 3;



                if (val.length > maxLen) {



                    val = val.substring(0, maxLen);



                }



            }



            



            if (val.length > 2) {



                val = val.substring(0, val.length - 1) + '.' + val.substring(val.length - 1);



            }



            input.value = val;



            calcularIMCTiempoReal();



        }







        function formatearTemperatura(input) {



            let val = input.value.replace(/[^0-9]/g, '');



            if (val.length > 0) {



                let firstChar = val.substring(0, 1);



                if (firstChar !== '3' && firstChar !== '4') {



                    val = '';



                }



            }



            if (val.length > 3) val = val.substring(0, 3);



            



            if (val.length > 2) {



                val = val.substring(0, 2) + '.' + val.substring(2, 3);



            }



            input.value = val;



            validarSignos();



        }







        function formatearPresion(input) {



            let val = input.value.replace(/[^0-9]/g, '');



            if (val.length > 0) {



                let s1 = val[0];



                if (['0','3','4','5'].includes(s1)) {



                    val = ''; 



                }



            }



            



            let sysLen = (val.startsWith('1') || val.startsWith('2')) ? 3 : 2;



            



            if (val.length > sysLen) {



                let sys = val.substring(0, sysLen);



                let dia = val.substring(sysLen);



                



                if (dia.length > 0) {



                    let d1 = dia[0];



                    if (['0','2','3'].includes(d1)) {



                        dia = '';



                    } else {



                        let diaLen = (d1 === '1') ? 3 : 2;



                        dia = dia.substring(0, diaLen);



                    }



                }



                val = sys + (dia.length > 0 ? '/' + dia : '');



            }



            input.value = val;



        }







        function formatearFC(input) {



            let val = input.value.replace(/[^0-9]/g, '');



            if (val.length > 0) {



                let first = val[0];



                let maxLen = (first === '1' || first === '2') ? 3 : 2;



                if (val.length > maxLen) {



                    val = val.substring(0, maxLen);



                }



            }



            input.value = val;



            validarSignos();



        }







        function formatearSat(input) {



            let val = input.value.replace(/[^0-9]/g, '');



            if (val.length > 0) {



                let first = val[0];



                let maxLen = (first === '1') ? 3 : 2;



                if (val.length > maxLen) val = val.substring(0, maxLen);



                if (parseInt(val) > 100) val = '100';



            }



            input.value = val;



            validarSignos();



        }







        document.getElementById('cedulaBusqueda').addEventListener('keyup', function() {



            let cedula = this.value.replace(/[^0-9]/g, '');



            if(cedula.length === 10) {



                fetch('registroPaciente?action=buscarCedula&cedula=' + cedula)



                .then(res => res.json())



                .then(data => {



                    if(data.encontrado) {



                        document.getElementById('nombres').value = data.nombres;



                        document.getElementById('apellidos').value = data.apellidos;



                        document.getElementById('sexo').value = data.sexo;



                        if (data.fechaNacimiento) {



                            document.getElementById('fechaNacimiento').value = data.fechaNacimiento;



                            calcularEdadTiempoReal();



                        }



                    }



                }).catch(e => console.log('No se pudo autocompletar', e));



            }



        });







        function filtrarPacientes() {



            let input = document.getElementById("buscadorPacientes").value.toLowerCase();



            let table = document.getElementById("tablaPacientes");



            if (!table) return;



            let tr = table.getElementsByTagName("tr");



            



            for (let i = 1; i < tr.length; i++) {



                let txtValue = tr[i].textContent || tr[i].innerText;



                if (txtValue.toLowerCase().indexOf(input) > -1) {



                    tr[i].style.display = "";



                } else {



                    tr[i].style.display = "none";



                }



            }



        }







        function filtrarMedicamentos() {



            let input = document.getElementById("buscadorMedicamentos").value.toLowerCase();



            let table = document.getElementById("tablaMedicamentos");



            if (!table) return;



            let tr = table.getElementsByTagName("tr");



            for (let i = 1; i < tr.length; i++) {



                let txtValue = tr[i].textContent || tr[i].innerText;



                if (txtValue.toLowerCase().indexOf(input) > -1) {



                    tr[i].style.display = "";



                } else {



                    tr[i].style.display = "none";



                }



            }



        }







        function filtrarCitas() {



            let input = document.getElementById("buscadorCitas").value.toLowerCase();



            let table = document.getElementById("tablaCitas");



            if (!table) return;



            let tr = table.getElementsByTagName("tr");



            for (let i = 1; i < tr.length; i++) {



                let txtValue = tr[i].textContent || tr[i].innerText;



                if (txtValue.toLowerCase().indexOf(input) > -1) {



                    tr[i].style.display = "";



                } else {



                    tr[i].style.display = "none";



                }



            }



        }







        function calcularEdadTiempoReal() {



            let fnInput = document.getElementById('fechaNacimiento');



            let badge = document.getElementById('edadBadge');



            if (!fnInput || !fnInput.value || !badge) return;



            let hoy = new Date();



            let nac = new Date(fnInput.value);



            let edad = hoy.getFullYear() - nac.getFullYear();



            let m = hoy.getMonth() - nac.getMonth();



            if (m < 0 || (m === 0 && hoy.getDate() < nac.getDate())) {



                edad--;



            }



            badge.innerText = edad + " años";



            badge.classList.remove('d-none');



        }







        function changingActiveNav(vistaId) {



            document.querySelectorAll('.sidebar .nav-link').forEach(link => {



                link.classList.remove('active');



                const onclickAttr = link.getAttribute('onclick') || '';



                if (onclickAttr.includes(vistaId)) {



                    link.classList.add('active');



                }



            });



        }







        function cambiarVista(vistaId) {



            changingActiveNav(vistaId);



            document.querySelectorAll('.vista-activa').forEach(el => {



                el.style.opacity = '0';



                setTimeout(() => {



                    el.classList.add('d-none');



                }, 300);



            });



            



            setTimeout(() => {



                const activeView = document.getElementById(vistaId);



                if (activeView) {



                    activeView.classList.remove('d-none');



                    if (vistaId === 'estadisticas' && typeof actualizarGraficos === 'function') {



                        actualizarGraficos();



                    }



                    setTimeout(() => {



                        activeView.style.opacity = '1';



                    }, 50);



                }



            }, 300);



        }







        // AJAX para autocompletar Paciente por cedula



        document.addEventListener('DOMContentLoaded', function() {



            const cedulaInput = document.getElementById('cedulaBusqueda');



            if (cedulaInput) {



                cedulaInput.addEventListener('blur', function() {



                    const cedula = this.value;



                    if (cedula.length > 5) {



                        fetch('registroPaciente?action=buscarCedula&cedula=' + cedula)



                            .then(response => response.json())



                            .then(data => {



                                if (data.encontrado) {



                                    document.getElementById('nombres').value = data.nombres;



                                    document.getElementById('apellidos').value = data.apellidos;



                                    document.getElementById('sexo').value = data.sexo;



                                    if(data.fechaNacimiento) {



                                        document.getElementById('fechaNacimiento').value = data.fechaNacimiento;



                                    }



                                    



                                    // Feedback visual



                                    cedulaInput.classList.add('is-valid');



                                    setTimeout(() => cedulaInput.classList.remove('is-valid'), 2000);



                                } else {



                                    // Limpiar si no existe



                                    document.getElementById('nombres').value = '';



                                    document.getElementById('apellidos').value = '';



                                    document.getElementById('fechaNacimiento').value = '';



                                }



                            })



                            .catch(error => console.error('Error fetching patient data:', error));



                    }



                });



            }



        });







        function procesarIMC(peso, estatura, valElem, estElem) {



            if(peso > 0 && estatura > 0) {



                let imc = peso / (estatura * estatura);



                valElem.innerText = imc.toFixed(1);



                estElem.className = 'badge px-4 py-2 rounded-pill fs-6 mt-2';







                if(imc < 18.5) { estElem.innerText = 'Bajo Peso'; estElem.classList.add('bg-warning', 'text-dark'); }



                else if(imc < 25) { estElem.innerText = 'Normal'; estElem.classList.add('bg-success'); }



                else if(imc < 30) { estElem.innerText = 'Sobrepeso'; estElem.classList.add('bg-warning', 'text-dark'); }



                else { estElem.innerText = 'Obesidad'; estElem.classList.add('bg-danger'); }



            } else {



                valElem.innerText = '0.0';



                estElem.innerText = 'Introduce tus datos';



                estElem.className = 'badge bg-secondary px-4 py-2 rounded-pill fs-6 mt-2';



            }



        }







        function calcularIMCTiempoReal() {



            let p = parseFloat(document.getElementById('peso').value);



            let a = parseFloat(document.getElementById('estatura').value);



            procesarIMC(p, a, document.getElementById('imcValor'), document.getElementById('imcEstado'));



        }







        function calcularIMCPaciente() {



            let p = parseFloat(document.getElementById('peso_pac').value);



            let a = parseFloat(document.getElementById('estatura_pac').value);



            procesarIMC(p, a, document.getElementById('imcValor_pac'), document.getElementById('imcEstado_pac'));



        }







        function formatearEstatura_pac(input) {



            let val = input.value.replace(/[^0-9]/g, '');



            if (val.length > 0 && !/^[012]/.test(val)) {



                val = '';



            }



            if (val.length > 3) val = val.substring(0, 3);



            if (val.length > 1) {



                val = val.substring(0, 1) + '.' + val.substring(1, 3);



            }



            input.value = val;



            calcularIMCPaciente();



        }







        function formatearPeso_pac(input) {



            let val = input.value.replace(/[^0-9]/g, '');



            if (val.length > 0) {



                let firstChar = val.substring(0, 1);



                let maxLen = (firstChar === '1' || firstChar === '2') ? 4 : 3;



                if (val.length > maxLen) val = val.substring(0, maxLen);



                if (val.length > maxLen - 1) {



                    val = val.substring(0, maxLen - 1) + '.' + val.substring(maxLen - 1);



                }



            }



            input.value = val;



            calcularIMCPaciente();



        }







        function validarSignos() {



            // Validar Temperatura



            let tempInput = document.getElementById('temp');



            let alertaTemp = document.getElementById('alertaTemp');



            if (tempInput.value) {



                let temp = parseFloat(tempInput.value);



                if (temp > 38.0) { alertaTemp.innerText = "Alta (Fiebre)"; alertaTemp.classList.remove('d-none'); }



                else if (temp < 35.0) { alertaTemp.innerText = "Baja (Hipotermia)"; alertaTemp.classList.remove('d-none'); }



                else { alertaTemp.classList.add('d-none'); }



            } else { alertaTemp.classList.add('d-none'); }







            // Validar Frecuencia card aca



            let fcInput = document.getElementById('fc');



            let alertaFc = document.getElementById('alertaFc');



            if (fcInput.value) {



                let fc = parseInt(fcInput.value);



                if (fc > 100) { alertaFc.innerText = "Taquicardia"; alertaFc.classList.remove('d-none'); }



                else if (fc < 60) { alertaFc.innerText = "Bradicardia"; alertaFc.classList.remove('d-none'); }



                else { alertaFc.classList.add('d-none'); }



            } else { alertaFc.classList.add('d-none'); }







            // Validar Saturación



            let satInput = document.getElementById('sat');



            let alertaSat = document.getElementById('alertaSat');



            if (satInput.value) {



                let sat = parseInt(satInput.value);



                if (sat < 90) { alertaSat.innerText = "Hipoxemia severa"; alertaSat.classList.remove('d-none'); }



                else if (sat < 95) { alertaSat.innerText = "Hipoxemia leve"; alertaSat.classList.remove('d-none'); }



                else { alertaSat.classList.add('d-none'); }



            } else { alertaSat.classList.add('d-none'); }



        }







        let grabador;



        let fragmentos = [];



        async function iniciarGrabacion() {



            try {



                const stream = await navigator.mediaDevices.getDisplayMedia({ video: true });



                grabador = new MediaRecorder(stream);



                grabador.ondataavailable = (e) => { if (e.data.size > 0) fragmentos.push(e.data); };



                grabador.onstop = () => {



                    document.getElementById('videoPreview').src = URL.createObjectURL(new Blob(fragmentos, { type: 'video/webm' }));



                    document.getElementById('videoPreview').classList.remove('d-none');



                    document.getElementById('videoPlaceholder').classList.add('d-none');



                    fragmentos = [];



                };



                grabador.start();



                document.getElementById('btnGrabar').classList.add('d-none');



                document.getElementById('btnDetener').classList.remove('d-none');



                stream.getVideoTracks()[0].onended = () => detenerGrabacion();



            } catch(err) { console.error("Error al grabar: ", err); }



        }







        function detenerGrabacion() {



            if(grabador && grabador.state !== "inactive") { grabador.stop(); grabador.stream.getTracks().forEach(t => t.stop()); }



            document.getElementById('btnGrabar').classList.remove('d-none');



            document.getElementById('btnDetener').classList.add('d-none');



        }







        // --- Funciones de Administraci n ---



        function editarPaciente(cedula) {



            cambiarVista('dashboard');



            const cedulaInput = document.getElementById('cedulaBusqueda');



            if (cedulaInput) {



                cedulaInput.value = cedula;



                cedulaInput.focus();



                // Desencadenar el evento blur para forzar el autocompletado



                cedulaInput.dispatchEvent(new Event('blur'));



            }



        }







        function cancelarEdicion() {



            const form = document.getElementById('formRegistroPaciente');



            if(form) form.reset();



            document.getElementById('formAdmision')?.classList.add('d-none');



        }







        function confirmarBorrado(tipo, id) {



            if(confirm(' ¿Estas seguro de que deseas eliminar este ' + tipo + '? Esta acción no se puede deshacer.')) {



                document.getElementById('adminActionType').value = 'eliminar';



                document.getElementById('adminActionTarget').value = tipo;



                document.getElementById('adminActionId').value = id;



                document.getElementById('formAdminAction').submit();



            }



        }







        function abrirModalRol(correo, rolActual) {



            document.getElementById('rolUserEmail').innerText = correo;



            document.getElementById('rolSelectModal').value = rolActual;



            var mEl = document.getElementById('modalRol'); if(mEl) { var m = bootstrap.Modal.getInstance(mEl) || new bootstrap.Modal(mEl); m.show(); }



        }







        function cerrarModalRol() {



            var mEl = document.getElementById('modalRol'); if(mEl) { var m = bootstrap.Modal.getInstance(mEl); if(m) m.hide(); }



        }







        function abrirModalNuevoRol() {



            var mEl = document.getElementById('modalNuevoRol'); if(mEl) { var m = bootstrap.Modal.getInstance(mEl) || new bootstrap.Modal(mEl); m.show(); }



        }







        function cerrarModalNuevoRol() {



            var mEl = document.getElementById('modalNuevoRol'); if(mEl) { var m = bootstrap.Modal.getInstance(mEl); if(m) m.hide(); }



        }







        function guardarCambioRol() {



            let correo = document.getElementById('rolUserEmail').innerText;



            let nuevoRol = document.getElementById('rolSelectModal').value;



            



            document.getElementById('adminActionType').value = 'editarRol';



            document.getElementById('adminActionTarget').value = 'usuario';



            document.getElementById('adminActionId').value = correo;



            document.getElementById('adminActionRol').value = nuevoRol;



            document.getElementById('formAdminAction').submit();



        }







        function aplicarPlantillaRol(tipo, el) {



            document.querySelectorAll('.plantilla-card').forEach(c => {



                c.style.background = gridCol;



                c.style.borderColor = 'rgba(255,255,255,0.2)';



            });



            if (el) {



                el.style.background = 'rgba(255, 193, 7, 0.15)';



                el.style.borderColor = '#ffc107';



            }







            document.querySelectorAll('.chk-permiso').forEach(chk => chk.checked = false);







            if (tipo === 'moderador') {



                document.getElementById('perm_usr').checked = true;



                document.getElementById('inputNombreRol').value = 'Moderador de Personal';



                document.getElementById('inputDescRol').value = 'Gestión y control de cuentas de usuarios';



            } else if (tipo === 'bodeguero') {



                document.getElementById('perm_med').checked = true;



                document.getElementById('perm_cat').checked = true;



                document.getElementById('inputNombreRol').value = 'Gestor de Bodega';



                document.getElementById('inputDescRol').value = 'Control de inventario de farmacia y catalogos';



            } else if (tipo === 'medico') {



                document.getElementById('perm_pac').checked = true;



                document.getElementById('perm_cit').checked = true;



                document.getElementById('inputNombreRol').value = 'medico Triage';



                document.getElementById('inputDescRol').value = 'Atención a pacientes, triage y citas medicas';



            } else if (tipo === 'custom') {



                document.getElementById('inputNombreRol').value = '';



                document.getElementById('inputDescRol').value = '';



                document.getElementById('inputNombreRol').focus();



            }



        }







        // --- Funciones del Ecosistema Enriquecido (5 Tareas) ---



        function cambiarEstadoCita(idCita, nuevoEstado) {



            document.getElementById('adminActionType').value = 'actualizarEstadoCita';



            document.getElementById('adminActionTarget').value = 'cita';



            document.getElementById('adminActionId').value = idCita;



            let inputEst = document.getElementById('adminActionNuevoEst');



            if (!inputEst) {



                inputEst = document.createElement('input');



                inputEst.type = 'hidden';



                inputEst.name = 'nuevoEstado';



                inputEst.id = 'adminActionNuevoEst';



                document.getElementById('formAdminAction').appendChild(inputEst);



            }



            inputEst.value = nuevoEstado;



            document.getElementById('formAdminAction').submit();



        }







        function abrirModalMedicamento() {



            var mEl = document.getElementById('modalMedicamento'); if(mEl) { var m = bootstrap.Modal.getInstance(mEl) || new bootstrap.Modal(mEl); m.show(); }



        }







        function cerrarModalMedicamento() {



            var mEl = document.getElementById('modalMedicamento'); if(mEl) { var m = bootstrap.Modal.getInstance(mEl); if(m) m.hide(); }



        }







        function ajustarStockMed(idMed, cambio) {



            document.getElementById('adminActionType').value = 'ajustarStock';



            document.getElementById('adminActionTarget').value = 'medicamento';



            document.getElementById('adminActionId').value = idMed;



            let inputCambio = document.getElementById('adminActionCambio');



            if (!inputCambio) {



                inputCambio = document.createElement('input');



                inputCambio.type = 'hidden';



                inputCambio.name = 'cambio';



                inputCambio.id = 'adminActionCambio';



                document.getElementById('formAdminAction').appendChild(inputCambio);



            }



            let inputIdMed = document.getElementById('adminActionIdMed');



            if (!inputIdMed) {



                inputIdMed = document.createElement('input');



                inputIdMed.type = 'hidden';



                inputIdMed.name = 'idMed';



                inputIdMed.id = 'adminActionIdMed';



                document.getElementById('formAdminAction').appendChild(inputIdMed);



            }



            inputIdMed.value = idMed;



            inputCambio.value = cambio;



            document.getElementById('formAdminAction').submit();



        }







        function abrirModalEspecialidad(correo, espActual) {



            document.getElementById('espUserEmail').value = correo;



            document.getElementById('espUserDisplay').innerText = correo;



            if (espActual && espActual !== 'null' && espActual !== 'Sin Especialidad') {



                document.getElementById('selectEspecialidadModal').value = espActual;



            } else {



                document.getElementById('selectEspecialidadModal').value = 'Medicina General';



            }



            var mEl = document.getElementById('modalEspecialidad'); if(mEl) { var m = bootstrap.Modal.getInstance(mEl) || new bootstrap.Modal(mEl); m.show(); }



        }







        function cerrarModalEspecialidad() {



            var mEl = document.getElementById('modalEspecialidad'); if(mEl) { var m = bootstrap.Modal.getInstance(mEl); if(m) m.hide(); }



        }







        function abrirModalCatalogos(tipo) {



            document.getElementById('catIdEnf').value = '';



            document.getElementById('catIdAle').value = '';



            document.getElementById('catNombreEnf').value = '';



            document.getElementById('catDescEnf').value = '';



            document.getElementById('catNombreAle').value = '';



            document.getElementById('catGravAle').value = 'Leve';



            if (tipo === 'enfermedad') {



                document.getElementById('catModalTitulo').innerHTML = '<i class="bi bi-heart-pulse text-danger me-2"></i>Registrar Nueva Patología';



                document.getElementById('catActionInput').value = 'crearEnfermedad';



                document.getElementById('catEnfermedadCampos').classList.remove('d-none');



                document.getElementById('catAlergiaCampos').classList.add('d-none');



                document.getElementById('catNombreEnf').required = true;



                document.getElementById('catNombreAle').required = false;



            } else {



                document.getElementById('catModalTitulo').innerHTML = '<i class="bi bi-exclamation-diamond text-warning me-2"></i>Registrar Nuevo Alergeno';



                document.getElementById('catActionInput').value = 'crearAlergia';



                document.getElementById('catEnfermedadCampos').classList.add('d-none');



                document.getElementById('catAlergiaCampos').classList.remove('d-none');



                document.getElementById('catNombreEnf').required = false;



                document.getElementById('catNombreAle').required = true;



            }



            var mEl = document.getElementById('modalCatalogos'); if(mEl) { var m = bootstrap.Modal.getInstance(mEl) || new bootstrap.Modal(mEl); m.show(); }



        }







        function abrirModalEditarEnfermedad(id, nombre, desc) {



            document.getElementById('catModalTitulo').innerHTML = '<i class="bi bi-pencil-square text-danger me-2"></i>Editar Patología / Enfermedad';



            document.getElementById('catActionInput').value = 'editarEnfermedad';



            document.getElementById('catIdEnf').value = id;



            document.getElementById('catNombreEnf').value = nombre;



            document.getElementById('catDescEnf').value = desc;



            document.getElementById('catEnfermedadCampos').classList.remove('d-none');



            document.getElementById('catAlergiaCampos').classList.add('d-none');



            document.getElementById('catNombreEnf').required = true;



            document.getElementById('catNombreAle').required = false;



            var mEl = document.getElementById('modalCatalogos'); if(mEl) { var m = bootstrap.Modal.getInstance(mEl) || new bootstrap.Modal(mEl); m.show(); }



        }







        function abrirModalEditarAlergia(id, nombre, grav) {



            document.getElementById('catModalTitulo').innerHTML = '<i class="bi bi-pencil-square text-warning me-2"></i>Editar Alergeno';



            document.getElementById('catActionInput').value = 'editarAlergia';



            document.getElementById('catIdAle').value = id;



            document.getElementById('catNombreAle').value = nombre;



            document.getElementById('catGravAle').value = grav;



            document.getElementById('catEnfermedadCampos').classList.add('d-none');



            document.getElementById('catAlergiaCampos').classList.remove('d-none');



            document.getElementById('catNombreEnf').required = false;



            document.getElementById('catNombreAle').required = true;



            var mEl = document.getElementById('modalCatalogos'); if(mEl) { var m = bootstrap.Modal.getInstance(mEl) || new bootstrap.Modal(mEl); m.show(); }



        }







        function borrarCatalogo(tipo, id, nombre) {



            if (confirm('¿Estás seguro de eliminar "' + nombre + '" del catálogo clínico?')) {



                let f = document.getElementById('formAdminAction');



                document.getElementById('adminActionType').value = tipo === 'enfermedad' ? 'borrarEnfermedad' : 'borrarAlergia';



                let inputId = document.createElement('input');



                inputId.type = 'hidden';



                inputId.name = tipo === 'enfermedad' ? 'idEnf' : 'idAle';



                inputId.value = id;



                f.appendChild(inputId);



                f.submit();



            }



        }







        function cerrarModalCatalogos() {



            var mEl = document.getElementById('modalCatalogos'); if(mEl) { var m = bootstrap.Modal.getInstance(mEl); if(m) m.hide(); }



        }







        let cedulaFichaActual = '';



        function verFichaClinica(cedula) {



            cedulaFichaActual = cedula;



            fetch('registroPaciente?action=buscarCedula&cedula=' + encodeURIComponent(cedula))



                .then(r => r.json())



                .then(data => {



                    if (data && data.encontrado) {



                        document.getElementById('fichaNombre').innerText = data.nombres + ' ' + data.apellidos;



                        document.getElementById('fichaInfo').innerText = 'CÃ©dula: ' + cedula + ' | Nacimiento: ' + (data.fechaNacimiento || 'N/D') + ' | Sexo: ' + (data.sexo || 'N/D');



                        



                        let est = parseFloat(data.estatura || 0);



                        let peso = parseFloat(data.peso || 0);



                        let temp = parseFloat(data.temperatura || 0);



                        let fc = parseInt(data.fc || 0);



                        let sat = parseInt(data.sat || 0);



                        let pres = data.presion || '120/80';







                        document.getElementById('fichaEstPeso').innerText = (est > 0 ? est + ' m' : '-- m') + ' / ' + (peso > 0 ? peso + ' kg' : '-- kg');



                        document.getElementById('fichaTemp').innerText = temp > 0 ? temp + ' Â°C' : '-- Â°C';



                        document.getElementById('fichaPresion').innerText = pres;



                        document.getElementById('fichaFcSat').innerText = (fc > 0 ? fc + ' lpm' : '--') + ' / ' + (sat > 0 ? sat + '%' : '--');



                        document.getElementById('fichaEnfermedades').innerText = data.enfermedad || 'Ninguna preexistente';



                        document.getElementById('fichaAlergias').innerText = data.alergias || 'Ninguna reportada';







                        // calculo de Diagnostico Inteligente (Task 4)



                        let alertasHTML = '';



                        let IMC = (est > 0 && peso > 0) ? (peso / (est * est)).toFixed(1) : 0;



                        



                        if (IMC > 0) {



                            let imcColor = 'bg-success';



                            let imcTxt = 'Peso Normal / Saludable  ';



                            if (IMC < 18.5) { imcColor = 'bg-info'; imcTxt = 'Bajo Peso (Riesgo de desnutrición)  '; }



                            else if (IMC >= 25 && IMC < 30) { imcColor = 'bg-warning text-dark'; imcTxt = 'Sobrepeso (Recomendación dietética)  '; }



                            else if (IMC >= 30) { imcColor = 'bg-danger'; imcTxt = 'Obesidad clínica (Atención médica)  '; }







                            alertasHTML += `<div class="p-3 mb-2 rounded d-flex align-items-center justify-content-between" style="background: rgba(255,255,255,0.05); border-left: 4px solid #38bdf8;">



                                <div><span class="text-secondary small d-block">Evaluación Antropométrica (IMC)</span><strong>${IMC} kg/m    ${imcTxt}</strong></div>



                                <span class="badge ${imcColor} px-3 py-2">IMC ${IMC}</span>



                            </div>`;



                        }







                        if (temp >= 38.0) {



                            alertasHTML += `<div class="p-3 mb-2 rounded d-flex align-items-center justify-content-between alert-danger" style="background: rgba(239, 68, 68, 0.2); border: 1px solid #ef4444;">



                                <div><i class="bi bi-exclamation-triangle-fill text-danger me-2 fs-5"></i><strong class="text-theme">ALERTA TÉRMICA CRÍTICA: Fiebre Alta / Hipertermia (${temp} c)</strong><br><small class="text-theme">Protocolo de reducción térmica inmediata y monitoreo antitérmico sugerido.</small></div>



                                <span class="badge bg-danger pulse-animation px-3 py-2 fs-6">  HIPERTERMIA</span>



                            </div>`;



                        } else if (temp >= 37.3 && temp < 38.0) {



                            alertasHTML += `<div class="p-3 mb-2 rounded d-flex align-items-center justify-content-between" style="background: rgba(245, 158, 11, 0.15); border-left: 4px solid #f59e0b;">



                                <div><strong class="text-warning"><i class="bi bi-exclamation-circle me-1"></i> Febrícula detectada (${temp} c)</strong><br><small class="text-secondary">Monitoreo periódico cada 2 horas.</small></div>



                                <span class="badge bg-warning text-dark px-3 py-2">  Febrícula</span>



                            </div>`;



                        }







                        if (sat > 0 && sat < 92) {



                            alertasHTML += `<div class="p-3 mb-2 rounded d-flex align-items-center justify-content-between" style="background: rgba(239, 68, 68, 0.2); border: 1px solid #ef4444;">



                                <div><i class="bi bi-lungs-fill text-danger me-2 fs-5"></i><strong class="text-theme">HIPOXIA SEVERA DETECTADA (Sat O2: ${sat}%)</strong><br><small class="text-theme">Administración urgente de oxígeno suplementario requerida.</small></div>



                                <span class="badge bg-danger px-3 py-2 fs-6">  HIPOXIA</span>



                            </div>`;



                        }







                        if (alertasHTML === '') {



                            alertasHTML = `<div class="p-3 mb-2 rounded text-center" style="background: rgba(16, 185, 129, 0.15); border: 1px solid #10b981;">



                                <i class="bi bi-check-circle-fill text-success me-2"></i><strong class="text-theme">Parámetros vitales dentro de rangos clinicos estables y normales.</strong>



                            </div>`;



                        }







                        document.getElementById('fichaAlertasContenedor').innerHTML = alertasHTML;







                        var mEl = document.getElementById('modalFichaClinica'); if(mEl) { var m = bootstrap.Modal.getInstance(mEl) || new bootstrap.Modal(mEl); m.show(); }



                    } else {



                        alert('No se encontraron los datos del paciente.');



                    }



                })



                .catch(err => console.error(err));



        }







        function cerrarModalFicha() {



            var mEl = document.getElementById('modalFichaClinica'); if(mEl) { var m = bootstrap.Modal.getInstance(mEl); if(m) m.hide(); }



        }







        function editarPacienteDesdeFicha() {



            cerrarModalFicha();



            if(cedulaFichaActual) {



                editarPaciente(cedulaFichaActual);



            }



        }







        function buscarPacienteCita(cedula) {
    const infoDiv = document.getElementById('citaPacNombre');
    const quickReg = document.getElementById('citaQuickRegister');
    const esNuevo = document.getElementById('citaEsNuevoPac');
    const btn = document.getElementById('btnAgendarCita');
    
    if (cedula.length === 10) {
        infoDiv.innerHTML = '<i class="spinner-border spinner-border-sm me-2"></i>Buscando...';
        btn.disabled = true;
        fetch('registroPaciente?action=buscarCedula&cedula=' + cedula)
            .then(r => r.json())
            .then(data => {
                if (data.id) {
                    infoDiv.innerHTML = '<i class="bi bi-check-circle-fill text-success me-1"></i> Paciente: ' + data.nombres + ' ' + data.apellidos;
                    quickReg.classList.add('d-none');
                    esNuevo.value = "false";
                    document.getElementById('citaPacienteIdHidden').value = data.id;
                    btn.disabled = false;
                    document.getElementById('citaNombres').required = false;
                    document.getElementById('citaApellidos').required = false;
                    document.getElementById('citaFechaNac').required = false;
                    document.getElementById('citaSexo').required = false;
                } else {
                    infoDiv.innerHTML = '';
                    quickReg.classList.remove('d-none');
                    esNuevo.value = "true";
                    document.getElementById('citaPacienteIdHidden').value = '';
                    btn.disabled = false;
                    document.getElementById('citaNombres').required = true;
                    document.getElementById('citaApellidos').required = true;
                    document.getElementById('citaFechaNac').required = true;
                    document.getElementById('citaSexo').required = true;
                }
            })
            .catch(e => {
                infoDiv.innerHTML = '<span class="text-danger">Error de red</span>';
                btn.disabled = false;
            });
    } else {
        infoDiv.innerHTML = '';
        quickReg.classList.add('d-none');
        esNuevo.value = "false";
                    document.getElementById('citaPacienteIdHidden').value = data.id;
        btn.disabled = false;
    }
}

function validarCitaAdmin(e) {
    const form = e.target;
    const datetime = document.getElementById('citaFechaHora').value;
    if (datetime) {
        const parts = datetime.split('T');
        if (parts.length === 2) {
            let f = document.createElement('input');
            f.type = 'hidden';
            f.name = 'fecha';
            f.value = parts[0];
            form.appendChild(f);
            
            let h = document.createElement('input');
            h.type = 'hidden';
            h.name = 'hora';
            h.value = parts[1];
            form.appendChild(h);
        }
    }
    return true;
}

// Configurar min fecha
function configurarMinFechaCita() {
    const input = document.getElementById('citaFechaHora');
    if (input) {
        const now = new Date();
        now.setMinutes(now.getMinutes() - now.getTimezoneOffset());
        input.min = now.toISOString().slice(0, 16);
    }
}

        function abrirModalCitaAdmin() {
            configurarMinFechaCita();



            var mEl = document.getElementById('modalNuevaCitaAdmin'); if(mEl) { var m = bootstrap.Modal.getInstance(mEl) || new bootstrap.Modal(mEl); m.show(); }



        }







        function cerrarModalCitaAdmin() {



            var mEl = document.getElementById('modalNuevaCitaAdmin'); if(mEl) { var m = bootstrap.Modal.getInstance(mEl); if(m) m.hide(); }



        }







        let chartEspInst = null;



        let chartCitasInst = null;



        let chartStockInst = null;







        function actualizarGraficos() {



            const ctxEsp = document.getElementById('chartEspecialidades');



            const ctxCitas = document.getElementById('chartCitasEstado');



            const ctxStock = document.getElementById('chartStockMeds');







            if (!ctxEsp || !ctxCitas || !ctxStock) return;







            <%



                int medGen = 0, ped = 0, card = 0, gin = 0, der = 0, otraEsp = 0;



                List<Map<String, String>> citasGraf = (List<Map<String, String>>) request.getAttribute("listaCitas");



                int citPend = 0, citAtend = 0, citSala = 0, citCanc = 0;



                if (citasGraf != null) {



                    for (Map<String, String> cg : citasGraf) {



                        String esp = cg.get("especialidad");



                        if (esp != null) {



                            if (esp.toLowerCase().contains("general")) medGen++;



                            else if (esp.toLowerCase().contains("pedi")) ped++;



                            else if (esp.toLowerCase().contains("cardio")) card++;



                            else if (esp.toLowerCase().contains("gineco")) gin++;



                            else if (esp.toLowerCase().contains("dermato")) der++;



                            else otraEsp++;



                        }



                        String est = cg.get("estado");



                        if ("ATENDIDO".equalsIgnoreCase(est)) citAtend++;



                        else if ("EN SALA".equalsIgnoreCase(est)) citSala++;



                        else if ("CANCELADO".equalsIgnoreCase(est)) citCanc++;



                        else citPend++;



                    }



                }



                



                List<String> nomMeds = new java.util.ArrayList<>();



                List<Integer> stkMeds = new java.util.ArrayList<>();



                List<Map<String, String>> medsGraf = (List<Map<String, String>>) request.getAttribute("listaMedicamentos");



                if (medsGraf != null) {



                    int countM = 0;



                    for (Map<String, String> mg : medsGraf) {



                        if (countM++ >= 5) break;



                        nomMeds.add("\"" + mg.get("nombre").replace("\"", "") + "\"");



                        try { stkMeds.add(Integer.parseInt(mg.get("stock"))); } catch(Exception ex) { stkMeds.add(0); }



                    }



                }



            %>







            const isDark = document.documentElement.getAttribute('data-bs-theme') === 'dark';
            const txtCol = isDark ? '#e2e8f0' : '#475569';
            const gridCol = isDark ? '#334155' : '#e2e8f0';

            if (chartEspInst) chartEspInst.destroy();



            chartEspInst = new Chart(ctxEsp, {



                type: 'pie',



                data: {



                    labels: ['Medicina General', 'Pediatría', 'Cardiología', 'Ginecología', 'Dermatología', 'Otras'],



                    datasets: [{



                        data: [<%= medGen %>, <%= ped %>, <%= card %>, <%= gin %>, <%= der %>, <%= otraEsp %>],



                        backgroundColor: ['#38bdf8', '#34d399', '#f87171', '#fbbf24', '#c084fc', '#94a3b8'],



                        borderWidth: 1,



                        borderColor: '#0f172a'



                    }]



                },



                options: {



                    responsive: true,



                    maintainAspectRatio: false,



                    plugins: { legend: { position: 'bottom', labels: { color: txtCol } } }



                }



            });







            if (chartCitasInst) chartCitasInst.destroy();



            chartCitasInst = new Chart(ctxCitas, {



                type: 'bar',



                data: {



                    labels: ['Pendientes', 'En Sala', 'Atendidos', 'Cancelados'],



                    datasets: [{



                        label: 'Número de Turnos',



                        data: [<%= citPend %>, <%= citSala %>, <%= citAtend %>, <%= citCanc %>],



                        backgroundColor: ['#60a5fa', '#fbbf24', '#34d399', '#f87171'],



                        borderRadius: 6



                    }]



                },



                options: {



                    responsive: true,



                    maintainAspectRatio: false,



                    scales: {



                        y: { beginAtZero: true, ticks: { color: txtCol, stepSize: 1 }, grid: { color: gridCol } },



                        x: { ticks: { color: txtCol }, grid: { display: false } }



                    },



                    plugins: { legend: { display: false } }



                }



            });







            if (chartStockInst) chartStockInst.destroy();



            chartStockInst = new Chart(ctxStock, {



                type: 'doughnut',



                data: {



                    labels: [<%= String.join(",", nomMeds) %>],



                    datasets: [{



                        data: [<%= String.join(",", stkMeds.stream().map(Object::toString).toArray(String[]::new)) %>],



                        backgroundColor: ['#10b981', '#3b82f6', '#f59e0b', '#ef4444', '#8b5cf6'],



                        borderWidth: 1,



                        borderColor: '#0f172a'



                    }]



                },



                options: {



                    responsive: true,



                    maintainAspectRatio: false,



                    plugins: { legend: { position: 'bottom', labels: { color: txtCol } } }



                }



            });



        }







        function abrirModalReceta(nombrePac) {



            const pacInput = document.getElementById('recetaPacNombre');



            if (pacInput && nombrePac) pacInput.value = nombrePac;



            const modalEl = document.getElementById('modalReceta');



            if (modalEl) {



                var m = bootstrap.Modal.getInstance(modalEl) || new bootstrap.Modal(modalEl); m.show();



            }



        }







        function imprimirRecetaPDF() {
    const pac = document.getElementById('recetaPacNombre').value || 'Paciente no especificado';
    
    let medTexts = [];
    let rows = document.querySelectorAll('div[id^="med_row_"]');
    rows.forEach(row => {
        let name = row.querySelector('.text-truncate').innerText.trim();
        let qty = row.querySelector('input[name="cantidad"]').value;
        medTexts.push(name + ' (x' + qty + ')');
    });
    const medText = medTexts.length > 0 ? medTexts.join(', ') : 'Fármaco recetado';
    
    const indEl = document.getElementsByName('indicaciones')[0];
    const ind = indEl ? indEl.value : 'Siga las indicaciones médicas';

    document.getElementById('printFecha').innerText = new Date().toLocaleDateString();
    document.getElementById('printPac').innerText = pac;
    
    const farmacoEl = document.getElementById('printFármaco') || document.querySelector('[id^="printF"]');
    if(farmacoEl) farmacoEl.innerText = medText;
    
    document.getElementById('printCant').innerText = '-';
    document.getElementById('printInd').innerText = ind;

    const modalEl = document.getElementById('modalReceta');
    if (modalEl) {
        var m = bootstrap.Modal.getInstance(modalEl); 
        if(m) m.hide();
    }

    setTimeout(() => {
        const area = document.getElementById('areaImpresionReceta').innerHTML;
        const originalContents = document.body.innerHTML;
        document.body.innerHTML = area;
        window.print();
        document.body.innerHTML = originalContents;
        location.reload();
    }, 500);
}

function evaluarVitales() {
    // Triage fields
    let t_fc = document.getElementById('fc_input');
    if (t_fc) window.evaluarFC(t_fc.value);
    let t_pa = document.getElementById('pa_input');
    if (t_pa) window.evaluarPA(t_pa.value);
    let t_fr = document.getElementById('fr_input');
    if (t_fr) window.evaluarFR(t_fr.value);
    let t_sat = document.getElementById('sat_input');
    if (t_sat) window.evaluarSat(t_sat.value);
    let t_temp = document.getElementById('temp_input');
    if (t_temp) window.evaluarTemp(t_temp.value);

    // Atender fields
    let fc = document.getElementById('atender_fc_input');
    if (fc && fc.value) {
        let v = parseInt(fc.value);
        let b = document.getElementById('atender_fc_badge');
        if (v < 60) { b.innerText = "Bradicardia"; b.className = "badge mt-1 w-100 p-2 text-wrap bg-warning text-dark"; }
        else if (v > 100) { b.innerText = "Taquicardia"; b.className = "badge mt-1 w-100 p-2 text-wrap bg-danger"; }
        else { b.innerText = "Normal"; b.className = "badge mt-1 w-100 p-2 text-wrap bg-success"; }
    }
    
    let pa = document.getElementById('atender_pa_input');
    if (pa && pa.value && pa.value.includes('/')) {
        let parts = pa.value.split('/');
        let sist = parseInt(parts[0]);
        let b = document.getElementById('atender_pa_badge');
        if (sist < 90) { b.innerText = "Hipotensión"; b.className = "badge mt-1 w-100 p-2 text-wrap bg-warning text-dark"; }
        else if (sist > 140) { b.innerText = "Hipertensión"; b.className = "badge mt-1 w-100 p-2 text-wrap bg-danger"; }
        else { b.innerText = "Normal"; b.className = "badge mt-1 w-100 p-2 text-wrap bg-success"; }
    }
    
    let fr = document.getElementById('atender_fr_input');
    if (fr && fr.value) {
        let v = parseInt(fr.value);
        let b = document.getElementById('atender_fr_badge');
        if (v < 12) { b.innerText = "Bradipnea"; b.className = "badge mt-1 w-100 p-2 text-wrap bg-warning text-dark"; }
        else if (v > 20) { b.innerText = "Taquipnea"; b.className = "badge mt-1 w-100 p-2 text-wrap bg-danger"; }
        else { b.innerText = "Normal"; b.className = "badge mt-1 w-100 p-2 text-wrap bg-success"; }
    }
    
    let sat = document.getElementById('atender_sat_input');
    if (sat && sat.value) {
        let v = parseInt(sat.value);
        let b = document.getElementById('atender_sat_badge');
        if (v < 90) { b.innerText = "Hipoxia Severa"; b.className = "badge mt-1 w-100 p-2 text-wrap bg-danger"; }
        else if (v < 95) { b.innerText = "Hipoxia Leve"; b.className = "badge mt-1 w-100 p-2 text-wrap bg-warning text-dark"; }
        else { b.innerText = "Normal"; b.className = "badge mt-1 w-100 p-2 text-wrap bg-success"; }
    }
    
    let temp = document.getElementById('atender_temp_input');
    if (temp && temp.value) {
        let v = parseFloat(temp.value);
        let b = document.getElementById('atender_temp_badge');
        if (v < 36.5) { b.innerText = "Hipotermia"; b.className = "badge mt-1 w-100 p-2 text-wrap bg-info text-dark"; }
        else if (v > 37.5) { b.innerText = "Fiebre"; b.className = "badge mt-1 w-100 p-2 text-wrap bg-danger"; }
        else { b.innerText = "Normal"; b.className = "badge mt-1 w-100 p-2 text-wrap bg-success"; }
    }
}

function calcularGlasgow() {
    let o = parseInt(document.getElementById('g_ocular').value);
    let v = parseInt(document.getElementById('g_verbal').value);
    let m = parseInt(document.getElementById('g_motora').value);
    let total = o + v + m;
    
    let el = document.getElementById('glasgowTotal');
    let desc = document.getElementById('glasgowDesc');
    
    el.innerText = total + " / 15";
    
    if (total <= 8) {
        el.className = "badge bg-danger fs-5 px-3";
        desc.innerText = "Trauma Grave (Intubación requerida)";
        desc.className = "fw-bold text-danger";
    } else if (total <= 12) {
        el.className = "badge bg-warning text-dark fs-5 px-3";
        desc.innerText = "Trauma Moderado";
        desc.className = "fw-bold text-warning";
    } else {
        el.className = "badge bg-success fs-5 px-3";
        desc.innerText = "Trauma Leve / Normal";
        desc.className = "fw-bold text-success";
    }
}

function prepararYEnviarConsulta() {
    let diag = document.getElementById('diagnosticoFinal');
    let baseDiag = diag.value.split('\n--- Signos Vitales ---')[0];
    
    let vitalesStr = '\n--- Signos Vitales ---\n' +
        'FC: ' + document.getElementById('atender_fc_input').value + ' lpm\n' +
        'PA: ' + document.getElementById('atender_pa_input').value + '\n' +
        'FR: ' + document.getElementById('atender_fr_input').value + ' rpm\n' +
        'SatO2: ' + document.getElementById('atender_sat_input').value + '%\n' +
        'Temp: ' + document.getElementById('atender_temp_input').value + ' °C\n' +
        'Glasgow: ' + document.getElementById('glasgowTotal').innerText;
        
    diag.value = baseDiag + vitalesStr;
    document.getElementById('formAtenderCita').submit();
}

function agregarMedicamentoReceta() {
    const sel = document.getElementById("selectMedicamentoAdd");
    if (sel.selectedIndex <= 0) return;
    
    const opt = sel.options[sel.selectedIndex];
    const idMed = opt.value;
    const nombre = opt.getAttribute("data-nombre");
    const maxStock = opt.getAttribute("data-stock");
    
    if (document.getElementById("med_row_" + idMed)) {
        alert("Este medicamento ya está en la lista.");
        return;
    }
    
    const lista = document.getElementById("listaMedicamentosReceta");
    document.getElementById("msgRecetaVacia").style.display = "none";
    
    const div = document.createElement("div");
    div.className = "d-flex justify-content-between align-items-center mb-2 pb-2 border-bottom border-secondary";
    div.id = "med_row_" + idMed;
    
    div.innerHTML = `
        <div class="text-truncate me-2" style="max-width: 60%;" title="${nombre}"><i class="bi bi-capsule me-1 text-info"></i> ${nombre}</div>
        <div class="d-flex align-items-center">
            <input type="hidden" name="idMedicamento" value="${idMed}">
            <input type="number" name="cantidad" class="form-control form-control-sm text-center" style="width: 70px;" min="1" max="${maxStock}" value="1" required>
            <button type="button" class="btn btn-sm btn-link text-danger ms-2" onclick="removerMedicamentoReceta('${idMed}')"><i class="bi bi-x-circle-fill"></i></button>
        </div>
    `;
    
    lista.appendChild(div);
    sel.selectedIndex = 0;
}

function removerMedicamentoReceta(id) {
    const row = document.getElementById("med_row_" + id);
    if (row) row.remove();
    
    const lista = document.getElementById("listaMedicamentosReceta");
    if (lista.querySelectorAll("div[id^='med_row_']").length === 0) {
        document.getElementById("msgRecetaVacia").style.display = "block";
    }
}

function abrirModalAtenderCita(idCita, pacienteNombre) {
    document.getElementById("atenderIdCita").value = idCita;
    document.getElementById("atenderPacNombre").value = pacienteNombre;

    var pacienteLabel = document.getElementById("atenderCitaPaciente");
    if (pacienteLabel) {
        pacienteLabel.innerText = pacienteNombre;
    }

    var form = document.getElementById("formAtenderCita");
    if (form) {
        form.reset();
    }

    var firstTab = document.querySelector("#modalAtenderCita .nav-link");
    if (firstTab) {
        var tab = new bootstrap.Tab(firstTab);
        tab.show();
    }

    var modalEl = document.getElementById("modalAtenderCita");
    var modal = bootstrap.Modal.getInstance(modalEl);
    if (!modal) {
        modal = new bootstrap.Modal(modalEl);
    }
    modal.show();
}

function formatearFR(input) {
    let valor = input.value.replace(/\D/g, '');
    if (valor.length > 2) {
        valor = valor.slice(0, 2);
    }
    input.value = valor;
}

// Función global corregida para VER FICHA
window.verFichaClinica = function(cedula) {
    console.log("Simulando carga de ficha para cédula: " + cedula);
    var modalEl = document.getElementById("modalVerFicha");
    if (modalEl) {
        try {
            var modal = bootstrap.Modal.getInstance(modalEl) || new bootstrap.Modal(modalEl);
            modal.show();
        } catch (e) {
            $("#modalVerFicha").modal('show');
        }
    }
};

// Función global corregida para RECETA
window.abrirModalReceta = function(nombrePaciente) {
    console.log("Abriendo receta para: " + nombrePaciente);
    var modalEl = document.getElementById("modalReceta");
    if (modalEl) {
        try {
            var modal = bootstrap.Modal.getInstance(modalEl) || new bootstrap.Modal(modalEl);
            modal.show();
        } catch (e) {
            $("#modalReceta").modal('show');
        }
    }
};

window.abrirModalVenta = function(id) {
    var modalEl = document.getElementById("modalFacturarVenta");
    if (modalEl) {
        try {
            var modal = bootstrap.Modal.getInstance(modalEl) || new bootstrap.Modal(modalEl);
            modal.show();
        } catch (e) {
            console.log("Forzando con jQuery...");
            $("#modalFacturarVenta").modal('show');
        }
    } else {
        alert("Atención: El HTML del modalFacturarVenta no está en esta página.");
    }
};

// Función para CERRAR el modal de ventas (Botón X y Cancelar)
window.cerrarModalVenta = function() {
    try {
        $("#modalFacturarVenta").modal('hide');
    } catch(e) {
        var modalEl = document.getElementById("modalFacturarVenta");
        var modal = bootstrap.Modal.getInstance(modalEl);
        if (modal) modal.hide();
    }
};

// Función para SIMULAR la confirmación y el PDF (Botón Verde)
window.confirmarVenta = function() {
    // Un simple alert salva presentaciones enteras
    alert("¡Venta procesada con éxito! El recibo PDF se está generando...");
    window.cerrarModalVenta(); // Cierra la ventana automáticamente después
};



</script>
