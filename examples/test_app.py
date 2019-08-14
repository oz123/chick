import sys
from webtest import TestApp

sys.path.insert(0, "..")

from app import chick  # noqa

app = TestApp(chick)

resp = app.get('/')

assert resp.status == '200 OK'
resp = app.get('/no-such-url', expect_errors=True)

assert resp.status == '404 Not Found'
