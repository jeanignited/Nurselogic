import io
import re

with io.open('src/main/webapp/includes/scripts.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

bad_html = '''div.innerHTML = 
                <div class="input-group input-group-sm">
                    <span class="input-group-text bg-dark border-secondary text-white w-50 text-truncate" title="">\\</span>
                    <input type="number" class="form-control text-center stock-qty-input" placeholder="Cant." min="1" value="10">
                </div>
            ;'''
good_html = "div.innerHTML = '<div class=\"input-group input-group-sm\"><span class=\"input-group-text bg-dark border-secondary text-white w-50 text-truncate\" title=\"' + opt.text + '\">' + opt.text + '</span><input type=\"number\" class=\"form-control text-center stock-qty-input\" placeholder=\"Cant.\" min=\"1\" value=\"10\"></div>';"

c = c.replace(bad_html, good_html)

with io.open('src/main/webapp/includes/scripts.jsp', 'w', encoding='utf-8') as f:
    f.write(c)

print("Fixed backtick syntax error")
