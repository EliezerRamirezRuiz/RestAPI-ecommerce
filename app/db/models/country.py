from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import Integer, String

from db import db


class Country(db.Model):
    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String, nullable=False, unique=True)