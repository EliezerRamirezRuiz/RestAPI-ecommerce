from typing import Optional
from dataclasses import dataclass
from flask_sqlalchemy import SQLAlchemy

from ..models import BrandModel


@dataclass
class BrandRepository:
    db: SQLAlchemy
    
    
    def find_by_id(self, id: int) -> Optional[BrandModel]:
        # self.session_db.session
        ...
        
        
    def find_by_name(self, name: str) -> Optional[BrandModel]: 
        # self.session_db.session
        ...