import io

with io.open('src/main/webapp/includes/scripts.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

broken_regex = '''let regex = /(FC|PA|FR|Temp|IMC|Glasgow|SpO2|SatO2|Talla|Peso):\s*([^
]+)
?/gi;'''

fixed_regex = r"let regex = /(FC|PA|FR|Temp|IMC|Glasgow|SpO2|SatO2|Talla|Peso):\s*([^\n]+)\n?/gi;"

c = c.replace(broken_regex, fixed_regex)

with io.open('src/main/webapp/includes/scripts.jsp', 'w', encoding='utf-8') as f:
    f.write(c)
    
print("Fixed broken regex")
