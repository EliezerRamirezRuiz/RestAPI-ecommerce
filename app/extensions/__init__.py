from flask_jwt_extended import JWTManager

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


jwt = JWTManager()
db = SQLAlchemy(model_class=Base)        
