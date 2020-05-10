from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from demo.models import Artist
from restful_jsonapi.web.flask import FlaskApi


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///chinook.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

db = SQLAlchemy()
db.init_app(app)


api_manager = FlaskApi(db.session, app=app)
api_manager.create_api(Artist, collection_name="artists")


if __name__ == '__main__':
    app.run(debug=True)
