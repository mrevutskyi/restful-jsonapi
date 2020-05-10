from wsgiref.simple_server import make_server

from pyramid.config import Configurator
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from demo.models import Artist
from restful_jsonapi.web.pyramid import PyramidAPI


engine = create_engine('sqlite:///chinook.db', echo=True)
create_session = sessionmaker(bind=engine)
session = create_session()


if __name__ == '__main__':
    with Configurator() as config:
        api_manager = PyramidAPI(session, config=config)
        api_manager.create_api(Artist, collection_name="artists")

        app = config.make_wsgi_app()
    server = make_server('127.0.0.1', 8000, app)
    server.serve_forever()
