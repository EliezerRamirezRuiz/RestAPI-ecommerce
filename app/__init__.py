from flask import Flask

from typing import Literal

from .extensions import jwt, db
from .config import Config
from .blueprints import load_blueprint


Mode = Literal["development", "production", "default"]


def create_app(mode: Mode = 'development'):
    app = Flask(__name__)
    config = Config()
    
    app.config.from_object(config.setup_config(mode))    
    jwt.init_app(app)
    db.init_app(app)

    with app.app_context():
        db.create_all()
        load_blueprint(app)
    
    return app
