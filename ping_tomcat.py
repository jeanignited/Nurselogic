import urllib.request
try:
    urllib.request.urlopen('http://localhost:8080/nurselogic/')
    print("Tomcat is up")
except Exception as e:
    print(e)
