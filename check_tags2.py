import io
import re

def check_file(path):
    with io.open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    opens = re.findall(r'<%(?!@|--)', content)
    closes = re.findall(r'(?<!--)%>', content)
    
    if len(opens) != len(closes):
        print(f"Error in {path}: open {len(opens)}, close {len(closes)}")

check_file('src/main/webapp/includes/sidebar.jsp')
check_file('src/main/webapp/views/dashboard.jsp')
check_file('src/main/webapp/views/personal.jsp')
check_file('src/main/webapp/index.jsp')
