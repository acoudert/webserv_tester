import requests

rhost = "http://localhost:"
red = "\033[0;31m"
green = "\033[0;32m"
blue = "\033[0;34m"
nc = "\033[0m"

def cgiRequest(port, uri, expected, expectedBody = False, contentLength = False, query = False):
    if query == False:
        print(red + "GET " + rhost + str(port) + uri + nc)
    else:
        print(red + "GET " + rhost + str(port) + uri + "?", end = "")
        n = 1
        for i in query.keys():
            print(i + "=" + query[i], end = "")
            if n == len(query.keys()):
                print()
            else:
                print("&", end = "")
            n += 1
    print(green + "Expected: " + expected + nc)
    if query == False:
        r = requests.get(rhost + str(port) + uri)
    else:
        r = requests.get(rhost + str(port) + uri, query)
    print(blue + "I received:" + nc)
    print("Status Code: " + str(r.status_code))
    for h in r.headers:
        print(h + ":" + r.headers[h])
    print()
    if contentLength == False:
        print(r.text)
    else:
        print("Body not displayed as it is too long")
    if expectedBody != False and r.text != expectedBody:
        print(red + "FAILURE BODY" + nc)
    if contentLength != False and r.headers["Content-Length"] != contentLength:
        print(red + "FAILURE CONTENT-LENGTH" + nc)


def cgi(port):
    pages = [
            ["/cgi", "Content of index.sh", "Index\n", False, False],
            ["/cgi/", "Content of index.sh", "Index\n", False, False],
            ["/cgi/hello.sh", "Content of hello.sh", "Hello\n", False, False],
            ["/cgi/emptyCGIOutput.sh", "No Freeze, No Crash", "", False, False],
            ["/cgi/helloLong.sh", "Content-Length of 1300000", False, "1300000", False],
            ["/cgi/envVar.sh", "Check body contains all request headers", False, False, False],
            ["/cgi/queryStr.sh", "Content of Query String Var", "name=John&id=10\n", False, 
                {"name": "John", "id": "10"} ]
        ]
    for page in pages:
        cgiRequest(port, page[0], page[1], page[2], page[3], page[4])
        input("Press Enter: ")
