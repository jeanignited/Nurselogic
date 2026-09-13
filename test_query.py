import urllib.request
import urllib.error

try:
    req = urllib.request.Request('http://localhost:8080/nurselogic/exportCsv?tipo=facturas&desde=2026-09-10&hasta=2026-09-11', headers={'Cookie': 'JSESSIONID=dummy'})
    with urllib.request.urlopen(req) as response:
        print("OK", response.status)
except urllib.error.HTTPError as e:
    # Tomcat 500 error page doesn't show the stack trace here because it forwards to the 404/500 error page.
    pass
