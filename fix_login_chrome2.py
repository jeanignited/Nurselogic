import io, re

with io.open('src/main/webapp/login.jsp', 'r', encoding='windows-1252') as f:
    c = f.read()

c = re.sub(r'(name="(?:clave|nuevaClave)"[^>]*?)autocomplete="off"', r'\1autocomplete="new-password"', c)
# And for email, sometimes autocomplete="off" is ignored, use autocomplete="nope"
c = re.sub(r'(name="(?:usuario|correo)"[^>]*?)autocomplete="off"', r'\1autocomplete="nope"', c)

with io.open('src/main/webapp/login.jsp', 'w', encoding='windows-1252') as f:
    f.write(c)
