import urllib.request
import urllib.error

try:
    req = urllib.request.Request('http://localhost:8080/nurselogic/', headers={'Cookie': 'JSESSIONID=dummy'})
    with urllib.request.urlopen(req) as response:
        print("OK", response.status)
except urllib.error.HTTPError as e:
    print(e.read().decode('utf-8'))
except Exception as e:
    print(e)
