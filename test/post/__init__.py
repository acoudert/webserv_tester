def enter():
    input("Press Enter: ")

def post_as_get_test(port):
    from . import post_as_get
    post_as_get.post_as_get(port)
    enter()

def chunk_size0_test(port):
    from . import chunk_size0
    chunk_size0.chunk_size0(port)
    enter()

def chunk_size10_test(port):
    from . import chunk_size10
    chunk_size10.chunk_size10(port)
    enter()

def chunk500_size1_test(port):
    from . import chunk500_size1
    chunk500_size1.chunk500_size1(port)
    enter()

def chunk_size501_test(port):
    from . import chunk_size501
    chunk_size501.chunk_size501(port)
    enter()

def chunk501_size1_test(port):
    from . import chunk501_size1
    chunk501_size1.chunk501_size1(port)
    enter()

def chunk_timeout_test(port):
    from . import chunk_timeout
    chunk_timeout.chunk_timeout(port)
    enter()

def urlencoded_size0_test(port):
    from . import urlencoded_size0
    urlencoded_size0.urlencoded_size0(port)
    enter()

def urlencoded_size10_test(port):
    from . import urlencoded_size10
    urlencoded_size10.urlencoded_size10(port)
    enter()

def urlencoded_size500_test(port):
    from . import urlencoded_size500
    urlencoded_size500.urlencoded_size500(port)
    enter()

def urlencoded_size501_test(port):
    from . import urlencoded_size501
    urlencoded_size501.urlencoded_size501(port)
    enter()

def formdata_size0_test(port):
    from . import formdata_size0
    formdata_size0.formdata_size0(port)
    enter()

def formdata_size500_test(port):
    from . import formdata_size500
    formdata_size500.formdata_size500(port)
    enter()

def formdata_size501_test(port):
    from . import formdata_size501
    formdata_size501.formdata_size501(port)
    enter()

