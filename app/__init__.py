from flask import Flask

from typing import Literal

from .config import Config
from .models import db
from .blueprints import load_blueprint


def create_app(
    mode:Literal["development", "production", "default"] = 'development'
):
    app = Flask(__name__)
    config = Config()
    
    app.config.from_object(config.setup_config(mode))
    
    with app.app_context():
        db.init_app(app)
        db.create_all()
        load_blueprint(app)
    
    return app