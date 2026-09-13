import urllib.request
try:
    urllib.request.urlopen('http://localhost:8080/nurselogic/')
except Exception as e:
    print(e.read().decode('utf-8'))
