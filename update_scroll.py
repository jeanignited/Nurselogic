import io
import re

with io.open('src/main/webapp/login.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

# Replace body css
old_body = '''        body { 
            background-color: var(--bg-main); 
            background-image: radial-gradient(circle at 50% 50%, rgba(59, 130, 246, 0.05), transparent 60%);
            color: #fff; 
            font-family: 'Inter', sans-serif; 
            display: flex; 
            align-items: center; 
            justify-content: center; 
            height: 100vh; 
            overflow: hidden; 
            margin: 0; 
        }'''

new_body = '''        body { 
            background-color: var(--bg-main); 
            background-image: radial-gradient(circle at 50% 50%, rgba(59, 130, 246, 0.05), transparent 60%);
            color: #fff; 
            font-family: 'Inter', sans-serif; 
            display: flex; 
            align-items: center; 
            justify-content: center; 
            min-height: 100vh; 
            overflow-y: auto; 
            overflow-x: hidden;
            margin: 0; 
            padding: 2rem 0;
        }
        
        ::-webkit-scrollbar { width: 8px; }
        ::-webkit-scrollbar-track { background: transparent; }
        ::-webkit-scrollbar-thumb { background: rgba(255,255,255,0.15); border-radius: 4px; }
        ::-webkit-scrollbar-thumb:hover { background: rgba(255,255,255,0.3); }'''

c = c.replace(old_body, new_body)

with io.open('src/main/webapp/login.jsp', 'w', encoding='utf-8') as f:
    f.write(c)

print("Updated body CSS for scrolling")
