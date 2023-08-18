from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import UUID

all = ('db', 'init_db')

db = SQLAlchemy()

def init_db(app=None, db=None):
    if isinstance(app, Flask) and isinstance(db, SQLAlchemy):
         db.init_app(app)
    else:
        raise ValueError("Cannot init DB wihtout db and app objects")
    

    ##########Not sure what all this does.