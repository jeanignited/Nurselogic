import urllib.request
import urllib.error

try:
    req = urllib.request.Request('http://localhost:8080/nurselogic/exportCsv?tipo=facturas&desde=2026-09-10&hasta=2026-09-11', headers={'Cookie': 'JSESSIONID=dummy'})
    with urllib.request.urlopen(req) as response:
        print("OK", response.status)
        content = response.read().decode('utf-8')
        print(content[:100])
except urllib.error.HTTPError as e:
    print("HTTPError", e.status)
except Exception as e:
    print(e)
