import threading
import socket
import time

rhost = "http://localhost:"
red = "\033[0;31m"
green = "\033[0;32m"
blue = "\033[0;34m"
nc = "\033[0m"
TCP_IP = '127.0.0.1'
BUFFER_SIZE = 1024

def thread_ft(port, toSend):
    allS = []
    for j in range(100):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((TCP_IP, port))
        allS.append(s)
    for i in range(10):
        for j in range(100):
            try:
                allS[j].send(bytes(str(toSend[i]), encoding="utf-8"))
            except:
                continue
        time.sleep(1)

def dos(port):
    toSend = []
    toSend.append("POST /cgiBis/hello.sh HTTP/1.1\r\nHost: localhost:" + str(port) + "\r\n")
    toSend.append("Transfer-Encoding: chunked\r\nContent-Type: application/x-www-form-urlencoded\r\n\r\n")
    print(blue + "I send line by line with 1s delay 8 thr x 100 request:\n" + nc)
    for i in toSend:
        print(i)
    print("7 x \"1\\r\\na\\r\\n\"")
    print("1 x \"0\\r\\n\\r\\n\"")
    toSend += "0\r\n\r\n"
    for i in range(2, 9):
        toSend.append("1\r\na\r\n")
    toSend.append("0\r\n\r\n")
    threads = []
    print(red + "Test Dos Attack" + nc)
    print(blue + "Ensure your server is launched without slowloris protection neither timeout" + nc)
    print(blue + "The purpose of this test is to exceed your nb of fds" + nc)
    print(green + "Expected: No Crash" + nc) 
    input("Press Enter: ")
    for i in range(8):
        thread = threading.Thread(target = thread_ft, args=(port, toSend))
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()
