def enter():
    input("Press Enter: ")

def classic_test(port):
    from . import classic
    classic.classic(port)

def cgi_test(port):
    from . import cgi
    cgi.cgi(port)

def body_test(port):
    from . import body
    body.body(port)

def not_accepted_method_test(port):
    from . import not_accepted_method
    not_accepted_method.not_accepted_method(port)

