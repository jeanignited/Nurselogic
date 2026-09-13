import urllib.request
import urllib.error
import urllib.parse
from http.cookiejar import CookieJar

cj = CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
urllib.request.install_opener(opener)

# 1. Login
data = urllib.parse.urlencode({'correo': 'admin@nurselogic.com', 'password': 'admin'}).encode('utf-8')
try:
    opener.open('http://localhost:8080/nurselogic/login', data)
except Exception as e:
    pass

# 2. Access dashboard
try:
    resp = opener.open('http://localhost:8080/nurselogic/dashboard')
    html = resp.read().decode('utf-8')
    with open('dashboard_dump.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Dashboard fetched, length:", len(html))
except urllib.error.HTTPError as e:
    err = e.read().decode('utf-8')
    with open('dashboard_error.html', 'w', encoding='utf-8') as f:
        f.write(err)
    print("Dashboard 500 error, saved to dashboard_error.html")
except Exception as e:
    print(e)
