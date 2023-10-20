from typing import List
from typing import TYPE_CHECKING

from dataclasses import dataclass

from sqlalchemy_serializer import SerializerMixin

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column, relationship
from sqlalchemy import Integer, String

from .database import db

if TYPE_CHECKING:
    from .product import ProductModel


@dataclass
class BrandModel(db.Model, SerializerMixin):
    __tablename__ = "brands"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    
    product: Mapped[List["ProductModel"]] = relationship()