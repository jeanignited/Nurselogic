import io
with io.open('src/main/webapp/views/medicamentos.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

old_td = '''out.print("<button class='btn btn-sm btn-outline-info rounded-circle px-2' title='A\\u00F1adir al carrito' onclick=\\"agregarAlCarrito(" + m.get("id") + ", '" + m.get("nombre").replace("'", "\\\\'") + "', " + m.get("precio") + ", " + m.get("stock") + ")\\"><i class='bi bi-cart-plus'></i></button>");'''
new_td = '''out.print("<div class='d-flex justify-content-center gap-2'>");
                                                out.print("<button class='btn btn-sm btn-outline-info rounded-circle px-2' title='A\\u00F1adir al carrito' onclick=\\"agregarAlCarrito(" + m.get("id") + ", '" + m.get("nombre").replace("'", "\\\\'") + "', " + m.get("precio") + ", " + m.get("stock") + ")\\"><i class='bi bi-cart-plus'></i></button>");
                                                if(isAdmin) { out.print("<button class='btn btn-sm btn-outline-danger rounded-circle px-2' title='Eliminar' onclick=\\"borrarMedicamento(" + m.get("id") + ")\\"><i class='bi bi-trash'></i></button>"); }
                                                out.print("</div>");'''

if old_td in c:
    c = c.replace(old_td, new_td)
    with io.open('src/main/webapp/views/medicamentos.jsp', 'w', encoding='utf-8') as f:
        f.write(c)
    print("Added delete button to medicamentos.jsp")
else:
    print("Not found old_td")
