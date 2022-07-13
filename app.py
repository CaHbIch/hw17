from flask import Flask
from flask_restx import Api

from config import Config
from setup_db import db
from views.views import movies_ns, director_ns, genre_ns


def create_app(config_object):
    """  Функция создания основного объекта app """
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    return app


def register_extensions(app):
    """ Функция подключения расширений (Flask-SQLAlchemy, Flask-RESTx) """
    db.init_app(app)
    api = Api(app)
    api.add_namespace(movies_ns)
    api.add_namespace(director_ns)
    api.add_namespace(genre_ns)
    create_data(app, db)


def create_data(app, db):
    with app.app_context():
        db.create_all()


app = create_app(Config())
app.debug = True

if __name__ == '__main__':
    app.run(debug=True)
