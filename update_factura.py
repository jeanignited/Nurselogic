import io

with io.open('src/main/webapp/views/facturas.jsp', 'r', encoding='utf-8') as f:
    fac = f.read()

old_td = 'out.print("<td style=\'font-size: 0.85rem;\'>" + detalles.toString() + "</td>");'
new_td = 'out.print("<td style=\'font-size: 0.85rem;\'><div style=\'display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden; text-overflow: ellipsis; max-height: 2.8em; line-height: 1.4em; min-width: 250px;\'>" + detalles.toString() + "</div></td>");'

fac = fac.replace(old_td, new_td)

with io.open('src/main/webapp/views/facturas.jsp', 'w', encoding='utf-8') as f:
    f.write(fac)
