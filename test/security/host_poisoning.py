import socket
import time

TCP_IP = '127.0.0.1'
BUFFER_SIZE = 1024
red = "\033[0;31m"
green = "\033[0;32m"
blue = "\033[0;34m"
nc = "\033[0m"

def host_poisoning1(port):
    print(red + "Test Host Poisoning Attack 1" + nc)
    print(green + "Expected: Error" + nc)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, port))
    toSend = "GET / HTTP/1.1\r\nHost: localhost:"
    if port < 65530:
        toSend += str(port + 1)
    else:
        toSend += str(port - 1)
    toSend += "\r\n\r\n"
    print(blue + "I send:\n" + nc)
    print(toSend, end = "")
    s.send(bytes(str(toSend), encoding="utf-8"))
    data = s.recv(1000)
    print(blue + "I received:\n" + nc)
    print(data.decode("ascii"))
    s.close()

def host_poisoning2(port, port2):
    print(red + "Test Host Poisoning Attack 2" + nc)
    print(green + "Expected: Error (NOT autoindex of /pythonTest)" + nc)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, port))
    toSend = "GET / HTTP/1.1\r\nHost: localhost:" + str(port2) + "\r\n\r\n"
    print(blue + "I send:\n" + nc)
    print(toSend, end = "")
    s.send(bytes(str(toSend), encoding="utf-8"))
    data = s.recv(1000)
    print(blue + "I received:\n" + nc)
    print(data.decode("ascii"))
    s.close()

def host_poisoning3(port, port2):
    print(red + "Test Host Poisoning Attack 3" + nc)
    print(green + "Expected: Error (NOT the file /pythonTest/putStuff/host_poisoned.txt)" + nc)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, port2))
    toSend = "PUT /host_poisoned.txt HTTP/1.1\r\nHost: localhost:" + str(port) + "\r\n"
    toSend += "Transfer-Encoding: chunked\r\nContent-Type: application/x-www-form-urlencoded\r\n\r\n"
    toSend += "1\r\na\r\n"
    toSend += "0\r\n\r\n"
    print(blue + "I send:\n" + nc)
    print(toSend, end = "")
    s.send(bytes(str(toSend), encoding="utf-8"))
    data = s.recv(1000)
    print(blue + "I received:\n" + nc)
    print(data.decode("ascii"))
    s.close()

