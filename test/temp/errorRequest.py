#!/usr/bin/python3
 
import socket
import time

TCP_IP = '127.0.0.1'
TCP_PORT = 1234
BUFFER_SIZE = 1024
blue = "\033[0;34m"
nc = "\033[0m"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(bytes("GETER / HTTP/1.1\r\n", encoding = "utf-8"))
time.sleep(0.1)

print()
data = s.recv(1000)
print(blue + "I received:\n" + nc)
print(data.decode("ascii"))

s.close()
