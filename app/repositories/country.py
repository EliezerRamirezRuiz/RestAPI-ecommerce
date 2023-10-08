from typing import Optional
from dataclasses import dataclass
from flask_sqlalchemy import SQLAlchemy

from models import CountryModel


@dataclass
class CountryRepository:
    session_db: SQLAlchemy
    
    
    def find_by_id(self, id: int) -> Optional[CountryModel]:
        # self.session_db.session
        ...
        
        
    def find_by_name(self, name: str) -> Optional[CountryModel]: 
        # self.session_db.session
        ...