



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



            sessionStorage.setItem('ultima_vista_nurselogic', vistaId);
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
            Swal.fire({
                title: '¿Eliminar ' + tipo + '?',
                text: 'Esta acción no se puede deshacer.',
                icon: 'warning',
                showCancelButton: true,
                confirmButtonColor: '#d33',
                cancelButtonColor: '#3085d6',
                confirmButtonText: 'Sí, Eliminar',
                cancelButtonText: 'Cancelar',
                background: 'var(--bg-panel)',
                color: 'var(--text-color)'
            }).then((result) => {
                if (result.isConfirmed) {
                    var formData = new URLSearchParams();
                    formData.append("action", "eliminar");
                    formData.append("target", tipo);
                    formData.append("idEnf", id);
                    formData.append("idAle", id);
                    fetch('adminAction', {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
                        body: formData.toString()
                    }).then(function(response) {
                        Swal.fire({title: 'Eliminado', text: 'El registro ha sido eliminado exitosamente.', icon: 'success', background: 'var(--bg-panel)', color: 'var(--text-color)'}).then(() => {
                            window.location.href = "dashboard";
                        });
                    });
                }
            });
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
                c.style.background = 'rgba(255,255,255,0.05)';
                c.style.borderColor = 'rgba(255,255,255,0.2)';
            });
            if (el) {
                el.style.background = 'rgba(255, 193, 7, 0.15)';
                el.style.borderColor = '#ffc107';
            }

            document.querySelectorAll('.perm-checkbox').forEach(chk => chk.checked = false);

            const t = (tipo || '').toLowerCase().normalize("NFD").replace(/[\u0300-\u036f]/g, "");

            if (t === 'moderador') {
                document.querySelectorAll('.perm-checkbox').forEach(chk => {
                    if (chk.value === 'Usuarios') chk.checked = true;
                });
            } else if (t === 'bodeguero') {
                document.querySelectorAll('.perm-checkbox').forEach(chk => {
                    if (chk.value === 'Inventario') chk.checked = true;
                });
            } else if (t === 'medico') {
                document.querySelectorAll('.perm-checkbox').forEach(chk => {
                    if (chk.value === 'Citas' || chk.value === 'Admision') chk.checked = true;
                });
            }
        }







        // --- Funciones del Ecosistema Enriquecido (5 Tareas) ---



        function cambiarEstadoCita(idCita, nuevoEstado) {
            let executeChange = () => {
                var formData = new URLSearchParams();
                formData.append("action", "actualizarEstadoCita");
                formData.append("target", "cita");
                formData.append("id", idCita);
                formData.append("nuevoEstado", nuevoEstado);
                fetch('adminAction', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
                    body: formData.toString()
                }).then(function(response) {
                    Swal.fire({title: 'Actualizado', text: 'El estado de la cita ha sido actualizado a ' + nuevoEstado, icon: 'success', background: 'var(--bg-panel)', color: 'var(--text-color)'}).then(() => {
                        window.location.href = "dashboard";
                    });
                });
            };

            if (nuevoEstado === 'CANCELADO') {
                Swal.fire({
                    title: '¿Cancelar Cita?',
                    text: '¿Estás seguro de que deseas cancelar esta cita? Esta acción la moverá al historial de cancelados.',
                    icon: 'warning',
                    showCancelButton: true,
                    confirmButtonColor: '#d33',
                    cancelButtonColor: '#3085d6',
                    confirmButtonText: 'Sí, Cancelar',
                    cancelButtonText: 'No, mantener',
                    background: 'var(--bg-panel)',
                    color: 'var(--text-color)'
                }).then((result) => {
                    if (result.isConfirmed) {
                        executeChange();
                    }
                });
            } else {
                executeChange();
            }
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







        function cerrarModalEspecialidad() { var mEl = document.getElementById('modalEspecialidad'); if(mEl) { var m = bootstrap.Modal.getInstance(mEl); if(m) m.hide(); } }

        function abrirModalNuevaEspecialidad() { var mEl = document.getElementById('modalNuevaEspecialidad'); if(mEl) { var m = bootstrap.Modal.getInstance(mEl) || new bootstrap.Modal(mEl); m.show(); } }

        function cerrarModalNuevaEspecialidad() { var mEl = document.getElementById('modalNuevaEspecialidad'); if(mEl) { var m = bootstrap.Modal.getInstance(mEl); if(m) m.hide(); } }







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
            Swal.fire({
                title: '¿Eliminar del catálogo?',
                text: '¿Estás seguro de eliminar "' + nombre + '" del catálogo clínico?',
                icon: 'warning',
                showCancelButton: true,
                confirmButtonColor: '#d33',
                cancelButtonColor: '#3085d6',
                confirmButtonText: 'Sí, Eliminar',
                cancelButtonText: 'Cancelar',
                background: 'var(--bg-panel)',
                color: 'var(--text-color)'
            }).then((result) => {
                if (result.isConfirmed) {
                    var formData = new URLSearchParams();
                    formData.append("action", tipo === 'enfermedad' ? 'borrarEnfermedad' : 'borrarAlergia');
                    formData.append("idEnf", id);
                    formData.append("idAle", id);
                    fetch('adminAction', {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
                        body: formData.toString()
                    }).then(function(response) {
                        Swal.fire({title: 'Eliminado', text: 'El elemento ha sido eliminado.', icon: 'success', background: 'var(--bg-panel)', color: 'var(--text-color)'}).then(() => {
                            window.location.href = "dashboard";
                        });
                    });
                }
            });
        }

        function configurarMinFechaCita() {
            let input = document.getElementById('citaFechaHora');
            if (input) {
                let now = new Date();
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







            null







            const isDark = document.documentElement.getAttribute('data-bs-theme') === 'dark';
            const txtCol = isDark ? '#e2e8f0' : '#475569';
            const gridCol = isDark ? '#334155' : '#e2e8f0';

            if (chartEspInst) chartEspInst.destroy();



            chartEspInst = new Chart(ctxEsp, {
                type: 'pie',
                data: {
                    labels: [null],
                    datasets: [{
                        data: [null],
                        backgroundColor: ['#38bdf8', '#34d399', '#f87171', '#fbbf24', '#c084fc', '#94a3b8', '#f472b6', '#2dd4bf', '#a3e635', '#a78bfa'],
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



                        data: [null, null, null, null],



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



                    labels: [null],



                    datasets: [{



                        data: [null],



                        backgroundColor: ['#10b981', '#3b82f6', '#f59e0b', '#ef4444', '#8b5cf6', '#06b6d4', '#ec4899'],



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
    if (!sel || sel.selectedIndex <= 0) return;
    
    const opt = sel.options[sel.selectedIndex];
    const idMed = opt.value;
    let nombre = opt.getAttribute("data-nombre");
    if (!nombre || nombre === "null" || nombre.trim() === "") {
        nombre = opt.text ? opt.text.split("(Stock:")[0].trim() : "Medicamento";
    }
    nombre = nombre.trim();
    if (!nombre) nombre = "Medicamento #" + idMed;
    
    const maxStock = opt.getAttribute("data-stock") || 100;
    
    if (document.getElementById("med_row_" + idMed)) {
        Swal.fire({text: "Este medicamento ya está en la lista.", icon: 'info', background: 'var(--bg-panel)', color: 'var(--text-color)'});
        return;
    }
    
    const lista = document.getElementById("listaMedicamentosReceta");
    const msgVacio = document.getElementById("msgRecetaVacia");
    if (msgVacio) msgVacio.style.display = "none";
    
    const div = document.createElement("div");
    div.className = "d-flex justify-content-between align-items-center mb-2 pb-2 border-bottom border-secondary";
    div.id = "med_row_" + idMed;
    
    div.innerHTML = 
        '<div class="text-truncate me-2 fw-bold" style="max-width: 65%; color: #38bdf8 !important; font-size: 0.95rem;" title="' + nombre + '"><i class="bi bi-capsule me-2 text-warning fs-5"></i>' + nombre + '</div>' +
        '<div class="d-flex align-items-center">' +
            '<input type="hidden" name="idMedicamento" value="' + idMed + '" autocomplete="off">' +
            '<input type="number" name="cantidad" class="form-control form-control-sm text-center fw-bold" style="width: 70px;" min="1" max="' + maxStock + '" value="1" required autocomplete="off">' +
            '<button type="button" class="btn btn-sm btn-link text-danger ms-2 p-0" onclick="removerMedicamentoReceta(\'' + idMed + '\')"><i class="bi bi-x-circle-fill fs-5"></i></button>' +
        '</div>';
    
    lista.appendChild(div);
    sel.selectedIndex = 0;
}

window.validarFormularioReceta = function(event) {
    const rows = document.querySelectorAll('#listaMedicamentosReceta input[name="idMedicamento"]');
    if (rows.length === 0) {
        Swal.fire({text: "Debe seleccionar y añadir al menos un medicamento a la lista haciendo clic en '+ Añadir'.", icon: 'info', background: 'var(--bg-panel)', color: 'var(--text-color)'});
        if (event) event.preventDefault();
        return false;
    }
    return true;
};

// BUSQUEDA Y DESPACHO DE RECETA EN FARMACIA POR CEDULA
window.buscarRecetaFarmacia = function() {
    var cedulaInput = document.getElementById('cedulaFarmaciaBuscador');
    var cedula = cedulaInput ? cedulaInput.value.trim() : '';
    var container = document.getElementById('recetaFarmaciaContainer');
    var notFound = document.getElementById('recetaFarmaciaNotFound');
    
    if (!cedula || cedula.length < 10) {
        Swal.fire({text: "Por favor ingrese una cédula válida de 10 dígitos.", icon: 'info', background: 'var(--bg-panel)', color: 'var(--text-color)'});
        return;
    }
    
    fetch('api/receta?cedula=' + cedula)
        .then(r => r.json())
        .then(data => {
            if (data.success) {
                window.currentRecetaIdCita = data.idCita || '';
                window.currentRecetaCedula = cedula;

                if (container) container.classList.remove('d-none');
                if (notFound) notFound.classList.add('d-none');
                
                var nameEl = document.getElementById('farmaciaPacienteNombre');
                if (nameEl) nameEl.innerText = data.pacienteNombre;
                
                var fechaEl = document.getElementById('farmaciaFechaCita');
                if (fechaEl) fechaEl.innerText = data.fecha;
                
                var contentEl = document.getElementById('farmaciaRecetaContenido');
                if (contentEl) {
                    contentEl.innerHTML = '<strong>' + data.receta + '</strong>';
                }
            } else {
                window.currentRecetaIdCita = '';
                window.currentRecetaCedula = '';
                if (container) container.classList.add('d-none');
                if (notFound) {
                    notFound.classList.remove('d-none');
                    notFound.innerText = data.message || "No se encontró ninguna receta vigente para esta cédula.";
                }
            }
        })
        .catch(err => {
            Swal.fire({text: "Error al consultar receta en el servidor.", icon: 'info', background: 'var(--bg-panel)', color: 'var(--text-color)'});
        });
};

window.completarVentaReceta = function() {
    var idCita = window.currentRecetaIdCita || '';
    var cedula = window.currentRecetaCedula || (document.getElementById('cedulaFarmaciaBuscador') ? document.getElementById('cedulaFarmaciaBuscador').value.trim() : '');

    var formData = new URLSearchParams();
    formData.append("action", "completarVentaReceta");
    formData.append("idCita", idCita);
    formData.append("cedula", cedula);

    fetch("adminAction", {
        method: "POST",
        headers: { "Content-Type": "application/x-www-form-urlencoded" },
        body: formData.toString()
    }).then(function(res) {
        Swal.fire({text: "¡Venta completada exitosamente! La receta ha sido despachada y la factura se encuentra registrada en el Reporte de Ventas.", icon: 'info', background: 'var(--bg-panel)', color: 'var(--text-color)'});
        window.location.href = "dashboard?vista=facturas";
    }).catch(function(err) {
        Swal.fire({text: "Error al finalizar la venta de la receta.", icon: 'info', background: 'var(--bg-panel)', color: 'var(--text-color)'});
    });
};

// Función global corregida para RECETA
window.abrirModalReceta = function(nombrePaciente, cedula) {
    var cedInput = document.getElementById("recetaCedula");
    var infoDiv = document.getElementById("recetaPacNombreInfo");
    var quickReg = document.getElementById("recetaQuickRegister");
    var hiddenName = document.getElementById("recetaPacNombre");
    
    if (quickReg) quickReg.classList.add("d-none");
    
    if (cedula && cedula.trim().length === 10) {
        if (cedInput) {
            cedInput.value = cedula.trim();
            cedInput.readOnly = true;
        }
        if (hiddenName && nombrePaciente) hiddenName.value = nombrePaciente;
        if (infoDiv && nombrePaciente) infoDiv.innerHTML = '<i class="bi bi-check-circle-fill text-success me-1"></i> Paciente: ' + nombrePaciente;
    } else {
        if (cedInput) {
            cedInput.value = "";
            cedInput.readOnly = false;
        }
        if (hiddenName) hiddenName.value = nombrePaciente || "";
        if (infoDiv) infoDiv.innerHTML = nombrePaciente ? ('<i class="bi bi-person me-1"></i> Paciente: ' + nombrePaciente) : "";
    }
    
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



// BUSQUEDA DE PACIENTE POR CEDULA EN RECETA
window.buscarPacienteReceta = function(cedula) {
    const infoDiv = document.getElementById('recetaPacNombreInfo');
    const quickReg = document.getElementById('recetaQuickRegister');
    const esNuevo = document.getElementById('recetaEsNuevoPac');
    const btn = document.getElementById('btnPrescribirReceta');
    const hiddenName = document.getElementById('recetaPacNombre');
    
    if (cedula.length === 10) {
        if (infoDiv) infoDiv.innerHTML = '<i class="spinner-border spinner-border-sm me-2"></i>Buscando...';
        if (btn) btn.disabled = true;
        fetch('registroPaciente?action=buscarCedula&cedula=' + cedula)
            .then(r => r.json())
            .then(data => {
                if (data.id) {
                    var full = data.nombres + ' ' + data.apellidos;
                    if (infoDiv) infoDiv.innerHTML = '<i class="bi bi-check-circle-fill text-success me-1"></i> Paciente: ' + full;
                    if (hiddenName) hiddenName.value = full;
                    if (quickReg) quickReg.classList.add('d-none');
                    if (esNuevo) esNuevo.value = "false";
                    var hiddenId = document.getElementById('recetaPacienteIdHidden');
                    if (hiddenId) hiddenId.value = data.id;
                    if (btn) btn.disabled = false;
                    
                    var nN = document.getElementById('recetaNuevoNombres'); if (nN) nN.required = false;
                    var nA = document.getElementById('recetaNuevoApellidos'); if (nA) nA.required = false;
                } else {
                    if (infoDiv) infoDiv.innerHTML = '';
                    if (hiddenName) hiddenName.value = '';
                    if (quickReg) quickReg.classList.remove('d-none');
                    if (esNuevo) esNuevo.value = "true";
                    var hiddenId = document.getElementById('recetaPacienteIdHidden');
                    if (hiddenId) hiddenId.value = '';
                    if (btn) btn.disabled = false;
                    
                    var nN = document.getElementById('recetaNuevoNombres'); if (nN) nN.required = true;
                    var nA = document.getElementById('recetaNuevoApellidos'); if (nA) nA.required = true;
                }
            })
            .catch(err => {
                if (infoDiv) infoDiv.innerHTML = '<span class="text-danger">Error al buscar cédula</span>';
                if (btn) btn.disabled = false;
            });
    } else {
        if (infoDiv) infoDiv.innerHTML = '';
        if (hiddenName) hiddenName.value = '';
        if (quickReg) quickReg.classList.add('d-none');
        if (esNuevo) esNuevo.value = "false";
        if (btn) btn.disabled = false;
    }
};

window.abrirModalVenta = function(id, nombre, precio, stock) {
    var modalEl = document.getElementById("modalFacturarVenta");
    if (modalEl) {
        var idHidden = document.getElementById("ventaIdMed");
        if (!idHidden) {
            idHidden = document.createElement("input");
            idHidden.type = "hidden";
            idHidden.id = "ventaIdMed";
            idHidden.name = "idMed";
            var mBody = modalEl.querySelector(".modal-body");
            if (mBody) mBody.appendChild(idHidden);
        }
        idHidden.value = id || "";

        var nombreInput = document.getElementById("ventaNombreMed");
        if (nombreInput) nombreInput.value = nombre || "Medicamento";

        var stockSpan = document.getElementById("ventaMaxStock");
        if (stockSpan) stockSpan.innerText = stock || 100;

        var cantInput = document.getElementById("ventaCantidad");
        if (cantInput) {
            cantInput.value = 1;
            cantInput.max = stock || 100;
        }

        window.currentPrecioVenta = parseFloat(precio) || 0.0;
        window.calcTotalVenta();

        try {
            var modal = bootstrap.Modal.getInstance(modalEl) || new bootstrap.Modal(modalEl);
            modal.show();
        } catch (e) {
            $("#modalFacturarVenta").modal('show');
        }
    } else {
        Swal.fire({text: "Atención: El HTML del modalFacturarVenta no está en esta página.", icon: 'info', background: 'var(--bg-panel)', color: 'var(--text-color)'});
    }
};

window.calcTotalVenta = function() {
    var cantInput = document.getElementById("ventaCantidad");
    var totalInput = document.getElementById("ventaTotal");
    var cant = cantInput ? (parseInt(cantInput.value) || 1) : 1;
    var precio = window.currentPrecioVenta || 0.0;
    if (totalInput) totalInput.value = "$" + (cant * precio).toFixed(2);
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

// Confirmación de Venta con Generación de Factura en BD
window.confirmarVenta = function() {
    var idHidden = document.getElementById("ventaIdMed");
    var idMed = idHidden ? idHidden.value : "";
    var cliente = document.getElementById("ventaCliente") ? document.getElementById("ventaCliente").value.trim() : "Consumidor Final";
    var cantidad = document.getElementById("ventaCantidad") ? document.getElementById("ventaCantidad").value : "1";

    if (!idMed) {
        Swal.fire({text: "Por favor seleccione un medicamento válido.", icon: 'info', background: 'var(--bg-panel)', color: 'var(--text-color)'});
        return;
    }

    var formData = new URLSearchParams();
    formData.append("action", "facturarVenta");
    formData.append("idMed", idMed);
    formData.append("cantidad", cantidad);
    formData.append("cliente", cliente || "Consumidor Final");

    fetch("adminAction", {
        method: "POST",
        headers: { "Content-Type": "application/x-www-form-urlencoded" },
        body: formData.toString()
    }).then(function(res) {
        Swal.fire({text: "¡Venta procesada exitosamente! Se generó la factura en el Reporte de Ventas.", icon: 'info', background: 'var(--bg-panel)', color: 'var(--text-color)'});
        window.cerrarModalVenta();
        window.location.href = "dashboard?vista=facturas";
    }).catch(function(err) {
        Swal.fire({text: "Error al procesar la factura de venta.", icon: 'info', background: 'var(--bg-panel)', color: 'var(--text-color)'});
    });
};

window.irAReporteVentas = function() {
    window.location.href = "dashboard?vista=facturas";
};

// CONEXIÓN A LA BASE DE DATOS Y MODAL PARA INTERNAR
window.abrirModalInternar = function(id, numero, sala) {
    var idInput = document.getElementById('internarIdCama');
    if (idInput) idInput.value = id;
    
    var numLabel = document.getElementById('internarCamaNumLabel');
    if (numLabel) numLabel.innerText = (numero || id) + (sala ? " (" + sala + ")" : "");
    
    var cedulaInput = document.getElementById('camaCedula');
    if (cedulaInput) cedulaInput.value = '';
    
    var infoDiv = document.getElementById('camaPacNombreInfo');
    if (infoDiv) infoDiv.innerHTML = '';
    
    var quickReg = document.getElementById('camaQuickRegister');
    if (quickReg) quickReg.classList.add('d-none');
    
    var esNuevo = document.getElementById('camaEsNuevoPac');
    if (esNuevo) esNuevo.value = "false";
    
    var hiddenId = document.getElementById('camaPacienteIdHidden');
    if (hiddenId) hiddenId.value = '';

    var modalEl = document.getElementById("modalInternarCama");
    if (modalEl) {
        try {
            var modal = bootstrap.Modal.getInstance(modalEl) || new bootstrap.Modal(modalEl);
            modal.show();
        } catch (e) {
            $("#modalInternarCama").modal('show');
        }
    }
};

window.buscarPacienteCita = function(cedula) {
    const infoDiv = document.getElementById('citaPacNombre');
    const quickReg = document.getElementById('citaQuickRegister');
    const esNuevo = document.getElementById('citaEsNuevoPac');
    const btn = document.getElementById('btnAgendarCita');
    
    if (cedula.length === 10) {
        if (infoDiv) infoDiv.innerHTML = '<i class="spinner-border spinner-border-sm me-2"></i>Buscando...';
        if (btn) btn.disabled = true;
        fetch('registroPaciente?action=buscarCedula&cedula=' + cedula)
            .then(r => r.json())
            .then(data => {
                if (data.id) {
                    if (infoDiv) infoDiv.innerHTML = '<i class="bi bi-check-circle-fill text-success me-1"></i> Paciente: ' + data.nombres + ' ' + data.apellidos;
                    if (quickReg) quickReg.classList.add('d-none');
                    if (esNuevo) esNuevo.value = "false";
                    var hiddenId = document.getElementById('citaPacienteIdHidden');
                    if (hiddenId) hiddenId.value = data.id;
                    if (btn) btn.disabled = false;
                    
                    var nN = document.getElementById('citaNombres'); if (nN) nN.required = false;
                    var nA = document.getElementById('citaApellidos'); if (nA) nA.required = false;
                } else {
                    if (infoDiv) infoDiv.innerHTML = '';
                    if (quickReg) quickReg.classList.remove('d-none');
                    if (esNuevo) esNuevo.value = "true";
                    var hiddenId = document.getElementById('citaPacienteIdHidden');
                    if (hiddenId) hiddenId.value = "";
                    if (btn) btn.disabled = false;
                    
                    var nN = document.getElementById('citaNombres'); if (nN) nN.required = true;
                    var nA = document.getElementById('citaApellidos'); if (nA) nA.required = true;
                }
            }).catch(e => {
                if (infoDiv) infoDiv.innerHTML = '<i class="bi bi-exclamation-triangle-fill text-danger me-1"></i> Error de conexión.';
            });
    } else {
        if (infoDiv) infoDiv.innerHTML = '';
        if (quickReg) quickReg.classList.add('d-none');
        if (esNuevo) esNuevo.value = "false";
        if (btn) btn.disabled = false;
    }
};

window.buscarPacienteCama = function(cedula) {
    const infoDiv = document.getElementById('camaPacNombreInfo');
    const quickReg = document.getElementById('camaQuickRegister');
    const esNuevo = document.getElementById('camaEsNuevoPac');
    const btn = document.getElementById('btnInternarCama');
    
    if (cedula.length === 10) {
        if (infoDiv) infoDiv.innerHTML = '<i class="spinner-border spinner-border-sm me-2"></i>Buscando...';
        if (btn) btn.disabled = true;
        fetch('registroPaciente?action=buscarCedula&cedula=' + cedula)
            .then(r => r.json())
            .then(data => {
                if (data.id) {
                    if (infoDiv) infoDiv.innerHTML = '<i class="bi bi-check-circle-fill text-success me-1"></i> Paciente: ' + data.nombres + ' ' + data.apellidos;
                    if (quickReg) quickReg.classList.add('d-none');
                    if (esNuevo) esNuevo.value = "false";
                    var hiddenId = document.getElementById('camaPacienteIdHidden');
                    if (hiddenId) hiddenId.value = data.id;
                    if (btn) btn.disabled = false;
                    
                    var nN = document.getElementById('camaNuevoNombres'); if (nN) nN.required = false;
                    var nA = document.getElementById('camaNuevoApellidos'); if (nA) nA.required = false;
                } else {
                    if (infoDiv) infoDiv.innerHTML = '';
                    if (quickReg) quickReg.classList.remove('d-none');
                    if (esNuevo) esNuevo.value = "true";
                    var hiddenId = document.getElementById('camaPacienteIdHidden');
                    if (hiddenId) hiddenId.value = '';
                    if (btn) btn.disabled = false;
                    
                    var nN = document.getElementById('camaNuevoNombres'); if (nN) nN.required = true;
                    var nA = document.getElementById('camaNuevoApellidos'); if (nA) nA.required = true;
                }
            })
            .catch(err => {
                if (infoDiv) infoDiv.innerHTML = '<span class="text-danger">Error al buscar cédula</span>';
                if (btn) btn.disabled = false;
            });
    } else {
        if (infoDiv) infoDiv.innerHTML = '';
        if (quickReg) quickReg.classList.add('d-none');
        if (esNuevo) esNuevo.value = "false";
        if (btn) btn.disabled = false;
    }
};

// CONEXIÓN INVISIBLE A BD PARA DAR DE ALTA
window.confirmarAltaCama = function(id, numero, paciente) {
    Swal.fire({
        title: 'Dar de Alta',
        text: "¿Confirmas dar de alta a " + paciente + " y liberar la " + numero + "?",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Sí, Dar de Alta',
        cancelButtonText: 'Cancelar',
        background: 'var(--bg-panel)',
        color: 'var(--text-color)'
    }).then((result) => {
        if (result.isConfirmed) {
            var formData = new URLSearchParams();
            formData.append("action", "liberar");
            formData.append("camaId", id);
            fetch('camasAction', {
                method: 'POST',
                headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
                body: formData.toString()
            }).then(function(response) {
                Swal.fire({title: 'Alta confirmada', text: 'La ' + numero + ' ha sido liberada.', icon: 'success', background: 'var(--bg-panel)', color: 'var(--text-color)'}).then(() => {
                    window.location.href = "dashboard";
                });
            });
        }
    });
};

// CONEXIÓN PARA CAMBIAR ESTADO DE CAMA (Mantenimiento / Disponible)
window.cambiarEstadoCama = function(id, estado) {
    var est = estado || "Mantenimiento";
    var formData = new URLSearchParams();
    formData.append("action", "cambiarEstado");
    formData.append("camaId", id);
    formData.append("estado", est);

    fetch('camasAction', {
        method: 'POST',
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
        body: formData.toString()
    }).then(function(response) {
        Swal.fire({text: "El estado de la cama ha sido actualizado a " + est + ".", icon: 'info', background: 'var(--bg-panel)', color: 'var(--text-color)'});
        window.location.href = "dashboard";
    }).catch(function(err) {
        Swal.fire({text: "Error al actualizar el estado de la cama.", icon: 'info', background: 'var(--bg-panel)', color: 'var(--text-color)'});
    });
};

document.addEventListener("DOMContentLoaded", function() {
    document.querySelectorAll("*").forEach(function(el) {
        if (el.children.length === 0 && el.textContent.trim() === "null") {
            el.textContent = "Sin registrar";
        }
    });

    try {
        var urlParams = new URLSearchParams(window.location.search);
        var vista = urlParams.get('vista');
        if (vista) {
            cambiarVista(vista);
        } else {
            var ultimaVista = sessionStorage.getItem('ultima_vista_nurselogic');
            if (ultimaVista) {
                cambiarVista(ultimaVista);
            }
        }
    } catch(e) {}
});

// ABRIR MODAL PARA CREAR NUEVA CAMA
window.crearNuevaCama = function() {
    var modalEl = document.getElementById("modalAnadirCama") || document.getElementById("modalAnadirCama");
    if (modalEl) {
        try {
            var modal = bootstrap.Modal.getInstance(modalEl) || new bootstrap.Modal(modalEl);
            modal.show();
        } catch (e) {
            $("#modalAñadirCama").modal('show');
        }
    }
};

// CONEXIÓN PARA ELIMINAR CAMA
window.confirmarBorradoCama = function(id, numero) {
    Swal.fire({
        title: '¿Eliminar Cama?',
        text: "¿Ests seguro de eliminar la " + (numero || "cama seleccionada") + "? Esta acción es irreversible.",
        icon: 'error',
        showCancelButton: true,
        confirmButtonColor: '#d33',
        cancelButtonColor: '#3085d6',
        confirmButtonText: 'Sí, Eliminar',
        cancelButtonText: 'Cancelar',
        background: 'var(--bg-panel)',
        color: 'var(--text-color)'
    }).then((result) => {
        if (result.isConfirmed) {
            var formData = new URLSearchParams();
            formData.append("action", "eliminar");
            formData.append("camaId", id);
            fetch('camasAction', {
                method: 'POST',
                headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
                body: formData.toString()
            }).then(function(response) {
                Swal.fire({title: 'Eliminada', text: 'La cama ha sido eliminada.', icon: 'success', background: 'var(--bg-panel)', color: 'var(--text-color)'}).then(() => {
                    window.location.href = "dashboard";
                });
            });
        }
    });
};

function aplicarPlantillaRol(tipo, el) {
    // 1. Resaltar la tarjeta seleccionada y desmarcar las demás
    document.querySelectorAll('.plantilla-card').forEach(card => {
        card.style.background = 'rgba(255, 255, 255, 0.05)';
        card.style.borderColor = 'rgba(255, 255, 255, 0.2)';
    });
    if (el) {
        el.style.background = 'rgba(255, 193, 7, 0.15)';
        el.style.borderColor = '#ffc107';
    }

    // 2. Desmarcar todos los checkboxes
    const checkboxes = document.querySelectorAll('.perm-checkbox');
    checkboxes.forEach(chk => chk.checked = false);

    // 3. Normalizar el parámetro (evita problemas con mayúsculas y tildes)
    const t = (tipo || '').toLowerCase().normalize("NFD").replace(/[\u0300-\u036f]/g, "");

    // 4. Activar los permisos según la tarjeta seleccionada
    if (t === 'moderador') {
        checkboxes.forEach(chk => { if (chk.value === 'Usuarios') chk.checked = true; });
    } else if (t === 'bodeguero') {
        checkboxes.forEach(chk => { if (chk.value === 'Inventario') chk.checked = true; });
    } else if (t === 'medico') {
        checkboxes.forEach(chk => { if (chk.value === 'Citas' || chk.value === 'Admision') chk.checked = true; });
    }
    // Si es 'custom' / 'amedida', los checkboxes ya quedaron desmarcados en el paso 2
}



        function abrirModalVerDiagnostico(paciente, btnEl) { document.getElementById('verDiagPaciente').innerText = paciente; document.getElementById('verDiagTexto').innerText = btnEl.getAttribute('data-diagnostico'); document.getElementById('verDiagReceta').innerText = btnEl.getAttribute('data-receta'); var mEl = document.getElementById('modalVerDiagnostico'); if(mEl) { var m = bootstrap.Modal.getInstance(mEl) || new bootstrap.Modal(mEl); m.show(); } }



        function filtrarCitasAvanzado() { let input = document.getElementById('buscadorCitas').value.toLowerCase(); let fechaFiltro = document.getElementById('filtroFechaCitas').value; let ocultarCerradas = document.getElementById('checkOcultarCerradas').checked; let table = document.getElementById('tablaCitas'); if(!table) return; let tr = table.getElementsByTagName('tr'); for (let i = 1; i < tr.length; i++) { let txtValue = tr[i].textContent || tr[i].innerText; txtValue = txtValue.toLowerCase(); let rowHtml = tr[i].innerHTML.toLowerCase(); let dateValue = ''; let tdFecha = tr[i].getElementsByTagName('small')[0]; if(tdFecha) { dateValue = tdFecha.innerText.trim(); } let matchTexto = txtValue.indexOf(input) > -1; let matchFecha = fechaFiltro === '' || dateValue === fechaFiltro; let estadoCelda = tr[i].getElementsByTagName('td')[3]; let estado = estadoCelda ? estadoCelda.innerText.trim().toLowerCase() : ''; let esCerrada = estado === 'atendido' || estado === 'cancelado'; let matchEstado = !(ocultarCerradas && esCerrada); if (matchTexto && matchFecha && matchEstado) { tr[i].style.display = ''; } else { tr[i].style.display = 'none'; } } } document.addEventListener('DOMContentLoaded', function() { setTimeout(function(){ if(document.getElementById('tablaCitas')) filtrarCitasAvanzado(); }, 100); });




        function filtrarTicketsTI() { let select = document.getElementById('filtroNivelTI').value.toLowerCase(); let cards = document.querySelectorAll('.ticket-card'); cards.forEach(card => { let nivel = card.getAttribute('data-nivel'); if (select === 'todos' || nivel.includes(select)) { card.style.display = ''; } else { card.style.display = 'none'; } }); }


        function filtrarFacturasAvanzado() { let input = document.getElementById('buscadorFacturas').value.toLowerCase(); let fechaFiltro = document.getElementById('filtroFechaFacturas').value; let table = document.getElementById('tablaFacturas'); if(!table) return; let tr = table.getElementsByTagName('tr'); for (let i = 1; i < tr.length; i++) { let txtValue = tr[i].textContent || tr[i].innerText; txtValue = txtValue.toLowerCase(); let dateValue = ''; let tdFecha = tr[i].getElementsByTagName('td')[1]; if(tdFecha) { let match = tdFecha.innerText.match(/(\d{4}-\d{2}-\d{2})/); if(match) dateValue = match[1]; } let matchTexto = txtValue.indexOf(input) > -1; let matchFecha = fechaFiltro === '' || dateValue === fechaFiltro; if (matchTexto && matchFecha) { tr[i].style.display = ''; } else { tr[i].style.display = 'none'; } } }

        function abrirModalVerFactura(id, cliente, fecha, total, btnEl) { document.getElementById('verFacId').innerText = id; document.getElementById('verFacCliente').innerText = cliente; document.getElementById('verFacFecha').innerText = fecha; document.getElementById('verFacTotal').innerText = total; document.getElementById('verFacDetalles').innerHTML = btnEl.getAttribute('data-detalles'); var mEl = document.getElementById('modalVerFactura'); if(mEl) { var m = bootstrap.Modal.getInstance(mEl) || new bootstrap.Modal(mEl); m.show(); } }
function abrirModalVerDiagnosticoCama(paciente, btnEl) { document.getElementById('verDiagPaciente').innerText = paciente; document.getElementById('verDiagTexto').innerText = btnEl.getAttribute('data-diagnostico'); var recetaEl = document.getElementById('verDiagReceta'); if(recetaEl) { recetaEl.innerText = 'No aplica (Hospitalizacion)'; } var mEl = document.getElementById('modalVerDiagnostico'); if(mEl) { var m = bootstrap.Modal.getInstance(mEl) || new bootstrap.Modal(mEl); m.show(); } }











<script>
// Lgica de Tema Claro / Oscuro
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

    // Update icons if topbar has them
    let iconNav = document.getElementById('themeIconDash');
    let labelNav = document.getElementById('themeLabelDash');
    let iconClass = 'bi-moon-stars-fill';
    let labelText = 'Oscuro';
    if (theme === 'light') { iconClass = 'bi-sun-fill text-warning'; labelText = 'Claro'; }
    else if (theme === 'auto') { iconClass = 'bi-display text-info'; labelText = 'Auto'; }

    if (iconNav) iconNav.className = 'bi ' + iconClass;
    if (labelNav) labelNav.innerText = labelText;
}


// ==========================================
// MOTOR DEL CARRITO DE VENTAS (FARMACIA)
// ==========================================
let carritoVentas = [];
window.vaciarCarrito = function() {
    carritoVentas = [];
    document.getElementById('cartBubbleContainer').classList.add('d-none');
    var mEl = document.getElementById('modalCarrito');
    if (mEl) { var m = bootstrap.Modal.getInstance(mEl); if(m) m.hide(); }
};


window.agregarAlCarrito = function(id, nombre, precio, maxStock) {
    let item = carritoVentas.find(i => i.id === id);
    if (item) {
        if (item.cantidad < maxStock) {
            item.cantidad++;
            Swal.fire({title: 'Actualizado', text: '+1 ' + nombre + ' al carrito.', icon: 'success', timer: 1000, showConfirmButton: false, background: 'var(--bg-panel)', color: 'var(--text-color)'});
        } else {
            Swal.fire({title: 'Stock Insuficiente', text: 'No hay más unidades disponibles en bodega.', icon: 'warning', background: 'var(--bg-panel)', color: 'var(--text-color)'});
        }
    } else {
        carritoVentas.push({ id: id, nombre: nombre, precio: parseFloat(precio), cantidad: 1, maxStock: parseInt(maxStock) });
        Swal.fire({title: 'Agregado', text: nombre + ' añadido al carrito.', icon: 'success', timer: 1000, showConfirmButton: false, background: 'var(--bg-panel)', color: 'var(--text-color)'});
    }
    actualizarBurbujaCarrito();
};

window.actualizarBurbujaCarrito = function() {
    let btn = document.getElementById('cartBubbleContainer');
    let badge = document.getElementById('cartBubbleBadge');
    if (!btn || !badge) return;
    
    let totalItems = carritoVentas.reduce((acc, item) => acc + item.cantidad, 0);
    if (totalItems > 0) {
        btn.classList.remove('d-none');
        badge.innerText = totalItems;
    } else {
        btn.classList.add('d-none');
    }
};

window.abrirModalCarrito = function() {
    renderizarTablaCarrito();
    var mEl = document.getElementById('modalCarrito');
    if (mEl) { var m = bootstrap.Modal.getInstance(mEl) || new bootstrap.Modal(mEl); m.show(); }
};

window.cambiarCantidadCarrito = function(id, delta) {
    let item = carritoVentas.find(i => i.id === id);
    if (item) {
        let nuevaCant = item.cantidad + delta;
        if (nuevaCant <= 0) {
            carritoVentas = carritoVentas.filter(i => i.id !== id);
        } else if (nuevaCant > item.maxStock) {
            Swal.fire({title: 'Límite', text: 'Alcanzó el máximo en bodega.', icon: 'warning', toast: true, position: 'top-end', timer: 2000, showConfirmButton: false});
        } else {
            item.cantidad = nuevaCant;
        }
        actualizarBurbujaCarrito();
        renderizarTablaCarrito();
    }
};

window.renderizarTablaCarrito = function() {
    let tbody = document.getElementById('tablaCarritoCuerpo');
    let totalSpan = document.getElementById('carritoTotalLabel');
    if (!tbody || !totalSpan) return;
    
    tbody.innerHTML = '';
    let total = 0;
    
    if (carritoVentas.length === 0) {
        tbody.innerHTML = '<tr><td colspan="5" class="text-center text-secondary py-4">El carrito está vacío</td></tr>';
        totalSpan.innerText = '0.00';
        return;
    }
    
    carritoVentas.forEach(item => {
        let subt = item.precio * item.cantidad;
        total += subt;
        
        let tr = document.createElement('tr');
        tr.innerHTML = 
            '<td class="align-middle fw-semibold">' + item.nombre + '</td>' +
            '<td class="align-middle text-info">$' + item.precio.toFixed(2) + '</td>' +
            '<td class="align-middle">' +
                '<div class="input-group input-group-sm" style="width: 100px;">' +
                    '<button class="btn btn-outline-secondary" type="button" onclick="cambiarCantidadCarrito(' + item.id + ', -1)">-</button>' +
                    '<input type="text" class="form-control text-center bg-transparent text-white border-secondary" value="' + item.cantidad + '" readonly>' +
                    '<button class="btn btn-outline-secondary" type="button" onclick="cambiarCantidadCarrito(' + item.id + ', 1)">+</button>' +
                '</div>' +
            '</td>' +
            '<td class="align-middle text-success fw-bold">$' + subt.toFixed(2) + '</td>' +
            '<td class="align-middle text-end">' +
                '<button class="btn btn-sm btn-outline-danger" onclick="cambiarCantidadCarrito(' + item.id + ', -9999)"><i class="bi bi-trash"></i></button>' +
            '</td>';
        tbody.appendChild(tr);
    });
    
    totalSpan.innerText = total.toFixed(2);
};

window.procesarCheckout = function() {
    if (carritoVentas.length === 0) return;
    
    Swal.fire({
        title: '¿Facturar Venta?',
        text: 'Se procesarán ' + carritoVentas.length + ' medicamentos.',
        icon: 'question',
        showCancelButton: true,
        confirmButtonColor: '#10b981',
        confirmButtonText: 'Sí, Facturar',
        cancelButtonText: 'Cancelar',
        background: 'var(--bg-panel)',
        color: 'var(--text-color)'
    }).then((result) => {
        if (result.isConfirmed) {
            Swal.fire({title: 'Procesando...', text: 'Registrando ventas...', allowOutsideClick: false, background: 'var(--bg-panel)', color: 'var(--text-color)', didOpen: () => { Swal.showLoading(); }});
            
                        let payload = carritoVentas.map(item => item.id + ":" + item.cantidad).join(",");
            let clienteNombre = document.getElementById("ventaClienteCarrito") ? document.getElementById("ventaClienteCarrito").value.trim() : "Consumidor Final";
            let clienteCedula = document.getElementById("ventaCedulaCarrito") ? document.getElementById("ventaCedulaCarrito").value.trim() : "";
            
            var formData = new URLSearchParams();
            formData.append("action", "facturarCarrito");
            formData.append("payload", payload);
            formData.append("cliente", clienteNombre);
            formData.append("cedula", clienteCedula);
            
            fetch("adminAction", {
                method: "POST",
                headers: { "Content-Type": "application/x-www-form-urlencoded" },
                body: formData.toString()
            }).then(() => {
                Swal.fire({title: 'Venta procesada exitosamente!', text: 'Se generó la factura correspondiente.', icon: 'success', background: 'var(--bg-panel)', color: 'var(--text-color)'}).then(() => {
                    carritoVentas = [];
                    window.location.href = "dashboard";
                });
            }).catch(e => {
                Swal.fire('Error', 'Hubo un problema al procesar la venta.', 'error');
            });
        }
    });
};


window.verFichaClinica = function(cedula) {
    if (!cedula) return;
    Swal.fire({title: 'Cargando Ficha...', text: 'Obteniendo información del paciente...', allowOutsideClick: false, didOpen: () => { Swal.showLoading(); }});
    fetch('registroPaciente?action=buscarCedula&cedula=' + cedula)
        .then(r => r.json())
        .then(data => {
            Swal.close();
            if (data.id) {
                document.getElementById('fichaNombre').innerText = data.nombres + ' ' + data.apellidos;
                document.getElementById('fichaInfo').innerText = 'Cédula: ' + cedula + ' | Nacimiento: ' + (data.fechaNacimiento || '--') + ' | Sexo: ' + (data.sexo || '--');
                document.getElementById('fichaFechaActualizacion').innerHTML = '<i class="bi bi-calendar3 me-1"></i> Fecha: ' + new Date().toLocaleDateString();
                document.getElementById('fichaEstPeso').innerText = (data.estatura && data.estatura !== '0.0' ? data.estatura : '--') + ' cm / ' + (data.peso && data.peso !== '0.0' ? data.peso : '--') + ' kg';
                document.getElementById('fichaTemp').innerText = (data.temperatura && data.temperatura !== '0.0' ? data.temperatura : '--') + ' °C';
                document.getElementById('fichaPresion').innerText = (data.presion || '--');
                document.getElementById('fichaFcSat').innerText = (data.fc && data.fc !== 0 ? data.fc : '--') + ' lpm / ' + (data.sat && data.sat !== 0 ? data.sat : '--') + ' %';
                document.getElementById('fichaEnfermedades').innerText = data.enfermedad && data.enfermedad !== 'null' && data.enfermedad !== 'Ninguna' ? data.enfermedad : 'Ninguna registrada';
                document.getElementById('fichaAlergias').innerText = data.alergias && data.alergias !== 'null' && data.alergias !== 'Ninguna' ? data.alergias : 'Ninguna registrada';
                
                let container = document.getElementById('fichaAlertasContenedor');
                container.innerHTML = '';
                if (data.alergias && data.alergias.trim() !== '') {
                    container.innerHTML += '<div class="alert alert-danger py-2 mb-2 border-0" style="background: rgba(220,38,38,0.1);"><i class="bi bi-exclamation-octagon-fill me-2"></i>Paciente reporta alergias. Riesgo de shock anafiláctico.</div>';
                }
                if (data.presion) {
                    let parts = data.presion.split('/');
                    if (parts.length === 2 && parseInt(parts[0]) >= 140) {
                        container.innerHTML += '<div class="alert alert-warning py-2 mb-2 border-0" style="background: rgba(245,158,11,0.1);"><i class="bi bi-heart-pulse-fill me-2"></i>Hipertensión detectada. Monitorear signos vitales.</div>';
                    }
                }
                if (container.innerHTML === '') {
                    container.innerHTML = '<div class="alert alert-success py-2 mb-0 border-0" style="background: rgba(16,185,129,0.1);"><i class="bi bi-check-circle-fill me-2"></i>Parámetros estables. Ninguna alerta clínica urgente.</div>';
                }
                
                var mEl = document.getElementById('modalFichaClinica');
                if (mEl) { var m = bootstrap.Modal.getInstance(mEl) || new bootstrap.Modal(mEl); m.show(); }
            } else {
                Swal.fire('Error', 'Paciente no encontrado.', 'error');
            }
        })
        .catch(e => {
            Swal.fire('Error', 'Problema de conexión al cargar la ficha.', 'error');
        });
};


window.editarPacienteDesdeFicha = function() {
    let cedulaText = document.getElementById('fichaInfo').innerText;
    let match = cedulaText.match(/Cédula: (\d+)/);
    if (match && match[1]) {
        cerrarModalFicha();
        editarPaciente(match[1]);
    } else {
        Swal.fire('Error', 'No se pudo obtener la cédula del paciente.', 'error');
    }
};

window.cerrarModalFicha = function() {
    var mEl = document.getElementById('modalFichaClinica');
    if (mEl) { var m = bootstrap.Modal.getInstance(mEl); if(m) m.hide(); }
};

// Inicializar estado del dropdown si es que existe
document.addEventListener('DOMContentLoaded', function() {
    var savedTheme = localStorage.getItem('nurselogic_theme') || 'dark';
    applyTheme(savedTheme);
});


window.borrarMedicamento = function(id) {
    Swal.fire({
        title: 'Eliminar F\u00E1rmaco?',
        text: "Esta acci\u00F3n es irreversible.",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#d33',
        cancelButtonColor: '#3085d6',
        confirmButtonText: 'S\u00ED, Eliminar',
        cancelButtonText: 'Cancelar',
        background: 'var(--bg-panel)',
        color: 'var(--text-color)'
    }).then((result) => {
        if (result.isConfirmed) {
            var formData = new URLSearchParams();
            formData.append("action", "eliminarMedicamento");
            formData.append("id", id);
            fetch('adminAction', {
                method: 'POST',
                headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
                body: formData.toString()
            }).then(function(response) {
                Swal.fire({title: 'Eliminado', text: 'El f\u00E1rmaco ha sido eliminado.', icon: 'success', background: 'var(--bg-panel)', color: 'var(--text-color)'}).then(() => {
                    window.location.href = "dashboard?vista=medicamentos";
                });
            });
        }
    });
};

window.confirmarBorradoFactura = function(id) {
    Swal.fire({
        title: '¿Eliminar Factura?',
        text: "Esta acción es irreversible.",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#d33',
        cancelButtonColor: '#3085d6',
        confirmButtonText: 'Sí, Eliminar',
        cancelButtonText: 'Cancelar',
        background: 'var(--bg-panel)',
        color: 'var(--text-color)'
    }).then((result) => {
        if (result.isConfirmed) {
            var formData = new URLSearchParams();
            formData.append("action", "eliminarFactura");
            formData.append("idEnf", id);
                    formData.append("idAle", id);
            fetch('adminAction', {
                method: 'POST',
                headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
                body: formData.toString()
            }).then(function(response) {
                Swal.fire({title: 'Eliminada', text: 'La factura ha sido eliminada.', icon: 'success', background: 'var(--bg-panel)', color: 'var(--text-color)'}).then(() => {
                    window.location.href = "dashboard";
                });
            });
        }
    });
};


window.cerrarModalCatalogos = function() {
    var mEl = document.getElementById('modalCatalogos');
    if(mEl) { 
        var m = bootstrap.Modal.getInstance(mEl); 
        if(m) m.hide(); 
    }
};



window.buscarClienteCarrito = function(cedula) {
    if (cedula.length === 10) {
        fetch("adminAction?action=buscarClienteCedula&cedula=" + cedula)
            .then(r => r.json())
            .then(data => {
                let input = document.getElementById("ventaClienteCarrito");
                if (data.nombre) {
                    input.value = data.nombre;
                    input.classList.add("fw-bold", "text-info");
                }
            }).catch(e => console.log(e));
    }
};

window.exportarFacturasFechas = function() {
    Swal.fire({
        title: 'Exportar Reporte de Ventas',
        html: '<div class="text-start">' +
              '<label class="form-label small text-secondary">Desde:</label>' +
              '<input type="date" id="expDesde" class="form-control mb-3 bg-transparent text-white border-secondary">' +
              '<label class="form-label small text-secondary">Hasta:</label>' +
              '<input type="date" id="expHasta" class="form-control bg-transparent text-white border-secondary">' +
              '</div>',
        background: 'var(--bg-panel)', color: 'var(--text-color)',
        showCancelButton: true, confirmButtonText: 'Exportar', cancelButtonText: 'Cancelar'
    }).then(res => {
        if (res.isConfirmed) {
            let d = document.getElementById('expDesde').value;
            let h = document.getElementById('expHasta').value;
            window.location.href = "exportCsv?tipo=facturas&desde=" + d + "&hasta=" + h;
        }
    });
};

window.imprimirFactura = function() {
    var id = document.getElementById('verFacId').innerText;
    var cliente = document.getElementById('verFacCliente').innerText;
    var fecha = document.getElementById('verFacFecha').innerText;
    var detalles = document.getElementById('verFacDetalles').innerHTML;
    var total = document.getElementById('verFacTotal').innerText;
    
    var w = window.open('', '', 'width=800,height=600');
    w.document.write('<html><head><title>Factura ' + id + '</title>');
    w.document.write('<style>body{font-family:sans-serif;padding:20px;} .factura-box{border:1px solid #ccc;padding:20px;} .header{text-align:center;} .tot{text-align:right;font-size:1.2em;font-weight:bold;}</style>');
    w.document.write('</head><body><div class="factura-box"><div class="header"><h2>Farmacia NurseLogic</h2><h3>Factura ' + id + '</h3></div>');
    w.document.write('<p><strong>Cliente:</strong> ' + cliente + '</p>');
    w.document.write('<p><strong>Fecha:</strong> ' + fecha + '</p><hr>');
    w.document.write('<div>' + detalles + '</div><hr>');
    w.document.write('<p class="tot">TOTAL: $' + total + '</p>');
    w.document.write('</div><script>window.print();<\/script></body></html>');
    w.document.close();
};

