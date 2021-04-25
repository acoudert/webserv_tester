import os
from sys import argv
from sys import stdin

import usage
import starting_line
import headers
import get
import head
import post
import put
import error_pages
import servers
import security

stdin
usage.checkArgv(argv)
stdin
usage.fileConf()

port = int(argv[1])
port2 = 0
if len(argv) == 3:
    port2 = int(argv[2])
red = "\033[0;31m"
green = "\033[0;32m"
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

print("\nDid you set a timeout?")
print("\t1. Type \"yes\" or \"y\" or \"1\"")
print("\t2. Type \"no\" or \"n\" or \"2\"")
timeout = input()
if timeout == "yes" or timeout == "y" or timeout == "1":
    timeout = True
elif timeout == "no" or timeout == "n" or timeout == "2":
    timeout = False
else:
    os._exit(1)

try:
    if not skip("STARTING LINE"):
        starting_line.higher_version_test(port)
        starting_line.lower_version_test(port)
        starting_line.version_error_test(port)
        starting_line.no_version_test(port)
        starting_line.not_a_uri_test(port)
        starting_line.no_uri_test(port)
        starting_line.unknown_method_test(port)
        starting_line.no_method_test(port)
        starting_line.no_starting_line_test(port)
        starting_line.four_elems_test(port)
    if not skip("HEADERS"):
        headers.no_host_test(port)
        headers.unknown_test(port)
        headers.malformed_test(port)
        headers.no_space_test(port)
        headers.too_long_test(port)
        headers.two_hosts_test(port)
        if timeout:
            headers.timeout_test(port)
        headers.char_by_char_test(port)
    if not skip("GET"):
        get.classic_test(port)
        get.cgi_test(port)
        get.body_test(port)
        if not skip("Gentle Brute Force: This test can take some time"):
            get.brute_test(port)
    if not skip("HEAD"):
        head.classic_test(port)
        head.cgi_test(port)
        head.body_test(port)
        head.not_accepted_method_test(port)
    if not skip("POST"):
        post.post_as_get_test(port)
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
        post.formdata_size500_test(port)
        post.formdata_size501_test(port)
    if not skip("PUT"):
        put.chunk_size0_test(port)
        put.chunk_size10_test(port)
        put.chunk500_size4000_test(port)
        put.chunk500_size4001_test(port)
        put.urlencoded_shell_test(port)
    if not skip("ERROR PAGES"):
        error_pages.custom404_test(port)
        error_pages.default_page_test(port)
    if port2 != 0 and not skip("MULTIPLE SERVERS"):
        servers.get_index_test(port, port2)
        servers.not_accepted_method_test(port, port2)
    if not skip("SECURITY"):
        security.dir_traversal1_test(port)
        security.dir_traversal2_test(port)
        security.dir_traversal3_test(port)
        security.dir_traversal4_test(port)
        security.host_poisoning1_test(port)
        if port2 != 0:
            security.host_poisoning2_test(port, port2)
            security.host_poisoning3_test(port, port2)
        if timeout and not skip("Slowloris Attack: This test can take some time"):
            security.slowloris_test(port)
        if not skip("DOS Attack: This test can take some time"):
            security.dos_test(port)
        security.reverse_shell_upload_test(port)
    print(green + "End of tests, I hope you liked them and thanks !!" + nc)
except Exception as e:
    print(repr(e))

