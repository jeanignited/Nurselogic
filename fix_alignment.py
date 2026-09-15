import io
import re

with io.open('src/main/webapp/includes/modals.jsp', 'r', encoding='utf-8') as f:
    mod = f.read()

# Remove the old "Asignacion de Permisos"
mod = mod.replace("""                        <label class="form-label small text-secondary fw-bold mb-3">
                            <i class="bi bi-toggles me-1"></i>Asignación de Permisos
                        </label>
                        <div class="row g-2">

                            <!-- COLUMNA IZQUIERDA — permisos CSV legacy -->
                            <div class="col-md-6">""", """                        <div class="row g-2">

                            <!-- COLUMNA IZQUIERDA — permisos CSV legacy -->
                            <div class="col-md-6">
                                <p class="text-secondary small fw-bold mb-3" style="border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom:4px;">
                                    <i class="bi bi-toggles me-1"></i>Asignación de Permisos
                                </p>""")

# Replace the right side to match
mod = mod.replace("""                            <div class="col-md-6">
                                <p class="text-secondary small fw-semibold mb-2" style="border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom:4px;">
                                    Módulos del Sistema
                                </p>""", """                            <div class="col-md-6">
                                <p class="text-secondary small fw-bold mb-3" style="border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom:4px;">
                                    Módulos del Sistema
                                </p>""")

with io.open('src/main/webapp/includes/modals.jsp', 'w', encoding='utf-8') as f:
    f.write(mod)
