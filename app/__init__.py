from flask import Flask

from .blueprints import *
from .typing import ConfigMode
from .config import Config
from .models import db


def create_app(mode: ConfigMode='development'):
    """In production create as app = create_app('production')
    
    `mode`: must be [default | development | production] 
    """
    
    app = Flask(__name__)
    config = Config()
    
    app.config.from_object(config.setup_config(mode))
    db.init_app(app)

    with app.app_context():
        db.create_all()
    
    return app