import socket

TCP_IP = '127.0.0.1'
BUFFER_SIZE = 1024
red = "\033[0;31m"
green = "\033[0;32m"
blue = "\033[0;34m"
nc = "\033[0m"

def formdata_size0(port):
    print(red + "Test Formdata Size 0" + nc)
    print(green + "Expected: Content-Length = 44" + nc)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, port))
    toSend = "POST /cgi/displayChunk.sh HTTP/1.1\r\nHost: localhost:" + str(port) + "\r\n"
    toSend += "Content-Type: multipart/form-data; boundary=------------------------fbaa703755ea1416\r\n"
    toSend += "Content-Length: 139\r\n\r\n"
    toSend += "--------------------------fbaa703755ea1416\r\n"
    toSend += "Content-Disposition: form-data; name=\"name\"\r\n\r\n\r\n"
    toSend += "--------------------------fbaa703755ea1416--\r\n"
    print(blue + "I send:\n" + nc)
    print(toSend)
    s.send(bytes(toSend, encoding="utf-8"))
    data = s.recv(1000)
    print(blue + "I received:\n" + nc)
    print(data.decode("ascii"))
    s.close()
