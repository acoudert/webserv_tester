import socket
import os

TCP_IP = '127.0.0.1'
BUFFER_SIZE = 1024
red = "\033[0;31m"
green = "\033[0;32m"
blue = "\033[0;34m"
nc = "\033[0m"

def urlencoded_shell(port):
    print(red + "Test Urlencoded Shell" + nc)
    print(green + "Expected: sh in pythonTest/putStuff" + nc)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, port))
    toSend = "PUT /sh HTTP/1.1\r\nHost: localhost:" + str(port) + "\r\n"
    toSend += "Content-Type: application/x-www-form-urlencoded\r\n"
    toSend += "Content-Length: "
    toSend += str(os.stat("/bin/sh").st_size) + "\r\n\r\n"
    s.send(bytes(toSend, encoding="utf-8"))
    f = open("/bin/sh", 'rb')
    byte = f.read()
    print(blue + "I send:\n" + nc)
    s.sendall(byte)
    data = s.recv(1000)
    print(blue + "I received:\n" + nc)
    print(data.decode("ascii"))
    print(green + "Check there is the file sh in /pythonTest/putStuff" + nc)
    print(green + "Execute this file, if you are not in sh terminal, the test failed" + nc)
    s.close()

