import io

with io.open('src/main/webapp/views/personal.jsp', 'r', encoding='utf-8') as f:
    personal = f.read()

bad = 'out.print("<button class=\'btn btn-sm btn-outline-danger\' onclick="confirmarBorrado(\'rol\', \'" + rObj.getId() + "\')"><i class=\'bi bi-trash\'></i></button>");'
good = 'out.print("<button class=\'btn btn-sm btn-outline-danger\' onclick=\\"confirmarBorrado(\'rol\', \'" + rObj.getId() + "\')\\"><i class=\'bi bi-trash\'></i></button>");'

personal = personal.replace(bad, good)

with io.open('src/main/webapp/views/personal.jsp', 'w', encoding='utf-8') as f:
    f.write(personal)
