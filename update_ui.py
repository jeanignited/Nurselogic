import io
import re

with io.open('src/main/webapp/login.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

# REWRITE REGISTER PASS REQS
old_reg_pass_reqs = """<div id="regPassReqs" class="small text-secondary" style="font-size: 0.75rem; text-align: left;">
                            <div id="reqLen" class="text-danger"><i class="bi bi-x-circle me-1"></i>M\u00ednimo 8 caracteres</div>
                            <div id="reqAlphaNum" class="text-danger"><i class="bi bi-x-circle me-1"></i>Letras y n\u00fameros</div>
                            <div id="reqSpec" class="text-danger"><i class="bi bi-x-circle me-1"></i>1 car\u00e1cter especial (ej. @$!%*?&)</div>
                            <div id="reqMatch" class="text-danger"><i class="bi bi-x-circle me-1"></i>Las contrase\u00f1as coinciden</div>
                        </div>"""

new_reg_pass_reqs = """<div id="regPassReqs" class="row g-1 mt-1 p-2 rounded-3 text-start text-secondary" style="font-size: 0.72rem; background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.05);">
                            <div class="col-6" id="reqLen" class="text-danger"><i class="bi bi-x-circle me-1"></i>M\u00edn 8 chars</div>
                            <div class="col-6" id="reqAlphaNum" class="text-danger"><i class="bi bi-x-circle me-1"></i>Letras y Nros</div>
                            <div class="col-6" id="reqSpec" class="text-danger"><i class="bi bi-x-circle me-1"></i>1 Especial (@#$)</div>
                            <div class="col-6" id="reqMatch" class="text-danger"><i class="bi bi-x-circle me-1"></i>Coinciden</div>
                        </div>"""

c = c.replace(old_reg_pass_reqs, new_reg_pass_reqs)

# REWRITE RESET PASS REQS
old_reset_pass_reqs = """<div id="resetPassReqs" class="small text-secondary mt-2" style="font-size: 0.75rem;">
                          <div id="reqLenR" class="text-danger"><i class="bi bi-x-circle me-1"></i>M\u00ednimo 8 caracteres</div>
                          <div id="reqAlphaNumR" class="text-danger"><i class="bi bi-x-circle me-1"></i>Letras y n\u00fameros</div>
                          <div id="reqSpecR" class="text-danger"><i class="bi bi-x-circle me-1"></i>1 car\u00e1cter especial (ej. @$!%*?&)</div>
                          <div id="reqMatchR" class="text-danger"><i class="bi bi-x-circle me-1"></i>Las contrase\u00f1as coinciden</div>
                      </div>"""

new_reset_pass_reqs = """<div id="resetPassReqs" class="row g-1 mt-2 p-2 rounded-3 text-start text-secondary" style="font-size: 0.72rem; background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.05);">
                          <div class="col-6" id="reqLenR" class="text-danger"><i class="bi bi-x-circle me-1"></i>M\u00edn 8 chars</div>
                          <div class="col-6" id="reqAlphaNumR" class="text-danger"><i class="bi bi-x-circle me-1"></i>Letras y Nros</div>
                          <div class="col-6" id="reqSpecR" class="text-danger"><i class="bi bi-x-circle me-1"></i>1 Especial (@#$)</div>
                          <div class="col-6" id="reqMatchR" class="text-danger"><i class="bi bi-x-circle me-1"></i>Coinciden</div>
                      </div>"""

c = c.replace(old_reset_pass_reqs, new_reset_pass_reqs)

# FIX CEDULA MSG JS
old_js_cedula = """function checkCedulaAPI(cedula) {
        let msg = document.getElementById('cedulaMsg');
        let btn = document.getElementById('btnRegistrar');
        msg.className = 'small mt-1 text-info';
        msg.innerHTML = '<i class="bi bi-hourglass-split me-1"></i>Verificando...';
        msg.classList.remove('d-none');
        btn.disabled = true;
        
        fetch('checkCedulaApi.jsp?cedula=' + cedula)
            .then(r => r.json())
            .then(data => {
                if(data.userExists) {
                    msg.className = 'small mt-1 text-danger fw-bold';
                    msg.innerHTML = '<i class="bi bi-exclamation-triangle-fill me-1"></i>Esta c\u00e9dula ya tiene una cuenta.';
                    btn.disabled = true;
                } else if(data.patientExists) {
                    msg.className = 'small mt-1 text-success';
                    msg.innerHTML = '<i class="bi bi-check-circle-fill me-1"></i>C\u00e9dula encontrada. Autocompletando...';
                    document.getElementById('regNombres').value = data.nombres;
                    document.getElementById('regApellidos').value = data.apellidos;
                    document.getElementById('regClave').dispatchEvent(new Event('input'));
                } else {
                    msg.className = 'small mt-1 text-success';
                    msg.innerHTML = '<i class="bi bi-check-circle-fill me-1"></i>C\u00e9dula disponible.';
                    document.getElementById('regClave').dispatchEvent(new Event('input'));
                }
            }).catch(e => {
                msg.className = 'd-none';
            });
    }"""

new_js_cedula = """function checkCedulaAPI(cedula) {
        let msg = document.getElementById('cedulaMsg');
        let btn = document.getElementById('btnRegistrar');
        msg.className = 'd-inline-block mt-2 px-2 py-1 rounded-2 fw-semibold text-info';
        msg.style.background = 'rgba(14, 165, 233, 0.1)';
        msg.style.border = '1px solid rgba(14, 165, 233, 0.2)';
        msg.style.fontSize = '0.75rem';
        msg.innerHTML = '<i class="bi bi-hourglass-split me-1"></i>Verificando...';
        msg.classList.remove('d-none');
        btn.disabled = true;
        
        fetch('checkCedulaApi.jsp?cedula=' + cedula)
            .then(r => r.json())
            .then(data => {
                if(data.userExists) {
                    msg.className = 'd-inline-block mt-2 px-2 py-1 rounded-2 fw-bold text-danger';
                    msg.style.background = 'rgba(239, 68, 68, 0.1)';
                    msg.style.border = '1px solid rgba(239, 68, 68, 0.2)';
                    msg.innerHTML = '<i class="bi bi-exclamation-triangle-fill me-1"></i>C\u00e9dula en uso.';
                    btn.disabled = true;
                } else if(data.patientExists) {
                    msg.className = 'd-inline-block mt-2 px-2 py-1 rounded-2 fw-semibold text-success';
                    msg.style.background = 'rgba(16, 185, 129, 0.1)';
                    msg.style.border = '1px solid rgba(16, 185, 129, 0.2)';
                    msg.innerHTML = '<i class="bi bi-check-circle-fill me-1"></i>Autocompletado.';
                    document.getElementById('regNombres').value = data.nombres;
                    document.getElementById('regApellidos').value = data.apellidos;
                    document.getElementById('regClave').dispatchEvent(new Event('input'));
                } else {
                    msg.className = 'd-inline-block mt-2 px-2 py-1 rounded-2 fw-semibold text-success';
                    msg.style.background = 'rgba(16, 185, 129, 0.1)';
                    msg.style.border = '1px solid rgba(16, 185, 129, 0.2)';
                    msg.innerHTML = '<i class="bi bi-check-circle-fill me-1"></i>C\u00e9dula disponible.';
                    document.getElementById('regClave').dispatchEvent(new Event('input'));
                }
            }).catch(e => {
                msg.className = 'd-none';
            });
    }"""

c = c.replace(old_js_cedula, new_js_cedula)

# FIX SET REQ CLASS
old_setreq = """                if(valid) {
                    el.className = 'text-success';
                    el.innerHTML = '<i class="bi bi-check-circle-fill me-1"></i>' + el.innerText;
                } else {
                    el.className = 'text-danger';
                    el.innerHTML = '<i class="bi bi-x-circle me-1"></i>' + el.innerText;
                }"""
                
new_setreq = """                if(valid) {
                    el.className = 'col-6 text-success fw-semibold';
                    el.innerHTML = '<i class="bi bi-check-circle-fill me-1"></i>' + el.innerText;
                } else {
                    el.className = 'col-6 text-danger';
                    el.innerHTML = '<i class="bi bi-x-circle me-1"></i>' + el.innerText;
                }"""

c = c.replace(old_setreq, new_setreq)

with io.open('src/main/webapp/login.jsp', 'w', encoding='utf-8') as f:
    f.write(c)

print("UI improved successfully")
