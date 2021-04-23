import socket

TCP_IP = '127.0.0.1'
BUFFER_SIZE = 1024
red = "\033[0;31m"
green = "\033[0;32m"
blue = "\033[0;34m"
nc = "\033[0m"

def chunk_size10(port):
    print(red + "Test Chunk Size 10" + nc)
    print(green + "Expected: /pythonTest/putStuff/chunk10 having a size of 10" + nc)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, port))
    toSend = "PUT /chunk10.txt HTTP/1.1\r\nHost: localhost:" + str(port) + "\r\n"
    toSend += "Transfer-Encoding: chunked\r\nContent-Type: application/x-www-form-urlencoded\r\n\r\n"
    toSend += "a\r\nJohn=Hola\n\r\n0\r\n\r\n"
    print(blue + "I send:\n" + nc)
    print(toSend)
    s.send(bytes(toSend, encoding="utf-8"))
    data = s.recv(1000)
    print(blue + "I received:\n" + nc)
    print(data.decode("ascii"))
    print(green + "Check there is the file chunk10.txt in /pythonTest/putStuff (file size = 10)" + nc)
    s.close()
