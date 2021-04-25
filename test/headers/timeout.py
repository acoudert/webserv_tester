import socket

TCP_IP = '127.0.0.1'
BUFFER_SIZE = 1024
red = "\033[0;31m"
green = "\033[0;32m"
blue = "\033[0;34m"
nc = "\033[0m"

def timeout(port):
    print(red + "Test Timeout" + nc)
    print(green + "Expected: Closed Connection | no CPU full time 100%" + nc)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, port))
    toSend = "GET / HTTP/1.1\r\nHost: localhost: " + str(port) + "\r\n"
    print(blue + "I send:\n" + nc)
    print(toSend)
    try:
        s.send(bytes(toSend, encoding="utf-8"))
        data = s.recv(1000)
        s.close()
    except Exception as e:
        print(repr(e))
