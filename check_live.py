import urllib.request

try:
    response = urllib.request.urlopen('http://localhost:8080/nurselogic-web/dashboard?vista=pacientes')
    html = response.read().decode('utf-8')
    if 'JasperException' in html:
        print("FOUND JASPER EXCEPTION!")
    elif 'SyntaxError' in html:
        print("Syntax error!")
    elif 'cambiarVista' not in html:
        print("cambiarVista function missing in HTML output!")
    else:
        print("HTML looks fine?")
        print(html[-500:])
except Exception as e:
    print(f"Error fetching: {e}")
    try:
        html = e.read().decode('utf-8')
        if 'JasperException' in html:
            print("FOUND JASPER EXCEPTION IN ERROR STREAM!")
            print(html[html.find('JasperException'):html.find('JasperException')+500])
    except:
        pass
