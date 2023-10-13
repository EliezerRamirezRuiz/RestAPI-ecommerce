from typing import Literal

from ..repositories import AddressRepository
from ..entities import AdressEntity
from ..mappers import AdressMapper
from ..models import AddressModel

from ..models import db


class AddressService:
    def __init__(self) -> None:
        self.address_repository:AddressRepository = AddressRepository(db)
    

    def address_by_id(self, id: int):
        address_model = AddressRepository.find_by_id(id)
        
        if isinstance(address_model, AddressModel):
            return address_model.to_dict()


    def create_address(self, address: AddressModel) -> None:
        try:
            self.address_repository.create(address)
            print("create")

        except: 
            print("a")
            return