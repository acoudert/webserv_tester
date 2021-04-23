def enter():
    input("Press Enter: ")

def chunk_size0_test(port):
    from . import chunk_size0
    chunk_size0.chunk_size0(port)
    enter()

def chunk_size10_test(port):
    from . import chunk_size10
    chunk_size10.chunk_size10(port)
    enter()

def chunk500_size4000_test(port):
    from . import chunk500_size4000
    chunk500_size4000.chunk500_size4000(port)
    enter()

def chunk500_size4001_test(port):
    from . import chunk500_size4001
    chunk500_size4001.chunk500_size4001(port)
    enter()

def urlencoded_shell_test(port):
    from . import urlencoded_shell
    urlencoded_shell.urlencoded_shell(port)
    enter()

