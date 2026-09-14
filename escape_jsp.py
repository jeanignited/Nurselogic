import io

with io.open('src/main/webapp/includes/scripts.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

c = c.replace('${vals.talla}', '\${vals.talla}')
c = c.replace('${vals.peso}', '\${vals.peso}')
c = c.replace('${vals.imc}', '\${vals.imc}')
c = c.replace('${vals.temp}', '\${vals.temp}')
c = c.replace('${vals.pa}', '\${vals.pa}')
c = c.replace('${vals.fc}', '\${vals.fc}')
c = c.replace('${vals.sato2}', '\${vals.sato2}')
c = c.replace('${vals.fr}', '\${vals.fr}')
c = c.replace('${vals.glasgow}', '\${vals.glasgow}')
c = c.replace('${restText}', '\${restText}')

with io.open('src/main/webapp/includes/scripts.jsp', 'w', encoding='utf-8') as f:
    f.write(c)

print("Escaped JSP EL")
