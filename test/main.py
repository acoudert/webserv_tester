from sys import argv

import usage
import starting_line
import headers
import get

usage.checkArgv(argv)
usage.fileConf()

port = int(argv[1])
red = "\033[0;31m"
nc = "\033[0m"

def skip(testStr):
    string = red + "TEST "
    string += testStr + ":" + nc
    string += "\n\t1. Enter to proceed\n\t2. Type something + Enter to skip\n"
    s = input(string)
    if s:
        return True
    return False

try:
    if not skip("STARTING LINE"):
        starting_line.higher_version_test(port)
        starting_line.lower_version_test(port)
        starting_line.version_error_test(port)
        starting_line.no_version_test(port)
        starting_line.dir_traversal1_test(port)
        starting_line.dir_traversal2_test(port)
        starting_line.not_a_uri_test(port)
        starting_line.no_uri_test(port)
        starting_line.unknown_method_test(port)
        starting_line.no_method_test(port)
        starting_line.no_starting_line_test(port)
    if not skip("HEADERS"):
        headers.char_by_char_test(port)
        headers.no_host_test(port)
        headers.unknown_test(port)
        headers.malformed_test(port)
        headers.too_long_test(port)
        headers.two_hosts_test(port)
        #headers.timeout_test(port)
    if not skip("GET"):
        get.classic_test(port)
        get.cgi_test(port)
        get.body_test(port)
        get.brute_test(port)

except Exception as e:
    print(repr(e))

