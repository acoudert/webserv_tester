import requests
import threading
import os

rhost = "http://localhost:1234"
red = "\033[0;31m"
green = "\033[0;32m"
blue = "\033[0;34m"
nc = "\033[0m"

def thread_ft(target, code, body = False, queryStr = False):
    for i in range(5000):
        if queryStr == False:
            r = requests.get(rhost + target)
        else:
            r = requests.get(rhost + target, queryStr)
        if r.status_code != code:
            print(red + "Error Status Code" + nc)
            os._exit(1)
        if body == False:
            if len(r.text) != int(r.headers['Content-Length']):
                print(red + "Error Body" + nc)
                os._exit(1)
            else:
                continue
        if r.text != body:
            print(red + "Error Body" + nc)
            os._exit(1)

def thread_launcher(target, code, n, body = False, queryStr = False):
    threads = []
    print(blue + "GET: " + target + nc)
    print("Test " + str(n) + " threads:")
    for i in range(n):
        thread = threading.Thread(target=thread_ft, args=(target, code, body, queryStr))
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()
    print(green + "Job succeeded !\n" + nc)

thread_launcher("/", 200, 5)
thread_launcher("/", 200, 20)
#thread_launcher("/directory/nop", 200, 128)
"""
thread_launcher("/text.txt", 200, 8, "I contain text.\n")
thread_launcher("/idonotexist.txt", 404, 8)
thread_launcher("/hello.sh", 200, 5)
thread_launcher("/php/queryStr.php", 200, 5, False, {"name": "John", "id": "10"})
"""
