from typing import Optional
from dataclasses import dataclass
from flask_sqlalchemy import SQLAlchemy

from ..models import AddressModel


@dataclass
class UserRepository:
    session_db: SQLAlchemy
    
    
    def find_by_id(self, id: int) -> Optional[AddressModel]:
        # self.session_db.session
        ...
        
        
    def find_by_name(self, name: str) -> Optional[AddressModel]: 
        # self.session_db.session
        ...