from typing import TYPE_CHECKING

from sqlalchemy_serializer import SerializerMixin

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import (mapped_column, relationship)
from sqlalchemy import (Integer, String, ForeignKey)

from .database import db

if TYPE_CHECKING:
    from .address import AddressModel


class OrderModel(db.Model, SerializerMixin):
    __tablename__ = "orders"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    
    # address: Mapped["AddressModel"] = relationship(back_populates="order")