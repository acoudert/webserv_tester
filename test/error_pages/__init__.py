def enter():
    input("Press Enter: ")

def custom404_test(port):
    from . import custom404
    custom404.custom404(port)
    enter()

def default_page_test(port):
    from . import default_page
    default_page.default_page(port)
    enter()

