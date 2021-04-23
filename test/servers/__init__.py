def enter():
    input("Press Enter: ")

def get_index_test(port, port2):
    from . import get_index
    get_index.get_index(port, port2)
    enter()

def not_accepted_method_test(port, port2):
    from . import not_accepted_method
    not_accepted_method.not_accepted_method(port, port2)
    enter()

