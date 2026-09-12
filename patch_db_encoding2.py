import io
with io.open('src/main/webapp/views/camas.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

c = c.replace('data-diagnostico="<%= c.get("diagnostico") %>', 'data-diagnostico="<%= c.get("diagnostico") != null ? c.get("diagnostico").replace("\xc3\xb3", "\xf3").replace("\xc3\xad", "\xed").replace("\xc3\xa1", "\xe1").replace("\xc3\xa9", "\xe9").replace("\xc3\xba", "\xfa").replace("\xc3\xb1", "\xf1") : "" %>')

with io.open('src/main/webapp/views/camas.jsp', 'w', encoding='utf-8') as f:
    f.write(c)
