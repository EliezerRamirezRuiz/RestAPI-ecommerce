from .types import ConfigMode
from .config import Config

from .db import db

from quart import Quart


def create_app(mode: ConfigMode = 'development') -> Quart:
    """In production create as app = create_app('Production')"""
    app = Quart(__name__)
    config = Config()
    
    app.config.from_object(config.setup_config(mode))
    db.init_app(app)

    with app.app_context():
        db.create_all()
    
    return app
