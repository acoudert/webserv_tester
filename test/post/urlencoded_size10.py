import socket

TCP_IP = '127.0.0.1'
BUFFER_SIZE = 1024
red = "\033[0;31m"
green = "\033[0;32m"
blue = "\033[0;34m"
nc = "\033[0m"

def urlencoded_size10(port):
    print(red + "Test Urlencoded Size 10" + nc)
    print(green + "Expected: Content must be \"John=Hola\\n\" & Content-Length = 10" + nc)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, port))
    toSend = "POST /cgi/displayChunk.sh HTTP/1.1\r\nHost: localhost:" + str(port) + "\r\n"
    toSend += "Content-Type: application/x-www-form-urlencoded\r\n"
    toSend += "Content-Length: 10\r\n\r\n"
    toSend += "John=Hola\n"
    print(blue + "I send:\n" + nc)
    print(toSend)
    s.send(bytes(toSend, encoding="utf-8"))
    data = s.recv(1000)
    print(blue + "I received:\n" + nc)
    print(data.decode("ascii"))
    s.close()
