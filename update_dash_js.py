import io
import re

with io.open('src/main/webapp/views/dashboard.jsp', 'r', encoding='utf-8', errors='ignore') as f:
    c = f.read()

# Fix Script Event Listeners
old_script = '''<script>
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
                            </script>'''

new_script = '''<script>
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

                                    if(hiddenInput && btnText) {
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
                                    }
                                });
                            </script>'''

c = c.replace(old_script, new_script)

# Add w-100 to all tables
c = c.replace('class="table table-borderless table-hover text-white align-middle mb-0" style="background: transparent;"', 'class="table table-borderless table-hover text-white align-middle mb-0 w-100" style="background: transparent;"')

with io.open('src/main/webapp/views/dashboard.jsp', 'w', encoding='utf-8') as f:
    f.write(c)

print("JS and table w-100 updated.")
