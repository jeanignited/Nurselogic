import io
import re

with io.open('src/main/webapp/login.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

# 1. Update HTML structure for cedulaMsg
old_html = """<div class="col-6">
                        <input type="text" id="regCedula" name="cedula" class="form-control" placeholder="C\u00e9dula (10 d\u00edgitos)" maxlength="10" oninput="this.value = this.value.replace(/[^0-9]/g, ''); if(this.value.length===10) checkCedulaAPI(this.value);" required autocomplete="off">
                        <div id="cedulaMsg" class="small mt-1 d-none"></div>
                    </div>
                    <div class="col-6"><input type="text" name="telefono" class="form-control" placeholder="Tel\u00e9fono (10 d\u00edgitos)" maxlength="10" oninput="this.value = this.value.replace(/[^0-9]/g, '');" required autocomplete="off"></div>"""

new_html = """<div class="col-6">
                        <input type="text" id="regCedula" name="cedula" class="form-control" placeholder="C\u00e9dula (10 d\u00edgitos)" maxlength="10" oninput="this.value = this.value.replace(/[^0-9]/g, ''); if(this.value.length===10){ checkCedulaAPI(this.value); } else if(this.value.trim() === '') { let cm = document.getElementById('cedulaMsg'); cm.className='d-none'; cm.style.display='none'; document.getElementById('regClave').dispatchEvent(new Event('input')); }" required autocomplete="off">
                    </div>
                    <div class="col-6"><input type="text" name="telefono" class="form-control" placeholder="Tel\u00e9fono (10 d\u00edgitos)" maxlength="10" oninput="this.value = this.value.replace(/[^0-9]/g, '');" required autocomplete="off"></div>
                    <div class="col-12 mt-2">
                        <div id="cedulaMsg" class="small d-none d-block w-100 text-center py-2 rounded-2"></div>
                    </div>"""

c = c.replace(old_html, new_html)

# 2. Update JS in checkCedulaAPI
old_js = """function checkCedulaAPI(cedula) {
        let msg = document.getElementById('cedulaMsg');
        let btn = document.getElementById('btnRegistrar');
        msg.className = 'd-inline-block mt-2 px-2 py-1 rounded-2 fw-semibold text-info';"""

new_js = """function checkCedulaAPI(cedula) {
        let msg = document.getElementById('cedulaMsg');
        let btn = document.getElementById('btnRegistrar');
        msg.style.display = 'block';
        msg.className = 'd-block w-100 text-center mt-0 py-2 rounded-2 fw-semibold text-info';"""
        
c = c.replace(old_js, new_js)

old_js2 = """msg.className = 'd-inline-block mt-2 px-2 py-1 rounded-2 fw-bold text-danger';"""
new_js2 = """msg.className = 'd-block w-100 text-center mt-0 py-2 rounded-2 fw-bold text-danger';"""
c = c.replace(old_js2, new_js2)

old_js3 = """msg.className = 'd-inline-block mt-2 px-2 py-1 rounded-2 fw-semibold text-success';"""
new_js3 = """msg.className = 'd-block w-100 text-center mt-0 py-2 rounded-2 fw-semibold text-success';"""
c = c.replace(old_js3, new_js3)
c = c.replace(old_js3, new_js3) # Do it twice because it appears twice

with io.open('src/main/webapp/login.jsp', 'w', encoding='utf-8') as f:
    f.write(c)
    
print("Updated cedula UI logic.")
