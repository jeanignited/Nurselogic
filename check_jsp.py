import io
with io.open('src/main/webapp/includes/scripts.jsp', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('<%')
while idx != -1:
    idx2 = text.find('%>', idx)
    content = text[idx:idx2+2]
    if 'medsGraf' in content:
        print("YES, medsGraf is inside <% %>")
    idx = text.find('<%', idx2)
