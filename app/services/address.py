from ..repositories import AddressRepository
from ..mappers import AddressMapper
from .base import BaseService


class AddressService(BaseService):
    def __init__(
        self,
        repository=AddressRepository(),
        mapper=AddressMapper()
    ) -> None:
        super().__init__(repository, mapper)
