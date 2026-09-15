import io

with io.open('src/main/webapp/includes/sidebar.jsp', 'r', encoding='utf-8') as f:
    sb = f.read()

sb = sb.replace('<% if(!isFarmaceutico) { %>', '<% if(permUsuarios || isAdmin) { %>')
sb = sb.replace('<% } /* fin !isFarmaceutico */ %>', '<% } /* fin estadisticas */ %>')

with io.open('src/main/webapp/includes/sidebar.jsp', 'w', encoding='utf-8') as f:
    f.write(sb)
