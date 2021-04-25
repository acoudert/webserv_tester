import os
import sys

def displayUsage():
    print("Usage: python3 main.py [port_nb]")
    print("Example: python3 main.py 1234")
    print ("OR")
    print("Usage: python3 main.py [port_nb_server1] [port_nb_server2]")
    print("Example: python3 main.py 1234 10000")

def checkArgv(argv):
    try:
        if len(argv) < 2 or len(argv) > 3:
            displayUsage()
            os._exit(1)
        if int(argv[1]) <= 0 or int(argv[1]) >= 65536:
            displayUsage()
            os._exit(1)
        if len(argv) == 3 and ((int(argv[2]) <= 0 or int(argv[2]) >= 65536)
                or int(argv[1]) == int(argv[2])):
            displayUsage()
            os._exit(1)
    except:
        os._exit(1)

def fileConf():
    print("Ensure your server configuration file contains: ")
    print("\t- A first server with:")
    print("\t\t1. A root linked to /pythonTest")
    print("\t\t2. /pythonTest/noperm.html has 400 as perms")
    print("\t\t3. Error 404 points to /pythonTest/error/404.txt")
    
    print("\t\t4. A location / pointing to /pythonTest:")
    print("\t\t\t- Accepted Methods: GET HEAD PUT")
    print("\t\t\t- Autoindex: on")
    print("\t\t\t- max body size: 2000000")
    print("\t\t\t- put save dir: /pythonTest/putStuff")
    
    print("\t\t5. A location /ipointtodir pointing to /pythonTest/dir:")
    print("\t\t\t- Accepted Methods: GET")
    print("\t\t\t- Autoindex: on")
    
    print("\t\t6. A location /cgi pointing to /pythonTest/sh :")
    print("\t\t\t- Accepted Methods: GET HEAD POST")
    print("\t\t\t- Autoindex: off")
    print("\t\t\t- index: index.sh")
    print("\t\t\t- cgi: /bin/sh for all *.sh")
    print("\t\t\t- max body size: 500")
    
    print("\t\t7. A location /cgiBis pointing to /pythonTest/sh :")
    print("\t\t\t- Accepted Methods: POST")
    print("\t\t\t- cgi: /bin/sh for all *.sh")
    print("\t\t\t- max body size: 1000000")
    
    print("\t\t8. A location /putStuff pointing to /pythonTest/putStuff:")
    print("\t\t\t- Accepted Methods: GET")
    print("\t\t\t- Autoindex: off")
    print("\t\t\t- cgi: /bin/sh for all *.sh")
    
    print("\t- A second server (not mandatory) with:")
    print("\t\t1. A root linked to /pythonTest")
    
    print("\t\t2. A location / pointing to /pythonTest:")
    print("\t\t\t- Accepted Methods: GET")
    print("\t\t\t- Autoindex: off")
    print("\t\t\t- index: index.html")
    
    input("Press enter: ")
