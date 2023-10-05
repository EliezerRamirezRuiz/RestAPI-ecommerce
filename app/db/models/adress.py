from typing import List

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import (mapped_column, relationship)
from sqlalchemy import (Integer, String, ForeignKey)

from .city import City

from db import db


class Adress(db.Model):
    __tablename__ = "adress"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    adress_name: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    number: Mapped[int] = mapped_column(Integer, nullable=False)
    city_id: Mapped[int] = mapped_column(ForeignKey("city.id"))
    city: Mapped[List["City"]] = relationship(back_populates="city")