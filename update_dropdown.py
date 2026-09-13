# -*- coding: utf-8 -*-
import io
import re

with io.open('src/main/webapp/views/dashboard.jsp', 'r', encoding='utf-8', errors='ignore') as f:
    c = f.read()

# 1. Change text-primary and text-warning to text-success for Estatura and Peso
c = c.replace('class="input-group-text border-secondary text-primary border-end-0"', 'class="input-group-text border-secondary text-success border-end-0"')
c = c.replace('class="input-group-text border-secondary text-warning border-end-0"', 'class="input-group-text border-secondary text-success border-end-0"')

# 2. Extract and replace the Especialidad block
pattern = r'<div class="mb-4">\s*<label class="form-label small text-secondary fw-semibold">Especialidad</label>.*?</div>\s*<div class="row g-4 mb-5">'

new_dropdown = u'''<div class="mb-4">
                                    <label class="form-label small text-secondary fw-semibold">Especialidad</label>
                                    <div class="dropdown">
                                        <input type="hidden" name="especialidad" id="hiddenEspecialidad" required>
                                        <button class="btn form-control form-control-lg border-secondary text-light text-start d-flex justify-content-between align-items-center dropdown-toggle" type="button" id="btnEspecialidad" data-bs-toggle="dropdown" aria-expanded="false" style="background: rgba(0,0,0,0.2);">
                                            <span id="btnEspecialidadText">Elige un &aacute;rea m&eacute;dica...</span>
                                        </button>
                                        <ul class="dropdown-menu w-100 dropdown-menu-dark p-2 shadow-lg border-secondary" style="max-height: 200px; overflow-y: auto;" aria-labelledby="btnEspecialidad">
                                            <li class="position-sticky top-0 bg-dark z-1 pb-2" style="margin-top: -8px; padding-top: 8px;">
                                                <input type="text" id="buscadorEspecialidades" class="form-control form-control-sm border-secondary text-light bg-dark" placeholder="Buscar especialidad..." autocomplete="off">
                                            </li>
                                            <%
                                                List<Map<String, String>> espMapPac = (List<Map<String, String>>) request.getAttribute("listaEspecialidadesMap");
                                                if(espMapPac != null && !espMapPac.isEmpty()) {
                                                    for(Map<String, String> mEsp : espMapPac) {
                                                        out.print("<li><a class='dropdown-item especialidad-item rounded' href='#' data-value='" + mEsp.get("id") + "'>" + mEsp.get("descripcion") + "</a></li>");
                                                    }
                                                } else {
                                                    out.print("<li><a class='dropdown-item especialidad-item rounded' href='#' data-value='1'>Medicina General</a></li>");
                                                    out.print("<li><a class='dropdown-item especialidad-item rounded' href='#' data-value='2'>Odontolog&iacute;a</a></li>");
                                                    out.print("<li><a class='dropdown-item especialidad-item rounded' href='#' data-value='3'>Pediatr&iacute;a</a></li>");
                                                    out.print("<li><a class='dropdown-item especialidad-item rounded' href='#' data-value='4'>Ginecolog&iacute;a</a></li>");
                                                    out.print("<li><a class='dropdown-item especialidad-item rounded' href='#' data-value='5'>Cardiolog&iacute;a</a></li>");
                                                    out.print("<li><a class='dropdown-item especialidad-item rounded' href='#' data-value='6'>Urgencias y Triage</a></li>");
                                                }
                                            %>
                                        </ul>
                                    </div>
                                </div>
                                <div class="row g-4 mb-5">'''

c = re.sub(pattern, new_dropdown, c, flags=re.DOTALL)

# Add the JS script before closing the form
# We can find </form> for this card and insert the script right before it.
script = u'''<script>
                                document.addEventListener("DOMContentLoaded", function() {
                                    const buscador = document.getElementById("buscadorEspecialidades");
                                    const items = document.querySelectorAll(".especialidad-item");
                                    const hiddenInput = document.getElementById("hiddenEspecialidad");
                                    const btnText = document.getElementById("btnEspecialidadText");

                                    if(buscador) {
                                        buscador.addEventListener("input", function(e) {
                                            const term = this.value.toLowerCase();
                                            items.forEach(item => {
                                                if(item.textContent.toLowerCase().includes(term)) {
                                                    item.style.display = "block";
                                                } else {
                                                    item.style.display = "none";
                                                }
                                            });
                                        });

                                        buscador.addEventListener("click", function(e) {
                                            e.stopPropagation();
                                        });
                                    }

                                    items.forEach(item => {
                                        item.addEventListener("click", function(e) {
                                            e.preventDefault();
                                            hiddenInput.value = this.getAttribute("data-value");
                                            btnText.textContent = this.textContent;
                                            if(buscador) {
                                                buscador.value = "";
                                                items.forEach(i => i.style.display = "block");
                                            }
                                        });
                                    });
                                });
                            </script>
                            </form>'''

# Replace the first </form> after the Agendar Cita text
form_pattern = r'CONFIRMAR CITA</button>\s*</form>'
form_replacement = u'CONFIRMAR CITA</button>\n' + script
c = re.sub(form_pattern, form_replacement, c)

with io.open('src/main/webapp/views/dashboard.jsp', 'w', encoding='utf-8') as f:
    f.write(c)

print("Dropdown and script integrated successfully.")
