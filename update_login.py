import io
import re

with io.open('src/main/webapp/login.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

# 1. UPDATE REGISTER PANEL
new_reg_fields = """<div class="col-6"><input type="text" id="regNombres" name="nombres" class="form-control" placeholder="Nombres" required autocomplete="off"></div>
                    <div class="col-6"><input type="text" id="regApellidos" name="apellidos" class="form-control" placeholder="Apellidos" required autocomplete="off"></div>
                    <div class="col-12"><input type="email" name="correo" class="form-control" placeholder="Correo Electr\u00f3nico" required autocomplete="nope"></div>
                    <div class="col-6">
                        <input type="text" id="regCedula" name="cedula" class="form-control" placeholder="C\u00e9dula (10 d\u00edgitos)" maxlength="10" oninput="this.value = this.value.replace(/[^0-9]/g, ''); if(this.value.length===10) checkCedulaAPI(this.value);" required autocomplete="off">
                        <div id="cedulaMsg" class="small mt-1 d-none"></div>
                    </div>
                    <div class="col-6"><input type="text" name="telefono" class="form-control" placeholder="Tel\u00e9fono (10 d\u00edgitos)" maxlength="10" oninput="this.value = this.value.replace(/[^0-9]/g, '');" required autocomplete="off"></div>
                    <div class="col-12"><input type="text" name="direccion" class="form-control" placeholder="Direcci\u00f3n" required autocomplete="off"></div>
                    <div class="col-6"><input type="password" id="regClave" name="clave" class="form-control" placeholder="Crear Contrase\u00f1a" required autocomplete="new-password"></div>
                    <div class="col-6"><input type="password" id="regConfirmar" class="form-control" placeholder="Confirmar" required autocomplete="new-password"></div>
                    <div class="col-12">
                        <div id="regPassReqs" class="small text-secondary" style="font-size: 0.75rem; text-align: left;">
                            <div id="reqLen" class="text-danger"><i class="bi bi-x-circle me-1"></i>M\u00ednimo 8 caracteres</div>
                            <div id="reqAlphaNum" class="text-danger"><i class="bi bi-x-circle me-1"></i>Letras y n\u00fameros</div>
                            <div id="reqSpec" class="text-danger"><i class="bi bi-x-circle me-1"></i>1 car\u00e1cter especial (ej. @$!%*?&)</div>
                            <div id="reqMatch" class="text-danger"><i class="bi bi-x-circle me-1"></i>Las contrase\u00f1as coinciden</div>
                        </div>
                    </div>
                    <div class="col-12">
                        <select name="tipoUsuario" class="form-select" required>
                            <option value="" disabled selected>Seleccione el tipo de cuenta...</option>
                            <option value="Paciente">Soy Paciente</option>
                            <option value="Medico">Soy Personal M\u00e9dico</option>
                        </select>
                    </div>
                </div>
                <button type="submit" id="btnRegistrar" class="btn btn-success" disabled><i class="bi bi-person-plus me-2"></i>REGISTRAR USUARIO</button>"""

c = re.sub(r'<div class="col-6"><input type="text" name="nombres"[\s\S]*?<button type="submit" class="btn btn-success"><i class="bi bi-person-plus me-2"></i>REGISTRAR USUARIO</button>', new_reg_fields, c)

# 2. UPDATE RESET PANEL
new_reset_fields = """<div class="mb-4 text-start">
                      <label class="form-label small text-secondary fw-semibold">Nueva Contrase\u00f1a</label>
                      <input type="password" id="resetClave" name="nuevaClave" class="form-control mb-2" placeholder="\u2022\u2022\u2022\u2022\u2022\u2022\u2022\u2022" required autocomplete="new-password">
                      <input type="password" id="resetConfirmar" class="form-control" placeholder="Confirmar Nueva Contrase\u00f1a" required autocomplete="new-password">
                      <div id="resetPassReqs" class="small text-secondary mt-2" style="font-size: 0.75rem;">
                          <div id="reqLenR" class="text-danger"><i class="bi bi-x-circle me-1"></i>M\u00ednimo 8 caracteres</div>
                          <div id="reqAlphaNumR" class="text-danger"><i class="bi bi-x-circle me-1"></i>Letras y n\u00fameros</div>
                          <div id="reqSpecR" class="text-danger"><i class="bi bi-x-circle me-1"></i>1 car\u00e1cter especial (ej. @$!%*?&)</div>
                          <div id="reqMatchR" class="text-danger"><i class="bi bi-x-circle me-1"></i>Las contrase\u00f1as coinciden</div>
                      </div>
                  </div>
                  <button type="submit" id="btnReset" class="btn btn-success" disabled><i class="bi bi-key me-2"></i>ACTUALIZAR CONTRASE\u00f1A</button>"""

c = re.sub(r'<div class="mb-4">\s*<label class="form-label small text-secondary fw-semibold">Nueva Contrase[^<]+</label>\s*<input type="password" name="nuevaClave" class="form-control" placeholder="[^\"]+" required autocomplete="new-password">\s*</div>\s*<button type="submit" class="btn btn-success"><i class="bi bi-key me-2"></i>ACTUALIZAR CONTRASE[^<]+</button>', new_reset_fields, c)

# 3. ADD JAVASCRIPT
js_code = """
<script>
    // Validation Logic
    function setupPasswordValidation(claveId, confId, btnId, reqIds) {
        let clave = document.getElementById(claveId);
        let conf = document.getElementById(confId);
        let btn = document.getElementById(btnId);
        if(!clave || !conf || !btn) return;
        
        function validate() {
            let v = clave.value;
            let c = conf.value;
            
            let hasLen = v.length >= 8;
            let hasAlphaNum = /[a-zA-Z]/.test(v) && /[0-9]/.test(v);
            let hasSpec = /[^a-zA-Z0-9]/.test(v);
            let match = (v !== '') && (v === c);
            
            function setReq(id, valid) {
                let el = document.getElementById(id);
                if(valid) {
                    el.className = 'text-success';
                    el.innerHTML = '<i class="bi bi-check-circle-fill me-1"></i>' + el.innerText;
                } else {
                    el.className = 'text-danger';
                    el.innerHTML = '<i class="bi bi-x-circle me-1"></i>' + el.innerText;
                }
            }
            
            setReq(reqIds[0], hasLen);
            setReq(reqIds[1], hasAlphaNum);
            setReq(reqIds[2], hasSpec);
            setReq(reqIds[3], match);
            
            // Check if cedula is valid (only for register form)
            let isCedulaValid = true;
            if(btnId === 'btnRegistrar') {
                let msg = document.getElementById('cedulaMsg');
                if(msg && msg.classList.contains('text-danger')) {
                    isCedulaValid = false;
                }
            }
            
            btn.disabled = !(hasLen && hasAlphaNum && hasSpec && match && isCedulaValid);
        }
        
        clave.addEventListener('input', validate);
        conf.addEventListener('input', validate);
    }
    
    document.addEventListener('DOMContentLoaded', () => {
        setupPasswordValidation('regClave', 'regConfirmar', 'btnRegistrar', ['reqLen', 'reqAlphaNum', 'reqSpec', 'reqMatch']);
        setupPasswordValidation('resetClave', 'resetConfirmar', 'btnReset', ['reqLenR', 'reqAlphaNumR', 'reqSpecR', 'reqMatchR']);
    });

    function checkCedulaAPI(cedula) {
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
    }
</script>
</body>
"""

c = c.replace('</body>', js_code)

with io.open('src/main/webapp/login.jsp', 'w', encoding='utf-8') as f:
    f.write(c)

print("Updated login.jsp successfully")
