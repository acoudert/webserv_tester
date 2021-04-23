import requests

rhost = "http://localhost:"
red = "\033[0;31m"
green = "\033[0;32m"
blue = "\033[0;34m"
nc = "\033[0m"

def get_index(port, port2):
    print(red + "GET " + rhost + str(port) + "/" + nc)
    print(red + "GET " + rhost + str(port2) + "/" + nc)
    print(green + "Expected: " + str(port) + " returns autoindex of /pythonTest" + nc)
    print(green + "Expected: " + str(port2) + " returns content of /pythonTest/index.html" + nc)
    r = requests.get(rhost + str(port) + "/")
    print(blue + "I received: port " + str(port) + nc)
    print(r.text)
    r = requests.get(rhost + str(port2) + "/")
    print(blue + "I received: port " + str(port2) + nc)
    print(r.text)

