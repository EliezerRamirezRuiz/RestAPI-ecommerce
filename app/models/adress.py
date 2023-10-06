from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import (mapped_column, relationship)
from sqlalchemy import (Integer, String)

from db import db

if TYPE_CHECKING:
    from .order import Order


class Adress(db.Model):
    __tablename__ = "adress"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    number: Mapped[int] = mapped_column(Integer, nullable=False)
    city_id: Mapped[int] = mapped_column(Integer, nullable=False)
    state_id: Mapped[int] = mapped_column(Integer, nullable=False)
    country_id: Mapped[int] = mapped_column(Integer, nullable=False)
    
    order: Mapped["Order"] = relationship(back_populates="adress")
    
