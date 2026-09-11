

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







        // AJAX para autocompletar Paciente por cédula



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







            // Validar Saturaci n



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



            if(confirm(' ¿Estás seguro de que deseas eliminar este ' + tipo + '? Esta acción no se puede deshacer.')) {



                document.getElementById('adminActionType').value = 'eliminar';



                document.getElementById('adminActionTarget').value = tipo;



                document.getElementById('adminActionId').value = id;



                document.getElementById('formAdminAction').submit();



            }



        }







        function abrirModalRol(correo, rolActual) {



            document.getElementById('rolUserEmail').innerText = correo;



            document.getElementById('rolSelectModal').value = rolActual;



            document.getElementById('modalRol').classList.add('show');



            document.getElementById('modalRol').style.display = 'block';



            document.getElementById('modalRol').style.backgroundColor = 'rgba(0,0,0,0.5)';



        }







        function cerrarModalRol() {



            document.getElementById('modalRol').classList.remove('show');



            document.getElementById('modalRol').style.display = 'none';



        }







        function abrirModalNuevoRol() {



            document.getElementById('modalNuevoRol').classList.add('show');



            document.getElementById('modalNuevoRol').style.display = 'block';



            document.getElementById('modalNuevoRol').style.backgroundColor = 'rgba(0,0,0,0.5)';



        }







        function cerrarModalNuevoRol() {



            document.getElementById('modalNuevoRol').classList.remove('show');



            document.getElementById('modalNuevoRol').style.display = 'none';



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



                document.getElementById('inputNombreRol').value = 'médico Triage';



                document.getElementById('inputDescRol').value = 'Atenci n a pacientes, triage y citas médicas';



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



            document.getElementById('modalMedicamento').classList.add('show');



            document.getElementById('modalMedicamento').style.display = 'block';



            document.getElementById('modalMedicamento').style.backgroundColor = 'rgba(0,0,0,0.5)';



        }







        function cerrarModalMedicamento() {



            document.getElementById('modalMedicamento').classList.remove('show');



            document.getElementById('modalMedicamento').style.display = 'none';



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



            document.getElementById('modalEspecialidad').classList.add('show');



            document.getElementById('modalEspecialidad').style.display = 'block';



            document.getElementById('modalEspecialidad').style.backgroundColor = 'rgba(0,0,0,0.5)';



        }







        function cerrarModalEspecialidad() {



            document.getElementById('modalEspecialidad').classList.remove('show');



            document.getElementById('modalEspecialidad').style.display = 'none';



        }







        function abrirModalCatalogos(tipo) {



            document.getElementById('catIdEnf').value = '';



            document.getElementById('catIdAle').value = '';



            document.getElementById('catNombreEnf').value = '';



            document.getElementById('catDescEnf').value = '';



            document.getElementById('catNombreAle').value = '';



            document.getElementById('catGravAle').value = 'Leve';



            if (tipo === 'enfermedad') {



                document.getElementById('catModalTitulo').innerHTML = '<i class="bi bi-heart-pulse text-danger me-2"></i>Registrar Nueva Patolog a';



                document.getElementById('catActionInput').value = 'crearEnfermedad';



                document.getElementById('catEnfermedadCampos').classList.remove('d-none');



                document.getElementById('catAlergiaCampos').classList.add('d-none');



                document.getElementById('catNombreEnf').required = true;



                document.getElementById('catNombreAle').required = false;



            } else {



                document.getElementById('catModalTitulo').innerHTML = '<i class="bi bi-exclamation-diamond text-warning me-2"></i>Registrar Nuevo Al rgeno';



                document.getElementById('catActionInput').value = 'crearAlergia';



                document.getElementById('catEnfermedadCampos').classList.add('d-none');



                document.getElementById('catAlergiaCampos').classList.remove('d-none');



                document.getElementById('catNombreEnf').required = false;



                document.getElementById('catNombreAle').required = true;



            }



            document.getElementById('modalCatalogos').classList.add('show');



            document.getElementById('modalCatalogos').style.display = 'block';



            document.getElementById('modalCatalogos').style.backgroundColor = 'rgba(0,0,0,0.5)';



        }







        function abrirModalEditarEnfermedad(id, nombre, desc) {



            document.getElementById('catModalTitulo').innerHTML = '<i class="bi bi-pencil-square text-danger me-2"></i>Editar Patolog a / Enfermedad';



            document.getElementById('catActionInput').value = 'editarEnfermedad';



            document.getElementById('catIdEnf').value = id;



            document.getElementById('catNombreEnf').value = nombre;



            document.getElementById('catDescEnf').value = desc;



            document.getElementById('catEnfermedadCampos').classList.remove('d-none');



            document.getElementById('catAlergiaCampos').classList.add('d-none');



            document.getElementById('catNombreEnf').required = true;



            document.getElementById('catNombreAle').required = false;



            document.getElementById('modalCatalogos').classList.add('show');



            document.getElementById('modalCatalogos').style.display = 'block';



            document.getElementById('modalCatalogos').style.backgroundColor = 'rgba(0,0,0,0.5)';



        }







        function abrirModalEditarAlergia(id, nombre, grav) {



            document.getElementById('catModalTitulo').innerHTML = '<i class="bi bi-pencil-square text-warning me-2"></i>Editar Al rgeno';



            document.getElementById('catActionInput').value = 'editarAlergia';



            document.getElementById('catIdAle').value = id;



            document.getElementById('catNombreAle').value = nombre;



            document.getElementById('catGravAle').value = grav;



            document.getElementById('catEnfermedadCampos').classList.add('d-none');



            document.getElementById('catAlergiaCampos').classList.remove('d-none');



            document.getElementById('catNombreEnf').required = false;



            document.getElementById('catNombreAle').required = true;



            document.getElementById('modalCatalogos').classList.add('show');



            document.getElementById('modalCatalogos').style.display = 'block';



            document.getElementById('modalCatalogos').style.backgroundColor = 'rgba(0,0,0,0.5)';



        }







        function borrarCatalogo(tipo, id, nombre) {



            if (confirm(' ¿Estás seguro de eliminar "' + nombre + '" del catálogo clínico?')) {



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



            document.getElementById('modalCatalogos').classList.remove('show');



            document.getElementById('modalCatalogos').style.display = 'none';



        }







        let cedulaFichaActual = '';



        function verFichaClinica(cedula) {



            cedulaFichaActual = cedula;



            fetch('registroPaciente?action=buscarCedula&cedula=' + encodeURIComponent(cedula))



                .then(r => r.json())



                .then(data => {



                    if (data && data.encontrado) {



                        document.getElementById('fichaNombre').innerText = data.nombres + ' ' + data.apellidos;



                        document.getElementById('fichaInfo').innerText = 'Cédula: ' + cedula + ' | Nacimiento: ' + (data.fechaNacimiento || 'N/D') + ' | Sexo: ' + (data.sexo || 'N/D');



                        



                        let est = parseFloat(data.estatura || 0);



                        let peso = parseFloat(data.peso || 0);



                        let temp = parseFloat(data.temperatura || 0);



                        let fc = parseInt(data.fc || 0);



                        let sat = parseInt(data.sat || 0);



                        let pres = data.presion || '120/80';







                        document.getElementById('fichaEstPeso').innerText = (est > 0 ? est + ' m' : '-- m') + ' / ' + (peso > 0 ? peso + ' kg' : '-- kg');



                        document.getElementById('fichaTemp').innerText = temp > 0 ? temp + ' °C' : '-- °C';



                        document.getElementById('fichaPresion').innerText = pres;



                        document.getElementById('fichaFcSat').innerText = (fc > 0 ? fc + ' lpm' : '--') + ' / ' + (sat > 0 ? sat + '%' : '--');



                        document.getElementById('fichaEnfermedades').innerText = data.enfermedad || 'Ninguna preexistente';



                        document.getElementById('fichaAlergias').innerText = data.alergias || 'Ninguna reportada';







                        // cálculo de Diagnóstico Inteligente (Task 4)



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



                                <div><i class="bi bi-exclamation-triangle-fill text-danger me-2 fs-5"></i><strong class="text-theme">ALERTA T RMICA cR TICA: Fiebre Alta / Hipertermia (${temp} c)</strong><br><small class="text-theme">Protocolo de reducci n t rmica inmediata y monitoreo antit rmico sugerido.</small></div>



                                <span class="badge bg-danger pulse-animation px-3 py-2 fs-6">  HIPERTERMIA</span>



                            </div>`;



                        } else if (temp >= 37.3 && temp < 38.0) {



                            alertasHTML += `<div class="p-3 mb-2 rounded d-flex align-items-center justify-content-between" style="background: rgba(245, 158, 11, 0.15); border-left: 4px solid #f59e0b;">



                                <div><strong class="text-warning"><i class="bi bi-exclamation-circle me-1"></i> Febr cula detectada (${temp} c)</strong><br><small class="text-secondary">Monitoreo peri dico cada 2 horas.</small></div>



                                <span class="badge bg-warning text-dark px-3 py-2">  Febr cula</span>



                            </div>`;



                        }







                        if (sat > 0 && sat < 92) {



                            alertasHTML += `<div class="p-3 mb-2 rounded d-flex align-items-center justify-content-between" style="background: rgba(239, 68, 68, 0.2); border: 1px solid #ef4444;">



                                <div><i class="bi bi-lungs-fill text-danger me-2 fs-5"></i><strong class="text-theme">HIPOXIA SEVERA DETECTADA (Sat O2: ${sat}%)</strong><br><small class="text-theme">Administraci n urgente de ox geno suplementario requerida.</small></div>



                                <span class="badge bg-danger px-3 py-2 fs-6">  HIPOXIA</span>



                            </div>`;



                        }







                        if (alertasHTML === '') {



                            alertasHTML = `<div class="p-3 mb-2 rounded text-center" style="background: rgba(16, 185, 129, 0.15); border: 1px solid #10b981;">



                                <i class="bi bi-check-circle-fill text-success me-2"></i><strong class="text-theme">Par metros vitales dentro de rangos clinicos estables y normales.</strong>



                            </div>`;



                        }







                        document.getElementById('fichaAlertasContenedor').innerHTML = alertasHTML;







                        document.getElementById('modalFichaClinica').classList.add('show');



                        document.getElementById('modalFichaClinica').style.display = 'block';



                        document.getElementById('modalFichaClinica').style.backgroundColor = 'rgba(0,0,0,0.6)';



                    } else {



                        alert('No se encontraron los datos del paciente.');



                    }



                })



                .catch(err => console.error(err));



        }







        function cerrarModalFicha() {



            document.getElementById('modalFichaClinica').classList.remove('show');



            document.getElementById('modalFichaClinica').style.display = 'none';



        }







        function editarPacienteDesdeFicha() {



            cerrarModalFicha();



            if(cedulaFichaActual) {



                editarPaciente(cedulaFichaActual);



            }



        }







        function abrirModalCitaAdmin() {



            document.getElementById('modalNuevaCitaAdmin').classList.add('show');



            document.getElementById('modalNuevaCitaAdmin').style.display = 'block';



            document.getElementById('modalNuevaCitaAdmin').style.backgroundColor = 'rgba(0,0,0,0.5)';



        }







        function cerrarModalCitaAdmin() {



            document.getElementById('modalNuevaCitaAdmin').classList.remove('show');



            document.getElementById('modalNuevaCitaAdmin').style.display = 'none';



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



                        data: [, , , , , ],



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



                        label: 'N mero de Turnos',



                        data: [, , , ],



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



                    labels: [],



                    datasets: [{



                        data: [],



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



                modalEl.classList.add('show');



                modalEl.style.display = 'block';



                modalEl.style.backgroundColor = 'rgba(0,0,0,0.6)';



            }



        }







        function imprimirRecetaPDF() {



            const pac = document.getElementById('recetaPacNombre').value || 'Paciente no especificado';



            const medSel = document.getElementById('recetaIdMed');



            const medText = medSel && medSel.selectedIndex > 0 ? medSel.options[medSel.selectedIndex].text : 'Fármaco recetado';



            const cant = document.getElementById('recetaCantidad').value || '1';



            const ind = document.getElementById('recetaIndicaciones').value || 'Siga las indicaciones médicas';







            document.getElementById('printFecha').innerText = new Date().toLocaleDateString();



            document.getElementById('printPac').innerText = pac;



            document.getElementById('printFarmaco').innerText = medText;



            document.getElementById('printCant').innerText = cant;



            document.getElementById('printInd').innerText = ind;







            const modalEl = document.getElementById('modalReceta');



            if (modalEl) {



                modalEl.classList.remove('show');



                modalEl.style.display = 'none';



            }







            const areaPrint = document.getElementById('areaImpresionReceta');



            if (areaPrint) {



                areaPrint.classList.remove('d-none');



                window.print();



                areaPrint.classList.add('d-none');



            }



        }







        function abrirModalInternar(idCama, numCama, salaCama) {



            document.getElementById('internarIdCama').value = idCama;



            document.getElementById('internarCamaNumLabel').innerText = '#' + numCama;



            document.getElementById('internarSalaLabel').value = salaCama;



            



            const modalEl = document.getElementById('modalInternarCama');



            if (modalEl) {



                modalEl.classList.add('show');



                modalEl.style.display = 'block';



                modalEl.style.backgroundColor = 'rgba(0,0,0,0.6)';



            }



        }







        function confirmarAltaCama(idCama, numCama, paciente) {



            if (confirm(` confirmas el alta médica de la cama #${numCama} del paciente ${paciente}?`)) {



                const form = document.createElement('form');



                form.method = 'POST';



                form.action = 'camasAction';



                



                const inputAction = document.createElement('input');



                inputAction.type = 'hidden';



                inputAction.name = 'action';



                inputAction.value = 'liberar';



                form.appendChild(inputAction);



                



                const inputId = document.createElement('input');



                inputId.type = 'hidden';



                inputId.name = 'camaId';



                inputId.value = idCama;



                form.appendChild(inputId);



                



                document.body.appendChild(form);



                form.submit();



            }



        }







        function cambiarEstadoCama(idCama, nuevoEstado) {



            window.location.href = `adminAction?action=cambiarEstadoCama&idCama=${idCama}&estado=${nuevoEstado}`;



        }







        document.addEventListener('DOMContentLoaded', function() {



            document.querySelectorAll('#modalReceta .btn-close, #modalReceta .btn-secondary').forEach(btn => {



                btn.addEventListener('click', () => {



                    const m = document.getElementById('modalReceta');



                    if(m) { m.classList.remove('show'); m.style.display = 'none'; }



                });



            });



            document.querySelectorAll('#modalInternarCama .btn-close, #modalInternarCama .btn-secondary').forEach(btn => {



                btn.addEventListener('click', () => {



                    const m = document.getElementById('modalInternarCama');



                    if(m) { m.classList.remove('show'); m.style.display = 'none'; }



                });



            });



        });







        function setTheme(theme) {



            localStorage.setItem('nurselogic_theme', theme);



            applyTheme(theme);



        }







        function applyTheme(theme) {



            let actualTheme = theme;



            if (theme === 'auto') {



                actualTheme = window.matchMedia('(prefers-color-scheme: light)').matches ? 'light' : 'dark';



            }



            document.documentElement.setAttribute('data-bs-theme', actualTheme);







            if (typeof actualizarGraficos === 'function') {



                actualizarGraficos();



            }







            let iconDash = document.getElementById('themeIconDash');



            let labelDash = document.getElementById('themeLabelDash');



            let iconClass = 'bi-moon-stars-fill';



            let labelText = 'Oscuro';



            if (theme === 'light') { iconClass = 'bi-sun-fill'; labelText = 'Claro'; }



            else if (theme === 'auto') { iconClass = 'bi-display'; labelText = 'Auto'; }







            if (iconDash) iconDash.className = 'bi ' + iconClass;



            if (labelDash) labelDash.innerText = labelText;



        }







        (function() {



            let savedTheme = localStorage.getItem('nurselogic_theme') || 'auto';



            applyTheme(savedTheme);



            window.matchMedia('(prefers-color-scheme: light)').addEventListener('change', e => {



                if (localStorage.getItem('nurselogic_theme') === 'auto') {



                    applyTheme('auto');



                }



            });



        })();



        function abrirModalAtenderCita(idCita, pacienteNombre) {



            document.getElementById('atenderIdCita').value = idCita;
            document.getElementById('atenderCitaPaciente').innerText = pacienteNombre;



            var modal = new bootstrap.Modal(document.getElementById('modalAtenderCita'));



            modal.show();



        }



        function cerrarModalAtenderCita() {



            var modalEl = document.getElementById('modalAtenderCita');



            var modal = bootstrap.Modal.getInstance(modalEl);



            if(modal) modal.hide();



        }



        function buscarRecetaFarmacia() {



            const cedula = document.getElementById('cedulaFarmaciaBuscador').value.trim();



            if(!cedula) return;



            



            fetch('api/receta?cedula=' + cedula)



                .then(response => response.json())



                .then(data => {



                    const container = document.getElementById('recetaFarmaciaContainer');



                    const notFound = document.getElementById('recetaFarmaciaNotFound');



                    



                    if(data.success) {



                        notFound.classList.add('d-none');



                        container.classList.remove('d-none');



                        document.getElementById('farmaciaPacienteNombre').innerText = data.pacienteNombre;



                        document.getElementById('farmaciaFechaCita').innerText = data.fecha;



                        document.getElementById('farmaciaRecetaContenido').innerText = data.receta;



                    } else {



                        container.classList.add('d-none');



                        notFound.classList.remove('d-none');



                        notFound.innerHTML = '<i class="bi bi-exclamation-triangle-fill me-2"></i> ' + data.message;



                    }



                })



                .catch(err => {



                    alert('Error de conexi n');



                });



        }



        // L gica de consulta médica Avanzada



        function evaluarFC(val) {



            const v = parseInt(val);



            const badge = document.getElementById('fc_badge');



            if(isNaN(v)) { badge.className='badge bg-secondary mt-1 w-100'; badge.innerText='Esperando...'; return; }



            if(v < 60) { badge.className='badge bg-warning text-dark mt-1 w-100'; badge.innerText='Bradicardia'; }



            else if(v <= 100) { badge.className='badge bg-success mt-1 w-100'; badge.innerText='Normocardia'; }



            else { badge.className='badge bg-danger mt-1 w-100'; badge.innerText='Taquicardia'; }



        }



        function evaluarPA(val) {



            const badge = document.getElementById('pa_badge');



            if(!val.includes('/')) { badge.className='badge bg-secondary mt-1 w-100'; badge.innerText='Esperando...'; return; }



            const parts = val.split('/');



            const sist = parseInt(parts[0]);



            if(isNaN(sist)) return;



            if(sist < 90) { badge.className='badge bg-warning text-dark mt-1 w-100'; badge.innerText='Hipotensi n'; }



            else if(sist <= 120) { badge.className='badge bg-success mt-1 w-100'; badge.innerText='Normotensi n'; }



            else if(sist <= 139) { badge.className='badge bg-warning text-dark mt-1 w-100'; badge.innerText='Prehipertensi n'; }



            else { badge.className='badge bg-danger mt-1 w-100'; badge.innerText='Hipertensi n'; }



        }



        function evaluarFR(val) {



            const v = parseInt(val);



            const badge = document.getElementById('fr_badge');



            if(isNaN(v)) { badge.className='badge bg-secondary mt-1 w-100'; badge.innerText='Esperando...'; return; }



            if(v < 12) { badge.className='badge bg-warning text-dark mt-1 w-100'; badge.innerText='Bradipnea'; }



            else if(v <= 20) { badge.className='badge bg-success mt-1 w-100'; badge.innerText='Eupnea'; }



            else { badge.className='badge bg-danger mt-1 w-100'; badge.innerText='Taquipnea'; }



        }



        function evaluarSat(val) {



            const v = parseInt(val);



            const badge = document.getElementById('sat_badge');



            if(isNaN(v)) { badge.className='badge bg-secondary mt-1 w-100'; badge.innerText='Esperando...'; return; }



            if(v >= 95) { badge.className='badge bg-success mt-1 w-100'; badge.innerText='Normal'; }



            else if(v >= 90) { badge.className='badge bg-warning text-dark mt-1 w-100'; badge.innerText='Hipoxia Leve'; }



            else { badge.className='badge bg-danger mt-1 w-100'; badge.innerText='Hipoxia Severa'; }



        }



        function evaluarTemp(val) {



            const v = parseFloat(val);



            const badge = document.getElementById('temp_badge');



            if(isNaN(v)) { badge.className='badge bg-secondary mt-1 w-100'; badge.innerText='Esperando...'; return; }



            if(v < 36.5) { badge.className='badge bg-info mt-1 w-100'; badge.innerText='Hipotermia'; }



            else if(v <= 37.5) { badge.className='badge bg-success mt-1 w-100'; badge.innerText='Afebril'; }



            else if(v <= 38.3) { badge.className='badge bg-warning text-dark mt-1 w-100'; badge.innerText='Febr cula'; }



            else { badge.className='badge bg-danger mt-1 w-100'; badge.innerText='Fiebre'; }



        }



        



        function calcularGlasgow() {



            const o = parseInt(document.getElementById('g_ocular').value);



            const v = parseInt(document.getElementById('g_verbal').value);



            const m = parseInt(document.getElementById('g_motora').value);



            const total = o + v + m;



            document.getElementById('glasgowTotal').innerText = total + " / 15";



            



            const interp = document.getElementById('glasgowInterpretacion');



            if(total >= 14) { interp.innerText = "Trauma Leve / Normal"; interp.className = "text-end small fw-bold mt-1 text-success"; }



            else if(total >= 9) { interp.innerText = "Trauma Moderado"; interp.className = "text-end small fw-bold mt-1 text-warning"; }



            else { interp.innerText = "Trauma Severo (Coma)"; interp.className = "text-end small fw-bold mt-1 text-danger"; }



        }







        function prepararGuardadoConsulta(e) {



            const fc = document.getElementById('fc_input').value;



            const pa = document.getElementById('pa_input').value;



            const fr = document.getElementById('fr_input').value;



            const sat = document.getElementById('sat_input').value;



            const temp = document.getElementById('temp_input').value;



            



            const g_total = document.getElementById('glasgowTotal').innerText;



            const g_interp = document.getElementById('glasgowInterpretacion').innerText;



            



            const diagOrig = document.getElementById('diagnosticoFinal').value;



            



            let resumen = "==== SIGNOS VITALES ====\n";



            resumen += "FC: " + (fc ? fc + " lpm" : "N/D") + "\n";



            resumen += "PA: " + (pa ? pa + " mmHg" : "N/D") + "\n";



            resumen += "FR: " + (fr ? fr + " rpm" : "N/D") + "\n";



            resumen += "SatO2: " + (sat ? sat + "%" : "N/D") + "\n";



            resumen += "Temp: " + (temp ? temp + "°C" : "N/D") + "\n\n";



            



            resumen += "==== ESCALA GLASGOW ====\n";



            resumen += "Puntaje: " + g_total + " (" + g_interp + ")\n\n";



            



            resumen += "==== OBSERVACIONES cL NICAS ====\n";



            resumen += diagOrig;



            



            document.getElementById('diagnosticoFinal').value = resumen;



        }









        let currentVentaId = 0;

        let currentVentaPrecio = 0;

        let currentVentaStock = 0;



        function abrirModalVenta(id, nombre, precio, stock) {

            currentVentaId = id;

            currentVentaPrecio = precio;

            currentVentaStock = stock;

            

            document.getElementById('ventaNombreMed').value = nombre;

            document.getElementById('ventaMaxStock').innerText = stock;

            document.getElementById('ventaCantidad').value = 1;

            document.getElementById('ventaCantidad').max = stock;

            document.getElementById('ventaCliente').value = 'Consumidor Final';

            

            calcTotalVenta();

            

            const m = document.getElementById('modalFacturarVenta');

            if(m) {

                m.classList.add('show');

                m.style.display = 'block';

                m.style.backgroundColor = 'rgba(0,0,0,0.6)';

            }

        }



        function cerrarModalVenta() {

            const m = document.getElementById('modalFacturarVenta');

            if(m) {

                m.classList.remove('show');

                m.style.display = 'none';

            }

        }



        function calcTotalVenta() {

            let cant = parseInt(document.getElementById('ventaCantidad').value) || 1;

            if (cant > currentVentaStock) {

                cant = currentVentaStock;

                document.getElementById('ventaCantidad').value = cant;

            }

            if (cant < 1) {

                cant = 1;

                document.getElementById('ventaCantidad').value = cant;

            }

            let total = cant * currentVentaPrecio;

            document.getElementById('ventaTotal').value = '$ ' + total.toFixed(2);

        }



        function confirmarVenta() {

            let cant = parseInt(document.getElementById('ventaCantidad').value) || 1;

            let cliente = document.getElementById('ventaCliente').value || 'Consumidor Final';

            let medNombre = document.getElementById('ventaNombreMed').value;

            let total = cant * currentVentaPrecio;

            

            document.getElementById('facFecha').innerText = new Date().toLocaleString();

            document.getElementById('facCliente').innerText = cliente;

            document.getElementById('facCant').innerText = cant;

            document.getElementById('facDesc').innerText = medNombre;

            document.getElementById('facSubt').innerText = '$' + total.toFixed(2);

            document.getElementById('facTotal').innerText = total.toFixed(2);

            

            cerrarModalVenta();

            

            const areaPrint = document.getElementById('areaImpresionFactura');

            if (areaPrint) {

                const win = window.open('', '_blank');

                win.document.write('<html><head><title>Factura PDF</title></head><body>');

                win.document.write(areaPrint.innerHTML);

                win.document.write('</body></html>');

                win.document.close();

                win.print();

            }

            

            setTimeout(function() {

                document.getElementById('adminActionType').value = 'facturarVenta';

                document.getElementById('adminActionTarget').value = 'factura';

                document.getElementById('adminActionId').value = currentVentaId;

                

                let form = document.getElementById('formAdminAction');

                

                let inputCant = document.getElementById('adminActionFacturaCant');

                if (!inputCant) {

                    inputCant = document.createElement('input');

                    inputCant.type = 'hidden';

                    inputCant.name = 'cantidad';

                    inputCant.id = 'adminActionFacturaCant';

                    form.appendChild(inputCant);

                }

                inputCant.value = cant;



                let inputMedId = document.getElementById('adminActionFacturaMed');

                if (!inputMedId) {

                    inputMedId = document.createElement('input');

                    inputMedId.type = 'hidden';

                    inputMedId.name = 'idMed';

                    inputMedId.id = 'adminActionFacturaMed';

                    form.appendChild(inputMedId);

                }

                inputMedId.value = currentVentaId;



                let inputCliente = document.getElementById('adminActionFacturaCli');

                if (!inputCliente) {

                    inputCliente = document.createElement('input');

                    inputCliente.type = 'hidden';

                    inputCliente.name = 'cliente';

                    inputCliente.id = 'adminActionFacturaCli';

                    form.appendChild(inputCliente);

                }

                inputCliente.value = cliente;



                form.submit();

            }, 500);



        }
































