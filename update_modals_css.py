import io
import re

with io.open('src/main/webapp/includes/modals.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

# I will just replace globally because print-text-black only affects the print view anyway!
c = c.replace('class=\"fw-bold text-warning\"', 'class=\"fw-bold text-warning print-text-black\"')
c = c.replace('class=\"fw-bold text-info\"', 'class=\"fw-bold text-info print-text-black\"')
c = c.replace('class=\"fw-bold text-success\"', 'class=\"fw-bold text-success print-text-black\"')
c = c.replace('text-warning\">', 'text-warning print-text-black\">')
c = c.replace('text-info\">', 'text-info print-text-black\">')
c = c.replace('text-success\">', 'text-success print-text-black\">')
c = c.replace('text-danger\">', 'text-danger print-text-black\">')
c = c.replace('text-primary\">', 'text-primary print-text-black\">')

with io.open('src/main/webapp/includes/modals.jsp', 'w', encoding='utf-8') as f:
    f.write(c)
print('Added print-text-black to modals.jsp')
