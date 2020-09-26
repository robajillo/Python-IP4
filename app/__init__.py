from flask import Flask
from flask_bs4 import Bootstrap
from flask_sqlalchemy import SQLAlchemy

bootstrap = Bootstrap()
db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)



    # Initializing flask extensions
    bootstrap.init_app(app)
    db.init_app(app)

    return app