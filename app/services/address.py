from typing import Optional

from ..repositories import AddressRepository
from ..entities import AddressEntity
from ..mappers import AddressMapper
from ..models import AddressModel

from ..models import db


class AddressService:
    """ Class focused in return data as Entity """

    def __init__(self):
        self.address_repository = AddressRepository(db)
        self.addres_mapper = AddressMapper

    def get_by_id(self, id: int) -> Optional[AddressEntity]:
        """ Get Address by id """
        address_model = self.address_repository.find_by_id(id)

        if address_model is None:
            return None

        return self.addres_mapper.create_entity(address_model)

    def get_by_name(self, name: str) -> Optional[AddressEntity]:
        """ Get Address by name """
        address_model = self.address_repository.find_by_name(name)

        if address_model is None:
            return None

        return self.addres_mapper.create_entity(address_model)

    def create_address(self, address: AddressModel) -> Optional[AddressEntity]:
        """ Create Address """
        address_created = self.address_repository.create_one(address)

        if address_created is None:
            return None

        return self.addres_mapper.create_entity(address)

    def update_address(
        self,
        id: int,
        param_address: AddressModel
    ) -> Optional[AddressEntity]:
        """ Update Address"""
        address = self.address_repository.update_one(
            id, param_address
        )

        if address is None:
            return None

        print(address)
        return "Address updated"
