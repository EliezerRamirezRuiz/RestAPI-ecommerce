from typing import List
from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column, relationship
from sqlalchemy import Integer, String

from .database import Base

if TYPE_CHECKING:
    from .product import ProductModel


class BrandModel(Base):
    __tablename__ = "brands"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    
    product: Mapped[List["ProductModel"]] = relationship()