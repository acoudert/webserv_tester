def enter():
    input("Press Enter: ")

def higher_version_test(port):
    from . import higher_version
    higher_version.higher_version(port)
    enter()

def lower_version_test(port):
    from . import lower_version
    lower_version.lower_version(port)
    enter()

def version_error_test(port):
    from . import version_error
    version_error.version_error(port)
    enter()

def no_version_test(port):
    from . import no_version
    no_version.no_version(port)
    enter()

def dir_traversal1_test(port):
    from . import dir_traversal
    dir_traversal.dir_traversal1(port)
    enter()

def dir_traversal2_test(port):
    from . import dir_traversal
    dir_traversal.dir_traversal2(port)
    enter()

def not_a_uri_test(port):
    from . import not_a_uri
    not_a_uri.not_a_uri(port)
    enter()

def no_uri_test(port):
    from . import no_uri
    no_uri.no_uri(port)
    enter()

def unknown_method_test(port):
    from . import unknown_method
    unknown_method.unknown_method(port)
    enter()

def no_method_test(port):
    from . import no_method
    no_method.no_method(port)
    enter()

def no_starting_line_test(port):
    from . import no_starting_line
    no_starting_line.no_starting_line(port)
    enter()

