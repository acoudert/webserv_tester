import socket

TCP_IP = '127.0.0.1'
BUFFER_SIZE = 1024
red = "\033[0;31m"
green = "\033[0;32m"
blue = "\033[0;34m"
nc = "\033[0m"

def chunk500_size4000(port):
    print(red + "Test 500 Chunks Size 4000" + nc)
    print(green + "Expected: /pythonTest/putStuff/chunk2000000 having a size of 2000000" + nc)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, port))
    toSend = "PUT /chunk2000000 HTTP/1.1\r\nHost: localhost:" + str(port) + "\r\n"
    toSend += "Transfer-Encoding: chunked\r\nContent-Type: application/x-www-form-urlencoded\r\n\r\n"
    print(blue + "I send:\n" + nc)
    print(toSend, end = "")
    print("500 x \"fa0\\r\\na[...]a x 4000\\r\\n\"")
    print("0\\r\\n\\r\\n")
    s.send(bytes(toSend, encoding="utf-8"))
    for i in range(500):
        toSend = "fa0\r\n"
        for j in range(4000):
            toSend += "a"
        toSend += "\r\n"
        s.send(bytes(toSend, encoding="utf-8"))
    toSend = "0\r\n\r\n"
    s.send(bytes(toSend, encoding="utf-8"))
    data = s.recv(1000)
    print(blue + "I received:\n" + nc)
    print(data.decode("ascii"))
    print(green + "Check there is the file chunk2000000 in /pythonTest/putStuff (file size = 2000000)" + nc)
    s.close()
