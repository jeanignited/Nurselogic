import urllib.request
import urllib.parse
from http.cookiejar import CookieJar

cj = CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))

# 1. Login
data = urllib.parse.urlencode({'correo': 'admin@nurselogic.com', 'password': 'admin', 'action': 'login'}).encode('utf-8')
req = urllib.request.Request('http://localhost:8080/nurselogic/login', data=data)
try:
    opener.open(req)
except Exception as e:
    pass

# 2. Fetch dashboard
try:
    resp = opener.open('http://localhost:8080/nurselogic/dashboard')
    html = resp.read().decode('utf-8')
    with open('dashboard_dump2.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Dashboard length:", len(html))
except Exception as e:
    if hasattr(e, 'read'):
        html = e.read().decode('utf-8')
        with open('dashboard_dump2.html', 'w', encoding='utf-8') as f:
            f.write(html)
        print("Dashboard 500 length:", len(html))
    else:
        print(e)
