import urllib.request
import urllib.parse
import http.cookiejar

cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))

# Login
url_login = "http://localhost:8080/nurselogic/login"
data = urllib.parse.urlencode({'usuario': 'admin@nurselogic.com', 'clave': 'admin123'}).encode('utf-8')
req_login = urllib.request.Request(url_login, data=data)
opener.open(req_login)

# Get dashboard
url_dash = "http://localhost:8080/nurselogic/dashboard"
req_dash = urllib.request.Request(url_dash)
response = opener.open(req_dash)
content = response.read().decode('utf-8', errors='ignore')

# print last 100 lines
lines = content.split('\n')
for i in range(max(0, len(lines)-100), len(lines)):
    print(f"Line {i+1}: {lines[i]}")
