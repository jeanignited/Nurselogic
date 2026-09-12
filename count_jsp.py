import re
with open('src/main/webapp/includes/scripts.jsp', 'r', encoding='utf-8', errors='ignore') as f:
    c = f.read()

print("Number of <% :", c.count('<%'))
print("Number of %> :", c.count('%>'))
