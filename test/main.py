import os
from sys import argv

import usage
import starting_line
import headers
import get
import head
import post

usage.checkArgv(argv)
usage.fileConf()

port = int(argv[1])
red = "\033[0;31m"
nc = "\033[0m"

def skip(testStr):
    string = "------\n"
    string += red + "TEST "
    string += testStr + ":" + nc
    string += "\n\t1. Enter to proceed\n\t2. Type something + Enter to skip"
    print(string)
    if (input()):
        return True
    return False
"""
timeout = input("Did you set a timeout?\n\t1. Type \"yes\"\n\t2. Type \"no\"\n")
if timeout == "yes":
    timeout = True
elif timeout == "no":
    timeout = False
else:
    os._exit(1)
"""
timeout = False
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
        headers.no_space_test(port)
        headers.too_long_test(port)
        headers.two_hosts_test(port)
        if timeout:
            headers.timeout_test(port)
    if not skip("GET"):
        get.classic_test(port)
        get.cgi_test(port)
        get.body_test(port)
        get.brute_test(port)
    if not skip("HEAD"):
        head.classic_test(port)
        head.cgi_test(port)
        head.body_test(port)
        head.not_accepted_method_test(port)
    if not skip("POST"):
        post.chunk_size0_test(port)
        post.chunk_size10_test(port)
        post.chunk500_size1_test(port)
        post.chunk_size501_test(port)
        post.chunk501_size1_test(port)
        if timeout:
            post.chunk_timeout_test(port)
        post.urlencoded_size0_test(port)
        post.urlencoded_size10_test(port)
        post.urlencoded_size500_test(port)
        post.urlencoded_size501_test(port)
        post.formdata_size0_test(port)

except Exception as e:
    print(repr(e))

