import requests

rhost = "http://localhost:"
red = "\033[0;31m"
green = "\033[0;32m"
blue = "\033[0;34m"
nc = "\033[0m"

def not_accepted_method(port):
    pages = [
            "/ipointtodir",
            "/ipointtodir/indexDir.html"
        ]
    for page in pages:
        print(red + "HEAD as not accepted method " + rhost + str(port) + page + nc)
        print(green + "Expected: Error" + nc)
        r = requests.head(rhost + str(port) + page)
        print("Status Code: " + str(r.status_code))
        if r.status_code < 400:
            print(red + "FAILURE NO ERROR" + nc)
        input("Press Enter: ")

