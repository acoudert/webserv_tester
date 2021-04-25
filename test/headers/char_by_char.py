import socket
import time

TCP_IP = '127.0.0.1'
BUFFER_SIZE = 1024
red = "\033[0;31m"
green = "\033[0;32m"
blue = "\033[0;34m"
nc = "\033[0m"

def char_by_char(port):
    print(red + "Test Char By Char" + nc)
    print(blue + "Ensure your server is launched without slowloris protection" + nc)
    print(green + "Expected: No Error" + nc)
    input("Press Enter: ")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, port))
    sent = ""
    print(blue + "I send:\n" + nc)
    for i in "GET / HTTP/1.1\r\nHost: localhost:" + str(port) + "\r\n\r\n":
        s.send(bytes(str(i), encoding="utf-8"))
        sent += i
        print(sent)
        time.sleep(0.1)
    print()
    data = s.recv(1000)
    print(blue + "I received:\n" + nc)
    print(data.decode("ascii"))
    s.close()
