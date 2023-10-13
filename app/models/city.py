from sqlalchemy_serializer import SerializerMixin

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import Integer, String

from .database import db


class CityModel(db.Model, SerializerMixin):
    __tablename__ = "cities"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    