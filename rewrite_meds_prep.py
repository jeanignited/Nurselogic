import io, re

with io.open('src/main/webapp/views/medicamentos.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

# 1. Remove <th>
old_th = '''<% if(canManageStock || canSellStock) { out.print("<th>Ajuste Ropido de Stock</th>"); } %>'''
old_th2 = '''<% if(canManageStock || canSellStock) { out.print("<th>Ajuste R\xc3\xadpido de Stock</th>"); } %>'''
old_th3 = '''<% if(canManageStock || canSellStock) { out.print("<th>Ajuste Rápido de Stock</th>"); } %>'''

# Find the actual line
for line in c.split('\n'):
    if 'Ajuste R' in line and '<th>' in line:
        c = c.replace(line, '<% if(canSellStock) { out.print("<th>Acciones</th>"); } %>')

# 2. Modify <td> loop
# We'll just replace the entire if (canManageStock || canSellStock) block in the loop.
# But let's first check what it looks like.
