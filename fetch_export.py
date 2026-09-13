import urllib.request
import urllib.error

try:
    req = urllib.request.Request('http://localhost:8080/nurselogic/exportCsv?tipo=facturas&desde=2026-09-10&hasta=2026-09-11', headers={'Cookie': 'JSESSIONID=dummy'})
    with urllib.request.urlopen(req) as response:
        print("OK", response.status)
except urllib.error.HTTPError as e:
    print(e.status, e.read().decode('utf-8'))
except Exception as e:
    print(e)
