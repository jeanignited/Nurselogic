import io
with io.open('src/main/webapp/views/camas.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

c = c.replace('Observaci\xc3\xb3n', 'Observaci\xf3n')
c = c.replace('desinfecci\xc3\xb3n', 'desinfecci\xf3n')
c = c.replace('\xc3\xb3', '\xf3')
c = c.replace('\xc3\xad', '\xed')
c = c.replace('\xc3\xa1', '\xe1')
c = c.replace('\xc3\xa9', '\xe9')
c = c.replace('\xc3\xba', '\xfa')
c = c.replace('\xc3\xb1', '\xf1')
c = c.replace('\xc3\x8d', '\xcd')

with io.open('src/main/webapp/views/camas.jsp', 'w', encoding='utf-8') as f:
    f.write(c)
