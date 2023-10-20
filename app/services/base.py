from typing import Optional

from dataclasses import dataclass

from ..mappers import AddressMapper


from ..variables import Entity, Model, Repository, Mapper


@dataclass
class AddressService:
    """ Class focused in return data as Entity """
    repository: Repository
    mapper = Mapper

    def get_by_id(
        self,
        id: int
    ) -> Optional[Entity]:
        """ Get Address by id """
        address_model = self.repository.find_by_id(id)

        if address_model is None:
            return None

        return self.mapper.create_entity(address_model)

    def get_by_name(
        self,
        name: str
    ) -> Optional[Entity]:
        """ Get Address by name """
        address_model = self.repository.find_by_name(name)

        if address_model is None:
            return None

        return self.mapper.create_entity(address_model)

    def create_address(
        self,
        model: Model
    ) -> Optional[Entity]:
        """ Create Address """
        model_created = self.repository.create_one(model)

        if model_created is None:
            return None

        return self.mapper.create_entity(model)

    def update_address(
        self,
        id: int,
        param_address: Model
    ) -> Optional[Entity]:
        """ Update Address"""
        address = self.repository.update_one(
            id, param_address
        )

        if address is None:
            return None

        print(address)
        return "Address updated"
