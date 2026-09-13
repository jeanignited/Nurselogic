# -*- coding: utf-8 -*-
import io, re

with io.open('src/main/webapp/views/medicamentos.jsp', 'r', encoding='utf-8', errors='ignore') as f:
    c = f.read()

# Replace the TH
c = re.sub(r'<% if\(canManageStock \|\| canSellStock\) \{ out\.print\("<th>Ajuste R[^<]*</th\>"\); \} %>', r'<% if(canSellStock) { out.print("<th><i class=\'bi bi-cart-plus me-1\'></i></th>"); } %>', c)

# Replace the TD buttons
old_td = r'if \(canManageStock \|\| canSellStock\) \{.*?out\.print\("</td>"\);\s*\}'

new_td = '''if (canSellStock) {
                                            out.print("<td class='text-center'>");
                                            if (st > 0) {
                                                out.print("<button class='btn btn-sm btn-outline-info rounded-circle px-2' title='A\\xf1adir al carrito' onclick=\\"agregarAlCarrito(" + m.get("id") + ", '" + m.get("nombre").replace("'", "\\\\'") + "', " + m.get("precio") + ", " + m.get("stock") + ")\\"><i class='bi bi-cart-plus'></i></button>");
                                            } else {
                                                out.print("<button class='btn btn-sm btn-outline-secondary rounded-circle px-2' disabled><i class='bi bi-cart-x'></i></button>");
                                            }
                                            out.print("</td>");
                                        }'''

c = re.sub(old_td, new_td, c, flags=re.DOTALL)

# Add the "Añadir Stock" button next to search bar
search_bar = r'<div class="mb-3 position-relative" style="max-width: 400px;">.*?</div>'
new_search = '''<div class="d-flex justify-content-between align-items-center mb-3 flex-wrap gap-2">
                <div class="position-relative flex-grow-1" style="max-width: 400px;">
                    <i class="bi bi-search position-absolute top-50 start-0 translate-middle-y ms-3 text-secondary"></i>
                    <input type="text" id="buscadorMedicamentos" class="form-control ps-5 form-control-sm" style="border: var(--glass-border); border-radius: 20px;" placeholder="Buscar f\\xe1rmaco o estado de bodega..." onkeyup="filtrarMedicamentos()" autocomplete="off">
                </div>
                <% if(canManageStock) { %>
                <button type="button" class="btn btn-sm px-4 py-2 fw-bold shadow-sm text-dark" style="background: linear-gradient(135deg, #a3e635, #84cc16); border:none; border-radius: 20px;" onclick="abrirModalAnadirStockMultiple()">
                    <i class="bi bi-box-arrow-in-down me-2"></i>Abastecimiento M\\xfaltiple
                </button>
                <% } %>
            </div>'''
c = re.sub(search_bar, new_search, c, flags=re.DOTALL)

with io.open('src/main/webapp/views/medicamentos.jsp', 'w', encoding='utf-8') as f:
    f.write(c)

print("Updated medicamentos.jsp")
