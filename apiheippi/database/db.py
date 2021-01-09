from flask_sqlalchemy import SQLAlchemy
from flask_sqlalchemy.model import BindMetaMixin, Model
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base

# Declaro esta metaclase de SQLAlchemy para poder darle nombres custom
# a los usuarios. Esto es útil para hacer la 'herencia' de los tipos de
# usuario desde el tipo básico. Ref. Doc. SQLAlchemy.
# La herencia en SQLAlchemy no implica una herencia explícita de clase.
# https://flask-sqlalchemy.palletsprojects.com/en/master/customizing/



class NoNameMeta(BindMetaMixin, DeclarativeMeta):
    pass

db = SQLAlchemy(model_class=declarative_base(
        cls=Model, metaclass=NoNameMeta, name='Model'))

def initialize_db(app):

    # El objeto db será una instancia de SQLAlchemy con la metaclase custom.
    db.init_app(app)
