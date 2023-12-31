from dataclasses import dataclass

from sqlalchemy_serializer import SerializerMixin

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import Integer, String, ForeignKey

from ..extensions import db


@dataclass
class StateModel(db.Model, SerializerMixin):
    __tablename__ = "states"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    
    country_id: Mapped[int] = mapped_column(ForeignKey("countries.id"))