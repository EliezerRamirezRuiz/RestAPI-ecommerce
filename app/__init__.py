import quart_flask_patch

from types.typing import ConfigMode
from config.config import setup_config

from db import db
from quart import Quart  


def create_app(mode: ConfigMode = 'development'):
    """In production create as app = create_app('Production')"""
    app = Quart(__name__)
    
    app.config.from_object(setup_config(mode))
    db.init_app(app)
    
    with app.app_context():
        db.create_all()
    
    return app