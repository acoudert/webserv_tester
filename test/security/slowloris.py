import socket
import time

TCP_IP = '127.0.0.1'
BUFFER_SIZE = 1024
red = "\033[0;31m"
green = "\033[0;32m"
blue = "\033[0;34m"
nc = "\033[0m"

def slowloris(port):
    print(red + "Test Slowloris Attack" + nc)
    print(green + "Expected: Broken pipe + CPU not full time at 100%" + nc)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, port))
    toSend = "POST /cgiBis/hello.sh HTTP/1.1\r\nHost: localhost:" + str(port) + "\r\n"
    toSend += "Transfer-Encoding: chunked\r\nContent-Type: application/x-www-form-urlencoded\r\n\r\n"
    print(blue + "I send:\n" + nc)
    print(toSend, end = "")
    print("1000000 x \"1\\r\\na\\r\\n\"")
    print("       1 x \"0\\r\\n\\r\\n\"")
    for i in range(999999):
        toSend += "1\r\na\r\n"
    toSend += "0\r\n\r\n"
    try:
        for i in toSend:
            s.send(bytes(str(i), encoding="utf-8"))
            print(str(i))
            time.sleep(0.1)
    except Exception as e:
        print(repr(e))
    s.close()
