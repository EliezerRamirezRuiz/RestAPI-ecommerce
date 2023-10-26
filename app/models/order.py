from typing import TYPE_CHECKING

from dataclasses import dataclass

from sqlalchemy_serializer import SerializerMixin

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import (mapped_column, relationship)
from sqlalchemy import (Integer, String, ForeignKey)

from ..extensions import db


if TYPE_CHECKING:
    from .address import AddressModel


@dataclass
class OrderModel(db.Model, SerializerMixin):
    __tablename__ = "orders"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    
    # address: Mapped["AddressModel"] = relationship(back_populates="order")