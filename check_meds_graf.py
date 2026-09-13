import io
with io.open('src/main/webapp/includes/scripts.jsp', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('List<Map<String, String>> medsGraf')
if idx == -1:
    idx = text.find('listaMedicamentos')
    
print(text[max(0, idx-50):idx+800])
