import io

with io.open('src/main/webapp/index.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

print_css = '''
          @media print {
              .print-text-black, .text-warning, .text-info, .text-success, .text-danger, .text-primary, .text-secondary, .text-light, .text-white, .text-purple { color: black !important; }
              .badge { color: black !important; border: 1px solid black !important; background: transparent !important; }
              body { color: black !important; }
          }
'''

c = c.replace('</style>', print_css + '</style>')

with io.open('src/main/webapp/index.jsp', 'w', encoding='utf-8') as f:
    f.write(c)

print("Added @media print to index.jsp")
