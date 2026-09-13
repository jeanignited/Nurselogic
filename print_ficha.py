import io
with io.open('src/main/webapp/includes/scripts.jsp', 'r', encoding='utf-8') as f:
    text = f.read()
idx = text.find('window.verFichaClinica')
print(text[idx:idx+800])
