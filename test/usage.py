import os

def checkArgv(argv):
    try:
        if (len(argv) != 2) or (int(argv[1]) <= 0 or int(argv[1]) >= 65536):
            print("Usage: python3 main.py [port_nb]")
            print("Example: python3 main.py 1234")
            os._exit(1)
    except:
        print("Usage: python3 main.py [port_nb]")
        print("Example: python3 main.py 1234")
        os._exit(1)

def fileConf():
    print("Ensure your server configuration file contains: ")
    print("\t1. A root linked to /pythonTest")
    print("\t2. /pythonTest/noperm.html has 400 as perms")
    
    print("\t3. A location / pointing to /pythonTest:")
    print("\t\t- Accepted Methods: GET HEAD")
    print("\t\t- Autoindex: on")
    
    print("\t4. A location /ipointtodir pointing to /pythonTest/dir:")
    print("\t\t- Accepted Methods: GET")
    print("\t\t- Autoindex: on")
    
    print("\t5. A location /cgi pointing to /pythonTest/sh :")
    print("\t\t- Accepted Methods: GET HEAD POST")
    print("\t\t- Autoindex: off")
    print("\t\t- index: index.sh")
    print("\t\t- cgi: /bin/sh for all *.sh")
    print("\t\t- max body size: 500")
    input("Press Enter: ")
