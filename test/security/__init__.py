def enter():
    input("Press Enter: ")

def dir_traversal1_test(port):
    from . import dir_traversal
    dir_traversal.dir_traversal1(port)
    enter()

def dir_traversal2_test(port):
    from . import dir_traversal
    dir_traversal.dir_traversal2(port)
    enter()

def dir_traversal3_test(port):
    from . import dir_traversal
    dir_traversal.dir_traversal3(port)
    enter()

def dir_traversal4_test(port):
    from . import dir_traversal
    dir_traversal.dir_traversal4(port)
    enter()

def slowloris_test(port):
    from . import slowloris
    slowloris.slowloris(port)
    enter()

def dos_test(port):
    from . import dos
    dos.dos(port)
    enter()

def host_poisoning1_test(port):
    from . import host_poisoning
    host_poisoning.host_poisoning1(port)
    enter()

def host_poisoning2_test(port, port2):
    from . import host_poisoning
    host_poisoning.host_poisoning2(port, port2)
    enter()

def host_poisoning3_test(port, port2):
    from . import host_poisoning
    host_poisoning.host_poisoning3(port, port2)
    enter()

def reverse_shell_upload_test(port):
    from . import reverse_shell_upload
    reverse_shell_upload.reverse_shell_upload(port)

