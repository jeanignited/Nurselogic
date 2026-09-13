import io
with io.open('src/main/webapp/views/medicamentos.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

# I will find the EXACT string by reading it first
idx = c.find('agregarAlCarrito')
if idx != -1:
    start = c.rfind('<button', 0, idx)
    end = c.find('</button>', idx) + 9
    old_btn = c[start:end]
    
    new_btns = '''<div class='d-flex justify-content-center gap-2'>
''' + old_btn + '''
<% if(isAdmin) { %>
<button class='btn btn-sm btn-outline-danger rounded-circle px-2' title='Eliminar F\u00E1rmaco' onclick="borrarMedicamento(<%= m.get(\\"id\\") %>)"><i class='bi bi-trash'></i></button>
<% } %>
</div>'''
    
    c = c.replace(old_btn, new_btns)
    with io.open('src/main/webapp/views/medicamentos.jsp', 'w', encoding='utf-8') as f:
        f.write(c)
    print("Replaced!")
else:
    print("Not found!")
