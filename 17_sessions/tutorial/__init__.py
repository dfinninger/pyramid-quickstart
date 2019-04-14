from pyramid.config import Configurator
from pyramid.session import SignedCookieSessionFactory, JSONSerializer


def main(global_config, **settings):
    my_session_factory = SignedCookieSessionFactory(
        "supersecret", serializer=JSONSerializer(), httponly=True
    )
    config = Configurator(settings=settings, session_factory=my_session_factory)
    config.include("pyramid_chameleon")
    config.add_route("home", "/")
    config.add_route("hello", "/howdy")
    config.scan(".views")
    return config.make_wsgi_app()
