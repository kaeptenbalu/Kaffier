# third-party imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bower import Bower

# local imports
from config import app_config

# db variable initialization
db = SQLAlchemy()
migrate = Migrate()
bower = Bower()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])
    db.init_app(app)
    migrate.init_app(app, db)
    bower.init_app(app)
    from app import models
    from .home import home as home_blueprint
    app.register_blueprint(home_blueprint)

    return app
