import io
with io.open('lint.js', 'r', encoding='utf-8') as f:
    c = f.read()
idx = c.find('chartStockInst = new Chart(ctxStock')
print(c[idx:idx+1500])
