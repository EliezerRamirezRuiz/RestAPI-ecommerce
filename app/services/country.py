from ..repositories import CountryRepository
from ..mappers import CountryMapper
from .base import BaseService


class CountryService(BaseService):
    def __init__(
        self, 
        repository=CountryRepository(), 
        mapper=CountryMapper()
        ) -> None:
        super().__init__(repository, mapper)