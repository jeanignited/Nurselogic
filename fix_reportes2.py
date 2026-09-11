import io, re

with io.open('src/main/webapp/views/reportes.jsp', 'r', encoding='windows-1252') as f:
    c = f.read()

# Replace the current description cell with expandable div
# Right now it's:
# out.print("<td>" + ticket.getDescripcion() + "</td>");
# We change it to:
# out.print("<td><div style='max-height: 40px; overflow: hidden;'>" + ticket.getDescripcion() + "</div><button class='btn btn-link btn-sm p-0 text-info' style='font-size: 0.8rem;' onclick='expandirDescTI(this)'>Ver ms</button></td>");

c = c.replace('out.print("<td>" + ticket.getDescripcion() + "</td>");', 'out.print("<td><div style=\'max-height: 40px; overflow: hidden;\'>" + ticket.getDescripcion() + "</div><button class=\'btn btn-link btn-sm p-0 text-info\' style=\'font-size: 0.8rem;\' onclick=\'expandirDescTI(this)\'>Ver ms</button></td>");')

with io.open('src/main/webapp/views/reportes.jsp', 'w', encoding='windows-1252') as f:
    f.write(c)
