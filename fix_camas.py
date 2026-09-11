import io, re
with io.open('src/main/webapp/views/camas.jsp', 'r', encoding='windows-1252') as f:
    c = f.read()
c = re.sub(r'replace\([^\)]*?, "&quot;"\)', r'replace("\"", "&quot;")', c)
with io.open('src/main/webapp/views/camas.jsp', 'w', encoding='windows-1252') as f:
    f.write(c)
