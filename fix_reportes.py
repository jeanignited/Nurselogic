import io, re

with io.open('src/main/webapp/views/reportes.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

def replace_alert(match):
    msg = match.group(1)
    if not msg.startswith("'") and not msg.startswith('"'):
        # It's a variable like data.message
        return "Swal.fire({text: " + msg + ", icon: 'info', background: 'var(--bg-panel)', color: 'var(--text-color)'})"
    return "Swal.fire({text: " + msg + ", icon: 'info', background: 'var(--bg-panel)', color: 'var(--text-color)'})"

c = re.sub(r'alert\((.*?)\)', replace_alert, c)

with io.open('src/main/webapp/views/reportes.jsp', 'w', encoding='utf-8') as f:
    f.write(c)

print("Replaced alerts in reportes")
