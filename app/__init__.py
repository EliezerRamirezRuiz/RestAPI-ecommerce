from flask import Flask

from typing import Literal

from .config import Config
from .models import db
from .blueprints import address_blueprint


def create_app(
    mode:Literal["development", "production", "default"] = 'development'
    ):
    """In production create as app = create_app('production')
    
    `mode`: must be [default | development | production] 
    """
    app = Flask(__name__)
    config = Config()
    
    app.config.from_object(config.setup_config(mode))
    db.init_app(app)
    
    with app.app_context():
        db.create_all()
    
    app.register_blueprint(address_blueprint)

    return app