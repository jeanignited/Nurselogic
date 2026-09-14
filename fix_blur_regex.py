import io
import re
with io.open('src/main/webapp/includes/scripts.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

c = re.sub(r'\} else \{\s*// Limpiar si no existe\s*document\.getElementById\(\'nombres\'\)\.value = \'\';\s*document\.getElementById\(\'apellidos\'\)\.value = \'\';\s*document\.getElementById\(\'fechaNacimiento\'\)\.value = \'\';\s*\}', 
    r'} else {\n                                    // Comentado para evitar que borre los campos al seleccionar fechas o dar click fuera\n                                }', c)

with io.open('src/main/webapp/includes/scripts.jsp', 'w', encoding='utf-8') as f:
    f.write(c)
