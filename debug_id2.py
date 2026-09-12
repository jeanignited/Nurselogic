import io, re
with io.open('src/main/webapp/includes/scripts.jsp', 'rb') as f:
    c = f.read()

match = re.search(b'modalA.{1,5}Cama', c)
if match:
    print(match.group(0))
