import io
for file in ['src/main/webapp/views/reportes.jsp', 'src/main/webapp/views/facturas.jsp']:
    with io.open(file, 'r', encoding='windows-1252') as f:
        c = f.read()
    print(f'{file} script tags: {c.count("<script")} / {c.count("</script")}')
