from waitress import serve
from pyramid.config import Configurator
from pyramid.response import Response

def hello_world(request):
    print ('Incoming request')
    return Response('<body><h1>hello world</h1></body>')

if __name__ == "__main__":
    with Configurator() as config:
        config.add_route('hello', '/')
        config.add_view(hello_world, route_name='hello')
        app = config.make_wsgi_app()
    serve(app, host='127.0.0.1', port=6543)