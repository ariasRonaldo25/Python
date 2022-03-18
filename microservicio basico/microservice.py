
import json
from wsgiref.simple_server import make_server

def application(environt, start_response):

    headers=[('content-type', 'application/json')]

    start_response('200 OK', headers)

    response={

       'mensaje':  'Hola mundo desde el servidor!'
    }

    return [bytes(json.dumps(response), 'utf-8')]

servidor=make_server('localhost', 8000, application)

servidor.handle_request()