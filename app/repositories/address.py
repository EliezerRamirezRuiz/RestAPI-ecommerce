from typing import Optional
from typing import List

from dataclasses import dataclass

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import select
 
from ..models import AddressModel


@dataclass
class AddressRepository:
    db: SQLAlchemy
    
    def find_by_id(self, id: int) -> Optional[AddressModel]:
        try:
            address = self.db.session.execute(select(AddressModel).filter_by(id=id)).scalar_one()
            return address

        except Exception as ex:
            print(ex)
            return None
        
        
    def find_by_name(self, name: str) -> Optional[AddressModel]: 
        try:
            address = self.db.session.execute(select(AddressModel).filter_by(id=id)).scalar_one()
            return address
            
        except Exception as ex:
            print(ex)
            return None
        
        
    def find_all(self) -> Optional[List[AddressModel]]:
        try:
            addresses = self.db.session.execute(select(AddressModel).order_by(AddressModel.id))
            return addresses

        except Exception as ex:
            print(ex)
            return None
        