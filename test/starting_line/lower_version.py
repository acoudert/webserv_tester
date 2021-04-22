import socket

TCP_IP = '127.0.0.1'
BUFFER_SIZE = 1024
red = "\033[0;31m"
green = "\033[0;32m"
blue = "\033[0;34m"
nc = "\033[0m"

def lower_version(port):
    print(red + "Test Lower Version" + nc)
    print(green + "Expected: Error" + nc)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, port))
    toSend = "GET / HTTP/0.9\r\nHost: localhost:" + str(port) + "\r\n\r\n"
    print(blue + "I send:\n" + nc)
    print(toSend)
    s.send(bytes(toSend, encoding="utf-8"))
    data = s.recv(1000)
    print(blue + "I received:\n" + nc)
    print(data.decode("ascii"))
    s.close()
