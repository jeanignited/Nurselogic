import sys
content = open('src/main/webapp/views/camas.jsp', 'r', encoding='windows-1252').read()
idx = content.find('replace', content.find('data-diagnostico'))
print(repr(content[idx:idx+40]))
