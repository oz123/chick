"""
Example application with Chick
"""

from chick import Chick

chick = Chick()


@chick.get("/")
def index(environ):
    return [b"Hello World!\n"]


@chick.post("/input/")
def test_post(environ):
    r = ''.join(('{} {}\n'. format(k, v) for
                k, v in environ.items())).encode()
    return [r]


if __name__ == "__main__":
    from wsgiref.simple_server import make_server
    httpd = make_server('', 8000, chick)
    print("Serving on port 8000...")

    # Serve until process is killed
    httpd.serve_forever()
