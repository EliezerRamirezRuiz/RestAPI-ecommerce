from typing import Optional
from dataclasses import dataclass
from flask_sqlalchemy import SQLAlchemy

from models import ProductModel


@dataclass
class ProductRepository:
    session_db: SQLAlchemy
    
    
    def find_by_id(self, id: int) -> Optional[ProductModel]:
        # self.session_db.session
        ...
        
        
    def find_by_name(self, name: str) -> Optional[ProductModel]: 
        # self.session_db.session
        ...