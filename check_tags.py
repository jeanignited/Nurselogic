import io
import sys

def check_file(path):
    with io.open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    open_count = content.count('<%') - content.count('<%@') - content.count('<%--')
    close_count = content.count('%>') - content.count('<%@') - content.count('--%>')
    if open_count != close_count:
        print(f"Error in {path}: open {open_count}, close {close_count}")

check_file('src/main/webapp/includes/sidebar.jsp')
check_file('src/main/webapp/views/dashboard.jsp')
check_file('src/main/webapp/views/personal.jsp')
