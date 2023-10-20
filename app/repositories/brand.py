from typing import Optional
from dataclasses import dataclass
from flask_sqlalchemy import SQLAlchemy

from .base import BaseRepository

from ..models import BrandModel


@dataclass
class BrandRepository(BaseRepository):
    model = BrandModel
    
    