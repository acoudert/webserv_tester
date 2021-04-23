import requests

rhost = "http://localhost:"
red = "\033[0;31m"
green = "\033[0;32m"
blue = "\033[0;34m"
nc = "\033[0m"

def custom404(port):
    print(red + "GET " + rhost + str(port) + "/idonotexist" + nc)
    print(green + "Expected: Error 404 + Content = \"404 Custom Error\\n\"" + nc)
    r = requests.get(rhost + str(port) + "/idonotexist")
    print(blue + "I received:" + nc)
    print("Status Code: " + str(r.status_code))
    for h in r.headers:
        print(h + ":" + r.headers[h])
    print()
    print(r.text)

