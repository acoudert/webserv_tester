import requests

rhost = "http://localhost:"
red = "\033[0;31m"
green = "\033[0;32m"
blue = "\033[0;34m"
nc = "\033[0m"

def not_accepted_method(port, port2):
    print(red + "HEAD " + rhost + str(port) + "/" + nc)
    print(red + "HEAD " + rhost + str(port2) + "/" + nc)
    print(green + "Expected: " + str(port) + " returns head of autoindex of /pythonTest" + nc)
    print(green + "Expected: " + str(port2) + " returns Error" + nc)
    r = requests.head(rhost + str(port) + "/")
    print(blue + "I received: port " + str(port) + nc)
    print("Status Code: " + str(r.status_code))
    r = requests.head(rhost + str(port2) + "/")
    print(blue + "I received: port " + str(port2) + nc)
    print("Status Code: " + str(r.status_code))
