import bottle

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from demo.models import Artist
from restful_jsonapi.web.bottle import BottleApi


engine = create_engine('sqlite:///chinook.db', echo=True)
create_session = sessionmaker(bind=engine)
session = create_session()

app = bottle.Bottle()

api_manager = BottleApi(session, app=app)
api_manager.create_api(Artist, collection_name="artists")


if __name__ == '__main__':
    app.run(debug=True, reloader=True)
