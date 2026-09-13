import io

with io.open('src/main/webapp/index.jsp', 'r', encoding='latin-1') as f:
    c = f.read()

animation_css = '''
        @keyframes fadeInDown {
            from { opacity: 0; transform: translateY(-20px); }
            to { opacity: 1; transform: translateY(0); }
        }
'''

if 'fadeInDown' not in c:
    c = c.replace('</style>', animation_css + '</style>')

with io.open('src/main/webapp/index.jsp', 'w', encoding='latin-1') as f:
    f.write(c)
print('Injected fadeInDown animation')
