import io
with io.open('src/main/webapp/index.jsp', 'r', encoding='utf-8', errors='ignore') as f:
    c = f.read()

if '<%@ page pageEncoding="UTF-8" %>' not in c:
    c = '<%@ page pageEncoding="UTF-8" %>\n' + c
    with io.open('src/main/webapp/index.jsp', 'w', encoding='utf-8') as f:
        f.write(c)
        print("Added pageEncoding to index.jsp")
