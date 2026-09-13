import io
import re

with io.open('src/main/webapp/includes/modals.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

c = c.replace('<%@ page contentType="text/html; charset=UTF-8" pageEncoding="UTF-8" %>', '<%@ page contentType="text/html; charset=UTF-8" %>')

with io.open('src/main/webapp/includes/modals.jsp', 'w', encoding='utf-8') as f:
    f.write(c)

print("modals.jsp encoding directive cleaned.")
