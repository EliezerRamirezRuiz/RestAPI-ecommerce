from datetime import datetime

from typing import List
from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import (mapped_column, relationship)

from sqlalchemy import Integer, String
from sqlalchemy import func

from .database import Base

if TYPE_CHECKING:
    from .order import OrderModel


class UserModel(Base):
    __tablename__ = "users"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String, nullable=False)
    email: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    create_date: Mapped[datetime] = mapped_column(insert_default=func.now())
    
    order: Mapped[List["OrderModel"]] = relationship()
    
    