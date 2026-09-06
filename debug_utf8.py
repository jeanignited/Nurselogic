import sys

def debug_file(path):
    with open(path, 'rb') as f:
        content = f.read()
    if content.startswith(b'\xef\xbb\xbf'):
        content = content[3:]
    text = content.decode('utf-8')
    
    for i, c in enumerate(text):
        try:
            c.encode('latin1')
        except:
            print(f"Error at char {i} in {path}: {repr(c)}")
            
debug_file('src/main/webapp/views/medicamentos.jsp')
debug_file('src/main/webapp/includes/modals.jsp')
