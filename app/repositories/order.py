from typing import Optional
from dataclasses import dataclass
from flask_sqlalchemy import SQLAlchemy

from ..models import OrderModel


@dataclass
class OrderRepository:
    session_db: SQLAlchemy
    
    
    def find_by_id(self, id: int) -> Optional[OrderModel]:
        # self.session_db.session
        ...
        
        
    def find_by_name(self, name: str) -> Optional[OrderModel]: 
        # self.session_db.session
        ...