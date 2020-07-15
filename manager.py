from wsgiref.simple_server import make_server
from urls import urlpatterns

def application(environ, start_response):
    start_response('200 OK', [('k1','v1'),])
    # print(environ['PATH_INFO'])
    path = environ['PATH_INFO']
    for i in urlpatterns:
        if path == i[0]:
            ret = i[1]()
            break
    else:
        ret = b'404 not found!'
    return [ret]


httpd = make_server('127.0.0.1', 9001, application)
print('Serving HTTP on port 9001...')
httpd.serve_forever()