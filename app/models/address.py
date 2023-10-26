from typing import TYPE_CHECKING

from dataclasses import dataclass

from sqlalchemy_serializer import SerializerMixin

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import (mapped_column, relationship)
from sqlalchemy import (Integer, String, ForeignKey)

from ..extensions import db

if TYPE_CHECKING:
    from .order import OrderModel


@dataclass
class AddressModel(db.Model, SerializerMixin):
    __tablename__ = "addresses"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    number: Mapped[int] = mapped_column(Integer, nullable=False)
    city_id: Mapped[int] = mapped_column(Integer, nullable=False)
    state_id: Mapped[int] = mapped_column(Integer, nullable=False)
    country_id: Mapped[int] = mapped_column(Integer, nullable=False)

    # order_id: Mapped[int] = mapped_column(ForeignKey("orders.id"))
    # order: Mapped["OrderModel"] = relationship(back_populates="address")