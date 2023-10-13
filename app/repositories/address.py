from typing import List

from dataclasses import dataclass

from sqlalchemy.exc import NoResultFound
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import select
 
from ..models import AddressModel


@dataclass
class AddressRepository:
    db: SQLAlchemy
    
    def find_by_id(self, id: int):
        try:
            address = self.db.session.execute(select(AddressModel).filter_by(id=id)).scalar_one()
            if address is not None:
                return address

        except NoResultFound:
            print("exec")
            return "address not found, check the id and try again."
        
        
    def find_by_name(self, name: str) -> AddressModel | str: 
        try:
            address = self.db.session.execute(select(AddressModel).filter_by(name=name)).scalar_one()
            if address is not None:
                return address
            
        except NoResultFound:
            print("exec")
            return "address not found, check the name and try again."
        
        
    def find_all(self) -> List[AddressModel] | str:
        try:
            addresses = self.db.session.execute(select(AddressModel).order_by(AddressModel.id))
            if addresses is not None:
                return addresses

        except NoResultFound:
            print("exec")
            return "we couldn't find addresses"
        
    
    def create(self, address: AddressModel):
        try:
            self.db.session.add(address)
            self.db.session.commit()
            
        except Exception as ex:
            print(ex)
            