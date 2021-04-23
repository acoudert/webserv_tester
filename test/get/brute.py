import threading
import requests

rhost = "http://localhost:"
red = "\033[0;31m"
green = "\033[0;32m"
blue = "\033[0;34m"
nc = "\033[0m"

def thread_ft(url, nb_request, status_code):
    for i in range(nb_request):
        r = requests.get(url)
        if r.status_code != status_code:
            print(red + "FAILURE" + nc)

def thread_launcher(url, nb_thread, nb_request, status_code):
    threads = []
    print(red + "GET " + url + nc)
    print("Threads nb: " + str(nb_thread))
    print("Request nb/thr: " + str(nb_request))
    print(green + "Expected: No FAILURE" + nc) 
    for i in range(nb_thread):
        thread = threading.Thread(target = thread_ft, args=(url, nb_request, status_code))
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()

def brute(port):
    args = [
            [rhost + str(port) + "/", 8, 20, 200],
            [rhost + str(port) + "/bla", 8, 20, 404],
            [rhost + str(port) + "/text.txt", 8, 20, 200],
            [rhost + str(port) + "/cgi/hello.sh", 8, 20, 200],
            [rhost + str(port) + "/text.txt", 100, 200, 200],
            [rhost + str(port) + "/cgi/hello.sh", 100, 200, 200],
        ]
    for i in range(len(args)):
        thread_launcher(args[i][0], args[i][1], args[i][2], args[i][3])
        input("Press Enter: ")
