import io
import re

with io.open('src/main/webapp/views/medicamentos.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

start_idx = c.find("out.print(\"<div class='d-flex justify-content-center gap-2'>")
if start_idx != -1:
    end_idx = c.find('</div>");', start_idx) + 9
    
    old_block = c[start_idx:end_idx]
    
    agg_start = old_block.find('<button')
    agg_end = old_block.find('</button>') + 9
    agg_btn = old_block[agg_start:agg_end]
    
    new_java = "out.print(\"<div class='d-flex justify-content-center gap-2'>\");\n"
    new_java += "out.print(\"" + agg_btn + "\");\n"
    new_java += "if(isAdmin) {\n"
    new_java += "    out.print(\"<button class='btn btn-sm btn-outline-danger rounded-circle px-2' title='Eliminar F\u00E1rmaco' onclick=\\\"borrarMedicamento(\" + m.get(\\\"id\\\") + \")\\\"><i class='bi bi-trash'></i></button>\");\n"
    new_java += "}\n"
    new_java += "out.print(\"</div>\");"
    
    c = c[:start_idx] + new_java + c[end_idx:]
    
    with io.open('src/main/webapp/views/medicamentos.jsp', 'w', encoding='utf-8') as f:
        f.write(c)
    print("Fixed out.print block")
else:
    print("Could not find the block")
