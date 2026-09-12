import io, re

with io.open('src/main/webapp/login.jsp', 'r', encoding='windows-1252') as f:
    c = f.read()

# Make the email input have autocomplete="off"
c = c.replace('name="usuario" class="form-control" placeholder="usuario@ejemplo.com" required autocomplete="off"', 
              'name="usuario" class="form-control" placeholder="usuario@ejemplo.com" required autocomplete="off"')
# Wait, let's just make the whole form have autocomplete="off" (it does)
# And the password field have autocomplete="new-password" to trick chrome
c = c.replace('name="clave" class="form-control" placeholder="&#9679;&#9679;&#9679;&#9679;&#9679;&#9679;&#9679;&#9679;" required autocomplete="off"',
              'name="clave" class="form-control" placeholder="&#9679;&#9679;&#9679;&#9679;&#9679;&#9679;&#9679;&#9679;" required autocomplete="new-password"')
# Also the create password
c = c.replace('name="clave" class="form-control" placeholder="Crear Contrase&ntilde;a" required autocomplete="off"',
              'name="clave" class="form-control" placeholder="Crear Contrase&ntilde;a" required autocomplete="new-password"')

with io.open('src/main/webapp/login.jsp', 'w', encoding='windows-1252') as f:
    f.write(c)
