import requests

rhost = "http://localhost:"
red = "\033[0;31m"
green = "\033[0;32m"
blue = "\033[0;34m"
nc = "\033[0m"

def getHeadComp(port, uri):
    print(red + "HEAD & GET compared " + rhost + str(port) + uri + nc)
    print(green + "Expected: No FAILURE" + nc)
    r1 = requests.get(rhost + str(port) + uri)
    r2 = requests.head(rhost + str(port) + uri)
    print(blue + "Get headers: " + nc)
    for key1 in r1.headers.keys():
        print (key1 + ": " + r1.headers[key1])
    print(blue + "Head headers: " + nc)
    for key2 in r2.headers.keys():
        print (key2 + ": " + r2.headers[key2])
    for key1 in r1.headers.keys():
        if key1 == "Date" or key1 == "Last-Modified":
            continue
        for key2 in r2.headers.keys():
            if key1 == key2:
                if r1.headers[key1] == r2.headers[key2]:
                    break
        else:
            print(red + "FAILURE HEADERS NOT SAME AS GET" + nc)
    if r2.text:
        print(red + "FAILURE CONTENT"  + nc)


def cgi(port):
    pages = [
            "/cgi/",
            "/cgi/hello.sh",
            "/cgi/emptyCGIOutput.sh",
            "/cgi/helloLong.sh",
            "/cgi/queryStr.sh"
        ]
    for page in pages:
        getHeadComp(port, page)
        input("Press Enter: ")

