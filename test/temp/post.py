import requests
import socket
import time

rhost = "http://localhost:1234"
red = "\033[0;31m"
green = "\033[0;32m"
blue = "\033[0;34m"
nc = "\033[0m"
"""
pages = ["/index.html", "/", ""]
for page in pages:
    print(red + "Request: POST " + rhost + page + nc)
    r = requests.post(rhost + page)
    print(red + "Response:" + nc)
    print(blue + "Headers:" + nc)
    for h in r.headers:
        print(green + h + ":" + r.headers[h] + nc)
    print(blue + "\nBody:" + nc)
    print(r.text)

pages = ["/php/hello.php", "/php/envVar.php", "/php/emptyFile.php", "/php/queryStr.php"]
for page in pages:
    print(red + "Request: POST " + rhost + page + nc)
    r = requests.post(rhost + page)
    print(red + "Response:" + nc)
    print(blue + "Headers:" + nc)
    for h in r.headers:
        print(green + h + ":" + r.headers[h] + nc)
    print(blue + "\nBody:" + nc)
    print(r.text)

pages = ["/php/queryStr.php"]
queries = { "/php/queryStr.php": {"name": "John", "id": "10"} }
for page in pages:
    print(red + "Request: POST " + rhost + page + "?", end = "")
    i = 0
    for query in queries[page].keys():
        print(query + "=" + queries[page][query], end = "")
        i += 1
        if i == len(queries[page].keys()):
            print()
        else:
            print("&", end = "")
    r = requests.post(rhost + page, queries[page])
    print(red + "Response:" + nc)
    print(blue + "Headers:" + nc)
    for h in r.headers:
        print(green + h + ":" + r.headers[h] + nc)
    print(blue + "\nBody:" + nc)
    print(r.text)
"""
pages = ["/php/www-urlencoded.php"]
queries = { "/php/www-urlencoded.php": {"name": "John", "id": "10"} }
for page in pages:
    print(red + "Request: POST (application/x-www-urlencoded) " + rhost + page)
    r = requests.post(rhost + page, queries[page])
    print(red + "Response:" + nc)
    print(blue + "Headers:" + nc)
    for h in r.headers:
        print(green + h + ":" + r.headers[h] + nc)
    print(blue + "\nBody:" + nc)
    print(r.text)

print(red + "Request: POST (multipart/form-data) " + rhost + "/php/multipart.php" + nc)
TCP_IP = '127.0.0.1'
TCP_PORT = 1234
BUFFER_SIZE = 1024
sent = b'POST /php/multipart.php HTTP/1.1\r\n\
Host: localhost:1234\r\n\
Content-Length: 246\r\n\
Content-Type: multipart/form-data; boundary=------------------------6f6fe664336cd609\r\n\
\r\n\
--------------------------6f6fe664336cd609\r\n\
Content-Disposition: form-data; name=\"letter\"\r\n\
\r\n\
abcde\r\n\
--------------------------6f6fe664336cd609\r\n\
Content-Disposition: form-data; name=\"number\"\r\n\
\r\n\
01234\r\n\
--------------------------6f6fe664336cd609--\r\n'
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.sendall(sent)
data = s.recv(10000)
string = data.decode("ascii")
print(red + "Response:" + nc)
print(blue + "Headers:" + nc)
print(green + string[:string.find("\n\n") + 1] + nc)
print(blue + "Body:" + nc)
print(string[string.find("\n\n") + 2:])
s.close()

