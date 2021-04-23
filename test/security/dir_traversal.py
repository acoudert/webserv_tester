import socket

TCP_IP = '127.0.0.1'
BUFFER_SIZE = 1024
red = "\033[0;31m"
green = "\033[0;32m"
blue = "\033[0;34m"
nc = "\033[0m"

def dir_traversal1(port):
    print(red + "Test Dir Traversal Attack 1" + nc)
    print(green + "Expected: Error OR Root" + nc)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, port))
    toSend = "GET ../../../ HTTP/1.1\r\nHost: localhost:" + str(port) + "\r\n\r\n"
    print(blue + "I send:\n" + nc)
    print(toSend)
    s.send(bytes(toSend, encoding="utf-8"))
    data = s.recv(1000)
    print(blue + "I received:\n" + nc)
    print(data.decode("ascii"))
    s.close()

def dir_traversal2(port):
    print(red + "Test Dir Traversal Attack 2" + nc)
    print(green + "Expected: Error OR Root" + nc)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, port))
    toSend = "GET /../../../ HTTP/1.1\r\nHost: localhost:" + str(port) + "\r\n\r\n"
    print(blue + "I send:\n" + nc)
    print(toSend)
    s.send(bytes(toSend, encoding="utf-8"))
    data = s.recv(1000)
    print(blue + "I received:\n" + nc)
    print(data.decode("ascii"))
    s.close()

def dir_traversal3(port):
    print(red + "Test Dir Traversal Attack 3" + nc)
    print(green + "Expected: Error OR Root" + nc)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, port))
    toSend = "GET ./../../ HTTP/1.1\r\nHost: localhost:" + str(port) + "\r\n\r\n"
    print(blue + "I send:\n" + nc)
    print(toSend)
    s.send(bytes(toSend, encoding="utf-8"))
    data = s.recv(1000)
    print(blue + "I received:\n" + nc)
    print(data.decode("ascii"))
    s.close()

def dir_traversal4(port):
    print(red + "Test Dir Traversal Attack 4" + nc)
    print(green + "Expected: Error OR Root" + nc)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, port))
    toSend = "GET /ipointtodir/../../../../../../../../../../../home HTTP/1.1\r\nHost: localhost:" + str(port) + "\r\n\r\n"
    print(blue + "I send:\n" + nc)
    print(toSend)
    s.send(bytes(toSend, encoding="utf-8"))
    data = s.recv(1000)
    print(blue + "I received:\n" + nc)
    print(data.decode("ascii"))
    s.close()
