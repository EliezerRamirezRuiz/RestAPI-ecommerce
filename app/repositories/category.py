from typing import Optional
from dataclasses import dataclass
from flask_sqlalchemy import SQLAlchemy

from ..models import CategoryModel


@dataclass
class CategoryRepository:
    session_db: SQLAlchemy
    
    
    def find_by_id(self, id: int) -> Optional[CategoryModel]:
        # self.session_db.session
        ...
        
        
    def find_by_name(self, name: str) -> Optional[CategoryModel]: 
        # self.session_db.session
        ...