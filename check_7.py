import io
with io.open('src/main/webapp/includes/scripts.jsp', 'r', encoding='utf-8') as f:
    text = f.read()
if 'countM++ >= 7' in text:
    print('YES, it limits to 7')
else:
    print('NO, missing limit 7')
