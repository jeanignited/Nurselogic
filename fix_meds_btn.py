import io
import re
with io.open('src/main/webapp/views/medicamentos.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

# Replace the TD that contains the Add to Cart button to also include the Delete button for admin
old_td = r'out\.print\("<button class=\'btn btn-sm btn-outline-info rounded-circle px-2\' title=\'A\u00F1adir al carrito\' onclick=\\"agregarAlCarrito\(" \+ m\.get\("id"\) \+ ", \'" \+ m\.get\("nombre"\)\.replace\("\'", "\\\\\'"\) \+ "\', " \+ m\.get\("precio"\) \+ ", " \+ m\.get\("stock"\) \+ "\)\\"><i class=\'bi bi-cart-plus\'><\/i><\/button>"\);'
new_td = '''out.print("<div class='d-flex justify-content-center gap-2'>");
                                                out.print("<button class='btn btn-sm btn-outline-info rounded-circle px-2' title='A\\u00F1adir al carrito' onclick=\\"agregarAlCarrito(" + m.get("id") + ", '" + m.get("nombre").replace("'", "\\\\'") + "', " + m.get("precio") + ", " + m.get("stock") + ")\\"><i class='bi bi-cart-plus'></i></button>");
                                                if(isAdmin) { out.print("<button class='btn btn-sm btn-outline-danger rounded-circle px-2' title='Eliminar F\\u00E1rmaco' onclick=\\"borrarMedicamento(" + m.get("id") + ")\\"><i class='bi bi-trash'></i></button>"); }
                                                out.print("</div>");'''

c = re.sub(old_td, new_td, c)
with io.open('src/main/webapp/views/medicamentos.jsp', 'w', encoding='utf-8') as f:
    f.write(c)

print("Added delete button to medicamentos.jsp")
