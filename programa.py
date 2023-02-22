import requests

r = requests.get('http://httpbin.org/status/404')

if r.status_code==404:
    print("ok")
    print("tengo un pedazo pollon")
    print(r.status_code)

else:
    print("joder que asco das puto negrata")
