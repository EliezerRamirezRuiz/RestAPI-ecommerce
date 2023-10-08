from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import (mapped_column, relationship)
from sqlalchemy import (Integer, String, ForeignKey)

from .db import db

if TYPE_CHECKING:
    from .adress import AdressModel


class OrderModel(db.Model):
    __tablename__ = "order"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    
    adress: Mapped["AdressModel"] = relationship(back_populates="order")