from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api
from flask_sqlalchemy.model import BindMetaMixin, Model
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base

# Declaro esta metaclase de SqlAlchemy para poder darle nombres custom
# a los usuarios. Esto es útil para hacer la 'herencia' de los tipos de
# usuario desde el tipo básico. Ref. Doc. SqlAlchemy.
# La herencia en sqlAlchemy no implica una herencia explícita de clase.
# https://flask-sqlalchemy.palletsprojects.com/en/master/customizing/


class NoNameMeta(BindMetaMixin, DeclarativeMeta):
    pass


db = SQLAlchemy(model_class=declarative_base(
    cls=Model, metaclass=NoNameMeta, name='Model'))


def create_app():
    app = Flask(__name__)
    app.config.update(
        DEBUG=True,
        SECRET_KEY='lorem*****',  #Esto hay que cambiarlo urgente. 
        SQLALCHEMY_DATABASE_URI="sqlite:///test.sqlite",
        SQLALCHEMY_TRACK_MODIFICATIONS=False
    )

    db.init_app(app)

    return app
