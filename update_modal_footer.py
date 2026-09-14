import io
import re

with io.open('src/main/webapp/includes/modals.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

# Replace the footer of modalFichaClinica
old_footer = '''<div class="modal-footer border-0 pt-0">
          <button type="button" class="btn btn-outline-warning rounded-pill px-4" onclick="editarPacienteDesdeFicha()"><i class="bi bi-pencil-square me-1"></i>Editar Paciente</button>
          <button type="button" class="btn btn-secondary rounded-pill px-4" onclick="cerrarModalFicha()">Cerrar</button>
        </div>'''

new_footer = '''<div class="modal-footer border-0 pt-0">
          <button type="button" class="btn btn-info px-4 me-auto text-white fw-bold" onclick="imprimirHistorialMedico('#modalFichaClinica')" style="border-radius: 8px;"><i class="bi bi-printer me-2"></i>Imprimir</button>
          <button type="button" class="btn btn-outline-warning rounded-pill px-4" onclick="editarPacienteDesdeFicha()"><i class="bi bi-pencil-square me-1"></i>Editar Paciente</button>
          <button type="button" class="btn btn-secondary rounded-pill px-4" onclick="cerrarModalFicha()">Cerrar</button>
        </div>'''

c = c.replace(old_footer, new_footer)

with io.open('src/main/webapp/includes/modals.jsp', 'w', encoding='utf-8') as f:
    f.write(c)
