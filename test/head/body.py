import socket

TCP_IP = '127.0.0.1'
BUFFER_SIZE = 1024
red = "\033[0;31m"
green = "\033[0;32m"
blue = "\033[0;34m"
nc = "\033[0m"

def body(port):
    print(red + "Test HEAD with Body x 2" + nc)
    print(green + "Expected: index.html ONLY x 2" + nc)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, port))
    toSend = "HEAD /index.html HTTP/1.1\r\nHost: localhost:" + str(port) + "\r\n"
    toSend += "Transfer-Encoding: chunked\r\n"
    toSend += "Content-Type: application/x-www-form-urlencoded\r\n\r\n"
    toSend += "a\r\nhello=test\r\n0\r\n\r\n"
    print(blue + "I send:\n" + nc)
    print(toSend)
    s.send(bytes(toSend, encoding="utf-8"))
    data = s.recv(1000)
    print(blue + "I received:\n" + nc)
    print(data.decode("ascii"))
    s.send(bytes(toSend, encoding="utf-8"))
    data = s.recv(1000)
    print(blue + "I received:\n" + nc)
    print(data.decode("ascii"))
    s.close()
