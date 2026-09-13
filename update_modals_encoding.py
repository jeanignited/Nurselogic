import io

with io.open('src/main/webapp/includes/modals.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

if not c.startswith('<%@ page'):
    c = '<%@ page contentType="text/html; charset=UTF-8" pageEncoding="UTF-8" %>\n' + c
    with io.open('src/main/webapp/includes/modals.jsp', 'w', encoding='utf-8') as f:
        f.write(c)
        print("modals.jsp prepended.")
else:
    print("Already has page directive.")
