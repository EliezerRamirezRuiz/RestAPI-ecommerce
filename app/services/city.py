from ..repositories import CityRepository
from ..mappers import CityMapper
from .base import BaseService


class CityService(BaseService):
    def __init__(
        self, 
        repository=CityRepository(), 
        mapper=CityMapper()
        ) -> None:
        super().__init__(repository, mapper)