import io
import re

with io.open('src/main/webapp/login.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

# Replace PANEL REGISTRO
old_register = '''        <!-- PANEL REGISTRO -->
        <div id="panel-register" class="panel d-none">
            <form action="registroUsuario" method="post" autocomplete="off">
                <div class="row g-2 mb-3">
                    <div class="col-6"><input type="text" name="nombres" class="form-control" placeholder="Nombres" required autocomplete="off"></div>
                    <div class="col-6"><input type="text" name="apellidos" class="form-control" placeholder="Apellidos" required autocomplete="off"></div>
                    <div class="col-12"><input type="email" name="correo" class="form-control" placeholder="Correo Electr\u00f3nico" required autocomplete="nope"></div>
                    <div class="col-6"><input type="text" name="cedula" class="form-control" placeholder="C\u00e9dula (10 d\u00edgitos)" maxlength="10" oninput="this.value = this.value.replace(/[^0-9]/g, '');" required autocomplete="off"></div>
                    <div class="col-6"><input type="text" name="telefono" class="form-control" placeholder="Tel\u00e9fono (10 d\u00edgitos)" maxlength="10" oninput="this.value = this.value.replace(/[^0-9]/g, '');" required autocomplete="off"></div>
                    <div class="col-12"><input type="text" name="direccion" class="form-control" placeholder="Direcci\u00f3n" required autocomplete="off"></div>
                    <div class="col-12"><input type="password" name="clave" class="form-control" placeholder="Crear Contrase\u00f1a" required autocomplete="new-password"></div>
                    <div class="col-12">
                        <select name="tipoUsuario" class="form-select" required>
                            <option value="" disabled selected>Seleccione el tipo de cuenta...</option>
                            <option value="Paciente">Soy Paciente</option>
                            <option value="Medico">Soy Personal M\u00e9dico</option>
                        </select>
                    </div>
                </div>
                <button type="submit" class="btn btn-success"><i class="bi bi-person-plus me-2"></i>REGISTRAR USUARIO</button>
            </form>
            <div class="text-center mt-4">
                <a href="#" class="text-decoration-none small text-secondary" onclick="mostrarPanel('panel-login')"><i class="bi bi-arrow-left me-1"></i>Volver al Login</a>
            </div>
        </div>'''

# We will use regex to replace it because of encoding chars in my string above
