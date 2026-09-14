import io
with io.open('src/main/webapp/includes/scripts.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

old_else = '''                                } else {



                                    // Limpiar si no existe



                                    document.getElementById('nombres').value = '';



                                    document.getElementById('apellidos').value = '';



                                    document.getElementById('fechaNacimiento').value = '';



                                }'''

new_else = '''                                } else {
                                    // Comentado para evitar que borre los campos al seleccionar fechas o dar click fuera
                                    // document.getElementById('nombres').value = '';
                                    // document.getElementById('apellidos').value = '';
                                    // document.getElementById('fechaNacimiento').value = '';
                                }'''

c = c.replace(old_else, new_else)

with io.open('src/main/webapp/includes/scripts.jsp', 'w', encoding='utf-8') as f:
    f.write(c)
