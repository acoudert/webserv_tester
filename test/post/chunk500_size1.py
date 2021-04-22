import socket

TCP_IP = '127.0.0.1'
BUFFER_SIZE = 1024
red = "\033[0;31m"
green = "\033[0;32m"
blue = "\033[0;34m"
nc = "\033[0m"

def chunk500_size1(port):
    print(red + "Test 500 Chunks Size 1" + nc)
    print(green + "Expected: Content must be \"a\" x 499 + \"\\n\" & Content-Length = 500" + nc)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, port))
    toSend = "POST /cgi/displayChunk.sh HTTP/1.1\r\nHost: localhost:" + str(port) + "\r\n"
    toSend += "Transfer-Encoding: chunked\r\nContent-Type: application/x-www-form-urlencoded\r\n\r\n"
    print(blue + "I send:\n" + nc)
    print(toSend, end = "")
    print("499 x \"1\\r\\na\\r\\n\"")
    print(" 1 x \"1\\r\\n\\n\\r\\n\"")
    print("0\\r\\n\\r\\n")
    for i in range(499):
        toSend += "1\r\na\r\n"
    toSend += "1\r\n\n\r\n"
    toSend += "0\r\n\r\n"
    s.send(bytes(toSend, encoding="utf-8"))
    data = s.recv(1000)
    print(blue + "I received:\n" + nc)
    print(data.decode("ascii"))
    s.close()
