with open('src/main/webapp/includes/modals.jsp', 'r', encoding='utf-8') as f:
    for i, line in enumerate(f.readlines()[:5]):
        print(f"Line {i+1}: {repr(line)}")
