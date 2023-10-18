from typing import Optional, Tuple

from flask_sqlalchemy import SQLAlchemy

from sqlalchemy import Result
from sqlalchemy import select, update

from ..models import AddressModel


class AddressRepository:
    """ Class Focused """

    def __init__(self, db: SQLAlchemy):
        self.db = db


    def find_by_id(self, id: int) -> Optional[AddressModel]:
        """ Find AddressModel by id """
        try:
            address = self.db.session.execute(
                select(AddressModel).filter_by(id=id)).scalar_one()
            return address

        except Exception as ex:
            print(ex)
            return None

    def find_by_name(self, name: str) -> Optional[AddressModel]:
        """ Find AddressModel by name """
        try:
            address = self.db.session.execute(
                select(AddressModel).filter_by(name=name)).scalar_one()
            return address

        except Exception as ex:
            print(ex)
            return None

    def find_all(self) -> Result[Tuple[Optional[AddressModel]]]:
        """ Find all AddressModel """
        try:
            addresses = self.db.session.execute(
                select(AddressModel).order_by(AddressModel.id))
            return addresses

        except Exception as ex:
            print(ex)
            return None

    def create_one(self, address: AddressModel):
        """ Create AddressModel """
        try:
            self.db.session.add(address)

            if address is None:
                self.db.session.rollback()
                return None

            self.db.session.commit()
            return address

        except Exception as ex:
            print(ex)
            return None
        
    def update_one(self, id: int, param_address: AddressModel):
        try:
            address = update(AddressModel).\
                where(AddressModel.id==id).\
                values(param_address)
                
            self.db.session.commit()
            print(f"address: {address}")
            return address

        except Exception as ex:
            print(ex)
            return None