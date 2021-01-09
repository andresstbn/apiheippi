from flask import Flask
from flask_restful import Resource, Api

from .resources.routes import initialize_routes
from .database.db import initialize_db


def create_app():
    app = Flask(__name__)

    #Strings para conexión con la base de datos. Por ahora pruebas en SQLite
    stringpostgresql = "postgresql+psycopg2://heippidbuser:abc123@localhost:5432/heippidb"
    stringsqlite = "sqlite:///test.sqlite"

    app.config.update(
        DEBUG=True,
        SECRET_KEY='lorem*****',  #Esto hay que cambiarlo urgente. 
        SQLALCHEMY_DATABASE_URI=stringsqlite,
        SQLALCHEMY_TRACK_MODIFICATIONS=False
    )

    api = Api(app)
    initialize_db(app)
    initialize_routes(api)
    return app

if __name__ == '__main__':
    create_app().run(debug=True)