from typing import List
from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column, relationship
from sqlalchemy import Integer, String

from .database import db

if TYPE_CHECKING:
    from .state import StateModel


class CountryModel(db.Model):
    __tablename__ = "countries"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False, unique=True)

    state: Mapped[List["StateModel"]] = relationship()