import requests

rhost = "http://localhost:"
red = "\033[0;31m"
green = "\033[0;32m"
blue = "\033[0;34m"
nc = "\033[0m"

def getRequest(port, uri, expected):
    print(red + "GET " + rhost + str(port) + uri + nc)
    print(green + "Expected: " + expected + nc)
    r = requests.get(rhost + str(port) + uri)
    print(blue + "I received:" + nc)
    print("Status Code: " + str(r.status_code))
    for h in r.headers:
        print(h + ":" + r.headers[h])
    print()
    print(r.text)


def classic(port):
    pages = [
            ["/index.html", "Content of index.html"],
            ["/noperm.html", "Error"],
            ["/", "Autoindex"],
            ["", "Autoindex"],
            ["/dir/indexDir.html", "Content of indexDir.html"],
            ["/ipointtodir/indexDir.html", "Content of indexDir.html"],
            ["/dir/", "autoindex of dir"],
            ["/dir/subdir/emptyFile.html", "No Body - No Crash - No Infinite Loop"],
            ["/text.txt", "Content of text.txt"],
            ["/idonotexist", "Error"]
        ]
    for page in pages:
        getRequest(port, page[0], page[1])
        input("Press Enter: ")

