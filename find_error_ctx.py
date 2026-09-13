with open('src/main/webapp/includes/scripts.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

idx = 53294
start = max(0, idx - 100)
end = min(len(c), idx + 100)
print(c[start:end])
