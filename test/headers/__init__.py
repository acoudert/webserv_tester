def enter():
    input("Press Enter: ")

def no_host_test(port):
    from . import no_host
    no_host.no_host(port)
    enter()

def unknown_test(port):
    from . import unknown
    unknown.unknown(port)
    enter()

def malformed_test(port):
    from . import malformed
    malformed.malformed(port)
    enter()

def no_space_test(port):
    from . import no_space
    no_space.no_space(port)
    enter()

def too_long_test(port):
    from . import too_long
    too_long.too_long(port)
    enter()

def two_hosts_test(port):
    from . import two_hosts
    two_hosts.two_hosts(port)
    enter()

def timeout_test(port):
    from . import timeout
    timeout.timeout(port)
    enter()

def char_by_char_test(port):
    from . import char_by_char
    char_by_char.char_by_char(port)
    enter()

