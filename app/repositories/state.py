from typing import Optional
from dataclasses import dataclass
from flask_sqlalchemy import SQLAlchemy

from ..models import StateModel


@dataclass
class StateRepository:
    session_db: SQLAlchemy
    
    
    def find_by_id(self, id: int) -> Optional[StateModel]:
        # self.session_db.session
        ...
        
        
    def find_by_name(self, name: str) -> Optional[StateModel]: 
        # self.session_db.session
        ...